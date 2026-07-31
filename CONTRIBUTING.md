# 贡献指南

感谢你对 FinanceOS 的关注！本项目采用 **社区驱动 + 核心维护者审核** 的模式。

## 贡献方式

### 🟢 低门槛贡献（无需编码）

| 方式 | 路径 | 说明 |
|------|------|------|
| 报告 Bug | [Issues → Bug Report](https://github.com/YOUR_USERNAME/financeos/issues/new?template=bug_report.md) | 任何问题都欢迎报告 |
| 提功能建议 | [Issues → Feature Request](https://github.com/YOUR_USERNAME/financeos/issues/new?template=feature_request.md) | 想要的功能、改进点 |
| 贡献 KB 条目 | [Issues → KB Contribution](https://github.com/YOUR_USERNAME/financeos/issues/new?template=kb_contribution.md) | 为你的行业添加规则/模板/案例 |
| 改进文档 | PR 到 `docs/` 目录 | 修正错误、补充说明、翻译 |

### 🔵 代码/内容贡献

1. **Fork 本仓库**
2. **创建分支** `feat/xxx` 或 `fix/xxx`
3. **提交 PR**，附清晰的变更说明
4. **通过审核后合并**

---

## KB 贡献规范

FinanceOS 的知识库（KB）按约束力分为四级，贡献前请确认你的内容属于哪一级：

### L1 规则库（强制约束·红线）
- **准入条件**：可复用、跨任务稳定、有明确判断标准
- **示例**：行业特定的合规红线、必须脱敏的数据类型、审批权限层级
- **格式要求**：Markdown，含版本号和生效日期

### L2 模板库（形式规范）
- **准入条件**：有标准化结构、可在同类任务中复用
- **示例**：特定行业的报告骨架、报送表格模板
- **格式要求**：Markdown，含章节结构 + 字段说明

### L2.5 任务模板库（编排复用）
- **准入条件**：同一任务编排路径已验证至少 2 次
- **示例**：月度预算执行分析编排、季度经营分析编排
- **格式要求**：Markdown，含角色编排表 + 分阶段执行路径

### L3 案例库（方法参考）
- **准入条件**：真实场景处理经验，标注 `[提炼]` 可复用或 `[原文]` 未验证
- **示例**：某月成本异常波动的归因过程
- **格式要求**：Markdown，含场景特征 + 分析方法 + 关键发现

---

## PR 规范

### Commit 信息
```
<type>: <简短描述>

类型: feat/fix/docs/style/refactor/test/chore
```

### PR 标题
```
[类型] 简短描述
```
类型同上。

### PR 正文模板
```markdown
## 变更说明
- 做了什么
- 为什么做

## 影响范围
- [ ] 核心系统文件（core/）
- [ ] 知识库（kb/）
- [ ] 适配器（adapters/）
- [ ] 文档（docs/）

## 测试
- [ ] 在至少一个 AI 平台上验证通过
- [ ] KB 引用关系检查无断裂
```

---

## 社区治理

### 角色与权限

| 角色 | 权限 | 如何获得 |
|------|------|---------|
| **Contributor** | 提交 PR、参与 Issue 讨论 | 提交并被合并至少 1 个 PR |
| **KB Maintainer** | 审核特定领域的 KB 条目 | 持续贡献某领域 KB 6 个月以上 |
| **Core Maintainer** | 审核核心系统变更、管理版本发布 | 由现有 Core Maintainer 提名并投票 |

### 决策流程

1. **日常 PR**：1 位 Core Maintainer 审核通过即可合并
2. **核心系统变更**（core/FINANCEOS_SYSTEM.md）：需 2 位 Core Maintainer 审核
3. **版本发布**：Core Maintainer 共识 + 更新 CHANGELOG
4. **重大分歧**：社区投票（Contributor 及以上可投票），简单多数

---

## 行为准则

参与本项目即表示同意遵守 [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md)。

---

## 问题与讨论

- 🐛 **Bug 报告**：[Issues](https://github.com/YOUR_USERNAME/financeos/issues)
- 💡 **功能建议**：[Issues](https://github.com/YOUR_USERNAME/financeos/issues)
- 💬 **社区讨论**：[Discussions](https://github.com/YOUR_USERNAME/financeos/discussions)

---

*FinanceOS 是一个开放的社区。你的每一个贡献，都在让 AI 财务助手变得更好。*
