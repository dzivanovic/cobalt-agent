---
title: "Universal Extractor Documentation"
status: Active
module: Tool
type: Class
dependencies:
  - "[[postgres]]"
  - "[[config]]"
  - "[[llm]]"
location: "src/cobalt_agent/tools/extractor.py"
tags: [cobalt, dev_docs, graphrag, extractor, llm]
created: 2026-02-28
updated: 2026-02-28
---

# Universal Extractor Module

**Location:** `src/cobalt_agent/tools/extractor.py`

## Overview

The Universal Extractor is an LLM-powered graph entity extraction system that parses raw text content (either Markdown from Fast-Path or AOM from Fallback) into structured graph entities. It implements strict Pydantic schemas matching the database structure and provides a delta engine for computing changes against existing graph state.

### Key Features
- **LLM-Powered Extraction** - Uses LiteLLM to parse entities from unstructured text
- **Strict Pydantic Schemas** - GraphNode and GraphEdge models match database structure
- **Delta Engine** - Computes new edges against existing graph state to silence daemon when no updates exist
- **Postgres Integration** - Automatic upsert of nodes/edges with change tracking

---

## Pydantic Schemas

### `GraphNode`

Represents a graph node (entity) in the knowledge graph.

| Field | Type | Description |
|--|--|--|
| `entity_type` | str | Entity category (e.g., 'Ticker', 'Material', 'Strategy', 'Company', 'Person') |
| `name` | str | Unique entity identifier (e.g., 'TSLA', 'Morning Gapper') |
| `properties` | Dict[str, Any] | Additional JSON metadata (e.g., {'price': 175.50, 'sector': 'Auto'}) |

**Example:**
```json
{
  "entity_type": "Ticker",
  "name": "TSLA",
  "properties": {
    "price": 175.50,
    "sector": "Auto",
    "market_cap": "850B"
  }
}
```

---

### `GraphEdge`

Represents a directed relationship between two graph nodes.

| Field | Type | Description |
|--|--|--|
| `source_name` | str | Name of the source node |
| `target_name` | str | Name of the target node |
| `relationship` | str | Relationship type (e.g., 'TRIGGERED_STRATEGY', 'IS_USED_IN') |
| `properties` | Dict[str, Any] | Additional edge metadata (e.g., {'confidence': 0.95}) |

**Example:**
```json
{
  "source_name": "TSLA",
  "target_name": "Morning Gapper",
  "relationship": "TRIGGERED_STRATEGY",
  "properties": {
    "confidence": 0.95
  }
}
```

---

### `DeltaResult`

Represents the result of delta computation between extracted and existing state.

| Field | Type | Description |
|--|--|--|
| `new_nodes` | List[Dict] | Nodes not present in database |
| `new_edges` | List[Dict] | Edges not present in database |
| `existing_count` | int | Count of edges already in database |

---

### `GraphExtractionOutput`

Output model for LLM extraction results.

| Field | Type | Description |
|--|--|--|
| `nodes` | List[GraphNode] | Extracted graph nodes |
| `edges` | List[GraphEdge] | Extracted graph edges |

---

## Class: `UniversalExtractor`

LLM-powered graph entity extractor.

### Constructor

```python
UniversalExtractor()
```

Initializes:
- LLM client from config
- PostgresMemory instance for delta computation

---

### Methods

#### `extract(raw_text: str) -> GraphExtractionOutput`

Extract graph entities from raw text using LLM.

**Parameters:**
- `raw_text`: The raw text content to extract from (max 15000 characters)

**Returns:** GraphExtractionOutput with nodes and edges

**Extraction Prompt:**

The system prompts the LLM with:
1. **Role**: Graph extraction agent
2. **Schema**: Node and edge JSON schemas
3. **Rules**: Extraction guidelines (all entities, proper types, relationships)
4. **Example**: Sample output format

**Response Format:**
```json
{
  "nodes": [
    {"entity_type": "Ticker", "name": "TSLA", "properties": {...}},
    {"entity_type": "Strategy", "name": "Morning Gapper", "properties": {...}}
  ],
  "edges": [
    {"source_name": "TSLA", "target_name": "Morning Gapper", "relationship": "TRIGGERED_STRATEGY", "properties": {...}}
  ]
}
```

---

## Delta Engine

### `compute_delta(extracted_nodes, extracted_edges, postgres_memory) -> Dict`

Compute the delta between extracted graph entities and existing database state.

**Parameters:**
- `extracted_nodes`: List of GraphNode objects
- `extracted_edges`: List of GraphEdge objects
- `postgres_memory`: Optional PostgresMemory instance for database queries

**Returns:**
```python
{
  "new_nodes": [...],      # List of new nodes (upserted)
  "new_edges": [...],      # List of new edges (upserted)
  "existing_count": 0      # Count of existing edges
}
```

**Algorithm:**
1. Upsert all nodes (get their database IDs)
2. For each edge:
   - Check if edge exists via `get_edges(source_id, direction='out')`
   - If edge exists: increment `existing_count`
   - If new: upsert edge and add to `new_edges`
3. Return delta payload

**Silent Operation Logic:**
- Daemon only triggers Mattermost alert if `new_edges` or `new_nodes` is non-empty
- Empty delta means no new information detected → no notification

---

### `extract_with_delta(raw_text, postgres_memory) -> Dict`

Convenience function combining extraction and delta computation.

**Parameters:**
- `raw_text`: Raw text content to extract from
- `postgres_memory`: Optional PostgresMemory instance

**Returns:**
```python
{
  "nodes": [...],    # All extracted nodes (dicts)
  "edges": [...],    # All extracted edges (dicts)
  "delta": {...}     # Delta payload
}
```

---

