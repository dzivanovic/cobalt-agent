---
title: "Live Finviz API Runner"
status: Active
module: Utility
type: Integration Test
dependencies: [finviz_api, vault]
location: "dev_utils/live_run_finviz.py"
tags: [finviz, api, testing, macro-engine]
created: 2026-04-07
---

# Live Finviz API Runner - The Macro Engine

**Location:** `dev_utils/live_run_finviz.py`

## Overview

A test utility that performs live, unmocked API calls to Finviz Elite via HTTP. This script validates the `FinvizApiClient` by executing real screener requests and parsing CSV responses into structured data.

## Purpose

This script serves as:
- **Integration Test**: Verifies end-to-end connectivity to Finviz Elite API
- **Latency Benchmark**: Measures actual API response times
- **Data Validation**: Confirms CSV parsing and dictionary conversion works correctly
- **Sort Verification**: Validates that results are returned in expected order (e.g., Volume DESC)

## Prerequisites

### Environment Setup

1. **COBALT_MASTER_KEY**: Must be set in environment
   ```bash
   export COBALT_MASTER_KEY="your-master-key-here"
   ```

2. **Vault Configuration**: Vault must be unlocked with Finviz API token
   - Path: `data/.cobalt_vault`
   - Required entry: `finviz.com::api_token`

3. **Dependencies**: 
   ```bash
   uv sync  # Ensures httpx and other dependencies are installed
   ```

## Usage

### Basic Execution

```bash
# Run the live Finviz API test
uv run dev_utils/live_run_finviz.py
```

### Setting Master Key (One-Time Setup)

```bash
# Add to ~/.zshrc for persistence
export COBALT_MASTER_KEY="your-secure-master-key"
```

## Execution Flow

The script performs these sequential steps:

### Step 1: Load Master Key
```python
master_key = os.getenv("COBALT_MASTER_KEY")
if not master_key:
    print("❌ ERROR: COBALT_MASTER_KEY environment variable not set!")
    sys.exit(1)
```

### Step 2: Initialize Client
```python
vault_path = "data/.cobalt_vault"
client = FinvizApiClient(vault_path=vault_path)
```

The client automatically:
- Resolves `finviz.com::api_token` from Vault
- Sets up authentication headers

### Step 3: Execute Screener Request
```python
result = await client.get_screener("Morning Up Gapper")
```

**Target Endpoint**: `https://elite.finviz.com/export.ashx`

### Step 4: Display Results
- Screener name confirmation
- Total results count
- Execution latency (in seconds)
- First 5 stocks displayed with Volume and Price formatting

## Output Reference

### Success Output Example
```
======================================================================
🚀 COBALT FINVIZ MACRO ENGINE - LIVE API EXECUTION RUNNER
======================================================================

📋 Step 1: Loading COBALT_MASTER_KEY from environment...
✅ Master key loaded (length: 32)

🔐 Step 2: Instantiating FinvizApiClient...
✅ Client initialized successfully

🎯 Step 3: Executing 'Morning Up Gapper' screener request...
   This will:
   - Resolve API token from Vault (finviz.com::api_token)
   - Perform async HTTP GET to elite.finviz.com/export.ashx
   - Parse CSV response into list of dictionaries

======================================================================
📈 API EXECUTION RESULTS
======================================================================

✅ Screener: Morning Up Gapper
📊 Total Results: 47
⏱️  Execution Time (Latency): 1.234 seconds

🔽 First 5 Stocks (sorted by Volume DESC):
----------------------------------------------------------------------
   1. AAPL     | Volume:    52,340,000 | Price: $178.45
   2. TSLA     | Volume:    31,200,000 | Price: $245.67
   3. NVDA     | Volume:    28,100,000 | Price: $467.89
   4. AMD      | Volume:    22,500,000 | Price: $112.34
   5. MSFT     | Volume:    19,800,000 | Price: $378.12

📉 Volume Sort Verification: ✅ CORRECT (descending)

----------------------------------------------------------------------
📋 First 5 Stocks (Pretty-Printed JSON):
----------------------------------------------------------------------
[
  {
    "ticker": "AAPL",
    "name": "Apple Inc.",
    "exchange": "NASDAQ",
    "volume": 52340000,
    "price": 178.45,
    ...
  },
  ...
]

======================================================================
✅ LIVE API EXECUTION COMPLETE
======================================================================
```

### Error Scenarios

| Scenario | Output | Exit Code |
|----------|--------|-----------|
| Missing master key | `❌ ERROR: COBALT_MASTER_KEY environment variable not set!` | 1 |
| Vault initialization error | `❌ ERROR: Failed to initialize client: {error}` | 1 |
| Screener execution failure | `❌ Screener failed with exception: {error}` + traceback | 1 |
| Empty results | `❌ ERROR: No data returned from API` | 1 |

## Key Components

### FinvizApiClient Integration

The script uses the `get_screener()` method:
```python
async def get_screener(screener_name: str) -> List[Dict[str, Any]]
```

**Parameters**:
- `screener_name`: Name of saved screener in Finviz Elite account

**Returns**:
- List of dictionaries, each representing a stock with 151 columns

### Data Structure

Each result dictionary contains:
```python
{
    "ticker": str,           # Stock ticker symbol
    "name": str,             # Company name
    "exchange": str,         # Exchange (NASDAQ, NYSE, etc.)
    "volume": int,           # Trading volume
    "price": float,          # Current price
    # ... 146 more columns
}
```

### Volume Sort Verification

The script validates that results are sorted correctly by:
1. Extracting numeric values from first 10 volumes
2. Checking descending order with `all(volumes[i] >= volumes[i+1])`
3. Reporting verification status

## Error Handling

| Exception Type | Behavior |
|----------------|----------|
| Missing environment variable | Prints setup instructions and exits with code 1 |
| Client initialization failure | Prints error message and exits with code 1 |
| Screener execution exception | Catches exception, prints full traceback, exits with code 1 |
| Empty result set | Prints error and exits with code 1 |

## Related Files

- **Source**: `dev_utils/live_run_finviz.py`
- **API Client**: `src/cobalt_agent/skills/research/finviz_api.py`
- **Vault**: `src/cobalt_agent/security/vault.py`
- **Configuration**: `data/.cobalt_vault`

## See Also

- [Dynamic Scanner YAML Test Runner](dev_utils/live_run_dynamic_scanners.md)
- [Finviz Quote Extractor](dev_utils/live_run_finviz_quote.md)
- [Vault Documentation](src/cobalt_agent/security/vault.md)