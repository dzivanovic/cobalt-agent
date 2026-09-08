---
title: "Create Missing Tasks Documentation"
status: Active
module: Utility
type: Script
dependencies:
  - "[[scribe]]"
location: "dev_utils/create_missing_tasks.py"
tags: [cobalt, dev_docs]
created: 2026-02-23
---

# Create Missing Tasks Script

**Location:** `dev_utils/create_missing_tasks.py`

## Overview

Create Missing Tasks generates Phase 4 (Ion) and Phase 5 (Ops) task files in the Obsidian Project Board. It creates markdown files with proper frontmatter for use with Dataview plugins.

## Usage

```bash
python dev_utils/create_missing_tasks.py
```

Or with uv:

```bash
uv run python dev_utils/create_missing_tasks.py
```

## Behavior

The script performs the following actions:

1. **Dynamically loads** the Scribe class from `cobalt_agent/skills/productivity/scribe.py`
2. **Creates** 5 task files in the `0 - Projects/Cobalt/Tasks` folder:
   - 30 Ion Core Architecture.md
   - 31 Cobalt-Ion Bridge.md
   - 32 HUD Widgets & Overlay.md
   - 33 Mattermost C2 Integration.md
   - 34 Automated Trade Journaling.md

Each task file contains:
- Status, priority, module, phase, complexity, tags
- Objective and requirements sections

## Output Files

| Filename | Phase | Priority | Description |
|--|--|--|--|
| 30 Ion Core Architecture.md | Phase 4 | P1 | Windows HUD Python application |
| 31 Cobalt-Ion Bridge.md | Phase 4 | P0 | ZeroMQ communication between Mac and Windows |
| 32 HUD Widgets & Overlay.md | Phase 4 | P1 | Visual components for the HUD |
| 33 Mattermost C2 Integration.md | Phase 5 | P1 | Remote command and control |
| 34 Automated Trade Journaling.md | Phase 5 | P2 | Trade log entry automation |

## Destructive Warnings

⚠️ **This script creates new files** - it does not modify existing ones. Ensure the target folder (`0 - Projects/Cobalt/Tasks`) exists in your Obsidian vault.

## Dependencies

- `importlib.util` - Dynamic module loading
- `datetime` - Date generation for frontmatter