# ChatGPT Adapter

## 安装为 Custom GPT

### 方法一：手动创建（推荐）

1. 打开 ChatGPT → Explore GPTs → Create
2. **Instructions** 区域：粘贴 [`core/FINANCEOS_SYSTEM.md`](../../core/FINANCEOS_SYSTEM.md) 的全部内容
3. **Knowledge** 区域：上传 `kb/` 目录下的所有 Markdown 文件
4. **Name**: `FinanceOS`
5. **Description**: `AI 财务操作系统 - 企业财务总监智能助手`
6. 保存并测试：输入"帮我做月度经营分析"

### 方法二：一键导入

1. 下载本仓库
2. 使用 Custom GPT 的"Import from ZIP"功能导入 `kb/` 目录
3. 将 `core/FINANCEOS_SYSTEM.md` 粘贴到 Instructions

## 使用示例

```
我是一家水务公司的财务总监，请帮我分析 6 月的经营情况。
这是报表数据：[粘贴数据或上传文件]
```

```
帮我按 FinanceOS 框架做季度财务分析
```

## 注意事项

- ChatGPT 的 Knowledge 文件有数量限制（当前为 20 个文件），优先上传 L1 规则和 L2 模板
- 如果数据敏感，不要上传到 ChatGPT 的 Knowledge，改为在对话中手动提供数据
- 脱敏功能在 Custom GPT 中需要依赖 AI 自觉遵守（无系统级 STOP gate）
