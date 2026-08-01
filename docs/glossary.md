# 术语表

| 术语 | 英文 | 定义 |
|------|------|------|
| **FinanceOS** | FinanceOS | AI 财务操作系统，基于双轴认知模型的智能调度框架 |
| **双轴模型** | Dual-Axis Model | 角色轴 × 生命周期轴的矩阵式任务编排模型 |
| **AI 主任** | Finance Director Agent | 调度中枢，只调度不判断 |
| **主动认知层** | Proactive Cognitive Layer | 自动巡检指标、预判时机、发现异常的雷达层 |
| **STOP gate** | STOP Gate | 任务执行中的强制确认点，AI 必须停下来等总监确认 |
| **Gate-L/M/H/X** | Gate-L/M/H/X | STOP Gate 四级：L 自动·纯读取 / M 确认后执行·分析计算 / H 确认+脱敏+留痕·对外报送 / X 禁止·删除修改原始数据 |
| **三色预警** | Three-Color Alert | 🟡黄(标注) → 🟠橙(通知+归因) → 🔴红(强制确认) |
| **四维校验** | Four-Dimension Verification | 执行收尾的强制检查：勾稽/异常/口径/格式 |
| **L1 规则库** | L1 Rule Library | 强制约束规则，红线不可违反 |
| **L2 模板库** | L2 Template Library | 输出格式规范，报告骨架与表格结构 |
| **L2.5 任务模板库** | L2.5 Task Template Library | 高频任务的预设编排路径，命中则跳过意图识别 |
| **L3 案例库** | L3 Case Library | 历史处理经验，`[提炼]`可作依据 |
| **L4 决策日志** | L4 Decision Log | 重要决策的上下文、选项、结果、复盘 |
| **数据缓冲区** | Data Buffer | 用户数据和资料的唯一入口（`data-buffer/`），AI 只读即弃，不沉淀 |
| **产出区** | Output Area | 报告成果的存放区（`output/`），与缓冲区物理隔离 |
| **风险分层** | Risk Tier | Gate-L 日常→Gate-M 分析→Gate-H 报送/Gate-H (strict) 审计→Gate-X 禁止 的四级风险体系（v2.4 由原 T1-T4 细化而来） |
| **协作模式** | Collaboration Mode | 委托/标准/紧控三种 AI-用户协作强度 |
| **接力契约** | Relay Contract | 下一棒发现上一棒产出不合格→回退补齐，不擅自改口径 |
| **紧急通道** | Emergency Channel | 紧急信号词 + 产出物意图满足时的最简路径 |
| **模式判别** | Mode Detection | Step 0：紧急/轻量/完整的任务模式自动判别 |
| **Token 三级加载** | Three-Tier Token Loading | 内核层(~500t) + 场景层(~2000t) + 工作层(动态) |
| **预设方案** | Preset Plan | 内部分析/对外报送的自动化 gate 方案 |
| **工位** | Workstation | 角色×生命周期的交叉点，定义特定角色在特定阶段的任务 |
| **领域适配** | Domain Adaptation | 替换 KB 内容以适配新行业，核心框架不变 |