## Delta Engine Integration with Watcher Daemon

### Silent Operation Flow

```
┌───────────────────────────────────────────────────────────────────────────────┐
│                      Watcher Daemon Silent Operation                          │
├───────────────────────────────────────────────────────────────────────────────┤
│ 1. Watcher job runs: fetch URL via BrowserTool                                │
│ 2. Extract entities via UniversalExtractor                                    │
│ 3. Compute delta: compute_delta(extracted_nodes, extracted_edges)             │
│ 4. Check delta payload:                                                       │
│    - new_edges = [] AND new_nodes = [] → SILENT (no alert)                   │
│    - new_edges ≠ [] OR new_nodes ≠ [] → TRIGGER MATTERMOST ALERT             │
└───────────────────────────────────────────────────────────────────────────────┘
```

### Mattermost Alert Trigger

```python
delta_payload = compute_delta(nodes, edges, postgres_memory)

if not delta_payload.get("new_edges") and not delta_payload.get("new_nodes"):
    # Silent operation - no new entities
    logger.info("No new entities detected")
    return

# New entities detected - trigger Mattermost interrupt
_send_watcher_alert(url, intent, delta_payload)
```

---

## Usage Examples

### Basic Extraction

```python
from cobalt_agent.tools.extractor import UniversalExtractor

extractor = UniversalExtractor()

# Extract from markdown content
result = extractor.extract("""
TSLA rose 5% after the Morning Gapper Strategy triggered on high volume.
The strategy uses a 80-point score threshold and has a 95% accuracy rate.
""")

print(result.nodes)   # List of GraphNode objects
print(result.edges)   # List of GraphEdge objects
```

### Extraction with Delta

```python
from cobalt_agent.tools.extractor import UniversalExtractor, compute_delta

extractor = UniversalExtractor()
postgres = PostgresMemory()

# First extraction
result1 = extractor.extract("TSLA is a ticker")
delta1 = compute_delta(result1.nodes, result1.edges, postgres)
# Result: new_edges = [...], existing_count = 0

# Second extraction (same content)
result2 = extractor.extract("TSLA is a ticker")
delta2 = compute_delta(result2.nodes, result2.edges, postgres)
# Result: new_edges = [...], existing_count = 1 (edge exists)
```

### Complete Watcher Workflow

```python
from cobalt_agent.tools.extractor import UniversalExtractor, compute_delta
from cobalt_agent.memory.postgres import PostgresMemory

postgres = PostgresMemory()
extractor = UniversalExtractor()

# 1. Fetch content (via BrowserTool Fast Path or Fallback)
content = fetch_from_url(url)

# 2. Extract entities
extraction_result = extractor.extract(content)

# 3. Compute delta against existing graph
delta = compute_delta(
    extraction_result.nodes,
    extraction_result.edges,
    postgres
)

# 4. Trigger alert only if new edges detected
if delta["new_edges"]:
    alert_new_entities(delta)
else:
    logger.info("No new entities - silent operation")
```

---

## LLM Integration

### Model Configuration

Uses `llm.model_name` from `configs/config.yaml`:

```yaml
llm:
  model_name: "gpt-4o-mini"  # Or other supported LiteLLM model
```

### Parameters

- **temperature**: 0.1 (deterministic extraction)
- **response_format**: `{"type": "json_object"}` (enforce JSON output)

---

## Error Handling

### Validation Errors

If LLM response doesn't match Pydantic schema:
1. Logs validation error
2. Returns empty `GraphExtractionOutput(nodes=[], edges=[])`

### JSON Parsing Failures

If response isn't valid JSON:
1. Tries regex extraction (`re.search(r'\{[\s\S]*\}', content)`)
2. If still fails: returns empty result

### Database Errors

If PostgresMemory is unavailable:
1. Logs warning
2. Returns all edges as "new" (no delta computation)
3. No database operations performed

---

## Performance

### Timing Metrics

| Operation | Typical Duration |
|--|--|
| LLM extraction | 1-3s |
| Delta computation | 500ms-2s |
| Postgres upsert (per node) | 100-200ms |
| Postgres edge check | 50-100ms |

### Optimization Tips

1. **Context Limiting**: Extractor truncates input to 15000 characters
2. **Delta Reuse**: Check existing edges before upserting
3. **Batch Processing**: Process multiple pages before committing to DB

---

## Testing

### Unit Tests

- `tests/test_universal_extractor.py` - Tests extraction and delta logic

### Test Scenarios

1. **Basic Extraction**: Valid markdown → nodes/edges
2. **Malformed JSON**: LLM returns non-JSON → empty result
3. **Delta Computation**: Same content → existing_count > 0
4. **No Postgres**: Returns all edges as new

---

## Related Modules

- **Postgres** (`src/cobalt_agent/memory/postgres.py`) - Graph storage with `upsert_node`, `upsert_edge`, `get_edges`
- **Browser** (`src/cobalt_agent/tools/browser.py`) - Provides content for extraction (Fast Path/Fallback)
- **Daemon** (`src/cobalt_agent/tools/daemon.py`) - Uses extractor + delta for watcher jobs
- **Config** (`src/cobalt_agent/config.py`) - LLM model configuration

---

## Migration Notes

### Previous Implementation

- Manual JSON parsing with regex
- No Pydantic validation
- No delta computation

### New Implementation

- LiteLLM for structured JSON output
- Pydantic schemas enforce correctness
- Delta engine silences daemon when no updates

---

## Future Enhancements

1. **Batch Extraction**: Process multiple URLs in parallel
2. **Schema Validation**: Add entity type whitelist from config
3. **Edge Weighting**: Learn relationship weights from history
4. **Delta Compression**: Only store deltas, not full graphs