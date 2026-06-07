import contextlib
import io
import importlib.util
from pathlib import Path
import re
import shutil
import subprocess
import sys
import tempfile
import textwrap
import unittest


ROOT = Path(__file__).resolve().parents[1]
PACKAGE = ROOT / "content-compliance"
SCORE_BREAKDOWN_FIELDS = [
    "severity",
    "confidence",
    "exposure",
    "scenario",
    "fix_difficulty",
    "accumulation",
]


REQUIRED_FILES = [
    "README.md",
    "SKILL.md",
    "rules/douyin.md",
    "rules/xiaohongshu.md",
    "scoring.md",
    "templates/report.md",
    "references/sources.md",
    "references/official-source-intake.md",
    "references/research/douyin-official-sources.md",
    "references/research/xiaohongshu-official-sources.md",
    "examples/douyin-topic-gate.md",
    "examples/douyin-draft-review.md",
    "examples/xiaohongshu-topic-gate.md",
    "examples/xiaohongshu-draft-review.md",
    "scripts/validate_skill.py",
]


def read_package_file(relative_path: str) -> str:
    return (PACKAGE / relative_path).read_text(encoding="utf-8")


def parse_rule_statuses(relative_paths: list[str]) -> dict[str, str]:
    statuses = {}
    for relative_path in relative_paths:
        current_rule = None
        for line in read_package_file(relative_path).splitlines():
            rule_match = re.match(r"Rule ID:\s*(\S+)\s*$", line)
            if rule_match:
                current_rule = rule_match.group(1)
                continue

            status_match = re.match(r"Status:\s*(\S+)\s*$", line)
            if status_match and current_rule:
                statuses[current_rule] = status_match.group(1)
                current_rule = None
    return statuses


def parse_source_review_statuses() -> dict[str, str]:
    statuses = {}
    for line in read_package_file("references/sources.md").splitlines():
        stripped = line.strip()
        if not stripped.startswith("|"):
            continue
        cells = [cell.strip() for cell in stripped.strip("|").split("|")]
        if not cells or cells[0] in {"Source ID", "---"}:
            continue
        if re.fullmatch(r"source\.[A-Za-z0-9_.-]+", cells[0]):
            statuses[cells[0]] = cells[-1]
    return statuses


def scored_rules_in_example(relative_path: Path) -> list[str]:
    rules = []
    pending_review_boundaries = ("- Pending Review Notes:", "- 待复核提示:")
    for line in relative_path.read_text(encoding="utf-8").splitlines():
        stripped_line = line.strip()
        if stripped_line in pending_review_boundaries:
            break

        rule_match = re.match(r"\s*-\s*Rule:\s*([A-Za-z0-9_.-]+)\s*$", line)
        if rule_match:
            rules.append(rule_match.group(1))
    return rules


def load_validator_module():
    validator_path = PACKAGE / "scripts/validate_skill.py"
    spec = importlib.util.spec_from_file_location("validate_skill", validator_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def write_rule_pack(
    root: Path,
    relative_path: str,
    official_sources: str,
    source_access_date: str = "2026-06-07",
) -> None:
    path = root / relative_path
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        textwrap.dedent(
            f"""\
            # Rule Pack

            ```text
            Rule ID: test.guidance
            Platform: Test
            Scope: ordinary
            Rule Name: Mentions source.fake outside the official source field
            Severity: 4
            Trigger Scenarios: This field mentions source.fake, but it is not source evidence.
            Official Sources: {official_sources}
            Source Access Date: {source_access_date}
            Status: needs_review
            ```
            """
        ),
        encoding="utf-8",
    )


