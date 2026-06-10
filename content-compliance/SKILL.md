---
name: content-compliance
description: Review Douyin and Xiaohongshu self-media topics, scripts, and visual descriptions using official-source-backed platform rule cards, a 1-10 risk score, a uniform-color visual risk bar, weak-area safety scores, rewrite suggestions, and a mandatory disclaimer. Use when the user says 检测, 合规检测, 内容合规, 审一下抖音/小红书选题, 查一下稿子风险, or asks whether a topic/script/visual plan can be posted or promoted.
---

# Content Compliance Skill

## Invocation

Preferred Chinese trigger:

```text
检测
合规检测
内容合规检测
帮我审一下抖音/小红书选题
帮我查一下这段稿子有没有违规风险
```

Slash-command aliases, when the runtime supports bundled commands:

```text
/检测
/content-compliance
```

Use this skill when the user wants to check whether a self-media topic, title, script, oral draft, subtitle plan, visual description, or promotion plan is likely to create compliance risk on Douyin or Xiaohongshu.

## Supported Platforms

- Douyin, including ordinary posting and DOU+ / OceanEngine promotion contexts.
- Xiaohongshu, including ordinary notes and Shutiao / Pgy / Juguang promotion contexts.

## Source Policy

Official-source-backed rules are required for confirmed risk findings.

Only `Status: active` rule matches enter confirmed risks and the final score. `Status: needs_review` matches must be reported separately as review-only / pending-review notes, not in confirmed risks or final score, unless the same evidence also independently matches an active rule.

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

Assign every layer a `Layer Safety Score` from 1-10, where 10 means this layer looks safest and 1 means this layer is the weakest. Layers with no concern should usually score 9-10. A weak layer can receive a low safety score even when the concern is only a pending-review note, but label it as diagnostic rather than a confirmed active-rule risk.

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

Also include:

```text
Total Risk Score
Risk Bar
Layer Safety Dashboard
Weakest Areas
```

Highlight the 1-3 lowest-scoring weak areas. Do not let a high overall score hide a local problem such as external download guidance, comment/private-message link acquisition, QR-code guidance, or promotion-specific qualification gaps.

Do not output Overall Safety Score or Safety Bar for the final score. They are only inverse restatements of Total Risk Score and add visual noise. Keep one final `Total Risk Score` and one final `Risk Bar`. Use `Layer Safety Score` only inside the layer dashboard.

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

For source gaps or `Status: needs_review` matches, say:

```text
这条风险只能作为待复核提示，因为当前规则卡处于 `needs_review`，官方来源覆盖范围或规则解释仍需人工复核。
```

## Output Tone

Be practical and direct. Avoid absolute promises such as “必过”, “一定安全”, “绝对违规”, or “平台一定会处罚”.
