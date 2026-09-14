# ADR-013: GraphRAG and Watcher Daemon

## Status
Accepted

## Context
The current RAG system stores documents in pgvector for semantic similarity search. However, this approach treats each document as an isolated vector, missing the relationships between entities (companies, people, financial instruments, events) that are critical for accurate reasoning and pattern detection. Additionally, there is no automated mechanism to continuously monitor external data sources for new information.

## Decision
1. **Postgres Graph Schema**: Instead of spinning up a dedicated graph database (e.g., Neo4j), we will extend our existing Postgres database with two new tables:
   - `nodes`: Stores entities with attributes (id, type, name, source_url, created_at, updated_at, metadata JSONB)
   - `edges`: Stores relationships between nodes (id, from_node_id, to_node_id, relationship_type, weight, created_at)

2. **Universal Extractor**: A unified LLM-based pipeline that parses the Agentic Browser Loop's AOM output to extract nodes and edges, converting free-form web content into structured graph data.

3. **Delta Engine**: A comparison engine that stores the JSON output of each extraction cycle and compares it against previous states to detect new entities, relationship changes, and attribute updates.

4. **APScheduler Integration**: The Watcher Daemon will use `APScheduler` as its scheduling engine to handle asynchronous polling intervals dynamically. The ReAct loop will be able to add/remove polling intervals at runtime via the scheduler's job management API.

5. **Event Bus Interrupts**: When the Delta Engine detects a change (new node, new edge, attribute update), it will trigger an event bus interrupt that sends a Mattermost notification with the delta summary.

## Consequences
- **Positive**: GraphRAG enables relationship-based queries that are impossible with vector-only storage (e.g., "Find all companies connected to this person via shared board membership")
- **Positive**: Using Postgres keeps the infrastructure simpler (one less service to manage, backup, and monitor)
- **Positive**: APScheduler allows dynamic scheduling without restarting the daemon
- **Positive**: Mattermost interrupts provide real-time awareness of significant changes
- **Negative**: The graph schema requires careful indexing strategy to maintain query performance
- **Negative**: Delta detection requires storing full JSON snapshots; storage costs will grow with extraction frequency