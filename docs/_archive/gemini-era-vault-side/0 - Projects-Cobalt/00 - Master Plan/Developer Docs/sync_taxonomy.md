# Sync Taxonomy Module

**File**: `src/cobalt_agent/skills/research/sync_taxonomy.py`  
**Purpose**: Synchronizes the Master Taxonomy markdown file with the PostgreSQL `public.themes` table

---

## Overview

The Sync Taxonomy module is a database synchronization script that parses the hierarchical theme taxonomy from `Master_Taxonomy.md` and maintains parity with the PostgreSQL `public.themes` table using a recursive parent-child structure.

---

## Architecture

### Input Source
- **File**: `Master_Taxonomy.md` located in the Obsidian vault at `{obsidian_vault_path}/0 - Projects/Cobalt/00 - Master Plan/Master_Taxonomy.md`
- **Format**: Markdown table with 4 columns: Macro Theme, Sub-Theme, Status, Example Tickers

### Database Target
- **Table**: `public.themes` (recursive/self-referential schema)
- **Schema Fields**:
  - `id`: Primary key
  - `name`: Theme name (unique within parent context)
  - `parent_id`: NULL for macro themes, references child theme ID for sub-themes
  - `status`: Theme status (e.g., ACTIVE, INACTIVE)
  - `example_tickers`: Comma-separated ticker symbols
  - `updated_at`: Timestamp of last modification

---

## Core Functions

### `get_db_connection(config)`
Establishes a PostgreSQL connection using credentials from the configuration object.

**Parameters**:
- `config`: Pydantic config object containing `postgres` connection settings

**Returns**: `psycopg2` database connection

---

### `parse_markdown_table(file_path: Path) -> list[dict]`
Parses the Master Taxonomy markdown file and extracts theme data.

**Parsing Logic**:
1. Detects table start by finding header row containing `| Macro Theme |` and `| Sub-Theme |`
2. Skips separator line containing `| :---` or `|---`
3. Extracts data rows starting with `|`
4. Parses pipe-delimited columns:
   - Column 1: Macro Theme name
   - Column 2: Sub-Theme name (optional)
   - Column 3: Status (converted to uppercase)
   - Column 4: Example tickers

**Returns**: List of dictionaries with keys: `macro_theme`, `sub_theme`, `status`, `example_tickers`

**Error Handling**: Returns empty list if file not found; logs error via logger

---

### `upsert_themes(conn, themes: list[dict])`
Performs upsert (insert or update) operations on the `public.themes` table.

**Algorithm**:
1. **Macro Theme (Parent)**:
   - Query existing record by `name` where `parent_id IS NULL`
   - If found: Update status and tickers only when no sub-theme exists
   - If not found: Insert new macro theme (with or without tickers depending on sub-theme presence)

2. **Sub-Theme (Child)**:
   - Uses PostgreSQL `ON CONFLICT (name, parent_id) DO UPDATE` for atomic upsert
   - Updates `status`, `example_tickers`, and `updated_at` on conflict

**Transaction**: Commits all changes after processing entire theme list; rolls back on exception

---

### `sync_taxonomy()`
Main entry point orchestrating the full synchronization workflow.

**Execution Flow**:
1. Load configuration via `get_config()`
2. Construct path to `Master_Taxonomy.md` from Obsidian vault config
3. Parse taxonomy data via `parse_markdown_table()`
4. Exit early if no themes parsed (logs warning)
5. Establish database connection
6. Call `upsert_themes()` to sync data
7. Commit and log success; rollback on error
8. Close database connection in `finally` block

---

## Database Schema Reference

The `public.themes` table uses a self-referential hierarchy:

```sql
-- Conceptual schema
CREATE TABLE public.themes (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    parent_id INTEGER REFERENCES public.themes(id),
    status VARCHAR(50),
    example_tickers TEXT,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UNIQUE(name, parent_id)  -- Enforces uniqueness within hierarchy level
);
```

---

## Configuration Dependencies

| Source | Key Path | Purpose |
|--------|----------|---------|
| `config.yaml` / `.env` | `postgres.host`, `postgres.port`, `postgres.db`, `postgres.user`, `postgres.password` | Database connection credentials |
| `config.yaml` / `.env` | `system.obsidian_vault_path` | Location of Master_Taxonomy.md file |

---

## Execution

### Direct Execution
```bash
python -m src.cobalt_agent.skills.research.sync_taxonomy
# or
uv run python src/cobalt_agent/skills/research/sync_taxonomy.py
```

### Programmatic Invocation
```python
from src.cobalt_agent.skills.research.sync_taxonomy import sync_taxonomy

sync_taxonomy()  # Returns None; logs results
```

---

## Error Handling

| Scenario | Behavior |
|----------|----------|
| Taxonomy file missing | Logs error, returns empty list, sync exits early |
| No themes parsed | Logs warning, function returns without DB connection |
| Database connection failure | Exception caught, logged, rollback executed |
| Upsert constraint violation | Handled by PostgreSQL `ON CONFLICT` clause |

---

## Related Documentation

- **ADR-015**: 5-Pillar Relational Schema
- **ADR-016**: Semantic Taxonomy Engine
- **Master_Taxonomy.md**: Source taxonomy definition
- **postgres.md**: PostgreSQL integration documentation