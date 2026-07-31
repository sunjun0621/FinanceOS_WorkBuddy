# Adapters

本目录包含 FinanceOS 在各 AI 平台上的适配器。

每个适配器提供该平台特有的安装说明和配置文件。核心指令集 `core/FINANCEOS_SYSTEM.md` 是平台无关的，适配器只负责"怎么在各平台加载它"。

## 已支持的平台

| 平台 | 目录 | 状态 |
|------|------|------|
| WorkBuddy | [workbuddy/](workbuddy/) | ✅ 完整（含 SKILL.md 指令文件） |
| ChatGPT | [chatgpt/](chatgpt/) | ⚠️ 仅 README 指南（待补 Custom GPT 指令模板） |
| Claude | [claude/](claude/) | ⚠️ 仅 README 指南（待补 Project 指令模板） |
| 通用 | [generic/](generic/) | ⚠️ 仅 README 指南（万能适配器，待补指令模板） |

## 贡献新适配器

1. 创建 `adapters/{platform-name}/` 目录
2. 包含 `README.md`（安装说明）
3. 如有平台特定配置文件，一并放入
4. 提交 PR

适配器模板：
```markdown
# {Platform} Adapter

## 安装
[步骤]

## 使用
[示例]

## 注意事项
[平台特有的限制或优势]
```
