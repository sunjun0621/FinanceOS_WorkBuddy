#!/usr/bin/env python3
"""
FinanceOS KB Validator
=====================
Checks: version consistency, file naming, directory naming, reference integrity,
term consistency, adapter completeness. Pure standard library, no dependencies.

Usage:
    python tools/validate_kb.py                    # validate current repo
    python tools/validate_kb.py --root /path/to    # validate specific path
    python tools/validate_kb.py --verbose          # show warnings too

Exit codes: 0 = pass, 1 = errors found
"""

import argparse
import json
import os
import re
import sys
from pathlib import Path
from dataclasses import dataclass, field
from typing import List, Dict, Set, Tuple, Optional


# ---------------------------------------------------------------------------
# Data structures
# ---------------------------------------------------------------------------

@dataclass
class Issue:
    level: str          # "error" or "warn"
    file: str           # relative path
    line: int           # line number (1-based), 0 if N/A
    check: str          # check name
    message: str        # human-readable message


@dataclass
class ValidationResult:
    errors: List[Issue] = field(default_factory=list)
    warnings: List[Issue] = field(default_factory=list)

    def add_error(self, file, line, check, message):
        self.errors.append(Issue("error", file, line, check, message))

    def add_warning(self, file, line, check, message):
        self.warnings.append(Issue("warn", file, line, check, message))

    @property
    def passed(self):
        return len(self.errors) == 0


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def read_lines(filepath: Path) -> List[str]:
    """Read file lines with UTF-8 fallback."""
    for enc in ("utf-8", "utf-8-sig", "gbk", "latin-1"):
        try:
            with open(filepath, "r", encoding=enc) as f:
                return f.readlines()
        except (UnicodeDecodeError, UnicodeError):
            continue
    return []


def list_md_files(root: Path) -> List[Path]:
    """List all .md files excluding .git and node_modules."""
    result = []
    for p in root.rglob("*.md"):
        parts = str(p.relative_to(root))
        if ".git" in parts or "node_modules" in parts:
            continue
        result.append(p)
    return result


# ---------------------------------------------------------------------------
# Check 1: Version consistency
# ---------------------------------------------------------------------------

