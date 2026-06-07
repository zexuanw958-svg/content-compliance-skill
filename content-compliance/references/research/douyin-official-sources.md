# Douyin Official Source Research

## Research Log

| Date | Source ID | What Was Checked | Result |
| --- | --- | --- | --- |
| 2026-06-07 | source.douyin.safety_center | CDP-rendered Douyin Safety and Trust Center home page | Dynamic page reachable; page update date not visible |
| 2026-06-07 | source.douyin.safety_governance | CDP-rendered safety/governance route from 95152.douyin.com | Dynamic page reachable; community and safety rule families visible |
| 2026-06-07 | source.douyin.creator_values | CDP-rendered trust/creator-values route from 95152.douyin.com | Dynamic page reachable; creator value and originality families visible |
| 2026-06-07 | source.douyin.douplus_official_site | CDP-rendered DOU+ official site | Dynamic page reachable; DOU+ product capabilities and official course families visible |
| 2026-06-07 | source.oceanengine.rules_center | OceanEngine support rule-center page and official loader JSON | Dynamic page reachable; official rule tree contains admission, qualification, content, governance, industry, and publication-change categories |
| 2026-06-07 | source.oceanengine.account_opening | OceanEngine support content 128059 | Dynamic page reachable; visible update time recorded |
| 2026-06-07 | source.oceanengine.ad_management | OceanEngine support content 130539 | Dynamic page reachable; visible update time recorded |
| 2026-06-07 | source.oceanengine.material_review_general | OceanEngine support content 128061 | Dynamic page reachable; title/update visible, imported document body needs further review |
| 2026-06-07 | source.oceanengine.app_miniprogram_business_norm | OceanEngine support content 137616 | Dynamic page reachable; app/miniprogram advertising behavior rules visible |
| 2026-06-07 | source.oceanengine.financial_industry_review | OceanEngine support content 128084 | Dynamic page reachable; financial regulated-industry ad review rules visible |
| 2026-06-07 | source.oceanengine.industry_targeted_access | OceanEngine support content 145159 | Dynamic page reachable; title/update visible, imported document body needs further review |

## source.douyin.safety_center

- Official URL: https://95152.douyin.com/
- Page Title: 抖音安全与信任中心
- Access Date: 2026-06-07
- Page Updated Date: not visible
- Retrieval Status: dynamic_reachable
- Review Status: needs_review
- Covered Rule Families:
  - safety/trust center
  - community rules entry
  - platform governance reports
  - user service and reporting channels
- Evidence Notes:
  - The home page presents the Safety and Trust Center as Douyin's central official portal for transparency, safety governance, services, and trust-building.
  - The rendered page exposes navigation to information transparency, community conventions, community advocacy, and user-service sections.
  - It also links official footer channels including user service agreements, privacy policy, account recovery, advertising delivery, harmful-content reporting, and illegal-content reporting.
- Rule Cards To Create:
  - douyin.community.source_portal
  - douyin.safety.reporting_channels

## source.douyin.safety_governance

- Official URL: https://95152.douyin.com/safety
- Page Title: 抖音安全与信任中心
- Access Date: 2026-06-07
- Page Updated Date: not visible
- Retrieval Status: dynamic_reachable
- Review Status: needs_review
- Covered Rule Families:
  - community rules
  - safety/trust rules
  - hot-topic governance
  - cyberbullying governance
  - AIGC governance guidance
- Evidence Notes:
  - Route checked: `/safety`; visible page heading: `安全`.
  - The page frames Douyin safety governance as ongoing improvement of community rules and risk-governance capability.
  - It lists official rule families for community self-discipline, hot-topic and account governance, AI truth-seeking, cyberbullying governance, governance disclosure, misinformation, and AIGC guidance.
  - No page-level updated date was visible in the rendered DOM.
- Rule Cards To Create:
  - douyin.community.self_discipline
  - douyin.safety.hot_topic_account_governance
  - douyin.safety.aigc_guidance

## source.douyin.creator_values

- Official URL: https://95152.douyin.com/trust
- Page Title: 抖音安全与信任中心
- Access Date: 2026-06-07
- Page Updated Date: not visible
- Retrieval Status: dynamic_reachable
- Review Status: needs_review
- Covered Rule Families:
  - creator rules
  - originality
  - high-quality content
  - community values
