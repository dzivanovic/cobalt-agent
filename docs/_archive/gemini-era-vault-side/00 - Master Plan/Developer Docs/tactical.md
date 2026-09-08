---
title: "Tactical Module Documentation"
status: Active
module: Brain
type: Class
dependencies:
  - "[[tactical]]"
  - "[[playbook]]"
  - "[[finance]]"
location: "src/cobalt_agent/brain/tactical.py"
tags: [cobalt, dev_docs]
created: 2026-02-23
---

# Tactical Module

## Overview

The Strategos Agent (Tactical Department Head) is responsible for:
1. Market Data Retrieval (FinanceTool)
2. Strategy Execution (Playbook)

## Class: `Strategos`

The Quantitative Trading Engine. Routes raw data requests or executes full strategy scans.

### Constructor

```python
Strategos()
```

Initializes Strategos with:
- `finance`: FinanceTool instance for market data retrieval
- `playbook`: Playbook instance for strategy execution

Logs the number of loaded strategies on initialization.

### Methods

#### `run(task: str) -> str`
Main entry point for the Tactical Department.

**Parameters:**
- `task`: The ticker symbol (e.g., 'NVDA') or a specific command.

**Returns:**
A combined intelligence report containing market data and strategy scan results.

**Workflow:**
1. Cleans input (extracts ticker symbol)
2. Retrieves raw market data via FinanceTool
3. Converts data to dictionary format
4. Runs all active strategies via Playbook
5. Returns combined intelligence

**Special Commands:**
- `"STRATEGY"` or `"PLAYBOOK"`: Returns list of active strategies instead of analysis

### Example Output

```
FinanceData(ticker='NVDA', price=165.50, volume=50000000)
[⚔️ Strategy Scan]
**second_day_play** [ACTIVE_WATCH]
   • Score: 75/100 (High)
   • Logic: Positive relative volume and gap up pattern
   • HUD Config: 3 dynamic rules active