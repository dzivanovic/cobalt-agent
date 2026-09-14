# Base Department (Unified ReAct Engine)

## Overview
`src/cobalt_agent/brain/base.py`

The `BaseDepartment` class is the Unified ReAct Execution Engine. All specialized Drones (Departments) inherit this execution loop, ensuring consistent behavior across all departments.

## Class: BaseDepartment

### Description
The abstract base class implementing a unified ReAct (Reason-Act) execution loop with HITL (Human-in-the-Loop) approval support. All specialized Drones inherit this execution loop.

### Constructor
```python
def __init__(self, name: str, role: str = "default", system_prompt: Optional[str] = None)
```

**Parameters:**
- `name` (str): The name of the department (e.g., "Ops", "Engineering")
- `role` (str): The LLM role for this department (default: "default")
- `system_prompt` (Optional[str]): Optional custom system prompt

**Instance Variables:**
- `self.llm`: LLM instance for generating responses
- `self.tool_manager`: ToolManager instance for tool execution
- `self.system_prompt`: Department-specific system prompt

### Methods

#### run
```python
def run(self, user_message: str, chat_history: Optional[List[Dict]] = None) -> str | dict
```

Process a request using the ReAct loop with HITL approval support.

**Parameters:**
- `user_message` (str): The user's request
- `chat_history` (Optional[List[Dict]]): Optional list of previous messages for context

**Returns:** 
- `str`: Final response when task completes or LLM responds without ACTION
- `dict`: When tool requires approval (status: "requires_approval")

**Raises:** 
- Returns error message string when ReAct loop maxes out

### Execution Flow

1. **Initialize Message History**
   - Build message list from optional `chat_history`
   - Append current user request as `{"role": "user", "content": ...}`

2. **ReAct Loop (max 4 iterations)**
   - Generate LLM response via `llm.generate_response()` with memory context
   - Check for `ACTION:` prefix in response

3. **Parse and Execute ACTION**
   - Extract lines starting with `ACTION:`
   - Parse command as `tool_name {json_args}` format
   - Handle JSON parsing with fallback for single-quote strings to double-quote conversion
   - Execute tool via `tool_manager.execute_tool()`

4. **Handle Tool Results**
   - If result is dict with `status == "requires_approval"`: Return immediately for HITL approval
   - If result contains "Action paused" or "Proposal [": Return immediately (Fast Exit)
   - Otherwise, append observation to message history and continue loop

5. **Final Response**
   - When no ACTION found: Return LLM response directly
   - When max loops reached: Return error message

### Key Fixes Implemented
- **FIX 1**: System prompt is NOT appended here; `llm.py` handles it internally
- **FIX 2**: All observations and errors use `role="user"` for proper chat history formatting

### Error Handling
- Malformed ACTION format: Returns error prompting correct syntax
- JSON parse failures: Logs warning, returns formatted error observation
- Tool execution exceptions: Logs full traceback, continues loop with error message

## Key Components
| Component | Purpose |
|-----------|---------|
| `LLM` | Generates responses using unified interface |
| `ToolManager` | Executes tools and returns results/statuses |
| `system_prompt` | Department-specific prompt (handled by LLM class) |

## HITL Approval Flow
When a tool returns `{"status": "requires_approval"}`, the `run()` method immediately returns this dict instead of continuing the loop. This triggers the ProposalEngine for human approval before executing sensitive operations.

## See Also
- `OpsDepartment` - Scribe/Operations department (uses this base class)
- `EngineeringDepartment` - Code generation department (uses this base class)
- `TacticalDepartment` - Tactical execution department (uses this base class)
