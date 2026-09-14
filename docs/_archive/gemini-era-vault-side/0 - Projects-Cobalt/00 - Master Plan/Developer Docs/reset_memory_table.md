---
title: "Reset Memory Table Documentation"
status: Active
module: Utility
type: Script
dependencies:
  - "[[postgres]]"
location: "dev_utils/reset_memory_table.py"
tags: [cobalt, dev_docs]
created: 2026-02-23
---

# Reset Memory Table Script

**Location:** `dev_utils/reset_memory_table.py`

## Overview

Reset Memory Table drops the `memory_logs` table from the PostgreSQL database. Use this when the schema is incorrect and needs to be recreated from scratch.

## Usage

```bash
python dev_utils/reset_memory_table.py
```

Or with uv:

```bash
uv run python dev_utils/reset_memory_table.py
```

## ⚠️ Destructive Warning

🚨 **THIS SCRIPT DELETES THE ENTIRE memory_logs TABLE** - All data in the table will be permanently lost. This action cannot be undone.

**Before running:**
1. Ensure you have a database backup
2. Verify the table name (`memory_logs`)
3. Confirm this is the correct table to reset

## Behavior

The script performs the following actions:

1. Connects to PostgreSQL using credentials from `.env` or environment variables
2. Drops the `memory_logs` table if it exists
3. Prints confirmation of successful deletion

## Environment Variables

| Variable | Default | Description |
|--|--|--|
| `POSTGRES_HOST` | `localhost` | Database host |
| `POSTGRES_DB` | `cobalt_memory` | Database name |
| `POSTGRES_USER` | `postgres` | Database user |
| `POSTGRES_PASSWORD` | `cobalt_password` | Database password |

## Typical Use Case

This script is used when:
- The database schema has been incorrectly initialized
- A schema migration has failed
- You need to start fresh with a new schema

**After running:**
1. Run the schema creation script to rebuild the table
2. Re-run any necessary data seeding scripts

## Dependencies

- `psycopg` - PostgreSQL client library
- `python-dotenv` - Environment variable loading