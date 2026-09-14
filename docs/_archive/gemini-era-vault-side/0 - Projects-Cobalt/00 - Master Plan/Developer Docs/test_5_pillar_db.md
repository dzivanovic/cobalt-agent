# 5-Pillar Database Integration Test

**Source File:** `dev_utils/test_5_pillar_db.py`  
**Author:** Cobalt SRE  
**Related ADR:** [ADR-015 5-Pillar Relational Schema](../ADR/ADR-015%205-Pillar%20Relational%20Schema.md)  
**Sprint:** Sprint 06 - Data Engine  

---

## Overview

This integration test verifies that the PostgreSQL database correctly handles JSONB columns and foreign key relationships within the 5-Pillar schema. It performs a complete CRUD workflow to validate data serialization, retrieval, and cleanup operations.

---

## Purpose

The script validates the following database capabilities:

1. **Foreign Key Relationships** - Ensures referential integrity between `instruments` and `market_snapshots` tables
2. **JSONB Column Handling** - Tests insertion, querying, and retrieval of JSONB data types
3. **Data Serialization** - Verifies Python dictionaries are correctly serialized to PostgreSQL JSONB and deserialized back
4. **Referential Integrity** - Confirms that orphaned records are prevented via foreign key constraints

---

## Database Schema Context

This test operates on two core tables from the 5-Pillar schema:

### `instruments` Table
| Column | Type | Description |
|--------|------|-------------|
| `id` | UUID (PK) | Primary key |
| `symbol` | VARCHAR(20) UNIQUE | Ticker symbol (e.g., NVDA, AAPL) |
| `asset_class` | VARCHAR(50) | Asset type (EQUITY, COMMODITY, CURRENCY, etc.) |
| `metadata` | JSONB | Extended instrument metadata |

### `market_snapshots` Table
| Column | Type | Description |
|--------|------|-------------|
| `id` | UUID (PK) | Primary key |
| `instrument_id` | UUID (FK → instruments.id) | Reference to instrument |
| `timestamp` | TIMESTAMP | Snapshot capture time |
| `price` | DECIMAL(18, 6) | Market price |
| `volume` | BIGINT | Trading volume |
| `raw_data` | JSONB | Full market data payload |

---

## Workflow Steps

### Step 1: Database Connection
Establishes connection using centralized configuration from `config.py`:
```python
conn = psycopg2.connect(
    host=config.postgres.host,
    port=config.postgres.port,
    database=config.postgres.db,
    user=config.postgres.user,
    password=config.postgres.password,
)
```

### Step 2: Insert Test Instrument
Creates a dummy instrument (`TEST_NVDA`) with JSONB metadata:
```sql
INSERT INTO instruments (symbol, asset_class, metadata)
VALUES ('TEST_NVDA', 'EQUITY', '{"test": true, "created_by": "5_pillar_integration_test"}')
ON CONFLICT (symbol) DO UPDATE SET metadata = EXCLUDED.metadata
RETURNING id;
```

### Step 3: Insert Market Snapshot
Creates a market snapshot with JSONB payload:
```sql
INSERT INTO market_snapshots (instrument_id, price, volume, raw_data)
VALUES (<instrument_id>, 120.50, 5000000, '{"Price": 120.50, "Volume": 5000000, "ATR": 1.5}')
RETURNING id;
```

### Step 4: Query Using JSONB Filter
Tests PostgreSQL's native JSONB query capability:
```sql
SELECT id, instrument_id, timestamp, price, volume, raw_data
FROM market_snapshots
WHERE raw_data->>'Price' = '120.50';
```

### Step 5: Verify Data Integrity
Compares retrieved values against inserted values to confirm round-trip serialization accuracy.

### Step 6: Teardown
Removes all test data to leave the database clean:
```sql
DELETE FROM market_snapshots WHERE id = <snapshot_id>;
DELETE FROM instruments WHERE symbol = 'TEST_NVDA';
```

---

## Functions Reference

