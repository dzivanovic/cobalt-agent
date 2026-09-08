---
title: "Playbook Module Documentation"
status: Active
module: Brain
type: Orchestrator
dependencies:
  - "[[strategy]]"
  - "[[tactical]]"
  - "[[config]]"
  - "[[second_day_play]]"
location: "src/cobalt_agent/brain/playbook.py"
tags: [cobalt, dev_docs]
created: 2026-02-23
---

# Playbook Module

## Overview

The Playbook Registry loads trading strategies and parameters from `configs/strategies.yaml` and executes strategy logic against market data.

## Class: `Playbook`

Manages active trading strategies and their parameters.

### Constructor

```python
Playbook(config_path: str = "configs/strategies.yaml")
```

Initializes the playbook with strategy configurations from a YAML file.

### Methods

#### `_load_config(path_str: str) -> Dict[str, Any]`
Loads the YAML configuration file and returns strategy parameters.

#### `_initialize_strategies()`
Hydrates strategy classes with their configurations by mapping YAML keys to Python classes.

#### `get_strategy(name: str)`
Returns the strategy instance by name.

#### `list_strategies() -> str`
Returns a formatted string list of ACTIVE (loaded) strategies with their configurations.

#### `run_all(market_data: Dict[str, Any]) -> str`
Runs ALL strategies against incoming market data and returns a summary string of scoring profiles.

### Example Output

```
📜 **Active Playbook:**
- **SecondDayPlay**: LONG (09:30-11:00)
   • Score: 75/100 (High)
   • Logic: Positive relative volume and gap up pattern
   • HUD Config: 3 dynamic rules active
```

---

## Related Files

- `strategy.py` - Abstract base class for all strategies
- `tactical.py` - Strategos agent that orchestrates playbook execution
- `strategies/` - Individual strategy implementations