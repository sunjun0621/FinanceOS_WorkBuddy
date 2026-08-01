# 数据缓冲区 / Data Buffer

FinanceOS 的**唯一数据入口**。用户将待分析的资料和数据放入 `input/`，OS 运行时从这里读取、处理，处理完后成果放入独立的产出区 `output/`。

> **设计原则**：存逻辑不存事实。AI 只拥有规则/模板/案例，业务数据通过缓冲区只读即弃，不沉淀。

---

## 工作流

```
用户 → input/（放数据和资料）→ OS 读取处理 → output/（产出报告）
         缓冲区                                    产出区
```

1. 从 `templates/` 下载对应的 CSV 模板
2. 按模板格式填入数据（脱敏后）
3. 将填好的文件放入 `input/` 目录
4. 告诉 AI 你需要做什么分析
5. AI 读取数据 → 分析处理 → 产出报告放入 `output/{日期}_{任务名}/`
6. 缓冲区数据读取后即弃，产出区保留

---

## 目录结构

```
data-buffer/                     ← 数据缓冲区（唯一入口）
├── README.md                    ← 本文件
├── .gitignore                   # input/ 不提交 Git
├── templates/                   ← CSV 数据模板
│   ├── budget-template.csv      # 预算执行数据模板
│   ├── income-statement.csv     # 利润表模板
│   ├── balance-sheet.csv        # 资产负债表模板
│   └── template-guide.md        # 模板填写指南
└── input/                       ← 放入待处理数据（.gitignore）
    └── .gitkeep

output/                          ← 产出区（独立于缓冲区）
├── .gitkeep
└── {YYYY-MM-DD}_{task-name}/    # 按任务日期+名称归档
    └── 报告.md
```

> **未来扩展**：API 端口直推时，数据推入 `input/`，流程不变。

---

## 安全提示

- `input/` 和 `output/` 均已加入 `.gitignore`，数据不会被提交到 Git
- 上传数据前请先按 `[L1:data-masking]` 脱敏标准进行处理
- 建议使用方案A（内部分析）或方案B（对外报告）进行脱敏
- AI 从 `input/` 读取数据后，任务完成即清除，不会持久化存储
- 涉密文件不进入缓冲区，不处理

---

## 清理策略

```bash
# 清理缓冲区已消费的数据（保留目录结构）
rm -rf data-buffer/input/*

# 清理产出区（确认不需要后）
rm -rf output/*
```

清理前确认没有正在进行的任务。缓冲区数据不跨会话保留，清理不影响知识库。

---

## 模板说明

| 模板 | 用途 | 适用场景 |
|------|------|---------|
| `budget-template.csv` | 预算执行数据 | 月度/季度预算执行分析 |
| `income-statement.csv` | 利润表 | 经营分析、盈利能力分析 |
| `balance-sheet.csv` | 资产负债表 | 偿债能力分析、资产结构分析 |

详细填写说明见 `templates/template-guide.md`
