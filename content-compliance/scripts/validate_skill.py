from pathlib import Path
import re
import sys


ROOT = Path(__file__).resolve().parents[1]
SOURCE_ID_RE = re.compile(r"source\.[A-Za-z0-9_.-]+")
ALLOWED_STATUSES = {"active", "needs_review", "deprecated"}
MIN_DECLARED_SOURCE_IDS = 6
REQUIRED_OFFICIAL_DOMAINS = [
    "95152.douyin.com",
    "support.oceanengine.com",
    "pgy.xiaohongshu.com",
    "e.xiaohongshu.com",
    "ad.xiaohongshu.com",
]
REQUIRED_SCORE_BREAKDOWN_FACTORS = [
    "严重度 severity",
    "置信度 confidence",
    "暴露范围 exposure",
    "场景系数 scenario",
    "修改难度 fix_difficulty",
    "风险累积 accumulation",
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
    "references/rule-refresh.md",
    "references/research/douyin-official-sources.md",
    "references/research/xiaohongshu-official-sources.md",
    "commands/检测.md",
    "commands/content-compliance.md",
    "examples/douyin-topic-gate.md",
    "examples/douyin-draft-review.md",
    "examples/xiaohongshu-topic-gate.md",
    "examples/xiaohongshu-draft-review.md",
]

RESEARCH_FILES = [
    "references/research/douyin-official-sources.md",
    "references/research/xiaohongshu-official-sources.md",
]

PENDING_REVIEW_BOUNDARIES = {"- 待复核提示:", "- 待复核提示："}


DISCLAIMER = (
    "本报告为 AI 辅助合规参考，依据公开可见的平台规则、整理后的规则卡片以及用户提供的材料生成，"
    "不代表抖音、巨量引擎、小红书、蒲公英、聚光、薯条或任何相关平台的官方审核意见。"
)


def read(relative_path: str) -> str:
    return (ROOT / relative_path).read_text(encoding="utf-8")


def fail(message: str) -> None:
    print(f"FAIL: {message}")
    raise SystemExit(1)


def ensure_required_files() -> None:
    missing = [path for path in REQUIRED_FILES if not (ROOT / path).is_file()]
    if missing:
        fail(f"missing required files: {missing}")


def ensure_disclaimer() -> None:
    report = read("templates/report.md")
    if DISCLAIMER not in report:
        fail("mandatory disclaimer is missing from report template")


def ensure_report_sections() -> None:
    report = read("templates/report.md")
    required_sections = [
        "## 1. 基本信息",
        "## 2. 总体结论",
        "## 3. 分项安全诊断仪表盘",
        "## 4. 最弱风险点",
        "## 5. 风险清单",
        "## 6. 投放专项提醒",
        "## 7. 待复核提示",
        "## 8. 免责声明",
    ]
    missing = [section for section in required_sections if section not in report]
    if missing:
        fail(f"report template sections missing: {missing}")


def ensure_report_score_breakdown() -> None:
    report = read("templates/report.md")
    missing = [factor for factor in REQUIRED_SCORE_BREAKDOWN_FACTORS if factor not in report]
    if "评分拆解：" not in report or missing:
        fail(f"report template score breakdown missing fields: {missing}")


def ensure_report_visual_fields() -> None:
    report = read("templates/report.md")
    required = [
        "风险条",
        "分项 | 安全诊断分 | 可视化条",
        "分项安全诊断分",
        "确认风险状态",
    ]
    missing = [item for item in required if item not in report]
    if missing:
        fail(f"report template visual fields missing: {missing}")


def ensure_scoring_constants() -> None:
    scoring = read("scoring.md")
    required = [
        "15.75",
        "severity 3: +0.5",
        "severity 4: +0.75",
        "accumulation cap: 2",
        "风险条必须固定 10 格。",
        "风险条：5/10 🟨🟨🟨🟨🟨⬜⬜⬜⬜⬜",
        "风险条：9/10 🟥🟥🟥🟥🟥🟥🟥🟥🟥⬜",
        "不要同时输出最终风险条和最终安全条。",
        "分项安全诊断仪表盘",
        "最弱风险点",
    ]
    missing = [item for item in required if item not in scoring]
    if missing:
        fail(f"scoring constants missing: {missing}")
    forbidden = [
        "Overall Safety Score: 11 - Total Risk Score",
        "Safety Bar: fill cells equal to Overall Safety Score",
        "Risk Bar fixed scale",
    ]
    present = [item for item in forbidden if item in scoring]
    if present:
        fail(f"obsolete final-score visual fields still present: {present}")


