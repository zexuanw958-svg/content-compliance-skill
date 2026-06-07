# Content Compliance Skill Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build a portable Codex / Claude Code skill that reviews Douyin and Xiaohongshu self-media content against official-source-backed compliance rules.

**Architecture:** The skill is a Markdown-first package under `content-compliance/`. `SKILL.md` routes the user's platform and production phase, platform rule packs store structured rule cards, `scoring.md` defines the 1-10 scoring system, `templates/report.md` defines the required report shape, and `references/` records official source intake. A Python validation script enforces source traceability, disclaimer presence, scoring constants, and example coverage.

**Tech Stack:** Markdown skill files, Python 3 standard library validation, shell commands, official web research through the web-access workflow when collecting rules.

---

## File Structure

Create this package structure:

```text
content-compliance/
  SKILL.md
  README.md
  rules/
    douyin.md
    xiaohongshu.md
  scoring.md
  templates/
    report.md
  references/
    official-source-intake.md
    sources.md
    research/
      douyin-official-sources.md
      xiaohongshu-official-sources.md
  examples/
    douyin-topic-gate.md
    douyin-draft-review.md
    xiaohongshu-topic-gate.md
    xiaohongshu-draft-review.md
  scripts/
    validate_skill.py
```

Create validation tests under:

```text
tests/
  test_content_compliance_skill.py
```

Responsibilities:

- `content-compliance/SKILL.md`: Runtime workflow for asking missing platform / phase context, loading the right rule pack, reviewing materials, scoring risk, and producing reports.
- `content-compliance/rules/*.md`: Platform rule cards with official source IDs. Active rules must cite official source IDs from `references/sources.md`.
- `content-compliance/scoring.md`: The risk formula, constants, accumulation rules, score bands, and explanation format.
- `content-compliance/templates/report.md`: Required report template and mandatory disclaimer.
- `content-compliance/references/sources.md`: Canonical official source inventory.
- `content-compliance/references/official-source-intake.md`: How to research, capture, summarize, and publish official rules safely.
- `content-compliance/references/research/*.md`: Human-readable research logs for official pages visited and rule families found.
- `content-compliance/examples/*.md`: Example inputs and example reports used as regression fixtures.
- `content-compliance/scripts/validate_skill.py`: Local quality gate.
- `tests/test_content_compliance_skill.py`: Unit tests that call the validator and inspect the package.

## Task 1: Add Package Skeleton and Baseline Tests

**Files:**
- Create: `tests/test_content_compliance_skill.py`
- Create: `content-compliance/README.md`
- Create: `content-compliance/SKILL.md`
- Create: `content-compliance/rules/douyin.md`
- Create: `content-compliance/rules/xiaohongshu.md`
- Create: `content-compliance/scoring.md`
- Create: `content-compliance/templates/report.md`
- Create: `content-compliance/references/sources.md`
- Create: `content-compliance/references/official-source-intake.md`
- Create: `content-compliance/references/research/douyin-official-sources.md`
- Create: `content-compliance/references/research/xiaohongshu-official-sources.md`
- Create: `content-compliance/examples/douyin-topic-gate.md`
- Create: `content-compliance/examples/douyin-draft-review.md`
- Create: `content-compliance/examples/xiaohongshu-topic-gate.md`
- Create: `content-compliance/examples/xiaohongshu-draft-review.md`
- Create: `content-compliance/scripts/validate_skill.py`

- [ ] **Step 1: Write the failing package-structure test**

Create `tests/test_content_compliance_skill.py`:

```python
from pathlib import Path
import subprocess
import sys
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


if __name__ == "__main__":
    unittest.main()
```

- [ ] **Step 2: Run the test to verify it fails**

Run:

```bash
python3 -m unittest tests/test_content_compliance_skill.py -v
```

Expected: FAIL because `content-compliance/` and required files do not exist.

- [ ] **Step 3: Create minimal package files and validator**

Create `content-compliance/README.md`:

```markdown
# Content Compliance Skill

Portable Codex / Claude Code skill for reviewing self-media topics, scripts, and visual descriptions against official-source-backed Douyin and Xiaohongshu compliance rules.
```

Create `content-compliance/SKILL.md`:

```markdown
---
name: content-compliance
description: Review Douyin and Xiaohongshu self-media topics, scripts, and visual descriptions using official-source-backed platform rule cards, a 1-10 risk score, rewrite suggestions, and a mandatory disclaimer.
---

# Content Compliance Skill

Use this skill when the user wants to check whether a self-media topic, title, script, oral draft, subtitle plan, visual description, or promotion plan is likely to create compliance risk on Douyin or Xiaohongshu.

## Supported Platforms

- Douyin, including ordinary posting and DOU+ / OceanEngine promotion contexts.
- Xiaohongshu, including ordinary notes and Shutiao / Pgy / Juguang promotion contexts.

## Required Behavior

1. Identify the target platform.
2. Identify whether the request is a topic gate or draft review.
3. Load the platform rule pack from `rules/douyin.md` or `rules/xiaohongshu.md`.
4. Use `scoring.md` to assign a 1-10 risk score.
5. Use `templates/report.md` for the output.
6. Include the mandatory disclaimer in every report.
7. Do not present unsupported or source-less risks as confirmed platform violations.

## Missing Context

Ask at most one clarifying question when platform is missing:

```text
老板，这次要按抖音还是小红书来审？
```

If only a topic is provided, run Topic Gate. If a title, script, oral draft, subtitle plan, visual description, or promotion plan is provided, run Draft Review.
```

Create `content-compliance/rules/douyin.md`:

