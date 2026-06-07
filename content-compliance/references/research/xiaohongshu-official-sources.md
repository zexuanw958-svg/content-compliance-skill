# Xiaohongshu Official Source Research

## Research Log

| Date | Source ID | What Was Checked | Result |
| --- | --- | --- | --- |
| 2026-06-07 | source.xiaohongshu.pgy_help | Official Pgy help center entry, navigation, and official help article listing | Dynamic page reachable; official menu/doc APIs exposed rule categories, article shortcut IDs, and article update times. |
| 2026-06-07 | source.xiaohongshu.commercial_site | Official Xiaohongshu commercialization product page | Dynamic page reachable; page identifies official commercial products including Pgy, Juguang, and Shutiao, but does not expose detailed compliance rules. |
| 2026-06-07 | source.xiaohongshu.pgy_community_covenant | Pgy article: Xiaohongshu community covenant | Official article reachable through Pgy help detail route and official doc API. |
| 2026-06-07 | source.xiaohongshu.pgy_content_review | Pgy article: content review norms | Official article reachable; covers commercial note review flow and note content standards. |
| 2026-06-07 | source.xiaohongshu.pgy_ad_delivery | Pgy article: advertising delivery norms | Official article reachable; serves as Pgy index to Juguang ad review documents. |
| 2026-06-07 | source.xiaohongshu.pgy_content_cooperation_law | Pgy article: legal requirements for content cooperation notes | Official article reachable; covers prohibited content families for commercial content cooperation. |
| 2026-06-07 | source.xiaohongshu.pgy_external_guidance | Pgy article: Pgy traffic diversion rules | Official article reachable; covers external contact, off-platform transaction, third-party link/code, and app download guidance limits. |
| 2026-06-07 | source.xiaohongshu.pgy_false_low_quality_notice | Pgy article: false and low-quality marketing governance notice | Official article reachable; covers false marketing and low-quality marketing governance. |
| 2026-06-07 | source.xiaohongshu.pgy_low_quality_governance | Pgy article: Xiaohongshu low-quality marketing governance rules | Official article reachable; covers Pgy cooperation note publication and promotion restrictions for low-quality marketing. |
| 2026-06-07 | source.xiaohongshu.pgy_prohibited_industries | Pgy article: prohibited industry rules | Official article reachable; covers categories barred from content cooperation. |
| 2026-06-07 | source.xiaohongshu.pgy_special_industry_access | Pgy article: special industry access rules | Official article reachable; covers regulated industries requiring brand/product qualifications. |
| 2026-06-07 | source.xiaohongshu.pgy_industry_qualification | Pgy article: industry qualification requirements | Official article reachable; covers industry qualification checks and medical-health content restrictions. |
| 2026-06-07 | source.xiaohongshu.pgy_medical_content_control | Pgy article: medical and medicine content control notice | Official article reachable; covers medical, medicine, device, health food, and medical service recommendation limits. |
| 2026-06-07 | source.xiaohongshu.juguang_official_site | Official Juguang platform landing and help entry | Dynamic page reachable; official ad-platform entry, not a detailed rule page. |
| 2026-06-07 | source.xiaohongshu.juguang_content_review_general | Juguang article: content review general rules | Official next_help article reachable; covers ad content review authority, prohibited directory, material rules, and qualification review. |
| 2026-06-07 | source.xiaohongshu.juguang_material_risk_rules | Juguang article: material rule risk explanation | Official help article reachable; covers material qualification, ad identifiability, external guidance, false claims, and consistency requirements. |
| 2026-06-07 | source.xiaohongshu.juguang_crossborder_content_rules | Juguang article: cross-border advertising content rules | Official next_help article reachable; covers cross-border ad content standards and regulated/prohibited categories. |
| 2026-06-07 | source.xiaohongshu.shutiao_prohibited_categories | Shutiao rule article under official Juguang help navigation | Official help article reachable; covers Shutiao prohibited promotion categories. |
| 2026-06-07 | source.xiaohongshu.shutiao_industry_qualification | Shutiao rule article under official Juguang help navigation | Official help article reachable; covers Shutiao industry qualification review. |

## source.xiaohongshu.pgy_help

- Official URL: https://pgy.xiaohongshu.com/help/home
- Page Title: 帮助中心 - 小红书蒲公英
- Access Date: 2026-06-07
- Page Updated Date: not visible; official menu API exposes article update times
- Retrieval Status: dynamic_reachable; official_menu_api_reachable
- Review Status: needs_review
- Covered Rule Families:
  - Pgy source index
  - content review
  - cooperation modes
  - marketing tools
  - rule notices
