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
Rule ID: douyin.topic.regulated_industry
Platform: Douyin
Scope: ordinary_post, dou_plus, oceanengine_ad_review
Rule Name: Regulated-industry topic with commercial or promotion context
Severity: 4
Trigger Scenarios: Topics involving finance, insurance, loans, banking, securities, funds, futures, auctions, payment software, or similarly regulated services, especially when the post plans lead acquisition, product promotion, DOU+, or OceanEngine ad delivery.
High-Risk Signals: Promising returns, recommending financial products, soliciting leads, presenting loan or investment services, naming a regulated service without qualification context, or packaging the topic as a business offer.
Lower-Risk Alternatives: Keep ordinary educational discussion neutral, avoid product recommendation or lead acquisition, disclose that regulated services need qualified entities, and rerun review before promotion or advertising.
Review Questions: Is the topic only technical or educational, or does it become a regulated-service promotion, lead funnel, financial recommendation, or ad-delivery plan?
Evidence Extraction: Check topic brief, business model, planned CTA, service category, DOU+ plan, OceanEngine plan, landing page, and any claim about returns, rates, or service availability. Evidence limitation: current official research clearly supports financial and advertising-review contexts, not a complete ordinary-post ban on all regulated-topic discussion.
Official Sources: source.oceanengine.financial_industry_review, source.oceanengine.account_opening
Source Access Date: 2026-06-07
Status: needs_review
```

```text
Rule ID: douyin.title.exaggeration_or_absolute_claim
Platform: Douyin
Scope: ordinary_post, dou_plus, oceanengine_ad_review
Rule Name: Exaggerated or absolute claim in title
Severity: 3
Trigger Scenarios: Titles using absolute, guaranteed, or exaggerated outcomes, especially in commercial, advertising, app-promotion, or regulated-industry contexts.
High-Risk Signals: "guaranteed", "100% works", "zero risk", "must earn", "best in the industry", "officially approved", or similar claims when the reviewed official notes only clearly support false-promotion and financial no-guarantee controls in ad contexts.
Lower-Risk Alternatives: Use measurable, contextual wording, name the scenario being tested, avoid guaranteed outcomes, and separate personal experience from platform, product, or financial promises.
Review Questions: Does the title make an absolute outcome claim that would be hard to verify or that could become false promotion in an ad or regulated-service context?
Evidence Extraction: Check title, cover text, subtitles, promotional copy, landing-page headline, and any title variant prepared for DOU+ or OceanEngine delivery. Evidence limitation: current official research supports false-promotion and financial no-guarantee controls in ad contexts, not a complete ordinary-post title taxonomy.
Official Sources: source.oceanengine.ad_management, source.oceanengine.financial_industry_review
Source Access Date: 2026-06-07
Status: needs_review
```

```text
Rule ID: douyin.guidance.external_download
Platform: Douyin
Scope: oceanengine_ad_review
Rule Name: External download guidance in ad or app/miniprogram delivery
Severity: 4
Trigger Scenarios: OceanEngine ad materials, landing pages, secondary jumps, apps, mini programs, or interactive ad materials guide users to downloads, automatic jumps, undisclosed third-party jumps, or third-party download platforms.
High-Risk Signals: App-download violation, automatic download or jump guidance, undisclosed third-party jump, misleading click-to-download behavior, or ad creative that makes a third-party download path the promoted user action.
Lower-Risk Alternatives: Keep ad creative and landing pages consistent, disclose third-party jumps where required, avoid automatic download guidance, and describe product functions without making unsupported off-platform download steps the user path.
Review Questions: In the ad or app/miniprogram delivery flow, does any material, landing page, secondary jump, app page, mini-program page, or interactive material direct the user into a download or third-party jump path?
Evidence Extraction: Check ad materials, landing pages, secondary jumps, app or mini-program flows, interactive materials, download buttons, jump disclosures, customer-service scripts, and promotion copy.
Official Sources: source.oceanengine.ad_management, source.oceanengine.app_miniprogram_business_norm
Source Access Date: 2026-06-07
Status: active
```

```text
Rule ID: douyin.guidance.comment_or_private_message_acquisition
Platform: Douyin
Scope: oceanengine_ad_review
Rule Name: Comment, private-message, customer-service, or personal-account acquisition in ad review
Severity: 4
Trigger Scenarios: OceanEngine ad materials, landing pages, private messages, customer service, comments, apps, mini programs, or interactive materials use platform interaction or personal social-account acquisition as the path to obtain services, accounts, benefits, links, or materials.
High-Risk Signals: Ad or landing-page prompts to comment for benefits, private-message for materials, contact customer service for access, add a personal social account, or move users into comments/private messages/customer service as the acquisition channel.
Lower-Risk Alternatives: Keep ad interactions transparent and consistent with the approved landing page, avoid personal social-account acquisition, and do not use comments, private messages, or customer service as a hidden delivery path for the promoted benefit.
Review Questions: In the ad or promotion review context, do comments, private messages, customer service, apps, mini programs, or interactive materials become the channel for acquiring the promised service, account, benefit, link, or material?
Evidence Extraction: Check ad materials, landing pages, customer-service scripts, private-message prompts, comment templates, apps, mini programs, interactive materials, personal-account contact prompts, and promotion copy.
Official Sources: source.oceanengine.ad_management
Source Access Date: 2026-06-07
Status: active
```

```text
Rule ID: douyin.visual.qr_code_or_external_link
Platform: Douyin
Scope: ordinary_post, dou_plus, oceanengine_ad_review
Rule Name: Visual QR code, external link, or third-party jump guidance
Severity: 4
Trigger Scenarios: Screenshots, subtitles, overlays, or screen recordings visually guide viewers to scan, click, jump, or download through a third-party path outside the platform.
High-Risk Signals: QR-code overlays, visible external URLs, third-party jump buttons, automatic download prompts, misleading click prompts, or screen-recorded steps that send viewers to outside sites or app stores.
Lower-Risk Alternatives: Remove QR codes and external-link acquisition steps, discuss resource names and safety checks neutrally, and avoid visual instructions that make off-platform acquisition the viewer action.
Review Questions: Does any visual frame, subtitle, screen recording, or landing-page screenshot show an external acquisition, jump, or download path?
Evidence Extraction: Check cover image, overlays, subtitles, screen recordings, link cards, landing pages, app/miniprogram flows, and any DOU+ or OceanEngine creative material. Evidence limitation: current official research clearly supports third-party jumps and download guidance in app/ad contexts; QR-specific ordinary-post evidence still needs follow-up.
Official Sources: source.oceanengine.app_miniprogram_business_norm, source.oceanengine.ad_management
Source Access Date: 2026-06-07
Status: needs_review
```

```text
Rule ID: douyin.promotion.dou_plus_review_stricter_context
Platform: Douyin
Scope: dou_plus, oceanengine_ad_review
Rule Name: DOU+ or promotion context requires stricter review
Severity: 3
Trigger Scenarios: A draft that may be acceptable as ordinary technical education is later planned for DOU+, customer acquisition, product traffic, live-room promotion, or OceanEngine advertising review.
High-Risk Signals: "plan to boost with DOU+", customer acquisition intent, product traffic goals, live-room promotion, landing-page traffic, or changing a neutral tutorial into a promotional funnel.
Lower-Risk Alternatives: Re-run draft review with promotion context, remove acquisition CTAs, verify ad qualifications and landing pages, and keep educational content separate from paid promotion claims.
Review Questions: Has the creator changed the distribution context from ordinary post to paid promotion, traffic acquisition, or ad delivery?
Evidence Extraction: Check promotion plan, DOU+ objective, campaign copy, landing page, customer-acquisition flow, product mentions, and any rewritten title or CTA for paid delivery. Evidence limitation: the DOU+ official source found product and course navigation, but detailed DOU+ audit text was not stable in this research pass.
Official Sources: source.douyin.douplus_official_site, source.oceanengine.ad_management
Source Access Date: 2026-06-07
Status: needs_review
```

```text
Rule ID: douyin.advertising.qualification_or_industry_restriction
Platform: Douyin
Scope: oceanengine_ad_review
Rule Name: Advertising qualification or regulated-industry restriction
Severity: 5
Trigger Scenarios: Advertising, lead acquisition, landing pages, or promotional materials involve regulated products, services, special qualifications, customer qualifications, or industry-specific access requirements.
High-Risk Signals: Financial services without license context, loans or insurance promotion, securities/funds/futures claims, payment software promotion, missing advertiser qualification, missing special delivery qualification, or landing pages inconsistent with account-opening information.
Lower-Risk Alternatives: Confirm advertiser and special-delivery qualifications before promotion, keep materials consistent with approved business scope, add required risk and product disclosures where applicable, and avoid promoting regulated services without qualified entities.
Review Questions: Does the campaign require customer qualification, special delivery qualification, financial license evidence, targeted industry admission, or landing-page consistency before it can be reviewed?
Evidence Extraction: Check advertiser entity, account-opening materials, qualification certificates, business scope, landing page, product category, rate/return claims, risk prompts, and regulated-industry category.
Official Sources: source.oceanengine.account_opening, source.oceanengine.financial_industry_review
Source Access Date: 2026-06-07
Status: active
```
