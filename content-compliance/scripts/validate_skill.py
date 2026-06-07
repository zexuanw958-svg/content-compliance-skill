from pathlib import Path
import re
import sys


ROOT = Path(__file__).resolve().parents[1]
SOURCE_ID_RE = re.compile(r"source\.[A-Za-z0-9_.-]+")


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


def ensure_scoring_constants() -> None:
    scoring = read("scoring.md")
    required = ["15.75", "severity 3: +0.5", "severity 4: +0.75", "accumulation cap: 2"]
    missing = [item for item in required if item not in scoring]
    if missing:
        fail(f"scoring constants missing: {missing}")


def ensure_rule_cards_have_source_ids() -> None:
    for rule_path in ["rules/douyin.md", "rules/xiaohongshu.md"]:
        content = read(rule_path)
        cards = re.findall(r"Rule ID: .+?(?=\n```|\nRule ID: |\Z)", content, flags=re.S)
        if not cards:
            fail(f"no rule cards found in {rule_path}")
        for card in cards:
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


def main() -> int:
    ensure_required_files()
    ensure_disclaimer()
    ensure_scoring_constants()
    ensure_rule_cards_have_source_ids()
    print("content-compliance skill validation passed")
    return 0


if __name__ == "__main__":
    sys.exit(main())
