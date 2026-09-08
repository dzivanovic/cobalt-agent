---
status: To Do
priority: P2 (Normal)
module: Skills
phase: 5 (Ops)
complexity: S
tags: [cobalt, task, journaling]
created: 2026-02-11
---

# 34 Automated Trade Journaling

## Objective
Remove manual data entry by having Cobalt write its own trade logs.

## Requirements
* [ ] Capture execution details (Entry, Exit, Size, P&L).
* [ ] Capture "Why?" (The Strategy Logic snapshot at moment of trade).
* [ ] Format as a Markdown table.
* [ ] Append to the **Daily Note** in Obsidian via Scribe.

## Format
| Time | Ticker | Side | P&L | Strategy | Confidence |
|------|--------|------|-----|----------|------------|