def ensure_user_visible_output_is_chinese() -> None:
    user_output_paths = [
        "templates/report.md",
        "scoring.md",
        "examples/douyin-topic-gate.md",
        "examples/douyin-draft-review.md",
        "examples/xiaohongshu-topic-gate.md",
        "examples/xiaohongshu-draft-review.md",
    ]
    forbidden_labels = [
        "Total Risk Score:",
        "Risk Bar:",
        "Layer Safety Dashboard",
        "Weakest Areas:",
        "Score Breakdown:",
        "Platform:",
        "Phase:",
        "Recommendation:",
        "Matched Risks:",
        "Official Source:",
        "Safer Revision:",
        "Disclaimer",
    ]
    findings = []
    for path in user_output_paths:
        content = read(path)
        for label in forbidden_labels:
            if label in content:
                findings.append(f"{path}: {label}")
    if findings:
        fail(f"user-visible output still has English report labels: {findings}")


def ensure_official_source_messaging() -> None:
    root_readme_path = ROOT.parent / "README.md"
    root_readme = root_readme_path.read_text(encoding="utf-8") if root_readme_path.exists() else ""
    package_readme = read("README.md")
    intake = read("references/official-source-intake.md")
    refresh = read("references/rule-refresh.md")

    required_public_phrases = [
        "官方来源优先",
        "Status: needs_review",
        "不是自动实时同步所有平台规则",
        "最终仍以平台官方审核",
        "references/rule-refresh.md",
    ]
    public_blob = "\n".join([root_readme, package_readme])
    missing = [phrase for phrase in required_public_phrases if phrase not in public_blob]
    if missing:
        fail(f"official-source public messaging missing: {missing}")

    required_refresh_phrases = [
        "official-source-first",
        "does not guarantee complete coverage",
        "does not automatically update rules in real time",
        "Before every public tutorial, launch post, or video demo.",
        "Avoid this phrasing",
    ]
    missing_refresh = [
        phrase
        for phrase in required_refresh_phrases
        if phrase not in "\n".join([intake, refresh])
    ]
    if missing_refresh:
        fail(f"official-source refresh policy missing: {missing_refresh}")

    forbidden_public_claims = [
        "抓完所有官方规则",
        "全部官方规则",
        "所有官方规则全部",
        "自动实时同步所有平台规则。",
    ]
    present = [phrase for phrase in forbidden_public_claims if phrase in public_blob]
    if present:
        fail(f"overclaiming public messaging present: {present}")


def iter_rule_cards():
    for rule_path in ["rules/douyin.md", "rules/xiaohongshu.md"]:
        content = read(rule_path)
        cards = re.findall(r"Rule ID: .+?(?=\n```|\nRule ID: |\Z)", content, flags=re.S)
        if not cards:
            fail(f"no rule cards found in {rule_path}")
        for card in cards:
            yield rule_path, card


def extract_rule_source_ids(rule_path: str, card: str) -> list[str]:
    official_sources = re.search(r"^Official Sources:[ \t]*([^\n]*)$", card, flags=re.M)
    if not official_sources:
        fail(f"rule card missing Official Sources in {rule_path}: {card[:120]}")
    official_source_value = official_sources.group(1).strip()
    if not official_source_value:
        fail(f"rule card has empty Official Sources in {rule_path}: {card[:120]}")
    source_ids = [source_id.strip() for source_id in official_source_value.split(",")]
    invalid_source_ids = [source_id for source_id in source_ids if not SOURCE_ID_RE.fullmatch(source_id)]
    if invalid_source_ids:
        fail(
            f"rule card Official Sources has invalid source ids in {rule_path}: "
            f"{invalid_source_ids}"
        )
    return source_ids


