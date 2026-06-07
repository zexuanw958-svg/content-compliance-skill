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
