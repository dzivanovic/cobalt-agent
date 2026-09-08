---
title: "Strategy Interface Documentation"
status: Active
module: Strategy
type: Class
dependencies:
  - "[[playbook]]"
  - "[[second_day_play]]"
location: "src/cobalt_agent/brain/strategy.py"
tags: [cobalt, dev_docs]
created: 2026-02-23
---

# Strategy Module

## Overview

The Strategy Interface defines the contract that all trading strategies must implement. This enforces a standard structure for the Backtester and Live Engine.

## Class: `Strategy` (ABC)

Abstract Base Class for all Cobalt Strategies.

### Constructor

```python
Strategy(config: Dict[str, Any])
```

Initializes a strategy with specific parameters from `strategies.yaml`.

**Parameters:**
- `config`: Dictionary containing strategy parameters including `name`, `time_window`, and other configuration data.

### Methods

#### `analyze(market_data: Any) -> Dict[str, Any]`
**Abstract Method** - Core logic that must be implemented by all strategies.

**Parameters:**
- `market_data`: A clean object containing Price, Volume, VWAP, etc.

**Returns:**
Dictionary containing:
- `signal`: 'BUY', 'SELL', or 'WAIT'
- `confidence`: 0.0 to 1.0 (The 'T-Shirt Size')
- `stop_loss`: Price level
- `target`: Price level
- `reason`: Text explanation

#### `check_time_window(current_time_str: str = None) -> bool`
Helper method that checks if trading is allowed within the configured time window.

**Parameters:**
- `current_time_str`: Optional time string in HH:MM format (defaults to current time).

**Returns:**
`True` if within the configured time window, `False` otherwise.

---

## Strategy Structure

All strategies must implement the `analyze()` method and return a consistent structure:

```python
{
    "signal": "BUY|SELL|WAIT",
    "confidence": 0.75,
    "stop_loss": 145.50,
    "target": 160.00,
    "reason": "Positive momentum and volume surge detected"
}
```

---

## Related Files

- `playbook.py` - Orchestrates strategy execution
- `tactical.py` - Strategos agent that uses strategies
- `strategies/second_day_play.py` - Example strategy implementation