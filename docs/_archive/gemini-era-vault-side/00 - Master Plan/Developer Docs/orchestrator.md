# Orchestrator Engine

## Overview
`cobalt_agent/core/orchestrator.py`

The `OrchestratorEngine` class is the Manager's Clipboard (Chief of Staff). It coordinates the "Split-Brain" architecture between the Architect (Planner) and specialized Drones (Executors).

## Class: OrchestratorEngine

### Description
The Manager's Clipboard (Chief of Staff). Coordinates the "Split-Brain" architecture between the Architect (Planner) and specialized Drones (Executors).

### Constructor
```python
def __init__(self)
```

Initializes the LLM instance for planning and execution.

### Methods

#### plan_and_execute
```python
def plan_and_execute(self, user_input: str) -> str
```

Executes the full planning and execution cycle.

**Parameters:**
- `user_input` (str): The user's request

**Returns:** String output log containing master plan and execution results

### Architecture Phases

#### Phase 1: Architect (Planning)
The Orchestrator generates a master plan by:
1. Analyzing the user's request
2. Breaking it down into atomic steps
3. Assigning each step to the appropriate Drone (ENGINEERING or OPS)

**AVAILABLE DRONES:**
- **ENGINEERING**: Writing Python code, modifying system files, analyzing software architecture
- **OPS**: Searching knowledge base, writing Markdown journals, summarizing text, reading/modifying Obsidian notes

**AVAILABLE TOOLS:**
- `search_knowledge`: Search internal codebase, playbooks, and Obsidian notes
- `read_file`: Read file contents
- `list_directory`: Explore folder structures
- `write_file`: Create or modify files

**Rules:**
1. Keep steps atomic (e.g., Step 1: search_knowledge, Step 2: read_file, Step 3: write_file)
2. Do NOT write code in the plan, just the actions the drone needs to take
3. Assign the correct Drone to each step based on the task domain

#### Phase 2: Drone Execution
The Orchestrator executes each step:
1. Builds context from previous steps
2. Routes to the appropriate Drone (Dynamic Drone Routing)
3. Captures results for the next step's context

**Dynamic Drone Routing:**
- OPS → `OpsDepartment`
- ENGINEERING → `EngineeringDepartment`

### Output Format
```
## 📋 Chief of Staff's Master Plan
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

### State Management
The orchestrator tracks execution state:
- `PLANNING`: Initial state
- `EXECUTING`: Actively running steps
- `COMPLETED`: All steps finished
- `PAUSED_FOR_APPROVAL`: Zero-Trust approval required
- `FAILED`: Execution halted due to error

### Error Handling
- Max retries: 3 for planning
- Self-healing retry loop for LLM JSON hallucinations
- Immediate halt on "Action paused" or "Proposal [" detection

## Key Components
- `LLM`: For structured planning responses
- `OpsDepartment`: Operations/Documentation drone
- `EngineeringDepartment`: Code generation drone
- `SubTask`: Pydantic model for planning steps

## See Also
- `BaseDepartment` - Unified ReAct execution engine
- `OpsDepartment` - Operations drone
- `EngineeringDepartment` - Engineering drone