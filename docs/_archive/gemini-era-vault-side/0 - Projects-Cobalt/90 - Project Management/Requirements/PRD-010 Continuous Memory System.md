# PRD-010: Continuous Memory System

**Status:** ✅ Implemented  
**Priority:** P0 - Critical Infrastructure  
**Author:** Cobalt Engineering Team  
**Date:** 2025-02-23  

---

## Executive Summary

Cobalt implements a **hybrid PostgreSQL memory system** with vector embeddings for semantic search. The Hippocampus provides persistent, queryable memory with pgvector integration for cosine similarity lookups and a Fast Path Cache for browser automation tasks.

---

## Technical Implementation

### Core Components

#### 1. PostgresMemory (Primary Storage)
**File:** `src/cobalt_agent/memory/postgres.py`

The main memory provider that handles persistent storage with vector embeddings.

**Key Features:**
- **Vector Embeddings**: 1536-dimensional embeddings using `text-embedding-3-small`
- **Cosine Similarity Search**: Native pgvector `<=>` operator for semantic search
- **Secret Scrubbing**: Automatic redaction of sensitive values before storage

```python
# Memory storage with automatic secret scrubbing
def add_log(self, message: str, source: str = "System", data: Dict = None):
    scrubbed_message = self._scrub_secrets(message)
    vector = self._generate_embedding(scrubbed_message)
    # Store scrubbed content with embedding
```

### Database Schema

#### memory_logs (Primary Table)
| Column | Type | Purpose |
|--------|------|---------|
| id | SERIAL | Primary key |
| timestamp | TIMESTAMP | When the memory was created |
| source | TEXT | Origin of the memory (e.g., "Assistant", "System") |
| content | TEXT | The actual memory content (scrubbed of secrets) |
| embedding | vector(1536) | Vector embedding for semantic search |
| metadata | JSONB | Additional context and properties |

#### graph_nodes (Knowledge Graph)
| Column | Type | Purpose |
|--------|------|---------|
| id | UUID | Entity identifier |
| entity_type | VARCHAR(255) | Type of entity (e.g., "Ticker", "Material") |
| name | VARCHAR(255) | Entity name |
| properties | JSONB | Additional entity data |

#### graph_edges (Relationships)
| Column | Type | Purpose |
|--------|------|---------|
| id | UUID | Edge identifier |
| source_id | UUID | Source node reference (FK) |
| target_id | UUID | Target node reference (FK) |
| relationship | VARCHAR(255) | Relationship type |

#### browser_fast_path (Cache)
| Column | Type | Purpose |
|--------|------|---------|
| id | SERIAL | Primary key |
| task_hash | UUID | Deterministic hash for lookup |
| task_intent | TEXT | Task description |
| context_signature | TEXT | SHA-256 hash for exact matching |
| element_tree_snapshot | JSONB | DOM snapshot |
| playwright_script | TEXT | Executable Playwright script |
| execution_time_ms | INTEGER | Performance metric |
| success_rate | FLOAT | Reliability tracking |
| task_hash_embedding | vector(1536) | Vector for similarity search |

### Fast Path Cache (Browser Optimization)

**Class:** `FastPathCache`

Provides specialized caching for browser automation tasks:

1. **Context Signature Hashing**: SHA-256 hash of URL + title + visible text
2. **Vector Similarity**: Cosine similarity on task embeddings
3. **Performance Metrics**: Tracks execution time and success rates

```python
# Cache lookup with similarity threshold
def lookup(self, task_intent: str, context_signature: str, 
           similarity_threshold: float = 0.85) -> Optional[Dict]:
    # First tries exact context signature match
    # Then falls back to vector similarity search
```

---

## Architecture Principles

### 1. Persistent Storage
- All memories persist across agent restarts via PostgreSQL
- Vector embeddings enable semantic search without external vector DB

### 2. Privacy First
- Secrets automatically scrubbed before storage via `_scrub_secrets()`
- Integration with VaultManager for secret detection

### 3. Graph-RAG Ready
- Entity-relationship graph supports knowledge graph patterns
- Nodes and edges can be queried for contextual retrieval

---

## API Reference

### Core Methods

```python
# Add a memory (with automatic embedding)
memory.add_log("User prefers dark mode", source="Preference")

# Semantic search (returns similar memories)
results = memory.search("appearance preferences", limit=5)

# Get recent context (short-term RAM)
context = memory.get_context(limit=10)

# Graph operations
node_id = memory.upsert_node("Preference", "dark_mode", {"value": True})
memory.upsert_edge(node_id, user_node_id, "HAS_PREFERENCE")

# HITL proposal storage
proposal_id = memory.store_hilt_proposal("delete_file", {"path": "secret.txt"})
```

### Graph Query Examples

```python
# Get all edges connected to a node
edges = memory.get_edges(node_id, direction='both')

# Get specific entity
entity = memory.get_node("Ticker", "NVDA")
```

---

## Integration Points

### Dependencies
- `psycopg` - PostgreSQL driver
- `pgvector` - Vector extension for Postgres
- `litellm` - Embedding generation

### Environment Configuration

Required environment variables (via `.env`):
```bash
POSTGRES_HOST=localhost
POSTGRES_PORT=5432
POSTGRES_DB=cobalt_memory
POSTGRES_USER=cobalt
POSTGRES_PASSWORD=your_secure_password
```

---

## Acceptance Criteria

- [x] PostgreSQL connection with autocommit enabled
- [x] Automatic table creation (memory_logs, graph_nodes, graph_edges, browser_fast_path)
- [x] Vector embeddings generated using LiteLLM
- [x] Semantic search with cosine similarity filtering
- [x] Secret scrubbing before storage
- [x] Graph node/edge CRUD operations
- [x] HITL proposal persistence
- [x] Fast Path Cache for browser automation

---

## Performance Characteristics

| Operation | Latency | Notes |
|-----------|---------|-------|
| Memory Write | ~50ms | Synchronous insert with embedding |
| Semantic Search | ~100ms | Includes embedding generation + vector search |
| Cache Lookup | <10ms | Exact signature match is O(1) |
| Graph Query | ~20ms | Indexed foreign key lookups |

---

## Future Enhancements

1. **Memory Compression**: Periodic summarization of old memories
2. **Contextual Retrieval**: RAG-style retrieval for LLM context injection
3. **Memory Expiration**: TTL-based cleanup of stale memories

---

## Related Documents

- [PRD-013: GraphRAG and Watcher Daemon](../ADR/ADR-013%20GraphRAG%20Watcher%20Daemon.md)
- [PRD-011: Vector Librarian](../ADR/ADR-011%20Vector%20Librarian.md)