# Knowledge Base (KB)

FinanceOS 的知识库按约束力分为四级。当前附带通用国企财务领域的完整示例。

## 结构

```
kb/
├── _contrib/                  # 社区贡献模板（降低贡献门槛）
│   ├── rule-template.md       # L1 规则模板
│   ├── template-template.md   # L2 模板的模板
│   ├── case-template.md       # L3 案例模板
│   └── checklist.md           # 提交前自检清单
├── L1-rules/                  # 强制约束 · 红线不可违反（8条）
│   ├── anomaly-thresholds.md  # 异常阈值标准
│   ├── data-masking.md        # 脱敏标准清单（12类+反推防护）
│   ├── permission-tiers.md    # 权限分级
│   ├── output-standards.md    # 输出标准（两层分级）
│   ├── fund-management.md     # 资金管理办法
│   ├── cost-control.md        # 成本费用管控制度
│   ├── regulatory-requirements.md  # 国资监管要求
│   └── chart-of-accounts.md   # 科目编码基线
├── L2-templates/              # 形式规范 · 输出格式（7个）
│   ├── monthly-analysis.md    # 月度经营分析模板
│   ├── quarterly-analysis.md  # 季度财务分析模板
│   ├── special-report.md      # 专项分析模板
│   ├── board-materials.md     # 董事会汇报材料模板
│   ├── fund-plan.md           # 月度资金计划模板
│   ├── cash-flow-analysis.md  # 现金流分析模板
│   └── gb-t9704-spec.md      # GB/T 9704 公文格式规范
├── L2.5-task-templates/       # 编排复用 · 高频任务路径
│   └── monthly-budget-analysis.md
├── L3-cases/                  # 方法参考 · 历史经验（11个）
│   ├── case-001-monthly.md        # 月度预算执行分析
│   ├── case-002-monthly-peak.md   # 月度预算执行（旺季）
│   ├── case-003-quarterly.md      # 季度财务分析
│   ├── case-004-first-month.md    # 首月运营分析（无基线）
│   ├── case-005-profit-vs-cashflow.md  # 利润增长与现金流下降
│   ├── case-006-budget-variance.md     # 预算差异归因法
│   ├── case-007-ar-risk.md             # 应收账款风险评估
│   ├── case-008-investment.md          # 投资项目财务评价
│   ├── case-009-tax-risk.md            # 税务风险识别
│   ├── case-010-cost-overrun.md        # 成本费用超支归因
│   └── case-011-capex-variance.md      # 资本性支出差异归因
└── L4-decision-logs/          # 决策追溯 · 记录模板
    └── template.md
```

## 引用方式

库间通过文件名 + 锚点引用，不复制内容：

```
[L1:anomaly-thresholds#4.1] → 引用异常阈值标准的判定矩阵
[L1:fund-management#三] → 引用资金管理办法的监控指标
[L2:monthly-analysis] → 引用月度经营分析模板
[L2:gb-t9704-spec] → 引用公文格式规范
[L3:case-006-budget-variance] → 引用预算差异归因案例
```

## 约束力说明

| 库 | 约束力 | AI 行为 |
|----|--------|--------|
| L1 | 强制 | 违反即停止，绝不绕行 |
| L2 | 形式 | 建议遵循，偏离需标注原因 |
| L2.5 | 编排 | 命中则用，跳过意图识别 |
| L3 | 参考 | 可作依据或仅参考 |
| L4 | 追溯 | 记录用，不影响当前决策 |

## 贡献新知识

想为知识库添加新规则、模板或案例？

1. 到 `_contrib/` 目录获取对应模板
2. 按模板填写内容
3. 用 `_contrib/checklist.md` 自检
4. 提交 PR

详见 [CONTRIBUTING.md](../CONTRIBUTING.md)

## 数据过渡空间

没有 ERP 的用户？将数据放入 `data-buffer/input/` 目录即可。

详见 [data-buffer/README.md](../data-buffer/README.md)

## 适配新领域

如果你想将 FinanceOS 用于其他行业（制造、金融、医疗等），只需替换 KB 内容：

1. 编写新领域的 L1 规则（异常阈值、脱敏标准、权限）
2. 编写新领域的 L2 模板（报告格式、文档骨架）
3. （可选）编写 L2.5 任务模板和 L3 案例

核心框架（FINANCEOS_SYSTEM.md）无需修改。

详见 [docs/domain-adaptation.md](../docs/domain-adaptation.md)