- Evidence Notes:
  - The official Pgy help center exposes rule navigation covering starter guidance, review norms, cooperation modes, marketing tools, and notices.
  - The help page itself is an index source. It should be used to confirm official article discovery, not as a standalone rule card source unless a rule is visible on the page.
- Rule Cards To Create:
  - none; index source only

## source.xiaohongshu.commercial_site

- Official URL: https://e.xiaohongshu.com/m/product
- Page Title: 商业产品 | 小红书商业化官网
- Access Date: 2026-06-07
- Page Updated Date: not visible
- Retrieval Status: dynamic_reachable
- Review Status: needs_review
- Covered Rule Families:
  - commercialization product index
  - Pgy official product
  - Juguang official product
  - Shutiao official product
- Evidence Notes:
  - The official commercialization product page identifies Xiaohongshu commercial products including Pgy, Juguang, and Shutiao.
  - The page does not expose detailed compliance rules, review standards, or rule update dates. Use it as an official product/source-family anchor only.
- Rule Cards To Create:
  - none; product index only

## source.xiaohongshu.pgy_community_covenant

- Official URL: https://pgy.xiaohongshu.com/help/detail?id=1eda0a065dd894063c2e029a49e8f6a1&userType=4
- Page Title: 小红书社区公约2.0
- Access Date: 2026-06-07
- Page Updated Date: 2026-06-05 22:18:13
- Retrieval Status: dynamic_reachable; official_api_reachable
- Review Status: needs_review
- Covered Rule Families:
  - community covenant
  - sincere sharing
  - originality
  - AI disclosure
  - false persona or fabricated content
  - merchant and brand orderly operation
- Evidence Notes:
  - The covenant frames Xiaohongshu participation around lawful conduct, public morals, sincere sharing, respect for originality, and real identity/content signals.
  - It also gives platform-level expectations for creators, merchants, and brands, including avoiding fake personas, misleading content, and undisclosed AI-generated content when disclosure is required.
- Rule Cards To Create:
  - xiaohongshu.community.sincere_sharing
  - xiaohongshu.community.ai_disclosure

## source.xiaohongshu.pgy_content_review

- Official URL: https://pgy.xiaohongshu.com/help/detail?id=6495c527d1eedeeb48fb18b1f875650e&userType=4
- Page Title: 内容审核规范
- Access Date: 2026-06-07
- Page Updated Date: 2026-06-05 22:08:27
- Retrieval Status: dynamic_reachable; official_api_reachable
- Review Status: needs_review
- Covered Rule Families:
  - note content standards
  - Pgy commercial note review
  - advertising review
  - false or exaggerated claims
  - absolute terms and guaranteed effects
  - external contact
  - regulated industries
- Evidence Notes:
  - Pgy content cooperation notes are subject to review before publication, including safety, content, and customer-review stages. If the note is also used for ad delivery, an additional ad-review stage applies.
  - The article covers risk examples around exaggerated efficacy, guaranteed outcomes, misleading visual effects, absolute language, medical/health claims, external diversion, and industry-specific limits.
- Rule Cards To Create:
  - xiaohongshu.pgy.note_review_flow
  - xiaohongshu.claims.exaggerated_or_guaranteed_effect
  - xiaohongshu.guidance.external_contact_or_download

## source.xiaohongshu.pgy_ad_delivery

- Official URL: https://pgy.xiaohongshu.com/help/detail?id=1562c4328f59ca669d4f3c996ce3df94&userType=4
- Page Title: 广告投放规范
- Access Date: 2026-06-07
- Page Updated Date: 2026-06-05 22:09:10
- Retrieval Status: dynamic_reachable; official_api_reachable
- Review Status: needs_review
- Covered Rule Families:
  - Pgy advertising rules index
  - Juguang advertising review
  - material review
  - industry access
  - cross-border advertising
- Evidence Notes:
  - The Pgy ad-delivery article points official Pgy users toward Juguang advertising review documents for ad content, prohibited promotion categories, material risk, qualification requirements, industry rules, and cross-border advertising.
  - Treat this as a bridge/index source. Detailed rule cards should cite the specific Juguang rule pages recorded separately below.
- Rule Cards To Create:
  - none; advertising rules index only

## source.xiaohongshu.pgy_content_cooperation_law

