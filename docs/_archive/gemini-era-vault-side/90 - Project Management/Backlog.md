---
status: In Progress
priority: P1 (High)
module: Ops
phase: 3 (Capabilities)
complexity: S
tags: [cobalt, planning, roadmap]
created: 2026-02-26
---
# Cobalt Product Backlog

## Completed (Phase 4 & 5)
* [x] **ADR-009: The Vector Librarian (pgvector)** - Implemented PostgreSQL-backed Vector Database with ingestion engine (`dev_utils/ingest_knowledge.py`), omni-memory integration, and `search_knowledge` tool for semantic queries.

## Completed (Phase 6)
* [x] **Refactor Orchestrator Abstraction:** Update `cortex.py` and `OrchestratorEngine` to handle multi-domain routing (Tactical, Ops, Intel) and spawn domain-specific Drones (Strategos, Scribe) instead of hardcoding the Engineering Forge.

## Completed (Phase 7)
* [x] **Phase 7: Continuous Memory & Automation** - Implemented scheduler service with cron-based Morning Briefing generation, automated vault management with AES-256 encryption, and robust orchestration state machine with Split-Brain architecture.

## Deferred / Future Infrastructure
* [ ] **Implement Syncthing over Tailscale for robust, bi-directional, air-gapped local vault sync.**
* [ ] **Implement v1beta routing in LLM class to natively support Google preview models.**
* [ ] **Live Market Data Feed Integration:** Select and integrate a structured API (e.g., Polygon, Alpaca) for the Tactical Drone.
* [ ] **Execution Broker API Integration:** Connect the HUD to a brokerage API to receive Cobalt's "Math Packages" for JIT execution.

## Strategic Pillars

### The Forge
Enable Cobalt to manage its own codebase, self-learn, self-heal, and write its own tools, eventually replacing external AI coding assistants.

### Top-Down Analysis Pipeline
Teach the agent to gather, filter, and analyze macro/micro market data, distilling it into actionable payloads for real-time monitoring and alerting.

### Strategy Redesign
Overhaul system identification and grading of market setups.

## High-Throughput Inference (Local Cluster)
* [ ] **[Epic] Async Parallel Fan-Out:** Refactor the `OrchestrationState` machine to support `asyncio.gather()`. Allow Cortex to dispatch independent sub-tasks (e.g., multiple file reads or web searches) to the Nginx cluster simultaneously.

## Deprecated / Wont-Do
* [ ] **[Epic] Speculative Decoding Pipeline** - (Superseded by 122B MoE MLX migration)
* [ ] **[Epic] Llama.cpp Nginx Cluster** - (Superseded by 122B MoE MLX migration)

## Active Sprints

### Sprint: Advanced Intel (Playwright & Search)
* [ ] **Upgrade Playwright Browser Tool:** Evolve the basic DSL into an advanced search and analysis engine. Must support multi-step interaction arrays (handling cookie banners, logins), targeted DOM extraction (tables/articles), and clean markdown formatting to allow the Intel Drone to scrape financial sites without a paid API.

## Unscheduled Ideas
* [ ] Integrate Discord scraping for sentiment analysis.
* [ ] Build "Ion Voice" for audio alerts.
* [ ] Research "Mean Reversion" strategy implementation.
* [ ] Integrate `pyotp` for Google Authenticator (TOTP) Zero-Trust execution verification.
* [ ] Technical Debt: Remove legacy `ToolResult` object checks (`.success`, `.output`) from ReAct loops, as tools now return standard strings.
* [ ] [Epic] Automated Obsidian Sync: Implement an automated cron schedule for the ThinkSync routine on the X1 Carbon to ensure the live Second Brain is always synchronized with the agent's environment.