class ContentComplianceSkillTest(unittest.TestCase):
    def test_required_package_files_exist(self):
        missing = [path for path in REQUIRED_FILES if not (PACKAGE / path).is_file()]
        self.assertEqual(missing, [])

    def test_validator_script_passes(self):
        result = subprocess.run(
            [sys.executable, str(PACKAGE / "scripts/validate_skill.py")],
            cwd=ROOT,
            text=True,
            capture_output=True,
            check=False,
        )
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)

    def test_skill_instructions_include_required_workflows(self):
        skill = read_package_file("SKILL.md")
        required_phrases = [
            "Topic Gate",
            "Draft Review",
            "rules/douyin.md",
            "rules/xiaohongshu.md",
            "templates/report.md",
            "mandatory disclaimer",
            "Only `Status: active`",
            "final score",
            "needs_review",
            "not in confirmed risks or final score",
            "这条风险只能作为待复核提示，因为当前规则卡处于 `needs_review`，官方来源覆盖范围或规则解释仍需人工复核。",
        ]
        missing = [phrase for phrase in required_phrases if phrase not in skill]
        self.assertEqual(missing, [])
        self.assertNotIn("这条风险只能作为待复核提示，因为当前规则卡尚未绑定足够官方来源。", skill)

    def test_scored_example_rules_are_active(self):
        statuses = parse_rule_statuses(["rules/douyin.md", "rules/xiaohongshu.md"])
        failures = []

        for example_path in (PACKAGE / "examples").glob("*.md"):
            for rule_id in scored_rules_in_example(example_path):
                status = statuses.get(rule_id)
                if status != "active":
                    failures.append(f"{example_path.name}: {rule_id} is {status or 'missing'}")

        self.assertEqual(failures, [])

    def test_active_rule_sources_are_active_in_inventory(self):
        source_statuses = parse_source_review_statuses()
        failures = []

        for relative_path in ["rules/douyin.md", "rules/xiaohongshu.md"]:
            content = read_package_file(relative_path)
            cards = re.findall(r"Rule ID: .+?(?=\n```|\nRule ID: |\Z)", content, flags=re.S)
            for card in cards:
                rule_id = re.search(r"^Rule ID:\s*(\S+)\s*$", card, flags=re.M).group(1)
                status = re.search(r"^Status:\s*(\S+)\s*$", card, flags=re.M).group(1)
                if status != "active":
                    continue

                official_sources = re.search(
                    r"^Official Sources:\s*([^\n]*)$", card, flags=re.M
                ).group(1)
                for source_id in [source.strip() for source in official_sources.split(",")]:
                    if source_statuses.get(source_id) != "active":
                        failures.append(
                            f"{rule_id}: {source_id} is "
                            f"{source_statuses.get(source_id, 'missing')}"
                        )

        self.assertEqual(failures, [])

    def test_douyin_active_qualification_rule_excludes_dou_plus_scope(self):
        rules = read_package_file("rules/douyin.md")
        rule_block = re.search(
            r"Rule ID: douyin\.advertising\.qualification_or_industry_restriction"
            r".+?Status: active",
            rules,
            flags=re.S,
        )
        self.assertIsNotNone(rule_block)
        self.assertIn("Scope: oceanengine_ad_review", rule_block.group(0))
        self.assertNotIn("dou_plus", rule_block.group(0))

    def test_xiaohongshu_pending_guidance_example_is_not_scored(self):
        example_path = PACKAGE / "examples" / "xiaohongshu-draft-review.md"
        content = example_path.read_text(encoding="utf-8")
        scored_section = content.split("- 待复核提示:", 1)[0]

        self.assertIn("Matched Risks: none confirmed under `Status: active` rules.", content)
        self.assertIn("它不支持本示例的 `Risk Score`", content)
        self.assertNotIn("Rule: xiaohongshu.guidance.external_contact_or_download", scored_section)
        self.assertNotIn("Rule: xiaohongshu.promotion.shutiao_review_stricter_context", scored_section)

    def test_xiaohongshu_shutiao_context_alone_is_not_scored_signal(self):
        rules = read_package_file("rules/xiaohongshu.md")
        rule_block = re.search(
            r"Rule ID: xiaohongshu\.promotion\.shutiao_review_stricter_context"
            r".+?Status: active",
            rules,
            flags=re.S,
        )
        self.assertIsNotNone(rule_block)
        block = rule_block.group(0)

        self.assertNotIn('"plan to use Shutiao"', block)
        self.assertNotIn("paid promotion objective", block)
        self.assertIn("Planning to use Shutiao alone is context for review", block)

    def test_sources_file_contains_required_official_domains(self):
        sources = read_package_file("references/sources.md")
        required_domains = [
            "95152.douyin.com",
            "support.oceanengine.com",
            "pgy.xiaohongshu.com",
            "e.xiaohongshu.com",
            "ad.xiaohongshu.com",
        ]
        missing = [domain for domain in required_domains if domain not in sources]
        self.assertEqual(missing, [])

    def test_report_template_includes_required_sections(self):
        report = read_package_file("templates/report.md")
        required_sections = [
            "## 1. Basic Information",
            "## 2. Overall Conclusion",
            "## 3. Risk List",
            "## 4. Promotion-Specific Notes",
            "## 5. Pending Review Notes",
            "## 6. Disclaimer",
        ]
        missing = [section for section in required_sections if section not in report]
        self.assertEqual(missing, [])
        self.assertIn(
            "These notes are not part of the Total Risk Score unless the same evidence independently matches a `Status: active` rule.",
            report,
        )

    def test_examples_include_disclaimer_and_risk_score(self):
        for relative_path in [
            "examples/douyin-topic-gate.md",
            "examples/douyin-draft-review.md",
            "examples/xiaohongshu-topic-gate.md",
            "examples/xiaohongshu-draft-review.md",
        ]:
            content = read_package_file(relative_path)
            self.assertIn("免责声明：本报告为 AI 辅助合规参考", content)
            self.assertIn("Risk Score:", content)

    def test_examples_include_score_breakdown_fields(self):
        for relative_path in [
            "examples/douyin-topic-gate.md",
            "examples/douyin-draft-review.md",
            "examples/xiaohongshu-topic-gate.md",
            "examples/xiaohongshu-draft-review.md",
        ]:
            content = read_package_file(relative_path)
            self.assertIn("Score Breakdown:", content)
            for field in SCORE_BREAKDOWN_FIELDS:
                self.assertIn(f"- {field}:", content)

    def test_active_rules_include_traceability_without_evidence_limitations(self):
        for relative_path in ["rules/douyin.md", "rules/xiaohongshu.md"]:
            content = read_package_file(relative_path)
            active_blocks = [block for block in content.split("Rule ID: ")[1:] if "Status: active" in block]
            for block in active_blocks:
                self.assertIn("Official Sources: source.", block)
                self.assertIn("Source Access Date:", block)
                self.assertNotIn("Evidence limitation:", block)

    def test_validator_requires_source_id_in_official_sources_field(self):
        validator = load_validator_module()

        for official_sources in [
            "",
            "not an official source id",
            "source.",
            "notsource.foo",
            "prefix source. suffix",
            "source.valid, random blog",
        ]:
            with self.subTest(official_sources=official_sources):
                with tempfile.TemporaryDirectory() as temporary_directory:
                    temporary_root = Path(temporary_directory)
                    write_rule_pack(temporary_root, "rules/douyin.md", official_sources)
                    write_rule_pack(temporary_root, "rules/xiaohongshu.md", "source.valid")

                    original_root = validator.ROOT
                    validator.ROOT = temporary_root
                    try:
                        with contextlib.redirect_stdout(io.StringIO()):
                            with self.assertRaises(SystemExit):
                                validator.ensure_rule_cards_have_source_ids()
                    finally:
                        validator.ROOT = original_root

    def test_validator_does_not_read_source_id_from_next_field(self):
        validator = load_validator_module()

        with tempfile.TemporaryDirectory() as temporary_directory:
            temporary_root = Path(temporary_directory)
            write_rule_pack(
                temporary_root,
                "rules/douyin.md",
                "",
                source_access_date="source.valid",
            )
            write_rule_pack(temporary_root, "rules/xiaohongshu.md", "source.valid")

            original_root = validator.ROOT
            validator.ROOT = temporary_root
            try:
                with contextlib.redirect_stdout(io.StringIO()):
                    with self.assertRaises(SystemExit):
                        validator.ensure_rule_cards_have_source_ids()
            finally:
                validator.ROOT = original_root

    def test_validator_rejects_undeclared_source_id(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            temp_root = Path(temp_dir)
            copied_package = temp_root / "content-compliance"
            shutil.copytree(PACKAGE, copied_package)

            rule_file = copied_package / "rules" / "douyin.md"
            original = rule_file.read_text(encoding="utf-8")
            rule_file.write_text(
                original
                + """

Rule ID: douyin.test.undeclared_source
Platform: Douyin
Scope: ordinary_post
Rule Name: Test undeclared source
Severity: 1
Trigger Scenarios: test only
High-Risk Signals: test only
Lower-Risk Alternatives: test only
Review Questions: test only
Evidence Extraction: test only
Official Sources: source.not_declared
Source Access Date: 2026-06-07
Status: active
""",
                encoding="utf-8",
            )

            result = subprocess.run(
                [sys.executable, str(copied_package / "scripts" / "validate_skill.py")],
                cwd=temp_root,
                text=True,
                capture_output=True,
                check=False,
            )
            output = result.stdout + result.stderr
            self.assertNotEqual(result.returncode, 0)
            self.assertIn("undeclared sources", output)

    def test_validator_rejects_active_rule_with_non_active_source(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            temp_root = Path(temp_dir)
            copied_package = temp_root / "content-compliance"
            shutil.copytree(PACKAGE, copied_package)

            rule_file = copied_package / "rules" / "douyin.md"
            original = rule_file.read_text(encoding="utf-8")
            rule_file.write_text(
                original
                + """

Rule ID: douyin.test.non_active_source
Platform: Douyin
Scope: ordinary_post
Rule Name: Test non-active source
Severity: 1
Trigger Scenarios: test only
High-Risk Signals: test only
Lower-Risk Alternatives: test only
Review Questions: test only
Evidence Extraction: test only
Official Sources: source.douyin.safety_center
Source Access Date: 2026-06-07
Status: active
""",
                encoding="utf-8",
            )

            result = subprocess.run(
                [sys.executable, str(copied_package / "scripts" / "validate_skill.py")],
                cwd=temp_root,
                text=True,
                capture_output=True,
                check=False,
            )
            output = result.stdout + result.stderr
            self.assertNotEqual(result.returncode, 0)
            self.assertIn("non-active sources", output)

    def test_validator_reads_source_status_from_last_table_cell(self):
        validator = load_validator_module()
        source_statuses = validator.parse_source_statuses(
            textwrap.dedent(
                """\
                | Source ID | Platform | Scope | Official URL | Page Title | Access Date | Page Updated Date | Retrieval Status | Review Status |
                | --- | --- | --- | --- | --- | --- | --- | --- | --- |
                | source.valid | Xiaohongshu | commercial_site | https://example.com | 商业产品 \\| 小红书商业化官网 | 2026-06-07 | not visible | dynamic_reachable | active |
                """
            )
        )
        self.assertEqual(source_statuses["source.valid"], "active")

    def test_validator_rejects_research_inventory_status_mismatch(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            temp_root = Path(temp_dir)
            copied_package = temp_root / "content-compliance"
            shutil.copytree(PACKAGE, copied_package)

            research_file = (
                copied_package
                / "references"
                / "research"
                / "douyin-official-sources.md"
            )
            original = research_file.read_text(encoding="utf-8")
            active_status_block = (
                "## source.oceanengine.ad_management\n\n"
                "- Official URL: https://support.oceanengine.com/support/content/130539\n"
                "- Page Title: 巨量引擎-广告投放管理规范\n"
                "- Access Date: 2026-06-07\n"
                "- Page Updated Date: 2022-12-08 20:31:19\n"
                "- Retrieval Status: dynamic_reachable\n"
                "- Review Status: active"
            )
            self.assertIn(active_status_block, original)
            research_file.write_text(
                original.replace(
                    active_status_block,
                    "## source.oceanengine.ad_management\n\n"
                    "- Official URL: https://support.oceanengine.com/support/content/130539\n"
                    "- Page Title: 巨量引擎-广告投放管理规范\n"
                    "- Access Date: 2026-06-07\n"
                    "- Page Updated Date: 2022-12-08 20:31:19\n"
                    "- Retrieval Status: dynamic_reachable\n"
                    "- Review Status: needs_review",
                    1,
                ),
                encoding="utf-8",
            )

            result = subprocess.run(
                [sys.executable, str(copied_package / "scripts" / "validate_skill.py")],
                cwd=temp_root,
                text=True,
                capture_output=True,
                check=False,
            )
            output = result.stdout + result.stderr
            self.assertNotEqual(result.returncode, 0)
            self.assertIn("research source status mismatch", output)

    def test_validator_accepts_declared_source_id_token_format(self):
        validator = load_validator_module()

        with tempfile.TemporaryDirectory() as temporary_directory:
            temporary_root = Path(temporary_directory)
            write_rule_pack(temporary_root, "rules/douyin.md", "source.valid_id-1")
            write_rule_pack(temporary_root, "rules/xiaohongshu.md", "source.valid.id_2")

            original_root = validator.ROOT
            validator.ROOT = temporary_root
            try:
                validator.ensure_rule_cards_have_source_ids()
            finally:
                validator.ROOT = original_root


if __name__ == "__main__":
    unittest.main()
