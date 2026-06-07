# Content Compliance Skill

Portable Codex / Claude Code skill for reviewing self-media topics, scripts, and visual descriptions against official-source-backed Douyin and Xiaohongshu compliance rules.

## Use Cases

- Topic Gate: check whether a topic is worth producing before writing the script.
- Draft Review: check title, script, oral draft, subtitles, visual description, comment plan, private-message plan, and promotion plan before publishing or promoting.
- Visual Review: show a 10-cell risk/safety bar and per-layer safety scores so the weakest local issue stands out.

## Invocation

Skill machine name:

```text
content-compliance
```

Recommended Chinese name:

```text
内容合规检测
```

Daily Chinese triggers:

```text
检测
合规检测
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

Validation note:

This `README.md` is intentionally kept inside the skill package for public distribution and standalone review. Some generic skill-creator validators prefer no `README.md` inside a skill folder and may warn about this. For this project, use the bundled validator and test suite above as the source of truth.