- Official URL: https://pgy.xiaohongshu.com/help/detail?id=ee4357cb4788db35031f8a6711ecc3a1&userType=4
- Page Title: 内容合作笔记法律法规要求
- Access Date: 2026-06-07
- Page Updated Date: 2026-05-29 17:37:02
- Retrieval Status: dynamic_reachable; official_api_reachable
- Review Status: needs_review
- Covered Rule Families:
  - Pgy content cooperation rules
  - legal prohibited content
  - privacy and personal information
  - violence, pornography, gambling, superstition
  - discrimination and protected groups
  - minors and vulnerable groups
  - social hot-event misuse
- Evidence Notes:
  - The article lists legal and platform-prohibited content categories for content cooperation notes, including misuse of state symbols, privacy leakage, illegal or harmful content, discrimination, and harmful handling of sensitive social events.
  - It should anchor broad legal-prohibition rule cards for commercial content cooperation, while more specific ad or industry rules should cite their dedicated source pages.
- Rule Cards To Create:
  - xiaohongshu.pgy.content_cooperation_legal_prohibitions

## source.xiaohongshu.pgy_external_guidance

- Official URL: https://pgy.xiaohongshu.com/help/detail?id=d2027d1aa0ed8b75e76da4c2ca762e2d&userType=4
- Page Title: 蒲公英导流规则
- Access Date: 2026-06-07
- Page Updated Date: 2026-06-05 22:14:58
- Retrieval Status: dynamic_reachable; official_api_reachable
- Review Status: needs_review
- Covered Rule Families:
  - external contact
  - off-platform guidance
  - third-party links or codes
  - app download guidance
  - off-platform consultation or transaction
- Evidence Notes:
  - The rule prohibits direct and indirect guidance from Pgy content to off-platform contact, consultation, transaction, third-party links, third-party command codes, QR codes, or app downloads.
  - The article states the Pgy diversion rule takes effect from 2025-10-13 and notes that ad-delivered notes should follow ad-review diversion standards.
- Rule Cards To Create:
  - xiaohongshu.guidance.external_contact_or_download

## source.xiaohongshu.pgy_false_low_quality_notice

- Official URL: https://pgy.xiaohongshu.com/help/detail?id=a76a1444fd620a8f78d662829ae736a0&userType=4
- Page Title: 关于虚假、低差营销行为的治理公告
- Access Date: 2026-06-07
- Page Updated Date: 2026-05-29 17:38:10
- Retrieval Status: dynamic_reachable; official_api_reachable
- Review Status: needs_review
- Covered Rule Families:
  - false marketing
  - low-quality marketing
  - fabricated reviews or stories
  - exaggerated efficacy
  - governance consequences
- Evidence Notes:
  - The notice describes Xiaohongshu governance against false marketing and low-quality marketing, including fabricated stories, fake reviews, fake authority signals, exaggerated effects, clickbait, negative-emotion manipulation, vulgar content, forced ad insertion, and repetitive low-value templates.
  - It records a governance start point of 2025-10-01 and indicates platform handling may include visibility, traffic, and content restrictions.
- Rule Cards To Create:
  - xiaohongshu.marketing.false_or_low_quality

## source.xiaohongshu.pgy_low_quality_governance

- Official URL: https://pgy.xiaohongshu.com/help/detail?id=bca8cfe9df181853ae4dfe8216299a3b&userType=4
- Page Title: 小红书低差营销治理规则
- Access Date: 2026-06-07
- Page Updated Date: 2026-06-05 22:08:28
- Retrieval Status: dynamic_reachable; official_api_reachable
- Review Status: needs_review
- Covered Rule Families:
  - low-quality marketing rules
  - Pgy cooperation note review
  - commercial delivery restrictions
  - Shutiao promotion restrictions
- Evidence Notes:
  - The rule requires creators and commercial partners to keep marketing content sincere, objective, and useful rather than low-quality or misleading.
  - Low-quality marketing in Pgy cooperation notes can block publication and can also make notes ineligible for commercial delivery or Shutiao promotion. A linked external example document was visible, but it was not recorded as a formal source because it is not an official Xiaohongshu/Pgy/Juguang/Shutiao page.
- Rule Cards To Create:
  - xiaohongshu.marketing.low_quality_commercial_content

## source.xiaohongshu.pgy_prohibited_industries

- Official URL: https://pgy.xiaohongshu.com/help/detail?id=78595374111b88b371ab36e69dd4be80&userType=4
- Page Title: 禁入行业规则
- Access Date: 2026-06-07
- Page Updated Date: 2026-05-29 17:37:40
- Retrieval Status: dynamic_reachable; official_api_reachable
- Review Status: needs_review
- Covered Rule Families:
  - prohibited industries
  - content cooperation bans
  - regulated products and services
  - illegal or high-risk services
