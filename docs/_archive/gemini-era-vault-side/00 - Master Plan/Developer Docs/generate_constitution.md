---
title: "Generate Constitution Documentation"
status: Active
module: Utility
type: Script
dependencies:
  - "[[scribe]]"
location: "dev_utils/generate_constitution.py"
tags: [cobalt, dev_docs]
created: 2026-02-23
---

# Generate Constitution Script

**Location:** `dev_utils/generate_constitution.py`

## Overview

Generate Constitution creates the Cobalt Constitution - a comprehensive set of architecture documentation, ADRs, and project management files. This script generates the foundational documentation structure for the entire Cobalt project.

## Usage

```bash
python dev_utils/generate_constitution.py
```

Or with uv:

```bash
uv run python dev_utils/generate_constitution.py
```

## ⚠️ Destructive Warning

🚨 **THIS SCRIPT DELETES AND CREATES FILES** - It creates the entire Constitution document structure. Run only once during initial setup or when explicitly updating the Constitution.

## Behavior

The script generates the following files in the Obsidian vault:

### Level 1: Master Plan
1. **Dashboard** (`00 Cobalt Master Plan.md`) - Root navigation document
2. **System Manifest** (`00 - Master Plan/System Manifest.md`) - Stack, hierarchy, and roles
3. **Security Architecture** (`00 - Master Plan/Security Architecture.md`) - Zero Trust, JIT, Kill-Switches

### Level 2: ADRs
4. **ADR-001** - Distributed Protocol (Mac/Windows architecture)
5. **ADR-002** - Hybrid AI Compute (Local vs Cloud models)
6. **ADR-003** - Python-First Architecture (PyQt6 for Ion HUD)

### Level 3: Project Management
7. **Roadmap** - Strategic phases (Q1/Q2 goals)
8. **Backlog** - Future ideas and placeholders

## Output Files Structure

```
0 - Projects/Cobalt/
├── 00 Cobalt Master Plan.md           (Dashboard)
├── 00 - Master Plan/
│   ├── System Manifest.md
│   └── Security Architecture.md
├── 00 - Master Plan/ADR/
│   ├── ADR-001 Cobalt-Ion Distributed Protocol.md
│   ├── ADR-002 Hybrid AI Compute.md
│   └── ADR-003 Python-First Architecture.md
└── 90 - Project Management/
    ├── Roadmap.md
    └── Backlog.md
```

## System Manifest Overview

### The Hierarchy
- **Level 1: CEO (Dejan)** - Final decision maker
- **Level 2: Cobalt (Chief of Staff)** - Orchestration and coaching
- **Level 3: Departments** - Strategos, Ion, Scribe, Sentinel, Scout

### The Hardware Stack
- **Brain (Mac Studio M2 Ultra)** - Central compute node
- **Engine (Windows Workstation)** - Execution environment
- **Console (Lenovo X1 Carbon)** - Development interface
- **Red Phone (Mobile)** - Command & Control

## Dependencies

- `importlib.util` - Dynamic module loading
- `datetime` - Date generation for frontmatter