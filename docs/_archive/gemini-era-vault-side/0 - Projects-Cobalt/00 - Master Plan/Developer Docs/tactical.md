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

# Tactical Module - Strategos Agent

## Overview

The **Strategos Agent** serves as Cobalt's Tactical Department Head and Quantitative Trading Engine. This module orchestrates market data retrieval and strategy execution, acting as the central hub for tactical trading decisions.

## Core Responsibilities

1. **Market Data Retrieval** - Leverages the `FinanceTool` to fetch real-time market data
2. **Strategy Execution** - Runs comprehensive playbook scans against market data

## Class: `Strategos`

```python
class Strategos:
    """The Quantitative Trading Engine. Routes raw data requests or executes full strategy scans."""
```

### Initialization

```python
def __init__(self):
    self.finance = FinanceTool()
    self.playbook = Playbook()
```

**Dependencies Injected:**
| Component | Type | Purpose |
|-----------|------|---------|
| `finance` | FinanceTool | Market data retrieval (quotes, volume, gaps) |
| `playbook` | Playbook | Strategy scan execution and scoring |

---

## Method: `run(task: str) -> str`

Main entry point for the Tactical Department.

### Parameters
- `task`: Ticker symbol (e.g., `'NVDA'`) or special command (`"STRATEGY"`, `"PLAYBOOK"`)

### Returns
Combined intelligence report containing:
1. Raw market data from FinanceTool
2. Strategy scan results with scores and HUD configurations

### Execution Flow

```
┌─────────────────────────────────────────────────────────────┐
│  INPUT: "NVDA" or "Show STRATEGY"                          │
└─────────────────────┬───────────────────────────────────────┘
                      │
                      ▼
┌─────────────────────────────────────────────────────────────┐
│  STEP 1: Clean Input                                        │
│  - Extract ticker: task.split()[0].strip(".,!?").upper()   │
└─────────────────────┬───────────────────────────────────────┘
                      │
              ┌───────┴───────┐
              ▼               ▼
    ┌─────────────────┐  ┌──────────────────┐
    │ Special Command │  │  Regular Ticker  │
    │ (STRATEGY/PLAY- │  │                  │
    │ BOOK)           │  │                  │
    └────────┬────────┘  └────────┬─────────┘
             │                    │
             ▼                    ▼
    ┌─────────────────┐  ┌──────────────────┐
    │ list_strategies()│ │ finance.run(ticker)│
    └────────┬─────────┘  └────────┬──────────┘
             │                     │
             │              ┌──────┴─────────┐
             │              ▼                │
             │     Convert to dict           │
             │  (model_dump / __dict__)      │
             │              │                │
             │              ▼                │
             │     playbook.run_all()        │
             │              │                │
             └──────┬───────┘                │
                    │                        │
                    ▼                        │
         ┌─────────────────────┐            │
         │  RETURN: Combined   │◄───────────┘
         │  Intelligence Report│
         └─────────────────────┘
```

### Step-by-Step Breakdown

#### Step 1: Input Cleaning
Extracts ticker symbol from user input by splitting on whitespace and stripping punctuation.

```python
ticker = task.split()[0].strip(".,!?").upper()
```

#### Step 2: Special Command Handling
Detects strategy listing requests:
- `"STRATEGY"` → Returns available playbook strategies
- `"PLAYBOOK"` → Returns available playbook strategies

```python
if "STRATEGY" in ticker or "PLAYBOOK" in ticker:
    return self.playbook.list_strategies()
```

#### Step 3: Market Data Retrieval
Invokes the FinanceTool to fetch real-time market data.

```python
market_data_obj = self.finance.run(ticker)
```

#### Step 4: Data Conversion
Converts Pydantic models to dictionaries for playbook consumption.

```python
if hasattr(market_data_obj, 'dict'):
    market_data_dict = market_data_obj.dict()
elif hasattr(market_data_obj, 'model_dump'):
    market_data_dict = market_data_obj.model_dump()
else:
    market_data_dict = market_data_obj.__dict__
```

#### Step 5: Playbook Execution
Runs all active strategies against the market data.

```python
strategy_output = self.playbook.run_all(market_data_dict)
```

#### Step 6: Response Assembly
Combines raw data with strategy analysis.

```python
return f"{market_data_obj}\n\n[⚔️ Strategy Scan]\n{strategy_output}"
```

---

## Integration Points

### FinanceTool Integration

The Strategos agent delegates all market data retrieval to the `FinanceTool`:

```python
from cobalt_agent.tools.finance import FinanceTool

self.finance = FinanceTool()  # Initialized in constructor
market_data_obj = self.finance.run(ticker)  # Called during execution
```

**Data Flow:**
1. Strategos receives ticker input
2. FinanceTool queries market data sources (Finviz, etc.)
3. Pydantic model returned with price, volume, gap metrics

### Playbook Integration

The Strategos agent orchestrates strategy scans through the `Playbook`:

```python
from cobalt_agent.brain.playbook import Playbook

self.playbook = Playbook()  # Initialized in constructor
strategy_output = self.playbook.run_all(market_data_dict)  # Execute scans
```

**Scan Execution:**
1. Market data dict passed to playbook
2. Each strategy evaluates against data
3. Scores calculated and aggregated
4. HUD-compatible output formatted

---

## Example Usage

```python
# Initialize Strategos
strategos = Strategos()
# Output: ⚔️ Strategos Online | Strategies Loaded: 1

# Run analysis on ticker
result = strategos.run("NVDA")
```

### Example Output

```
FinanceData(ticker='NVDA', price=165.50, volume=50000000)

[⚔️ Strategy Scan]
**second_day_play** [ACTIVE_WATCH]
   • Score: 75/100 (High)
   • Logic: Positive relative volume and gap up pattern
   • HUD Config: 3 dynamic rules active
```

---

## Error Handling

All exceptions are caught and logged:

```python
try:
    # ... execution flow ...
except Exception as e:
    logger.error(f"Strategos failed on {ticker}: {e}")
    return f"Tactical Error: {e}"
```

---

## Related Documentation

- [[playbook]] - Strategy execution engine
- [[finance]] - Market data retrieval tool
- [[strategy]] - Strategy configuration and management