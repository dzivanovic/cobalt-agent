---
title: "Memory Postgres Documentation"
status: Active
module: Memory
type: Class
dependencies:
  - "[[memory_base]]"
  - "[[memory_core]]"
  - "[[config]]"
location: "src/cobalt_agent/memory/postgres.py"
tags: [cobalt, dev_docs, pgvector, fast-path]
created: 2026-02-23
updated: 2026-02-27
---

# Postgres Memory Module

**Location:** `src/cobalt_agent/memory/postgres.py`

## Overview

Postgres Memory Adapter (The Hippocampus) provides persistent memory with vector embeddings for semantic search. Combines database persistence with AI-powered similarity search.

**Phase 3 Update:** Fast Path caching via `browser_fast_path` table with pgvector for millisecond-latency browser task execution.

## Class: `PostgresMemory`

Implements `MemoryProvider` interface from `base.py`.

### Constructor

```python
PostgresMemory()
```

Initializes database connection and auto-creates tables. Loads credentials from:
1. Environment variables: `POSTGRES_HOST`, `POSTGRES_DB`, `POSTGRES_USER`, `POSTGRES_PASSWORD`
2. YAML config in `configs/*.yaml`

### Methods

#### `add_log(message: str, source: str = "System", data: Dict = None) -> None`
Saves a memory AND its vector embedding to Postgres.

**Parameters:**
- `message`: Memory content to store
- `source`: Origin of the memory (default: "System")
- `data`: Optional dictionary for metadata

**Workflow:**
1. Generate vector embedding using LiteLLM (`text-embedding-3-small`)
2. Insert into database with content, embedding, and metadata

#### `get_context(limit: int = 10) -> str`
Retrieve recent logs (Short Term RAM) from database.

**Parameters:**
- `limit`: Number of recent entries to retrieve

**Returns:** Formatted chat-log string (chronological order)

#### `search(query: str, limit: int = 5) -> List[Dict]`
Semantic search - finds memories similar to the query using vector cosine distance.

**Parameters:**
- `query`: Search query string
- `limit`: Maximum number of results

**Returns:** List of matching memories with similarity scores (filtering out scores < 0.3)

### Attributes

| Attribute | Description |
|--|--|
| `conn_str` | PostgreSQL connection string |
| `table_name` | Table name: "memory_logs" |
| `host`, `port`, `db`, `user`, `password` | Database connection credentials |

### Database Schema

| Column | Type | Description |
|--|--|--|
| `id` | SERIAL PRIMARY KEY | Unique identifier |
| `timestamp` | TIMESTAMP | Auto-generated |
| `source` | TEXT | Origin of the memory |
| `content` | TEXT | Memory content |
| `embedding` | vector(1536) | OpenAI embedding vector |
| `metadata` | JSONB | Additional data |

### Features

- **Hybrid Storage**: Combines persistent logging with vector search
- **Vector Search**: Uses Postgres `vector` extension for semantic similarity
- **Fallback**: Saves without vector if embedding fails
- **Context Retrieval**: Returns chronologically sorted short-term memory

---

## Fast Path Cache (Phase 3)

### Overview

The `FastPathCache` class manages the `browser_fast_path` table for caching browser automation tasks. Uses pgvector cosine similarity to bypass LLM inference for repeated tasks.

### Table Schema

```sql
CREATE TABLE browser_fast_path (
    id SERIAL PRIMARY KEY,
    task_hash UUID NOT NULL UNIQUE,
    task_intent TEXT NOT NULL,
    context_signature TEXT NOT NULL,
    element_tree_snapshot JSONB NOT NULL,
    playwright_script TEXT NOT NULL,
    execution_time_ms INTEGER DEFAULT 0,
    success_rate FLOAT DEFAULT 1.0,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    task_hash_embedding vector(1536)
);
```

### Fields

| Field | Type | Description |
|--|--|--|
| `task_hash` | UUID | Deterministic hash of task intent |
| `task_intent` | TEXT | Human-readable task description |
| `context_signature` | TEXT | SHA-256 hash of page context |
| `element_tree_snapshot` | JSONB | AOM element tree at time of caching |
| `playwright_script` | TEXT | Native Playwright script to execute |
| `execution_time_ms` | INTEGER | Actual execution time for metrics |
| `success_rate` | FLOAT | Task success rate (0.0-1.0) |
| `created_at` | TIMESTAMP | Cache entry creation time |
| `task_hash_embedding` | vector(1536) | pgvector embedding for similarity |

### Helper Functions

#### `compute_context_signature(url: str, title: str, visible_text: str) -> str`
Computes deterministic SHA-256 hash for page context.

