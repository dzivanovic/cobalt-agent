---
title: "Finance Tool Documentation"
status: Active
module: Tool
type: Class
dependencies:
  - "[[tool_manager]]"
  - "[[config]]"
location: "src/cobalt_agent/tools/finance.py"
tags: [cobalt, finance, technical-indicators, market-data]
created: 2026-02-23
updated: 2026-04-08
---

# Finance Tool Module

**Location:** `src/cobalt_agent/tools/finance.py`

## Overview

The Finance Tool provides structured market data with technical indicators for trading analysis. It fetches historical price data via `yfinance` and computes a comprehensive set of technical indicators including momentum oscillators, volatility measures, anchored VWAPs, and moving averages. All configuration parameters are sourced from `config.yaml` trading rules, ensuring consistent signal logic across the Cobalt system.

## Dependencies

| Package | Purpose |
|---------|---------|
| `yfinance` | Fetches historical market data from Yahoo Finance |
| `pandas` | Data manipulation and time-series analysis |
| `numpy` | Numerical computations for indicator calculations |
| `pydantic` | Structured data validation via Pydantic models |
| `loguru` | Logging for debugging and error tracking |

---

## Class: `MarketMetrics` (Pydantic Model)

Structured financial data container for a single asset. All fields are typed and validated via Pydantic.

### Fields

| Field | Type | Description |
|-------|------|-------------|
| `ticker` | `str` | The stock symbol (e.g. AAPL) |
| `price` | `float` | Current market price |
| `change_percent` | `float` | Daily percentage change |
| `volume` | `int` | Current trading volume |
| `rsi` | `float` | Relative Strength Index (momentum oscillator) |
| `atr` | `float` | Average True Range (volatility measure) |
| `rvol` | `float` | Relative Volume vs. 20-day average |
| `avwap_earnings` | `str` | VWAP from last earnings date with price position |
| `avwap_high` | `str` | VWAP from 2-month swing high with price position |
| `avwap_low` | `str` | VWAP from 2-month swing low with price position |
| `sma_10` | `str` | 10-day Simple Moving Average with slope |
| `sma_20` | `str` | 20-day Simple Moving Average with slope |
| `sma_50` | `str` | 50-day Simple Moving Average with slope |
| `sma_100` | `str` | 100-day Simple Moving Average with slope |
| `sma_200` | `str` | 200-day Simple Moving Average with slope |
| `signal` | `str` | Computed technical signal (e.g., BULLISH, OVERBOUGHT) |
| `alert_flags` | `str` | Special alerts (e.g., RVOL ALERT, PARABOLIC MOVE) |
| `calculation_meta` | `str` | Debug string showing which rules were used |

### Methods

#### `__str__() -> str`
Returns a human-readable string representation with formatted output including price, signal, momentum metrics, anchored VWAPs, and SMAs.

---

## Class: `FinanceTool`

Main orchestrator for fetching market data and calculating technical indicators. Implements configuration-driven logic from `config.yaml`.

### Attributes

| Attribute | Value | Description |
|-----------|-------|-------------|
| `name` | `"finance"` | Tool identifier for the orchestrator |
| `description` | `"Get current stock market data..."` | LLM-facing description for tool routing |
| `system_config` | Config object | Loaded system configuration |
| `rules` | Trading rules | Reference to trading rule definitions |

### Configuration Access

The tool uses a safe nested-access helper `_get_rule()` that handles both dictionary and object notation for configuration values:

| Config Path | Default | Purpose |
|-------------|---------|---------|
| `rsi.period` | 14 | RSI calculation window |
| `rsi.overbought` | 70 | Overbought threshold |
| `rsi.oversold` | 30 | Oversold threshold |
| `atr.period` | 14 | ATR calculation window |
| `atr.expansion_multiplier` | 5.0 | Parabolic move threshold multiplier |
| `moving_averages.bullish_cross.fast` | 10 | Fast MA for cross detection |
| `moving_averages.bullish_cross.slow` | 20 | Slow MA for cross detection |
| `momentum.rvol_alert_threshold` | 3.0 | RVOL alert threshold |

---

## Indicator Calculations

