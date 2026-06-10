# Periodic Official Rule Refresh

This project is official-source-first, not generic-web-rule-first.

The rule library should be refreshed on a fixed cadence and before major public demos, releases, or video examples. The refresh goal is to detect whether official public rules have changed, then update source metadata, research notes, rule cards, examples, and tests.

## What This Workflow Guarantees

- Official public sources are checked before rule-card updates.
- Confirmed risk rules must cite official source IDs from `references/sources.md`.
- Ambiguous or partially reviewed official pages remain `Status: needs_review`.
- Third-party articles can help discover official URLs, but cannot become rule evidence.
- The package records access dates and visible official update dates where available.

## What This Workflow Does Not Guarantee

- It does not guarantee complete coverage of every platform rule, hidden review policy, account-specific decision, or login-only backend change.
- It does not automatically update rules in real time.
- It does not guarantee publishing approval, paid-promotion approval, traffic delivery, account safety, or legal compliance.

## Refresh Cadence

Recommended cadence:

- Before every public tutorial, launch post, or video demo.
- Monthly for normal maintenance.
- Immediately when a platform publishes a visible rule update, enforcement notice, or product-policy change.

## Refresh Steps

1. Open `references/sources.md`.
2. Visit each official URL listed in the inventory.
3. Record:
   - access date
   - visible page update date, if shown
   - retrieval status
   - review status
   - important rule-family changes
4. Update the matching research file under `references/research/`.
5. If the official wording is clear enough to support a confirmed finding, update the matching rule card and keep `Status: active`.
6. If the page is an index, dynamic shell, login-limited page, or ambiguous source, keep or move it to `Status: needs_review`.
7. Update examples only when a changed rule affects expected output.
8. Run validation and tests:

```bash
python3 content-compliance/scripts/validate_skill.py
python3 -m unittest tests/test_content_compliance_skill.py -v
git diff --check
```

## Public Messaging

Use this phrasing:

```text
这个 Skill 不是拿网上通用说法凑规则，而是官方来源优先：规则卡会追溯到抖音、小红书、巨量引擎、蒲公英、聚光、薯条等公开官方来源。没有确认清楚的来源会标成待复核，不会硬算成确认风险。我也会定期复核这些官方来源，如果规则更新，就同步到规则卡和示例里。
```

Avoid this phrasing:

```text
已经抓完所有官方规则。
自动实时同步所有平台规则。
用了这个就一定能过审。
```

