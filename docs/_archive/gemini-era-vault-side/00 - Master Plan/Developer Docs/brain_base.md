# Base Department (Unified ReAct Engine)

## Overview
`cobalt_agent/brain/base.py`

The `BaseDepartment` class is the Unified ReAct Execution Engine. All specialized Drones inherit this execution loop, ensuring consistent behavior across all departments.

## Class: BaseDepartment

### Description
The Unified ReAct Execution Engine. All specialized Drones inherit this execution loop.

### Constructor
```python
def __init__(self, name: str, system_prompt: Optional[str] = None)
```

**Parameters:**
- `name` (str): The name of the department
- `system_prompt` (Optional[str]): Optional custom system prompt

### Methods

#### run
```python
def run(self, user_message: str, chat_history: Optional[List[Dict]] = None) -> str
```

Process a request using the ReAct loop.

**Parameters:**
- `user_message` (str): The user's request
- `chat_history` (Optional[List[Dict]]): Optional list of previous messages for context

**Returns:** The final response after tool execution or max loops

### Execution Flow
1. Build message history with system prompt and user input
2. Loop up to 4 times (max_loops):
   - Get LLM response using unified interface
   - Parse ACTION lines for tool execution
   - Execute tools via ToolManager
   - Append observations to history
3. Return final response when no ACTION found or max loops reached

### Fast Exit Protocol
The ReAct loop exits early when:
- "Action paused" is in result (Zero-Trust Proposal wall)
- "Proposal [" is in result (Pending human approval)

## Key Components
- `LLM`: LLM instance for generating responses
- `ToolManager`: Handles tool execution
- `system_prompt`: Department-specific system prompt

## See Also
- `OpsDepartment` - Scribe/Operations department
- `EngineeringDepartment` - Code generation department
- `BaseDepartment` - Abstract base class for all departments