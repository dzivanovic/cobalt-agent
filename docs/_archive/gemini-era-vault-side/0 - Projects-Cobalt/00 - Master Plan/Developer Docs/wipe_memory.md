---
title: "Wipe Memory Documentation"
status: Active
module: Utility
type: Script
dependencies:
  - "[[postgres]]"
location: "dev_utils/wipe_memory.py"
tags: [cobalt, dev_docs]
created: 2026-02-23
---

# Wipe Memory Script

**Location:** `dev_utils/wipe_memory.py`

## Overview

Wipe Memory is a utility script that removes all data from any table in the PostgreSQL public schema. It finds all tables and truncates them without dropping them.

## Usage

```bash
python dev_utils/wipe_memory.py
```

Or with uv:

```bash
uv run python dev_utils/wipe_memory.py
```

## ⚠️ Destructive Warning

🚨 **THIS SCRIPT DELETES ALL DATA FROM ALL TABLES** in the public schema - all records will be permanently lost. This action cannot be undone.

**Before running:**
1. Ensure you have a database backup
2. Verify you are connected to the correct database
3. Understand that ALL tables will be truncated

## Behavior

The script performs the following actions:

1. Connects to PostgreSQL using credentials from `.env` or environment variables
2. Queries the `information_schema.tables` to find all tables in the public schema
3. Truncates each table found (removes all rows)
4. Prints the name of each table being wiped

## Environment Variables

| Variable | Default | Description |
|--|--|--|
| `POSTGRES_HOST` | `localhost` | Database host |
| `POSTGRES_DB` | `cobalt_memory` | Database name |
| `POSTGRES_USER` | `postgres` | Database user |
| `POSTGRES_PASSWORD` | `cobalt_password` | Database password |

## Typical Use Case

This script is used when:
- You need to clear all memory logs for testing
- You want to reset the database to empty state
- You are debugging and need a clean slate

**After running:**
- All tables remain (schema intact), but all rows are deleted
- You may need to re-seed any reference data

## Dependencies

- `psycopg` - PostgreSQL client library
- `python-dotenv` - Environment variable loading