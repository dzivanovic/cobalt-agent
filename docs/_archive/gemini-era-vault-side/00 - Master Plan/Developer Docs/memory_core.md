---
title: "Memory Core Documentation"
status: Active
module: Memory
type: Class
dependencies:
  - "[[memory_base]]"
  - "[[postgres]]"
location: "src/cobalt_agent/memory/core.py"
tags: [cobalt, dev_docs]
created: 2026-02-23
updated: 2026-02-27
---

# Memory Core Module

**Location:** `src/cobalt_agent/memory/core.py`

## Overview

Memory System Core (JSON Implementation) manages short-term (RAM) and long-term (Disk) memory for the Cobalt Agent.

## Class: `MemorySystem`

Manages:
- Short-term memory: Last 10 interactions (RAM - Fast)
- Long-term memory: Persistent storage in `data/memory.json` (Disk - Safe)

Implements the `MemoryProvider` interface from `base.py`.

### Constructor

```python
MemorySystem(memory_file: str = "data/memory.json")
```

**Parameters:**
- `memory_file`: Path to the memory JSON file.

### Attributes

- `memory_file`: Path to the memory storage file
- `short_term`: List of last 10 interactions (RAM)
- `long_term`: Dictionary containing all historical logs (Disk)

### Methods

#### `add_log(message: str, source: str = "System", data: Dict = None) -> None`
Add a message to both short-term and long-term memory.

**Parameters:**
- `message`: The memory content
- `source`: Origin of the memory (default: "System")
- `data`: Optional dictionary of additional data

Automatically saves to disk and maintains RAM limit of 10 entries.

#### `get_context(limit: int = 10) -> List[Dict[str, Any]]`
Fast retrieval of short-term memory for AI prompts.

**Parameters:**
- `limit`: Number of recent interactions to retrieve

**Returns:** List of memory entries sorted by timestamp.

#### `search(query: str, limit: int = 5) -> List[Dict[str, Any]]`
Simple keyword search through long-term memory.

**Parameters:**
- `query`: Search string to match against memory messages
- `limit`: Maximum number of results

**Returns:** List of matching memory entries (newest first).

#### `save_memory() -> None`
Save long-term memory to disk.

#### `load_memory() -> None`
Load long-term memory from disk and hydrate short-term RAM.

---

## Memory Entry Format

```python
{
    "timestamp": "2026-02-22T23:00:00",
    "source": "System",
    "message": "Strategy scan completed",
    "data": {"strategy": "second_day_play", "score": 75}
}
```

---

## Fast Path: pgvector Macro Caching

### Overview

The Fast Path implementation uses PostgreSQL with pgvector extension for millisecond-latency execution of repeated browser automation tasks. Bypasses LLM inference by matching new tasks to previously cached solutions using cosine similarity on task hashes.

### Architecture

```
User Task Request
    ↓
Compute Task Intent Hash (SHA-256)
    ↓
Query pgvector (cosine similarity > 0.85)
    ↓
    ├─> CACHE HIT → Execute Stored Script (5-10ms)
    │
    └─> CACHE MISS → LLM Inference (1-3s) → Store in Cache
```

### Task Hash Computation

```python
import hashlib
import json

def compute_task_hash(task_intent: str, context_signature: str) -> str:
    """
    Compute SHA-256 hash from task intent + context signature.
    
    Parameters:
        task_intent: Description of the task (e.g., "click login button")
        context_signature: Page context (URL + title + visible text preview)
    
    Returns:
        Hex string of SHA-256 hash
    """
    data = {
        "intent": task_intent,
        "context": context_signature
    }
    data_str = json.dumps(data, sort_keys=True)
    return hashlib.sha256(data_str.encode()).hexdigest()
```

### Fast Path Table Schema

```sql
CREATE TABLE browser_fast_path (
    id SERIAL PRIMARY KEY,
    task_hash UUID NOT NULL,
    task_intent TEXT NOT NULL,
    context_signature TEXT NOT NULL,
    element_tree_snapshot JSONB NOT NULL,
    playwright_script TEXT NOT NULL,
    execution_time_ms INTEGER NOT NULL,
    success_rate FLOAT NOT NULL DEFAULT 1.0,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE INDEX idx_task_hash ON browser_fast_path USING HASH (task_hash);
CREATE INDEX idx_created_at ON browser_fast_path (created_at);
```