def parse_source_statuses(sources: str) -> dict[str, str]:
    source_statuses = {}
    invalid_source_ids = []
    invalid_statuses = {}
    for line in sources.splitlines():
        stripped = line.strip()
        if not stripped.startswith("|"):
            continue
        # Source titles may contain escaped pipes, so only the first and last
        # cells are semantically important for source ID and Review Status.
        cells = [cell.strip() for cell in stripped.strip("|").split("|")]
        if not cells or cells[0] in {"Source ID", "---"}:
            continue
        source_id = cells[0]
        review_status = cells[-1]
        if SOURCE_ID_RE.fullmatch(source_id):
            source_statuses[source_id] = review_status
            if review_status not in ALLOWED_STATUSES:
                invalid_statuses[source_id] = review_status
        elif source_id.startswith("source."):
            invalid_source_ids.append(source_id)
    if invalid_source_ids:
        fail(f"sources inventory has invalid source ids: {invalid_source_ids}")
    if invalid_statuses:
        fail(f"sources inventory has invalid Review Status values: {invalid_statuses}")
    return source_statuses


def parse_declared_source_ids(sources: str) -> set[str]:
    return set(parse_source_statuses(sources))


def parse_research_source_statuses() -> dict[str, tuple[str, str]]:
    research_statuses = {}
    invalid_source_ids = []
    invalid_statuses = {}
    for research_path in RESEARCH_FILES:
        current_source_id = None
        for line_number, line in enumerate(read(research_path).splitlines(), start=1):
            heading = re.match(r"^## (source\.[A-Za-z0-9_.-]+)\s*$", line)
            if heading:
                current_source_id = heading.group(1)
                if not SOURCE_ID_RE.fullmatch(current_source_id):
                    invalid_source_ids.append(current_source_id)
                continue

            status = re.match(r"^- Review Status:\s*(\S+)\s*$", line)
            if status and current_source_id:
                status_value = status.group(1)
                research_statuses[current_source_id] = (
                    status_value,
                    f"{research_path}:{line_number}",
                )
                if status_value not in ALLOWED_STATUSES:
                    invalid_statuses[current_source_id] = status_value
    if invalid_source_ids:
        fail(f"research logs have invalid source ids: {invalid_source_ids}")
    if invalid_statuses:
        fail(f"research logs have invalid Review Status values: {invalid_statuses}")
    return research_statuses


def ensure_sources_inventory() -> dict[str, str]:
    sources = read("references/sources.md")
    missing_domains = [domain for domain in REQUIRED_OFFICIAL_DOMAINS if domain not in sources]
    if missing_domains:
        fail(f"sources inventory missing required official domains: {missing_domains}")
    source_statuses = parse_source_statuses(sources)
    declared_source_ids = set(source_statuses)
    if len(declared_source_ids) < MIN_DECLARED_SOURCE_IDS:
        fail(
            "sources inventory has too few declared source ids: "
            f"{len(declared_source_ids)} found, expected at least {MIN_DECLARED_SOURCE_IDS}"
        )
    return source_statuses


def ensure_rule_cards_have_source_ids() -> None:
    for rule_path, card in iter_rule_cards():
        extract_rule_source_ids(rule_path, card)


def ensure_rule_card_sources_are_declared(declared_source_ids: set[str]) -> None:
    for rule_path, card in iter_rule_cards():
        source_ids = extract_rule_source_ids(rule_path, card)
        undeclared_source_ids = [
            source_id for source_id in source_ids if source_id not in declared_source_ids
        ]
        if undeclared_source_ids:
            fail(
                f"rule card Official Sources has undeclared sources in {rule_path}: "
                f"{undeclared_source_ids}"
            )


def extract_rule_status(rule_path: str, card: str) -> str:
    status = re.search(r"^Status:[ \t]*([^\n]*)$", card, flags=re.M)
    if not status:
        fail(f"rule card missing Status in {rule_path}: {card[:120]}")
    status_value = status.group(1).strip()
    if status_value not in ALLOWED_STATUSES:
        fail(
            f"rule card has invalid Status in {rule_path}: "
            f"{status_value!r}; expected one of {sorted(ALLOWED_STATUSES)}"
        )
    return status_value


def ensure_rule_cards_have_valid_statuses() -> None:
    for rule_path, card in iter_rule_cards():
        extract_rule_status(rule_path, card)


def ensure_active_rule_card_sources_are_active(source_statuses: dict[str, str]) -> None:
    for rule_path, card in iter_rule_cards():
        if extract_rule_status(rule_path, card) != "active":
            continue
        inactive_source_ids = [
            f"{source_id} ({source_statuses.get(source_id, 'missing')})"
            for source_id in extract_rule_source_ids(rule_path, card)
            if source_statuses.get(source_id) != "active"
        ]
        if inactive_source_ids:
            fail(
                f"active rule card cites non-active sources in {rule_path}: "
                f"{inactive_source_ids}"
            )


