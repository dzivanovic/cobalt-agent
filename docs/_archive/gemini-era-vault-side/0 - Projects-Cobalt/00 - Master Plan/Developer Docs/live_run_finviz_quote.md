---
title: "Finviz Quote API Test Runner"
status: Active
module: Utility
type: Integration Test
dependencies: [finviz_api]
location: "dev_utils/live_run_finviz_quote.py"
tags: [finviz, api, testing, quote]
created: 2026-04-07
---

# Finviz Quote API Test Runner

**Location:** `dev_utils/live_run_finviz_quote.py`

## Overview

A standalone test script that evaluates the latency and payload structure of the `get_quote` endpoint from Finviz Elite API. This script provides high-precision timing measurements without modifying existing screener tests.

## Purpose

This script serves as:
- **Latency Benchmark**: Measures API response time using `time.perf_counter()` for high precision
- **Payload Validation**: Verifies the structure and content of quote API responses
- **Isolated Testing**: Tests `get_quote()` independently from screener functionality

## Prerequisites

### Dependencies

```bash
uv sync  # Ensures httpx and other dependencies are installed
```

### Configuration

No environment variables required. The script uses default Vault path (`data/.cobalt_vault`) and automatically resolves the Finviz API token.

## Usage

### Basic Execution

```bash
# Run the quote API test (default ticker: NVDA)
uv run dev_utils/live_run_finviz_quote.py
```

## Execution Flow

The script performs these sequential steps:

### Step 1: Display Header
```python
def print_header():
    print(f"{Colors.CYAN}{'=' * 60}{Colors.RESET}")
    print(f"{Colors.BOLD}Finviz Quote API Test Runner{Colors.RESET}")
    print(f"{Colors.CYAN}{'=' * 60}{Colors.RESET}")
```

### Step 2: Initialize Client
```python
client = FinvizApiClient()
```

The client automatically:
- Loads Vault from default path (`data/.cobalt_vault`)
- Resolves `finviz.com::api_token` for authentication

### Step 3: Execute Quote Request with High-Precision Timing
```python
start_time = time.perf_counter()
result = await client.get_quote(ticker)
elapsed_time = time.perf_counter() - start_time
```

**Why `perf_counter()`?**
- Provides highest available resolution for timing measurements
- Suitable for benchmarking sub-millisecond latencies

### Step 4: Display Results
- Latency in milliseconds and seconds
- Success confirmation
- Full JSON payload structure (pretty-printed)
- Total rows returned count

## Output Reference

### Success Output Example
```
============================================================
Finviz Quote API Test Runner
============================================================
Target Ticker: NVDA

Latency: 847.23 ms (0.8472 s)
✅ Data retrieved successfully

Payload Structure (first dictionary):
------------------------------------------------------------
{
  "ticker": "NVDA",
  "name": "NVIDIA Corporation",
  "exchange": "NASDAQ",
  "sector": "Technology",
  "industry": "Semiconductors",
  "market_cap": 1234567890,
  "price": 467.89,
  "change_percent": "+2.34%",
  "volume": 28100000,
  ...
}

------------------------------------------------------------
Total rows returned: 1
```

### Error Scenarios

| Scenario | Output | Exit Code |
|----------|--------|-----------|
| API authentication failure | `❌ ERROR: Failed to fetch quotes: {error}` | 0 (graceful) |
| Network timeout | `❌ ERROR: Failed to fetch quotes: {error}` | 0 (graceful) |
| Empty response | `⚠️  WARNING: No data returned from API` | 0 (graceful) |

## Key Components

### FinvizApiClient Integration

The script uses the `get_quote()` method:
```python
async def get_quote(ticker: str) -> List[Dict[str, Any]]
```

**Parameters**:
- `ticker`: Stock ticker symbol (e.g., "NVDA", "AAPL")

**Returns**:
- List containing single dictionary with quote data

### Data Structure

Each quote dictionary contains:
```python
{
    "ticker": str,           # Stock ticker symbol
    "name": str,             # Company name
    "exchange": str,         # Exchange (NASDAQ, NYSE, etc.)
    "sector": str,           # Industry sector
    "industry": str,         # Specific industry
    "market_cap": int,       # Market capitalization
    "price": float,          # Current price
    "change_percent": str,   # Daily change percentage
    "volume": int,           # Trading volume
    # ... additional fields
}
```

### Color Output System

The script uses ANSI color codes for enhanced readability:

| Color | Code | Usage |
|-------|------|-------|
| Cyan | `\033[96m` | Headers, separators |
| Green | `\033[92m` | Success messages, latency |
| Yellow | `\033[93m` | Warnings |
| Red | `\033[91m` | Errors |
| Blue | `\033[94m` | General highlights |
| Bold | `\033[1m` | Emphasis on key text |

### JSON Formatting Utility

```python
def format_json(data, indent=2):
    """Pretty-print JSON data."""
    return json.dumps(data, indent=indent, default=str)
```

The `default=str` parameter ensures non-serializable objects are converted to strings.

## Error Handling

The script uses graceful error handling:
- Exceptions are caught and displayed with descriptive messages
- Script continues execution after errors (exit code 0)
- No abrupt terminations

```python
try:
    result = await client.get_quote(ticker)
except Exception as e:
    print_error(f"Failed to fetch quotes: {e}")
```

## Target Ticker Configuration

The default ticker is hardcoded as "NVDA":
```python
TARGET_TICKER = "NVDA"
```

To test a different ticker, modify this constant before running.

## Related Files

- **Source**: `dev_utils/live_run_finviz_quote.py`
- **API Client**: `src/cobalt_agent/skills/research/finviz_api.py`
- **Vault**: `src/cobalt_agent/security/vault.py`

## See Also

- [Live Finviz API Runner](dev_utils/live_run_finviz.md) - Screener endpoint testing
- [Dynamic Scanner YAML Test Runner](dev_utils/live_run_dynamic_scanners.md) - YAML-based scanner testing