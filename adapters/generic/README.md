# Generic Adapter (Any AI Platform)

## 通用安装

任何支持 System Prompt 或自定义指令的 AI 平台都可以使用 FinanceOS：

1. 复制 [`core/FINANCEOS_SYSTEM.md`](../../core/FINANCEOS_SYSTEM.md) 的全部内容
2. 粘贴到平台的 System Prompt / Instructions / 系统指令 区域
3. 将 `kb/` 目录下的相关文件作为上下文提供给 AI

## 支持的平台

| 平台 | 设置方式 |
|------|---------|
| **Google Gemini** | System instructions（Gemini Advanced） |
| **DeepSeek** | 系统提示词 |
| **Kimi** | 自定义指令 |
| **通义千问** | 系统提示 |
| **本地 LLM (Ollama/LM Studio)** | Modelfile 的 SYSTEM 部分 |
| **Cursor / Copilot** | `.cursorrules` 或 `.github/copilot-instructions.md` |
| **任意 API** | messages 数组的 system role |

## 本地 LLM 安装 (Ollama)

创建 Modelfile：
```dockerfile
FROM llama3
SYSTEM """
[粘贴 core/FINANCEOS_SYSTEM.md 的全部内容]
"""
```

然后：
```bash
ollama create financeos -f Modelfile
ollama run financeos
```

## 最小化安装（Token 受限时）

如果 AI 平台的上下文窗口较小，使用精简版：

```
你是 AI 财务办公室主任。你按 FinanceOS 框架工作：
1. 角色轴：数据分析师/报告撰写员/知识管家（核心）+ 预算管控官/政策研究员（按需）
2. 生命周期：感知→研判→执行(含校验)→交付→沉淀
3. 风险分层（STOP Gate 四级）：Gate-L 直接回答 / Gate-M 关键节点确认 / Gate-H 加脱敏+留痕 / Gate-X 禁止（删除修改原始数据）
4. 校验强制：勾稽/异常/口径/格式四项不跳过
5. 缓冲区数据只读即弃，不沉淀

详细规则见 [完整版](../../core/FINANCEOS_SYSTEM.md)
```
