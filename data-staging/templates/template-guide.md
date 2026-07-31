# 数据模板填写指南 / Data Template Guide

> 适用于 FinanceOS_WorkBuddy 数据暂存区（data-staging）的三套标准模板。
> Applicable to the three standard templates in the FinanceOS_WorkBuddy data-staging area.

---

## 目录 / Contents

1. [模板总览 / Template Overview](#1-模板总览--template-overview)
2. [预算执行模板 / Budget Execution Template](#2-预算执行模板--budget-execution-template)
3. [利润表模板 / Income Statement Template](#3-利润表模板--income-statement-template)
4. [资产负债表模板 / Balance Sheet Template](#4-资产负债表模板--balance-sheet-template)
5. [通用填写规范 / General Filling Rules](#5-通用填写规范--general-filling-rules)
6. [常见陷阱与注意事项 / Common Pitfalls](#6-常见陷阱与注意事项--common-pitfalls)
7. [数据提交流程 / Submission Workflow](#7-数据提交流程--submission-workflow)

---

## 1. 模板总览 / Template Overview

| 文件 / File | 用途 / Purpose | 数据来源 / Data Source |
|---|---|---|
| `budget-template.csv` | 预算执行对比分析 | 预算管理系统 / 财务部门 |
| `income-statement.csv` | 利润表（损益表）数据 | 财务核算系统 |
| `balance-sheet.csv` | 资产负债表数据 | 财务核算系统 |

**所有模板均使用 UTF-8 with BOM 编码**，可直接用 Excel 打开而不会出现中文乱码。
All templates use **UTF-8 with BOM** encoding and can be opened directly in Excel without garbled Chinese characters.

---

## 2. 预算执行模板 / Budget Execution Template

**文件：** `budget-template.csv`

### 用途 / Purpose
用于预算与实际执行的对比分析，支持差异分解和归因分析。
Used for budget vs. actual variance analysis, supporting factor decomposition and attribution analysis.

### 字段说明 / Field Descriptions

| 字段名 | 说明 | 必填 | 示例 |
|---|---|---|---|
| 科目编码 | 企业内部预算科目编码 | 是 | `5001` |
| 科目名称 | 科目中文名称 | 是 | `主营业务收入` |
| 科目类型 | 分类标签（收入类/运营支出/期间费用/人员经费/资本性支出/税费等） | 是 | `收入类` |
| 本期预算 | 当月/当季预算金额 | 是 | `85000000` |
| 本期实际 | 当月/当季实际发生金额 | 是 | `82000000` |
| 累计预算 | 年初至本期累计预算 | 是 | `510000000` |
| 累计实际 | 年初至本期累计实际 | 是 | `492000000` |
| 去年同期 | 上年同期实际发生额（用于同比分析） | 建议填写 | `79000000` |

### 填写说明 / Filling Instructions

1. **科目编码**：使用企业统一的预算科目编码体系。如企业无统一编码，可自行编排，但须保持前后一致。
   Use your enterprise's unified budget account coding system. If none exists, create your own but maintain consistency.

2. **科目类型**：建议使用以下标准分类：
   Recommended standard categories:
   - `收入类` — 各类收入
   - `运营支出` — 主营业务成本、其他业务成本
   - `期间费用` — 管理费用、销售费用、财务费用、研发费用
   - `人员经费` — 工资、社保、福利等
   - `资本性支出` — 设备购置、工程建设、无形资产
   - `税费` — 税金及附加、所得税
   - `专项资金` — 专项拨款对应的支出

3. **金额**：填写绝对值，以**元**为单位。收入类科目填正数。
   Enter absolute values in **CNY (yuan)**. Revenue items should be positive.

---

## 3. 利润表模板 / Income Statement Template

**文件：** `income-statement.csv`

### 用途 / Purpose
用于编制标准利润表（损益表），支持盈利能力分析和趋势对比。
Used to prepare a standard PRC income statement, supporting profitability analysis and trend comparison.

### 字段说明 / Field Descriptions

| 字段名 | 说明 | 必填 | 示例 |
|---|---|---|---|
| 报表项目 | 利润表标准项目名称 | 是 | `一、营业收入` |
| 行次 | 报表行号（参照财政部报表格式） | 是 | `1` |
| 本期金额 | 当月发生额 | 是 | `50000000` |
| 本年累计 | 年初至本期末累计发生额 | 是 | `50000000` |
| 上年同期 | 上年同期的本年累计金额 | 建议填写 | `0` |

### 填写说明 / Filling Instructions

1. **报表项目与行次**：已按照财政部《企业会计准则》利润表格式预置。请勿修改项目名称和行次编号，以确保报表勾稽关系正确。
   Report items and line numbers follow the MOF "Accounting Standards for Business Enterprises" format. Do not modify item names or line numbers to preserve cross-checking integrity.

2. **金额方向**：
   Amount direction:
   - 收入类：正数 / Revenue: positive
   - 成本费用类：正数（系统自动做减法） / Costs: positive (system subtracts automatically)
   - 损失类（减值损失、信用减值损失）：负数 / Losses: negative
   - 财务费用：正数表示净支出，负数表示净收入 / Financial expenses: positive = net expense, negative = net income

3. **本期金额 vs 本年累计**：
   - "本期金额"= 本月的发生额
   - "本年累计"= 1月至本月的累计发生额
   - 两者关系：12月的本期金额 = 本年累计 - 11月本年累计

---

## 4. 资产负债表模板 / Balance Sheet Template

**文件：** `balance-sheet.csv`

### 用途 / Purpose
用于编制标准资产负债表，支持偿债能力分析和财务健康诊断。
Used to prepare a standard PRC balance sheet, supporting solvency analysis and financial health diagnosis.

### 字段说明 / Field Descriptions

| 字段名 | 说明 | 必填 | 示例 |
|---|---|---|---|
| 报表项目 | 资产负债表标准项目名称 | 是 | `货币资金` |
| 行次 | 报表行号（参照财政部报表格式） | 是 | `1` |
| 期末余额 | 本期末（如月末、季末、年末）余额 | 是 | `15000000` |
| 年初余额 | 本年年初（即上年末）余额 | 是 | `12000000` |

### 填写说明 / Filling Instructions

1. **时点数据**：资产负债表为时点报表，填写的是某一天的余额（如12月31日），而非期间发生额。
   The balance sheet is a point-in-time statement. Fill in balances as of a specific date (e.g., December 31), not period activity.

2. **勾稽关系**：请确保以下等式成立：
   Cross-checking equations that must hold:
   - `资产总计` = `负债合计` + `所有者权益合计`
   - `负债和所有者权益总计` = `资产总计`
   - `流动资产合计` = 各流动资产项目之和
   - `非流动资产合计` = 各非流动资产项目之和
   - `流动负债合计` = 各流动负债项目之和
   - `非流动负债合计` = 各非流动负债项目之和

3. **年初余额**：应与上年末资产负债表的期末余额一致。如有会计政策变更或前期差错更正，需调整年初余额。
   Opening balances should match the prior year-end closing balances. Adjust for accounting policy changes or prior-period error corrections.

4. **国有资本标注**：实收资本中的国有资本部分，如存在多个出资方，请在备注中说明。
   For state-owned capital in paid-in capital, note the breakdown if multiple investors exist.

---

## 5. 通用填写规范 / General Filling Rules

### 编码与格式 / Encoding & Format

- **文件编码**：UTF-8 with BOM（模板已预置，请勿另存为 ANSI 或 GBK）
  Encoding: UTF-8 with BOM (pre-set in templates; do not save as ANSI or GBK)
- **分隔符**：逗号（半角） / Delimiter: comma (half-width)
- **金额单位**：元（人民币），保留整数或最多两位小数
  Currency unit: CNY (yuan), integer or up to 2 decimal places
- **负数表示**：使用负号 `-`，不要用括号 `()`
  Negative numbers: use minus sign `-`, not parentheses `()`

### 注释行 / Comment Lines

- 以 `#` 开头的行为注释行，系统会自动忽略。
  Lines starting with `#` are comments and will be ignored by the system.
- 示例数据行前有注释标记 `# 示例数据（非真实数据，仅供参考格式）`。
  Sample data rows are preceded by a comment marker.
- **提交数据前请删除所有注释行和示例数据行。**
  **Delete all comment lines and sample data rows before submission.**

### 空值处理 / Handling Empty Values

- 如某项数据为零，填写 `0`，不要留空。
  If a value is zero, enter `0` — do not leave blank.
- 如某科目不适用，也填写 `0`。
  If an item is not applicable, also enter `0`.
- 仅"上年同期"或"年初余额"在确实无法取得时可留空。
  Only "prior year same period" or "opening balance" may be left blank if truly unavailable.

---

## 6. 常见陷阱与注意事项 / Common Pitfalls

### 含税 vs 不含税 / Tax-Inclusive vs Tax-Exclusive

> **重要：所有模板中的金额均应使用不含税金额（价税分离）。**
> **IMPORTANT: All amounts in templates should be tax-exclusive (tax separated).**

- 利润表中的收入和成本均为不含税金额。
  Revenue and costs in the income statement are tax-exclusive.
- 资产负债表中的应交税费单独列示，其余项目均为不含税口径。
  Taxes payable are shown separately on the balance sheet; other items are tax-exclusive.
- 预算执行数据中，如预算批复口径为含税，需自行换算为不含税。
  If the approved budget is tax-inclusive, convert to tax-exclusive yourself.

### 合并报表 vs 母公司报表 / Consolidated vs Standalone

> **请明确数据来源口径，并在文件命名或注释中注明。**
> **Clarify the data scope and note it in the filename or comments.**

- 利润表和资产负债表均可能是母公司单体报表或合并报表。
  Both statements may be standalone (parent company only) or consolidated.
- 预算执行数据通常为合并口径。
  Budget execution data is usually on a consolidated basis.
- **同一批分析中不要混用合并与母公司数据。**
  **Do not mix consolidated and standalone data within the same analysis.**

### 期间一致性 / Period Consistency

- 确保同一分析中所有报表的报告期一致（如均为2024年1-6月）。
  Ensure all statements in the same analysis cover the same period (e.g., all for Jan-Jun 2024).
- "本期"与"本年累计"的期间必须匹配。
  "Current period" and "YTD cumulative" periods must align.

### 行次与勾稽 / Line Numbers & Cross-Checks

- 不要随意增删行次，否则勾稽关系校验会失败。
  Do not arbitrarily add or remove line numbers, or cross-check validation will fail.
- 如需增加明细科目，请在对应合计行之前插入，并使用子编码（如 `9.1`、`9.2`）。
  To add detail items, insert before the corresponding subtotal line and use sub-codes (e.g., `9.1`, `9.2`).

### Excel 打开注意事项 / Excel Opening Notes

- 模板为 UTF-8 with BOM，Excel 可直接正确识别中文。
  Templates are UTF-8 with BOM; Excel will correctly recognize Chinese characters.
- 如用 Excel 的"数据 > 从文本/CSV"导入，请在文件来源中选择 **65001: Unicode (UTF-8)**。
  If importing via Excel's "Data > From Text/CSV", select **65001: Unicode (UTF-8)** as file origin.
- 切勿用"另存为 CSV"覆盖原模板，Excel 默认保存为 ANSI 编码会导致乱码。
  Do not overwrite the original template with "Save As CSV" — Excel defaults to ANSI encoding, which will corrupt Chinese characters.

### 常见数值错误 / Common Numerical Errors

| 错误类型 | 说明 | 预防措施 |
|---|---|---|
| 资产≠负债+权益 | 资产负债表不平衡 | 提交前验证行：资产总计 = 负债和所有者权益总计 |
| 累计≠上期累计+本期 | 期间数据不衔接 | 核对月度间勾稽关系 |
| 同比数据口径不一致 | 上年同期含已调整项目 | 使用调整后的可比数据 |
| 千分位/万分位混淆 | 金额单位错误 | 统一使用"元"为单位 |

---

## 7. 数据提交流程 / Submission Workflow

数据模板的使用遵循 data-staging 区域的统一工作流。详细流程请参阅 `data-staging/README.md`。
Template usage follows the unified workflow of the data-staging area. For the full workflow, refer to `data-staging/README.md`.

### 简要流程 / Quick Workflow

```
1. 下载模板 / Download template
       |
2. 填入数据（删除示例数据和注释行） / Fill in data (remove samples & comments)
       |
3. 自检勾稽关系 / Self-check cross-validation
       |
4. 命名文件：{类型}_{报告期}_{实体}.csv
   Name file: {type}_{period}_{entity}.csv
   例 / Example: income-statement_2024H1_集团公司.csv
       |
5. 上传至 data-staging/incoming/ 目录
   Upload to data-staging/incoming/ directory
       |
6. 系统自动校验并移入 processed/ 目录
   System auto-validates and moves to processed/ directory
```

### 文件命名规范 / File Naming Convention

| 模板类型 | 命名格式 | 示例 |
|---|---|---|
| 预算执行 | `budget_{YYYYMM}_{entity}.csv` | `budget_202406_集团公司.csv` |
| 利润表 | `income-statement_{YYYYMM}_{entity}.csv` | `income-statement_202406_集团公司.csv` |
| 资产负债表 | `balance-sheet_{YYYYMM}_{entity}.csv` | `balance-sheet_202406_集团公司.csv` |

---

## 附录：会计准则参考 / Appendix: Accounting Standards Reference

- 中华人民共和国财政部《企业会计准则》（2006年发布，后续修订）
  MOF "Accounting Standards for Business Enterprises" (issued 2006, subsequently amended)
- 《企业会计准则——应用指南》
  "Application Guidelines for Accounting Standards for Business Enterprises"
- 一般企业财务报表格式（财政部财会〔2019〕6号）
  General enterprise financial statement format (MOF Cai Kuai [2019] No. 6)

---

*最后更新 / Last updated: 2025-01*
*版本 / Version: 1.0*