#### `compute_task_hash(task_intent: str) -> str`
Computes deterministic UUID hash from task intent string.

#### `extract_visible_text(page_content: str, max_length: int = 500) -> str`
Extracts visible text from HTML for context signature.

### FastPathCache Methods

#### `lookup(task_intent: str, context_signature: str, similarity_threshold: float = 0.85, limit: int = 1) -> Optional[Dict]`
Look up cached task by intent and context signature.

**Algorithm:**
1. Compute task hash from `task_intent` using SHA-256
2. Query pgvector with `context_signature` for cosine similarity > 0.85
3. Return cached `playwright_script` for millisecond execution

#### `write_back(task_hash: str, task_intent: str, context_signature: str, element_tree_snapshot: Dict, playwright_script: str, success_rate: float = 1.0) -> bool`
Write new cached task to database.

**Fields written:**
- `task_hash`: UUID hash of task intent
- `task_intent`: Human-readable description
- `context_signature`: SHA-256 hash of page context
- `element_tree_snapshot`: AOM snapshot JSON
- `playwright_script`: Compiled Playwright macro
- `success_rate`: Task reliability score

#### `record_hit(task_hash: str, execution_time_ms: int) -> None`
Record a cache hit for metrics.

#### `invalidate_old_cache(days: int = 30) -> int`
Invalidate cache entries older than specified days. Default: 30-day threshold.

**Usage:**
- Weekly cleanup job
- Removes stale cached tasks
- Returns count of invalidated entries

#### `get_metrics() -> Dict[str, Any]`
Get cache performance metrics (total tasks, avg execution time, success rate, age distribution).

---

## Entity-Relationship Knowledge Graph

### Overview

The Graph Memory System implements a graph database on top of PostgreSQL using `graph_nodes` and `graph_edges` tables. This enables Cobalt to store and query entities (nodes) and their relationships (edges) for knowledge graph construction and GraphRAG operations.

### Database Schema

#### `graph_nodes` Table

| Column | Type | Description |
|--|--|--|
| `id` | UUID PRIMARY KEY | Unique identifier (gen_random_uuid()) |
| `entity_type` | VARCHAR(255) NOT NULL | Entity category (e.g., 'Ticker', 'Strategy', 'Material') |
| `name` | VARCHAR(255) NOT NULL | Unique entity name (e.g., 'TSLA', 'Morning Gapper') |
| `properties` | JSONB | Additional metadata as JSON object |
| `created_at` | TIMESTAMP | Node creation timestamp |
| `updated_at` | TIMESTAMP | Last update timestamp |

**Unique Constraint:** `(entity_type, name)` ensures no duplicate entities

**Indexes:**
- `idx_graph_nodes_entity_type_name` on `(entity_type, name)`

#### `graph_edges` Table

| Column | Type | Description |
|--|--|--|
| `id` | UUID PRIMARY KEY | Unique identifier (gen_random_uuid()) |
| `source_id` | UUID NOT NULL | Reference to source node (FK with ON DELETE CASCADE) |
| `target_id` | UUID NOT NULL | Reference to target node (FK with ON DELETE CASCADE) |
| `relationship` | VARCHAR(255) NOT NULL | Relationship type (e.g., 'TRIGGERED_STRATEGY', 'IS_USED_IN') |
| `properties` | JSONB | Additional edge metadata as JSON object |
| `created_at` | TIMESTAMP | Edge creation timestamp |

**Unique Constraint:** `(source_id, target_id, relationship)` prevents duplicate edges

**Indexes:**
- `idx_graph_edges_source` on `source_id`
- `idx_graph_edges_target` on `target_id`

### CRUD Methods

#### `upsert_node(entity_type: str, name: str, properties: Dict = None) -> str`

Insert or update a graph node.

**Parameters:**
- `entity_type`: Entity category (e.g., 'Ticker', 'Material', 'Strategy')
- `name`: Unique entity name
- `properties`: Optional JSONB properties dictionary

**Returns:** Node UUID as string

**Workflow:**
1. Query for existing node by `(entity_type, name)`
2. If exists: update `properties` and `updated_at`
3. If not: insert new node with generated UUID

#### `upsert_edge(source_id: str, target_id: str, relationship: str, properties: Dict = None) -> str`

Insert or update a graph edge.

**Parameters:**
- `source_id`: UUID of source node
- `target_id`: UUID of target node
- `relationship`: Relationship type description
- `properties`: Optional JSONB properties dictionary

**Returns:** Edge UUID as string

