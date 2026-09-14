---
title: "5-Pillar Schema Initialization"
status: Active
module: Utility
type: Migration Script
dependencies: [postgres]
location: "dev_utils/init_5_pillar_schema.py"
tags: [cobalt, database, schema, migration]
created: 2026-02-23
---

# 5-Pillar Schema Initialization Script

**Location:** `dev_utils/init_5_pillar_schema.py`

## Overview

A safe database migration script that initializes the 12-table 5-Pillar Relational Schema for Cobalt Agent. It performs a controlled teardown of legacy market data tables while explicitly preserving Cortex conversational memory tables.

## Purpose

This script handles the database schema migration with critical safety guarantees:
- **Safe Teardown**: Drops only legacy `tickers` table, never touching Cortex memory tables
- **Schema Creation**: Creates 12 new tables for the 5-Pillar architecture
- **Verification**: Validates all expected tables exist after migration
- **Rollback Safety**: Uses transaction commits per statement to avoid blocking

## Prerequisites

1. PostgreSQL database running and accessible
2. Credentials configured in `.env`:
   ```bash
   POSTGRES_HOST=localhost
   POSTGRES_PORT=5432
   POSTGRES_USER=cobalt
   POSTGRES_PASSWORD=<your-password>
   POSTGRES_DB=cobalt
   ```
3. `psycopg2` package installed:
   ```bash
   uv add psycopg2-binary
   ```

## Usage

### Basic Execution

```bash
# Initialize the 5-Pillar schema (default)
uv run dev_utils/init_5_pillar_schema.py
```

## Execution Flow

The script performs these steps in sequence:

### Step 1: Load Database Credentials
```
[INIT] Loading PostgreSQL credentials from cobalt_agent.config...
[INIT] Connecting to PostgreSQL at localhost:5432/cobalt
[INIT] ✓ Database connection established
```

### Step 2: Safe Teardown
Drops ONLY the legacy `tickers` table:
```sql
DROP TABLE IF EXISTS tickers CASCADE;
```

**Critical Safety Guarantee**: Cortex memory tables are NEVER touched:
- `memory` (conversational memory)
- `conversation_metadata`
- `graph_nodes`, `graph_edges` (knowledge graph)

### Step 3: Schema Creation
Executes `src/cobalt_agent/db/schema.sql` containing the 12-table schema:

| Table | Purpose |
|-------|---------|
| `daily_in_play` | Active trading instruments for the day |
| `instruments` | Master instrument metadata |
| `key_levels` | Support/resistance and price levels |
| `market_snapshots` | Point-in-time market state captures |
| `news_events` | News article metadata and content |
| `news_mentions` | Entity mentions in news (linking table) |
| `order_fills` | Executed trade orders |
| `system_alerts` | System notifications and alerts |
| `themes` | Market themes and sentiment tracking |
| `trading_accounts` | Account balances and status |
| `trades` | Trade history and positions |

### Step 4: Verification
```
[INIT] ✓ Tables in database:
[INIT]   ✓ daily_in_play
[INIT]   ✓ instruments
[INIT]   ✓ key_levels
...
[INIT] SUCCESS: 5-Pillar Schema initialized successfully!
```

## Output Reference

### Success Output
```
============================================================
Cobalt Agent - 5-Pillar Schema Initialization
============================================================
[INIT] Loading PostgreSQL credentials from cobalt_agent.config...
[INIT] Connecting to PostgreSQL at localhost:5432/cobalt
[INIT] ✓ Database connection established
------------------------------------------------------------
[INIT] Step 1: Safe teardown of legacy market data tables
[INIT] ✓ Legacy 'tickers' table dropped (if existed)
[INIT] ✓ Cortex memory tables PRESERVED (not touched)
------------------------------------------------------------
[INIT] Step 2: Creating new 12-table 5-Pillar Schema
[INIT] Reading SQL schema from: src/cobalt_agent/db/schema.sql
[INIT] Created extension
[INIT] Created table: instruments
...
[INIT] ✓ Executed 12 SQL statements from schema.sql
------------------------------------------------------------
[INIT] Step 3: Verifying schema creation
[INIT] ✓ Tables in database:
...
------------------------------------------------------------
============================================================
SUCCESS: 5-Pillar Schema initialized successfully!
[INIT] Created 11 tables for the 5-Pillar Relational Schema
============================================================
[INIT] Database connection closed
```

### Error Handling

| Scenario | Behavior |
|----------|----------|
| Schema file not found | Exits with error, no changes made |
| Database connection failed | Exits immediately with error message |
| SQL statement failure | Logs warning, continues with remaining statements |
| Missing expected tables | Exits with error listing missing tables |

## Related Files

- **Source**: `dev_utils/init_5_pillar_schema.py`
- **Schema Definition**: `src/cobalt_agent/db/schema.sql`
- **ADR Reference**: [ADR-015 5-Pillar Relational Schema](../ADR/ADR-015%205-Pillar%20Relational%20Schema.md)

## See Also

- [PostgreSQL Memory Core](../postgres.md)
- [Cortex Conversational Memory](cortex.md)