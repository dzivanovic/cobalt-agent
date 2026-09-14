# Semantic Tagger

**File Path:** `src/cobalt_agent/skills/research/semantic_tagger.py`  
**Module Type:** Batch Processing / Semantic Tagging Engine  
**Last Updated:** 2026-04-08

---

## Overview

The `SemanticTagger` class implements a recursive, batch-processing semantic tagging system that assigns market themes to financial instruments (stocks) using controlled vocabulary from the PostgreSQL database. It operates as **Step 3** in Cobalt's research pipeline, following data extraction and enrichment phases.

This module is designed for **drip-feeding** untagged instruments through an LLM-powered tagging process, ensuring deterministic JSON output and maintaining database consistency.

---

## Architecture

### Core Components

| Component | Type | Purpose |
|-----------|------|---------|
| `SemanticTagger` | Class | Main batch processing engine |
| `ThemeAssignment` | Pydantic Model | Schema for LLM theme assignments |
| `ThemeAssignmentResponse` | Pydantic Model | Schema for complete LLM response |
| `InstrumentThemeState` | Pydantic Model | Schema for theme state stored in database |
| `process_entire_queue()` | Function | Orchestrates full pipeline execution |

---

## SemanticTagger Class

### Initialization

```python
SemanticTagger(batch_size: int = 20)
```

**Parameters:**
- `batch_size` (int): Number of instruments to process per batch (default: 20)

**Attributes:**
- `batch_size`: Configurable batch size for processing
- `conn`: Database connection handle (lazy-initialized)
- `config`: Central configuration instance

---

### Methods

#### `_get_db_connection()`

Creates or retrieves a PostgreSQL connection using centralized configuration from `cobalt_agent.config`.

**Returns:** Postgres connection object

---

#### `_get_active_themes() -> list[str]`

Queries the `themes` table for all ACTIVE theme names to establish the controlled vocabulary.

**SQL Query:**
```sql
SELECT name FROM themes WHERE status ILIKE 'active' ORDER BY name ASC
```

**Returns:** Sorted list of active theme names (e.g., `["Nuclear Energy", "AI Infrastructure", ...]`)

---

#### `_get_untagged_batch(limit: int = 20) -> list[dict]`

Retrieves untagged instruments from the `instruments` table. Filters for records where:
- `active_themes IS NULL`
- `active_themes = '[]'::jsonb`
- `jsonb_array_length(active_themes) = 0`

**Returns:** List of instrument dictionaries containing:
- `id`: Database record ID
- `ticker`: Stock symbol
- `company_name`: Company full name
- `sector`: Industry sector (from metadata)
- `industry`: Specific industry (from metadata)

---

#### `_build_prompt(active_themes: list[str], instruments: list[dict]) -> str`

Constructs the LLM prompt by:
1. Formatting instrument data into JSON structure
2. Loading prompt template from `configs/prompts.yaml` (research.semantic_tagger key)
3. Falling back to built-in template if config is unavailable

**Prompt Structure:**
```
You are a semantic tagging assistant. Assign market themes to stocks from the ALLOWED_LIST below.

ALLOWED THEMES (use ONLY these exact names):
{themes}

INSTRUMENTS TO TAG:
{instruments}

Return a JSON array with this exact schema:
{{"assignments": [{{"ticker": "NVDA", "themes": ["Nuclear Energy"]}}]}}
```

---

#### `_format_theme_state(theme_names: list[str]) -> list[dict]`

Converts theme names into the database-ready state format.

**Returns:** List of theme state objects:
```json
[{"theme": "Nuclear Energy", "status": "HOT", "added_at": "2026-04-08"}]
```

---

#### `_update_instruments(assignments: list[dict]) -> int`

Persists LLM-tagged themes back to the `instruments.active_themes` JSONB column.

**Logic:**
- For each assignment, constructs theme state with status:
  - **HOT/ACTIVE**: Themes successfully assigned by LLM
  - **NONE**: Fallback state for omitted tickers (`[{"theme": "Not Tagged Yet", "status": "NONE"}]`)
- Updates `updated_at` timestamp

**Returns:** Count of successfully updated records

---

#### `run_batch() -> dict[str, Any]`

Executes a single batch processing cycle:

**Workflow:**
1. Fetch untagged instruments via `_get_untagged_batch()`
2. If queue empty → return early with status "complete" (0 processed)
3. Fetch active themes via `_get_active_themes()`
4. Build prompt via `_build_prompt()`
5. Invoke LLM with temperature=0.0 (deterministic mode)
6. Extract JSON via `_extract_json()`
7. Reconcile "ghost tickers" (LLM omissions → force fallback state)
8. Update database via `_update_instruments()`
9. Return result dictionary

**Returns:**
```json
{
  "status": "complete",
  "instruments_processed": 20,
  "instruments_updated": 18,
  "duration_seconds": 45.2
}
```

---

#### `_extract_json(response: str) -> str`

