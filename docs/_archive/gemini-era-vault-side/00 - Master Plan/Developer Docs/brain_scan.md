---
title: "Brain Scan Documentation"
status: Active
module: Utility
type: Script
dependencies:
  - "[[postgres]]"
location: "dev_utils/brain_scan.py"
tags: [cobalt, dev_docs]
created: 2026-02-23
---

# Brain Scan Script

**Location:** `dev_utils/brain_scan.py`

## Overview

Brain Scan is a diagnostic tool that performs a comprehensive health check on the PostgreSQL memory database. It verifies schema integrity, checks for vector embeddings, and confirms content storage.

## Usage

```bash
python dev_utils/brain_scan.py
```

Or with uv:

```bash
uv run python dev_utils/brain_scan.py
```

## Behavior

The script connects to the PostgreSQL database and performs the following checks:

### 1. Schema Verification
- Lists all columns in the `memory_logs` table
- Identifies if a `vector` or `embedding` column exists
- Reports if semantic search is possible

### 2. Content Audit
- Retrieves the last 20 memory entries
- Shows embedding status for each record
- Verifies specific content (e.g., "TSLA") exists in the database

### 3. Diagnosis Report
Outputs a summary with:
- **Schema Health**: Whether vector columns exist
- **Content Status**: Whether expected content is present
- **Embedding Status**: Whether embeddings are populated

## Example Output

```
🔬 Scanning Database: cobalt_memory

📋 Schema for 'memory_logs':
   - id (integer)
   - timestamp (timestamp without time zone)
   - source (text)
   - content (text)
   - embedding (vector)

--- DIAGNOSIS ---
✅ 'TSLA' memory FOUND.
```

## Destructive Warnings

⚠️ **This is a READ-ONLY diagnostic script** - it does not modify the database. However, if the `embedding` column does not exist, semantic search will be impossible, and you may need to run an embedding generation script.

## Dependencies

- `psycopg` - PostgreSQL client library
- `python-dotenv` - Environment variable loading