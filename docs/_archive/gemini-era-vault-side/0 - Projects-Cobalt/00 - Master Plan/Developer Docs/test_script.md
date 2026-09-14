# Test Script

## Overview
`cobalt_agent/tools/test_script.py`

A simple test script used for validating tool execution in the Cobalt agent.

## File Contents
```python
print("Hello from the Forge")
```

## Purpose
This minimal script serves as a basic smoke test to:
1. Verify tool execution pipeline is functional
2. Confirm file write operations work correctly
3. Validate the `write_file` tool integration

## Usage
When invoked via the `write_file` tool in the agent:
1. Creates or overwrites a file with this content
2. Outputs "Hello from the Forge" to standard output

## See Also
- `ToolManager` - Tool execution coordination
- `BrainBase` - ReAct loop execution