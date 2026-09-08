# ADR-011: The Vector Librarian (pgvector)

## Status
Accepted

## Context
The Sovereign Split-Brain architecture (ADR-007) requires the Architect to plan complex tasks. However, the Architect lacked a semantic understanding of the codebase and the user's Second Brain (Obsidian), forcing it to blindly guess file paths or rely on slow directory listings.

## Decision
We implemented a PostgreSQL-backed Vector Database using `pgvector`.
1. **Ingestion Engine**: Created `dev_utils/ingest_knowledge.py` to chunk and embed `.py`, `.yaml`, and `.md` files using `text-embedding-3-small`.
2. **Omni-Memory**: Leveraged the existing `PostgresMemory` class so that all project files, config playbooks, and historical chat logs reside in the same searchable vector space.
3. **The Librarian Tool**: Created `search_knowledge` to allow the Architect to semantically query the database during the planning phase.

## Consequences
- **Positive**: The Architect can now instantly locate exact files and context across the entire project and Obsidian vault.
- **Positive**: Eradicates path-guessing hallucinations.
- **Negative/Risk**: The vector database requires continuous updating to prevent stale data retrieval. Mitigation planned via automated background syncs.