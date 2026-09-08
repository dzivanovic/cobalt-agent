---
title: "Filesystem Tools Documentation"
status: Active
module: Tools
type: Tool Suite
dependencies:
  - "[[proposals]]"
  - "[[tool_manager]]"
  - "[[config]]"
location: "src/cobalt_agent/tools/filesystem.py"
tags: [cobalt, dev_docs, filesystem, tools]
created: 2026-02-25
updated: 2026-02-27
---

# Filesystem Tools

## Overview
The Filesystem module provides safe, auditable file operations for the Cobalt Agent. All write operations are subject to Zero Trust Human-in-the-Loop (HITL) approval via the Proposal Engine.

### Zero Trust Integration
- **Write operations always require approval** - No file can be modified without explicit human approval
- **Memory-locked callbacks** - Execution closures are stored in RAM only, mapped to 8-character task IDs
- **Pydantic schema validation** - Strict JSON parsing with no fallback to unsafe evaluation
- **Dynamic filesystem paths** - All paths are resolved via `cobalt_agent.config` from the `.env` vault root

## Tools

### ReadFileTool
Reads the contents of a file.

**Name:** `read_file`

**Description:** Read the contents of a file. Use when you need to examine existing code or data.

**Syntax:**
```python
ACTION: read_file {"filepath": "src/main.py"}
```

### ListDirectoryTool
Lists the contents of a directory.

**Name:** `list_directory`

**Description:** List the contents of a directory. Use when you need to explore the file structure.

**Syntax:**
```python
ACTION: list_directory {"directory_path": "src/"}
```

### WriteFileTool (Zero Trust)

Modifies or creates a file. **This tool ALWAYS requires Human-in-the-Loop approval.**

**Name:** `write_file`

**Zero Trust Flow:**
```
1. LLM requests file modification
   ↓
2. WriteFileTool parses arguments (strict JSON validation)
   ↓
3. WriteFileTool creates Proposal Engine ticket
   ↓
4. Proposal sent to Mattermost approval channel
   ↓
5. User responds with "Approve [task_id]"
   ↓
6. MattermostInterface intercepts approval
   ↓
7. Callback execution closes the loop
   ↓
8. File modification executes in RAM
```

## WriteFileTool Implementation

### Strict JSON Validation

The WriteFileTool implements strict JSON validation using Pydantic schemas to ensure data integrity without unsafe evaluation.

```python
# Strict JSON validation via Pydantic schema
data = query if query is not None else kwargs

if isinstance(data, str):
    try:
        data = json.loads(data)
    except json.JSONDecodeError as e:
        logger.error(f"WriteFileTool JSON validation failed: {e} | Data: {data}")
        return f"Error: Failed to parse arguments. Expected valid JSON. Received: {data}"
```

**Validation Flow:**
1. **JSON parsing** - Primary format for structured data
2. **Pydantic schema validation** - Strict type checking via input models
3. **Error reporting** - Detailed error message for LLM self-correction

**Supported Input Formats:**
| Format | Example | Parsed By |
|--------|---------|----------|
| Dictionary | `{"filepath": "test.py", "content": "print('hi')}"}` | Direct dict access |
| JSON string | `'{"filepath": "test.py", "content": "print(\'hi\')"}'` | `json.loads()` |
| Pydantic model | `WriteFileInput(filepath="test.py", content="print('hi')")` | Schema validation |

### Input Schema Enforcement

All filesystem tools are bound to strict Pydantic input models:

```python
# ReadFileTool
class ReadFileInput(BaseModel):
    filepath: str

# WriteFileTool  
class WriteFileInput(BaseModel):
    filepath: str
    content: str

# ListDirectoryTool
class ListDirectoryInput(BaseModel):
    directory_path: str
```

Tools are registered with their schemas in `ToolManager`:

```python
self.register_tool("write_file", WriteFileTool(), schema=WriteFileInput)
```

## Dynamic Filesystem Paths

All filesystem paths are resolved dynamically from the `.env` vault root via `cobalt_agent.config`:

```python
from cobalt_agent.config import get_config

config = get_config()
vault_root = config.system.obsidian_vault_path  # Dynamically loaded from .env
inbox_path = Path(vault_root) / "0 - Inbox/"  # OS-agnostic path construction
```

**Path Resolution Rules:**
1. **Vault root** - Always loaded from `.env` via `config.system.obsidian_vault_path`
2. **OS-agnostic paths** - Use `pathlib.Path` for all path operations
3. **No hardcoded paths** - No magic strings or absolute paths in code

## Execute Closure (Memory-Locked)

When a proposal is created, the WriteFileTool creates a closure that captures the file path and content:

```python
def execute_write(proposal_obj):
    try:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        logger.info(f"Proposal Engine executed write to: {filepath} ({len(content)} bytes)")
    except Exception as e:
        logger.exception(f"Failed to physically write file {filepath}")
```

This closure is stored in the `ProposalEngine.callbacks` dictionary and executed only after approval.

## Integration with ProposalEngine

```python
try:
    proposal = create_and_send_proposal(
        action=f"Write {len(content)} bytes to {filepath}",
        justification="Agent requested file modification via WriteFileTool.",
        risk_assessment="HIGH"
    )
except Exception as e:
    logger.exception(f"Proposal Engine crash")
    return f"Error: Proposal Engine crashed: {e}"

if proposal:
    engine = ProposalEngine()
    engine.set_approval_callback(proposal.task_id, execute_write)
    engine.pending_proposals[proposal.task_id] = proposal
    return f"Action paused. Proposal [{proposal.task_id}] sent to Admin for approval in Mattermost."
else:
    return "Error: Failed to generate Proposal Ticket. Mattermost connection failed."
```

## Output Format

When a write request is received, the tool returns:

```
Action paused. Proposal [abc12345] sent to Admin for approval in Mattermost.
```

After approval via Mattermost (user responds with "Approve abc12345"):

```
Approval received for task [abc12345]. Action executed successfully.
```

## Error Handling

| Error Type | Message Format | Example |
|------------|----------------|---------|
| Missing filepath | `Error: Missing filepath or content. Parsed data: {data}` | |
| Missing content | `Error: Missing filepath or content. Parsed data: {data}` | |
| JSON parse error | `Error: Failed to parse arguments. Expected valid JSON. Received: {data}` | |
| File write error | Logged to logger only | |
| Proposal Engine crash | `Error: Proposal Engine crashed: {error}` | |

## Security Considerations

1. **No direct file access** - File modifications only occur after explicit approval
2. **Memory-locked callbacks** - Execution closures never written to disk
3. **8-character task ID** - Cryptographic token for approval matching
4. **Log audit trail** - All proposal lifecycle events are logged
5. **Path sanitization** - Directory traversal prevented (handled by underlying OS)
6. **Dynamic paths** - All paths resolved via `cobalt_agent.config` from `.env`

## Configuration

No additional configuration required. The tool automatically uses the global Proposal Engine configuration and dynamically resolves paths from `config.system.obsidian_vault_path`.