def ensure_research_statuses_match_inventory(source_statuses: dict[str, str]) -> None:
    research_statuses = parse_research_source_statuses()
    mismatches = []
    for source_id, (research_status, location) in research_statuses.items():
        inventory_status = source_statuses.get(source_id)
        if inventory_status is None:
            mismatches.append(f"{source_id} missing from inventory at {location}")
        elif inventory_status != research_status:
            mismatches.append(
                f"{source_id}: inventory={inventory_status}, "
                f"research={research_status} at {location}"
            )
    if mismatches:
        fail(f"research source status mismatch: {mismatches}")


def iter_scored_example_rule_blocks(content: str):
    current_rule_id = None
    current_block = []
    for line in content.splitlines():
        stripped = line.strip()
        if stripped in PENDING_REVIEW_BOUNDARIES:
            break

        rule = re.match(r"\s*-\s*(?:Rule|规则)[：:]\s*([A-Za-z0-9_.-]+)\s*$", line)
        if rule:
            if current_rule_id:
                yield current_rule_id, "\n".join(current_block)
            current_rule_id = rule.group(1)
            current_block = [line]
            continue

        if current_rule_id:
            current_block.append(line)

    if current_rule_id:
        yield current_rule_id, "\n".join(current_block)


def ensure_examples_are_complete(declared_source_ids: set[str]) -> None:
    for example_path in [
        "examples/douyin-topic-gate.md",
        "examples/douyin-draft-review.md",
        "examples/xiaohongshu-topic-gate.md",
        "examples/xiaohongshu-draft-review.md",
    ]:
        content = read(example_path)
        if "免责声明：本报告为 AI 辅助合规参考" not in content:
            fail(f"example missing disclaimer: {example_path}")
        if "总风险分：" not in content:
            fail(f"example missing risk score: {example_path}")
        missing_visual_fields = [
            field
            for field in [
                "风险条：",
                "分项安全诊断仪表盘：",
                "最弱风险点：",
            ]
            if field not in content
        ]
        if missing_visual_fields:
            fail(f"example visual fields missing in {example_path}: {missing_visual_fields}")
        missing_score_breakdown_factors = [
            factor for factor in REQUIRED_SCORE_BREAKDOWN_FACTORS if factor not in content
        ]
        if "评分拆解：" not in content or missing_score_breakdown_factors:
            fail(
                f"example score breakdown missing fields in {example_path}: "
                f"{missing_score_breakdown_factors}"
            )
        for rule_id, rule_block in iter_scored_example_rule_blocks(content):
            official_source = re.search(
                r"^\s*-\s*(?:Official Source|官方来源)[：:]\s*([^\n]*)$",
                rule_block,
                flags=re.M,
            )
            if not official_source:
                fail(f"example scored rule missing official source: {example_path} {rule_id}")
            source_ids = [source_id.strip() for source_id in official_source.group(1).split(",")]
            invalid_source_ids = [
                source_id for source_id in source_ids if not SOURCE_ID_RE.fullmatch(source_id)
            ]
            undeclared_source_ids = [
                source_id for source_id in source_ids if source_id not in declared_source_ids
            ]
            if invalid_source_ids:
                fail(
                    f"example scored rule has invalid official sources: "
                    f"{example_path} {rule_id} {invalid_source_ids}"
                )
            if undeclared_source_ids:
                fail(
                    f"example scored rule has undeclared official sources: "
                    f"{example_path} {rule_id} {undeclared_source_ids}"
                )


def main() -> int:
    ensure_required_files()
    ensure_disclaimer()
    ensure_report_sections()
    ensure_report_score_breakdown()
    ensure_report_visual_fields()
    ensure_scoring_constants()
    ensure_user_visible_output_is_chinese()
    ensure_official_source_messaging()
    source_statuses = ensure_sources_inventory()
    declared_source_ids = set(source_statuses)
    ensure_rule_cards_have_source_ids()
    ensure_rule_card_sources_are_declared(declared_source_ids)
    ensure_rule_cards_have_valid_statuses()
    ensure_active_rule_card_sources_are_active(source_statuses)
    ensure_research_statuses_match_inventory(source_statuses)
    ensure_examples_are_complete(declared_source_ids)
    print("content-compliance skill validation passed")
    return 0


if __name__ == "__main__":
    sys.exit(main())