```markdown
# Douyin Rule Pack

Rule cards in this file apply to Douyin, DOU+, and OceanEngine contexts. Active rules must cite official source IDs from `../references/sources.md`.

## Rule Card Format

```text
Rule ID:
Platform:
Scope:
Rule Name:
Severity:
Trigger Scenarios:
High-Risk Signals:
Lower-Risk Alternatives:
Review Questions:
Evidence Extraction:
Official Sources:
Source Access Date:
Status:
```

## Rule Cards

```text
Rule ID: douyin.guidance.external_download
Platform: Douyin
Scope: ordinary_post, dou_plus, oceanengine_ad_review
Rule Name: External download or off-platform acquisition guidance
Severity: 4
Trigger Scenarios: Comments asking users to get links, private-message collection, QR-code acquisition, explicit third-party download routes, and visual or spoken instructions that steer users away from the platform.
High-Risk Signals: "comment for link", "private message me", "scan the QR code", "download from this site", "go to GitHub/Gitee and download this package" when framed as an acquisition call-to-action.
Lower-Risk Alternatives: Mention public project names and explain that users should verify official project pages themselves without providing link-claiming, private-message, QR-code, or download prompts.
Review Questions: Does the title, script, subtitle, visual description, pinned comment plan, or promotion plan direct users to obtain materials outside the platform?
Evidence Extraction: Check title, opening, ending CTA, subtitles, visual steps, link descriptions, comments, and private-message prompts.
Official Sources: source.oceanengine.rules_center, source.oceanengine.ad_management
Source Access Date: 2026-06-07
Status: needs_review
```
```

Create `content-compliance/rules/xiaohongshu.md`:

```markdown
# Xiaohongshu Rule Pack

Rule cards in this file apply to Xiaohongshu ordinary notes, Shutiao, Pgy, and Juguang contexts. Active rules must cite official source IDs from `../references/sources.md`.

## Rule Card Format

```text
Rule ID:
Platform:
Scope:
Rule Name:
Severity:
Trigger Scenarios:
High-Risk Signals:
Lower-Risk Alternatives:
Review Questions:
Evidence Extraction:
Official Sources:
Source Access Date:
Status:
```

## Rule Cards

```text
Rule ID: xiaohongshu.guidance.external_contact_or_download
Platform: Xiaohongshu
Scope: ordinary_note, shutiao, pgy, juguang
Rule Name: External contact, private acquisition, or off-platform download guidance
Severity: 4
Trigger Scenarios: Notes, images, comments, or captions asking users to get links through private messages, comments, QR codes, external websites, or third-party downloads.
High-Risk Signals: "comment to get", "private message for resource", QR-code acquisition, external download path, and disguised contact instructions.
Lower-Risk Alternatives: Name public resources without asking users to claim, message, scan, or leave the platform.
Review Questions: Does the note or visual plan turn the platform interaction into an off-platform acquisition path?
Evidence Extraction: Check title, first paragraph, image text, captions, comment plan, private-message prompts, and promotion copy.
Official Sources: source.xiaohongshu.pgy_help, source.xiaohongshu.commercial_site
Source Access Date: 2026-06-07
Status: needs_review
```
```

Create `content-compliance/scoring.md`:

```markdown
# Risk Scoring

Each risk item receives an item score:

```text
item_score = severity × confidence × exposure × scenario × fix_difficulty
```

The theoretical item-score maximum is 15.75, from:

```text
5 × 1.0 × 1.5 × 1.4 × 1.5
```

Final score:

```text
max_item_score = highest item_score
base = ceil(max_item_score / 15.75 * 10)
base = clamp(base, 1, 10)
accumulation = extra risks capped at 2
final_score = min(10, round(base + accumulation))
```

Accumulation:

```text
severity 1-2: +0.25 each
severity 3: +0.5 each
severity 4: +0.75 each
severity 5: +1.0 each
accumulation cap: 2
```

Score bands:

```text
1-2: low risk, publishable reference
3-4: light to medium risk, minor edits recommended
5-6: medium risk, revise before publishing
7-8: high risk, do not publish directly
9-10: very high risk, reframe or rewrite
```

Reports must explain the score. Do not output only a number.
```

Create `content-compliance/templates/report.md`:

```markdown
# Content Compliance Review Report

## 1. Basic Information

- Platform:
- Phase:
- Material Types:
- Promotion Plan:
- Rule Source Date:

## 2. Overall Conclusion

- Recommendation:
- Total Risk Score:
- One-Sentence Rationale:

## 3. Risk List

### Risk 1

- Risk Point:
- Risk Level:
- Item Score:
- Evidence Location:
- Matched Rule:
- Official Source:
- Why It Is Risky:
- Recommended Revision:
- Conservative Revision:
- Avoid This Wording:

## 4. Promotion-Specific Notes

- DOU+ / Shutiao / Pgy / Juguang / OceanEngine notes:

## 5. Disclaimer

免责声明：本报告为 AI 辅助合规参考，依据公开可见的平台规则、整理后的规则卡片以及用户提供的材料生成，不代表抖音、巨量引擎、小红书、蒲公英、聚光、薯条或任何相关平台的官方审核意见。本报告不保证内容发布成功、投放审核通过、获得流量推荐、账号安全或完全符合法律法规。平台规则和审核尺度可能随时间、账号状态、内容上下文和执行口径变化。用户应自行核对最新官方规则，并对内容发布、商业推广、广告合规及相关法律责任负责。涉及法律、医疗、金融、教育、未成年人、食品药品等高风险或强监管领域时，请咨询具备资质的专业人士或平台官方渠道。
```

Create `content-compliance/references/sources.md`:

```markdown
# Official Sources

Only official platform, official help-center, official rule-center, official safety-center, or official commercialization-platform pages count as confirmed sources.

| Source ID | Platform | Scope | Official URL | Page Title | Access Date | Page Updated Date | Retrieval Status | Review Status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| source.douyin.safety_center | Douyin | safety_center | https://95152.douyin.com/ | Douyin safety and trust center | 2026-06-07 | not visible in initial entry | reachable | needs_review |
| source.oceanengine.rules_center | Douyin/OceanEngine | rules_center | https://support.oceanengine.com/support/content/6503488514?graphId=514&mappingType=1&spaceId=171&visitor_source_app_id=171 | OceanEngine rules center | 2026-06-07 | not verified | reachable | needs_review |
| source.oceanengine.ad_management | Douyin/OceanEngine | ad_management | https://support.oceanengine.com/support/content/130539 | OceanEngine advertising delivery management rules | 2026-06-07 | not verified | reachable | needs_review |
| source.oceanengine.account_opening | Douyin/OceanEngine | account_opening | https://support.oceanengine.com/support/content/128059?graphId=514&spaceId=171 | OceanEngine account opening rules | 2026-06-07 | not verified | reachable | needs_review |
| source.xiaohongshu.pgy_help | Xiaohongshu/Pgy | help_center | https://pgy.xiaohongshu.com/help/home | Xiaohongshu Pgy help center | 2026-06-07 | not verified | reachable | needs_review |
| source.xiaohongshu.commercial_site | Xiaohongshu | commercial_site | https://e.xiaohongshu.com/m/product | Xiaohongshu commercialization site | 2026-06-07 | not visible in initial entry | reachable | needs_review |
```