- Evidence Notes:
  - Route checked: `/trust`; visible page heading: `信任`.
  - The rendered page states Douyin encourages high-quality and original content and ties creator behavior to positive social value.
  - Visible sections cover community values, originality encouragement, and high-quality content incentives.
  - The page is a high-level creator-values source; it should not be treated as a detailed enforcement rule until linked article pages are traversed.
- Rule Cards To Create:
  - douyin.creator.originality
  - douyin.creator.quality_content

## source.douyin.douplus_official_site

- Official URL: https://doujia.douyin.com/
- Page Title: DOU+官网
- Access Date: 2026-06-07
- Page Updated Date: not visible
- Retrieval Status: dynamic_reachable
- Review Status: needs_review
- Covered Rule Families:
  - DOU+ promotion rules
  - DOU+ promotion goals
  - creator promotion
  - customer acquisition
  - live-room and product promotion
- Evidence Notes:
  - The official DOU+ site describes DOU+ as a promotion product for account growth, customer acquisition, product traffic, and live-room promotion.
  - The rendered page lists official courses including DOU+ introduction, quick-start methods, DOU+ specification guidance, advanced techniques, and DOU+ web usage.
  - It mentions DOU+ specification guidance as audit and safety guidance, but the page itself is mainly product/learning navigation rather than a detailed rule document.
- Rule Cards To Create:
  - douyin.douplus.promotion_scope
  - douyin.douplus.audit_and_safety_review

## source.oceanengine.rules_center

- Official URL: https://support.oceanengine.com/support/content/6503488514?graphId=514&mappingType=1&spaceId=171&visitor_source_app_id=171
- Page Title: 巨量营销规则中心法律法规及平台规则
- Access Date: 2026-06-07
- Page Updated Date: not visible; official loader graph modifyTime is 2023-05-22
- Retrieval Status: dynamic_reachable
- Review Status: needs_review
- Covered Rule Families:
  - advertising review
  - account opening
  - qualification review
  - governance rules
  - regulated industries
  - rule changes and public notices
- Evidence Notes:
  - The rendered rule center and official loader JSON expose a rule tree covering admission rules, qualification rules, content rules, governance rules, other rules, industry norms, case guidance, and rule-change announcements.
  - The tree revealed concrete official content IDs later recorded as separate source rows, including account opening, material review, APP/miniprogram business behavior, financial industry review, and targeted industry admission.
  - This source is best used as an index and source-discovery anchor, not as a standalone rule card source.
- Rule Cards To Create:
  - none; use as official source index only

## source.oceanengine.account_opening

- Official URL: https://support.oceanengine.com/support/content/128059?graphId=514&spaceId=171
- Page Title: 开户总则
- Access Date: 2026-06-07
- Page Updated Date: 2026-01-14 19:01:59
- Retrieval Status: dynamic_reachable
- Review Status: needs_review
- Covered Rule Families:
  - account opening rules
  - customer qualification
  - delivery material definitions
  - landing-page definitions
- Evidence Notes:
  - The page states that OceanEngine formulates account-opening and delivery-review norms under advertising-law and related legal requirements.
  - It defines customer qualification, delivery materials, special delivery qualifications, and landing pages as concepts relevant to account and material review.
  - It also says the norms may be adjusted as laws, policies, and market conditions change.
- Rule Cards To Create:
  - douyin.ad.account_opening_qualification
  - douyin.ad.landing_page_review_basis

## source.oceanengine.ad_management

- Official URL: https://support.oceanengine.com/support/content/130539
- Page Title: 巨量引擎-广告投放管理规范
- Access Date: 2026-06-07
- Page Updated Date: 2022-12-08 20:31:19
- Retrieval Status: dynamic_reachable
- Review Status: needs_review
- Covered Rule Families:
  - ad delivery management
  - advertising review
  - external guidance
  - app/download risk
  - personal social-account acquisition
  - violation handling and appeal