Sanitizes LLM response by:
1. Stripping `<thought>` reasoning tags (splits at `</think>`)
2. Removing markdown code fences (` ```json ` and ` ``` `)
3. Isolating JSON object between first `{` and last `}`

**Returns:** Clean JSON string ready for parsing

---

## Process Functions

### `process_entire_queue(batch_size: int = 50) -> dict`

Orchestrates continuous processing until the instrument queue is exhausted.

**Loop Behavior:**
1. Instantiate `SemanticTagger` with configured batch size
2. Execute `run_batch()`
3. If failed → pause 15 seconds, retry
4. Accumulate totals (batches processed, instruments tagged)
5. If `instruments_processed == 0` → queue empty, exit loop
6. Cool-down: Sleep 3 seconds between batches (KV cache management)

**Returns:**
```json
{
  "status": "complete",
  "total_batches": 12,
  "total_tagged": 580
}
```

---

## Role in Research Pipeline

The Semantic Tagger operates within Cobalt's **5-Pillar Relational Schema** research workflow:

```
┌─────────────────┐    ┌──────────────────┐    ┌─────────────────────┐
│  Finviz Extract │ →  │ Enrich Metadata  │ →  │ Semantic Tagger     │
└─────────────────┘    └──────────────────┘    └─────────────────────┘
                                                                    ↓
                    ┌───────────────────────────────────────────┐  │
                    │        PostgreSQL (Themes + Instruments)  │  │
                    └───────────────────────────────────────────┘  │
                                                                    ↓
                                                    ┌───────────────────────┐
                                                    │ Sync Taxonomy / ADR-016│
                                                    └───────────────────────┘
```

**Input:** Untagged instruments from `instruments` table  
**Output:** Populated `active_themes` JSONB column with structured theme assignments

---

## Database Schema Integration

### Tables Used

| Table | Purpose | Key Columns |
|-------|---------|-------------|
| `themes` | Controlled vocabulary | `name`, `status` (ACTIVE/INACTIVE) |
| `instruments` | Financial instrument data | `symbol`, `metadata`, `active_themes` (JSONB) |

### Theme State Schema

Stored in `instruments.active_themes`:
```json
[
  {
    "theme": "Nuclear Energy",
    "status": "ACTIVE",
    "added_at": "2026-04-08"
  }
]
```

---

## Configuration

### Prompt Template Location

**File:** `configs/prompts.yaml`  
**Key Path:** `prompts.research.semantic_tagger`

If missing, falls back to built-in template in `_get_fallback_prompt_template()`.

---

## Usage Examples

### Command Line Execution

```bash
python -m src.cobalt_agent.skills.research.semantic_tagger
```

### Programmatic Usage

```python
from src.cobalt_agent.skills.research.semantic_tagger import (
    SemanticTagger, 
    process_entire_queue
)

# Process single batch
tagger = SemanticTagger(batch_size=20)
result = tagger.run_batch()

# Process entire queue
final_result = process_entire_queue(batch_size=50)
```

---

## Error Handling

| Scenario | Behavior |
|----------|----------|
| Empty queue | Returns early with `instruments_processed: 0` |
| LLM omission | Forces "ghost ticker" into fallback state (`themes: []`) |
| Database error | Rolls back transaction, logs error via `logger.error()` |
| JSON parse failure | Exception caught in `run_batch()`, returns `status: failed` |

---

## Logging Output

**Info Level:**
- Batch processing status
- Number of instruments processed/updated
- Duration metrics

**Warning Level:**
- LLM omissions (ghost tickers)

**Error Level:**
- Database update failures
- Batch processing exceptions

---

## Dependencies

| Package | Purpose |
|---------|---------|
| `psycopg2` | PostgreSQL connectivity |
| `pydantic` | Schema validation |
| `loguru` | Structured logging |
| `cobalt_agent.config` | Central configuration |
| `cobalt_agent.llm` | LLM integration |

---

## Related Documentation

- **ADR-016:** [Semantic Taxonomy Engine](../ADR/ADR-016%20Semantic%20Taxonomy%20Engine.md)
- **ADR-015:** [5-Pillar Relational Schema](../ADR/ADR-015%205-Pillar%20Relational%20Schema.md)
- **PRD-013:** [Multidimensional Market Data Engine](../../Requirements/PRD-013%20Multidimensional%20Market%20Data%20Engine.md)
- **Master Taxonomy:** [Master_Taxonomy.md](../../Master_Taxonomy.md)

---

## Technical Notes

### Design Principles

1. **Deterministic Output:** Temperature locked at 0.0 for consistent JSON
2. **Recursive Processing:** Batch-based drip engine prevents memory overflow
3. **Controlled Vocabulary:** Only ACTIVE themes from database are valid
4. **Fallback Safety:** Ghost tickers forced into fallback state (no silent failures)
5. **Idempotent Operations:** Can be re-run without side effects

### Performance Considerations

- Batch size configurable (default: 20-50 instruments)
- 3-second cooldown between batches for KV cache management
- 15-second retry delay on failure

---

*Documentation generated by Cobalt Agent Technical Scribe*