Create `content-compliance/references/official-source-intake.md`:

```markdown
# Official Source Intake

## Source Standard

Use official platform sources first. Third-party posts can help discover official URLs, but they cannot become rule evidence.

## Intake Steps

1. Locate official rule entry pages for the target platform and commercialization product.
2. Visit the official page and record URL, page title, access date, visible page update date, scope, and retrieval status.
3. For dynamic or login-required pages, use a real browser and record the visible scope.
4. Convert official rules into concise rule cards.
5. Mark ambiguous rules as `needs_review` until a human confirms the source interpretation.
6. Do not publish copied full official documents. Publish source links, access metadata, and structured summaries.

## Retrieval Status Values

```text
reachable
dynamic_reachable
login_required
blocked
not_found
```

## Review Status Values

```text
active
needs_review
deprecated
```
```

Create both research files with this starting shape, changing the title line for each platform:

```markdown
# Douyin Official Source Research

## Research Log

| Date | Source ID | What Was Checked | Result |
| --- | --- | --- | --- |
| 2026-06-07 | source.douyin.safety_center | Initial official entry identified from design spec | Needs full rule-entry traversal |
```

```markdown
# Xiaohongshu Official Source Research

## Research Log

| Date | Source ID | What Was Checked | Result |
| --- | --- | --- | --- |
| 2026-06-07 | source.xiaohongshu.pgy_help | Initial official entry identified from design spec | Needs full rule-entry traversal |
```

Create `content-compliance/examples/douyin-topic-gate.md`:

```markdown
# Douyin Topic Gate Example

## Input

Platform: Douyin
Phase: Topic Gate
Topic: How to connect a domestic model to Codex
Promotion Plan: none

## Expected Review Shape

- Recommendation: Continue with a technical education angle, avoiding off-platform acquisition framing.
- Risk Score: 3/10
- Main Check: The topic is acceptable as technical education, but title and calls-to-action must avoid link claiming, private-message delivery, or download guidance.

## Disclaimer

免责声明：本报告为 AI 辅助合规参考，依据公开可见的平台规则、整理后的规则卡片以及用户提供的材料生成，不代表抖音、巨量引擎、小红书、蒲公英、聚光、薯条或任何相关平台的官方审核意见。本报告不保证内容发布成功、投放审核通过、获得流量推荐、账号安全或完全符合法律法规。平台规则和审核尺度可能随时间、账号状态、内容上下文和执行口径变化。用户应自行核对最新官方规则，并对内容发布、商业推广、广告合规及相关法律责任负责。涉及法律、医疗、金融、教育、未成年人、食品药品等高风险或强监管领域时，请咨询具备资质的专业人士或平台官方渠道。
```

Create `content-compliance/examples/douyin-draft-review.md`:

```markdown
# Douyin Draft Review Example

## Input

Platform: Douyin
Phase: Draft Review
Title: Domestic model to Codex, beginner tutorial
Script: I will show you how to download two open-source projects. Get the links in the comments.
Visual Description: Show a project page, a download button, terminal installation, and subtitle text saying "get the link in comments".
Promotion Plan: DOU+

## Expected Review Shape

- Recommendation: Revise before publishing or promotion.
- Risk Score: 7/10
- Main Check: The comment-link and download guidance should be removed or reframed into neutral project-name discussion.

## Disclaimer

免责声明：本报告为 AI 辅助合规参考，依据公开可见的平台规则、整理后的规则卡片以及用户提供的材料生成，不代表抖音、巨量引擎、小红书、蒲公英、聚光、薯条或任何相关平台的官方审核意见。本报告不保证内容发布成功、投放审核通过、获得流量推荐、账号安全或完全符合法律法规。平台规则和审核尺度可能随时间、账号状态、内容上下文和执行口径变化。用户应自行核对最新官方规则，并对内容发布、商业推广、广告合规及相关法律责任负责。涉及法律、医疗、金融、教育、未成年人、食品药品等高风险或强监管领域时，请咨询具备资质的专业人士或平台官方渠道。
```

Create `content-compliance/examples/xiaohongshu-topic-gate.md`:

```markdown
# Xiaohongshu Topic Gate Example

## Input

Platform: Xiaohongshu
Phase: Topic Gate
Topic: How to connect a domestic model to Codex
Promotion Plan: none

## Expected Review Shape

- Recommendation: Continue with a practical tutorial angle, avoiding resource-claiming or exaggerated productivity promises.
- Risk Score: 3/10
- Main Check: The topic is acceptable as technical education if it does not become a private-message resource delivery path.

## Disclaimer

免责声明：本报告为 AI 辅助合规参考，依据公开可见的平台规则、整理后的规则卡片以及用户提供的材料生成，不代表抖音、巨量引擎、小红书、蒲公英、聚光、薯条或任何相关平台的官方审核意见。本报告不保证内容发布成功、投放审核通过、获得流量推荐、账号安全或完全符合法律法规。平台规则和审核尺度可能随时间、账号状态、内容上下文和执行口径变化。用户应自行核对最新官方规则，并对内容发布、商业推广、广告合规及相关法律责任负责。涉及法律、医疗、金融、教育、未成年人、食品药品等高风险或强监管领域时，请咨询具备资质的专业人士或平台官方渠道。
```

Create `content-compliance/examples/xiaohongshu-draft-review.md`:

