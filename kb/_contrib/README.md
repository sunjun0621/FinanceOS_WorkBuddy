# 知识库贡献模板 / KB Contribution Templates

本目录提供 L1/L2/L3 条目的标准模板，降低社区贡献门槛。

This directory provides standard templates for L1/L2/L3 entries to lower the barrier for community contributions.

---

## 模板说明

| 模板文件 | 用途 | 对应库 |
|---------|------|--------|
| `rule-template.md` | 规则条目模板 | L1-rules/ |
| `template-template.md` | 格式模板的模板 | L2-templates/ |
| `case-template.md` | 案例条目模板 | L3-cases/ |
| `checklist.md` | 提交前自检清单 | 所有库 |

---

## 贡献流程

1. 从本目录复制对应模板
2. 按模板填写内容
3. 用 `checklist.md` 自检
4. 将完成的文件放入对应的库目录（L1-rules/ / L2-templates/ / L3-cases/）
5. 提交 PR，标题格式：`[KB-L1] 新增：规则名称` / `[KB-L2] 新增：模板名称` / `[KB-L3] 新增：案例名称`

详细贡献规范见 [CONTRIBUTING.md](../../CONTRIBUTING.md)

---

## 命名规范

- L1 规则：`{english-name}.md`（如 `fund-management.md`）
- L2 模板：`{english-name}.md`（如 `board-materials.md`）
- L3 案例：`case-{NNN}-{english-name}.md`（如 `case-011-investment.md`）
