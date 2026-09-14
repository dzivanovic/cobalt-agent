---
status: Done
priority: P0
module: Brain
phase: 4
complexity: M
tags: [cobalt, task, split-brain]
created: 2026-02-26
---
# 38 Split-Brain Architect (Cortex)

## Objective
Upgrade `cortex.py` from a dumb switchboard into an LLM-powered Chief of Staff that generates step-by-step Master Plans for the Engineering department.

## Acceptance Criteria
- [ ] Cortex uses `ask_structured` to generate an `OrchestrationState` plan.
- [ ] Cortex prints its plan to Mattermost before execution.