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
