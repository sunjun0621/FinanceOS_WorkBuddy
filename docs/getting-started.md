# 快速开始

欢迎使用 FinanceOS！本指南帮助你在 5 分钟内完成首次设置。

## 第一步：选择你的 AI 平台

FinanceOS 目前支持以下平台：

| 平台 | 推荐度 | 特点 |
|------|--------|------|
| **Claude** | ⭐⭐⭐⭐⭐ | 最佳上下文窗口、最强指令遵守 |
| **WorkBuddy** | ⭐⭐⭐⭐⭐ | 原生集成、文件系统访问、STOP gate |
| **ChatGPT** | ⭐⭐⭐⭐ | 最易上手、Custom GPT 分享方便 |
| **通用/本地 LLM** | ⭐⭐⭐ | 完全离线、数据不外传 |

## 第二步：安装

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
# 安装 Skill
skillhub install financeos

# 或者手动复制
cp adapters/workbuddy/SKILL.md ~/.workbuddy/skills/financeos/SKILL.md

# 复制 KB
cp -r kb/ ~/.workbuddy/financeos-kb/
```

### 本地 LLM (Ollama)

```bash
# 创建 Modelfile
cat > Modelfile << 'EOF'
FROM llama3.1
SYSTEM """
[粘贴 core/FINANCEOS_SYSTEM.md 内容]
"""
EOF

ollama create financeos -f Modelfile
ollama run financeos
```

## 第三步：测试

安装完成后，对你的 AI 说：

```
帮我做一份月度经营分析。假设数据如下：
- 营业收入：500 万元
- 营业成本：250 万元
- 管理费用：80 万元
- 利润总额：170 万元
```

AI 应该按照 FinanceOS 框架（感知→研判→执行→交付→沉淀）来分析数据，自动标注异常、分色预警、结构化输出。

## 第四步：适配你的领域

当前 KB 附带**水务/公用事业**领域的规则和模板。如果你的领域不同：

1. 阅读 [domain-adaptation.md](domain-adaptation.md)
2. 修改 L1 规则（异常阈值、脱敏标准）
3. 修改 L2 模板（报告格式）
4. （可选）编写 L3 案例

## 需要帮助？

- 📖 完整架构：[architecture.md](architecture.md)
- 🔧 平台适配：[adapters/README.md](../adapters/README.md)
- 🐛 报告问题：[GitHub Issues](https://github.com/YOUR_USERNAME/financeos/issues)
- 💬 社区讨论：[GitHub Discussions](https://github.com/YOUR_USERNAME/financeos/discussions)