def check_version_consistency(root: Path, result: ValidationResult):
    """Verify version numbers are consistent across files."""
    version_file = root / "core" / "VERSION.json"
    if not version_file.exists():
        result.add_error("core/VERSION.json", 0, "version", "VERSION.json not found")
        return

    try:
        with open(version_file, "r", encoding="utf-8") as f:
            vdata = json.load(f)
        project_version = vdata.get("version", "")
    except (json.JSONDecodeError, OSError) as e:
        result.add_error("core/VERSION.json", 0, "version", f"Cannot parse VERSION.json: {e}")
        return

    if not project_version:
        result.add_error("core/VERSION.json", 0, "version", "version field is empty")
        return

    # README.md badge
    readme = root / "README.md"
    if readme.exists():
        lines = read_lines(readme)
        for i, line in enumerate(lines, 1):
            if "img.shields.io/badge/version" in line:
                # Extract version from badge URL
                m = re.search(r"version-([^-]+)-blue", line)
                if m:
                    badge_ver = m.group(1)
                    if badge_ver != project_version:
                        result.add_error(
                            "README.md", i, "version",
                            f"Badge version '{badge_ver}' != VERSION.json '{project_version}'"
                        )
                break

    # core/FINANCEOS_SYSTEM.md title
    sysfile = root / "core" / "FINANCEOS_SYSTEM.md"
    if sysfile.exists():
        lines = read_lines(sysfile)
        for i, line in enumerate(lines, 1):
            if line.startswith("# ") and "FinanceOS System Prompt" in line:
                m = re.search(r"v(\d+\.\d+)", line)
                if m:
                    sys_ver = m.group(1)
                    proj_major_minor = ".".join(project_version.split(".")[:2])
                    if sys_ver != proj_major_minor:
                        result.add_error(
                            "core/FINANCEOS_SYSTEM.md", i, "version",
                            f"Title version 'v{sys_ver}' != VERSION.json 'v{proj_major_minor}'"
                        )
                break

    # adapters/workbuddy/SKILL.md frontmatter
    skill_file = root / "adapters" / "workbuddy" / "SKILL.md"
    if skill_file.exists():
        lines = read_lines(skill_file)
        for i, line in enumerate(lines[:20], 1):
            if "version:" in line and "v" in line:
                m = re.search(r"version:\s*v?([\d.]+)", line)
                if m:
                    skill_ver = m.group(1)
                    skill_major_minor = ".".join(skill_ver.split(".")[:2])
                    proj_major_minor = ".".join(project_version.split(".")[:2])
                    if skill_major_minor != proj_major_minor:
                        result.add_error(
                            "adapters/workbuddy/SKILL.md", i, "version",
                            f"SKILL.md version 'v{skill_ver}' != VERSION.json 'v{project_version}'"
                        )
                break

    # CHANGELOG.md latest entry
    changelog = root / "CHANGELOG.md"
    if changelog.exists():
        lines = read_lines(changelog)
        for i, line in enumerate(lines, 1):
            m = re.match(r"##\s*\[([\d.]+)\]", line)
            if m:
                cl_ver = m.group(1)
                if cl_ver != project_version:
                    result.add_error(
                        "CHANGELOG.md", i, "version",
                        f"Latest changelog entry '[{cl_ver}]' != VERSION.json '{project_version}'"
                    )
                break

    # architecture.md title
    arch_file = root / "docs" / "architecture.md"
    if arch_file.exists():
        lines = read_lines(arch_file)
        for i, line in enumerate(lines[:20], 1):
            if line.startswith("# ") and "FinanceOS" in line:
                m = re.search(r"V(\d+\.\d+)", line)
                if m:
                    arch_ver = m.group(1)
                    proj_major_minor = ".".join(project_version.split(".")[:2])
                    if arch_ver != proj_major_minor:
                        result.add_error(
                            "docs/architecture.md", i, "version",
                            f"Title 'V{arch_ver}' != VERSION.json 'v{proj_major_minor}'"
                        )
                break


# ---------------------------------------------------------------------------
# Check 2: Directory naming (must be English kebab-case)
# ---------------------------------------------------------------------------

CHINESE_DIR_PATTERN = re.compile(r"[\u4e00-\u9fff]+")

def check_directory_naming(root: Path, result: ValidationResult):
    """Check that all directories under kb/ use English kebab-case."""
    kb_dir = root / "kb"
    if not kb_dir.exists():
        return

    expected_dirs = {
        "L1-rules", "L2-templates", "L2.5-task-templates",
        "L3-cases", "L4-decision-logs", "_contrib"
    }

    # Check actual directories
    actual_dirs = set()
    for item in kb_dir.iterdir():
        if item.is_dir():
            actual_dirs.add(item.name)

    # Check for Chinese characters in directory names
    for d in actual_dirs:
        if CHINESE_DIR_PATTERN.search(d):
            result.add_error(
                f"kb/{d}/", 0, "dir-naming",
                f"Directory name contains non-ASCII characters: '{d}'. Use English kebab-case."
            )

    # Check expected directories exist
    for expected in expected_dirs:
        if expected not in actual_dirs:
            result.add_warning(
                "kb/", 0, "dir-naming",
                f"Expected directory 'kb/{expected}/' not found"
            )


# ---------------------------------------------------------------------------
# Check 3: File naming (KB files must be English kebab-case)
# ---------------------------------------------------------------------------

