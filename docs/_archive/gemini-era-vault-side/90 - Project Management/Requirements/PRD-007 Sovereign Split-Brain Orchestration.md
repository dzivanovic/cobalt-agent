---
title: "PRD-007: Sovereign Split-Brain Orchestration"
status: Approved
priority: P0
module: [Requirements, Brain]
phase: 4
complexity: M
tags: [cobalt, prd, requirements, multi-agent]
created: 2026-02-26
---

# PRD-007: Sovereign Split-Brain Orchestration

## 1. Executive Summary
**The Problem:** The current agent suffers from Cognitive Overload. When asked to write code, it attempts to plan architecture, write Python, format JSON tools, and adhere to trading risk-management rules simultaneously within a single context window. This leads to infinite loops and hallucinated syntax.
**The Solution:** Implement a Hierarchical Multi-Agent Architecture ("Split-Brain"). A Manager agent (Cortex) plans the architecture, and a Worker agent (The Forge) executes the code.

## 2. Core Philosophy
1. **Cognitive Decoupling:** Planning and Execution must never happen in the same LLM inference call.
2. **Sovereignty Preserved:** Both the Manager and Worker roles will be executed sequentially by the local model to maintain absolute data privacy.
3. **Dynamic Personas:** The Manager will dynamically generate restricted personas for the Worker, removing irrelevant context (like trading rules during a coding task).
4. **Future-Proofing (Async):** The state machine must be designed synchronously first for stability, but decoupled enough to support `asyncio.gather()` when the local infrastructure is upgraded to a multi-instance Nginx cluster.

## 3. Functional Requirements
* **The Master Plan:** Cortex must output a step-by-step array of tasks *before* any tools are invoked.
* **The State Clipboard:** Python must maintain an `OrchestrationState` dictionary tracking the original request, the plan, current step, and worker observations.
* **The Feedback Loop:** If a Worker errors out, the Manager must be woken up, handed the error via the Clipboard, and asked to revise the Master Plan.