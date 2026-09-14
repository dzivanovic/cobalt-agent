---
title: "Generate Context Utility"
status: Active
module: Utility
type: Script
dependencies: []
location: "dev_utils/generate_context.py"
tags: [cobalt, context, lmm-context]
created: 2026-02-23
---

# Generate Context Utility

**Location:** `dev_utils/generate_context.py`

## Overview

A CLI-driven utility that generates targeted context files for architectural review and LLM analysis. It traverses the project directory tree, applies configurable filters, and outputs a consolidated context file containing both the directory structure and file contents.

## Purpose

This utility serves multiple use cases:
- **Architectural Review**: Creates a complete snapshot of the codebase structure and content
- **LLM Context Generation**: Produces optimized context files for large language model analysis
- **Targeted Analysis**: Supports filtering by file type (docs vs code) and custom output paths

## Usage

### Basic Commands

```bash
# Generate full context (default: cobalt_context.txt)
uv run dev_utils/generate_context.py

# Specify custom output file
uv run dev_utils/generate_context.py -o my_context.txt

# Target a specific directory
uv run dev_utils/generate_context.py -d src/cobalt_agent/brain

# Generate directory tree only (no file contents)
uv run dev_utils/generate_context.py -t

# Include only documentation files
uv run dev_utils/generate_context.py --docs

# Include only code/config files
uv run dev_utils/generate_context.py --code
```

### CLI Arguments Reference

| Argument | Short | Default | Description |
|----------|-------|---------|-------------|
| `--dir` | `-d` | `.` | Target directory to parse (e.g., `src/cobalt_agent/brain`) |
| `--tree` | `-t` | `False` | Output ONLY the directory tree (no file contents) |
| `--docs` | - | `False` | Include ONLY documentation files (`.md`, `.txt`) |
| `--code` | - | `False` | Include ONLY code/config files (`.py`, `.yaml`, `.toml`) |
| `--out` | `-o` | `cobalt_context.txt` | Output filename |

## Behavior

### Exclusion Rules

The script automatically excludes:
- Files/directories starting with `.` (hidden) or `__` (dunder)
- `venv` directory
- `uv.lock` file
- `node_modules` directory

### File Extension Handling

| Extension | Type | Special Handling |
|-----------|------|------------------|
| `.py` | Code | Full content |
| `.md`, `.txt` | Documentation | Full content |
| `.yaml`, `.yml` | Configuration | Full content |
| `.toml` | Project config | Full content |
| `.sql` | Schema/queries | Full content |
| `.log` | Logs | **Last 200 lines only** |

### Output Structure

The generated context file follows this format:

```
PROJECT DIRECTORY STRUCTURE
================================================================================
<directory-tree>

========================================
FILE: <relative-path>
========================================

<file-content>
```

## Use Cases

| Scenario | Command |
|----------|---------|
| Full project context for LLM | `uv run dev_utils/generate_context.py` |
| Quick directory structure review | `uv run dev_utils/generate_context.py -t` |
| Documentation audit | `uv run dev_utils/generate_context.py --docs -d docs` |
| Code review for specific module | `uv run dev_utils/generate_context.py --code -d src/cobalt_agent/brain` |
| Custom context for specific task | `uv run dev_utils/generate_context.py -d src/cobalt_agent/skills/research -o research_context.txt` |

## Error Handling

| Scenario | Behavior |
|----------|----------|
| Target directory does not exist | Prints error message and exits without creating output file |
| Permission denied on directory | Displays `[Permission denied]` in tree, continues with accessible paths |
| File read error | Shows `[Error reading file: <message>]` in output, continues processing |

## Related Files

- **Source**: `dev_utils/generate_context.py`
- **Default Output**: `cobalt_context.txt`

## See Also

- [Master Context File](../../90%20Project%20Management/Context/cobalt_master_context.md)