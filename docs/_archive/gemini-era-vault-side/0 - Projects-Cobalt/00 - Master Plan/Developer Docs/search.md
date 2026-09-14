---
title: "Search Tool Documentation"
status: Active
module: Tool
type: Class
dependencies:
  - "[[tool_manager]]"
location: "src/cobalt_agent/tools/search.py"
tags: [cobalt, dev_docs]
created: 2026-02-23
---

# Search Tool Module

**Location:** `src/cobalt_agent/tools/search.py`

## Overview

Search Tool provides internet search functionality using the `ddgs` package. Returns strict Pydantic models instead of raw dictionaries.

## Class: `SearchResult` (Pydantic Model)

A single search result item.

### Fields

| Field | Type | Description |
|-------|------|---------|
| `title` | `str` | The title of the search result |
| `href` | `str` | The URL link to the result |
| `body` | `str` | The snippet or summary text |

---

## Class: `SearchTool`

Executes internet searches and returns structured results.

### Attributes

| Attribute | Value |
|--|--|
| `name` | `"search"` |
| `description` | `"Search the internet for news, information, and general knowledge. Use for questions about current events, topics, or general queries."` |

### Methods

#### `run(query: str, max_results: int = 5) -> List[SearchResult]`

Executes a search and returns a list of typed SearchResult objects.

**Parameters:**
- `query`: Search query string
- `max_results`: Maximum number of results to return (default: 5)

**Returns:** List of SearchResult objects

**Workflow:**
1. Execute search using DDGS context manager
2. Convert raw results to Pydantic models
3. Handle malformed results gracefully
4. Return empty list on failure

### Usage Example

```python
tool = SearchTool()
results = tool.run(" Cobalt AI agent", max_results=3)
for result in results:
    print(f"{result.title}: {result.href}")