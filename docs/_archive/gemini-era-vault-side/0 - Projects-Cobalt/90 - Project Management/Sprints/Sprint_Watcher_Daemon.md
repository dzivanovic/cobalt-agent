---
title: "Sprint Watcher Daemon: Postgres Graph, Universal Extractor & Delta Engine"
date: 2026-03-01
sprint: 3
status: Done
tags: [cobalt, sprint, watcher, graphrag, apscheduler, mattermost]
---

# Sprint Watcher Daemon: Postgres Graph, Universal Extractor & Delta Engine

## Overview

This sprint implements the Watcher Daemon architecture, extending the existing Postgres database with graph tables (`nodes` and `edges`) and building a system that can automatically extract entities and relationships from web content, detect changes over time, and trigger real-time notifications.

## Sprint Goals

1. Create Postgres graph schema (`nodes` and `edges` tables) with proper indexing
2. Build a universal LLM-based extractor that parses AOM output into graph entities and relationships
3. Implement a Delta Engine that compares JSON snapshots to detect changes
4. Integrate APScheduler for dynamic polling and Mattermost for change notifications

## Phase 1: Postgres Graph Schema

### Objective
Create the underlying graph data model in Postgres to store entities and their relationships.

### Deliverables

#### 1.1 Migration Script
- **File:** `src/cobalt_agent/migrations/003_graph_schema.sql` (new)
- **Tables:**
  ```sql
  CREATE TABLE nodes (
      id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
      type VARCHAR(50) NOT NULL,
      name TEXT NOT NULL,
      source_url TEXT,
      created_at TIMESTAMP DEFAULT NOW(),
      updated_at TIMESTAMP DEFAULT NOW(),
      metadata JSONB
  );

  CREATE TABLE edges (
      id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
      from_node_id UUID NOT NULL REFERENCES nodes(id),
      to_node_id UUID NOT NULL REFERENCES nodes(id),
      relationship_type VARCHAR(50) NOT NULL,
      weight FLOAT DEFAULT 1.0,
      created_at TIMESTAMP DEFAULT NOW(),
      source_url TEXT
  );
  ```

#### 1.2 Indexes
- **File:** `src/cobalt_agent/migrations/003_graph_schema.sql` (new)
- **Indexes:**
  - Bitmap index on `nodes.type`
  - B-tree indexes on `edges.from_node_id` and `edges.to_node_id`
  - GIN index on `nodes.metadata` and `edges.metadata`

#### 1.3 Python Models
- **File:** `src/cobalt_agent/models/graph.py` (new)
- **Models:** Pydantic models for `Node` and `Edge` matching the database schema

### Testing
- [ ] Run migration on test database
- [ ] Verify indexes are created
- [ ] Insert sample node and edge data
- [ ] Query with WHERE clauses on type and relationship_type

---

## Phase 2: Universal Extractor & Delta Engine

### Objective
Build the core extraction pipeline and change detection system.

### Deliverables

#### 2.1 Universal Extractor
- **File:** `src/cobalt_agent/extractor/universal.py` (new)
- **Functionality:**
  - Accept AOM JSON output from browser tool
  - Construct prompt that instructs LLM to extract entities and relationships
  - Parse LLM response into Pydantic `Node` and `Edge` models
  - Validate outputs against schema constraints

#### 2.2 Extraction Storage
- **File:** `src/cobalt_agent/memory/postgres.py` (update)
- **Table:** `extraction_history`
  ```sql
  CREATE TABLE extraction_history (
      id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
      source_url TEXT NOT NULL,
      timestamp TIMESTAMP DEFAULT NOW(),
      full_output JSONB NOT NULL
  );
  ```

#### 2.3 Delta Engine
- **File:** `src/cobalt_agent/extractor/delta.py` (new)
- **Functionality:**
  - Query `extraction_history` for most recent snapshot of source URL
  - Compare JSON structure between current and previous
  - Identify: new nodes, deleted nodes, modified attributes, new edges, deleted edges
  - Return summary with counts and details