def check_file_naming(root: Path, result: ValidationResult):
    """Check that KB files use English kebab-case naming."""
    kb_dir = root / "kb"
    if not kb_dir.exists():
        return

    kb_subdirs = ["L1-rules", "L2-templates", "L2.5-task-templates", "L3-cases", "L4-decision-logs"]

    for subdir in kb_subdirs:
        d = kb_dir / subdir
        if not d.exists():
            continue
        for f in d.iterdir():
            if f.is_file() and f.suffix == ".md":
                name = f.stem
                # Check for Chinese characters
                if CHINESE_DIR_PATTERN.search(name):
                    result.add_error(
                        str(f.relative_to(root)), 0, "file-naming",
                        f"File name contains non-ASCII characters: '{f.name}'. Use English kebab-case."
                    )
                # Check for version numbers in filename
                if re.search(r"_v\d|version|\d+\.\d+", name, re.IGNORECASE):
                    result.add_warning(
                        str(f.relative_to(root)), 0, "file-naming",
                        f"File name may contain version number: '{f.name}'. Version belongs in frontmatter."
                    )


# ---------------------------------------------------------------------------
# Check 4: Reference integrity ([L{level}:{id}] must point to existing files)
# ---------------------------------------------------------------------------

REF_PATTERN = re.compile(r"\[L(\d(?:\.\d)?):([a-zA-Z0-9\-]+)(?:#([^\]]+))?\]")

def get_kb_file_map(root: Path) -> Dict[str, Path]:
    """Build a map of file-id -> path for all KB files."""
    kb_dir = root / "kb"
    file_map = {}

    if not kb_dir.exists():
        return file_map

    level_dirs = {
        "1": "L1-rules",
        "2": "L2-templates",
        "2.5": "L2.5-task-templates",
        "3": "L3-cases",
        "4": "L4-decision-logs",
    }

    for level, dirname in level_dirs.items():
        d = kb_dir / dirname
        if d.exists():
            for f in d.glob("*.md"):
                file_map[(level, f.stem)] = f

    return file_map


def check_reference_integrity(root: Path, result: ValidationResult):
    """Check that all [L{level}:{id}] references point to existing files."""
    file_map = get_kb_file_map(root)
    md_files = list_md_files(root)

    # Skip template files and SPEC.md - they contain example references
    SKIP_FILES = {"_contrib/checklist.md", "_contrib/case-template.md",
                  "_contrib/rule-template.md", "_contrib/template-template.md"}
    # Also skip example patterns like xxx, rule-name, template-name, case-name
    SKIP_IDS = {"xxx", "rule-name", "template-name", "case-name", "DEC-YYYYMMDD-001",
                "DEC-20260730-001"}

    for filepath in md_files:
        rel_path = str(filepath.relative_to(root))
        # Skip contrib templates
        if any(s in rel_path for s in SKIP_FILES):
            continue
        if "SPEC.md" in rel_path:
            continue
        # Skip L4 template (it has example references)
        if "L4-decision-logs/template.md" in rel_path:
            continue

        lines = read_lines(filepath)
        for i, line in enumerate(lines, 1):
            for m in REF_PATTERN.finditer(line):
                level = m.group(1)
                file_id = m.group(2)

                # Skip example/placeholder IDs
                if file_id in SKIP_IDS:
                    continue

                key = (level, file_id)
                if key not in file_map:
                    result.add_error(
                        rel_path, i, "ref-integrity",
                        f"Reference [L{level}:{file_id}] points to non-existent file"
                    )


# ---------------------------------------------------------------------------
# Check 5: File ID uniqueness within each level
# ---------------------------------------------------------------------------

def check_id_uniqueness(root: Path, result: ValidationResult):
    """Check that file IDs are unique within each KB level."""
    file_map = get_kb_file_map(root)
    seen = {}

    for (level, file_id), path in file_map.items():
        if file_id in seen:
            existing = seen[file_id]
            if existing[0] == level:
                result.add_error(
                    str(path.relative_to(root)), 0, "id-uniqueness",
                    f"Duplicate file ID '{file_id}' in L{level} (also in {existing[1]})"
                )
        else:
            seen[file_id] = (level, str(path.relative_to(root)))


# ---------------------------------------------------------------------------
# Check 6: Term consistency (no T1/T2/T3/T4 outside CHANGELOG)
# ---------------------------------------------------------------------------