```markdown
# Xiaohongshu Draft Review Example

## Input

Platform: Xiaohongshu
Phase: Draft Review
Title: Domestic model to Codex, resource pack ready
Copy: Reply in comments and I will send you the project links.
Visual Description: First image says "comment to get the links"; second image shows a download page.
Promotion Plan: Shutiao

## Expected Review Shape

- Recommendation: Revise before publishing or promotion.
- Risk Score: 7/10
- Main Check: Remove comment-based resource claiming and private acquisition framing.

## Disclaimer

免责声明：本报告为 AI 辅助合规参考，依据公开可见的平台规则、整理后的规则卡片以及用户提供的材料生成，不代表抖音、巨量引擎、小红书、蒲公英、聚光、薯条或任何相关平台的官方审核意见。本报告不保证内容发布成功、投放审核通过、获得流量推荐、账号安全或完全符合法律法规。平台规则和审核尺度可能随时间、账号状态、内容上下文和执行口径变化。用户应自行核对最新官方规则，并对内容发布、商业推广、广告合规及相关法律责任负责。涉及法律、医疗、金融、教育、未成年人、食品药品等高风险或强监管领域时，请咨询具备资质的专业人士或平台官方渠道。
```

Create `content-compliance/scripts/validate_skill.py`:

```python
from pathlib import Path
import re
import sys


ROOT = Path(__file__).resolve().parents[1]


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
        cards = re.findall(r"Rule ID: .+?(?=\\n```|\\nRule ID: |\\Z)", content, flags=re.S)
        if not cards:
            fail(f"no rule cards found in {rule_path}")
        for card in cards:
            if "Official Sources:" not in card:
                fail(f"rule card missing Official Sources in {rule_path}: {card[:120]}")
            if "source." not in card:
                fail(f"rule card has no source id in {rule_path}: {card[:120]}")


def main() -> int:
    ensure_required_files()
    ensure_disclaimer()
    ensure_scoring_constants()
    ensure_rule_cards_have_source_ids()
    print("content-compliance skill validation passed")
    return 0


if __name__ == "__main__":
    sys.exit(main())
```

- [ ] **Step 4: Run the tests**

Run:

```bash
python3 -m unittest tests/test_content_compliance_skill.py -v
```

Expected: PASS.

- [ ] **Step 5: Commit**

Run:

```bash
git add content-compliance tests/test_content_compliance_skill.py
git commit -m "feat: add content compliance skill skeleton"
```

Expected: commit succeeds.

## Task 2: Strengthen Validation for Official Source Traceability

**Files:**
- Modify: `tests/test_content_compliance_skill.py`
- Modify: `content-compliance/scripts/validate_skill.py`
- Modify: `content-compliance/references/sources.md`

- [ ] **Step 1: Add failing tests for official source IDs**

Add these imports near the top of `tests/test_content_compliance_skill.py`:

```python
import shutil
import tempfile
```

Add these methods inside `ContentComplianceSkillTest`:

```python
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
```

- [ ] **Step 2: Run tests to verify undeclared-source detection is missing**

Run:

```bash
python3 -m unittest tests/test_content_compliance_skill.py -v
```

Expected: FAIL because the current validator accepts `source.not_declared`.

- [ ] **Step 3: Update validator to check that every rule source ID is declared**

Replace `content-compliance/scripts/validate_skill.py` with:

```python
from pathlib import Path
import re
import sys


ROOT = Path(__file__).resolve().parents[1]


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


def declared_source_ids() -> set[str]:
    sources = read("references/sources.md")
    return set(re.findall(r"\\|\\s*(source\\.[a-z0-9_.-]+)\\s*\\|", sources))


def ensure_source_inventory() -> None:
    sources = read("references/sources.md")
    required_domains = [
        "95152.douyin.com",
        "support.oceanengine.com",
        "pgy.xiaohongshu.com",
        "e.xiaohongshu.com",
    ]
    missing_domains = [domain for domain in required_domains if domain not in sources]
    if missing_domains:
        fail(f"required official domains missing from sources.md: {missing_domains}")
    ids = declared_source_ids()
    if len(ids) < 6:
        fail("expected at least six official source IDs")


def ensure_rule_cards_have_declared_source_ids() -> None:
    ids = declared_source_ids()
    for rule_path in ["rules/douyin.md", "rules/xiaohongshu.md"]:
        content = read(rule_path)
        cards = re.findall(r"Rule ID: .+?(?=\\n```|\\nRule ID: |\\Z)", content, flags=re.S)
        if not cards:
            fail(f"no rule cards found in {rule_path}")
        for card in cards:
            source_match = re.search(r"Official Sources:\\s*(.+)", card)
            if not source_match:
                fail(f"rule card missing Official Sources in {rule_path}: {card[:120]}")
            card_sources = [part.strip() for part in source_match.group(1).split(",")]
            undeclared = [source for source in card_sources if source not in ids]
            if undeclared:
                fail(f"undeclared sources in {rule_path}: {undeclared}")
            status_match = re.search(r"Status:\\s*(active|needs_review|deprecated)", card)
            if not status_match:
                fail(f"rule card has invalid status in {rule_path}: {card[:120]}")


def main() -> int:
    ensure_required_files()
    ensure_disclaimer()
    ensure_scoring_constants()
    ensure_source_inventory()
    ensure_rule_cards_have_declared_source_ids()
    print("content-compliance skill validation passed")
    return 0


if __name__ == "__main__":
    sys.exit(main())
