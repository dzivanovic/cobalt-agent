# Finviz API Client Documentation

## Overview

The `FinvizApiClient` is an ultra-fast asynchronous HTTP client designed for Finviz Elite authenticated CSV exports. It bypasses browser automation entirely by directly querying `elite.finviz.com` API endpoints, providing 10-50x performance improvement over Playwright-based extraction methods.

## Role in Research Architecture

This module serves as the **Macro Engine** within Cobalt's research infrastructure, enabling:
- Real-time market screener data retrieval
- Individual stock quote extraction
- Ticker-specific and general market news aggregation
- Dynamic filter-based screener execution

It integrates with the Vault system for secure credential management and provides async/non-blocking data retrieval for high-throughput research workflows.

---

## Architecture

### Core Components

```
FinvizApiClient
├── Credential Management (VaultManager)
├── Screener Execution (get_screener, execute_dynamic_screener)
├── Quote Fetching (get_quote)
├── News Retrieval (get_news)
└── CSV Parsing Layer (_fetch_csv)
```

### Data Flow

1. **Vault Resolution**: Extract domain from URL, query VaultManager for API token
2. **HTTP Request**: Construct authenticated CSV endpoint URL with `httpx.AsyncClient`
3. **CSV Parsing**: Parse raw CSV string using `csv.DictReader(io.StringIO)`
4. **Return**: List of dictionaries with dynamic column names as keys

---

## Finviz Endpoints

### Base URL
```
https://elite.finviz.com
```

### Available Endpoints

| Endpoint | Purpose | Authentication |
|----------|---------|----------------|
| `export.ashx` | Screener results export | `auth={api_token}` |
| `quote_export.ashx` | Individual stock quote data | `auth={api_token}` |
| `news_export.ashx` | Ticker-specific or general news | `auth={api_token}` |

### Endpoint Query Parameters

#### Screener Export (`export.ashx`)
- `v=152` - Custom export mode (enables full column selection)
- `c={columns}` - Comma-separated list of column indices (0-150 for all 151 columns)
- `f={filters}` - Comma-separated filter pairs (e.g., `sh_avgvol_o2000,sh_curvol_o100`)
- `o={sort}` - Sort order (e.g., `-volume` for descending)

#### Quote Export (`quote_export.ashx`)
- `t={TICKER}` - Stock ticker symbol
- `ty=c` - Output type: CSV
- `p=d` - Period: Daily
- `b=1` - Include basic quote fields

#### News Export (`news_export.ashx`)
- `t={TICKER}` - Optional ticker symbol (omitted for general market news)

---

## Screener Presets

The client includes predefined screener presets mapped to query strings:

| Preset Name | Description | Key Filters |
|-------------|-------------|-------------|
| `Morning Up Gapper` | High-volume upward gap scanners | `ta_gap_u3`, `sh_avgvol_o2000` |
| `Morning Down Gapper` | High-volume downward gap scanners | `ta_gap_d3`, `sh_avgvol_o2000` |
| `Morning Low Float Runners` | Low float gap-up scanners | `sh_float_u10`, `ta_gap_u10` |
| `Day Scan Custom` | High-volume momentum scan | `sh_curvol_o10000`, `sh_relvol_o3` |

### Master Columns (All 151)
The client uses `MASTER_COLUMNS` to fetch complete data extraction across all available Finviz fields (indices 0-150).

---

## API Reference

### Class: `FinvizApiClient`

#### Initialization
```python
def __init__(self, vault_path: str = "data/.cobalt_vault")
```

**Parameters:**
- `vault_path` - Path to the encrypted vault file for credential storage (default: `"data/.cobalt_vault"`)

#### Methods

##### `compile_filters(filters_dict: Dict[str, str]) -> str`
Converts a filter dictionary into Finviz's comma-separated format.

**Example:**
```python
{"sh_price": "o1", "ta_gap": "u3"} → "sh_price_o1,ta_gap_u3"
```

##### `execute_dynamic_screener(filters_dict: Dict[str, str]) -> List[Dict[str, Any]]`
Executes a dynamic screener with arbitrary filters using all 151 columns.

**Parameters:**
- `filters_dict` - Dictionary of filter names to values (e.g., `{"sh_avgvol": "o2000", "sh_curvol": "o100"}`)

**Returns:** List of dictionaries containing screener results with all 151 columns

**Raises:**
- `httpx.TimeoutException` - Network timeout
- `httpx.HTTPError` - HTTP request failure

##### `get_screener(preset_name: str) -> List[Dict[str, Any]]`
Fetches screener results for a named preset.

**Parameters:**
- `preset_name` - Name of the screener preset (e.g., `"Morning Up Gapper"`)

**Returns:** List of dictionaries containing screener results

**Raises:**
- `ValueError` - Preset name not found in `PRESET_QUERIES` mapping

##### `get_quote(ticker: str) -> List[Dict[str, Any]]`
Fetches quote data for a specific ticker.

**Parameters:**
- `ticker` - Stock ticker symbol (e.g., `"AAPL"`)

**Returns:** List of dictionaries containing quote data

##### `get_news(ticker: Optional[str] = None) -> List[Dict[str, Any]]`
Fetches news data for a ticker or general market news.

