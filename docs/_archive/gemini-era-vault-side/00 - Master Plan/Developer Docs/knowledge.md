# Knowledge Search Tool

## Overview
`cobalt_agent/tools/knowledge.py`

The `KnowledgeSearchTool` class provides semantic search capabilities against the agent's internal vector database containing codebase, playbooks, and Obsidian vault.

## Class: KnowledgeSearchTool

### Description
Search the agent's internal vector database (codebase, playbooks, and Obsidian vault) for semantic context.

### Attributes
- `name`: "search_knowledge"
- `description`: "Search the agent's internal vector database (codebase, playbooks, and Obsidian notes) for semantic context. Pass a conceptual query string."

### Constructor
```python
def __init__(self)
```

Initializes:
1. Creates `PostgresMemory` instance for vector database access

### Methods

#### run
```python
def run(self, query=None, **kwargs) -> str
```

Searches the vector DB and returns formatted results.

**Parameters:**
- `query` (Optional[str]): Search query string
- `**kwargs`: Additional parameters (supports dict format)

**Returns:** Formatted search results as a string

### Input Parsing
The method handles multiple input formats:
1. **String input:** Uses directly
2. **JSON string:** Parsed with `json.loads()`
3. **Python dict literal:** Parsed with `ast.literal_eval()`
4. **Dict:** Extracts `query` or `search` key

### Search Execution
1. Extracts search query from input
2. Calls `memory.search()` with query and limit of 5
3. Formats results with source, relevance score, and content

### Result Format
```
### Knowledge Base Results for '{query}':

**Result 1** (Source: `filepath`, Relevance: 0.85)
```text
content
```

**Result 2** (Source: `filepath`, Relevance: 0.82)
```text
content
```
```

### Error Handling
- Returns error message if search query is missing
- Returns message if no relevant information found
- Logs errors and returns formatted error string on exception

## Key Components
- `PostgresMemory`: Vector database backend

## See Also
- `SearchTool` - Web search tool
- `BrowserTool` - Browser automation tool
- `PostgresMemory` - Vector database integration