```

- [ ] **Step 4: Run tests**

Run:

```bash
python3 -m unittest tests/test_content_compliance_skill.py -v
```

Expected: PASS.

- [ ] **Step 5: Commit**

Run:

```bash
git add content-compliance/scripts/validate_skill.py tests/test_content_compliance_skill.py content-compliance/references/sources.md
git commit -m "test: enforce official source traceability"
```

Expected: commit succeeds.

## Task 3: Research Douyin and OceanEngine Official Sources

**Files:**
- Modify: `content-compliance/references/sources.md`
- Modify: `content-compliance/references/research/douyin-official-sources.md`

- [ ] **Step 1: Load web-access requirements**

Run:

```bash
sed -n '1,220p' /Users/wzx/.agents/skills/web-access/SKILL.md
```

Expected: The workflow confirms that official source research must use official pages and that browser CDP is available for dynamic or login-required pages.

- [ ] **Step 2: Check browser access for dynamic pages**

Run:

```bash
CLAUDE_SKILL_DIR=/Users/wzx/.agents/skills/web-access node /Users/wzx/.agents/skills/web-access/scripts/check-deps.mjs
```

Expected: exit code `0`, with Node and browser reported as ready.

- [ ] **Step 3: Research official Douyin/OceanEngine rule sources**

Use official pages only as formal evidence. Start with these known official entries:

```text
https://95152.douyin.com/
https://support.oceanengine.com/support/content/6503488514?graphId=514&mappingType=1&spaceId=171&visitor_source_app_id=171
https://support.oceanengine.com/support/content/130539
https://support.oceanengine.com/support/content/128059?graphId=514&spaceId=171
```

For each reachable page, record:

```text
Source ID:
Platform:
Scope:
Official URL:
Page Title:
Access Date:
Page Updated Date:
Retrieval Status:
Review Status:
Key Official Rule Families:
Notes:
```

Add additional official Douyin / OceanEngine source rows when official navigation reveals pages for:

```text
community rules
creator rules
safety/trust rules
advertising review rules
account opening rules
ad delivery management rules
DOU+ promotion rules
external-link or off-platform guidance rules
regulated industry rules
```

- [ ] **Step 4: Update source inventory and research log**

Update `content-compliance/references/sources.md` by adding one table row per confirmed official source.

Update `content-compliance/references/research/douyin-official-sources.md` with this structure for each source:

```markdown
## source.example.official_id

- Official URL:
- Page Title:
- Access Date:
- Page Updated Date:
- Retrieval Status:
- Review Status:
- Covered Rule Families:
  - external guidance
  - advertising review
  - regulated industries
- Evidence Notes:
  - Summarize official rule meaning in your own words.
  - Use only short excerpts when needed.
- Rule Cards To Create:
  - douyin.guidance.external_download
```

Use concrete values from the visited official page. Mark pages that require login or cannot be reached as `login_required` or `blocked`.

- [ ] **Step 5: Run validation**

Run:

```bash
python3 content-compliance/scripts/validate_skill.py
python3 -m unittest tests/test_content_compliance_skill.py -v
```

Expected: both PASS.

- [ ] **Step 6: Commit**

Run:

```bash
git add content-compliance/references/sources.md content-compliance/references/research/douyin-official-sources.md
git commit -m "docs: record Douyin official compliance sources"
```

Expected: commit succeeds.

## Task 4: Build Douyin Rule Cards from Official Sources

**Files:**
- Modify: `content-compliance/rules/douyin.md`
- Modify: `content-compliance/examples/douyin-topic-gate.md`
- Modify: `content-compliance/examples/douyin-draft-review.md`

- [ ] **Step 1: Add failing test for active-rule traceability**

Add this method inside `ContentComplianceSkillTest`:

```python
    def test_active_rules_do_not_use_needs_review_status(self):
        for relative_path in ["rules/douyin.md", "rules/xiaohongshu.md"]:
            content = read_package_file(relative_path)
            active_blocks = [block for block in content.split("Rule ID: ")[1:] if "Status: active" in block]
            for block in active_blocks:
                self.assertIn("Official Sources: source.", block)
                self.assertIn("Source Access Date:", block)
```

- [ ] **Step 2: Run tests**

Run:

```bash
python3 -m unittest tests/test_content_compliance_skill.py -v
```

Expected: PASS because no active rules are required yet.

- [ ] **Step 3: Replace Douyin starter card with official-source-backed rule cards**

Edit `content-compliance/rules/douyin.md`. Keep the Rule Card Format section. Replace the starter rule cards with official-source-backed cards covering these families when supported by sources collected in Task 3:

```text
douyin.topic.regulated_industry
douyin.title.exaggeration_or_absolute_claim
douyin.guidance.external_download
douyin.guidance.comment_or_private_message_acquisition
douyin.visual.qr_code_or_external_link
douyin.promotion.dou_plus_review_stricter_context
douyin.advertising.qualification_or_industry_restriction
```

Use this exact card shape for each card:

```text
Rule ID: douyin.guidance.external_download
Platform: Douyin
Scope: ordinary_post, dou_plus, oceanengine_ad_review
Rule Name: External download or off-platform acquisition guidance
Severity: 4
Trigger Scenarios: User-facing instructions that make the viewer obtain tools, links, packages, or files through comments, private messages, QR codes, external websites, or third-party download platforms.
High-Risk Signals: "comment for link", "private message me", "scan the QR code", "download from this site", "go to GitHub/Gitee and download this package" when framed as a call-to-action.
Lower-Risk Alternatives: Explain project names and evaluation criteria without asking viewers to claim links, message the creator, scan codes, or follow an off-platform acquisition path.
Review Questions: Does any title, script line, subtitle, visual step, comment plan, or promotion copy direct the viewer to obtain materials outside the platform?
Evidence Extraction: Check title, opening, ending CTA, subtitles, visual steps, screen recordings, link descriptions, comments, and private-message prompts.
Official Sources: source.oceanengine.rules_center, source.oceanengine.ad_management
Source Access Date: 2026-06-07
Status: active
```

Only mark a card `active` when the official-source research supports it. Keep unsupported cards as `needs_review` and make the evidence limitation explicit in the card's wording.

- [ ] **Step 4: Add Douyin example reports**

Create `content-compliance/examples/douyin-topic-gate.md`:

```markdown
# Douyin Topic Gate Example

## Input

```text
平台：抖音
阶段：选题
选题：如何把国产模型接入 Codex
是否计划投放：否
```

## Expected Review Shape

- Platform: Douyin
- Phase: topic_gate
- Recommendation: 可继续做，但避免把内容包装成绕过限制、获取资源、领取链接或站外下载教程。
- Risk Score: 3/10
- Required Checks:
  - The topic itself is technical education.
  - Title and angle must avoid off-platform acquisition guidance.
  - If promotion is planned later, rerun Draft Review with DOU+ context.

## Disclaimer

