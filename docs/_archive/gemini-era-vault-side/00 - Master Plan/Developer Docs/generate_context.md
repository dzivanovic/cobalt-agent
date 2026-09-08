---
title: "Generate Context Documentation"
status: Active
module: Utility
type: Script
dependencies: []
location: "dev_utils/generate_context.py"
tags: [cobalt, dev_docs]
created: 2026-02-23
---

# Generate Context Script

**Location:** `dev_utils/generate_context.py`

## Overview

Generate Context is a utility script that generates a master context file (`cobalt_master_context.txt`) for architectural review. It walks the project directory, collects relevant files, and outputs a single file containing the directory tree and file contents.

## Usage

Run the script from the project root:

```bash
python dev_utils/generate_context.py
```

Or with uv:

```bash
uv run python dev_utils/generate_context.py
```

## Behavior

### Exclusions

The script automatically excludes:
- Files/directories starting with `.` or `__`
- `venv` directory
- `uv.lock` file

### Inclusions

The script processes files with the following extensions:
- `.py` (Python)
- `.md` (Markdown)
- `.yaml` / `.yml` (YAML)
- `.toml` (TOML)
- `.log` (Log files - last 200 lines only)
- `.txt` (Text files)

### Output

The script generates `cobalt_master_context.txt` containing:
1. **Directory Tree**: Text-based representation of the project structure
2. **File Contents**: All processed files with their full content

## Use Cases

- **Architectural Review**: Provides a complete snapshot of the codebase for review
- **Context Generation**: Creates a consolidated file for LLM analysis
- **Documentation**: Serves as a baseline for project documentation

## Notes

- Log files are automatically truncated to the last 200 lines to manage file size
- Files that cannot be read (permissions, binary) will show an error message