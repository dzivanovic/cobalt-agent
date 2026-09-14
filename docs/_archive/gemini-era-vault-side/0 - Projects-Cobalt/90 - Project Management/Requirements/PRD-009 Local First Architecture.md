# PRD-009: Local First Architecture

**Status:** ✅ Implemented  
**Priority:** P0 - Critical Infrastructure  
**Author:** Cobalt Engineering Team  
**Date:** 2025-02-23  

---

## Executive Summary

Cobalt operates as a **local-first AI agent** with config-driven architecture. All routing decisions, department definitions, and behavioral policies are loaded from YAML configuration files at runtime, enabling rapid iteration without code changes.

---

## Technical Implementation

### Core Components

#### 1. Cortex (Router)
**File:** `src/cobalt_agent/brain/cortex.py`

The Cortex is the central routing engine that classifies user intent and dispatches to appropriate departments.

**Key Features:**
- **Config-Driven Departments**: Loads department definitions from `config.yaml` at initialization
- **Fast-Path Routing**: Deterministic keyword-based triage for common patterns
- **Prime Directive Gate**: Intercepts high-risk actions for HITL approval

```python
# Fast-path routing example
if any(keyword in message_lower for keyword in self.orchestrator_keywords):
    return orchestrator.plan_and_execute(user_input)

# High-risk intercept
if is_high_risk:
    return self._generate_proposal(user_input)
```

**Routing Flow:**
1. Parse user input
2. Check fast-path keywords (orchestrator, web research)
3. Classify domain using LLM with structured output (`DomainDecision` Pydantic model)
4. Apply Prime Directive security gate
5. Route to department handler

### Department Handlers

| Department | Function | Implementation |
|------------|----------|----------------|
| TACTICAL | Trading & Market Data | `Strategos` class in `brain/tactical.py` |
| INTEL | Research & Briefings | `MorningBriefing`, `DeepResearch` skills |
| OPS | Operations (Scribe, Scheduling) | `Scribe` class with file-based storage |
| ENGINEERING | Code generation | `EngineeringDepartment` in `brain/engineering.py` |
| GROWTH | Growth strategy | Placeholder (not yet implemented) |

### Configuration Structure

**File:** `configs/config.yaml`

```yaml
departments:
  TACTICAL:
    active: true
    description: "Handles Trading & Market Data"
  INTEL:
    active: true
    description: "Handles Research & Briefings"
  OPS:
    active: true
    description: "Handles Operations (Scribe, Medical, Scheduling)"

rules:
  cortex_routing:
    orchestrator_keywords:
      - "analyze"
      - "research"
      - "deep dive"
    high_risk_keywords:
      - "delete"
      - "remove"
      - "modify"
```

---

## Architecture Principles

### 1. Local First
- All core functionality operates without external dependencies
- Configuration files drive behavior, not hardcoded logic
- LLM calls use local LiteLLM interface with configurable providers

### 2. Configurable Routing
- Department definitions in YAML enable rapid reconfiguration
- Keyword lists for fast-path routing are configurable
- No hardcoded department names or routing logic

### 3. Graceful Degradation
- Unknown domains route to DEFAULT (ReAct loop)
- Missing configurations fall back to safe defaults
- Error handling with structured logging via `loguru`

---

## Technical Specifications

### Routing Model Schema

```python
class DomainDecision(BaseModel):
    domain_name: str = Field(description="The exact name of the department")
    reasoning: str = Field(description="Why this department fits the request")
    task_parameters: str = Field(description="Precise entity or query to act on")
```

### Error Handling Pattern

All department handlers use consistent error handling:

```python
try:
    return department_handler.run(params)
except Exception:
    logger.exception("Department execution failed")
    return "Error message"
```

---

## Integration Points

### Dependencies
- `pydantic` - Structured LLM outputs
- `loguru` - Unified logging
- `litellm` - LLM abstraction layer

### External Systems
- **Mattermost**: HITL approval notifications (via `interfaces/mattermost.py`)
- **PostgreSQL**: Memory persistence (via `memory/postgres.py`)
- **File System**: Scribe notes storage (`0 - Inbox/` directory)

---

## Acceptance Criteria

- [x] Cortex loads department definitions from `config.yaml`
- [x] Fast-path routing for orchestrator keywords works without LLM call
- [x] High-risk keyword intercept triggers HITL proposal engine
- [x] Unknown domains fall back to DEFAULT route (ReAct loop)
- [x] All department handlers have consistent error handling

---

## Future Enhancements

1. **Dynamic Department Loading**: Hot-reload config changes without restart
2. **Routing Analytics**: Track routing decisions for optimization
3. **Multi-Tenant Support**: Per-user department configurations

---

## Related Documents

- [PRD-004: Cortex LLM Switchboard Router](./PRD-004%20Cortex%20LLM%20Switchboard%20Router.md)
- [PRD-007: Sovereign Split-Brain Orchestration](./PRD-007%20Sovereign%20Split-Brain%20Orchestration.md)
- [ADR-014: Unified MoE Architecture](../ADR/ADR-014%20Unified%20MoE%20Architecture.md)