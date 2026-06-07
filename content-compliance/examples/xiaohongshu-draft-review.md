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
- Recommendation: 修改后再发布；如计划薯条，应移除评论区领取和私信资源交付表达。
- Risk Score: 6/10
- Score Breakdown:
  - severity: 3, from the single scored active Shutiao stricter-review context rule.
  - confidence: 1.0, because the draft explicitly plans Shutiao promotion and includes resource-claim CTA wording.
  - exposure: 1.5, because the note is planned for paid promotion rather than ordinary posting only.
  - scenario: 1.4, because the issue appears in a confirmed promotion-review scenario.
  - fix_difficulty: 1.5, because the title, body, and cover CTA all need coordinated edits.
  - accumulation: 0; the matched guidance/download rule is `needs_review` and remains a pending-review note, so it is not scored.
- Matched Risk:
  - Rule: xiaohongshu.promotion.shutiao_review_stricter_context
  - Evidence: 明确计划投放薯条，且标题“资料包直接拿”、正文“评论区回复关键词”、首图“评论区领链接”形成资源领取 CTA，进入付费推广审核时会触发更严格的营销质量复核。
  - Safer Revision: 如计划薯条，移除评论区领取、私信交付或资源包直接获取表达，改为介绍项目名称、适用场景和安全校验方法。
- 待复核提示:
  - Rule: xiaohongshu.guidance.external_contact_or_download
  - Note: 这条风险只能作为待复核提示，因为当前规则卡处于 `needs_review`，官方来源覆盖范围或规则解释仍需人工复核。它不支持本示例的 `Risk Score`。

## Disclaimer

免责声明：本报告为 AI 辅助合规参考，依据公开可见的平台规则、整理后的规则卡片以及用户提供的材料生成，不代表抖音、巨量引擎、小红书、蒲公英、聚光、薯条或任何相关平台的官方审核意见。本报告不保证内容发布成功、投放审核通过、获得流量推荐、账号安全或完全符合法律法规。平台规则和审核尺度可能随时间、账号状态、内容上下文和执行口径变化。用户应自行核对最新官方规则，并对内容发布、商业推广、广告合规及相关法律责任负责。涉及法律、医疗、金融、教育、未成年人、食品药品等高风险或强监管领域时，请咨询具备资质的专业人士或平台官方渠道。
