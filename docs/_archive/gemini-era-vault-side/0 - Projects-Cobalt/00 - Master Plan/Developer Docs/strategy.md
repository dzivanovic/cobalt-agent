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

# Strategy Interface

## Overview

The `Strategy` module defines the **Abstract Base Class (ABC)** contract that all trading strategies must implement. This enforces a standardized structure for the Backtester and Live Engine, ensuring consistent interfaces across all strategy implementations.

## Role: Abstract Base Class (ABC)

The `Strategy` class inherits from Python's `abc.ABC`, making it an **Abstract Base Class**. This means:

1. **Cannot be instantiated directly** - Only concrete subclasses can be created
2. **Enforces implementation** - Subclasses MUST implement all `@abstractmethod` methods or they remain abstract
3. **Standardizes the interface** - All strategies expose the same contract for downstream consumers

```python
from abc import ABC, abstractmethod

class Strategy(ABC):
    @abstractmethod
    def analyze(self, market_data: Any) -> Dict[str, Any]:
        pass
```

## Class: `Strategy`

Abstract Base Class for all Cobalt strategies.

### Constructor

```python
def __init__(self, config: Dict[str, Any])
```

Initializes a strategy with configuration loaded from `strategies.yaml`.

**Parameters:**
| Parameter | Type | Description |
|-----------|------|-------------|
| `config` | `Dict[str, Any]` | Dictionary containing strategy configuration including `name`, `time_window`, and other parameters |

**Instance Attributes:**
| Attribute | Type | Description |
|-----------|------|-------------|
| `self.config` | `Dict[str, Any]` | Full configuration dictionary |
| `self.name` | `str` | Strategy name from config (defaults to "Unknown Strategy") |

---

## Required Contract: `analyze()` Method

All concrete strategy classes **must** implement this abstract method.

### Signature

```python
@abstractmethod
def analyze(self, market_data: Any) -> Dict[str, Any]
```

### Purpose

The core decision-making logic of a strategy. Receives market data and returns a structured trading signal.

### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `market_data` | `Any` | Clean data object containing Price, Volume, VWAP, and other indicators |

### Returns

A dictionary with the following structure:

| Key | Type | Description |
|-----|------|-------------|
| `signal` | `str` | One of: `'BUY'`, `'SELL'`, or `'WAIT'` |
| `confidence` | `float` | Signal confidence from `0.0` to `1.0` (the "T-Shirt Size") |
| `stop_loss` | `float` | Price level for stop-loss order |
| `target` | `float` | Target price level for profit-taking |
| `reason` | `str` | Human-readable explanation of the decision |

### Example Return Value

```python
{
    "signal": "BUY",
    "confidence": 0.75,
    "stop_loss": 145.50,
    "target": 160.00,
    "reason": "Positive momentum and volume surge detected"
}
```

---

## Helper Method: `check_time_window()`

A utility method for enforcing trading time restrictions.

### Signature

```python
def check_time_window(self, current_time_str: str = None) -> bool
```

### Purpose

Checks whether the current time falls within a configured trading window. This prevents strategies from executing trades outside allowed hours (e.g., pre-market, after-hours restrictions).

### Parameters

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `current_time_str` | `str` | `None` | Time string in HH:MM 24-hour format. If not provided, defaults to current system time |

### Returns

| Return Type | Description |
|-------------|-------------|
| `bool` | `True` if current time is within the configured window, `False` otherwise |

### Configuration

The time window is read from `self.config`:

```yaml
time_window:
  start: "09:30"   # Market open
  end: "16:00"     # Market close
```

### Implementation Details

- Uses simple string comparison for HH:MM format (24-hour clock)
- Default window if not configured: `"00:00"` to `"23:59"` (always allowed)
- Comparison logic: `start <= current_time_str <= end`

---

## Strategy Implementation Template

```python
from cobalt_agent.brain.strategy import Strategy

class MyStrategy(Strategy):
    def analyze(self, market_data) -> Dict[str, Any]:
        # Implement custom logic here
        return {
            "signal": "BUY",
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
- `configs/strategies.yaml` - Strategy configuration definitions