# Changelog

All notable changes to FinanceOS will be documented in this file.

## [2.4.1] - 2026-08-01

### Fixed
- 修复 `adapters/generic/README.md` 最小化安装示例中的断链：`core/FINANCEOS_SYSTEM.md` → `../../core/FINANCEOS_SYSTEM.md`（原相对路径在 GitHub 上 404）
- 修复 `tools/validate_kb.py` 误扫 `.trae/` 等 IDE 目录导致本地校验误报 8 个 T1-T4 ERROR 的问题：`list_md_files` 现跳过 `.git` / `.trae` / `.vscode` / `.idea` / `node_modules` / `__pycache__`，本地 QA 不再被 gitignore 的规划文档污染
- 修复 `tools/validate_kb.py` 对 generic 适配器误报 "not registered" 的问题：注册检查现同时解析 `adapters/README.md` 表格第二列的目录链接，使中文显示名"通用"正确映射到真实目录 `generic`
- 补全 `INSTALL.md` 验证步骤的触发词表（3/5 → 5/5，补 `/gongwen`、`/ask`），与 README.md / skills/README.md 保持一致
- 清理 KB 与文档中残留的 cfo-command-center 旧内部版本号引用（`v4.1` → `v2.4.1`）：`docs/operations-manual.md` 适用版本、`docs/kb-framework.md` 衔接机制标题、`kb/L1-rules/anomaly-thresholds.md` 与 `kb/L4-decision-logs/template.md` 的章节关联（`kb-framework.md` 推进进度日志中的 `v4.1` 作为 2026-07-30 dated 历史记录保留）
- 修正现金流分析 SKILL 的来源合规声称：原标注来源 `virattt/dexter` 为 MIT 许可，实际该仓库无任何 LICENSE 文件（GitHub API `/repos/virattt/dexter/license` 返回 404，默认 All Rights Reserved），违反"来源项目须 MIT/Apache-2.0"硬约束。现将现金流分析 SKILL 重声明为 **FinanceOS 原创**方法论（无外部来源项目），同步更新 `skills/cashflow-analysis/SKILL.md`、`skills/README.md`、`README.md` 的来源与合规描述

### Changed
- 版本号 2.4.0 → 2.4.1，同步更新 VERSION.json / README badge / 系统指令标题 / 各 SKILL.md frontmatter / SPEC 当前基准 / operations-manual 版本戳

## [2.4.0] - 2026-07-31

### Changed — 去平台化（Block 2）
- Removed QoderWork residuals from `docs/architecture.md` (async-dialog and token-monitor notes generalized to "AI platform")
- Removed DuMate citations from `kb/L1-rules/permission-tiers.md` (data-classification matrix now stands on its own) and `core/VERSION.json`
- Generalized hardcoded `~/.workbuddy/financeos-kb/` paths to the `{FINANCEOS_KB_ROOT}` variable across core files (`core/FINANCEOS_SYSTEM.md`, `adapters/workbuddy/SKILL.md`, `docs/operations-manual.md`); WorkBuddy remains as one legitimate adapter among equals
- Rewrote `docs/getting-started.md` as a three-step universal install with a 7-platform comparison table (Claude / ChatGPT / WorkBuddy / Cursor / Trae CN / Claude Code / Local LLM / Generic)
- README core positioning restated: "面向国企 CFO 的 AI 财务指令集，可运行在任何支持 Markdown 指令的 AI 平台"

### Changed — Prompt 精简（Block 3）
- Simplified `adapters/workbuddy/SKILL.md` per four iron rules (指令先于解释 / 一条≤3行 / 删除重复约束 / 动词开头); line count reduced ≥30%; routing logic (Step0 模式判别 + 意图识别 + 双轴编排 + STOP gate) preserved

