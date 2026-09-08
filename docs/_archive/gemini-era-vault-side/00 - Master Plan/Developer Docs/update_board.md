---
title: "Update Board Documentation"
status: Active
module: Utility
type: Script
dependencies:
  - "[[scribe]]"
location: "dev_utils/update_board.py"
tags: [cobalt, dev_docs]
created: 2026-02-23
---

# Update Board Script

**Location:** `dev_utils/update_board.py`

## Overview

Update Board populates the Obsidian Project Board with Phase 4 & 5 tasks. It creates markdown files with proper frontmatter for use with Dataview plugins or Kanban views.

## Usage

```bash
python dev_utils/update_board.py
```

Or with uv:

```bash
uv run python dev_utils/update_board.py
```

## ⚠️ Destructive Warning

⚠️ **This script creates new files** - it does not modify existing ones. However, if run multiple times, it may create duplicate task files. Check the `0 - Inbox` folder before running.

## Behavior

The script performs the following actions:

1. **Imports** the Scribe class from `cobalt_agent.skills.productivity.scribe`
2. **Calls** `create_task()` for each Phase 4 & 5 task
3. **Saves** each task to the `0 - Inbox` folder in your Obsidian vault

## Output Files

| ID | Title | Priority | Module | Complexity |
|--|--|--|--|--|
| 23 | Strategos Agent Setup | P0 | Tactical | M |
| 24 | Playbook Registry | P1 | Tactical | S |
| 25 | Strategy Interface | P1 | Tactical | M |
| 26 | Second Day Play Impl | P1 | Tactical | L |
| 27 | Backtest Engine | P2 | Tactical | XL |
| 28 | Ops Medical Stub | P2 | Ops | S |
| 29 | Privacy Guardrails | P0 | Ops | M |

## Task File Format

Each task file contains:
- Status: `To Do`
- Priority: `P0` (Critical) through `P2` (Normal)
- Module: `Tactical` or `Ops`
- Complexity: `S`, `M`, `L`, or `XL`
- Acceptance criteria: Code implemented and verified

## Dependencies

- `cobalt_agent.skills.productivity.scribe` - Obsidian integration
- `sys`, `os` - Path handling