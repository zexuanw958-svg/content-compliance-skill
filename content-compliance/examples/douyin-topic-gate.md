# Douyin Topic Gate Example

## Input

```text
平台：抖音
阶段：选题
选题：如何把国产模型接入 Codex
是否计划投放：否
```

## Expected Review Shape

- Platform: Douyin
- Phase: topic_gate
- Recommendation: 可继续做，但避免把内容包装成绕过限制、获取资源、领取链接或站外下载教程。
- Risk Score: 2/10
- Overall Safety Score: 9/10
- Risk Bar: 2/10 🟩🟩🟩🟩🟨🟨🟥🟥🟥🟥 (current: 2, low-risk zone)
- Safety Bar: 9/10 🟩🟩🟩🟩🟩🟩🟩🟩🟩⬜
- Score Breakdown:
  - severity: none; no confirmed `Status: active` rule match at topic stage.
  - confidence: no confirmed risk evidence; this is baseline caution.
  - exposure: ordinary topic planning only, with no promotion plan.
  - scenario: minor editorial caution for possible future off-platform acquisition framing, not a confirmed violation.
  - fix_difficulty: low; keep the angle educational and avoid resource-claim CTA wording.
  - accumulation: 0; no active matched risks and no pending-review notes are scored.
- Layer Safety Dashboard:
  - topic: 9/10 🟩🟩🟩🟩🟩🟩🟩🟩🟩⬜, technical education topic.
  - title_or_cover: 8/10 🟩🟩🟩🟩🟩🟩🟩🟩⬜⬜, future title should avoid “领取链接” framing.
  - script_or_oral_wording: 9/10 🟩🟩🟩🟩🟩🟩🟩🟩🟩⬜, no script yet.
  - visual_or_subtitle: 9/10 🟩🟩🟩🟩🟩🟩🟩🟩🟩⬜, no visual risk yet.
  - external_guidance_download_comment_private_message_or_qr: 7/10 🟨🟨🟨🟨🟨🟨🟨⬜⬜⬜, watch for later resource-link guidance.
  - promotion_or_ad_review: 10/10 🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩, no promotion plan.
  - regulated_industry: 10/10 🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩, no regulated-industry signal.
- Weakest Areas:
  - external_guidance_download_comment_private_message_or_qr: 7/10. Do not turn the topic into “comment for link” or “download package” content later.
- Required Checks:
  - The topic itself is technical education.
  - Title and angle must avoid off-platform acquisition guidance.
  - If promotion is planned later, rerun Draft Review with the actual promotion or ad-delivery context.

## Disclaimer

免责声明：本报告为 AI 辅助合规参考，依据公开可见的平台规则、整理后的规则卡片以及用户提供的材料生成，不代表抖音、巨量引擎、小红书、蒲公英、聚光、薯条或任何相关平台的官方审核意见。本报告不保证内容发布成功、投放审核通过、获得流量推荐、账号安全或完全符合法律法规。平台规则和审核尺度可能随时间、账号状态、内容上下文和执行口径变化。用户应自行核对最新官方规则，并对内容发布、商业推广、广告合规及相关法律责任负责。涉及法律、医疗、金融、教育、未成年人、食品药品等高风险或强监管领域时，请咨询具备资质的专业人士或平台官方渠道。
