---
title: "Dynamic Scanner YAML Test Runner"
status: Active
module: Utility
type: Integration Test
dependencies: [finviz_api]
location: "dev_utils/live_run_dynamic_scanners.py"
tags: [finviz, scanner, testing, yaml]
created: 2026-04-07
---

# Dynamic Scanner YAML Test Runner

**Location:** `dev_utils/live_run_dynamic_scanners.py`

## Overview

A test utility that validates the Universal Abstract Screener by loading Finviz scanner configurations from `configs/scanners.yaml` and executing them via the `FinvizApiClient`. This script demonstrates dynamic filter compilation and screener execution without hardcoding any screeners.

## Purpose

This script provides:
- **Configuration-Driven Testing**: Loads scanner definitions from YAML instead of hardcoding
- **Dynamic Filter Compilation**: Tests the `compile_filters()` method for converting YAML filters to Finviz URL parameters
- **Screener Execution**: Validates `execute_dynamic_screener()` against live Finviz API
- **Metrics Validation**: Verifies expected output (151 columns) from all active scanners

## Prerequisites

1. **Configuration File**: `configs/scanners.yaml` with active scanner definitions
2. **Finviz API Client**: `src/cobalt_agent/skills/research/finviz_api.py`
3. **Dependencies**: `pyyaml` package installed (via `uv add pyyaml`)

## Configuration Format

The script expects `configs/scanners.yaml` in this format:

```yaml
scanners:
  scanner_name:
    active: true
    description: "Human-readable description"
    filters:
      filter_key: "filter_value"
      # Example:
      # exchange: "usa"
      # marketCap: "mid+"
      # volume: "over200k"
```

### Active Scanner Detection

Only scanners with `active: true` are executed. Inactive scanners (`active: false`) are skipped silently.

## Usage

### Basic Execution

```bash
# Run all active scanners from YAML configuration
uv run dev_utils/live_run_dynamic_scanners.py
```

## Execution Flow

The script performs these steps:

### Step 1: Load Configuration
```python
config_path = Path("configs/scanners.yaml")
with open(config_path, "r") as f:
    config = yaml.safe_load(f)

scanners = config.get("scanners", {})
```

### Step 2: Identify Active Scanners
```python
active_scanners = {
    name: data for name, data in scanners.items()
    if data.get("active", False)
}
```

### Step 3: Execute Each Scanner

For each active scanner:

1. **Display Metadata**:
   - Scanner name
   - Description (or "No description")

2. **Compile Filters**:
   ```python
   compiled_filters = client.compile_filters(filters)
   print(f"Compiled Filters: {compiled_filters}")
   ```

3. **Execute Screener**:
   ```python
   results = await client.execute_dynamic_screener(filters)
   ```

4. **Report Metrics**:
   - Total tickers found
   - Total columns extracted (expected: 151)

## Output Reference

### Success Output
```
============================================================
🔬 Universal Abstract Screener - YAML Test Runner
============================================================

📊 Scanner: momentum_screener
----------------------------------------
   Description: High momentum stocks with strong volume
   Compiled Filters: exchange=usa&marketCap=mid+&volume=over200k
   Total Tickers Found: 47
   Total Columns Extracted: 151
   ✅ All 151 columns successfully extracted

📊 Scanner: value_screener
----------------------------------------
   Description: Undervalued stocks with low P/E
   Compiled Filters: exchange=usa&pe=low+&priceToBook=under1
   Total Tickers Found: 23
   Total Columns Extracted: 151
   ✅ All 151 columns successfully extracted

============================================================
✅ Test run complete
============================================================
```

### Warning Scenarios

| Scenario | Output |
|----------|--------|
| No active scanners | `⚠️  No active scanners found in configuration` |
| Undefined filters | `⚠️  No filters defined` (skips to next scanner) |
| Column mismatch | `⚠️  Expected 151 columns, got {actual}` |
| Execution error | `❌ Error executing screener: {error_message}` |

## Key Components

### FinvizApiClient Integration

The script uses these client methods:
- `compile_filters(filters)` - Converts YAML dict to URL-encoded filter string
- `execute_dynamic_screener(filters)` - Executes screener and returns results as list of dicts

### Expected Output Schema

Each result is a dictionary with 151 keys (columns):
```python
{
    "ticker": "AAPL",
    "name": "Apple Inc.",
    "exchange": "NASDAQ",
    # ... 148 more columns
}
```

## Error Handling

| Exception Type | Behavior |
|----------------|----------|
| Config file missing | Prints error and exits gracefully |
| No active scanners | Warns and completes without execution |
| Screener execution error | Catches exception, logs error for that scanner, continues with others |

## Related Files

- **Source**: `dev_utils/live_run_dynamic_scanners.py`
- **Configuration**: `configs/scanners.yaml`
- **API Client**: `src/cobalt_agent/skills/research/finviz_api.py`
- **Related Test**: `dev_utils/live_run_finviz.py` (hardcoded screener test)

## See Also

- [Finviz API Documentation](dev_utils/live_run_finviz.md)
- [Scanner Orchestrator](src/cobalt_agent/skills/research/scanner_orchestrator.md)