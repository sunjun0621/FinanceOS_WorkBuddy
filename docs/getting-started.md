# 快速开始

欢迎使用 FinanceOS！本指南用**三步通用法**帮你在 5 分钟内完成首次设置。

> FinanceOS 与具体 AI 平台解耦——核心指令 `core/FINANCEOS_SYSTEM.md` 是平台无关的，各平台只是"怎么加载它"的差异。

---

## 三步通用法

### 第一步：获取指令集

```bash
git clone https://github.com/sunjun0621/FinanceOS_WorkBuddy.git financeos
cd financeos
```

或直接下载 ZIP 解压。你只需要两个东西：
- `core/FINANCEOS_SYSTEM.md` — 核心系统指令（平台无关）
- `kb/` — 知识库（L1 规则 / L2 模板 / L2.5 任务模板 / L3 案例 / L4 决策日志）

### 第二步：配置知识库路径

FinanceOS 通过变量 `{FINANCEOS_KB_ROOT}` 引用知识库根目录。各平台配置方式见下表【平台对照表】。

> 默认值：项目根目录下的 `kb/`（即 `{FINANCEOS_KB_ROOT} = ./kb`）。无需额外配置即可使用。

### 第三步：验证安装

对 AI 说一句测试指令，确认框架已激活：

```
帮我做一份月度经营分析。假设数据如下：
- 营业收入：500 万元
- 营业成本：250 万元
- 管理费用：80 万元
- 利润总额：170 万元
```

AI 应按 FinanceOS 框架（感知→研判→执行→交付→沉淀）分析数据，自动标注异常、分色预警、结构化输出。

---

## 平台对照表

| 平台 | 指令加载方式 | KB 路径配置方式 | 验证指令 |
|------|------------|---------------|---------|
| **Claude** | Project → Custom Instructions → 粘贴 `core/FINANCEOS_SYSTEM.md` | Project knowledge 上传 `kb/` 下 .md 文件 | "分析本月预算执行情况" |
| **ChatGPT** | Custom GPT → Instructions → 粘贴 `core/FINANCEOS_SYSTEM.md` | Knowledge 上传 `kb/` 下 .md 文件（20 文件上限） | 同上 |
| **WorkBuddy** | 安装 `adapters/workbuddy/SKILL.md` 到 `~/.workbuddy/skills/financeos/` | 复制 `kb/` 到 `~/.workbuddy/financeos-kb/` | `/financeos 分析本月预算执行情况` |
| **Cursor / Trae CN** | `.cursorrules` 或 `.trae/rules` 中引用核心指令 | 项目根目录 `kb/`（默认即可） | 同上 |
| **Claude Code** | `CLAUDE.md` 中引用 `core/FINANCEOS_SYSTEM.md` | 项目根目录 `kb/`（默认即可） | 同上 |
| **本地 LLM (Ollama)** | Modelfile 的 `SYSTEM` 部分粘贴核心指令 | Modelfile 中指明 `kb/` 路径 | 同上 |
| **通用 / 任意 API** | System Prompt / messages system role 粘贴核心指令 | 手动提及 `kb/` 目录或上传文件 | 同上 |

> 适配器详细说明见 [`adapters/`](../adapters/) 目录（含 chatgpt / claude / workbuddy / generic 各平台专项指南）。

---

## 各平台详细步骤

### Claude（推荐新手）

1. 打开 [claude.ai](https://claude.ai) → Projects → Create Project
2. Project name: `FinanceOS`
3. Custom Instructions: 粘贴 `core/FINANCEOS_SYSTEM.md` 全部内容
4. Project knowledge: 上传 `kb/L1-rules/` 下所有文件 + `kb/L2-templates/` 下所有文件
5. 保存

### ChatGPT

1. 打开 ChatGPT → Explore GPTs → Create
2. Instructions: 粘贴 `core/FINANCEOS_SYSTEM.md` 全部内容
3. Knowledge: 上传 `kb/` 目录下所有 .md 文件（注意 20 文件上限）
4. Name: `FinanceOS`
5. 保存

### WorkBuddy

```bash
# 安装 Skill（方式一：SkillHub）
skillhub install financeos

# 或手动复制（方式二）
cp adapters/workbuddy/SKILL.md ~/.workbuddy/skills/financeos/SKILL.md

# 配置 KB
cp -r kb/ ~/.workbuddy/financeos-kb/
```

### 本地 LLM (Ollama)

```bash
cat > Modelfile << 'EOF'
FROM llama3.1
SYSTEM """
[粘贴 core/FINANCEOS_SYSTEM.md 内容]
"""
EOF

ollama create financeos -f Modelfile
ollama run financeos
```

---

## 第四步：适配你的领域

当前 KB 附带**水务/公用事业**领域的规则和模板。如果你的领域不同：

1. 阅读 [domain-adaptation.md](domain-adaptation.md)
2. 修改 L1 规则（异常阈值、脱敏标准）
3. 修改 L2 模板（报告格式）
4. （可选）编写 L3 案例

> 核心框架（`core/FINANCEOS_SYSTEM.md`）领域无关，适配新领域只需替换 KB 内容，无需改核心。

## 需要帮助？

- 📖 完整架构：[architecture.md](architecture.md)
- 🔧 平台适配：[adapters/README.md](../adapters/README.md)
- 🐛 报告问题：[GitHub Issues](https://github.com/sunjun0621/FinanceOS_WorkBuddy/issues)
- 💬 社区讨论：[GitHub Discussions](https://github.com/sunjun0621/FinanceOS_WorkBuddy/discussions)
