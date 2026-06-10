# 内容合规检测 Skill

![内容合规检测 Skill 封面](assets/readme-banner.png)

<p>
  <a href="https://github.com/zexuanw958-svg/content-compliance-skill"><img alt="GitHub 仓库" src="https://img.shields.io/badge/GitHub-content--compliance--skill-24292f?logo=github"></a>
  <img alt="MIT 许可证" src="https://img.shields.io/badge/License-MIT-0A7D5A">
  <img alt="测试通过" src="https://img.shields.io/badge/%E6%B5%8B%E8%AF%95-26%20%E9%A1%B9%E9%80%9A%E8%BF%87-16A34A">
  <img alt="支持平台" src="https://img.shields.io/badge/%E5%B9%B3%E5%8F%B0-%E6%8A%96%E9%9F%B3%20%7C%20%E5%B0%8F%E7%BA%A2%E4%B9%A6-C13584">
  <img alt="智能体运行时" src="https://img.shields.io/badge/Agent-Codex%20%7C%20Claude%20Code%20%7C%20OpenClaw%20%7C%20Hermes%20Agent-475467">
</p>

面向国内中文自媒体创作者的 `SKILL.md` 合规检测工具。它可以在 **Codex / Code X、Claude Code、OpenClaw、Hermes Agent** 等智能体运行时中使用，用来在发布前检查抖音、小红书内容的选题、口播、画面、评论区话术和投放计划，让你在发视频前更有底。

日常唤醒方式：`检测`、`合规检测`、`内容合规检测`、`/检测`、`/content-compliance`。

默认输出简体中文检测报告。除了规则 ID、官方来源 ID、`Status: active` / `Status: needs_review` 这类必要机器标识外，用户可见栏目统一使用中文。

## 为什么更安心

这个 Skill 不是拿网上通用说法凑一套“玄学审核规则”。它采用 **官方来源优先** 的规则整理方式：

- 规则卡追溯到抖音、小红书、巨量引擎、蒲公英、聚光、薯条等公开官方来源。
- 确认风险必须引用 `references/sources.md` 里的官方来源 ID。
- 官方来源解释不够清楚、页面只是索引、动态页面只看到部分信息时，会标成 `Status: needs_review`，不会硬算成确认风险。
- 项目内置 `content-compliance/references/rule-refresh.md` 作为官方来源定期复核流程，用来检查可公开访问的官方规则是否有可见更新，并同步到规则卡、示例和测试。

边界也要说清楚：这不是自动实时同步所有平台规则，也不是平台官方审核工具。它提供的是发布前参考，最终仍以平台官方审核、账号状态、内容上下文和实际执行口径为准。

## 它解决什么问题

自媒体内容的风险通常不是整篇稿子都危险，而是某一个局部突然出问题：

- 选题没问题，但评论区话术写成了“回复关键词领链接”。
- 普通发布风险不高，但一投 DOU+、薯条、蒲公英或巨量引擎，审核尺度立刻变严。
- 口播整体正常，但某一句“下载两个开源项目”叠加“工具地址放评论区”，就容易变成站外引导。
- 标题和封面看着刺激，但可能出现夸大、绝对化、资料领取入口等问题。

这个 Skill 的目标不是替代平台审核，而是在你发布前给出一份可读、可改、可复查的风险体检单。

## 可以检查什么

| 检查模块 | 具体内容 |
| --- | --- |
| 选题检测 | 选题是否适合继续做，是否提前埋下导流、夸大、强监管行业风险 |
| 成稿检测 | 标题、口播、正文、字幕、画面描述、评论区、私信计划 |
| 外部引导 | 评论区拿链接、私信领取、二维码、外链、第三方下载、跳转路径 |
| 投放语境 | DOU+、巨量引擎、薯条、蒲公英、聚光等商业化场景 |
| 强监管提示 | 金融、医疗、教育、食品药品、未成年人等敏感领域 |

## 输出效果预览

```text
建议：普通发布前建议小改；如果计划投放，不建议保留“评论区拿链接”和直接下载引导。

总风险分：3/10
风险条：3/10 🟩🟩🟩⬜⬜⬜⬜⬜⬜⬜（低风险）


最弱风险点：
- 外部引导 / 下载 / 评论区取链接：5/10
  证据：“完整教程和工具地址，我已经放在评论区了。”
  快速改法：改成“工具名称和注意事项我会整理出来，使用前请自行核对官方仓库和安全风险。”
```

评分会拆成两层：

- **总风险分**：1-10，越高越危险。
- **风险条**：填充格数等于总风险分；1-4 分全绿，5-6 分全黄，7-10 分全红。
- **分项安全仪表盘**：专门把最差的 1-3 个局部风险拎出来，避免“整体还行”掩盖某一句危险话术。

## 安装和使用

先克隆仓库：

```bash
git clone https://github.com/zexuanw958-svg/content-compliance-skill.git
cd content-compliance-skill
```

然后把 `content-compliance/` 这个 Skill 包复制到你使用的 Agent 技能目录。

