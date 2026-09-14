---
title: "Memory Base Documentation"
status: Active
module: Memory
type: Class
dependencies:
  - "[[memory_core]]"
  - "[[postgres]]"
location: "src/cobalt_agent/memory/base.py"
tags: [cobalt, dev_docs]
created: 2026-02-23
---

# Memory Base Module

**Location:** `src/cobalt_agent/memory/base.py`

## Overview

Memory Interface (The Contract) defines how Agents interact with memory, regardless of storage implementation (JSON vs Postgres).

## Class: `MemoryProvider` (ABC)

Abstract Base Class for Memory. Any memory system (JSON, SQL, Vector) MUST implement these methods.

### Methods

#### `add_log(message: str, source: str = "System", data: Dict = None) -> None`
Record an event or thought.

**Parameters:**
- `message`: The memory content
- `source`: Origin of the memory (default: "System")
- `data`: Optional dictionary of additional data

#### `get_context(limit: int = 10) -> List[Dict[str, Any]]`
Get recent conversation history (Short Term RAM).

**Parameters:**
- `limit`: Maximum number of recent interactions to retrieve

**Returns:** List of memory entries

#### `search(query: str, limit: int = 5) -> List[Dict[str, Any]]`
Find relevant memories based on meaning/content.

**Parameters:**
- `query`: Search query string
- `limit`: Maximum number of results to return

**Returns:** List of matching memory entries

**Notes:**
- For JSON storage: Uses keyword search
- For Postgres: Uses vector search

---

## Implementation Pattern

Any memory provider must inherit from `MemoryProvider`:

```python
from cobalt_agent.memory.base import MemoryProvider

class MyMemoryProvider(MemoryProvider):
    def add_log(self, message, source="System", data=None):
        # Implementation here
        pass
    
    def get_context(self, limit=10):
        # Implementation here
        return []
    
    def search(self, query, limit=5):
        # Implementation here
        return []