- Evidence Notes:
  - The page applies to OceanEngine products including Douyin and to advertisers using OceanEngine delivery systems.
  - It classifies cooperation behavior and promotion behavior violations, including risks from ad materials, landing pages, secondary jumps, private messages, customer service, comments, apps, mini programs, and interactive materials.
  - It includes examples of high-risk promotion categories such as illegal products/services, false promotion, app-download violations, personal social-account acquisition, and review-evasion behavior.
- Rule Cards To Create:
  - douyin.guidance.external_download
  - douyin.ad.personal_social_account_acquisition
  - douyin.ad.review_evasion

## source.oceanengine.material_review_general

- Official URL: https://support.oceanengine.com/support/content/128061?graphId=514&spaceId=171
- Page Title: 素材计划通用审核规范
- Access Date: 2026-06-07
- Page Updated Date: 2026-01-15 01:56:48
- Retrieval Status: dynamic_reachable
- Review Status: needs_review
- Covered Rule Families:
  - advertising review
  - material-plan review
  - content-control rules
- Evidence Notes:
  - The official rule-center tree places this page under content rules, audit rules, and content-control norms.
  - The rendered page and official loader exposed title and updated date, but the imported Feishu document body did not provide stable text during this pass.
  - Use this row as a confirmed official source placeholder until the full document body can be reviewed through the document component.
- Rule Cards To Create:
  - douyin.ad.material_plan_general_review

## source.oceanengine.app_miniprogram_business_norm

- Official URL: https://support.oceanengine.com/support/content/137616?graphId=514&spaceId=171
- Page Title: 互联网应用程序（APP/小程序等）营商行为规范 V1.0
- Access Date: 2026-06-07
- Page Updated Date: 2026-01-15 16:57:04
- Retrieval Status: dynamic_reachable
- Review Status: needs_review
- Covered Rule Families:
  - external guidance
  - off-platform guidance
  - app and mini-program promotion
  - user-rights protection
  - misleading click/jump behavior
- Evidence Notes:
  - The page applies to customers using OceanEngine products for APP, mini-program, and similar internet-application delivery.
  - It requires application content, delivery behavior, and advertising interactions to protect user rights and platform order.
  - It specifically addresses third-party jump disclosure, misleading click behavior, content/promotion inconsistency, automatic download or jump guidance, and insufficient disclosure around paid or authorized functions.
- Rule Cards To Create:
  - douyin.guidance.external_download
  - douyin.ad.third_party_jump_disclosure
  - douyin.ad.app_promotion_consistency

## source.oceanengine.financial_industry_review

- Official URL: https://support.oceanengine.com/support/content/128084?graphId=514&spaceId=171
- Page Title: 金融行业审核规则
- Access Date: 2026-06-07
- Page Updated Date: 2026-01-15 16:28:44
- Retrieval Status: dynamic_reachable
- Review Status: needs_review
- Covered Rule Families:
  - regulated industries
  - financial advertising
  - required qualifications
  - risk-disclosure prompts
  - prohibited financial claims
- Evidence Notes:
  - The page records financial-industry advertising review requirements for insurance, loans, banking, securities, funds, futures, auctions, payment software, and other financial activities.
  - It requires appropriate licenses or permits for relevant financial products and services.
  - It also records risk-prompt, rate-disclosure, product-name, lender-name, and no-guaranteed-return style requirements for financial materials.
- Rule Cards To Create:
  - douyin.ad.financial_qualification
  - douyin.ad.financial_risk_prompt
  - douyin.ad.no_guaranteed_financial_return

## source.oceanengine.industry_targeted_access

- Official URL: https://support.oceanengine.com/support/content/145159?graphId=514&spaceId=171
- Page Title: 巨量营销行业定向准入规则
- Access Date: 2026-06-07
- Page Updated Date: 2026-05-19 15:12:49
- Retrieval Status: dynamic_reachable
- Review Status: needs_review
- Covered Rule Families:
  - regulated industries
  - targeted industry admission
  - account opening rules
  - pre-delivery admission control
- Evidence Notes:
  - The official rule-center tree places this page under admission rules and targeted admission industries.
  - The rendered page and loader exposed title and updated date, but the imported document body did not provide stable text during this pass.
  - Treat this as a confirmed official source for the existence and metadata of targeted industry admission rules; detailed rule extraction needs a follow-up traversal.
- Rule Cards To Create:
  - douyin.ad.targeted_industry_access
