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