DEPRECATED_TERMS = [
    (re.compile(r"\bT1\b(?![-\w])", re.UNICODE), "T1", "Gate-L"),
    (re.compile(r"\bT2\b(?![-\w])", re.UNICODE), "T2", "Gate-M"),
    (re.compile(r"\bT3\b(?![-\w])", re.UNICODE), "T3", "Gate-H"),
    (re.compile(r"\bT4\b(?![-\w])", re.UNICODE), "T4", "Gate-H (strict)"),
]

# Contexts where T1-T4 are legitimate historical references, not current usage
HISTORICAL_CONTEXT = re.compile(r"(原\s*T[1-4]|T[1-4].*→.*Gate|映射|V\d\.\d|变更|变更明细|前序|version)", re.UNICODE)

def check_term_consistency(root: Path, result: ValidationResult):
    """Check that deprecated T1-T4 terms don't appear outside CHANGELOG/historical context."""
    md_files = list_md_files(root)

    for filepath in md_files:
        rel_path = str(filepath.relative_to(root))
        if "CHANGELOG" in rel_path:
            continue
        # Skip SPEC.md (it documents the mapping as a reference table)
        if "SPEC.md" in rel_path:
            continue

        lines = read_lines(filepath)
        for i, line in enumerate(lines, 1):
            # Skip lines in historical/version evolution context
            if HISTORICAL_CONTEXT.search(line):
                continue
            for pattern, old_term, new_term in DEPRECATED_TERMS:
                if pattern.search(line):
                    result.add_error(
                        rel_path, i, "term-consistency",
                        f"Deprecated term '{old_term}' found. Use '{new_term}' instead."
                    )


# ---------------------------------------------------------------------------
# Check 7: Adapter completeness
# ---------------------------------------------------------------------------

def check_adapters(root: Path, result: ValidationResult):
    """Check that each adapter directory has required files."""
    adapters_dir = root / "adapters"
    if not adapters_dir.exists():
        return

    adapters_readme = adapters_dir / "README.md"
    registered = set()

    if adapters_readme.exists():
        lines = read_lines(adapters_readme)
        for line in lines:
            m = re.search(r"\|\s*\[?(\w+)\]?\s*\|.*\|", line)
            if m and m.group(1) not in ("平台", "Platform", "---"):
                registered.add(m.group(1).lower())

    for item in adapters_dir.iterdir():
        if not item.is_dir() or item.name.startswith("."):
            continue
        platform = item.name

        # Must have README.md
        readme = item / "README.md"
        if not readme.exists():
            result.add_error(
                f"adapters/{platform}/", 0, "adapter-completeness",
                f"Adapter '{platform}' missing README.md"
            )

        # Should be registered in adapters/README.md
        if platform.lower() not in registered and registered:
            result.add_warning(
                f"adapters/{platform}/", 0, "adapter-registration",
                f"Adapter '{platform}' not registered in adapters/README.md"
            )


# ---------------------------------------------------------------------------
# Check 8: Chinese path references in docs
# ---------------------------------------------------------------------------

# Chinese terms that are ONLY problematic when used as path references (with / or .md suffix)
# vs. terms that are problematic in any path-like context
CHINESE_PATH_DIRS = [
    "L1-规则库/", "L2-模板库/", "L2.5-任务模板库/", "L3-案例库/", "L4-决策日志/",
    "数据缓冲区/",
]

# Deprecated path references (renamed directories)
DEPRECATED_PATHS = [
    ("data-staging", "data-buffer"),
]

# Chinese filenames - problematic when referenced as paths (with .md or in path context)
CHINESE_PATH_FILES = [
    "脱敏标准清单.md", "权限分级.md", "异常阈值标准.md",
    "三库框架规范_v1.md",
    "决策日志记录模板",
]

# Chinese template names used in comments/metadata - warn only
CHINESE_TEMPLATE_NAMES = [
    "月度经营分析模板", "季度财务分析报告模板", "专项财务分析报告模板",
    "月度预算执行分析_任务模板", "月度预算执行分析_案例",
    "季度财务分析_案例",
]

