# Database Status Audit Utility (db_status.py)

## Overview

A comprehensive full-stack database audit utility that connects to the `cobalt_brain` PostgreSQL database and displays health metrics for all core tables using Rich formatting.

## Purpose

This utility provides real-time visibility into the state of Cobalt Agent's PostgreSQL database by:
- Dynamically extracting table names from `schema.sql`
- Displaying sample data rows for each table
- Computing and presenting health metrics (record counts, unique values, status breakdowns)
- Gracefully handling missing or empty tables with a clean "zero-state" UI (no stack traces)

## Usage

```bash
uv run dev_utils/db_status.py
```

## Features

### 1. Dynamic Schema Discovery
Automatically parses `src/cobalt_agent/db/schema.sql` to extract all table names using regex matching on `CREATE TABLE` statements.

### 2. Per-Table Audit Output
For each table, the utility displays:
- **Data Sample**: Up to 2 rows of actual data (or "Table missing or empty" status)
- **Health Metrics**: Table-specific metrics such as:
  - `instruments`: Total Records, Unique Tickers, Tagged/Untagged counts, Active/Inactive status
  - `daily_market_data`: Total Records, Unique Tickers, Latest Date Recorded
  - `corporate_events`: Total Events, Unique Tickers, Events in Last 7 Days
  - `intraday_bars`: Total Records, Unique Tickers, Latest Timestamp
  - `scanner_alerts`: Total Alerts, Alerts Today
  - `strategy_signals`: Total Signals, Risk Grade Breakdown, Status Breakdown
  - `trade_proposals`: Total Proposals, HITL Status Breakdown
  - `audit_logs`: Total Logs, Department Breakdown, Status Breakdown

### 3. Zero-State UI
When a table is missing or empty:
- Displays "Table missing or empty" instead of stack traces
- Shows all metrics as `0` or `N/A` for a clean, user-friendly output

### 4. Rich Terminal Formatting
Uses the [Rich](https://rich.readthedocs.io/) library for:
- Styled tables with rounded borders
- Color-coded output (cyan for samples, green for metrics)
- Clear section headers and status indicators

## Dependencies

- `psycopg2-binary`: PostgreSQL database adapter
- `rich`: Terminal UI formatting library

## Configuration

Connects to the PostgreSQL database using credentials from `config.yaml`:
- `postgres.host`
- `postgres.port`
- `postgres.user`
- `postgres.password`
- `postgres.db`

## Error Handling

| Scenario | Behavior |
|----------|----------|
| Database connection failure | Displays error message and suggests checking PostgreSQL service |
| Missing table | Shows "Table missing or empty" with zero-state metrics |
| Empty table | Displays sample as "Table missing or empty", metrics show 0 |
| Schema parsing error | Reports error and exits with code 1 |

## Output Example

```
╔══════════════════════════════════════════════════════════╗
║           Cobalt Agent Database Audit Utility            ║
╚══════════════════════════════════════════════════════════╝

Connecting to cobalt_brain database...
✓ Connected successfully

============================================================
Auditing table: instruments

=== INSTRUMENTS ===
Metrics -> Total: 150 | Unique: 45 | Tagged: 30
┌───────────┬────────────┬──────────────┐
│ symbol    │ name       │ active_themes│
├───────────┼────────────┼──────────────┤
│ AAPL      │ Apple Inc. │ ["tech"]     │
│ MSFT      │ Microsoft  │ []           │
└───────────┴────────────┴──────────────┘

╭─ instruments - Data Sample ─────────────────────────────╮
│ Status: Table has data                                  │
╰─────────────────────────────────────────────────────────╯

╭─ instruments - Health Metrics ──────────────────────────╮
│ Metric              │ Value                             │
├────────────────────┼───────────────────────────────────┤
│ Total Records       │ 150                               │
│ Total Unique Tickers│ 45                                │
│ Total Tagged        │ 30                                │
│ ...                 │ ...                               │
╰─────────────────────────────────────────────────────────╯

============================================================
✓ Audit Complete!
```

## Related Files

- **Source**: `dev_utils/db_status.py`
- **Schema Reference**: `src/cobalt_agent/db/schema.sql`
- **Configuration**: `configs/config.yaml`
- **Test Suite**: `tests/test_postgres_memory.py`

## See Also

- [ADR-015 5-Pillar Relational Schema](../ADR/ADR-015%205-Pillar%20Relational%20Schema.md)
- [PostgreSQL Memory Core](postgres.md)