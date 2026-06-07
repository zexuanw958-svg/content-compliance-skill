# Content Compliance Skill

Codex / Claude Code skill for reviewing Douyin and Xiaohongshu self-media topics, scripts, visual descriptions, and promotion plans against official-source-backed platform rule cards.

中文名建议：内容合规检测。

## What It Does

- Checks topic ideas before production.
- Reviews titles, scripts, subtitles, visual plans, comment/private-message plans, and promotion plans before publishing.
- Supports Douyin, DOU+ / OceanEngine contexts, Xiaohongshu, Shutiao, Pgy, and Juguang contexts.
- Produces a 1-10 risk score with severity, confidence, exposure, scenario, fix difficulty, and accumulation factors.
- Produces 10-cell visual bars and per-layer safety scores, so local weak spots such as external download guidance can stand out even when the overall score is acceptable.
- Separates confirmed active-rule risks from pending-review notes.
- Includes mandatory disclaimer text for public or team use.

## Install

Copy the skill package into your local skill root:

```bash
cp -R content-compliance ~/.codex/skills/
cp -R content-compliance ~/.agents/skills/
```

Use the first command for Codex. Use the second command for agent runtimes that read `~/.agents/skills`.

## Invocation

Natural Chinese triggers:

```text
检测
合规检测
内容合规检测
帮我审一下抖音选题
帮我查一下小红书稿子风险
```

Slash aliases, where supported:

```text
/检测
/content-compliance
```

If a runtime does not support non-ASCII slash-command names, use `/content-compliance` or ask naturally in Chinese.

## Validate

```bash
python3 content-compliance/scripts/validate_skill.py
python3 -m unittest tests/test_content_compliance_skill.py -v
```

Validation note:

This repository intentionally keeps `content-compliance/README.md` inside the skill package because the package is meant for public distribution and standalone inspection. Some generic skill-creator validators prefer no `README.md` inside a skill folder and may warn about this. For this project, use the bundled validator and test suite above as the source of truth.

## Disclaimer

This skill is a compliance reference tool, not an official review tool. It does not guarantee publishing approval, ad review approval, traffic delivery, account safety, or legal compliance.
