---
title: "Sprint 06: Data Engine"
status: Planned
priority: P0
module: Core
start_date: 2026-03-25
end_date: 2026-04-01
tags: [cobalt, sprint, data-engine]
---

# Sprint 06: Data Engine

## Sprint Goal
Build the foundational 5-Pillar Relational Schema that enables multi-asset trading, semantic news deduplication, and psychological performance tracking.

## Sprint Backlog

### Task 1: Initialize 12-Table Schema
**ID:** `S06-T01`  
**Priority:** P0  
**Estimate:** 2h

Create `schema.sql` with all 12 tables and required indexes:
- `instruments` (with active_themes JSONB)
- `themes` (hierarchical taxonomy)
- `key_levels` (support/resistance)
- `daily_in_play` (in-play ticker snapshot)
- `market_snapshots` (real-time price/volume)
- `news_events` (with vector embeddings + sources JSONB)
- `news_mentions` (news-to-instrument linking)
- `system_alerts` (MFE/MAE tracking)
- `trading_accounts` (portfolio state)
- `trades` (with mistake_tags JSONB + tilt_score)
- `order_fills` (granular fill history)

**Acceptance Criteria:**
- [ ] Schema.sql executes without errors on PostgreSQL 15+
- [ ] pgvector extension enabled with 768-dimension embeddings
- [ ] GIN indexes on all JSONB fields
- [ ] Foreign key constraints enforce referential integrity
- [ ] Script uses psycopg to auto-initialize on first run

**Dependencies:** None  
**Blocks:** All other sprint tasks

---

### Task 2: Implement Finviz API Market Snapshot Ingestion Loop
**ID:** `S06-T02`  
**Priority:** P0  
**Estimate:** 3h

Build continuous ingestion loop that fetches market data via Finviz Quote API:
- Poll configured watchlist every N seconds
- Normalize response into `market_snapshots` table
- Auto-create missing instruments in `instruments` table
- Track historical snapshots for trend analysis

**Acceptance Criteria:**
- [ ] Ingestion loop runs continuously without memory leaks
- [ ] New instruments auto-created with correct asset_type
- [ ] Snapshot latency < 5 seconds from source
- [ ] Graceful handling of API rate limits

**Dependencies:** S06-T01  
**Blocks:** News ingestion pipeline

---

### Task 3: Build LLM Semantic News Extractor (Taxonomy to Hash)
**ID:** `S06-T03`  
**Priority:** P1  
**Estimate:** 4h

Create LLM-powered news extraction pipeline:
- Parse raw news articles from multiple sources (RSS, Twitter, NewsAPI)
- Extract structured taxonomy: {headline, summary, entities, themes}
- Generate deterministic hash for deduplication
- Create 768-dimension embedding via pgvector

**Acceptance Criteria:**
- [ ] Extractor produces consistent taxonomy_hash for identical content
- [ ] Embeddings stored in `news_events.embedding` column
- [ ] Sources tracked in JSONB for attribution
- [ ] Integration with [[PRD-012 The Recon Scout]] news feed

**Dependencies:** S06-T01  
**Blocks:** Deduplication engine

---

### Task 4: Build the Cobalt Orchestrator Deduplication Engine
**ID:** `S06-T04`  
**Priority:** P1  
**Estimate:** 3h

Implement semantic deduplication using vector similarity:
- Compare new news embeddings against existing entries
- Cluster similar articles (threshold: cosine_similarity > 0.7)
- Link related news via `news_mentions` table
- Flag unique vs. duplicate content

**Acceptance Criteria:**
- [ ] Duplicate detection accuracy > 80%
- [ ] Related instruments auto-linked via news_mentions
- [ ] Sentiment scoring per instrument mention
- [ ] Performance: < 100ms per deduplication check

**Dependencies:** S06-T03  
**Blocks:** Playbook generation

---

### Task 5: Construct the Obsidian Daily Markdown Sync Job
**ID:** `S06-T05`  
**Priority:** P1  
**Estimate:** 3h

Build post-market sync job that generates Obsidian Playbook entries:
- Query `trades` + `system_alerts` for daily performance
- Generate markdown with [[WikiLinks]] to instruments and themes
- Include MFE/MAE metrics and R-multiple analysis
- Tag psychological mistakes from `mistake_tags` JSONB

**Acceptance Criteria:**
- [ ] Daily setup files generated in `docs/0 - Projects/Cobalt/Playbook/Daily/`
- [ ] All trades auto-linked to [[instruments]] and [[themes]]
- [ ] MFE/MAE summary included in each entry
- [ ] Sync completes within 5 minutes of market close

**Dependencies:** S06-T01, S06-T04  
**Blocks:** None

---

## Sprint Metrics

| Metric | Target |
|--------|--------|
| Schema Tables | 12 complete |
| News Deduplication Rate | > 80% |
| Snapshot Latency | < 5 seconds |
| Playbook Coverage | 100% of trades |

## Integration Points
- [[PRD-013 Multidimensional Market Data Engine]] - Functional requirements
- [[ADR-015 5-Pillar Relational Schema]] - Technical specifications
- [[PRD-012 The Recon Scout]] - News feed source
- [[Sprint_05_The_Ion_Bridge]] - Obsidian sync foundation

## Definition of Done
- [ ] All tasks completed with acceptance criteria met
- [ ] Schema tested on production-like dataset (1000+ records)
- [ ] No critical bugs in ingestion pipeline
- [ ] Documentation updated in Obsidian vault