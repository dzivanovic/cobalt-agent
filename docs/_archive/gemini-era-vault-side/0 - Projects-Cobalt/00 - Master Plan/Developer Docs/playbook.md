# Playbook Module

**File:** `src/cobalt_agent/brain/playbook.py`  
**Purpose:** Loads and hydrates trading strategies from `strategies.yaml`, then executes them against market data.

---

## Overview

The `Playbook` class is a configuration-driven strategy orchestrator that:
1. Loads strategy definitions from `configs/strategies.yaml`
2. Hydrates each active strategy into a `Strategy` class instance
3. Executes all strategies via the `run_all()` loop against provided market data

---

## Configuration Loading

### Strategy Definition (strategies.yaml)

Each strategy is defined under the `strategies` key with the following structure:

```yaml
strategies:
  <strategy_key>:
    name: "Display Name"
    active: true|false          # Only active strategies are hydrated
    direction: "LONG"|"SHORT"|"BOTH"
    description: "Strategy summary"
    
    # Optional: Time window for execution
    time_window:
      start: "HH:MM"
      end: "HH:MM"
    
    # Strategy-specific filters (e.g., min_atr, volume thresholds)
    filters:
      <filter_name>: value
    
    # Execution parameters (entry triggers, stop rules, targets)
    execution:
      entry_trigger: "trigger_type"
      stop_rule: "rule_name"
      target_rule: "rule_name"
    
    # Optional scoring system for ranking setups
    scoring:
      base_score: 50
      <modifier>: points
```

### YAML Loader

The `Playbook` uses PyYAML to load the configuration:

```python
def _load_config() -> Dict[str, Any]:
    """Load strategies from configs/strategies.yaml"""
    config_path = Path(__file__).parent.parent.parent / "configs" / "strategies.yaml"
    with open(config_path, 'r') as f:
        return yaml.safe_load(f)
```

---

## Strategy Hydration

### The `hydrate_strategies()` Method

This method transforms raw YAML configs into live `Strategy` instances:

```python
def hydrate_strategies(self) -> List[Strategy]:
    """
    Instantiate Strategy classes for all active strategies.
    
    Returns:
        List of Strategy objects ready for analysis
    """
```

**Process:**
1. Load the full YAML config
2. Iterate through each strategy definition
3. Check if `active: true`
4. Instantiate the corresponding `Strategy` subclass with its config dict

**Note:** The current implementation uses a placeholder pattern (`pass`) where specific strategy class instantiation logic would be added. Each strategy key in YAML should map to a concrete `Strategy` subclass (e.g., `SecondDayPlay`, `FashionablyLateScalp`).

---

## Execution Loop

### The `run_all()` Method

The main entry point for strategy execution:

```python
def run_all(self, market_data: Any) -> Dict[str, Any]:
    """
    Execute all active strategies against market data.
    
    Args:
        market_data: Market data object (prices, volume, indicators)
        
    Returns:
        Dict containing all strategy signals and scores
    """
```

**Process:**
1. Call `hydrate_strategies()` to get active strategy instances
2. Iterate through each hydrated strategy
3. Call `strategy.analyze(market_data)` for each one
4. Collect results into a unified response dictionary

**Return Structure:**
```python
{
    "signals": [
        {
            "strategy_name": "...",
            "signal": "BUY" | "SELL" | "WAIT",
            "confidence": 0.0-1.0,
            "stop_loss": price,
            "target": price,
            "reason": "explanation"
        },
        ...
    ],
    "summary": {
        "total_strategies": <count>,
        "active_signals": <count>
    }
}
```

---

## Architecture Diagram

```
configs/strategies.yaml
        │
        ▼
  Playbook._load_config()
        │
        ▼
 hydrate_strategies() ──► [Strategy1, Strategy2, ...]
        │                        │
        ▼                        ▼
   run_all()             strategy.analyze(market_data)
        │                        │
        └──────────► Collect Results ◄────────────┘
                           │
                           ▼
                    Dict[str, Any] (signals)
```

---

## Key Design Principles

1. **Configuration-Driven:** All strategy parameters live in YAML, not code
2. **Active Flag Filtering:** Only `active: true` strategies execute
3. **Abstract Base Enforcement:** All strategies inherit from `Strategy(ABC)` with mandatory `analyze()` method
4. **Unified Output:** All signals return the same dict structure for easy consumption

---

## Adding a New Strategy

1. Define the strategy in `configs/strategies.yaml`
2. Create a new class in `src/cobalt_agent/brain/strategies/` inheriting from `Strategy`
3. Implement the `analyze(market_data)` method
4. Set `active: true` in YAML to enable execution

---

## See Also

- `src/cobalt_agent/brain/strategy.py` - Strategy abstract base class
- `configs/strategies.yaml` - Strategy configuration file
- `src/cobalt_agent/brain/strategies/` - Concrete strategy implementations