**Workflow:**
1. Query for existing edge by `(source_id, target_id, relationship)`
2. If exists: update `properties` and `created_at`
3. If not: insert new edge with generated UUID

#### `get_node(entity_type: str, name: str) -> Optional[Dict]`

Retrieve a node by entity type and name.

**Parameters:**
- `entity_type`: Entity category
- `name`: Unique entity name

**Returns:** Dictionary with node data or None if not found

#### `get_edges(node_id: str, direction: str = 'both') -> List[Dict]`

Retrieve edges connected to a node.

**Parameters:**
- `node_id`: UUID of the node
- `direction`: 'out' (outgoing/source), 'in' (incoming/target), 'both'

**Returns:** List of edge dictionaries with properties

**Direction Options:**
- `out`: Edges where node is source (`source_id = node_id`)
- `in`: Edges where node is target (`target_id = node_id`)
- `both`: All edges connected to node

### Usage Examples

```python
from cobalt_agent.memory.postgres import PostgresMemory

postgres = PostgresMemory()

# Upsert a node (Ticker)
node_id = postgres.upsert_node(
    entity_type="Ticker",
    name="TSLA",
    properties={"price": 175.50, "sector": "Auto"}
)

# Upsert another node (Strategy)
strategy_id = postgres.upsert_node(
    entity_type="Strategy",
    name="Morning Gapper",
    properties={"score_threshold": 80}
)

# Create an edge between them
edge_id = postgres.upsert_edge(
    source_id=node_id,
    target_id=strategy_id,
    relationship="TRIGGERED_STRATEGY",
    properties={"confidence": 0.95}
)

# Get edges from the ticker node
ticker_edges = postgres.get_edges(node_id, direction="out")

# Get a specific node
ticker = postgres.get_node("Ticker", "TSLA")
```

### Graph Integration with Extractor

The Universal Extractor (`src/cobalt_agent/tools/extractor.py`) automatically:
1. Parses LLM-extracted nodes and edges into Pydantic schemas
2. Calls `upsert_node()` and `upsert_edge()` for persistence
3. Computes deltas against existing graph state
4. Triggers alerts only when new edges are detected

### AST-Based Knowledge Ingestion

#### Overview

The `dev_utils/ingest_knowledge.py` utility implements programmatic knowledge graph ingestion via the `ingest_ast_graph()` function. This approach uses Python's built-in `ast` module to parse source files and extract structural relationships without LLM overhead.

#### How It Works

The AST ingestion pipeline extracts two relationship types directly from Python source code:

1. **CONTAINS Relationships**: Maps classes and top-level functions as nodes
   - Class nodes: Entity type `Class`, name is the class identifier
   - Function nodes: Entity type `Function`, name is the function identifier (top-level only)

2. **IMPORTS Relationships**: Maps import dependencies between modules
   - Source: The importing module (as a `Module` node)
   - Target: The imported module or class
   - Relationship type: `IMPORTS`

#### Workflow

```python
def ingest_ast_graph(file_path: str) -> None
```

**Steps:**
1. Read and parse Python source file using `ast.parse()`
2. Traverse AST to identify `ClassDef` and top-level `FunctionDef` nodes
3. For each class/function, create a node with entity type and name
4. Traverse `Import` and `ImportFrom` nodes to create IMPORTS edges
5. Batch insert all nodes and edges via `upsert_node()` and `upsert_edge()`

#### Node Types

| Entity Type | Description | Example Name |
|--|--|--|
| `Module` | Python source file | `src.cobalt_agent.core.orchestrator` |
| `Class` | Class definition | `Orchestrator`, `StateMachine` |
| `Function` | Top-level function | `main()`, `initialize()` |

#### Edge Types

| Relationship | Source | Target | Description |
|--|--|--|--|
| `IMPORTS` | Module node | Module/Class node | Import dependency |
| `CONTAINS` | Module/Class node | Function/Class node | Structural containment |

#### Usage

```bash
# Ingest a single file
python dev_utils/ingest_knowledge.py src/cobalt_agent/core/orchestrator.py

# Ingest entire project (recursive)
python dev_utils/ingest_knowledge.py --recursive src/cobalt_agent/
```

#### Features

- **Zero LLM Dependency**: Pure AST parsing, no embedding generation
- **Deterministic Output**: Same source always produces same graph structure
- **Fast Processing**: Sub-second parsing for typical modules
- **Structural Accuracy**: Captures exact code relationships from AST

### Features

