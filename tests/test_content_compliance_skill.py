import contextlib
import io
import importlib.util
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import textwrap
import unittest


ROOT = Path(__file__).resolve().parents[1]
PACKAGE = ROOT / "content-compliance"


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

    def test_sources_file_contains_required_official_domains(self):
        sources = read_package_file("references/sources.md")
        required_domains = [
            "95152.douyin.com",
            "support.oceanengine.com",
            "pgy.xiaohongshu.com",
            "e.xiaohongshu.com",
        ]
        missing = [domain for domain in required_domains if domain not in sources]
        self.assertEqual(missing, [])

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