免责声明：本报告为 AI 辅助合规参考，依据公开可见的平台规则、整理后的规则卡片以及用户提供的材料生成，不代表抖音、巨量引擎、小红书、蒲公英、聚光、薯条或任何相关平台的官方审核意见。本报告不保证内容发布成功、投放审核通过、获得流量推荐、账号安全或完全符合法律法规。平台规则和审核尺度可能随时间、账号状态、内容上下文和执行口径变化。用户应自行核对最新官方规则，并对内容发布、商业推广、广告合规及相关法律责任负责。涉及法律、医疗、金融、教育、未成年人、食品药品等高风险或强监管领域时，请咨询具备资质的专业人士或平台官方渠道。
```

Create `content-compliance/examples/douyin-draft-review.md`:

```markdown
# Douyin Draft Review Example

## Input

```text
平台：抖音
阶段：成稿
标题：国产模型接入 Codex，保姆级教程
口播稿：我会教你下载两个开源项目，评论区拿链接。
画面描述：展示 GitHub 页面、下载按钮、字幕提示“评论区拿链接”。
是否计划投放：DOU+
```

## Expected Review Shape

- Platform: Douyin
- Phase: draft_review
- Recommendation: 修改后再发布；如计划 DOU+，不建议保留“评论区拿链接”和直接下载引导。
- Risk Score: 7/10
- Matched Risk:
  - Rule: douyin.guidance.external_download
  - Evidence: 口播“下载两个开源项目”、字幕“评论区拿链接”、画面展示下载按钮。
  - Safer Revision: 说明项目名称、用途和安全校验方法，不把评论区、私信或下载链接作为行动路径。

## Disclaimer

免责声明：本报告为 AI 辅助合规参考，依据公开可见的平台规则、整理后的规则卡片以及用户提供的材料生成，不代表抖音、巨量引擎、小红书、蒲公英、聚光、薯条或任何相关平台的官方审核意见。本报告不保证内容发布成功、投放审核通过、获得流量推荐、账号安全或完全符合法律法规。平台规则和审核尺度可能随时间、账号状态、内容上下文和执行口径变化。用户应自行核对最新官方规则，并对内容发布、商业推广、广告合规及相关法律责任负责。涉及法律、医疗、金融、教育、未成年人、食品药品等高风险或强监管领域时，请咨询具备资质的专业人士或平台官方渠道。
```

- [ ] **Step 5: Run validation and tests**

Run:

```bash
python3 content-compliance/scripts/validate_skill.py
python3 -m unittest tests/test_content_compliance_skill.py -v
```

Expected: both PASS.

- [ ] **Step 6: Commit**

Run:

```bash
git add content-compliance/rules/douyin.md content-compliance/examples/douyin-topic-gate.md content-compliance/examples/douyin-draft-review.md tests/test_content_compliance_skill.py
git commit -m "feat: add Douyin official-source rule cards"
```

Expected: commit succeeds.

## Task 5: Research Xiaohongshu, Pgy, Shutiao, and Juguang Official Sources

**Files:**
- Modify: `content-compliance/references/sources.md`
- Modify: `content-compliance/references/research/xiaohongshu-official-sources.md`

- [ ] **Step 1: Confirm browser access**

Run:

```bash
CLAUDE_SKILL_DIR=/Users/wzx/.agents/skills/web-access node /Users/wzx/.agents/skills/web-access/scripts/check-deps.mjs
```

Expected: exit code `0`, with browser proxy ready.

- [ ] **Step 2: Research official Xiaohongshu sources**

Use official pages only as formal evidence. Start with:

```text
https://pgy.xiaohongshu.com/help/home
https://e.xiaohongshu.com/m/product
```

Traverse official navigation or official search results for:

```text
community covenant or community rules
note content standards
Shutiao promotion review rules
Pgy content cooperation rules
Pgy advertising or brand cooperation rules
Juguang advertising review rules
external contact or off-platform guidance rules
commercial disclosure rules
false marketing or exaggerated claim rules
regulated industry rules
```

Record each official page using the same structure as Task 3.

- [ ] **Step 3: Update source inventory and research log**

Update `content-compliance/references/sources.md` with every confirmed official Xiaohongshu-related source.

Update `content-compliance/references/research/xiaohongshu-official-sources.md` using this structure:

```markdown
## source.xiaohongshu.example_id

- Official URL:
- Page Title:
- Access Date:
- Page Updated Date:
- Retrieval Status:
- Review Status:
- Covered Rule Families:
  - external contact
  - commercial disclosure
  - promotion review
- Evidence Notes:
  - Summarize official rule meaning in your own words.
  - Use only short excerpts when needed.
- Rule Cards To Create:
  - xiaohongshu.guidance.external_contact_or_download
```

- [ ] **Step 4: Run validation**

Run:

```bash
python3 content-compliance/scripts/validate_skill.py
python3 -m unittest tests/test_content_compliance_skill.py -v
```

Expected: both PASS.

- [ ] **Step 5: Commit**

Run:

```bash
git add content-compliance/references/sources.md content-compliance/references/research/xiaohongshu-official-sources.md
git commit -m "docs: record Xiaohongshu official compliance sources"
```

Expected: commit succeeds.

## Task 6: Build Xiaohongshu Rule Cards from Official Sources

**Files:**
- Modify: `content-compliance/rules/xiaohongshu.md`
- Modify: `content-compliance/examples/xiaohongshu-topic-gate.md`
- Modify: `content-compliance/examples/xiaohongshu-draft-review.md`

- [ ] **Step 1: Replace Xiaohongshu starter card with official-source-backed rule cards**

Edit `content-compliance/rules/xiaohongshu.md`. Keep the Rule Card Format section. Replace the starter rule cards with official-source-backed cards covering these families when supported by sources collected in Task 5:

```text
xiaohongshu.topic.regulated_industry
xiaohongshu.title.exaggeration_or_false_marketing
xiaohongshu.guidance.external_contact_or_download
xiaohongshu.visual.qr_code_or_contact_information
xiaohongshu.commerce.undisclosed_commercial_content
xiaohongshu.promotion.shutiao_review_stricter_context
xiaohongshu.advertising.qualification_or_industry_restriction
```

Use this exact card shape for each card:

```text
Rule ID: xiaohongshu.guidance.external_contact_or_download
Platform: Xiaohongshu
Scope: ordinary_note, shutiao, pgy, juguang
Rule Name: External contact, private acquisition, or off-platform download guidance
Severity: 4
Trigger Scenarios: Notes, images, captions, comments, or private-message plans that ask users to obtain links, files, tools, or contact paths outside the platform.
High-Risk Signals: "comment to get", "private message for resource", QR-code acquisition, external download path, disguised contact instructions, or image text that redirects users to off-platform resources.
Lower-Risk Alternatives: Name public resources and describe evaluation criteria without asking users to claim, message, scan, or leave the platform.
Review Questions: Does the note, image text, comment plan, or promotion copy turn engagement into an off-platform acquisition path?
Evidence Extraction: Check title, first paragraph, image text, captions, comment plan, private-message prompts, and promotion copy.
Official Sources: source.xiaohongshu.pgy_help, source.xiaohongshu.commercial_site
Source Access Date: 2026-06-07
Status: active
```

Only mark a card `active` when official-source research supports it.

- [ ] **Step 2: Add Xiaohongshu example reports**

Create `content-compliance/examples/xiaohongshu-topic-gate.md`:

```markdown
# Xiaohongshu Topic Gate Example

