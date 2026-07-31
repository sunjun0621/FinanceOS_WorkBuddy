# 数据过渡空间 / Data Staging Area

本目录为没有 ERP 系统的用户提供数据输入通道。将待分析的财务数据放入 `input/` 目录，AI 将从这里读取并处理。

This directory provides a data input channel for users without ERP systems. Place financial data files to be analyzed into the `input/` folder — the AI will read and process them from here.

---

## 使用方法 / How to Use

1. 从 `templates/` 下载对应的 CSV 模板
2. 按模板格式填入你的数据
3. 将填好的文件放入 `input/` 目录
4. 告诉 AI 你需要做什么分析

1. Download the corresponding CSV template from `templates/`
2. Fill in your data following the template format
3. Place the completed file into the `input/` directory
4. Tell the AI what analysis you need

---

## 目录结构 / Directory Structure

```
data-staging/
├── README.md                 ← 本文件 / This file
├── templates/                ← 数据模板 / Data templates
│   ├── budget-template.csv   ← 预算执行数据模板
│   ├── income-statement.csv  ← 利润表模板
│   ├── balance-sheet.csv     ← 资产负债表模板
│   └── template-guide.md     ← 模板填写指南
└── input/                    ← 放入待处理数据 / Place data here
    └── .gitkeep
```

---

## 安全提示 / Security Notice

- `input/` 目录已加入 `.gitignore`，数据不会被提交到 Git
- 上传数据前请先按 `[L1:data-masking]` 脱敏标准进行处理
- 建议使用方案A（内部分析）或方案B（对外报告）进行脱敏
- AI 从 `input/` 读取数据到缓冲区后，任务完成即清除，不会持久化存储

---

## 模板说明 / Template Descriptions

| 模板 | 用途 | 适用场景 |
|------|------|---------|
| `budget-template.csv` | 预算执行数据 | 月度/季度预算执行分析 |
| `income-statement.csv` | 利润表 | 经营分析、盈利能力分析 |
| `balance-sheet.csv` | 资产负债表 | 偿债能力分析、资产结构分析 |

详细填写说明见 `templates/template-guide.md`
