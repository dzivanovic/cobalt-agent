# PostgreSQL Memory Management

**File**: `src/cobalt_agent/memory/postgres.py`  
**Purpose**: Persistent memory storage with vector similarity search, graph knowledge mapping, HITL workflow support, and deterministic browser caching.  
**Last Updated**: 2026-04-08

---

## Overview

The `postgres.py` module serves as the "Hippocampus" of the Cobalt Agent. It implements a hybrid persistent memory layer using PostgreSQL with the `pgvector` extension. 

It is divided into two primary classes and several utility functions:
1. **Utility Functions**: Handle deterministic SHA-256 and UUID hashing for contexts and tasks.
2. **`FastPathCache`**: A dedicated class managing the browser task reuse pipeline.
3. **`PostgresMemory`**: The core memory adapter integrating all 5 database pillars (Vector Logs, Graph Nodes, Graph Edges, HITL Proposals, and Browser Cache).

---

## Architecture & Core Components

### Configuration Loading
Credentials are automatically loaded with a strict hierarchy (highest to lowest priority):
1. Environment variables (`POSTGRES_HOST`, `POSTGRES_DB`, `POSTGRES_USER`, `POSTGRES_PASSWORD`)
2. YAML configurations (`configs/*.yaml`)

### Connection Strategy
- Relies on `psycopg` with **autocommit mode** enabled.
- Utilizes a connection-per-operation pattern (`_get_conn()`). There are no persistent connections kept open; operations are stateless.

---

## Database Schema (The 5-Pillar Integration)

### Pillar 1: Memory Logs (`memory_logs`)
Core table for persistent, semantic memory storage.
- **Fields**: `id`, `timestamp`, `source`, `content`, `embedding vector(1536)`, `metadata JSONB`
- Uses `text-embedding-3-small` via LiteLLM to generate 1536-dimensional embeddings.

### Pillar 2: Graph Nodes (`graph_nodes`)
Entities for the GraphRAG knowledge base.
- **Fields**: `id UUID`, `entity_type`, `name`, `properties JSONB`, `created_at`, `updated_at`
- **Constraint**: Unique on `(entity_type, name)`.

### Pillar 3: Graph Edges (`graph_edges`)
Relationships connecting graph nodes.
- **Fields**: `id UUID`, `source_id`, `target_id`, `relationship`, `properties JSONB`
- **Constraint**: Unique on `(source_id, target_id, relationship)` with `ON DELETE CASCADE` for node cleanup.

### Pillar 4: HITL Proposals (`hitl_proposals`)
Tracks Human-in-the-Loop workflows and tool execution approvals.
- **Fields**: `id VARCHAR(50)`, `status`, `tool_name`, `tool_kwargs JSONB`
- Supported statuses: `'pending'`, `'approved'`, `'rejected'`.

### Pillar 5: Browser Fast Path (`browser_fast_path`)
Stores previously executed Playwright scripts to bypass redundant LLM visual processing.
- **Fields**: `id`, `task_hash UUID`, `task_intent`, `context_signature`, `element_tree_snapshot JSONB`, `playwright_script`, `execution_time_ms`, `success_rate`
- **Vector Index**: Includes `task_hash_embedding vector(1536)` with an `ivfflat` index (`lists=100`) for cosine similarity lookups.

---

## Class: `FastPathCache`

Dedicated manager for the browser automation fast-path pipeline.

### Core Methods
*   **`lookup(task_intent, context_signature, similarity_threshold=0.85)`**: Searches for a cached browser task. First attempts an exact match on `context_signature`. If found, validates intent via vector cosine similarity.
*   **`write_back(...)`**: Inserts or updates (`ON CONFLICT (task_hash) DO UPDATE`) a new cached task along with its embedding.
*   **`record_hit(task_hash, execution_time_ms)`**: Updates execution time and refreshes the `created_at` timestamp for cache hits.
*   **`invalidate_old_cache(days=30)`**: Deletes cache entries older than the specified threshold.
*   **`get_metrics()`**: Returns cache statistics, including total tasks, average execution time, success rate, and age distribution.

---

## Class: `PostgresMemory`

The core integration layer bridging Cobalt's brain with the database.

### Memory & Vector Operations
*   **`add_log(message, source, data)`**: Scrubs secrets, generates an embedding, and saves a memory. If embedding generation fails, falls back to saving text without vectors.
*   **`get_context(limit=10)`**: Retrieves recent memory logs, formatting them chronologically for LLM context injection.
*   **`search(query, limit=5)`**: Performs semantic search using the `<=>` (Cosine Distance) operator. Filters out noise by requiring a minimum similarity score of 0.3.

### GraphRAG Operations
*   **`upsert_node(entity_type, name, properties)`**: Creates or updates a knowledge graph entity.
*   **`get_node(entity_type, name)`**: Retrieves a specific node.
*   **`upsert_edge(source_id, target_id, relationship, properties)`**: Creates or updates a relationship link between two nodes.
*   **`get_edges(node_id, direction='both')`**: Retrieves incoming (`'in'`), outgoing (`'out'`), or all relationships for a given node.

### HITL (Human-in-the-Loop) Operations
*(Note: Method names use `_hilt_` while the DB schema uses `hitl_`)*
*   **`store_hilt_proposal(tool_name, tool_kwargs)`**: Creates a new proposal with an 8-character ID (matching Bouncer format) and sets status to `'pending'`.
*   **`get_hilt_proposal(task_id)`**: Retrieves a specific proposal by ID.
*   **`update_hilt_proposal_status(task_id, status)`**: Updates a proposal's status.

---

## Utility Functions

*   **`compute_context_signature(url, title, visible_text)`**: Generates a deterministic SHA-256 hash using the page URL, title, and text preview, concatenated with a null byte delimiter (`\x00`) to prevent collisions.
*   **`compute_task_hash(task_intent)`**: Converts a task intent into a deterministic Version-5-like UUID for DB storage and lookups.
*   **`extract_visible_text(page_content, max_length=500)`**: Uses `HTMLParser` to strip scripts and styles and extract raw visible text. Features a fallback RegEx stripper if parsing fails.

---

## Security & Resilience Features

### Zero-Trust Secret Scrubbing
The `_scrub_secrets()` method automatically intercepts all messages prior to database insertion or LLM API calls. 
- It attempts to unlock the `VaultManager` using `COBALT_MASTER_KEY`.
- It scans the vault and config files for API keys or credentials.
- Replaces any identified secrets with `[REDACTED_SECRET]`.

### Offline Vector Fallbacks
The system is built to survive in "Zero-Trust" local environments where API keys might be restricted. If the LiteLLM embedding call fails due to an `AuthenticationError` (e.g., missing OpenAI key), the `FastPathCache` seamlessly falls back to saving deterministic cache rows *without* embeddings, ensuring core functionality remains operational.