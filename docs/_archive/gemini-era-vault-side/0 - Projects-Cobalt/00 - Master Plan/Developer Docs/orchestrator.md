# Orchestrator Engine

## Overview
**File:** `src/cobalt_agent/core/orchestrator.py`

The `OrchestratorEngine` class serves as the **Central Loop Manager** for Cobalt Agent. It coordinates the "Split-Brain" architecture between the Architect (Planner) and specialized Drones (Executors), managing dynamic routing between departments.

---

## Architecture Role

### Central Loop Manager
The Orchestrator is the system's **Chief of Staff**, responsible for:
- Breaking down complex user requests into atomic, executable steps
- Maintaining state across the execution lifecycle
- Routing tasks to appropriate specialized departments (Engineering or Ops)
- Implementing self-healing retry loops to overcome LLM JSON hallucinations

### System Initialization
Upon initialization, the Orchestrator:
1. Instantiates an LLM configured with "architect" role for structured planning
2. Prepares the execution environment for state tracking via Pydantic models

---

## Data Models

### SubTask
Represents an individual step in the master plan.

| Field | Type | Description |
|-------|------|-------------|
| `step_number` | int | Sequential order (1, 2, 3...) |
| `assigned_drone` | str | Department: 'ENGINEERING' or 'OPS' |
| `action` | str | Description of what needs to be done |
| `tool_to_use` | str | Exact name of the tool to invoke |
| `status` | str | PENDING, SUCCESS, or FAILED |
| `observation` | str | Output or error from execution |

### OrchestrationState
Tracks the complete state of a planning/execution cycle.

| Field | Type | Description |
|-------|------|-------------|
| `scratchpad` | str | Chain of thought reasoning |
| `original_request` | str | User's exact original request |
| `master_plan` | List[SubTask] | Step-by-step execution plan (min 1 task) |
| `current_step` | int | Current step index (default: 1) |
| `status` | str | PLANNING, EXECUTING, FAILED, COMPLETED |

---

## Class: OrchestratorEngine

### Constructor
```python
def __init__(self)
```
Initializes the LLM instance configured for architectural planning.

### Primary Method: `plan_and_execute`
```python
def plan_and_execute(self, user_input: str) -> str
```

**Purpose:** Executes the full planning and execution cycle.

**Parameters:**
- `user_input` (str): The user's request to process

**Returns:** String output log containing master plan and execution results

---

## Execution Flow

### Phase 1: Architect (Planning)
The Orchestrator generates a master plan by:

1. **Analyzing** the user's request through the Architect LLM
2. **Breaking down** into atomic, sequential steps
3. **Assigning** each step to the appropriate Drone based on domain

**Available Drones:**
- **ENGINEERING**: Writing Python code, modifying system files, analyzing software architecture
- **OPS**: Searching knowledge base, writing Markdown journals, summarizing text, reading/modifying Obsidian notes

**Available Tools:**
- `search_knowledge`: Search internal codebase, playbooks, and Obsidian notes
- `read_file`: Read file contents
- `list_directory`: Explore folder structures
- `write_file`: Create or modify files

**Planning Rules:**
1. Keep steps atomic (e.g., Step 1: search_knowledge, Step 2: read_file)
2. Do NOT write code in the plan—just drone actions
3. Assign correct Drone based on task domain

### Phase 2: Drone Execution (Dynamic Routing)
The Orchestrator executes each step through a dynamic routing mechanism:

1. **Build Context:** Aggregates results from previous steps
2. **Route Dynamically:** Selects appropriate department based on `assigned_drone` field
3. **Execute:** Invokes the drone's ReAct loop with localized context
4. **Capture Results:** Stores observations for subsequent steps

**Dynamic Routing Logic:**
```python
if drone_type == "OPS":
    from cobalt_agent.brain.ops import OpsDepartment
    drone = OpsDepartment()
else:  # Default to Engineering
    from cobalt_agent.brain.engineering import EngineeringDepartment
    drone = EngineeringDepartment()
```

**Execution Context Structure:**
- Overall mission (original user request)
- Previous step results (context accumulation)
- System map (current working directory structure)
- Specific step to execute
- Execution rules for tool usage

---

## State Management

### Lifecycle States
| State | Description |
|-------|-------------|
| `PLANNING` | Initial state during plan generation |
| `EXECUTING` | Actively running steps |
| `COMPLETED` | All steps finished successfully |
| `PAUSED_FOR_APPROVAL` | Zero-Trust HITL approval required |
| `FAILED` | Execution halted due to error |

### Zero Trust Break Conditions
Execution pauses when:
- `"Action paused"` detected in result → `PAUSED_FOR_APPROVAL`
- `"Proposal ["` detected in result → HITL approval required
- `"Error:"` detected in result → `FAILED`, halt immediately

---

## Error Handling

### Self-Healing Retry Loop
- **Max Retries:** 3 attempts for planning phase
- **Purpose:** Overcome local LLM JSON hallucinations
- **Mechanism:** Retry loop with exponential backoff logic

### Failsafe Protocol
If no valid plan is generated after 3 attempts:
```python
return "❌ **Architect Error:** The LLM failed to generate a valid plan after 3 attempts. Please simplify the request."
```

---

## Output Format

```
### 📋 Chief of Staff's Master Plan
**Thoughts:** *Chain of thought explanation*

1. **[ENGINEERING]** Action description (Tool: `tool_name`)
2. **[OPS]** Action description (Tool: `tool_name`)

### 🚀 Execution Log
**Executing Step 1 (ENGINEERING):** Action description
> Result from drone

**Executing Step 2 (OPS):** Action description
> Result from drone

✅ **Mission Accomplished.**
```

---

## Key Dependencies

| Component | Purpose |
|-----------|---------|
| `LLM` | Structured planning and responses |
| `OpsDepartment` | Operations/Documentation drone |
| `EngineeringDepartment` | Code generation drone |
| `SubTask` | Pydantic model for planning steps |
| `OrchestrationState` | Complete state tracking model |

---

## Related Components

- **BaseDepartment** - Unified ReAct execution engine
- **OpsDepartment** - Operations and documentation specialist
- **EngineeringDepartment** - Code generation and architecture specialist
- **Cortex** - Central brain component for decision making

---

## Usage Example

```python
from cobalt_agent.core.orchestrator import OrchestratorEngine

orchestrator = OrchestratorEngine()
result = orchestrator.plan_and_execute("Write a Python script to fetch market data")
print(result)
```

---

## Design Principles

1. **Atomic Steps:** Each step performs one discrete action
2. **Context Accumulation:** Previous results inform subsequent steps
3. **Domain Routing:** Tasks routed to specialized departments
4. **Self-Healing:** Retry loops overcome transient LLM failures
5. **Zero Trust:** Human approval required for critical actions

---

## See Also

- `src/cobalt_agent/brain/base.py` - Base department implementation
- `src/cobalt_agent/brain/engineering.py` - Engineering department
- `src/cobalt_agent/brain/ops.py` - Operations department
- `PRD-007 Sovereign Split-Brain Orchestration` - Architecture requirements