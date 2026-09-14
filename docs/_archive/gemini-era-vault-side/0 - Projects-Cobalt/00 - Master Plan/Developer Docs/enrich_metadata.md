# Metadata Enrichment Skill

## Overview

The `MetadataEnricher` class is a production-grade skill for enriching financial instrument metadata from the Finviz API. It provides an automated bridge between Cobalt's PostgreSQL database and external market data sources, injecting critical financial metrics into the `instruments` table.

## Purpose

This module serves as a programmatic interface for:
- Fetching missing metadata (sector, industry, market cap, etc.) from Finviz
- Updating the central database with accurate financial instrument data
- Supporting scheduled sweeps to find and enrich "starving" tickers

## Architecture

### Dependencies
- `psycopg2`: PostgreSQL database connectivity
- `RealDictCursor`: Dict-based cursor for row access
- `FinvizApiClient`: Internal API client for fetching market data
- `loguru`: Structured logging

### Class: MetadataEnricher

**Signature:**
```python
class MetadataEnricher:
    def __init__(self, batch_size: int = 100)
```

**Parameters:**
- `batch_size`: Number of tickers to process per API request (default: 100)

## Core Components

### `get_db_connection()`

Creates a PostgreSQL connection using central config.

```python
def get_db_connection():
    """Create a Postgres connection using the central config engine."""
```

**Connection Parameters (from config):**
- `host`: Database host
- `port`: Database port
- `database`: Database name
- `user`: Database user
- `password`: Database password

---

### `_get_starving_tickers()`

Fetches all ticker symbols from the database that are missing core metadata.

**Returns:** `List[str]` - List of ticker symbols needing enrichment

**Query Logic:**
```sql
SELECT symbol 
FROM instruments 
WHERE metadata IS NULL 
   OR metadata = '{}'::jsonb 
   OR metadata->>'sector' IS NULL;
```

This identifies instruments with:
- Completely null metadata
- Empty JSON objects (`{}`)
- Missing sector classification

---

### `enrich()`

Executes the metadata enrichment pipeline.

**Signature:**
```python
async def enrich(
    tickers: Optional[List[str]] = None, 
    enrich_starving: bool = False,
    force_update: bool = False
) -> Dict[str, Any]
```

**Parameters:**
| Parameter | Type | Description |
|-----------|------|-------------|
| `tickers` | `List[str]` | Specific tickers to enrich (optional) |
| `enrich_starving` | `bool` | If True, auto-find missing metadata tickers |
| `force_update` | `bool` | Future: overwrite existing data |

**Returns:**
```python
{
    "status": "complete" | "error",
    "tickers_targeted": int,
    "instruments_updated": int,
    "error": str  # Only on error
}
```

---

## Metadata Enrichment Logic

### Data Flow

1. **Target Resolution**: Combine explicit tickers with starving tickers (if enabled)
2. **Batch Processing**: Split into chunks based on `batch_size`
3. **API Query Construction**: Build Finviz export query with master columns
4. **Data Fetching**: Async CSV retrieval via `FinvizApiClient`
5. **Field Mapping**: Transform API response to canonical schema
6. **Validation**: Filter empty/null values and dash placeholders
7. **Database Update**: Upsert enriched metadata with timestamp

### Query Construction

```python
query_string = f"v=152&c={self.client.MASTER_COLUMNS}&t={ticker_str}"
```

**Query Parameters:**
- `v=152`: View template ID for comprehensive instrument data
- `c`: Comma-separated column list (MASTER_COLUMNS)
- `t`: Comma-separated ticker symbols

### Cross-Reference Mechanism

The enrichment process cross-references database instruments with Finviz's market data:

1. **Input**: List of ticker symbols from `instruments` table
2. **Lookup**: Query Finviz export endpoint with tickers via `&t=` parameter
3. **Mapping**: Match API response rows by "Ticker" field to database symbols
4. **Transformation**: Convert string values from API to canonical metadata schema

### Output Formatting for Database Insertion

**Raw Metadata Extraction:**
```python
new_metadata = {
    "sector": row.get("Sector", "").strip(),
    "industry": row.get("Industry", "").strip(),
    "market_cap": row.get("Market Cap.", "") or row.get("Market Cap", ""),
    "shares_float": row.get("Shares Float", "").strip(),
    "short_float": row.get("Short Float", "").strip(),
    "average_volume": row.get("Average Volume", "").strip(),
    "atr": row.get("Average True Range", "").strip()
}
```

**Validation & Cleaning:**
```python
clean_metadata = {k: v for k, v in new_metadata.items() if v and v != "-"}
```

**Database Insertion:**
```sql
UPDATE instruments 
SET metadata = %s, updated_at = CURRENT_TIMESTAMP 
WHERE symbol = %s
```

---

## Metadata Schema

### Canonical Fields

| Field | Type | Description |
|-------|------|-------------|
| `sector` | TEXT | Industry sector (e.g., "Technology", "Healthcare") |
| `industry` | TEXT | Specific industry category |
| `market_cap` | TEXT | Market capitalization (raw string from Finviz) |
| `shares_float` | TEXT | Number of tradable shares |
| `short_float` | TEXT | Short interest percentage |
| `average_volume` | TEXT | Typical daily trading volume |
| `atr` | TEXT | Average True Range (volatility metric) |

### Data Quality Rules
- Empty strings are filtered out
- Dash values (`"-"`) are treated as null/missing data
- Only non-empty, valid values are persisted

---

## Usage Patterns

### Programmatic Usage
```python
from cobalt_agent.skills.research.enrich_metadata import MetadataEnricher

enricher = MetadataEnricher()
stats = await enricher.enrich(tickers=["AAPL", "TSLA"])
```

### CLI / Automated Sweep
```bash
uv run src/cobalt_agent/skills/research/enrich_metadata.py
```

This executes with `enrich_starving=True` by default, automatically finding and enriching all instruments missing sector/industry data.

---

## Database Impact

**Table:** `instruments`  
**Columns Modified:**
- `metadata`: JSONB field containing enriched data
- `updated_at`: Timestamp of last update

---

## Error Handling

The enrichment pipeline includes:
1. **Transaction Rollback**: On any exception, `conn.rollback()` reverts partial updates
2. **Structured Logging**: `loguru` captures full stack traces on failure
3. **Graceful Degradation**: Missing data is filtered, not treated as errors
4. **Safe Iteration**: Individual row failures don't halt batch processing

**Error Response:**
```python
{
    "status": "error",
    "error": str(e)  # Full error message
}
```

---

## Integration Points

| Component | Purpose |
|-----------|---------|
| **Finviz API** | External market data source via `FinvizApiClient` |
| **PostgreSQL** | Persistent storage via psycopg2 |
| **Config System** | Database credentials via `get_config()` |
| **Logger** | Observability via loguru |

---

## File Location

`src/cobalt_agent/skills/research/enrich_metadata.py`