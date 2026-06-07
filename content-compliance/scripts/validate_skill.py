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
]


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
        "## 1. Basic Information",
        "## 2. Overall Conclusion",
        "## 3. Risk List",
        "## 4. Promotion-Specific Notes",
        "## 5. Pending Review Notes",
        "## 6. Disclaimer",
    ]
    missing = [section for section in required_sections if section not in report]
    if missing:
        fail(f"report template sections missing: {missing}")


def ensure_scoring_constants() -> None:
    scoring = read("scoring.md")
    required = ["15.75", "severity 3: +0.5", "severity 4: +0.75", "accumulation cap: 2"]
    missing = [item for item in required if item not in scoring]
    if missing:
        fail(f"scoring constants missing: {missing}")


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


def parse_declared_source_ids(sources: str) -> set[str]:
    source_ids = set()
    invalid_source_ids = []
    for line in sources.splitlines():
        stripped = line.strip()
        if not stripped.startswith("|"):
            continue
        cells = [cell.strip() for cell in stripped.strip("|").split("|")]
        if not cells or cells[0] in {"Source ID", "---"}:
            continue
        source_id = cells[0]
        if SOURCE_ID_RE.fullmatch(source_id):
            source_ids.add(source_id)
        elif source_id.startswith("source."):
            invalid_source_ids.append(source_id)
    if invalid_source_ids:
        fail(f"sources inventory has invalid source ids: {invalid_source_ids}")
    return source_ids


def ensure_sources_inventory() -> set[str]:
    sources = read("references/sources.md")
    missing_domains = [domain for domain in REQUIRED_OFFICIAL_DOMAINS if domain not in sources]
    if missing_domains:
        fail(f"sources inventory missing required official domains: {missing_domains}")
    declared_source_ids = parse_declared_source_ids(sources)
    if len(declared_source_ids) < MIN_DECLARED_SOURCE_IDS:
        fail(
            "sources inventory has too few declared source ids: "
            f"{len(declared_source_ids)} found, expected at least {MIN_DECLARED_SOURCE_IDS}"
        )
    return declared_source_ids


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


def ensure_rule_cards_have_valid_statuses() -> None:
    for rule_path, card in iter_rule_cards():
        status = re.search(r"^Status:[ \t]*([^\n]*)$", card, flags=re.M)
        if not status:
            fail(f"rule card missing Status in {rule_path}: {card[:120]}")
        status_value = status.group(1).strip()
        if status_value not in ALLOWED_STATUSES:
            fail(
                f"rule card has invalid Status in {rule_path}: "
                f"{status_value!r}; expected one of {sorted(ALLOWED_STATUSES)}"
            )


def ensure_examples_are_complete() -> None:
    for example_path in [
        "examples/douyin-topic-gate.md",
        "examples/douyin-draft-review.md",
        "examples/xiaohongshu-topic-gate.md",
        "examples/xiaohongshu-draft-review.md",
    ]:
        content = read(example_path)
        if "免责声明：本报告为 AI 辅助合规参考" not in content:
            fail(f"example missing disclaimer: {example_path}")
        if "Risk Score:" not in content:
            fail(f"example missing risk score: {example_path}")


def main() -> int:
    ensure_required_files()
    ensure_disclaimer()
    ensure_report_sections()
    ensure_scoring_constants()
    declared_source_ids = ensure_sources_inventory()
    ensure_rule_cards_have_source_ids()
    ensure_rule_card_sources_are_declared(declared_source_ids)
    ensure_rule_cards_have_valid_statuses()
    ensure_examples_are_complete()
    print("content-compliance skill validation passed")
    return 0


if __name__ == "__main__":
    sys.exit(main())