- Evidence Notes:
  - The article lists product and service categories barred from Pgy content cooperation, including gambling, drugs, illegal medical or health services, counterfeit products, illegal education offerings, K12 subject training, franchise/investment solicitation, unlawful network services, illegal finance, dangerous goods, and privacy-invasive tools.
  - Some linked attachments or documents were visible from the official article context but were not separately reviewed as standalone sources in this task.
- Rule Cards To Create:
  - xiaohongshu.pgy.prohibited_industries

## source.xiaohongshu.pgy_special_industry_access

- Official URL: https://pgy.xiaohongshu.com/help/detail?id=1d0163a46f5c32bb139e46637909ed0a&userType=4
- Page Title: 特殊行业准入规则
- Access Date: 2026-06-07
- Page Updated Date: 2026-06-02 04:12:58
- Retrieval Status: dynamic_reachable; official_api_reachable
- Review Status: needs_review
- Covered Rule Families:
  - regulated industry rules
  - special industry access
  - brand qualification
  - product qualification
- Evidence Notes:
  - The article allows content cooperation in listed special industries only when required brand, business, product, or professional qualifications are complete.
  - Covered examples include medical and health-related categories, special cosmetics, education, business services, pets and veterinary services, finance, games, and legal services.
- Rule Cards To Create:
  - xiaohongshu.pgy.special_industry_access

## source.xiaohongshu.pgy_industry_qualification

- Official URL: https://pgy.xiaohongshu.com/help/detail?id=e0cbd1954fe7364ea0201ba2099affdf&userType=4
- Page Title: 行业资质要求
- Access Date: 2026-06-07
- Page Updated Date: 2026-05-29 17:34:05
- Retrieval Status: dynamic_reachable; official_api_reachable
- Review Status: needs_review
- Covered Rule Families:
  - industry qualification
  - medical and health knowledge cooperation
  - professional qualification
  - treatment-effect or efficacy claims
- Evidence Notes:
  - The article records qualification expectations for industries that require proof before content cooperation can proceed.
  - For medical-health knowledge cooperation, it restricts use of endorsers, doctors, patients, or other recommendation/proof signals, and it limits unqualified services/products, false or exaggerated effect claims, treatment promises, and irregular medical terminology.
- Rule Cards To Create:
  - xiaohongshu.pgy.medical_health_qualification

## source.xiaohongshu.pgy_medical_content_control

- Official URL: https://pgy.xiaohongshu.com/help/detail?id=6f23bc23acfe5edf82c060b3f72bb773&userType=4
- Page Title: 关于蒲公英加强对医疗医药领域内容管控的公告
- Access Date: 2026-06-07
- Page Updated Date: 2026-06-02 16:08:13
- Retrieval Status: dynamic_reachable; official_api_reachable
- Review Status: needs_review
- Covered Rule Families:
  - regulated industry rules
  - medical and medicine content control
  - drugs and medical devices
  - health foods
  - medical services and medical aesthetics
- Evidence Notes:
  - The notice tightens Pgy controls over medical and medicine-related content.
  - It indicates that Pgy creation content involving medical or medicine products/services should not recommend or prove specific products or services, including drugs, medical devices, health foods, foods for special medical purposes, veterinary drugs, medical services, and medical-aesthetic services.
- Rule Cards To Create:
  - xiaohongshu.pgy.medical_medicine_content_control

## source.xiaohongshu.juguang_official_site

- Official URL: https://ad.xiaohongshu.com/
- Page Title: 小红书聚光-一站式广告投放平台
- Access Date: 2026-06-07
- Page Updated Date: not visible
- Retrieval Status: dynamic_reachable
- Review Status: needs_review
- Covered Rule Families:
  - Juguang advertising platform
  - advertising help center entry
  - commercial delivery product index
- Evidence Notes:
  - The official Juguang landing page identifies the one-stop Xiaohongshu advertising delivery platform and provides access into the official help/rule system.
  - The landing page is not itself a detailed ad-review rule source; cite specific help documents for rule-card evidence.
- Rule Cards To Create:
  - none; platform index only

## source.xiaohongshu.juguang_content_review_general

