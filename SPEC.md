# FinanceOS 规范 (Specification)

> 版本：v1.0 · 2026-07-31
> 状态：active
> 适用范围：本仓库所有文件、所有适配器、所有 KB 条目、所有社区贡献

---

## 目录

1. [版本编号规范](#1-版本编号规范)
2. [文件命名规范](#2-文件命名规范)
3. [KB 条目 Schema](#3-kb-条目-schema)
4. [引用语法规范](#4-引用语法规范)
5. [适配器接口规范](#5-适配器接口规范)
6. [跨文件一致性规则](#6-跨文件一致性规则)
7. [目录结构规范](#7-目录结构规范)
8. [变更管理流程](#8-变更管理流程)
9. [校验工具](#9-校验工具)

---

## 1. 版本编号规范

### 1.1 项目版本

项目整体版本由 `core/VERSION.json` 的 `version` 字段定义，格式为语义化版本：

```
MAJOR.MINOR.PATCH
```

| 版本段 | 何时递增 | 示例 |
|--------|---------|------|
| MAJOR | 核心架构变更（双轴模型调整、库体系重构） | 2.x.x → 3.0.0 |
| MINOR | 新增功能或 KB 扩充（新增 L1 规则、新增适配器） | 2.4.0 → 2.5.0 |
| PATCH | 修复错误、文档修正、不动架构 | 2.4.0 → 2.4.1 |

### 1.2 组件版本

各组件独立维护版本号，记录在文件头部的元数据中：

| 组件 | 版本位置 | 当前基准 |
|------|---------|---------|
| `core/FINANCEOS_SYSTEM.md` | 文件标题 `v2.4` | 与项目版本同步 |
| `adapters/workbuddy/SKILL.md` | frontmatter `version: v2.4` | 与项目版本同步 |
| 各 KB 条目 | 文件元数据头 `> 版本：vX.Y` | 独立递进 |

### 1.3 版本一致性铁律

- `core/VERSION.json` 的 `version` 字段是**唯一真相源**（single source of truth）
- `README.md` 的 version badge 必须与 `VERSION.json` 一致
- `core/FINANCEOS_SYSTEM.md` 标题中的版本号必须与 `VERSION.json` 一致
- `adapters/workbuddy/SKILL.md` frontmatter 中的 `version` 必须与 `VERSION.json` 一致
- `CHANGELOG.md` 最新条目的版本号必须与 `VERSION.json` 一致
- 所有文档中引用"当前版本"时，必须与 `VERSION.json` 一致，不得引用过时版本号

### 1.4 版本术语统一

以下术语在所有文档中必须保持一致，禁止混用：

| 规范术语 | 禁止出现的旧术语 | 说明 |
|---------|----------------|------|
| Gate-L | T1 | 自动·纯读取 |
| Gate-M | T2 | 确认后执行·分析计算 |
| Gate-H | T3 | 确认+脱敏+留痕·对外报送 |
| Gate-H 严格子级 | T4 | 审计巡视·完整审计三段 |
| Gate-X | （新增） | 禁止·删除修改原始数据 |
| `kb/L1-rules/` | `L1-规则库/` | 目录名用英文 |
| `kb/L2-templates/` | `L2-模板库/` | 目录名用英文 |
| `kb/L2.5-task-templates/` | `L2.5-任务模板库/` | 目录名用英文 |
| `kb/L3-cases/` | `L3-案例库/` | 目录名用英文 |
| `kb/L4-decision-logs/` | `L4-决策日志/` | 目录名用英文 |
| `data-buffer/` | `data-staging/`（v2.5 已统一） | 数据缓冲区，用户数据入口 |
| `output/` | — | 产出区，报告成果单独存放 |

---

## 2. 文件命名规范

### 2.1 KB 条目文件名

所有 KB 条目文件使用 **全小写英文** + 连字符（kebab-case），以 `.md` 为扩展名：

```
{level}-{category}-{name}.md     # L1 规则
{level}-{name}.md                # L2/L2.5/L3/L4
```

**L1 规则库**命名模式：`{descriptive-name}.md`

| 正确 | 错误 |
|------|------|
| `anomaly-thresholds.md` | `异常阈值标准.md` |
| `data-masking.md` | `脱敏标准清单.md` |
| `permission-tiers.md` | `权限分级.md` |

**L2 模板库**命名模式：`{report-type}.md`

| 正确 | 错误 |
|------|------|
| `monthly-analysis.md` | `月度经营分析模板_v1.md` |
| `quarterly-analysis.md` | `季度财务分析报告模板_v1.md` |

**L3 案例库**命名模式：`case-{NNN}-{description}.md`

| 正确 | 错误 |
|------|------|
| `case-001-monthly.md` | `月度预算执行分析_案例001.md` |
| `case-006-budget-variance.md` | `预算差异归因_案例006.md` |

**L4 决策日志**命名模式：`DEC-YYYYMMDD-NNN_{description}.md`

```
DEC-20260730-001_threshold-adjustment.md
```

### 2.2 版本号不入文件名

版本号记录在文件元数据头中，不嵌入文件名。文件名只描述内容，不含版本信息。

| 正确 | 错误 |
|------|------|
| `monthly-analysis.md` | `monthly-analysis_v1.md` |
| `anomaly-thresholds.md` | `anomaly-thresholds-v1.1.md` |

### 2.3 目录名规范

仓库内所有目录名使用**全小写英文** + 连字符：

```
kb/L1-rules/           # 不是 L1-规则库/
kb/L2-templates/       # 不是 L2-模板库/
kb/L2.5-task-templates/ # 不是 L2.5-任务模板库/
kb/L3-cases/           # 不是 L3-案例库/
kb/L4-decision-logs/   # 不是 L4-决策日志/
data-buffer/           # 数据缓冲区（用户数据入口）
output/                # 产出区（报告成果）
```

### 2.4 文档文件命名

`docs/` 目录下的文档文件使用全小写英文 + 连字符：

```
docs/architecture.md
docs/operations-manual.md
docs/getting-started.md
docs/domain-adaptation.md
docs/kb-framework.md
docs/glossary.md
```

---

## 3. KB 条目 Schema

### 3.1 元数据头格式

每个 KB 条目文件**必须**以 YAML frontmatter 块或引用块格式的元数据头开始。推荐使用 YAML frontmatter：

```markdown
---
id: anomaly-thresholds
level: L1
name: 异常阈值标准
version: "1.1"
date: "2026-07-30"
source: internal
status: active
applies_to:
  - 感知阶段异常检测
  - 研判阶段差异归因
  - 主动认知层巡检
references:
  - cfo-command-center#3
  - cfo-command-center#5
---

# 异常阈值标准

> 效力等级：L1 强制约束 · 红线不可违反
> 适用：...
```

### 3.2 各级 Schema 定义

#### L1 规则库 Schema

```yaml
# 必填字段
id: string          # 唯一标识符，kebab-case，与文件名一致
level: "L1"         # 固定为 L1
name: string        # 中文名称
version: string     # 语义化版本 "X.Y"
date: string        # YYYY-MM-DD
status: string      # active | deprecated

# 选填字段
source: string      # internal | external | merged
applies_to: [string]    # 适用场景列表
references: [string]    # 关联的技能章节或其他条目
supersedes: string      # 替代的旧条目 id
deprecated_by: string   # 被哪个新条目替代（如已废弃）
```

#### L2 模板库 Schema

```yaml
id: string              # 唯一标识符
level: "L2"
name: string
version: string
date: string
status: string
report_type: string     # monthly | quarterly | special | board | fund | cash-flow
sections: [string]      # 章节结构列表
format_ref: string      # 引用的格式规范，如 [L2:gb-t9704-spec]
```

#### L2.5 任务模板库 Schema

```yaml
id: string              # 唯一标识符
level: "L2.5"
name: string
version: string
date: string
status: string           # draft | validated | stable
task_type: string       # 任务类型
run_count: integer      # 已验证运行次数
template_ref: string    # 产出的 L2 模板引用
validation_status: string  # unverified | partially-verified | verified
```

#### L3 案例库 Schema

```yaml
id: string              # 唯一标识符
level: "L3"
name: string
date: string
source_type: string     # refined | external（对应 [提炼] / [原文]
status: string
data_source: string     # simulated | real-masked | public
scenario: string        # 场景描述
key_findings: [string]  # 关键发现
reusable_points: [string]  # 可复用要点
```

#### L4 决策日志 Schema

```yaml
id: string              # DEC-YYYYMMDD-NNN
level: "L4"
name: string
date: string
status: string
gate: string            # Gate-H | Gate-H-strict
decision_type: string   # threshold-adjustment | process-change | other
context: string         # 决策上下文
options: [string]       # 选项列表
decision: string        # 最终决策
outcome: string         # 结果复盘（待填充）
```

### 3.3 兼容性说明

- 已有 KB 条目使用引用块格式（`> 效力等级：...`）的，保持兼容，不强制回溯改写
- 新增条目**必须**使用 YAML frontmatter 格式
- 校验脚本同时支持两种格式

---

## 4. 引用语法规范

### 4.1 统一引用格式

库间引用使用以下统一格式：

```
[L{level}:{file-id}#{anchor}]
```

| 组成 | 说明 | 示例 |
|------|------|------|
| `L{level}` | 库级别 | `L1`、`L2`、`L2.5`、`L3`、`L4` |
| `{file-id}` | 文件的 id 字段（与文件名一致，不含 `.md`） | `anomaly-thresholds`、`data-masking` |
| `#{anchor}` | 锚点（可选），指向文件内特定章节 | `#3.1`、`#四双方案机制` |

### 4.2 正确示例

```
[L1:anomaly-thresholds#3.1]        → 引用异常阈值标准的制水成本章节
[L1:data-masking#四]               → 引用脱敏标准的双方案机制
[L2:monthly-analysis]              → 引用月度分析模板（整体）
[L2.5:monthly-budget-analysis]     → 引用月度预算执行分析任务模板
[L3:case-006-budget-variance]      → 引用预算差异归因案例
[L4:DEC-20260730-001]              → 引用特定决策日志
```

### 4.3 禁止的引用格式

| 错误格式 | 问题 | 正确格式 |
|---------|------|---------|
| `[L1:脱敏标准清单]` | 使用中文名而非 file-id | `[L1:data-masking]` |
| `[L1:异常阈值标准#3.1制水成本-电费]` | 锚点含中文 | `[L1:anomaly-thresholds#3.1]` |
| `kb/L1-rules/anomaly-thresholds.md` | 直接路径引用 | `[L1:anomaly-thresholds]` |

### 4.4 引用与文件路径的关系

引用语法是**语义引用**，不是文件路径。AI 在解析引用时按以下规则映射：

```
[L1:anomaly-thresholds]  →  kb/L1-rules/anomaly-thresholds.md
[L2:monthly-analysis]    →  kb/L2-templates/monthly-analysis.md
[L3:case-001-monthly]   →  kb/L3-cases/case-001-monthly.md
```

映射规则：`L{level}:{id}` → `kb/L{level-dir}/{id}.md`

---

## 5. 适配器接口规范

### 5.1 适配器必须提供的文件

每个适配器目录**必须**包含以下文件：

| 文件 | 必须 | 说明 |
|------|------|------|
| `README.md` | 是 | 安装指南、使用示例、平台注意事项 |
| `SKILL.md` 或等效指令文件 | 条件必须 | 如果平台支持 skill/instruction 文件格式，则必须提供 |

> **条件必须**：若平台不支持独立指令文件（如 ChatGPT Custom GPT 只能粘贴到 Instructions），README.md 中需明确说明替代加载方式。

### 5.2 README.md 必须包含的章节

```markdown
# {Platform} Adapter

## 安装
[逐步安装指南，含截图描述或步骤编号]

## 使用
[至少 2 个使用示例]

## 注意事项
[平台特有的限制、文件数量上限、安全性提示]
```

### 5.3 SKILL.md frontmatter 规范

```yaml
---
name: cfo-command-center          # 固定名称
version: v{项目版本}               # 与 VERSION.json 一致
description: |
  财务总监指挥台 · FinanceOS 双轴认知操作系统的调度中枢。
  [与 core/FINANCEOS_SYSTEM.md 定位一致的简述]
---
```

### 5.4 适配器目录命名

```
adapters/{platform-name}/
```

`{platform-name}` 使用全小写英文 + 连字符：`chatgpt`、`claude`、`workbuddy`、`generic`、`gemini`、`cursor` 等。

### 5.5 新增适配器检查清单

- [ ] 目录名为全小写英文 kebab-case
- [ ] `README.md` 包含安装、使用、注意事项三章
- [ ] 如平台支持指令文件，已提供 `SKILL.md` 或等效文件
- [ ] frontmatter 中的 `version` 与 `core/VERSION.json` 一致
- [ ] 在 `adapters/README.md` 的平台对照表中注册
- [ ] 在 `docs/getting-started.md` 的平台对照表中注册

---

## 6. 跨文件一致性规则

### 6.1 版本号一致性

| 校验项 | 规则 |
|--------|------|
| README.md badge | 必须与 `VERSION.json.version` 一致 |
| FINANCEOS_SYSTEM.md 标题 | `v{X.Y}` 必须与 `VERSION.json` 一致 |
| SKILL.md frontmatter | `version: v{X.Y}` 必须与 `VERSION.json` 一致 |
| CHANGELOG.md 最新条目 | 版本号必须与 `VERSION.json` 一致 |
| architecture.md 标题 | 必须与 `VERSION.json` 一致 |

### 6.2 术语一致性

| 校验项 | 规则 |
|--------|------|
| Gate 术语 | 全仓库不得出现 T1/T2/T3/T4（CHANGELOG.md 历史记录除外） |
| 目录名 | 全仓库不得出现中文目录名引用（operations-manual.md 等） |
| 文件引用 | 引用 KB 文件时必须使用 `[L{level}:{file-id}]` 语法，不使用中文文件名 |

### 6.3 文件路径一致性

| 校验项 | 规则 |
|--------|------|
| operations-manual.md 中的路径 | 必须与实际仓库文件路径一致 |
| kb-framework.md 中的路径 | 必须与实际仓库文件路径一致 |
| SKILL.md 中的路径 | 必须与实际仓库文件路径一致 |
| 所有文档中的路径 | 使用 `{FINANCEOS_KB_ROOT}` 变量或相对仓库根目录的路径 |

### 6.4 KB 引用完整性

| 校验项 | 规则 |
|--------|------|
| 每个引用 `[L{level}:{id}]` | 被引用的文件必须存在 |
| 引用的锚点 | 被引用的锚点应存在于目标文件中（警告级，不阻断） |
| 文件 id 唯一性 | 同一级别内不允许重复 id |

---

## 7. 目录结构规范

### 7.1 标准目录结构

```
financeos/
├── core/
│   ├── FINANCEOS_SYSTEM.md     # 核心指令集
│   └── VERSION.json            # 版本真相源
├── kb/
│   ├── README.md               # KB 索引与说明
│   ├── _contrib/               # 社区贡献模板
│   ├── L1-rules/               # 规则库（强制约束）
│   ├── L2-templates/           # 模板库（形式规范）
│   ├── L2.5-task-templates/    # 任务模板库（编排复用）
│   ├── L3-cases/               # 案例库（方法参考）
│   └── L4-decision-logs/       # 决策日志（追溯记录）
├── data-buffer/
│   ├── README.md
│   ├── templates/              # CSV 数据模板
│   └── input/                 # 用户数据输入（.gitignore）
├── output/                    # 产出区（报告成果，.gitignore）
│   └── {YYYY-MM-DD}_{task}/  # 按任务名归档
├── adapters/
│   ├── README.md               # 适配器索引
│   ├── workbuddy/
│   ├── chatgpt/
│   ├── claude/
│   └── generic/
├── docs/
│   ├── architecture.md
│   ├── getting-started.md
│   ├── operations-manual.md
│   ├── kb-framework.md
│   ├── dual-axis-model.md
│   ├── domain-adaptation.md
│   └── glossary.md
├── examples/
│   └── water-utility/
├── tools/                      # 校验工具
│   └── validate_kb.py
├── SPEC.md                     # 本文件
├── README.md
├── CONTRIBUTING.md
├── CHANGELOG.md
├── CODE_OF_CONDUCT.md
└── LICENSE
```

### 7.2 新增目录规则

- 顶级目录需 Core Maintainer 审核
- `kb/` 子目录名必须与现有命名风格一致（`L{level}-{category}/`）
- `adapters/` 子目录名必须为平台英文名 kebab-case
- `examples/` 子目录名为领域英文名 kebab-case

---

## 8. 变更管理流程

### 8.1 变更分类

| 变更类型 | 影响范围 | 审核要求 | 版本递增 |
|---------|---------|---------|---------|
| 核心系统变更 | `core/` | 2 位 Core Maintainer | MINOR 或 MAJOR |
| KB 新增 | `kb/` | 1 位 Maintainer | PATCH |
| 适配器新增 | `adapters/` | 1 位 Maintainer | PATCH |
| 文档修正 | `docs/` | 1 位 Maintainer | 无（或 PATCH） |
| 规范变更 | `SPEC.md` | 2 位 Core Maintainer | PATCH |

### 8.2 PR 提交规范

```markdown
## 变更说明
- 做了什么
- 为什么做

## 影响范围
- [ ] 核心系统文件（core/）
- [ ] 知识库（kb/）
- [ ] 适配器（adapters/）
- [ ] 文档（docs/）
- [ ] 规范（SPEC.md）

## 校验
- [ ] 运行 `python tools/validate_kb.py` 通过
- [ ] 版本号一致性检查通过
- [ ] 在至少一个 AI 平台上验证通过（KB/适配器变更时）
```

### 8.3 版本发布流程

1. 更新 `core/VERSION.json`（version、release_date、changelog）
2. 更新 `README.md` 的 version badge
3. 更新 `core/FINANCEOS_SYSTEM.md` 标题版本号
4. 更新 `adapters/workbuddy/SKILL.md` frontmatter 版本号
5. 在 `CHANGELOG.md` 添加新条目
6. 运行 `python tools/validate_kb.py` 确认通过
7. 创建 git tag `v{X.Y.Z}`

---

## 9. 校验工具

### 9.1 校验脚本

位于 `tools/validate_kb.py`，使用纯 Python 标准库，无外部依赖。

```bash
# 运行校验
python tools/validate_kb.py

# 指定仓库根目录（默认为脚本上级目录）
python tools/validate_kb.py --root /path/to/financeos

# CI/CD 集成（退出码 0=通过，1=失败）
python tools/validate_kb.py && echo "PASS" || echo "FAIL"
```

### 9.2 校验项

| 校验项 | 级别 | 说明 |
|--------|------|------|
| 版本号一致性 | error | VERSION.json 与各文件引用的版本号比对 |
| 目录名规范 | error | 目录名必须为英文 kebab-case |
| 文件名规范 | error | KB 文件名必须为英文 kebab-case |
| KB 引用完整性 | error | 每个引用指向的文件必须存在 |
| 文件 id 唯一性 | error | 同级内 id 不得重复 |
| 术语一致性 | error | 不应出现 T1/T2/T3/T4（CHANGELOG 除外） |
| frontmatter 合规 | warn | 新增条目推荐使用 YAML frontmatter |
| 引用锚点存在性 | warn | 引用的锚点应存在于目标文件中 |
| 适配器完整性 | error | 每个适配器必须包含 README.md |
| 适配器注册 | warn | 适配器应在 adapters/README.md 中注册 |

---

*— FinanceOS Specification v1.0 · 完 —*
