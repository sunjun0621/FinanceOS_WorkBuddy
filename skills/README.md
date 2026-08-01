# FinanceOS 预制 SKILL 体系

> 5 个开箱即用的 AI 财务技能 · 装完 30 秒见效

## 这是什么

FinanceOS 预制 SKILL 是一组**开箱即用**的 AI 财务技能。每个 SKILL 附带脱敏示例数据——用户安装 FinanceOS 后，粘贴一句触发指令，AI 即可自动跑完五阶段闭环（感知→研判→执行→交付→沉淀），输出一份完整报告。**无需自己想"该问什么"**。

定位：默认覆盖 CFO 40%+ 日常高频工作。用户看到效果后，再按自身需求调整 KB 和模板。

---

## 30 秒上手

对 AI 说以下任一指令，立即体验（示例数据已内置）：

| 触发指令 | 效果 |
|---------|------|
| `用示例数据跑一次月度经营分析` 或 `/monthly` | 输出带 🟡🟠 预警标注的八章节月度经营分析报告 |
| `用示例数据跑一次预算差异归因` 或 `/variance` | 输出分科目对比 + 量价归因链 + 改进建议 |
| `用示例数据跑一次现金流分析` 或 `/cashflow` | 输出利润与现金流背离归因报告 |
| `用示例数据写一份化债资金请示` 或 `/gongwen` | 输出符合 GB/T 9704 的标准公文 |
| `/ask 产销差率` 或 "什么是产销差率" | 秒回 + 引用 KB 来源标注 |

---

## 5 个 SKILL 总览

| # | SKILL | 触发词 | 风险等级 | 关联 KB | 来源参考 |
|---|------|--------|---------|---------|---------|
| 1 | [月度经营分析](monthly-analysis/) · *旗舰演示* | `/monthly` | Gate-M | L2 月度模板 + L1 异常阈值 + L2.5 任务模板 | FinRobot (Apache-2.0) |
| 2 | [预算差异归因](budget-variance/) | `/variance` | Gate-M | L3 case-006 + L1 异常阈值 | actualbudget (MIT) |
| 3 | [现金流分析](cashflow-analysis/) | `/cashflow` | Gate-M | L2 现金流模板 + L3 case-005 | dexter (MIT) |
| 4 | [公文起草](document-drafting/) | `/gongwen` | Gate-M → Gate-H | L2 GB/T 9704 规范 | wenshu (MIT) |
| 5 | [财务知识问答](knowledge-qa/) | `/ask` | Gate-L | L1 全部规则 + L3 案例库 + 术语表 | awesome-chatgpt-prompts-zh (MIT) |

> 风险等级遵循 FinanceOS STOP Gate 四级体系（Gate-L 自动 / Gate-M 确认后执行 / Gate-H 确认+脱敏+留痕 / Gate-X 禁止）。

---

## 来源合规性

所有 SKILL 的方法论 / 工作流范式参考自 GitHub 开源项目，**全部为 MIT 或 Apache-2.0 许可**（开源世界最友好的两种许可证）。FinanceOS 提取的是**工作流范式**而非代码，SKILL.md 内容为 FinanceOS 原创。

| SKILL | 来源项目 | 许可证 | 提取价值 |
|------|---------|--------|---------|
| 月度经营分析 | [AI4Finance-Foundation/FinRobot](https://github.com/AI4Finance-Foundation/FinRobot) | Apache-2.0 | "感知→建模→综合→报告" 四阶段范式 |
| 预算差异归因 | [actualbudget/actual](https://github.com/actualbudget/actual) | MIT | 信封预算法差异追踪闭环 |
| 现金流分析 | [virattt/dexter](https://github.com/virattt/dexter) | MIT | "分解→取数→分析→自验证→精炼" 范式 |
| 公文起草 | [Aether-liusiqi/wenshu](https://github.com/Aether-liusiqi/wenshu) | MIT | 6 步公文写作工作流 + 15 法定文种结构 |
| 财务知识问答 | [PlexPt/awesome-chatgpt-prompts-zh](https://github.com/PlexPt/awesome-chatgpt-prompts-zh) | MIT | 角色 Prompt 结构（角色定义→知识边界→回答规范） |

详见各 SKILL.md 的"来源与合规"章节。

---

## 使用指南

### 用示例数据体验（最快）
直接说 **"用示例数据跑一次 {技能名}"**，AI 读取该 SKILL 的 `SKILL.md` + `examples/sample-data.json`，自动执行五阶段闭环。

### 用自己的数据
把你的数据按 `examples/sample-data.json` 的结构整理后粘贴给 AI，再说触发词。AI 会用你的数据替换示例数据执行。

### 与主调度中枢的关系
预制 SKILL 是**独立可执行的技能指令**。主调度中枢（`cfo-command-center`，见 `adapters/workbuddy/SKILL.md`）感知到 `skills/` 目录——命中触发词即加载对应 SKILL 执行，五阶段闭环与 STOP Gate 体系照常生效。SKILL 内通过 `[L1:xxx]` `[L2:xxx]` `[L3:xxx]` 引用知识库，不复制 KB 内容。

### 目录结构

```
skills/
├── README.md                  ← 本文件（索引）
├── monthly-analysis/          ← SKILL 1
│   ├── SKILL.md               ← 技能指令
│   ├── examples/sample-data.json   ← 示例数据
│   └── README.md
├── budget-variance/           ← SKILL 2
├── cashflow-analysis/         ← SKILL 3
├── document-drafting/         ← SKILL 4
│   └── examples/sample-report.md   ← 示范公文
└── knowledge-qa/              ← SKILL 5
    └── examples/sample-questions.md ← 10 个示例问题
```

---

## 扩展

用户使用过程中，可根据自身工作习惯和行业特点，参照这 5 个 SKILL 的结构自建新 SKILL，放入 `skills/` 目录即可被识别。OS 有成长空间，但成长由用户驱动，不由开发者预设。

---

*— FinanceOS 预制 SKILL 体系 v2.4 —*