def check_chinese_path_refs(root: Path, result: ValidationResult):
    """Check that docs don't reference Chinese file/directory names as paths."""
    md_files = list_md_files(root)

    for filepath in md_files:
        rel_path = str(filepath.relative_to(root))
        # Skip SPEC.md and CHANGELOG (they legitimately reference old names)
        if "SPEC.md" in rel_path:
            continue
        if "CHANGELOG" in rel_path:
            continue

        lines = read_lines(filepath)
        for i, line in enumerate(lines, 1):
            # Error: Chinese directory names used as paths
            for ref in CHINESE_PATH_DIRS:
                if ref in line:
                    result.add_error(
                        rel_path, i, "chinese-path",
                        f"Chinese directory reference '{ref}' found. Use English name."
                    )
            # Error: Chinese filenames referenced as paths
            for ref in CHINESE_PATH_FILES:
                if ref in line:
                    result.add_error(
                        rel_path, i, "chinese-path",
                        f"Chinese filename reference '{ref}' found. Use English filename."
                    )
            # Warning: Chinese template names in metadata/comments
            for ref in CHINESE_TEMPLATE_NAMES:
                if ref in line:
                    result.add_warning(
                        rel_path, i, "chinese-path",
                        f"Chinese template name '{ref}' found. Consider using English filename."
                    )
            # Error: Deprecated path references (renamed directories)
            # Skip if line is in a historical/version evolution context
            is_historical = any(kw in line for kw in ("V1.", "V2.", "v2.", "原 ", "更名为", "历史", "changelog"))
            if not is_historical:
                for old_name, new_name in DEPRECATED_PATHS:
                    if old_name in line:
                        result.add_error(
                            rel_path, i, "deprecated-path",
                            f"Deprecated path '{old_name}' found. Use '{new_name}' instead."
                        )


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def run_all_checks(root: Path, verbose: bool = False) -> ValidationResult:
    result = ValidationResult()

    check_version_consistency(root, result)
    check_directory_naming(root, result)
    check_file_naming(root, result)
    check_reference_integrity(root, result)
    check_id_uniqueness(root, result)
    check_term_consistency(root, result)
    check_adapters(root, result)
    check_chinese_path_refs(root, result)

    return result


def format_issues(issues: List[Issue], show: bool = True) -> str:
    if not show or not issues:
        return ""
    lines = []
    for issue in issues:
        loc = f"{issue.file}:{issue.line}" if issue.line > 0 else issue.file
        lines.append(f"  [{issue.level.upper()}] {loc} — {issue.check}: {issue.message}")
    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(description="FinanceOS KB Validator")
    parser.add_argument("--root", default=None, help="Repository root path (default: parent of tools/)")
    parser.add_argument("--verbose", "-v", action="store_true", help="Show warnings")
    args = parser.parse_args()

    if args.root:
        root = Path(args.root).resolve()
    else:
        # Default: parent of this script's directory
        script_dir = Path(__file__).parent.resolve()
        root = script_dir.parent

    if not root.exists():
        print(f"ERROR: Root path does not exist: {root}")
        sys.exit(1)

    print(f"FinanceOS KB Validator")
    print(f"Root: {root}")
    print(f"{'=' * 60}")

    result = run_all_checks(root, args.verbose)

    # Report
    if result.errors:
        print(f"\nERRORS ({len(result.errors)}):")
        print(format_issues(result.errors, show=True))

    if result.warnings and args.verbose:
        print(f"\nWARNINGS ({len(result.warnings)}):")
        print(format_issues(result.warnings, show=True))

    if not result.errors:
        if result.warnings and not args.verbose:
            print(f"\nPASS (with {len(result.warnings)} warnings, use --verbose to see)")
        else:
            print("\nPASS — all checks passed")
        sys.exit(0)
    else:
        print(f"\nFAIL — {len(result.errors)} error(s) found")
        if not args.verbose and result.warnings:
            print(f"  ({len(result.warnings)} warnings hidden, use --verbose)")
        sys.exit(1)


if __name__ == "__main__":
    main()
