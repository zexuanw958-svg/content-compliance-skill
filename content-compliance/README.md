# 内容合规检测 Skill 包

用于抖音 / 小红书内容发布前合规检测的 `SKILL.md` 包。适配 Codex / Code X、Claude Code、OpenClaw、Hermes Agent，以及其他兼容 `SKILL.md` 文件夹格式的智能体运行时。

## 能力

- 选题检测：在写稿前判断选题是否值得继续做。
- 成稿检测：检查标题、口播、正文、字幕、画面、评论区、私信计划。
- 可视化检测：输出 10 格风险条、安全条和分项安全分。
- 投放语境检测：区分普通发布和 DOU+、巨量引擎、薯条、蒲公英、聚光等商业化场景。
- 官方来源约束：把 `Status: active` 的确认风险和 `Status: needs_review` 的待复核提示分开。

## 唤醒方式

Skill 机器名：

```text
content-compliance
```

中文触发词：

```text
检测
合规检测
内容合规检测
帮我审一下抖音选题
帮我查一下小红书稿子风险
```

支持斜杠命令的运行时可用：

```text
/检测
/content-compliance
```

如果某个运行时不支持中文斜杠命令，用 `/content-compliance` 或自然语言触发即可。

## 安装目标

| Agent | 安装位置或命令 |
| --- | --- |
| Codex / Code X | `~/.agents/skills/content-compliance` 或 `.agents/skills/content-compliance`；部分本地版本也读取 `~/.codex/skills/content-compliance` |
| Claude Code | `~/.claude/skills/content-compliance` 或 `.claude/skills/content-compliance` |
| OpenClaw | `openclaw skills install ./content-compliance --as content-compliance --global`，或复制到 `~/.openclaw/skills/content-compliance` |
| Hermes Agent | 复制到运行时配置的 `SKILL.md` 技能目录；Hermes 兼容环境常见为 `~/.hermes/skills/content-compliance` |

更完整的安装命令和示例提示词，请看仓库根目录的 `README.md`。

## 支持平台

| 平台 | 场景 |
| --- | --- |
| 抖音 | 普通发布、DOU+、巨量引擎广告审核语境 |
| 小红书 | 普通笔记、薯条、蒲公英、聚光投放语境 |

## 输出要求

每份检测报告应包含：

- `总风险分`：1-10，越高越危险。
- `整体安全分`：1-10，越高越安全。
- `风险条` 和 `安全条`：固定 10 格。
- `分项安全仪表盘`：选题、标题/封面、话术、画面/字幕、外部引导、投放、强监管领域。
- `最弱风险点`：分数最低的 1-3 个模块，附证据和快速改法。
- 免责声明。

## 验证

从仓库根目录运行：

```bash
python3 content-compliance/scripts/validate_skill.py
python3 -m unittest tests/test_content_compliance_skill.py -v
```

说明：

这个 `README.md` 是为了公开分发和单独查看而保留在 Skill 包内。某些通用 skill-creator 校验器可能不喜欢 Skill 文件夹内放 README；本项目请以自带校验器和测试套件为准。

## 免责声明

本 Skill 是合规参考工具，不是官方审核工具。它不保证发布成功、投放审核通过、获得流量推荐、账号安全或完全符合法律法规。
