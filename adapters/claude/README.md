# Claude Adapter

## 安装为 Claude Project

### 步骤

1. 打开 Claude → Projects → Create Project
2. **Project name**: `FinanceOS`
3. **Custom Instructions**: 粘贴 [`core/FINANCEOS_SYSTEM.md`](../../core/FINANCEOS_SYSTEM.md) 的全部内容
4. **Project knowledge**: 将 `kb/` 目录下的文件添加到 Project knowledge
   - 推荐至少添加所有 L1 规则文件 + L2 模板文件
   - L3 案例和 L2.5 任务模板按需添加
5. 保存

### 使用示例

在 Claude Project 中直接对话：

```
我是水务公司的财务总监，6月报表如下：
[提供数据]
请按 FinanceOS 框架分析。
```

### Claude 特有优势

- 更大的上下文窗口（200K tokens），可以一次加载更多 KB 内容
- Project knowledge 无文件数量硬限制
- 更好的长文档处理能力

### 注意事项

- Claude 对系统指令的遵守度较高，FinanceOS 的 STOP gate 机制在 Claude 上表现更好
- 建议将脱敏规则放在 Project knowledge 最前面，确保 AI 优先遵守
