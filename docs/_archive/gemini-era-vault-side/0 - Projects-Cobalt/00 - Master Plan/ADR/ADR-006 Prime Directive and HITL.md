---
title: "ADR-006 Prime Directive and HITL"
status: Active
priority: P0
module: [Architecture, Security]
phase: 2
complexity: M
tags: [cobalt, architecture, documentation, adr, security]
created: 2026-02-23
---

# ADR-006: Prime Directive and Human-In-The-Loop (HITL) Core Personality

## Status: ACCEPTED

## Decision
We are explicitly binding the Cobalt Agent's personality to a "Zero Trust" and "Proposal Engine" framework via configuration-as-code (`config.yaml`). Cobalt will operate under a strict Prime Directive: it cannot execute destructive, financial, or system-altering commands autonomously. 

## Context
Previously, Cobalt's directives were generic ("Protect capital", "Analyze data"). To achieve enterprise-grade security, the system prompt must fundamentally restrict the agent's autonomy at the personality level, forcing it to generate a "proposal" for the human operator rather than taking unilateral action.

## Implementation Details
1.  **Configuration Driven:** The Prime Directive is injected via the `persona.directives` list in `config.yaml`.
2.  **Prompt Engine Integration:** The existing `prompt.py` will automatically parse these new directives and construct the system prompt.
3.  **The Proposal Engine Hook:** The agent is explicitly instructed to draft proposals and await cryptographic authorization for high-stakes tasks.

## Trade-offs
| Option | Pros | Cons |
|--------|------|------|
| Hardcoded Python Logic | Unbreakable | Violates decoupled architecture |
| Config-Driven (Chosen) | Flexible, maintains separation of concerns | Relies on LLM adherence to prompt |