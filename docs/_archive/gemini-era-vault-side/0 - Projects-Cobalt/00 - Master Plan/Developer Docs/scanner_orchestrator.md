# Scanner Orchestrator

**File:** `src/cobalt_agent/skills/research/scanner_orchestrator.py`  
**Purpose:** Orchestrates Finviz screener data ingestion into the 5-Pillar database with deduplication and scanner tagging.

---

## Overview

The `ScannerOrchestrator` class coordinates the ingestion of financial screener data from multiple active scanners. It executes a three-phase pipeline:

1. **Data Fetching** - Retrieves market data from all active scanners concurrently
2. **Deduplication & Tagging** - Consolidates tickers and tracks which scanners found each one
3. **Database Persistence** - Inserts instruments and market snapshots into the 5-Pillar schema

---

## Class Architecture

### ScannerOrchestrator

```python
class ScannerOrchestrator:
    def __init__(self, db_connection: Any, client: Any, scanners_config_path: str = "configs/scanners.yaml")
    
    async def run_ingestion_cycle(self) -> None
```

**Constructor Parameters:**

| Parameter | Type | Description |
|-----------|------|-------------|
| `db_connection` | `Any` | PostgreSQL database connection (psycopg2) |
| `client` | `Any` | Finviz API client with `execute_dynamic_screener` method |
| `scanners_config_path` | `str` | Path to scanners YAML configuration (default: `configs/scanners.yaml`) |

---

## Execution Flow: `run_ingestion_cycle()`

### Phase 1: Load Configuration & Identify Active Scanners

```python
with open(self.scanners_config_path, "r") as f:
    config = yaml.safe_load(f)

scanners = config.get("scanners", {})
active_scanners = {k: v for k, v in scanners.items() if v.get("active", False)}
```

**Process:**
1. Loads scanner configuration from YAML file
2. Filters to only scanners with `active: true`
3. Returns early if no active scanners found

---

### Phase 2: Concurrent Data Fetching

```python
all_results = []
for scanner_name, scanner_config in active_scanners.items():
    filters = scanner_config.get("filters", {})
    data = await self.client.execute_dynamic_screener(filters)
    all_results.append((scanner_name, data))
```

**Process:**
- Iterates through each active scanner
- Extracts filter parameters from scanner config
- Calls `client.execute_dynamic_screener(filters)` to fetch data
- Stores results as tuples of `(scanner_name, row_data[])`

**Error Handling:**
- Individual scanner failures are logged but do not halt the cycle
- Failed scanners are skipped; successful ones continue processing

---

### Phase 3: Deduplication & Scanner Tagging

```python
deduped_tickers = {}
for scanner_name, rows in all_results:
    for row in rows:
        ticker = row.get("Ticker") or row.get("1_Ticker") or row.get("ticker") or ""
        ticker = str(ticker).strip().upper()
        
        if not ticker or ticker == "NONE":
            continue
        
        if ticker not in deduped_tickers:
            row["active_on_scanners"] = [scanner_name]
            deduped_tickers[ticker] = row
        else:
            if scanner_name not in deduped_tickers[ticker]["active_on_scanners"]:
                deduped_tickers[ticker]["active_on_scanners"].append(scanner_name)
```

**Deduplication Logic:**

| Step | Action |
|------|--------|
| 1 | Normalize ticker: handle `Ticker`, `1_Ticker`, or lowercase variants |
| 2 | Strip whitespace and convert to uppercase |
| 3 | Skip empty tickers or `"NONE"` values |
| 4 | First occurrence: initialize with `[scanner_name]` |
| 5 | Subsequent occurrences: append scanner name to `active_on_scanners` list |

**Output:** Dictionary mapping ticker symbols → full row data with `active_on_scanners` field

---

### Phase 4: Database Persistence (Pillars 1 & 2)

```python
with self.db.cursor() as cursor:
    for ticker, raw_data in deduped_tickers.items():
        # Step A: Upsert Instrument
        cursor.execute("""
            INSERT INTO instruments (symbol, asset_class, metadata, active_themes)
            VALUES (%s, 'EQUITY', '{}'::jsonb, '[]'::jsonb)
            ON CONFLICT (symbol) DO UPDATE 
            SET updated_at = CURRENT_TIMESTAMP
            RETURNING id;
        """, (ticker,))
        
        instrument_id = cursor.fetchone()[0]
        
        # Step B: Insert Market Snapshot
        cursor.execute("""
            INSERT INTO market_snapshots (instrument_id, timestamp, raw_data)
            VALUES (%s, %s, %s)
        """, (instrument_id, datetime.now(timezone.utc), Json(raw_data)))
```