- Official URL: https://ad.xiaohongshu.com/next_help/docs/8dc5bd9c45c9a90cb9912f3400d43f92
- Page Title: 内容审核规则总则
- Access Date: 2026-06-07
- Page Updated Date: 2026-03-23
- Retrieval Status: dynamic_reachable; official_api_reachable
- Review Status: needs_review
- Covered Rule Families:
  - Juguang advertising review rules
  - prohibited promotion categories
  - material review
  - qualification review
  - advertising law review authority
- Evidence Notes:
  - The rule states Xiaohongshu may review advertising content under applicable advertising law and platform standards, and ads that do not pass review will not be published.
  - It serves as the general Juguang source for prohibited promotion categories, material risk rules, qualification requirements, and related advertising review standards.
- Rule Cards To Create:
  - xiaohongshu.juguang.ad_content_review
  - xiaohongshu.juguang.prohibited_promotion_categories

## source.xiaohongshu.juguang_material_risk_rules

- Official URL: https://ad.xiaohongshu.com/help/docs?id=4305
- Page Title: 聚光平台素材规则风险解读
- Access Date: 2026-06-07
- Page Updated Date: 2025-04-30
- Retrieval Status: dynamic_reachable
- Review Status: needs_review
- Covered Rule Families:
  - Juguang material review
  - commercial disclosure
  - false or exaggerated claims
  - external contact
  - off-platform transaction guidance
  - substantiation and consistency
- Evidence Notes:
  - The article explains that advertising materials should match advertiser and product qualifications, disclose advertising identity clearly enough, support factual claims and data, and keep material, account, and landing-page information consistent.
  - It also flags risk around false or exaggerated claims, absolute language, missing third-party authorization, inadequate safety warnings, and guidance to off-platform contact or transactions.
- Rule Cards To Create:
  - xiaohongshu.juguang.material_risk_review
  - xiaohongshu.disclosure.ad_identifiability
  - xiaohongshu.guidance.off_platform_transaction

## source.xiaohongshu.juguang_crossborder_content_rules

- Official URL: https://ad.xiaohongshu.com/next_help/docs/be8301efc43f80ebaa4fd8068307cd1d
- Page Title: 跨境广告内容规范
- Access Date: 2026-06-07
- Page Updated Date: 2026-04-30
- Retrieval Status: dynamic_reachable; official_api_reachable
- Review Status: needs_review
- Covered Rule Families:
  - cross-border advertising review
  - prohibited categories
  - regulated industry rules
  - cross-border material rules
- Evidence Notes:
  - The rule applies to cross-border advertising scenarios and records category restrictions and content/material requirements for advertisers whose entity or delivery context triggers cross-border review.
  - Use it as the formal source for cross-border Xiaohongshu ad restrictions rather than general Pgy cooperation rules.
- Rule Cards To Create:
  - xiaohongshu.juguang.crossborder_ad_review

## source.xiaohongshu.shutiao_prohibited_categories

- Official URL: https://ad.xiaohongshu.com/help/docs?id=4062
- Page Title: 薯条禁投类目
- Access Date: 2026-06-07
- Page Updated Date: 2025-01-14
- Retrieval Status: dynamic_reachable
- Review Status: needs_review
- Covered Rule Families:
  - Shutiao promotion review
  - prohibited promotion categories
  - regulated industries
  - illegal or high-risk products and services
- Evidence Notes:
  - The official Juguang help navigation exposes this Shutiao rule page under Shutiao rules.
  - The article lists categories that cannot be promoted through Shutiao, including medical categories, high-risk education, business services, franchise/investment solicitation, counterfeit goods, restricted food categories, adult-related products, dangerous chemicals, high-risk finance, illegal services, and privacy-invasive tools. It notes that actual review results follow system display.
- Rule Cards To Create:
  - xiaohongshu.shutiao.prohibited_categories

## source.xiaohongshu.shutiao_industry_qualification

- Official URL: https://ad.xiaohongshu.com/help/docs?id=3824
- Page Title: 薯条-行业资质规范
- Access Date: 2026-06-07
- Page Updated Date: 2025-01-14
- Retrieval Status: dynamic_reachable
- Review Status: needs_review
- Covered Rule Families:
  - Shutiao promotion review
  - industry qualification
  - advertising law review authority
  - regulated industry rules
- Evidence Notes:
  - The article states Xiaohongshu reviews Shutiao notes as the publisher under advertising-law and platform requirements, and unapproved Shutiao notes will not be published.
  - It records qualification expectations across industries such as education, legal services, business services, safety/security, network services, local life services, pets, finance, and real estate.
- Rule Cards To Create:
  - xiaohongshu.shutiao.industry_qualification_review
