# Xiaohongshu Draft Review Example

## Input

平台：小红书
阶段：成稿
标题：国产模型接入 Codex，资料包直接拿
正文：评论区回复关键词，我把项目链接发给你。
画面描述：首图写“评论区领链接”，第二张展示下载页面。
是否计划投放：薯条

## Expected Review Shape

- Platform: Xiaohongshu
- Phase: draft_review
- Recommendation: 先人工复核并修改后再发布；如计划薯条，应移除评论区领取和私信资源交付表达。
- Risk Score: 3/10
- Overall Safety Score: 8/10
- Risk Bar: 3/10 🟩🟩🟩🟩🟨🟨🟥🟥🟥🟥 (current: 3, low-risk zone)
- Safety Bar: 8/10 🟩🟩🟩🟩🟩🟩🟩🟩⬜⬜
- Score Breakdown:
  - severity: none; no confirmed `Status: active` rule independently scores the resource-claim wording.
  - confidence: pending-review only; the draft clearly includes resource-claim wording, but the directly relevant guidance/download rule is `needs_review`.
  - exposure: planned paid promotion increases review attention, but exposure is not item-scored without an independently matched active rule.
  - scenario: baseline caution for a draft-review uncertainty with planned Shutiao distribution and pending-review acquisition signals.
  - fix_difficulty: low to medium; title, body, and cover CTA should be edited together before manual review.
  - accumulation: 0; no active matched risks are scored and the pending guidance/download note is excluded from the final score.
- Layer Safety Dashboard:
  - topic: 8/10 🟩🟩🟩🟩🟩🟩🟩🟩⬜⬜, technical education topic but resource framing is emerging.
  - title_or_cover: 6/10 🟨🟨🟨🟨🟨🟨⬜⬜⬜⬜, “资料包直接拿” creates acquisition framing.
  - script_or_oral_wording: 6/10 🟨🟨🟨🟨🟨🟨⬜⬜⬜⬜, comment-keyword delivery needs review.
  - visual_or_subtitle: 5/10 🟨🟨🟨🟨🟨⬜⬜⬜⬜⬜, cover and second image show link/download acquisition.
  - external_guidance_download_comment_private_message_or_qr: 5/10 🟨🟨🟨🟨🟨⬜⬜⬜⬜⬜, pending-review weak area, not a confirmed active-rule score.
  - promotion_or_ad_review: 7/10 🟨🟨🟨🟨🟨🟨🟨⬜⬜⬜, planned Shutiao means manual review is recommended.
  - regulated_industry: 10/10 🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩, no regulated-industry signal.
- Weakest Areas:
  - external_guidance_download_comment_private_message_or_qr: 5/10. Pending-review weak area; remove “评论区回复关键词” and avoid private-message resource delivery.
  - visual_or_subtitle: 5/10. Remove “评论区领链接” cover text and download-page imagery.
- Matched Risks: none confirmed under `Status: active` rules.
- Required Checks:
  - Before scoring a higher risk, verify whether the same evidence independently matches an active Shutiao category, qualification, false-marketing, or low-quality-marketing rule.
  - Do not score the comment/link acquisition concern through the Shutiao context rule unless a directly supported active rule is added.
- 待复核提示:
  - Rule: xiaohongshu.guidance.external_contact_or_download
  - Note: 这条风险只能作为待复核提示，因为当前规则卡处于 `needs_review`，官方来源覆盖范围或规则解释仍需人工复核。它不支持本示例的 `Risk Score`。

## Disclaimer

免责声明：本报告为 AI 辅助合规参考，依据公开可见的平台规则、整理后的规则卡片以及用户提供的材料生成，不代表抖音、巨量引擎、小红书、蒲公英、聚光、薯条或任何相关平台的官方审核意见。本报告不保证内容发布成功、投放审核通过、获得流量推荐、账号安全或完全符合法律法规。平台规则和审核尺度可能随时间、账号状态、内容上下文和执行口径变化。用户应自行核对最新官方规则，并对内容发布、商业推广、广告合规及相关法律责任负责。涉及法律、医疗、金融、教育、未成年人、食品药品等高风险或强监管领域时，请咨询具备资质的专业人士或平台官方渠道。