### Fields

| Field | Type | Description |
|--|--|--|
| `task_hash` | `UUID` | Hash of task intent + context signature |
| `task_intent` | `TEXT` | Human-readable task description |
| `context_signature` | `TEXT` | Page context for similarity matching |
| `element_tree_snapshot` | `JSONB` | AOM elements at time of caching |
| `playwright_script` | `TEXT` | Native Playwright script to execute |
| `execution_time_ms` | `INTEGER` | Actual execution time in milliseconds |
| `success_rate` | `FLOAT` | Success rate for this cached task |
| `created_at` | `TIMESTAMP` | Cache entry creation time |

### Cosine Similarity Lookup

```python
from typing import Optional, Dict, Any
import numpy as np

def find_cached_task(
    task_hash: str,
    context_embedding: np.ndarray,
    threshold: float = 0.85
) -> Optional[Dict[str, Any]]:
    """
    Query pgvector for similar cached tasks.
    
    Parameters:
        task_hash: SHA-256 hash of task intent + context
        context_embedding: Vector embedding of current page context
        threshold: Minimum cosine similarity (default 0.85)
    
    Returns:
        Cached task entry if found, None otherwise
    """
    # Query Postgres with cosine similarity
    query = """
        SELECT task_hash, task_intent, playwright_script, execution_time_ms, success_rate
        FROM browser_fast_path
        WHERE task_hash = %s
        ORDER BY created_at DESC
        LIMIT 1
    """
    # Use vector cosine distance < (1 - threshold) for similarity
    # cosine_distance = 1 - cosine_similarity
    # So we want cosine_distance < 0.15 for threshold=0.85
    return execute_query(query, (task_hash,))
```

### Cache Hit Macro Execution

```python
def execute_cached_task(cached_task: Dict[str, Any]) -> str:
    """
    Execute cached Playwright script natively (bypass LLM).
    
    Parameters:
        cached_task: Fast Path cache entry
    
    Returns:
        Result of script execution
    """
    script = cached_task["playwright_script"]
    
    # Execute natively via Playwright
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        # ... navigate and execute script ...
        result = page.evaluate(script)
        browser.close()
    
    return result
```

### Cache Invalidation

```python
def invalidate_old_cache(days: int = 30) -> int:
    """
    Remove cache entries older than specified days.
    
    Parameters:
        days: Age threshold in days
    
    Returns:
        Number of entries deleted
    """
    query = """
        DELETE FROM browser_fast_path
        WHERE created_at < NOW() - INTERVAL '%s days'
        RETURNING id
    """
    deleted = execute_query(query, (days,))
    return len(deleted)
```

### Performance Metrics

| Metric | Target |
|--|--|
| Cache hit latency | <20ms (vs 1-3s for LLM) |
| Cache hit ratio | >70% for repeated tasks |
| Cache invalidation | Weekly job (30-day threshold) |

### Integration Points

- **BrowserTool** (`src/cobalt_agent/tools/browser.py`) - Uses Fast Path for action execution
- **AOMExtractor** (`src/cobalt_agent/tools/aom.py`) - Provides element tree snapshots
- **PostgresMemory** (`src/cobalt_agent/memory/postgres.py`) - pgvector storage and queries

### Debugging

Enable debug logging for Fast Path operations:

```python
import logging
logging.basicConfig(level=logging.DEBUG)

# See cache hit/miss decisions
# See query execution times
# See cache invalidation events
```

### Best Practices

1. **Context Signature Quality** - Include URL, title, and visible text preview for accurate matching
2. **Threshold Selection** - 0.85 provides good balance; lower for more matches, higher for precision
3. **Cache Invalidation** - Run weekly to remove stale cached tasks
4. **Success Rate Tracking** - Monitor and invalidate low-success-rate entries

### Error Handling

| Error Type | Handling |
|--|--|
| Cache lookup timeout | Fall back to LLM inference |
| Script execution failure | Re-extract AOM and retry |
| Database connection error | Log and continue without Fast Path |