- **Hybrid Storage:** Graph entities stored as JSONB with vector embedding support
- **Cascade Delete:** `ON DELETE CASCADE` removes orphan edges when nodes are deleted
- **Idempotent Operations:** `upsert_*` methods prevent duplicate entities
- **Delta Detection:** compare extracted state against database for change tracking

---

## Graph Memory Persistence Fix

### Overview

The **Graph Memory Persistence Fix** ensures that `graph_nodes` and `graph_edges` tables are safely initialized on system boot **without wiping existing vector data**. This critical fix prevents accidental data loss during application restarts and ensures stable graph state across sessions.

### The Problem (Resolved)

Previously, boot initialization routines would unconditionally recreate graph tables, resulting in:
- **Complete loss of all graph nodes and edges** on every restart
- **Loss of vector embeddings** stored in related memory tables
- **Broken knowledge graph continuity** requiring manual re-extraction

### The Solution

The initialization process now follows a **safe, non-destructive pattern**:

```python
def _initialize_graph_tables(self) -> None:
    """
    Safely initialize graph tables without wiping existing data.
    
    Uses CREATE TABLE IF NOT EXISTS to ensure tables exist
    without dropping or truncating existing data.
    """
    with self.cursor() as cur:
        # Create graph_nodes table if it doesn't exist
        cur.execute("""
            CREATE TABLE IF NOT EXISTS graph_nodes (
                id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
                entity_type VARCHAR(255) NOT NULL,
                name VARCHAR(255) NOT NULL,
                properties JSONB DEFAULT '{}',
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                UNIQUE (entity_type, name)
            )
        """)
        
        # Create graph_edges table if it doesn't exist
        cur.execute("""
            CREATE TABLE IF NOT EXISTS graph_edges (
                id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
                source_id UUID NOT NULL REFERENCES graph_nodes(id) ON DELETE CASCADE,
                target_id UUID NOT NULL REFERENCES graph_nodes(id) ON DELETE CASCADE,
                relationship VARCHAR(255) NOT NULL,
                properties JSONB DEFAULT '{}',
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                UNIQUE (source_id, target_id, relationship)
            )
        """)
        
        # Create indexes if they don't exist
        cur.execute("""
            CREATE INDEX IF NOT EXISTS idx_graph_nodes_entity_type_name
            ON graph_nodes (entity_type, name)
        """)
        
        cur.execute("""
            CREATE INDEX IF NOT EXISTS idx_graph_edges_source
            ON graph_edges (source_id)
        """)
        
        cur.execute("""
            CREATE INDEX IF NOT EXISTS idx_graph_edges_target
            ON graph_edges (target_id)
        """)
```

### Key Safety Mechanisms

| Mechanism | Purpose | Impact |
|-----------|---------|--------|
| `CREATE TABLE IF NOT EXISTS` | Prevents table recreation | Existing data preserved |
| `CREATE INDEX IF NOT EXISTS` | Prevents index recreation | No duplicate index errors |
| **No `DROP TABLE`** | Eliminates destructive operations | Zero data loss on boot |
| **No `TRUNCATE`** | Preserves all rows | Graph state persists across restarts |

### Boot Sequence (Safe Initialization)

```
1. PostgresMemory.__init__() called
   ↓
2. Establish database connection
   ↓
3. _initialize_graph_tables() called
   ↓
4. CREATE TABLE IF NOT EXISTS graph_nodes
   → Table exists: NO-OP, data preserved
   → Table missing: Created fresh (first boot only)
   ↓
5. CREATE TABLE IF NOT EXISTS graph_edges
   → Table exists: NO-OP, data preserved
   → Table missing: Created fresh (first boot only)
   ↓
6. CREATE INDEX IF NOT EXISTS (all indexes)
   → Index exists: NO-OP
   → Index missing: Created
   ↓
7. Ready for graph operations (existing data intact)
```

### Verification

To verify the fix is working:

```python
from cobalt_agent.memory.postgres import PostgresMemory

# Add some data
postgres = PostgresMemory()
node_id = postgres.upsert_node("Ticker", "TSLA", {"price": 175.50})

# Restart application (create new instance)
postgres = PostgresMemory()

# Verify data persists
ticker = postgres.get_node("Ticker", "TSLA")
assert ticker is not None  # ✅ Data preserved across restarts
```

### Related Tables

The following tables are **NOT affected** by initialization and remain untouched:
- `memory_logs` - Core memory storage with vector embeddings
- `browser_fast_path` - Browser automation cache
- All other application tables

### Migration Notes

For systems affected by the previous bug:
1. No automatic recovery is possible for lost data
2. Re-run graph extraction tools to rebuild knowledge graph
3. After this fix, all future restarts preserve data

