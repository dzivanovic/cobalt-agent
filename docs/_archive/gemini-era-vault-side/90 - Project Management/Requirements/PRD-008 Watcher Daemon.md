---
title: "PRD-008: Watcher Daemon & GraphRAG"
status: Approved
priority: P1
module: [Requirements, Architecture, Data]
phase: 4
complexity: L
tags: [cobalt, prd, requirements, watcher, graphrag, apscheduler, mattermost]
created: 2026-02-28
---

# PRD-008: Watcher Daemon & GraphRAG

## 1. Executive Summary
**The Vision:** Transform Cobalt from a reactive agent into a proactive watcher that continuously monitors external data sources and builds a living knowledge graph of entities and relationships.
**The Problem:** Current RAG stores documents as isolated vectors, missing critical relationships. There is no automated mechanism to discover new entities or detect when existing entities change.
**The Solution:** Implement a Watcher Daemon using `APScheduler` to periodically scrape指定 data sources, extract entities and relationships into a Postgres graph schema (`nodes` and `edges` tables), compare current state against previous state with a Delta Engine, and trigger Mattermost notifications when significant changes occur.

## 2. User Stories

### Story A: Entity Discovery
**As a** Researcher,
**I want** Cobalt to automatically discover new companies, people, and financial instruments from monitored websites,
**So that** my knowledge graph stays current without manual intervention.

### Story B: Relationship Mapping
**As a** Analyst,
**I want** Cobalt to identify and store relationships between entities (e.g., "Company A owns Company B", "Person X sits on Board of Company Y"),
**So that** I can perform relationship-based queries that reveal hidden connections.

### Story C: Change Detection
**As a** Chief of Staff,
**I want** Cobalt to notify me via Mattermost when a monitored entity's key attributes change (e.g., new CEO, changed financial figures),
**So that** I can respond to important updates in real-time.

### Story D: Dynamic Scheduling
**As a** System Operator,
**I want** the ReAct loop to add/remove polling intervals for specific sources at runtime,
**So that** I can prioritize certain sources during critical periods without restarting the daemon.

## 3. Core Requirements

### 3.1 Postgres Graph Schema (Phase 1)
1. **Nodes Table**:
   - `id` (UUID, primary key)
   - `type` (VARCHAR: 'company', 'person', 'instrument', 'event', 'other')
   - `name` (TEXT)
   - `source_url` (TEXT)
   - `created_at` (TIMESTAMP)
   - `updated_at` (TIMESTAMP)
   - `metadata` (JSONB)

2. **Edges Table**:
   - `id` (UUID, primary key)
   - `from_node_id` (UUID, foreign key to nodes)
   - `to_node_id` (UUID, foreign key to nodes)
   - `relationship_type` (VARCHAR: 'owns', 'employs', 'boards', 'associates_with', 'related_to')
   - `weight` (FLOAT)
   - `created_at` (TIMESTAMP)
   - `source_url` (TEXT)

3. **Indexes**:
   - Bitmap index on `nodes.type`
   - B-tree index on `edges.from_node_id` and `edges.to_node_id`
   -GIN index on `nodes.metadata` and `edges.metadata`

### 3.2 Universal Extractor (Phase 2)
1. **Input**: AOM JSON output from the Agentic Browser Loop, containing the compressed element tree
2. **LLM Prompt**: A structured prompt that instructs the LLM to extract entities (nodes) and their relationships (edges) from the AOM content
3. **Output Schema**: Pydantic models for `Node` and `Edge` with fields matching the database schema
4. **Validation**: Reject outputs where node IDs are missing, types are unknown, or edge relationships don't match allowed values

### 3.3 Delta Engine (Phase 2)
1. **State Storage**: Store the full JSON output of each extraction cycle in a `extraction_history` table
2. **Comparison Logic**: Compare current JSON output against the most recent stored state:
   - New nodes (present in current, absent in previous)
   - Deleted nodes (present in previous, absent in current)
   - Modified attributes (same node, different metadata values)
   - New edges
   - Deleted edges
3. **Delta Output**: Return a summary of all deltas with node/edge IDs and change types

### 3.4 Dynamic APScheduler Integration (Phase 3)
1. **Job Management**: The Watcher Daemon will initialize with `APScheduler` and load existing polling intervals from config
2. **ReAct Integration**: Implement a Mattermost command or tool that allows the ReAct loop to:
   - List active polling jobs
   - Add a new polling job with specified URL, interval, and extraction profile
   - Remove a polling job by ID
3. **Persistence**: Store job configurations in a `watcher_jobs` table for recovery after restart

### 3.5 Event Bus Interrupts (Phase 3)
1. **Trigger**: When the Delta Engine detects changes (new node, new edge, modified attributes), trigger an interrupt
2. **Mattermost Notification**: Send a formatted message to the configured Mattermost channel with:
   - Change summary (e.g., "2 new entities, 3 new relationships")
   - List of new/changed nodes with type and name
   - List of new/changed edges with relationship type
   - Link to the source URL
3. **Rate Limiting**: Implement a 5-minute cooldown per source URL to prevent notification spam

## 4. Performance Requirements
- Delta comparison must complete in <100ms for extraction outputs up to 10KB JSON
- New polling jobs must be active within 1 second of the ReAct command
- Mattermost notifications must be delivered within 10 seconds of detection

## 5. Security Constraints
- All source URLs must be validated against a `WATCHER_WHITELIST` before scheduling
- Node metadata must be sanitized to remove any executable content (scripts, HTML event handlers)
- The Watcher Daemon runs with read-only database permissions (INSERT on nodes/edges/history/jobs, no SELECT on secrets)

## 6. Failure Modes
| Mode | Response |
|------|----------|
| AOM extraction fails | Log error, retry once, then mark job as failed in `watcher_jobs` table |
| Delta comparison timeout | Fall back to storing current state as new baseline |
| Mattermost notification fails | Retry 3 times, then log and continue |
| Database connection lost | Reconnect with exponential backoff, pause all polling until recovered |

## 7. Configuration
```yaml
watcher:
  postgres_connection: ${WATCHER_DB_URL}
  mattermost_webhook: ${WATCHER_MM_WEBHOOK}
  whitelist: ${WATCHER_WHITELIST}  # YAML list of allowed domains
  default_interval: 3600  # seconds
  rate_limit_cooldown: 300  # seconds
  extraction_profile: "financial"  # or "general"