**Parameters:**
- `ticker` - Stock ticker symbol (optional). If `None`, returns general market news.

**Returns:** List of dictionaries containing news data

---

### Convenience Functions

#### `fetch_finviz_screener(preset_name: Optional[str] = None, vault_path: str = "data/.cobalt_vault") -> List[Dict[str, Any]]`
Convenience function to fetch Finviz screener data.

**Parameters:**
- `preset_name` - Screener preset name (default: `"Morning Up Gapper"`)
- `vault_path` - Path to encrypted vault file

#### `fetch_finviz_quote(ticker: str, vault_path: str = "data/.cobalt_vault") -> List[Dict[str, Any]]`
Convenience function to fetch Finviz quote data.

**Parameters:**
- `ticker` - Stock ticker symbol
- `vault_path` - Path to encrypted vault file

#### `fetch_finviz_news(ticker: Optional[str] = None, vault_path: str = "data/.cobalt_vault") -> List[Dict[str, Any]]`
Convenience function to fetch Finviz news data.

**Parameters:**
- `ticker` - Stock ticker symbol (optional)
- `vault_path` - Path to encrypted vault file

---

## Security Model

### Vault Integration
- **Zero Trust Architecture**: API tokens are NEVER hardcoded
- **Dynamic Resolution**: Credentials resolved at runtime via `VaultManager`
- **Namespace Format**: `{domain}::api_token` (e.g., `finviz.com::api_token`)

### Credential Resolution Flow
1. Extract domain from target URL using `urllib.parse.urlparse`
2. Query VaultManager for credentials in namespace format
3. If vault is locked, attempt unlock via `COBALT_MASTER_KEY` env var or config `master_key`
4. Retrieve API token and append to requests as `auth={token}`

---

## Error Handling

| Error Type | Condition | Response |
|------------|-----------|----------|
| `ValueError` | Missing API token in vault | `"Finviz API token not found in vault. Please ensure '{api_token_key}' is set."` |
| `ValueError` | Invalid preset name | `"Preset '{preset_name}' not found. Available presets: [...]"` |
| `httpx.TimeoutException` | Network timeout | Logged + re-raised |
| `httpx.HTTPError` | HTTP 4xx/5xx response | Logged + re-raised |

---

## Dependencies

| Package | Purpose |
|---------|---------|
| `httpx` | Async HTTP client for non-blocking requests |
| `csv` | CSV parsing via `DictReader` |
| `io` | String buffer for CSV parsing |
| `urllib.parse` | URL/domain parsing and query string building |
| `loguru` | Structured logging |

---

## Usage Examples

### Basic Screener Query
```python
from cobalt_agent.skills.research.finviz_api import fetch_finviz_screener

results = await fetch_finviz_screener("Morning Up Gapper")
for row in results:
    print(f"{row['s']}: ${row['price']} - Vol: {row['volume']}")
```

### Dynamic Screener
```python
from cobalt_agent.skills.research.finviz_api import FinvizApiClient

client = FinvizApiClient()
results = await client.execute_dynamic_screener({
    "sh_avgvol": "o2000",
    "sh_curvol": "o100",
    "ta_gap": "u3"
})
```

### Quote Fetching
```python
from cobalt_agent.skills.research.finviz_api import fetch_finviz_quote

quote = await fetch_finviz_quote("AAPL")
print(quote)  # List of dicts with quote data
```

### News Retrieval
```python
from cobalt_agent.skills.research.finviz_api import fetch_finviz_news

# Ticker-specific news
news = await fetch_finviz_news("TSLA")

# General market news
market_news = await fetch_finviz_news()
```

---

## Performance Characteristics

| Metric | Value |
|--------|-------|
| **Latency** | 10-50x faster than Playwright-based extraction |
| **Concurrency** | Fully async/non-blocking I/O |
| **Data Format** | Direct CSV parsing (no HTML overhead) |
| **Throughput** | Limited only by network and Finviz rate limits |

---

## Configuration

### Environment Variables
| Variable | Purpose |
|----------|---------|
| `COBALT_MASTER_KEY` | Master key for vault unlock fallback |

### Config File (`config.yaml`)
```yaml
system:
  debug_mode:
    vault:
      master_key: <optional_master_key>
```

---

## File Structure

```
src/cobalt_agent/skills/research/finviz_api.py
├── FinvizApiClient (class)
│   ├── Constants (FINVIZ_DOMAIN, MASTER_COLUMNS, PRESET_QUERIES)
│   ├── __init__ (initialization)
│   ├── compile_filters (filter formatting)
│   ├── execute_dynamic_screener (dynamic query execution)
│   ├── _initialize_vault (vault setup)
│   ├── _resolve_vault_credentials (credential resolution)
│   ├── _fetch_csv (base CSV fetcher)
│   ├── get_screener (preset screener retrieval)
│   ├── get_quote (quote data retrieval)
│   └── get_news (news data retrieval)
├── fetch_finviz_screener (convenience function)
├── fetch_finviz_quote (convenience function)
└── fetch_finviz_news (convenience function)
```

---

## Related Documentation

- [`vault.md`](../vault.md) - VaultManager security architecture
- [`config.md`](../config.md)` - Configuration management
- `PRD-013 Multidimensional Market Data Engine` - Product requirements