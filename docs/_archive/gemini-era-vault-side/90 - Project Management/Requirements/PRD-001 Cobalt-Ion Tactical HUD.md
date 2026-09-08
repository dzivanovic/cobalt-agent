---
title: "PRD-001: Cobalt-Ion Tactical HUD"
status: Draft
priority: P0
module: [Requirements]
phase: 1
complexity: L
tags: [cobalt, prd, requirements]
created: 2026-02-23
---

# PRD-001: Cobalt-Ion Tactical HUD

## 1. Executive Summary
**The Vision:** Build a "Co-Pilot" system for manual day trading.
**The Problem:** Professional trading requires processing dozens of variables (RVOL, Levels, Tape, News) in real-time. Humans are slow and emotional.
**The Solution:** A "Heads-Up Display" (HUD) that acts as a real-time **Confidence Gauge**. It calculates the mathematical "Expected Value" (EV) of a trade 10x/second, allowing the trader to execute with conviction.

## 2. Core Philosophy: Unified MoE Architecture

### 2.1 Single-System Local Execution
The system runs entirely on a single Mac Studio workstation using Python/PyQt6. All intelligence is provided by the local Qwen 3.5 122B model executing via LM Studio's headless API.

### 2.2 Unified Mixture of Experts (MoE)
The system utilizes a unified MoE architecture with domain-specific expert routing via the AOM (Accessibility Object Model) Fast Path router:

* **Cortex Dispatcher:** Central routing engine that directs tasks to appropriate expert brains based on domain classification.
* **Engineering Brain:** Code analysis, tool development, and system architecture tasks.
* **Ops Brain:** System monitoring, health checks, and operational intelligence.
* **Tactical Brain:** Real-time trading analysis, risk assessment, and trade execution support.
* **Strategy Brain:** Playbook-based strategy evaluation and pattern recognition.

### 2.3 Separation of Concerns
* **Unified Processing:** All computation occurs locally on the Mac Studio. No distributed architecture.
* **Local LLM Inference:** Qwen 3.5 122B provides all reasoning capabilities via headless LM Studio API.
* **pgvector Fast Path:** Repeated queries are cached in pgvector to bypass LLM inference on redundant computations.

## 3. User Stories

### Story A: The "Morning Briefing" (Context)
**As a** Trader,
**I want** Cobalt to scan the market for "In Play" stocks and identify the specific *Strategies* (from my Playbook) that apply to them (e.g., "NVDA is an Earnings Gap"),
**So that** I start the day with a curated list of opportunities, not just raw tickers.

### Story B: The "Formula Injection" (Handoff)
**As a** System Architect,
**I want** Cobalt to send a "Math Package" (JSON) containing the specific *Weights and Variables* for the day (e.g., "For NVDA, Gap Fill is +10 points, Resistance at $145 is -20 points"),
**So that** the local MoE can run calculations efficiently using cached pgvector results where applicable.

### Story C: The "Tactical Engagement" (The HUD)
**As a** Trader executing a trade,
**I want** a visual Gauge (0-100) that updates in real-time based on Price, Volume, and Time,
**So that** I can intuitively see if the trade is degrading (Score dropping) or improving (Score rising) without doing mental math.
* *Example:* "I am long NVDA. Volume dries up -> Score drops 10 points -> Gauge turns Yellow -> I trim my position."

### Story D: The "JIT Token" (Autonomous Execution)
**As a** Human-in-the-Loop Trader,
**I want** to issue a cryptographic Just-In-Time execution token via the Mattermost Proposal Engine,
**So that** Cobalt can execute trades autonomously during high-velocity market conditions while maintaining strict human oversight.
* *Example:* "I approve this trade with a 5-minute JIT token -> Cobalt executes at $145.25 -> Trade is closed if price moves against me."

## 4. Functional Requirements

### 4.1 The Scoring Engine (Dynamic EV)
The Score (0-100) is calculated as:
$$ Score = Base + Fuel - Friction - Decay $$
* **Base:** Static score from the Daily Setup (e.g., "A+ Setup" = 60).
* **Fuel (Momentum):** Live modifiers (e.g., `RVOL > 2.0` adds +10).
* **Friction (Risk):** Proximity to Resistance (e.g., `Dist < $0.10` subtracts -20).
* **Decay (Time):** Penalty for stalling (e.g., `-1 point` per minute of chop).

### 4.2 The "Math Package" Protocol
Cobalt must send a JSON payload containing:
* `Ticker`: Symbol (e.g., "NVDA").
* `Strategies`: List of active setups (e.g., ["GapAndGo", "BellaFade"]).
* `Zones`: Key Price Levels (Entry, Stop, Target).
* `Coefficients`: The weights for the Scoring Engine.

### 4.3 The Multi-Strategy Capability
The system must support **Conflicting Strategies** simultaneously.
* *Scenario:* NVDA gaps up.
* *HUD State:* Cobalt displays *two* potential scores:
    1.  **Long Score:** For the "Gap & Go" breakout.
    2.  **Short Score:** For the "Extension Fade" reversal.

### 4.4 The JIT Token Protocol
* **Format:** Cryptographically signed JWT token containing:
  * `symbol`: Trading pair/ticker
  * `direction`: Long/Short
  * `quantity`: Amount to execute
  * `deadline`: Unix timestamp for token expiration
  * `signature`: HMAC-SHA256 signature from Mattermost Proposal Engine
* **Validation:** Cobalt MUST verify the token signature before executing any trade.
* **Expiration:** Tokens expire after a configured time window (default: 5 minutes).

## 5. Technical Constraints
* **Language:** Python 3.11+.
* **GUI Framework:** PyQt6 for transparent overlays and HUD rendering.
* **LLM Backend:** Qwen 3.5 122B via headless LM Studio API (local execution).
* **Memory System:** pgvector for vector embeddings and Fast Path caching.
* **Data Source:** TradeStation API (connected locally).
* **Latency Target:** < 50ms from Tick to HUD Update (excluding LLM inference time).
* **Security:** All autonomous execution requires cryptographic token verification.
* **Architecture:** Unified MoE with AOM Fast Path router for domain-specific routing.

## 6. Future Extensibility
* **Discord Integration:** Manual scraping of trader sentiment to adjust "Base Scores."
* **Journaling:** Automated logging of *why* a score was high/low at the moment of execution.
* **Token Dashboard:** Web interface to view active JIT tokens and their expiration times.<task_progress>
- [x] Read and audit PRD-001 (identify Rust/Split-Brain references)
- [x] Update PRD-001 to Unified MoE Architecture (Python/PyQt6)
- [ ] Generate PRD-012 (Recon Scout and Vision Gateway)
- [ ] Task Board Alignment - Delete obsolete tasks
- [ ] Task Board Alignment - Create new formatted Markdown tasks
</task_progress>
</write_to_file>