# Content Compliance Skill Package

Portable Codex / Claude Code skill package for reviewing Douyin and Xiaohongshu self-media content against official-source-backed rule cards.

Recommended Chinese name: **内容合规检测**.

## Capabilities

- Topic Gate: review whether a content idea is worth producing before writing the script.
- Draft Review: review titles, scripts, subtitles, visual descriptions, comment plans, private-message plans, and promotion plans before publishing.
- Visual Review: output 10-cell risk and safety bars, plus per-layer safety scores, so weak local issues stand out clearly.
- Promotion Review: separate ordinary publishing context from DOU+, OceanEngine, Shutiao, Pgy, and Juguang contexts.
- Source Discipline: separate confirmed `Status: active` rule matches from `Status: needs_review` notes.

## Invocation

Skill machine name:

```text
content-compliance
```

Daily Chinese triggers:

```text
检测
合规检测
内容合规检测
帮我审一下抖音选题
帮我查一下小红书稿子风险
```

Slash-command aliases, where supported:

```text
/检测
/content-compliance
```

If a runtime does not support non-ASCII slash-command names, use `/content-compliance` or ask naturally in Chinese.

## Supported Platforms

| Platform | Contexts |
| --- | --- |
| Douyin | ordinary posts, DOU+, OceanEngine ad-review contexts |
| Xiaohongshu | ordinary notes, Shutiao, Pgy, Juguang promotion contexts |

## Output Contract

Every report should include:

- `Total Risk Score`: 1-10, higher means riskier.
- `Overall Safety Score`: 1-10, higher means safer.
- `Risk Bar` and `Safety Bar`: exactly 10 cells.
- `Layer Safety Dashboard`: topic, title/cover, wording, visual/subtitle, external guidance, promotion, regulated-industry.
- `Weakest Areas`: the 1-3 lowest-scoring layers with evidence and fast fixes.
- Mandatory disclaimer.

## Validation

From the repository root, run:

```bash
python3 content-compliance/scripts/validate_skill.py
python3 -m unittest tests/test_content_compliance_skill.py -v
```

Validation note:

This `README.md` is intentionally kept inside the skill package for public distribution and standalone review. Some generic skill-creator validators prefer no `README.md` inside a skill folder and may warn about this. For this project, use the bundled validator and test suite above as the source of truth.

## Public-Release Warning

This skill is a compliance reference tool, not an official review tool. It does not guarantee publishing approval, ad review approval, traffic delivery, account safety, or legal compliance.