| Function | Description | Parameters | Returns |
|----------|-------------|------------|---------|
| `get_db_connection()` | Establishes PostgreSQL connection using config | None | `psycopg2.connection` |
| `insert_test_instrument()` | Inserts test instrument with metadata | `cursor`, `symbol`, `asset_class` | `str` (instrument UUID) |
| `insert_test_snapshot()` | Inserts market snapshot with JSONB payload | `cursor`, `instrument_id`, `raw_data` | `str` (snapshot UUID) |
| `query_snapshot_by_jsonb()` | Queries snapshots using JSONB filter | `cursor`, `price` | `list` of records |
| `delete_snapshot()` | Removes snapshot by ID | `cursor`, `snapshot_id` | None |
| `delete_instrument()` | Removes instrument by symbol | `cursor`, `symbol` | None |
| `run_integration_test()` | Executes full test workflow | None | `bool` (success/failure) |

---

## Dependencies

| Package | Purpose |
|---------|---------|
| `psycopg2` | PostgreSQL driver with JSONB support |
| `psycopg2.extras.RealDictCursor` | Dict-like cursor for named column access |
| `psycopg2.extras.Json` | JSONB serialization helper |

---

## Configuration Requirements

This script requires the following environment variables to be configured in `.env`:

```bash
POSTGRES_HOST=localhost
POSTGRES_PORT=5432
POSTGRES_DB=cobalt
POSTGRES_USER=<username>
POSTGRES_PASSWORD=<password>
```

---

## Execution

### Running the Test
```bash
cd /Users/cobalt/cobalt
python dev_utils/test_5_pillar_db.py
```

### Expected Output
```
============================================================
5-PILLAR DATABASE INTEGRATION TEST
============================================================

[STEP 1] Connecting to PostgreSQL...
✓ Connection established

[STEP 2] Inserting dummy instrument (TEST_NVDA)...
✓ Instrument inserted with ID: <uuid>

[STEP 3] Inserting market snapshot with JSONB payload...
✓ Snapshot inserted with ID: <uuid>

[STEP 4] Querying snapshot with JSONB filter (raw_data->>'Price' = '120.50')...
✓ Query returned 1 result(s)

============================================================
RETRIEVED SNAPSHOT DATA
============================================================

Snapshot ID: <uuid>
Instrument ID: <uuid>
Timestamp: 2026-04-07 13:30:00
Price (from table): 120.50
Volume (from table): 5000000

Raw JSONB Payload:
----------------------------------------
{
    "Price": 120.50,
    "Volume": 5000000,
    "ATR": 1.5
}

----------------------------------------
VERIFICATION:
✓ Price matches: 120.50
✓ Volume matches: 5000000
✓ ATR matches: 1.5

✓ JSONB serialization/deserialization verified successfully!

============================================================
TEARDOWN: Cleaning up test data...
✓ Deleted snapshot ID: <uuid>
✓ Deleted instrument: TEST_NVDA

============================================================
TEST RESULT: ALL CHECKS PASSED
============================================================

The 5-Pillar database schema is ready for Task 2 (Finviz Orchestrator).
```

---

## Error Handling

| Exception Type | Trigger Condition | Response |
|----------------|-------------------|----------|
| `IntegrityError` | FK violation or unique constraint conflict | Rollback, detailed error message |
| `psycopg2.Error` | General database operation failure | Rollback, error details |
| `ValueError` | Missing configuration values | Configuration error message |
| `Exception` | Any unexpected errors | Rollback, full traceback |

---

## Exit Codes

| Code | Meaning |
|------|---------|
| `0` | All tests passed successfully |
| `1` | Test failed or error occurred |

---

## Related Documentation

- [ADR-015 5-Pillar Relational Schema](../ADR/ADR-015%205-Pillar%20Relational%20Schema.md)
- [Sprint 06 - Data Engine](../../90%20-%20Project%20Management/Sprints/Sprint_06_Data_Engine.md)
- [PRD-013 Multidimensional Market Data Engine](../../90%20-%20Project%20Management/Requirements/PRD-013%20Multidimensional%20Market%20Data%20Engine.md)
- [PostgreSQL Memory Core](./postgres.md)

---

## Author Notes

This test is designed to be idempotent and safe for repeated execution. The `ON CONFLICT DO UPDATE` pattern ensures that running the test multiple times won't cause duplicate key errors. The teardown phase guarantees no residual test data remains after execution.