### Codex / Code X

Codex / Code X 推荐优先使用共享 Skill 目录：用户级放到 `~/.agents/skills`，项目级放到 `.agents/skills`。

用户级安装：

```bash
mkdir -p ~/.agents/skills
cp -R content-compliance ~/.agents/skills/
```

项目级安装：

```bash
mkdir -p .agents/skills
cp -R content-compliance .agents/skills/
```

部分本地 Codex / Code X 版本也会读取 `~/.codex/skills`。如果你的环境使用这个目录，可以额外复制一份：

```bash
mkdir -p ~/.codex/skills
cp -R content-compliance ~/.codex/skills/
```

使用示例：

```text
/检测
/content-compliance
帮我审一下这个抖音口播稿有没有合规风险
```

### Claude Code

Claude Code 的个人 Skill 目录是 `~/.claude/skills`，项目级 Skill 目录是 `.claude/skills`。

个人级安装：

```bash
mkdir -p ~/.claude/skills
cp -R content-compliance ~/.claude/skills/
```

项目级安装：

```bash
mkdir -p .claude/skills
cp -R content-compliance .claude/skills/
```

使用示例：

```text
/content-compliance
/检测
检测这个小红书标题和正文，看看能不能发
```

如果 Claude Code 已经在运行但没有识别到 Skill，可以执行 `/reload-skills`，或者重启 Claude Code。

### OpenClaw

OpenClaw 支持用 skills CLI 安装本地 Skill 文件夹。

全局安装：

```bash
openclaw skills install ./content-compliance --as content-compliance --global
```

手动安装：

```bash
mkdir -p ~/.openclaw/skills
cp -R content-compliance ~/.openclaw/skills/
```

使用示例：

```text
/content-compliance
合规检测：按抖音规则检查这段口播稿
```

### Hermes Agent

如果你使用的是 Hermes Agent，或其他兼容 `SKILL.md` 文件夹格式的智能体工具，把同一个 `content-compliance/` 文件夹复制到该运行时配置的 Skill 目录即可。

常见 Hermes 兼容目录示例：

```bash
mkdir -p ~/.hermes/skills
cp -R content-compliance ~/.hermes/skills/
```

如果你的客户端使用其他目录，以客户端文档为准。这个 Skill 需要保持下面的包结构：

```text
content-compliance/
  SKILL.md
  rules/
  scoring.md
  templates/
  references/
  examples/
  scripts/
```

不支持斜杠命令时，可以直接自然语言唤醒：

```text
请使用 content-compliance skill，按抖音规则检测这段口播稿。
```

## 兼容性速查

| Agent | 推荐安装位置 | 可用唤醒方式 |
| --- | --- | --- |
| Codex / Code X | `~/.agents/skills/content-compliance` 或 `.agents/skills/content-compliance` | `/检测`、`/content-compliance`、`检测这个抖音稿子` |
| Claude Code | `~/.claude/skills/content-compliance` 或 `.claude/skills/content-compliance` | `/检测`、`/content-compliance`、`帮我查一下小红书稿子风险` |
| OpenClaw | `openclaw skills install ./content-compliance --as content-compliance --global` | `/content-compliance`、`合规检测：按抖音规则检查` |
| Hermes Agent | 运行时自己的 `SKILL.md` 技能目录，常见为 `~/.hermes/skills/content-compliance` | 取决于客户端；自然语言唤醒稳定可用 |

## 项目结构

```text
content-compliance/
  SKILL.md                         # Skill 主流程和触发说明
  rules/                           # 抖音 / 小红书规则卡
  scoring.md                       # 风险分、可视化进度条和分项安全诊断分算法
  templates/report.md              # 检测报告模板
  references/                      # 官方来源清单、调研记录和定期复核流程
  examples/                        # 抖音 / 小红书示例报告
  scripts/validate_skill.py        # Skill 包校验器
tests/
  test_content_compliance_skill.py # 回归测试
```

## 验证

```bash
python3 content-compliance/scripts/validate_skill.py
python3 -m unittest tests/test_content_compliance_skill.py -v
```

说明：

这个仓库是公开分发包，所以 `content-compliance/README.md` 会保留在 Skill 包内，方便用户单独查看。某些通用 skill-creator 校验器可能不喜欢 Skill 文件夹内放 README；对本项目来说，请以自带校验器和测试套件为准。

## 封面图

当前封面图是 `assets/readme-banner.png`，原始大图保存在 `assets/readme-banner-source.png`。如果后续需要重新生成，提示词放在 `assets/readme-banner.prompt.md`，建议保持 1200 × 360 的横幅比例。

## 免责声明

本 Skill 是合规参考工具，不是抖音、小红书、巨量引擎、蒲公英、聚光、薯条或任何平台的官方审核工具。它不保证内容发布成功、投放审核通过、获得流量推荐、账号安全或完全符合法律法规。平台规则和审核口径可能随时间、账号状态、内容上下文和执行尺度变化。使用者应自行核对最新官方规则，并对发布、投放、商业推广和法律责任负责。
