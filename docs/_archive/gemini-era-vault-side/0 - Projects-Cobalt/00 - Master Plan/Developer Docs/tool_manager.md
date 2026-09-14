---
title: "Tool Manager Documentation"
status: Active
module: Core
type: Orchestrator
dependencies:
  - "[[search]]"
  - "[[browser]]"
  - "[[finance]]"
location: "src/cobalt_agent/tools/tool_manager.py"
tags: [cobalt, dev_docs]
created: 2026-02-23
---

# Tool Manager Module

## Overview

Cobalt Agent - Tool Manager is a registry and execution engine for all agent capabilities.

## Class: `ToolResult` (Pydantic Model)

Standardized output for any tool execution.

### Fields

| Field | Type | Description |
|-------|------|-------------|
| `success` | `bool` | Whether the tool execution succeeded |
| `output` | `Any` | The result output from the tool |
| `error` | `Optional[str]` | Error message if execution failed |

---

## Class: `ToolManager`

Manages the registration and execution of tools. Allows the LLM to 'see' and 'use' functions.

### Constructor

```python
ToolManager()
```

Initializes the tool manager and registers core tools:
1. SearchTool
2. BrowserTool
3. FinanceTool

### Methods

#### `register_tool(name: str, tool_instance: Any) -> None`
Add a new tool to the registry.

**Parameters:**
- `name`: Unique identifier for the tool
- `tool_instance`: Instance of the tool (must have a `run()` method)

#### `get_tool_descriptions() -> List[Any]`
Return the list of tool objects for the Prompt Engine.

#### `execute_tool(tool_name: str, args: Dict[str, Any]) -> ToolResult`
Execute a registered tool by name.

**Parameters:**
- `tool_name`: The name of the tool (e.g., 'search')
- `args`: Dictionary of arguments for the tool

**Returns:** `ToolResult` with success status, output, and optional error message.

### Tool Execution Logic

1. Extract query from args (supports 'query', 'q', or first value)
2. Check if tool exists
3. Call tool's `run()` method
4. Return standardized result

---

## Tool Registry

| Name | Class | Description |
|------|-------|-------------|
| `search` | SearchTool | Internet search for information |
| `browser` | BrowserTool | Web page content retrieval |
| `finance` | FinanceTool | Market data retrieval |