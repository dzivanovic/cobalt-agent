---
title: "Project Cobalt Architecture Assessment"
status: Active
priority: P0
module: [Architecture]
phase: 1
complexity: L
tags: [cobalt, architecture, master_plan]
created: 2026-02-23
---

# ARCHITECTURE ASSESSMENT: Project Cobalt
**Date:** February 2026
**Status:** Alpha / Proof of Concept
**Focus:** Enterprise-Grade Autonomous Trading & Chief of Staff System

## 1. Executive Summary
Project Cobalt has successfully established its "Nervous System" and "Memory." The core event loop is decoupled, allowing asynchronous communication via Mattermost, while the brain utilizes a robust LiteLLM abstraction layer mapped to local and cloud models. The architecture strictly enforces type-safety via Pydantic and relies on configuration-as-code (YAML) for strategy and system parameters. 

## 2. Current Strengths (The Foundation)
* **Decoupled C2 Interface:** The `mattermost.py` implementation successfully uses `asyncio.to_thread` to maintain a persistent WebSocket connection without blocking the primary LLM inference loop.
* **Agentic RAG Foundation:** `postgres.py` successfully utilizes `pgvector` to store both textual logs and high-dimensional semantic embeddings, creating a persistent "Hippocampus" that can be queried conceptually.
* **Config-Driven Playbooks:** The `Playbook` and `SecondDayPlay` modules load dynamic scoring weights from `strategies.yaml`, avoiding hardcoded logic and enabling future autonomous modification.
* **LLM Abstraction:** The `llm.py` module elegantly wraps `litellm`, exposing a strict `ask_structured` method that guarantees JSON/Pydantic compliance for complex agent reasoning.

## 3. Technical Debt & Immediate Gaps
* **Routing Brittleness:** The current `cortex.py` and `mattermost.py` routing relies on hardcoded keyword bypasses (e.g., `if "?" in text`). This must be replaced with a localized "Switchboard" LLM router.
* **Missing Execution Hands:** The system currently lacks a sandboxed Code Execution Tool (Docker/Seccomp) to safely run Python scripts.
* **Missing "Touch" (Playwright):** Browser capability has been upgraded to a full Playwright Agentic Browser Loop with AOM extraction and pgvector Fast Path cache, enabling dynamic web interaction, complex scraping, and persistent semantic caching of DOM state.
* **Missing Secrets Management:** Integration with a Vault/LastPass API is required to facilitate Just-In-Time (JIT) credential injection without hardcoding keys.
* **Proposal Engine:** There is no standardized Pydantic schema for the AI to request "Google Auth" permission before executing a high-risk task.

## 4. Target State Architecture
* **Unified Mixture of Experts (MoE) Runtime:**
    * **Single Frontier-Class Model:** A unified, frontier-class local Mixture of Experts (Qwen 3.5 122B MoE via LM Studio) handles both routing and deep reasoning tasks.
    * **MLX Acceleration:** Native Apple Silicon optimization via MLX provides deterministic, low-latency inference without external API dependencies.
    * **Consistent Context Window:** All operations—chat, tool routing, strategy analysis, and backtesting—execute within a single, coherent context space.
* **Local-First Execution:** Python orchestrates all operations directly on Apple Silicon hardware; no execution split or external clients required.
* **Zero Trust (ZTA):** All system modifications and external actions proposed by Cobalt are halted at a Privilege Boundary, requiring asynchronous Human-in-the-Loop (HITL) cryptographic approval.