## Input

```text
平台：小红书
阶段：选题
选题：如何把国产模型接入 Codex
是否计划投放：否
```

## Expected Review Shape

- Platform: Xiaohongshu
- Phase: topic_gate
- Recommendation: 可以继续做，但标题和封面应避免夸大、神化工具效果或设计成资料领取入口。
- Risk Score: 3/10
- Required Checks:
  - The topic is technical education.
  - Avoid off-platform acquisition, private-message resource delivery, and exaggerated productivity claims.

## Disclaimer

免责声明：本报告为 AI 辅助合规参考，依据公开可见的平台规则、整理后的规则卡片以及用户提供的材料生成，不代表抖音、巨量引擎、小红书、蒲公英、聚光、薯条或任何相关平台的官方审核意见。本报告不保证内容发布成功、投放审核通过、获得流量推荐、账号安全或完全符合法律法规。平台规则和审核尺度可能随时间、账号状态、内容上下文和执行口径变化。用户应自行核对最新官方规则，并对内容发布、商业推广、广告合规及相关法律责任负责。涉及法律、医疗、金融、教育、未成年人、食品药品等高风险或强监管领域时，请咨询具备资质的专业人士或平台官方渠道。
```

Create `content-compliance/examples/xiaohongshu-draft-review.md`:

```markdown
# Xiaohongshu Draft Review Example

## Input

```text
平台：小红书
阶段：成稿
标题：国产模型接入 Codex，资料包直接拿
正文：评论区回复关键词，我把项目链接发给你。
画面描述：首图写“评论区领链接”，第二张展示下载页面。
是否计划投放：薯条
```

## Expected Review Shape

- Platform: Xiaohongshu
- Phase: draft_review
- Recommendation: 修改后再发布；如计划薯条，应移除评论区领取和私信资源交付表达。
- Risk Score: 7/10
- Matched Risk:
  - Rule: xiaohongshu.guidance.external_contact_or_download
  - Evidence: 标题“资料包直接拿”、正文“评论区回复关键词”、首图“评论区领链接”。
  - Safer Revision: 改为介绍项目名称、适用场景和安全校验方法，不把评论区或私信作为资源获取路径。

## Disclaimer

免责声明：本报告为 AI 辅助合规参考，依据公开可见的平台规则、整理后的规则卡片以及用户提供的材料生成，不代表抖音、巨量引擎、小红书、蒲公英、聚光、薯条或任何相关平台的官方审核意见。本报告不保证内容发布成功、投放审核通过、获得流量推荐、账号安全或完全符合法律法规。平台规则和审核尺度可能随时间、账号状态、内容上下文和执行口径变化。用户应自行核对最新官方规则，并对内容发布、商业推广、广告合规及相关法律责任负责。涉及法律、医疗、金融、教育、未成年人、食品药品等高风险或强监管领域时，请咨询具备资质的专业人士或平台官方渠道。
```

- [ ] **Step 3: Run validation and tests**

Run:

```bash
python3 content-compliance/scripts/validate_skill.py
python3 -m unittest tests/test_content_compliance_skill.py -v
```

Expected: both PASS.

- [ ] **Step 4: Commit**

Run:

```bash
git add content-compliance/rules/xiaohongshu.md content-compliance/examples/xiaohongshu-topic-gate.md content-compliance/examples/xiaohongshu-draft-review.md
git commit -m "feat: add Xiaohongshu official-source rule cards"
```

Expected: commit succeeds.

## Task 7: Finalize Runtime Instructions in SKILL.md

**Files:**
- Modify: `content-compliance/SKILL.md`
- Modify: `tests/test_content_compliance_skill.py`

- [ ] **Step 1: Add tests for workflow instructions**

Add this method inside `ContentComplianceSkillTest`:

```python
    def test_skill_instructions_include_required_workflows(self):
        skill = read_package_file("SKILL.md")
        required_phrases = [
            "Topic Gate",
            "Draft Review",
            "rules/douyin.md",
            "rules/xiaohongshu.md",
            "templates/report.md",
            "mandatory disclaimer",
            "needs_review",
        ]
        missing = [phrase for phrase in required_phrases if phrase not in skill]
        self.assertEqual(missing, [])
```

- [ ] **Step 2: Run tests to verify failure**

Run:

```bash
python3 -m unittest tests/test_content_compliance_skill.py -v
```

Expected: FAIL because `SKILL.md` does not yet contain all required workflow phrases.

- [ ] **Step 3: Replace SKILL.md with final workflow**

Replace `content-compliance/SKILL.md` with:

```markdown
---
name: content-compliance
description: Review Douyin and Xiaohongshu self-media topics, scripts, and visual descriptions using official-source-backed platform rule cards, a 1-10 risk score, rewrite suggestions, and a mandatory disclaimer.
---

# Content Compliance Skill

Use this skill when the user wants to check whether a self-media topic, title, script, oral draft, subtitle plan, visual description, or promotion plan is likely to create compliance risk on Douyin or Xiaohongshu.

## Supported Platforms

- Douyin, including ordinary posting and DOU+ / OceanEngine promotion contexts.
- Xiaohongshu, including ordinary notes and Shutiao / Pgy / Juguang promotion contexts.

