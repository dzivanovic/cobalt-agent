---
title: "ADR-007 HITL Proposal Engine"
status: Active
priority: P0
module: [Cortex, Security]
phase: 3
complexity: L
tags: [cobalt, architecture, security, hitl]
created: 2026-02-23
---

# ADR-007: Human-in-the-Loop (HITL) Proposal Engine

## Status: ACCEPTED

## Decision
We will implement a standardized `Proposal` Pydantic model that the Cortex must generate for any "High-Stakes" action. A high-stakes action is defined as any command that modifies the file system, executes code, or initiates a financial transaction.

## Context
The current routing logic in `cortex.py` is susceptible to keyword misclassification (e.g., mistaking "NVIDIA files" for a "TACTICAL" trading query). By forcing a "Proposal" step, the agent must pause, summarize the risk, and await a cryptographic token (or manual 'YES' in the short term) before proceeding.

## Implementation Details
1. **Middleware Layer**: A new validation step in `cortex.py` that checks the "Risk Level" of a classified task.
2. **Standardized Model**: All proposals will include:
   - `task_id`: Unique identifier.
   - `action`: The raw command to be executed.
   - `justification`: Why the agent thinks this is necessary.
   - `risk_assessment`: A summary of what could go wrong (e.g., "Permanent data loss").
3. **Approval Flow**: The agent will post the proposal to Mattermost and wait for the user to respond with "Approve [task_id]".

## Next Steps
- Define the `Proposal` model in a new `src/cobalt_agent/core/proposals.py` file.
- Update `cortex.py` to utilize this model for any non-read-only tasks.