### Changed — STOP Gate 细化（Block 4）
- Refined STOP Gate from T1/T2/T3(/T4) to a unified four-level **Gate-L/M/H/X** scheme across `kb/L1-rules/permission-tiers.md`, `core/FINANCEOS_SYSTEM.md`, `adapters/workbuddy/SKILL.md`, `adapters/generic/README.md`, `docs/architecture.md`, `docs/operations-manual.md`
- Added new **Gate-X (禁止)** tier for delete/modify-original-data operations — SOE financial compliance baseline (original data must not be tampered with)
- Mapping: T1→Gate-L, T2→Gate-M, T3→Gate-H, T4→Gate-H (stricter sub-requirements preserved), new Gate-X

### Notes
- Local environment has no git; v2.4 changes are uncommitted (to be committed when git is available)

## [2.3.0] - 2026-07-31

### Added
- **L1 Rules** (3 → 8): output-standards, fund-management, cost-control, regulatory-requirements, chart-of-accounts
- **L2 Templates** (3 → 7): board-materials, fund-plan, gb-t9704-spec, cash-flow-analysis
- **L3 Cases** (4 → 11): profit-vs-cashflow, budget-variance, ar-risk, investment, tax-risk, cost-overrun, capex-variance (DuMate revenue-variance merged into budget-variance)
- **Data Staging Area** (`data-buffer/`): dedicated input channel for non-ERP users with CSV templates (budget, income statement, balance sheet)
- **KB Contribution Templates** (`kb/_contrib/`): rule/template/case templates + pre-submission checklist to lower community contribution barrier
- Enhanced data-masking rule: 9 → 12 categories, dual-scheme mechanism (A/B), anti-inference protection
- GB/T 9704-2012 document format specification for compliant report generation

### Changed
- data-masking.md upgraded from v1 to v2 (12 categories, dual schemes, anti-inference)
- permission-tiers.md supplemented with DuMate 4-level data classification matrix (L1-L4)
- Merged DuMate revenue-variance into case-006; merged DuMate rigid-spending & flood-emergency into case-002
- KB README updated with complete file index; README counts corrected to L2=7, L3=11
- Core system prompt bumped to v2.3; added data-buffer reference in domain-adaptation guide

### Sources
- Knowledge content merged from FinanceOS_WorkBuddy (battle-tested rules, templates, cases)
- Industry-depth content merged from FinanceOS-DuMate (desensitization, regulatory, chart-of-accounts)

## [2.2.0] - 2026-07-30

### Added
- Platform-agnostic core system prompt (`core/FINANCEOS_SYSTEM.md`)
- Multi-platform adapters (WorkBuddy, ChatGPT, Claude, Generic)
- Contribution guidelines and community governance model
- Domain adaptation guide for non-water-utility industries
- Dual-axis cognitive model documentation
- Glossary of terms
- STOP gate presets (internal analysis vs external reporting)

### Changed
- **BREAKING**: Renamed KB files to English for cross-platform compatibility
- Restructured repository for open-source best practices
- Simplified architecture documentation for public consumption
- Merged audit checker role into data analyst (company has dedicated internal audit)
- Lifecycle reduced from 6 to 5 stages (verification merged into execution)
- Role axis reduced from 7 to 5 roles
- Verification retry reduced from 3 to 2 rounds

### Fixed
- Emergency channel false positives (single-character triggers removed)
- Dual-condition trigger for emergency mode detection

### Security
- Added CODE_OF_CONDUCT.md
- Explicit MIT license

## [2.1.0] - 2026-07-29

### Added
- Audit three-tier grading (T1-T4)
- STOP gate mechanism
- Preset plans for internal/external reporting

### Changed
- Weakened audit requirements per organizational structure

## [2.0.0] - 2026-07-28

### Added
- Dual-axis cognitive model (role axis × lifecycle axis)
- 3+2 library system (L1 rules, L2 templates, L3 cases + data buffer)
- Finance Director Agent as scheduling center
- Merged Dumat gstack paradigm with FinanceOS

## [1.0.0] - 2026-07-25

### Added
- Initial GPT-based enterprise architecture design
- Basic finance analysis framework for SOE water utilities