**Database Operations:**

1. **Instrument Upsert (cobalt_brain.instruments)**
   - Inserts new equity instrument with symbol
   - On conflict: updates `updated_at` timestamp
   - Returns `instrument_id` for foreign key reference

2. **Market Snapshot Insert (cobalt_brain.market_snapshots)**
   - Stores full raw data as JSONB
   - Timestamps with UTC timezone awareness
   - Links to parent instrument via `instrument_id`

**Commit:** Single transaction commit after all insertions

---

## Configuration Schema

The orchestrator reads from `configs/scanners.yaml`:

```yaml
scanners:
  scanner_name:
    active: true
    filters:
      # Finviz screener filter parameters
      market_cap: "over2b"
      price: "over10"
      # Additional filter criteria...
```

**Key Configuration Fields:**

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `active` | `bool` | Yes | Enables/disables scanner |
| `filters` | `dict` | No | Screener filter parameters passed to API |

---

## Database Schema Integration

### Tables Modified

| Table (Pillar) | Purpose | Key Columns |
|----------------|---------|-------------|
| `instruments` (Pillar 1) | Core entity registry | `id`, `symbol`, `asset_class`, `metadata`, `active_themes` |
| `market_snapshots` (Pillar 2) | Time-series market data | `instrument_id`, `timestamp`, `raw_data` (JSONB) |

### Data Flow Diagram

```
┌─────────────────┐     ┌──────────────────┐     ┌─────────────────────┐
│  Scanner Config │────▶│ Active Scanners  │────▶│ Fetch Data via API  │
└─────────────────┘     └──────────────────┘     └─────────────────────┘
                                                                        │
                                                                        ▼
┌───────────────────────────────────────────────────────────────────────────┐
│                    DEDUPLICATION & TAGGING                                │
│  ticker → active_on_scanners: ["scanner1", "scanner2"]                   │
└───────────────────────────────────────────────────────────────────┬───────┘
                                                                    │
                                                                    ▼
                    ┌──────────────────┐     ┌─────────────────────┐
                    │ instruments (1)  │────▶│ market_snapshots(2) │
                    └──────────────────┘     └─────────────────────┘
```

---

## Error Handling Strategy

| Failure Point | Behavior |
|---------------|----------|
| Scanner API failure | Log error, skip scanner, continue with others |
| Missing ticker field | Skip row, log warning |
| Database insertion failure | Log error for specific ticker, continue with others |
| No active scanners | Log warning, exit gracefully |
| No unique tickers after dedup | Log warning, exit without DB writes |

---

## Usage Example

```python
from cobalt_agent.memory.postgres import PostgresMemory
from cobalt_agent.skills.research.scanner_orchestrator import ScannerOrchestrator

# Initialize database connection
db = PostgresMemory()  # psycopg2 connection
client = FinvizClient()  # API client with execute_dynamic_screener method

# Create orchestrator
orchestrator = ScannerOrchestrator(db, client)

# Execute ingestion cycle
await orchestrator.run_ingestion_cycle()
```

**Expected Console Output:**

```
Loading scanners config from configs/scanners.yaml
Executing 2 active scanner(s)...
Scanner momentum: Fetched 15 rows
Scanner value: Fetched 8 rows
Total Unique Tickers after deduplication: 18
Processing 18 unique instruments into cobalt_brain...
Successfully inserted 18 snapshots into cobalt_brain.

============================================================
INGESTION CYCLE SUMMARY
============================================================
Active scanners executed: 2
Unique instruments processed: 18
Snapshots inserted:       18
============================================================
```

---

## Integration Points

### Upstream Dependencies
- `configs/scanners.yaml` - Scanner configuration definitions
- `FinvizClient.execute_dynamic_screener()` - Data fetching interface

### Downstream Consumers
- **Cortex** - Query market snapshots for context generation
- **Watcher Daemon** - Triggers periodic ingestion cycles
- **Analytics Modules** - Read historical snapshot data

---

## Related Documentation

- [5-Pillar Relational Schema](../ADR/ADR-015%205-Pillar%20Relational%20Schema.md)
- [Finviz API](finviz_api.md) - Screener data source
- [PostgreSQL Persistence](postgres.md) - Database layer
- [PRD-013: Multidimensional Market Data Engine](../../../90%20-%20Project%20Management/Requirements/PRD-013%20Multidimensional%20Market%20Data%20Engine.md)