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
**Version:** 1.1  
**Author:** Cobalt AI

## Overview

Second Day Play is a day trading strategy that identifies high-probability setups based on the second day of a breakout pattern. The strategy looks for stocks that showed strong momentum on Day 1, then evaluates whether the second day presents a favorable entry opportunity. It dynamically loads scoring rules and thresholds from `strategies.yaml`.

## Class: `SecondDayPlay`

Analyzes market data and returns a Scoring Profile (JSON) for potential trades.

### Constructor

```python
SecondDayPlay(config: dict = None)
```

**Parameters:**
- `config`: Configuration dictionary containing `parameters`, `scoring`, and strategy metadata from `strategies.yaml`

**Attributes:**
| Attribute | Type | Description |
|-----------|------|-------------|
| `params` | dict | Trading parameters (RVOL thresholds, price zones) |
| `scoring` | dict | Scoring modifiers and point values |
| `name` | str | Strategy identifier |
| `version` | str | Strategy version string |

---

## Method: `analyze()`

```python
def analyze(self, ticker: str, market_data: dict) -> dict
```

**Purpose:** Evaluates a ticker against the Second Day Play strategy criteria and returns either a rejection or an ACTIVE_WATCH setup with calculated price zones.

**Parameters:**
| Parameter | Type | Description |
|-----------|------|-------------|
| `ticker` | str | Stock ticker symbol (e.g., "NVDA") |
| `market_data` | dict | Raw market data containing price/volume information |

**Required Market Data Fields:**
| Field | Type | Description |
|-------|------|-------------|
| `yesterday_close` | float | Previous day's closing price |
| `yesterday_volume` | int | Previous day's volume |
| `average_volume` | int | Typical/average volume for the stock |
| `today_open` | float | Current day's opening price |
| `pre_market_high` | float | Highest price reached in pre-market session |

---

## Evaluation Logic Flow

### Step 1: Data Unpacking

Extracts key price and volume metrics from the input data:
- `y_close`: Yesterday's closing price
- `y_vol`: Yesterday's volume
- `avg_vol`: Average volume baseline
- `today_open`: Today's opening price
- `pm_high`: Pre-market high

### Step 2: Validation (The Gatekeeper)

**Relative Volume Check (RVOL):**
```python
y_rvol = y_vol / avg_vol  # Yesterday's relative volume
```

**Rejection Condition - Low RVOL:**
- If `y_rvol < min_rvol` (default: 1.5), the setup is rejected
- Rationale: Insufficient volume indicates lack of institutional interest

**Rejection Condition - Gap Down:**
- If `today_open < (y_close * 0.98)`, the setup is rejected
- Rationale: A gap down (>2% below yesterday's close) signals momentum loss

### Step 3: Price Zone Calculation

If validation passes, the strategy calculates key price levels:

| Zone | Formula | Purpose |
|------|---------|---------|
| `entry` | `pm_high + 0.05` | Entry point: $0.05 above pre-market high |
| `stop_loss` | `y_close - 0.20` | Stop: $0.20 below yesterday's close |
| `risk` | `entry_price - stop_loss` | Risk per share |
| `target` | `entry + (risk * 2)` | Target: 2:1 reward-to-risk ratio |

### Step 4: Scoring Engine

The strategy calculates a dynamic score starting from `base_score` (default: 50) and applies modifiers:

**RVOL Modifiers:**
| Condition | Points Added | Default Value |
|-----------|--------------|---------------|
| `y_rvol >= high_rvol_threshold` | `high_rvol_points` | 15 (threshold: 3.0) |
| `min_rvol <= y_rvol < high_rvol_threshold` | `base_rvol_points` | 10 |

**Gap Modifiers:**
| Condition | Points Added | Default Value |
|-----------|--------------|---------------|
| `today_open > y_close` (Gap Up) | `gap_up_points` | 10 |

### Step 5: Output Construction

Returns a comprehensive JSON structure with all calculated values.

---

## Rejection Conditions

The strategy returns `status: "REJECTED"` when:

| Condition | Reason Message |
|-----------|----------------|
| `y_rvol < min_rvol` | `"Low Relative Volume Yesterday (RVOL: {value} < {threshold})"` |
| `today_open < y_close * 0.98` | `"Gap Down - Momentum Lost"` |

---

## Output Structure

### Successful Match (ACTIVE_WATCH)

```json
{
    "timestamp": "2026-02-22T16:30:00",
    "ticker": "NVDA",
    "strategy": "SecondDayPlay",
    "status": "ACTIVE_WATCH",
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
    "abort_conditions": [
        "price < 162.30",
        "volume_run_rate < 50%"
    ]
}
```

### Rejected Setup

```json
{
    "ticker": "NVDA",
    "strategy": "SecondDayPlay",
    "status": "REJECTED",
    "reason": "Low Relative Volume Yesterday (RVOL: 1.2 < 1.5)"
}
```

---

## Configuration Parameters (strategies.yaml)

### Parameters Section
| Parameter | Default | Description |
|-----------|---------|-------------|
| `min_rvol` | 1.5 | Minimum relative volume threshold |

### Scoring Section
| Parameter | Default | Description |
|-----------|---------|-------------|
| `base_score` | 50 | Starting score before modifiers |
| `high_rvol_threshold` | 3.0 | RVOL level for exceptional volume bonus |
| `high_rvol_points` | 15 | Points added for high RVOL |
| `base_rvol_points` | 10 | Points for meeting minimum RVOL |
| `gap_up_points` | 10 | Points for gap-up opening |
| `live_rvol_multiplier` | 5.0 | Multiplier during active market hours |
| `spy_correlation_weight` | 10.0 | Weight for SPY correlation factor |
| `resistance_penalty` | -20.0 | Penalty for hitting resistance levels |
| `time_decay_per_min` | -0.5 | Score decay per minute elapsed |

---

## Abort Conditions

Active positions are monitored against these exit triggers:
1. **Price Stop:** `price < stop_loss` - Hard stop below calculated level
2. **Volume Decay:** `volume_run_rate < 50%` - Insufficient volume progression

---

## Strategy Rationale

The Second Day Play strategy capitalizes on continuation patterns where:
1. **Day 1** shows strong bullish momentum with above-average volume
2. **Day 2 Open** maintains or improves on Day 1's close (no gap down)
3. **Entry Trigger** occurs when price breaks above pre-market high

The 2:1 reward-to-risk ratio ensures favorable risk management, while the scoring system prioritizes setups with exceptional volume and positive momentum.