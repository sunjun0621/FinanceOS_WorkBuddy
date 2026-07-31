# Changelog

All notable changes to FinanceOS will be documented in this file.

## [2.3.0] - 2026-07-31

### Added
- **L1 Rules** (3 → 8): output-standards, fund-management, cost-control, regulatory-requirements, chart-of-accounts
- **L2 Templates** (3 → 7): board-materials, fund-plan, gb-t9704-spec, cash-flow-analysis
- **L3 Cases** (4 → 11): profit-vs-cashflow, budget-variance, ar-risk, investment, tax-risk, cost-overrun, capex-variance (DuMate revenue-variance merged into budget-variance)
- **Data Staging Area** (`data-staging/`): dedicated input channel for non-ERP users with CSV templates (budget, income statement, balance sheet)
- **KB Contribution Templates** (`kb/_contrib/`): rule/template/case templates + pre-submission checklist to lower community contribution barrier
- Enhanced data-masking rule: 9 → 12 categories, dual-scheme mechanism (A/B), anti-inference protection
- GB/T 9704-2012 document format specification for compliant report generation

### Changed
- data-masking.md upgraded from v1 to v2 (12 categories, dual schemes, anti-inference)
- permission-tiers.md supplemented with DuMate 4-level data classification matrix (L1-L4)
- Merged DuMate revenue-variance into case-006; merged DuMate rigid-spending & flood-emergency into case-002
- KB README updated with complete file index; README counts corrected to L2=7, L3=11
- Core system prompt bumped to v2.3; added data-staging reference in domain-adaptation guide

### Sources
- Knowledge content merged from FinanceOS_QoderWork (battle-tested rules, templates, cases)
- Industry-depth content merged from FinanceOS-DuMate (desensitization, regulatory, chart-of-accounts)

## [2.2.0] - 2026-07-31

### Added
- Platform-agnostic core system prompt (`core/FINANCEOS_SYSTEM.md`)
- Multi-platform adapters (WorkBuddy, ChatGPT, Claude, Generic)
- Contribution guidelines and community governance model
- Domain adaptation guide for non-water-utility industries
- Dual-axis cognitive model documentation
- Glossary of terms

### Changed
- **BREAKING**: Renamed KB files to English for cross-platform compatibility
- Restructured repository for open-source best practices
- Simplified architecture documentation for public consumption

### Security
- Added CODE_OF_CONDUCT.md
- Explicit MIT license

## [2.2.0-pre] - 2026-07-30

### Changed
- Merged audit checker role into data analyst (company has dedicated internal audit)
- Lifecycle reduced from 6 to 5 stages (verification merged into execution)
- Role axis reduced from 7 to 5 roles
- Verification retry reduced from 3 to 2 rounds
- Added STOP gate presets (internal analysis vs external reporting)

### Fixed
- Emergency channel false positives (single-character triggers removed)
- Dual-condition trigger for emergency mode detection

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
