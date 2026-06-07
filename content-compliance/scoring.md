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
