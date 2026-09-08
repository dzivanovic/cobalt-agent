---
title: "Create PRD Documentation"
status: Active
module: Utility
type: Script
dependencies:
  - "[[scribe]]"
location: "dev_utils/create_prd.py"
tags: [cobalt, dev_docs]
created: 2026-02-23
---

# Create PRD Script

**Location:** `dev_utils/create_prd.py`

## Overview

Create PRD generates the PRD-001 document based on the "Strategic Pause" conversation. It creates a comprehensive Product Requirements Document for the Cobalt-Ion Tactical HUD project.

## Usage

```bash
python dev_utils/create_prd.py
```

Or with uv:

```bash
uv run python dev_utils/create_prd.py
```

## Behavior

The script performs the following actions:

1. **Loads** the Scribe class dynamically from `cobalt_agent/skills/productivity/scribe.py`
2. **Generates** the PRD-001 content including:
   - Executive Summary
   - Core Philosophy (Distributed Brain, Python-First)
   - User Stories (Morning Briefing, Formula Injection, Tactical Engagement)
   - Functional Requirements (Scoring Engine, Math Package, Multi-Strategy)
   - Technical Constraints (Python, PyQt6, ZeroMQ, TradeStation API)
   - Future Extensibility (Discord, Journaling)
3. **Writes** the file to `0 - Projects/Cobalt/90 - Project Management/Requirements/`

## Output

Creates: `PRD-001 Cobalt-Ion Tactical HUD.md` in the Requirements folder.

## PRD Summary

### The Vision
Build a "Co-Pilot" system for manual day trading with a real-time Confidence Gauge.

### Core Philosophy
1. **Not an Auto-Trader** - System never executes trades autonomously
2. **Distributed Brain** - Mac (Cobalt) for strategy, Windows (Ion) for HUD math
3. **Python-First** - Shared logic between components

### Scoring Engine Formula
```
Score = Base + Fuel - Friction - Decay
```

## Destructive Warnings

⚠️ **This script creates new files** - it does not modify existing ones. Ensure the target folder exists in your Obsidian vault.

## Dependencies

- `importlib.util` - Dynamic module loading
- `datetime` - Date generation for frontmatter