#### 2.4 Save Extracted Data
- **File:** `src/cobalt_agent/extractor/store.py` (new)
- **Functionality:**
  - Upsert nodes (update if exists by name+type, insert otherwise)
  - Insert edges
  - Store current extraction output in `extraction_history`

### Testing
- [ ] Extract from 5 sample web pages
- [ ] Verify nodes and edges are stored correctly
- [ ] Run delta comparison and verify change detection works
- [ ] Test with malformed AOM input (error handling)

---

## Phase 3: APScheduler Tool Integration & Event Bus Interrupts

### Objective
Enable dynamic scheduling and real-time notifications.

### Deliverables

#### 3.1 Watcher Daemon
- **File:** `src/cobalt_agent/services/watcher.py` (new)
- **Functionality:**
  - Initialize APScheduler
  - Load existing jobs from `watcher_jobs` table
  - Start polling for each configured source

#### 3.2 Watcher Jobs Table
- **File:** `src/cobalt_agent/migrations/003_graph_schema.sql` (update)
- **Table:**
  ```sql
  CREATE TABLE watcher_jobs (
      id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
      source_url TEXT NOT NULL UNIQUE,
      interval_seconds INTEGER NOT NULL,
      extraction_profile VARCHAR(50) DEFAULT 'financial',
      active BOOLEAN DEFAULT TRUE,
      created_at TIMESTAMP DEFAULT NOW()
  );
  ```

#### 3.3 ReAct Integration
- **File:** `src/cobalt_agent/tools/watcher.py` (new)
- **Commands:**
  - `watcher list`: Return active polling jobs
  - `watcher add [url] [interval_seconds] [profile]`: Add new job
  - `watcher remove [job_id]`: Remove job

#### 3.4 Event Bus Interrupts
- **File:** `src/cobalt_agent/interrupts/delta.py` (new)
- **Functionality:**
  - Trigger when Delta Engine detects changes
  - Format notification message with change summary
  - Send to Mattermost webhook
  - Implement rate limiting (cooldown per source)

#### 3.5 Scheduler Management
- **File:** `src/cobalt_agent/services/scheduler.py` (update)
- **Add:** Methods to add/remove APScheduler jobs dynamically

### Testing
- [ ] Add/remove polling jobs via Mattermost command
- [ ] Verify jobs appear in `watcher_jobs` table
- [ ] Trigger a delta and verify Mattermost notification
- [ ] Test rate limiting with repeated deltas

---

## Sprint Metrics

| Metric | Target |
|--------|--------|
| Sprint Duration | 2026-03-01 to 2026-03-08 |
| Files Modified | 4+ |
| New Files Created | 7+ |
| Graph Tables Created | 3 (nodes, edges, extraction_history) |
| Delta Detection Accuracy | >90% |
| Notification Latency | <10 seconds |

## Documentation Updates (To Complete)

- [x] `docs/0 - Projects/Cobalt/00 - Master Plan/Developer Docs/postgres.md` - Entity-Relationship Knowledge Graph section added
- [x] `docs/0 - Projects/Cobalt/00 - Master Plan/Developer Docs/browser.md` - Dual-Path Routing section added
- [x] `docs/0 - Projects/Cobalt/00 - Master Plan/Developer Docs/extractor.md` - Universal Extractor documentation created
- [x] `docs/0 - Projects/Cobalt/00 - Master Plan/Developer Docs/daemon.md` - Watcher Daemon documentation created
- [x] `docs/0 - Projects/Cobalt/00 - Master Plan/Developer Docs/scheduler.md` - Update with Watcher integration

## Success Criteria

1. Postgres graph schema is deployed and all indexes are functional
2. Universal Extractor successfully converts AOM output to nodes/edges with >90% accuracy
3. Delta Engine correctly identifies new/changed/deleted entities
4. APScheduler jobs can be added/removed at runtime via Mattermost command
5. Mattermost notifications are delivered within 10 seconds of change detection