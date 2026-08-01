# 安装指南

> 5 分钟完成 FinanceOS 首次安装。核心指令 `core/FINANCEOS_SYSTEM.md` 平台无关，各平台只是"怎么加载它"的差异。

---

## 一、获取项目

```bash
git clone https://github.com/sunjun0621/FinanceOS_WorkBuddy.git financeos
cd financeos
```

或直接下载 ZIP 解压。你只需要两样东西：

- `core/FINANCEOS_SYSTEM.md` — 核心系统指令（平台无关）
- `kb/` — 知识库（L1 规则 / L2 模板 / L2.5 任务模板 / L3 案例 / L4 决策日志）

---

## 二、平台兼容性表

FinanceOS 通过变量 `{FINANCEOS_KB_ROOT}` 引用知识库根目录（默认 `./kb`，无需额外配置）。下表列出各 AI 平台的加载与配置方式：

| 平台 | 指令加载方式 | KB 路径配置方式 | 适配器 |
|------|------------|---------------|--------|
| **Claude** | Project → Custom Instructions → 粘贴 `core/FINANCEOS_SYSTEM.md` | Project knowledge 上传 `kb/` 下 .md 文件 | [adapters/claude/](adapters/claude/) |
| **ChatGPT** | Custom GPT → Instructions → 粘贴 `core/FINANCEOS_SYSTEM.md` | Knowledge 上传 `kb/` 下 .md 文件（20 文件上限） | [adapters/chatgpt/](adapters/chatgpt/) |
| **WorkBuddy** | 安装 `adapters/workbuddy/SKILL.md` 到 `~/.workbuddy/skills/financeos/` | 复制 `kb/` 到 `~/.workbuddy/financeos-kb/` | [adapters/workbuddy/](adapters/workbuddy/) ✅ 完整 |
| **Cursor / Trae CN** | `.cursorrules` 或 `.trae/rules` 中引用核心指令 | 项目根目录 `kb/`（默认即可） | [adapters/generic/](adapters/generic/) |
| **Claude Code** | `CLAUDE.md` 中引用 `core/FINANCEOS_SYSTEM.md` | 项目根目录 `kb/`（默认即可） | [adapters/generic/](adapters/generic/) |
| **本地 LLM (Ollama)** | Modelfile 的 `SYSTEM` 部分粘贴核心指令 | Modelfile 中指明 `kb/` 路径 | [adapters/generic/](adapters/generic/) |
| **通用 / 任意 API** | System Prompt / messages system role 粘贴核心指令 | 手动提及 `kb/` 目录或上传文件 | [adapters/generic/](adapters/generic/) |

> 适配器详细说明见 [`adapters/`](adapters/) 目录。WorkBuddy 已提供完整 SKILL.md 指令文件；其余平台为 README 指南（待补指令模板）。

---

## 三、验证安装

对 AI 说一句测试指令，确认框架已激活：

```
帮我做一份月度经营分析。假设数据如下：
- 营业收入：500 万元
- 营业成本：250 万元
- 管理费用：80 万元
- 利润总额：170 万元
```

AI 应按 FinanceOS 框架（感知→研判→执行→交付→沉淀）分析数据，自动标注异常、分色预警、结构化输出。

或直接使用预制 SKILL 触发词（示例数据已内置，30 秒出报告）：

| 触发词 | 效果 |
|---------|------|
| `/monthly` 或 "月度经营分析" | 八章节月度经营分析报告（含 🟡🟠🔴 三色预警） |
| `/variance` 或 "预算差异归因" | 分科目量价归因链 + 改进建议 |
| `/cashflow` 或 "现金流分析" | 利润与现金流背离归因报告 |

> 5 个开箱即用技能见 [`skills/`](skills/) 目录。

---

## 四、适配你的领域

当前 KB 附带**水务/公用事业**领域的规则和模板。如果你的领域不同：

1. 阅读 [docs/domain-adaptation.md](docs/domain-adaptation.md)
2. 修改 L1 规则（异常阈值、脱敏标准）
3. 修改 L2 模板（报告格式）
4. （可选）编写 L3 案例

> 核心框架领域无关，适配新领域只需替换 KB 内容，无需改核心。

---

## 需要帮助？

- 📖 完整快速开始：[docs/getting-started.md](docs/getting-started.md)
- 🏗️ 架构设计：[docs/architecture.md](docs/architecture.md)
- 📋 规范文档：[SPEC.md](SPEC.md)
- 🐛 报告问题：[GitHub Issues](https://github.com/sunjun0621/FinanceOS_WorkBuddy/issues)
