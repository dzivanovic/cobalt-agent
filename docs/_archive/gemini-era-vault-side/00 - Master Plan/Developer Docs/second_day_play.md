---
title: "Second Day Play Strategy Documentation"
status: Active
module: Strategy
type: Class
dependencies:
  - "[[playbook]]"
  - "[[strategy]]"
  - "[[config]]"
location: "src/cobalt_agent/brain/strategies/second_day_play.py"
tags: [cobalt, dev_docs]
created: 2026-02-23
---

# Second Day Play Strategy

**Location:** `src/cobalt_agent/brain/strategies/second_day_play.py`

## Overview

Second Day Play is a day trading strategy that identifies high-probability setups based on the second day of a breakout pattern. It dynamically loads scoring rules and thresholds from `strategies.yaml`.

## Class: `SecondDayPlay`

Analyzes market data and returns a Scoring Profile (JSON) for potential trades.

### Constructor

```python
SecondDayPlay(config: dict = None)
```

**Parameters:**
- `config`: Configuration dictionary containing `parameters`, `scoring`, and strategy metadata.

### Attributes

- `params`: Dictionary of trading parameters (RVOL thresholds, price zones)
- `scoring`: Dictionary of scoring modifiers and points
- `name`: Strategy name
- `version`: Strategy version (1.1)

---

## Scoring Engine

The strategy calculates a dynamic score based on:

### RVOL Modifiers
- **High RVOL Threshold** (default: 3.0): Adds points for exceptional volume
- **Base RVOL Points** (default: 10): Points for meeting minimum volume requirement
- **Live RVOL Multiplier** (default: 5.0): Applied during market hours
- **Base Score** (default: 50): Starting point before modifiers

### Gap Modifiers
- **Gap Up Points** (default: 10): Applied when price gaps up at open

### abort_conditions
List of price/volume conditions that trigger immediate exit:
- Price drops below stop loss
- Volume run rate falls below 50% of expected

---

## Output Structure

```python
{
    "timestamp": "2026-02-22T16:30:00",
    "ticker": "NVDA",
    "strategy": "SecondDayPlay",
    "status": "ACTIVE_WATCH",  # or "REJECTED"
    "direction": "LONG",
    "zones": {
        "entry": 165.50,
        "stop": 162.30,
        "target": 171.10,
        "risk_per_share": 3.20
    },
    "scoring_engine": {
        "base_score": 75,
        "modifiers": {
            "live_rvol_multiplier": 5.0,
            "spy_correlation_weight": 10.0,
            "resistance_penalty": -20.0,
            "time_decay_per_min": -0.5
        }
    },
    "abort_conditions": ["price < 162.30", "volume_run_rate < 50%"]
}