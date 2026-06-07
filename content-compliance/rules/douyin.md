# Douyin Rule Pack

Rule cards in this file apply to Douyin, DOU+, and OceanEngine contexts. Active rules must cite official source IDs from `../references/sources.md`.

## Rule Card Format

```text
Rule ID:
Platform:
Scope:
Rule Name:
Severity:
Trigger Scenarios:
High-Risk Signals:
Lower-Risk Alternatives:
Review Questions:
Evidence Extraction:
Official Sources:
Source Access Date:
Status:
```

## Rule Cards

```text
Rule ID: douyin.guidance.external_download
Platform: Douyin
Scope: ordinary_post, dou_plus, oceanengine_ad_review
Rule Name: External download or off-platform acquisition guidance
Severity: 4
Trigger Scenarios: Comments asking users to get links, private-message collection, QR-code acquisition, explicit third-party download routes, and visual or spoken instructions that steer users away from the platform.
High-Risk Signals: "comment for link", "private message me", "scan the QR code", "download from this site", "go to GitHub/Gitee and download this package" when framed as an acquisition call-to-action.
Lower-Risk Alternatives: Mention public project names and explain that users should verify official project pages themselves without providing link-claiming, private-message, QR-code, or download prompts.
Review Questions: Does the title, script, subtitle, visual description, pinned comment plan, or promotion plan direct users to obtain materials outside the platform?
Evidence Extraction: Check title, opening, ending CTA, subtitles, visual steps, link descriptions, comments, and private-message prompts.
Official Sources: source.oceanengine.rules_center, source.oceanengine.ad_management
Source Access Date: 2026-06-07
Status: needs_review
```
