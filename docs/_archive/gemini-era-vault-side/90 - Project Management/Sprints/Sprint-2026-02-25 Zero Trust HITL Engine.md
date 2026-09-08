---
title: "Sprint 2026-02-25: Zero Trust HITL Execution Engine"
date: 2026-02-25
sprint: 1
status: Complete
tags: [cobalt, sprint, hitl, security]
---

# Sprint 2026-02-25: Zero Trust HITL Execution Engine

## Overview

This sprint completed the foundational Zero Trust Human-in-the-Loop (HITL) Execution Engine, implementing memory-locked callbacks, Mattermost interceptors, and optimized ReAct loops for safe, auditable file modifications.

## Key Achievements

### 1. Zero Trust HITL: Air-Gapped Approval Workflow

Built an asynchronous, air-gapped approval workflow for file modifications. The LLM cannot write files directly; it must propose them via a Coat-Check ticket system.

**Implementation Details:**
- `ProposalEngine` class stores frozen Python execution callbacks in a shared class dictionary
- Callbacks are mapped to 8-character task IDs for secure retrieval
- File write operations are paused and require explicit human approval
- Approved proposals trigger callbacks that execute the actual file modifications

**Files Modified:**
- `src/cobalt_agent/core/proposals.py`

### 2. Memory-Locked Callbacks

Implemented `ProposalEngine.callbacks` as a shared class dictionary for storing frozen Python execution callbacks.

**Key Features:**
```python
class ProposalEngine:
    callbacks: Dict[str, Callable[[Proposal], None]] = {}
    
    def set_approval_callback(self, task_id: str, callback: Callable) -> None:
        self.callbacks[task_id] = callback
```

**Security Benefits:**
- Callbacks are stored in memory, not persisted to disk
- 8-character task ID provides cryptographic token for approval matching
- No direct file access until approval is received

### 3. Mattermost Interceptor

Updated the WebSocket listener to intercept messages starting with "Approve", bypassing the LLM entirely to execute secure RAM callbacks.

**Implementation:**
```python
# HITL APPROVAL INTERCEPTOR
text_lower = text.strip().lower()
if text_lower.startswith("approve") or text_lower.startswith("reject"):
    engine = ProposalEngine()
    result_msg = engine.handle_approval_response(text)
    self.send_message_to_channel_id(channel_id, result_msg)
    return
```

**Features:**
- Intercepts approval/reject messages before LLM processing
- Validates task ID format (8 characters)
- Executes RAM callbacks for approved proposals
- Ignores Mattermost system messages (joins, leaves, header updates)

**Files Modified:**
- `src/cobalt_agent/interfaces/mattermost.py`

### 4. Universal Tool Parser

Upgraded `ToolManager` and `WriteFileTool` to safely extract dictionary payloads using `ast.literal_eval` and prevent silent string-parsing errors.

**WriteFileTool Parsing:**
```python
# Universal extraction
data = query if query is not None else kwargs

if isinstance(data, str):
    try:
        data = json.loads(data)
    except Exception as e1:
        try:
            data = ast.literal_eval(data)
        except Exception as e2:
            logger.error(f"WriteFileTool parsing failed. JSON error: {e1} | AST error: {e2}")
            return f"Error: Failed to parse arguments. Received: {data}"
```

**Benefits:**
- Handles both JSON and Python dictionary string formats
- Graceful error handling with detailed error messages
- Prevents silent parsing failures

**Files Modified:**
- `src/cobalt_agent/tools/filesystem.py`
- `src/cobalt_agent/tools/tool_manager.py`

### 5. ReAct Loop Optimization

Added critical prompt rules to the Engineering prompt to:
- Stop infinite loops via the "Wait Protocol"
- Skip directory crawls when given exact file paths (context efficiency)

**Wait Protocol:**
```
6. WAIT PROTOCOL: If you use the `write_file` tool and the System Observation says "Action paused. Proposal sent", YOU MUST STOP. Output a final conversational message saying "I have submitted the proposal for your approval." DO NOT try to write the file again.
```

**Context Efficiency:**
```
5. WORKFLOW EFFICIENCY: If the user provides an exact filepath (e.g., "create a file at src/test.py"), DO NOT use `list_directory`. Execute `write_file` immediately to save context space.
```

**Files Modified:**
- `src/cobalt_agent/brain/engineering.py`

## Sprint Metrics

| Metric | Value |
|--------|-------|
| Sprint Duration | 2026-02-25 |
| Files Modified | 4 |
| New Features | 2 (HITL interceptor, memory-locked callbacks) |
| Bugs Fixed | N/A |
| Documentation Updated | 4 |

## Documentation Updates

- `docs/0 - Projects/Cobalt/00 - Master Plan/Developer Docs/proposals.md` - Updated with callbacks documentation
- `docs/0 - Projects/Cobalt/00 - Master Plan/Developer Docs/mattermost.md` - Updated with HITL interceptor documentation
- `docs/0 - Projects/Cobalt/00 - Master Plan/Developer Docs/filesystem.md` - Created new page for WriteFileTool
- `docs/0 - Projects/Cobalt/00 - Master Plan/Developer Docs/engineering.md` - Created new page for prompt rules

## Next Steps

- [ ] Add rejection handling documentation
- [ ] Document the callback execution flow in more detail
- [ ] Add integration testing for HITL workflow
- [ ] Create user-facing approval channel documentation