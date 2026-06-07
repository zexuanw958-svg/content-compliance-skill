# Xiaohongshu Rule Pack

Rule cards in this file apply to Xiaohongshu ordinary notes, Shutiao, Pgy, and Juguang contexts. Active rules must cite official source IDs from `../references/sources.md`.

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
Rule ID: xiaohongshu.topic.regulated_industry
Platform: Xiaohongshu
Scope: pgy_content_cooperation, shutiao_promotion_review, juguang_ad_review
Rule Name: Regulated-industry topic in commercial cooperation, promotion, or ad review
Severity: 5
Trigger Scenarios: Topics involving medical and health services, medicines, medical devices, health foods, education, finance, legal services, games, pets or veterinary services, franchise or investment solicitation, dangerous goods, privacy-invasive tools, or other regulated products and services when the plan includes Pgy cooperation, Shutiao promotion, or Juguang ad delivery.
High-Risk Signals: Regulated category without qualification context, product or service recommendation in a restricted industry, medical or treatment-effect claims, investment or franchise lead acquisition, illegal or high-risk service promotion, or a topic brief that turns education into commercial solicitation.
Lower-Risk Alternatives: Keep ordinary educational discussion separate from promotion, verify whether the category is prohibited or qualification-gated before cooperation or boosting, remove lead-acquisition framing, and rerun review when a promotion plan is added.
Review Questions: Does the topic involve a category that is prohibited, qualification-gated, or specially reviewed for Pgy, Shutiao, or Juguang delivery?
Evidence Extraction: Check topic brief, product or service category, intended brand cooperation, promotion plan, ad account/category, qualification materials, CTA, landing page, and any health, education, finance, legal, game, pet, or investment-related claims.
Official Sources: source.xiaohongshu.pgy_prohibited_industries, source.xiaohongshu.pgy_special_industry_access, source.xiaohongshu.pgy_industry_qualification, source.xiaohongshu.shutiao_prohibited_categories, source.xiaohongshu.shutiao_industry_qualification, source.xiaohongshu.juguang_content_review_general
Source Access Date: 2026-06-07
Status: active
```

```text
Rule ID: xiaohongshu.title.exaggeration_or_false_marketing
Platform: Xiaohongshu
Scope: pgy_content_cooperation, pgy_marketing_governance, shutiao_or_commercial_delivery_review, juguang_ad_review
Rule Name: Exaggerated title, false marketing, or unverifiable effect claim
Severity: 4
Trigger Scenarios: Titles, covers, captions, or promotional copy use absolute language, guaranteed effects, fake authority, fabricated reviews, clickbait, or claims that overstate product, service, tool, health, business, or productivity outcomes.
High-Risk Signals: "guaranteed", "100% effective", "officially certified" without basis, fake expert or institution endorsement, fabricated user stories, exaggerated before/after effects, negative-emotion clickbait, or a title promising a result the material cannot substantiate.
Lower-Risk Alternatives: Describe the tested scenario, method, limits, and evidence; avoid guaranteed or absolute outcomes; separate personal experience from product promises; and keep title, cover, copy, account, and landing-page claims consistent.
Review Questions: Does the title or cover make a marketing claim that is exaggerated, unverifiable, fabricated, absolute, or inconsistent with the supporting material?
Evidence Extraction: Check title, cover text, first paragraph, captions, product screenshots, before/after visuals, cited qualifications, data claims, ad material, landing page, and any Shutiao or commercial-delivery variant.
Official Sources: source.xiaohongshu.pgy_content_review, source.xiaohongshu.pgy_false_low_quality_notice, source.xiaohongshu.pgy_low_quality_governance, source.xiaohongshu.juguang_material_risk_rules
Source Access Date: 2026-06-07
Status: active
```

```text
Rule ID: xiaohongshu.guidance.external_contact_or_download
Platform: Xiaohongshu
Scope: pgy_content_cooperation, juguang_ad_review, commercial_or_promotion_review_context
Rule Name: External contact, private acquisition, off-platform consultation, or download guidance
Severity: 4
Trigger Scenarios: Pgy content, commercial notes, ad materials, or promotion-review drafts ask users to obtain links, files, consultations, transactions, benefits, or app downloads through comments, private messages, QR codes, third-party links, command codes, external websites, or off-platform apps.
High-Risk Signals: "comment to get", "private message for resource", "scan code to consult", third-party link or code, off-platform transaction path, external app download, customer-service diversion, or disguised contact instructions in copy or visuals.
Lower-Risk Alternatives: Name public resources without making comments, private messages, scans, external apps, or off-platform contact the acquisition path; explain selection criteria, setup steps, and safety checks inside the note.
Review Questions: Does the content turn platform interaction into an off-platform contact, download, consultation, transaction, or resource-delivery path?
Evidence Extraction: Check title, body, cover text, image overlays, captions, comment plan, private-message prompts, QR codes, third-party codes, app-download wording, landing page, and promotion copy.
Official Sources: source.xiaohongshu.pgy_external_guidance, source.xiaohongshu.pgy_content_review, source.xiaohongshu.juguang_material_risk_rules
Source Access Date: 2026-06-07
Status: needs_review
Evidence Limitation: Official evidence directly supports Pgy commercial content and Juguang ad-material review; application to every ordinary note or all Shutiao-only contexts should be rechecked against current platform execution.
```

```text
Rule ID: xiaohongshu.visual.qr_code_or_contact_information
Platform: Xiaohongshu
Scope: pgy_content_cooperation, juguang_ad_review
Rule Name: Visual QR code, contact information, or off-platform acquisition signal
Severity: 4
Trigger Scenarios: Covers, screenshots, overlays, screen recordings, captions, or product images show QR codes, phone numbers, social handles, third-party command codes, external URLs, customer-service contact, or visual instructions for off-platform acquisition.
High-Risk Signals: QR-code overlays, visible WeChat or other social handles, phone numbers, third-party links or command codes, "scan to consult", "add for quote", "DM for link", app-download screenshots, or contact details embedded in images.
Lower-Risk Alternatives: Remove scannable/contact information and visual acquisition paths; describe the resource, product, or method in platform-native wording; use neutral screenshots that do not expose contact or transaction instructions.
Review Questions: Does any visual frame reveal or imply a contact, scan, code, link, app-download, consultation, or transaction path outside the platform?
Evidence Extraction: Check cover image, image text, screenshots, watermarks, subtitles, video frames, captions, product images, landing-page captures, and ad material variants.
Official Sources: source.xiaohongshu.pgy_external_guidance, source.xiaohongshu.juguang_material_risk_rules
Source Access Date: 2026-06-07
Status: active
```

```text
Rule ID: xiaohongshu.commerce.undisclosed_commercial_content
Platform: Xiaohongshu
Scope: juguang_ad_review, pgy_content_cooperation, brand_or_merchant_commercial_context
Rule Name: Undisclosed commercial content or unclear advertising identity
Severity: 4
Trigger Scenarios: Commercial, brand, merchant, cooperation, or advertising materials present a product, service, benefit, or endorsement as purely personal sharing while hiding sponsorship, advertiser identity, ad nature, or material connection.
High-Risk Signals: Commercial benefit or brand cooperation not apparent to viewers, ad material that lacks clear advertising identity, disguised product recommendation, inconsistent account/product/landing-page information, fake persona, fabricated experience, or brand/merchant operation that undermines sincere sharing.
Lower-Risk Alternatives: Make the commercial nature and material relationship clear where required, keep advertiser, account, product, and landing-page information consistent, avoid fake personas or fabricated usage stories, and distinguish personal experience from sponsored or advertising claims.
Review Questions: Would a viewer or reviewer understand the content's commercial or advertising nature and the relationship between the creator, brand, product, and landing page?
Evidence Extraction: Check cooperation brief, brand mentions, product benefits, creator compensation context, ad labels, account identity, merchant/brand identity, landing page, material consistency, and claims that appear personal but are commercially directed.
Official Sources: source.xiaohongshu.juguang_material_risk_rules, source.xiaohongshu.pgy_community_covenant, source.xiaohongshu.pgy_content_review
Source Access Date: 2026-06-07
Status: needs_review
Evidence Limitation: Official evidence clearly supports Juguang ad identifiability and commercial-material consistency; ordinary-note sponsorship disclosure coverage was not fully established in the collected sources.
```

```text
Rule ID: xiaohongshu.promotion.shutiao_review_stricter_context
Platform: Xiaohongshu
Scope: shutiao_promotion_review
Rule Name: Shutiao promotion triggers stricter category, qualification, and marketing-quality review
Severity: 3
Trigger Scenarios: A note that may be low risk as ordinary education or sharing is planned for Shutiao promotion, commercial delivery, traffic boosting, lead acquisition, or product/service promotion.
High-Risk Signals: "plan to use Shutiao", paid promotion objective, regulated category, missing industry qualification, prohibited promotion category, low-quality marketing, false or exaggerated claim, resource-claim CTA, or content rewritten from neutral tutorial into acquisition funnel.
Lower-Risk Alternatives: Rerun review when Shutiao is added, remove acquisition CTAs and exaggerated claims, verify prohibited category and qualification rules, keep the note useful and objective, and avoid promoting restricted products or services.
Review Questions: Does the planned Shutiao use introduce a paid-promotion review context with category, qualification, or low-quality-marketing restrictions?
Evidence Extraction: Check promotion plan, note category, product or service involved, qualification materials, title and cover variants, commercial-delivery objective, CTA, landing page, and any regulated-industry signals.
Official Sources: source.xiaohongshu.shutiao_prohibited_categories, source.xiaohongshu.shutiao_industry_qualification, source.xiaohongshu.pgy_low_quality_governance
Source Access Date: 2026-06-07
Status: active
```

```text
Rule ID: xiaohongshu.advertising.qualification_or_industry_restriction
Platform: Xiaohongshu
Scope: juguang_ad_review, shutiao_promotion_review, pgy_content_cooperation
Rule Name: Advertising, promotion, or commercial cooperation qualification and industry restriction
Severity: 5
Trigger Scenarios: Advertising materials, Shutiao notes, Pgy cooperation notes, landing pages, or commercial campaigns involve qualification-gated industries, prohibited categories, special product/service access, regulated claims, or advertiser/material inconsistency.
High-Risk Signals: Missing business, brand, product, or professional qualification; prohibited promotion category; regulated industry ad without access proof; medical, finance, education, legal, game, pet, real-estate, safety/security, or business-service claims without qualification context; landing page inconsistent with account or material.
Lower-Risk Alternatives: Confirm industry access and qualifications before cooperation or promotion, align material with approved account/product scope, remove claims outside qualification coverage, add required warnings or disclosures, and avoid promoting prohibited categories.
Review Questions: Does the campaign require advertiser, brand, product, professional, or industry-specific qualification before Pgy cooperation, Shutiao promotion, or Juguang ad review?
Evidence Extraction: Check advertiser entity, account materials, brand authorization, product qualification, professional qualification, industry category, campaign objective, note copy, ad material, landing page, and any cross-stage review feedback.
Official Sources: source.xiaohongshu.juguang_content_review_general, source.xiaohongshu.juguang_material_risk_rules, source.xiaohongshu.shutiao_industry_qualification, source.xiaohongshu.pgy_special_industry_access, source.xiaohongshu.pgy_industry_qualification
Source Access Date: 2026-06-07
Status: active
```
