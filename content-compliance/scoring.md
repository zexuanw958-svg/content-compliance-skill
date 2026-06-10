# Risk Scoring

Only confirmed risks matched by `Status: active` rule cards are item-score inputs.

`Status: needs_review` matches are pending-review notes. They do not enter item score, accumulation, or final score unless the same evidence independently matches a `Status: active` rule.

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

Do not double-count the same evidence across overlapping active rules. If one phrase, frame, CTA, landing-page flow, or qualification gap triggers several closely related active rules, score the strongest matching item and use the overlap only in the rationale unless there is distinct evidence for another item.

If no `Status: active` rule matches, use a low baseline caution score instead of a confirmed-risk score:

```text
1: baseline caution, no concern found
2: baseline caution, minor editorial caution
3: baseline caution, unresolved topic-gate uncertainty such as missing promotion context, missing regulated-category context, incomplete distribution assumptions, or draft-review uncertainty where only `Status: needs_review` rules are implicated
```

Label baseline scores as baseline caution, not confirmed violations or confirmed risks.

Score bands:

```text
1-2: low risk, publishable reference
3-4: light to medium risk, minor edits recommended
5-6: medium risk, revise before publishing
7-8: high risk, do not publish directly
9-10: very high risk, reframe or rewrite
```

Reports must explain the score. Do not output only a number. Include the factors `severity`, `confidence`, `exposure`, `scenario`, `fix_difficulty`, and `accumulation`, and make clear when pending-review notes were excluded from scoring.

## Visual Scores

Reports must include one risk-oriented visual for the final score:

```text
Total Risk Score: 1-10, higher means riskier.
```

For the visual bar, always use exactly 10 cells.

Risk Bar is a score-fill bar with one uniform color. Fill cells equal to Total Risk Score, leave the rest empty, and choose the filled-cell color from the score band:

```text
1-4: 🟩 low-risk filled cells
5-6: 🟨 medium-risk filled cells
7-10: 🟥 high-risk filled cells
Empty cells: ⬜
```

Risk Bar output format:

```text
Risk Bar: <score>/10 <filled cells in one band color><empty cells> (<low-risk|medium-risk|high-risk>)
```

Do not output both a final Risk Bar and a final Safety Bar. Overall safety is only the inverse of risk and adds visual noise. Keep one final risk score and one final risk bar.

Layer Safety Scores remain useful because they identify weak local areas. Keep them in the Layer Safety Dashboard.

Examples:

```text
Risk Bar: 3/10 🟩🟩🟩⬜⬜⬜⬜⬜⬜⬜ (low-risk)
Risk Bar: 5/10 🟨🟨🟨🟨🟨⬜⬜⬜⬜⬜ (medium-risk)
Risk Bar: 9/10 🟥🟥🟥🟥🟥🟥🟥🟥🟥⬜ (high-risk)
```

## Layer Safety Scores

Layer safety scores are diagnostic scores for user readability. They help expose local weak spots even when the official-source-backed `Total Risk Score` remains low.

Use these bands:

```text
9-10: clean or only negligible wording caution
8: minor wording caution
6-7: pending-review concern, missing context, or moderate edit recommended
4-5: confirmed active-rule concern or strong pending-review concern; revise before publishing or promotion
1-3: major confirmed concern, paid-promotion blocker, or severe off-platform acquisition/qualification issue
```

Every report must include a `Layer Safety Dashboard` with the standard layers:

```text
topic
title_or_cover
script_or_oral_wording
visual_or_subtitle
external_guidance_download_comment_private_message_or_qr
promotion_or_ad_review
regulated_industry
```

After the dashboard, list `Weakest Areas`: the 1-3 layers with the lowest safety scores. For each weak area, include evidence location, why it is weak, and the fastest safe revision. Pending-review weak areas must explicitly say they are not confirmed active-rule risks unless the same evidence independently matches an active rule.
