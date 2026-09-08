---
title: "Finance Tool Documentation"
status: Active
module: Tool
type: Class
dependencies:
  - "[[tool_manager]]"
  - "[[config]]"
location: "src/cobalt_agent/tools/finance.py"
tags: [cobalt, dev_docs]
created: 2026-02-23
---

# Finance Tool Module

**Location:** `src/cobalt_agent/tools/finance.py`

## Overview

Finance Tool returns structured market data with Technical Indicators. Implements all rules from `rules.yaml`.

## Class: `MarketMetrics` (Pydantic Model)

Structured financial data for a single asset.

### Fields

| Field | Type | Description |
|--|--|--|
| `ticker` | `str` | The stock symbol (e.g. AAPL) |
| `price` | `float` | Current market price |
| `change_percent` | `float` | Daily percentage change |
| `volume` | `int` | Current trading volume |
| `rsi` | `float` | Relative Strength Index |
| `atr` | `float` | Average True Range |
| `rvol` | `float` | Relative Volume |
| `avwap_earnings` | `str` | VWAP from last earnings date |
| `avwap_high` | `str` | VWAP from 2-month Swing High |
| `avwap_low` | `str` | VWAP from 2-month Swing Low |
| `sma_10` | `str` | 10-day SMA with slope |
| `sma_20` | `str` | 20-day SMA with slope |
| `sma_50` | `str` | 50-day SMA with slope |
| `sma_100` | `str` | 100-day SMA with slope |
| `sma_200` | `str` | 200-day SMA with slope |
| `signal` | `str` | Computed technical signal |
| `alert_flags` | `str` | Special alerts |
| `calculation_meta` | `str` | Debug string showing which rules were used |

### Methods

#### `__str__() -> str`
Returns a human-readable string representation with formatted output.

---

## Class: `FinanceTool`

Fetches market data and calculates technical indicators.

### Attributes

| Attribute | Value |
|--|--|
| `name` | `"finance"` |
| `description` | `"Get current stock market data and technical indicators. Use for price queries, e.g., 'What is the price of AAPL?'"` |
| `system_config` | Loaded config object |
| `rules` | Trading rules from config |

### Methods

#### `run(ticker: str) -> MarketMetrics`

Fetches market data and returns structured metrics.

**Parameters:**
- `ticker`: Stock symbol (e.g., AAPL)

**Returns:** `MarketMetrics` with all calculated indicators

**Workflow:**
1. Load 2-year historical data via yfinance
2. Calculate RSI, ATR, RVOL
3. Compute Anchored VWAPs (earnings, swing high, swing low)
4. Calculate SMAs with slope detection
5. Apply signal logic from rules.yaml
6. Return structured metrics

#### `_get_rule(path: str, default: Any = None) -> Any`

Safely access nested config rules (handles dict or object notation).

#### `_calculate_rsi(data, window: int) -> float`

Calculates Relative Strength Index.

#### `_calculate_atr(data, window: int) -> float`

Calculates Average True Range.

#### `_calculate_rvol(data, window: int) -> float`

Calculates Relative Volume against 20-day average.

#### `_calculate_avwap(data, start_date: str) -> float`

Calculates Anchored VWAP from a specific date.

#### `_get_sma_data(data, window: int) -> Tuple[float, str]`

Returns SMA value and slope direction ("RISING" or "FALLING").

#### `_get_last_earnings_date(ticker_obj) -> Optional[str]`

Gets the most recent past earnings date.

### Signal Logic

1. **Overbought/ Oversold**: RSI > 70 or RSI < 30
2. **Bullish Cross**: Fast SMA > Slow SMA AND both rising
3. **Trend**: Price above/below earnings VWAP
4. **Default**: NEUTRAL

### Alerts

- **RVOL ALERT**: Relative volume > 3.0
- **PARABOLIC MOVE**: 5-day move > 5x ATR