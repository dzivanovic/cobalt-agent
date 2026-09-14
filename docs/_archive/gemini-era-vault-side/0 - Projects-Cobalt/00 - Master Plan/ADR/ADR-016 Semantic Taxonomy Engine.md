# ADR-016: Semantic Taxonomy Engine

## Status
Active

## Context
The original semantic tagging implementation processed instruments sequentially (1-by-1), passing 150+ Finviz columns to the local LLM. This architecture produced three critical failures:

1. **KV Cache Fragmentation**: Sequential processing caused memory leaks and context pollution across LLM calls
2. **Token Bloat & OOM Crashes**: 145+ financial columns per ticker exceeded local VRAM capacity, causing LM Studio to crash
3. **Hallucinated Taxonomy**: Without a controlled vocabulary, the LLM generated arbitrary thematic tags (e.g., "Short Squeezes", "Pump and Dumps") that did not reflect actual business narratives

Additionally, the 5-minute cron window for batch tagging was consistently missed due to per-ticker API latency.

## Decision

### 1. Data as Code: Obsidian → Postgres Sync
The source of truth for the taxonomy will be a human-readable Markdown table (`Master_Taxonomy.md`) maintained in Obsidian. This file will be synced to Postgres via a dedicated sync job that:

- Parses the Markdown table into structured taxonomy data
- Validates theme definitions against schema constraints
- Populates the `themes` and `instrument_themes` tables for runtime access

**Rationale**: Obsidian provides a git-friendly, human-editable interface for taxonomy management. The Markdown format is trivial to parse and version-control, eliminating the need for a dedicated admin UI while maintaining auditability.

### 2. Batch Tagging: 20-Ticker Prompt Batching
The SemanticTagger will process untagged instruments in batches of 20 rather than sequentially. Each batch request:

- Groups 20 instruments into a single LLM prompt
- Reduces total API calls by 95% (from N calls to N/20)
- Ensures completion within the 5-minute cron window
- Protects Apple Silicon memory from aggressive purges during long-running operations

**Rationale**: Batching amortizes the fixed overhead of LLM initialization and network latency. A 20-instrument batch fits within typical context window limits while maximizing throughput.

### 3. Controlled Vocabulary: Lean JSON Schema
The LLM prompt will receive only four fields per instrument instead of 145+ columns:

| Field | Type | Description |
|-------|------|-------------|
| `ticker` | string | Exchange symbol (e.g., "AAPL") |
| `name` | string | Company full name |
| `sector` | string | Finviz sector classification |
| `industry` | string | Finviz industry classification |

The LLM is constrained to select themes **only** from the active taxonomy loaded from Postgres. No free-form tag generation is permitted.

**Rationale**: Reducing input columns from 145+ to 4 eliminates token bloat while preserving semantic context. The controlled vocabulary prevents hallucination of non-existent themes and ensures consistent tagging across all instruments.

## Consequences
- **Positive**: Token usage reduced by ~97% (from 150+ columns to 4 fields)
- **Positive**: Batch processing reduces API calls by 95%, meeting cron timing constraints
- **Positive**: Controlled vocabulary eliminates hallucinated themes and ensures taxonomy consistency
- **Positive**: Obsidian-based taxonomy enables non-technical stakeholders to review and edit themes
- **Negative**: Requires maintaining a sync pipeline between Obsidian and Postgres
- **Negative**: Taxonomy changes require manual sync job execution (not real-time)
- **Negative**: Batch processing introduces slight latency for the last instrument in each batch

## References
- [[ADR-015 5-Pillar Relational Schema]] - Database schema foundation
- [[PRD-013 Multidimensional Market Data Engine]] - Functional requirements for semantic tagging