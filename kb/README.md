# Knowledge Base (KB)

FinanceOS 的知识库按约束力分为四级。当前附带**水务/公用事业**领域的完整示例。

## 结构

```
kb/
├── L1-rules/              # 强制约束 · 红线不可违反
│   ├── anomaly-thresholds.md    # 异常阈值标准
│   ├── data-masking.md          # 脱敏标准清单
│   └── permission-tiers.md      # 权限分级
├── L2-templates/          # 形式规范 · 输出格式
│   ├── monthly-analysis.md      # 月度经营分析模板
│   ├── quarterly-analysis.md    # 季度财务分析模板
│   └── special-report.md        # 专项分析模板
├── L2.5-task-templates/   # 编排复用 · 高频任务路径
│   └── monthly-budget-analysis.md
├── L3-cases/              # 方法参考 · 历史经验
│   ├── case-001-monthly.md
│   ├── case-002-monthly-peak.md
│   ├── case-003-quarterly.md
│   └── case-004-first-month.md
└── L4-decision-logs/      # 决策追溯 · 记录模板
    └── template.md
```

## 引用方式

库间通过文件名 + 锚点引用，不复制内容：

```
[L1:anomaly-thresholds#4.1] → 引用异常阈值标准的判定矩阵
[L2:monthly-analysis] → 引用月度经营分析模板
[L3:case-004-first-month] → 引用首月运营案例
```

## 约束力说明

| 库 | 约束力 | AI 行为 |
|----|--------|--------|
| L1 | 强制 | 违反即停止，绝不绕行 |
| L2 | 形式 | 建议遵循，偏离需标注原因 |
| L2.5 | 编排 | 命中则用，跳过意图识别 |
| L3 | 参考 | 可作依据或仅参考 |
| L4 | 追溯 | 记录用，不影响当前决策 |

## 适配新领域

如果你想将 FinanceOS 用于其他行业（制造、金融、医疗等），只需替换 KB 内容：

1. 编写新领域的 L1 规则（异常阈值、脱敏标准、权限）
2. 编写新领域的 L2 模板（报告格式、文档骨架）
3. （可选）编写 L2.5 任务模板和 L3 案例

核心框架（FINANCEOS_SYSTEM.md）无需修改。

详见 [docs/domain-adaptation.md](../docs/domain-adaptation.md)