## Source Policy

Official-source-backed rules are required for confirmed risk findings. A rule card marked `needs_review` can be mentioned only as an uncertainty note, not as a confirmed platform violation.

Never claim that a report guarantees publishing approval, traffic delivery, ad approval, account safety, or legal compliance.

## Workflow

### Step 1: Identify Platform

If the platform is missing, ask one question:

```text
老板，这次要按抖音还是小红书来审？
```

If the user says Douyin, load `rules/douyin.md`. If the user says Xiaohongshu, load `rules/xiaohongshu.md`.

### Step 2: Choose Review Mode

Use Topic Gate when the user provides only a topic, rough angle, title idea, or outline.

Use Draft Review when the user provides any title, script, oral draft, subtitle plan, visual description, comment plan, private-message plan, promotion plan, or screenshot/video-frame description.

### Step 3: Collect Review Context

Extract:

```text
platform:
phase:
topic:
title:
script_or_copy:
visual_description:
comment_or_private_message_plan:
promotion_plan:
regulated_industry_context:
```

If a field is absent, leave it absent and review the provided material. Do not invent missing content.

### Step 4: Check Risk Layers

Review these layers:

```text
topic risk
title or cover risk
script or oral wording risk
visual or subtitle risk
external guidance, download, comment, private-message, or QR-code risk
commercial or promotion review risk
regulated-industry risk
```

### Step 5: Score

Use `scoring.md`. Reports must explain the score using:

```text
severity
confidence
exposure
scenario
fix_difficulty
accumulation
```

### Step 6: Report

Use `templates/report.md`. Every report must include the mandatory disclaimer.

For each confirmed risk, cite:

```text
rule ID
official source ID
evidence location
risk reason
recommended revision
conservative revision
```

For source gaps, say:

```text
这条风险只能作为待复核提示，因为当前规则卡尚未绑定足够官方来源。
```

## Output Tone

Be practical and direct. Avoid absolute promises such as “必过”, “一定安全”, “绝对违规”, or “平台一定会处罚”.
```

- [ ] **Step 4: Run tests**

Run:

```bash
python3 -m unittest tests/test_content_compliance_skill.py -v
```

Expected: PASS.

- [ ] **Step 5: Commit**

Run:

```bash
git add content-compliance/SKILL.md tests/test_content_compliance_skill.py
git commit -m "feat: finalize content compliance skill workflow"
```

Expected: commit succeeds.

## Task 8: Strengthen Report Template and Examples Validation

**Files:**
- Modify: `content-compliance/templates/report.md`
- Modify: `content-compliance/scripts/validate_skill.py`
- Modify: `tests/test_content_compliance_skill.py`

- [ ] **Step 1: Add tests for example disclaimers and report sections**

Add this method inside `ContentComplianceSkillTest`:

```python
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
```

- [ ] **Step 2: Run tests**

Run:

```bash
python3 -m unittest tests/test_content_compliance_skill.py -v
```

Expected: PASS after examples from Tasks 4 and 6 exist.

- [ ] **Step 3: Add validator checks for report sections and example disclaimers**

Add these functions to `content-compliance/scripts/validate_skill.py` before `main()`:

```python
def ensure_report_sections() -> None:
    report = read("templates/report.md")
    required_sections = [
        "## 1. Basic Information",
        "## 2. Overall Conclusion",
        "## 3. Risk List",
        "## 4. Promotion-Specific Notes",
        "## 5. Disclaimer",
    ]
    missing = [section for section in required_sections if section not in report]
    if missing:
        fail(f"report template sections missing: {missing}")


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
```

Update `main()`:

```python
def main() -> int:
    ensure_required_files()
    ensure_disclaimer()
    ensure_report_sections()
    ensure_scoring_constants()
    ensure_source_inventory()
    ensure_rule_cards_have_declared_source_ids()
    ensure_examples_are_complete()
    print("content-compliance skill validation passed")
    return 0
```

- [ ] **Step 4: Run validation and tests**

Run:

```bash
python3 content-compliance/scripts/validate_skill.py
python3 -m unittest tests/test_content_compliance_skill.py -v
```

Expected: both PASS.

- [ ] **Step 5: Commit**

Run:

```bash
git add content-compliance/templates/report.md content-compliance/scripts/validate_skill.py tests/test_content_compliance_skill.py
git commit -m "test: validate report template and examples"
```

Expected: commit succeeds.

## Task 9: Final Verification and Packaging Notes

**Files:**
- Modify: `content-compliance/README.md`

- [ ] **Step 1: Update README usage instructions**

Replace `content-compliance/README.md` with:

```markdown
# Content Compliance Skill

Portable Codex / Claude Code skill for reviewing self-media topics, scripts, and visual descriptions against official-source-backed Douyin and Xiaohongshu compliance rules.

## Use Cases

- Topic Gate: check whether a topic is worth producing before writing the script.
- Draft Review: check title, script, oral draft, subtitles, visual description, comment plan, private-message plan, and promotion plan before publishing or promoting.

## Supported Platforms

- Douyin, including DOU+ and OceanEngine contexts.
- Xiaohongshu, including Shutiao, Pgy, and Juguang contexts.

## Public-Release Warning

This skill is a compliance reference tool, not an official review tool. It does not guarantee publishing approval, ad review approval, traffic delivery, account safety, or legal compliance.

## Validation

Run:

```bash
python3 content-compliance/scripts/validate_skill.py
python3 -m unittest tests/test_content_compliance_skill.py -v
```
```

- [ ] **Step 2: Run full validation**

Run:

```bash
python3 content-compliance/scripts/validate_skill.py
python3 -m unittest tests/test_content_compliance_skill.py -v
git status --short
```

Expected:

```text
content-compliance skill validation passed
tests pass
only intentional README change is uncommitted
```

- [ ] **Step 3: Commit README**

Run:

```bash
git add content-compliance/README.md
git commit -m "docs: add content compliance skill usage notes"
```

Expected: commit succeeds.

- [ ] **Step 4: Final clean-status check**

Run:

```bash
git status --short
```

Expected: no tracked changes. The pre-existing `.codex-hub.json` may remain untracked unless the user asks to include it.
