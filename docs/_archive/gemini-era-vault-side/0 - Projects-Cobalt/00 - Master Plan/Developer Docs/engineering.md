---
title: "Engineering Department Documentation"
status: Active
module: Brain
type: Department
dependencies:
  - "[[cortex]]"
  - "[[tool_manager]]"
  - "[[filesystem]]"
  - "[[proposals]]"
location: "src/cobalt_agent/brain/engineering.py"
tags: [cobalt, dev_docs, engineering, prompt]
created: 2026-02-25
---

# Engineering Department

## Overview
The Engineering Department is Cobalt's **principal systems architect and senior software engineer**. It handles code reading, analysis, and writing tasks with strict Zero Trust Human-in-the-Loop (HITL) approval for file modifications.

### Zero Trust Integration
- **Write operations always require approval** - No file can be modified without explicit human approval
- **Wait Protocol** - LLM must stop after submitting a proposal, not retry writing
- **Context Efficiency** - Skip directory crawls when given exact file paths

## Class: `EngineeringDepartment`

### Constructor
```python
def __init__(self)
```
Initializes the Engineering Department with configuration from `config.yaml`.

**Components:**
- `llm`: LLM instance for code analysis and generation
- `tool_manager`: Tool registry for code operations

---

## Critical Prompt Rules

The Engineering Department's system prompt enforces strict Zero Trust and efficiency protocols.

### 1. Strict Tool Syntax

**Rule:** YOU MUST USE THE EXACT SYNTAX BELOW TO CALL A TOOL.

**Correct Syntax:**
```python
ACTION: write_file {"filepath": "src/test.py", "content": "print('hello')"}
```

**Incorrect Syntax:**
```python
# No ACTION prefix
{"filepath": "src/test.py", "content": "print('hello')"}

# JSON wrapper
```json
{"filepath": "src/test.py", "content": "print('hello')"}
```

# Text response
I will create the file now.
```

**Enforcement:** The LLM generates a syntax error if the ACTION: prefix is missing.

### 2. No Roleplaying

**Rule:** DO NOT roleplay. DO NOT say "I will create the file now." Just output the ACTION string.

**Compliance:**
- Output ONLY the ACTION line
- Do not explain what you're doing
- Do not provide conversational preamble

### 3. Context Efficiency (Workflow)

**Rule:** If the user provides an exact filepath, DO NOT use `list_directory`. Execute `write_file` immediately to save context space.

**Example:**
```
User: "Create a file at src/new_module.py"

INCORRECT: List directory first
1. ACTION: list_directory {"directory_path": "src/"}
2. ACTION: write_file {...}

CORRECT: Direct write
1. ACTION: write_file {"filepath": "src/new_module.py", "content": "..."}

**Benefit:** Saves context window tokens for longer conversations
```

### 4. Wait Protocol (Infinite Loop Prevention)

**Rule:** If you use the `write_file` tool and the System Observation says "Action paused. Proposal sent", YOU MUST STOP. Output a final conversational message saying "I have submitted the proposal for your approval." DO NOT try to write the file again.

**Implementation:**
```python
# System Observation after write_file proposal:
"[Observation: Action paused. Proposal abc12345 sent to Admin for approval in Mattermost.]"

# LLM MUST respond with:
"I have submitted the proposal for your approval."

# LLM MUST NOT:
# - Try write_file again
# - Ask for approval
# - Provide multiple ACTION lines
```

**Zero Trust Flow:**
```
1. LLM outputs ACTION: write_file {...}
   ↓
2. WriteFileTool creates Proposal Engine ticket
   ↓
3. System returns: "[Observation: Action paused. Proposal abc12345 sent...]"
   ↓
4. LLM receives observation, must STOP
   ↓
5. LLM outputs final message: "I have submitted the proposal for your approval."
   ↓
6. User responds in Mattermost: "Approve abc12345"
   ↓
7. Callback executes, file modification completes
```

### 5. No Guessing

**Rule:** NEVER guess the contents of a file or directory.

**Compliance:**
- Always use `read_file` to examine file contents
- Always use `list_directory` to explore folder contents
- Do not invent file structures or content

---

## Available Tools

### `read_file`
Reads the contents of a file.

**Syntax:**
```python
ACTION: read_file {"filepath": "src/main.py"}
```

**Use Cases:**
- Examine existing code
- Verify file contents before modification
- Read configuration files

### `list_directory`
Lists the contents of a directory.

**Syntax:**
```python
ACTION: list_directory {"directory_path": "src/"}
```

**Use Cases:**
- Explore project structure
- Find existing files
- Verify directory layout

### `write_file`
Modifies or creates a file. **Always requires HITL approval.**

**Syntax:**
```python
ACTION: write_file {"filepath": "src/test.py", "content": "print('hello')"}
```

**Use Cases:**
- Create new files
- Update existing files
- Modify configuration

---

## ReAct Loop Implementation

The Engineering Department uses a ReAct (Reasoning-Acting) loop for tool execution.

### Loop Constraints

```python
max_loops = 4  # Maximum tool invocations per request
```

### Loop Flow
```
1. Get LLM response with system prompt
   ↓
2. ┌───────────── ACTION: detected? ─────────┐
   │                                         ↓
   │                                     No → return response
   ↓
3. Extract tool name and arguments
   ↓
4. Execute tool via ToolManager
   ↓
5. Format observation
   ↓
6. Append observation to conversation history
   ↓
7. Loop back to step 1
   ↓
8. ┌───────────── Max loops reached? ─────────┐
   │                                         ↓
   │                                     No → continue
   ↓
   ┌───────────── Yes ─────────┐
   │                           ↓
   │                  Return error: "ReAct loop maxed out"
   │
   └───────────────────────────┘
```

---

## Output Format

### Successful Tool Execution

```
Observation: File written successfully to src/test.py (100 bytes)
```

### Proposal Sent (Write File)

```
Observation: Action paused. Proposal abc12345 sent to Admin for approval in Mattermost.
```

### Error Output

```
Error: Tool 'read_file' failed: File not found: src/nonexistent.py
```

### Final Response

```
I have successfully created the file at src/test.py.
```

---

## Error Handling

| Error Type | Message | Action |
|-----------|---------|--------|
| Tool not found | `"Error: Tool 'xxx' not found."` | Return to user |
| Missing filepath | `"Error: Missing filepath or content."` | Return to user |
| LLM no ACTION | Return response as final answer | Done |
| ReAct loop maxed | `"Error: ReAct loop maxed out. Please simplify the request."` | Return to user |

---

## Integration with Proposal Engine

When `write_file` is called:

```python
# WriteFileTool executes:
proposal = create_and_send_proposal(
    action=f"Write {len(content)} bytes to {filepath}",
    justification="Agent requested file modification via WriteFileTool.",
    risk_assessment="HIGH"
)

if proposal:
    engine = ProposalEngine()
    engine.set_approval_callback(proposal.task_id, execute_write)
    return f"Action paused. Proposal [{proposal.task_id}] sent to Admin for approval."
```

---

## Configuration

No additional configuration required. The department uses the global Proposal Engine configuration for write operations.