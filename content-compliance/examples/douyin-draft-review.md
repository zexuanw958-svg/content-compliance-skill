# Douyin Draft Review Example

## Input

```text
平台：抖音
阶段：成稿
标题：国产模型接入 Codex，保姆级教程
口播稿：我会教你下载两个开源项目，评论区拿链接。
画面描述：展示第三方下载落地页、下载按钮、字幕提示“评论区拿链接”。
是否计划投放：巨量引擎广告
```

## Expected Review Shape

- Platform: Douyin
- Phase: draft_review
- Recommendation: 修改后再投放；如计划巨量引擎广告，不建议保留“评论区拿链接”和直接下载引导。
- Risk Score: 7/10
- Overall Safety Score: 3/10
- Risk Bar: 7/10 🟩🟩🟩🟩🟨🟨🟥🟥🟥🟥 (current: 7, high-risk zone)
- Safety Bar: 3/10 🟥🟥🟥⬜⬜⬜⬜⬜⬜⬜
- Score Breakdown:
  - severity: 4, based on the strongest active OceanEngine ad-review guidance risk.
  - confidence: 1.0, because the draft explicitly says it will use OceanEngine ads and includes download/link-acquisition wording.
  - exposure: 1.2, because this is pre-publication ad material with planned paid delivery.
  - scenario: 1.2, because the risk is in a confirmed ad-review context.
  - fix_difficulty: 1.5, because title, 口播, 字幕, and visual landing-page frames all need coordinated revision.
  - accumulation: +0.75 for one additional distinct severity-4 active acquisition-path risk; no needs_review rule is scored.
- Layer Safety Dashboard:
  - topic: 8/10 🟩🟩🟩🟩🟩🟩🟩🟩⬜⬜, technical education topic but tied to tool access.
  - title_or_cover: 7/10 🟨🟨🟨🟨🟨🟨🟨⬜⬜⬜, tutorial framing is acceptable but may imply resource acquisition.
  - script_or_oral_wording: 5/10 🟨🟨🟨🟨🟨⬜⬜⬜⬜⬜, says to download projects.
  - visual_or_subtitle: 3/10 🟥🟥🟥⬜⬜⬜⬜⬜⬜⬜, shows third-party download page and button.
  - external_guidance_download_comment_private_message_or_qr: 2/10 🟥🟥⬜⬜⬜⬜⬜⬜⬜⬜, uses comments as link-acquisition path.
  - promotion_or_ad_review: 3/10 🟥🟥🟥⬜⬜⬜⬜⬜⬜⬜, planned OceanEngine delivery makes review stricter.
  - regulated_industry: 10/10 🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩, no regulated-industry signal.
- Weakest Areas:
  - external_guidance_download_comment_private_message_or_qr: 2/10. Remove “评论区拿链接” and avoid using comments, private messages, or customer service as the access path.
  - visual_or_subtitle: 3/10. Remove third-party download-page frames and download-button closeups from ad material.
  - promotion_or_ad_review: 3/10. Re-review all copy and landing paths before OceanEngine delivery.
- Matched Risks:
  - Rule: douyin.guidance.external_download
  - Official Source: source.oceanengine.ad_management, source.oceanengine.app_miniprogram_business_norm
  - Evidence: 计划巨量引擎广告投放，口播“下载两个开源项目”，画面展示第三方下载落地页和下载按钮。
  - Safer Revision: 保持广告素材与落地页一致，避免把第三方下载路径作为主要行动引导。
  - Rule: douyin.guidance.comment_or_private_message_acquisition
  - Official Source: source.oceanengine.ad_management
  - Evidence: 字幕提示“评论区拿链接”。
  - Safer Revision: 不把评论区、私信、客服或个人账号作为获取链接、资料或权益的行动路径。

## Disclaimer

免责声明：本报告为 AI 辅助合规参考，依据公开可见的平台规则、整理后的规则卡片以及用户提供的材料生成，不代表抖音、巨量引擎、小红书、蒲公英、聚光、薯条或任何相关平台的官方审核意见。本报告不保证内容发布成功、投放审核通过、获得流量推荐、账号安全或完全符合法律法规。平台规则和审核尺度可能随时间、账号状态、内容上下文和执行口径变化。用户应自行核对最新官方规则，并对内容发布、商业推广、广告合规及相关法律责任负责。涉及法律、医疗、金融、教育、未成年人、食品药品等高风险或强监管领域时，请咨询具备资质的专业人士或平台官方渠道。