### `_calculate_rsi(data: pd.DataFrame, window: int) -> float`
Computes Relative Strength Index using standard RSI formula:
1. Calculate price delta (change between consecutive closes)
2. Separate gains and losses
3. Compute rolling averages for both
4. Calculate RS = avg(gain) / avg(loss)
5. Return RSI = 100 - (100 / (1 + RS))

### `_calculate_atr(data: pd.DataFrame, window: int) -> float`
Computes Average True Range for volatility measurement:
1. Calculate High-Low range
2. Calculate |High - Previous Close| and |Low - Previous Close|
3. Take maximum of the three as True Range
4. Return rolling average over window

### `_calculate_rvol(data: pd.DataFrame, window: int = 20) -> float`
Computes Relative Volume:
1. Calculate 20-day average volume
2. Divide current volume by average
3. Returns ratio indicating unusual volume activity

### `_calculate_avwap(data: pd.DataFrame, start_date: str) -> float`
Computes Anchored VWAP from a specific date:
1. Filter data from start_date onward
2. Calculate Typical Price = (High + Low + Close) / 3
3. Compute cumulative (TP × Volume) / cumulative Volume

### `_get_sma_data(data: pd.DataFrame, window: int) -> Tuple[float, str]`
Returns SMA value and trend direction:
1. Calculate rolling mean of closing prices
2. Compare current vs previous SMA value
3. Return (value, "RISING" or "FALLING")

### `_get_last_earnings_date(ticker_obj) -> Optional[str]`
Retrieves most recent past earnings date from yfinance ticker object.

---

## Signal Logic (run method)

The `run(ticker: str)` method orchestrates the full calculation pipeline:

### Workflow Steps

1. **Fetch Data**: Load 2-year historical data via `yfinance.Ticker`
2. **Handle Empty Data**: Return error metrics if no data available
3. **Calculate Price Metrics**: Current price, daily change percentage
4. **Compute Indicators**: RSI, ATR, RVOL using configured parameters
5. **Calculate Anchored VWAPs**:
   - Earnings VWAP (from last earnings date)
   - Swing High VWAP (from 2-month high)
   - Swing Low VWAP (from 2-month low)
6. **Calculate SMAs**: 10, 20, 50, 100, 200-day with slope detection
7. **Apply Signal Logic**:
   - RSI overbought (> 70) or oversold (< 30)
   - Bullish cross (fast SMA > slow SMA, both rising)
   - Earnings VWAP trend (price above/below)
8. **Generate Alerts**: RVOL threshold, parabolic moves
9. **Return MarketMetrics**: Structured output with all values

### Signal Priority Order

1. `OVERBOUGHT (> 70)` - RSI above threshold
2. `OVERSOLD (< 30)` - RSI below threshold
3. `BULLISH CROSS (fast/slow Rising)` - Fast SMA crosses above slow SMA
4. `BULLISH (Above Earnings VWAP)` - Price above earnings AVWAP
5. `BEARISH (Below Earnings VWAP)` - Price below earnings AVWAP
6. `NEUTRAL` - Default state

### Alert Conditions

| Alert | Trigger Condition |
|-------|-------------------|
| RVOL ALERT | Relative volume > 3.0 |
| PARABOLIC MOVE | 5-day price move > 5 × ATR |

---

## Error Handling

- **Empty Data**: Returns zeroed metrics with `signal="NO DATA"`
- **Calculation Errors**: Returns error state with `signal="ERROR"`
- **Missing Config**: Falls back to default values via `_get_rule()`

---

## Usage Example

```python
from cobalt_agent.tools.finance import FinanceTool

tool = FinanceTool()
result = tool.run("AAPL")
print(result)  # Formatted output with all metrics
```

---

## Role in Cobalt Trading Operations

The Finance Tool serves as the primary data source for:
- **Tactical Analysis**: Provides real-time price and indicator data for trade decisions
- **Strategy Evaluation**: Supplies technical metrics for strategy backtesting
- **Risk Assessment**: ATR and volatility measures inform position sizing
- **Entry/Exit Signals**: RSI, moving average crosses, and VWAP levels guide timing
- **Market Context**: Volume analysis (RVOL) identifies unusual activity

All calculations respect configuration from `config.yaml`, enabling parameter tuning without code changes.