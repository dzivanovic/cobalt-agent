# Ops Department (The Scribe)

## Overview
**File:** `src/cobalt_agent/brain/ops.py`

The `OpsDepartment` class serves as Cobalt's **Chief of Operations**—known as "The Scribe." It inherits from `BaseDepartment` and specializes in journaling, documentation formatting, playbook management, and Obsidian vault integration.

## Role: The Scribe
The Scribe is Cobalt's dedicated documentation expert with the following responsibilities:

| Responsibility | Description |
|----------------|-------------|
| **Journaling** | Records session logs, meeting notes, and operational summaries |
| **Documentation** | Formats technical content in pristine Markdown |
| **Playbook Management** | Reads and references operational playbooks |
| **Obsidian Integration** | Maintains the Obsidian vault through file operations |

> **Critical Distinction:** The Scribe does NOT write Python application code. It writes journals, summaries, reports, and documentation only.

## Class: OpsDepartment

### Description
The Scribe - Cobalt's Operations and Documentation department. Handles journaling, formatting, reading playbooks, and Obsidian integration.

### Constructor
```python
def __init__(self, system_prompt: Optional[str] = None)
```

**Parameters:**
- `system_prompt` (Optional[str]): Optional custom system prompt

**Default Name:** "The Scribe (Operations)"

## ReAct Loop Parameters

The Scribe operates within a strict **ReAct (Reason + Act)** loop with the following parameters:

### Tool Call Syntax
**MUST use exact syntax—no deviations allowed:**

| Format | Example | Status |
|--------|---------|--------|
| **CORRECT** | `ACTION: write_file {"filepath": "0 - Inbox/note.md", "content": "# Hello"}` | ✅ Accepted |
| **INCORRECT** | `{"filepath": "0 - Inbox/note.md", "content": "# Hello"}` | ❌ Missing ACTION prefix |
| **INCORRECT** | ```json\n{"filepath": "0 - Inbox/note.md", "content": "# Hello"}\n``` | ❌ Markdown code blocks forbidden |

### Behavioral Rules
1. **No Roleplay:** Output only the ACTION string when invoking tools
2. **Direct Execution:** Do not preface with "I will..." statements
3. **Clean Exit:** When task complete, output final text response without ACTION string

### Wait Protocol (Human-in-the-Loop)
When `write_file` returns *"Action paused. Proposal sent"*:

1. **STOP** all further tool calls
2. Output conversational confirmation: *"I have submitted the proposal for your approval."*
3. **DO NOT** attempt to write the file again

This enforces zero-trust approval workflows for file modifications.

## Available Tools

| Tool | Purpose | Syntax Example |
|------|---------|----------------|
| `read_file` | Read file contents | `ACTION: read_file {"filepath": "docs/file.md"}` |
| `list_directory` | List folder contents | `ACTION: list_directory {"directory_path": "0 - Inbox/"}` |
| `write_file` | Create or modify files (requires approval) | `ACTION: write_file {"filepath": "0 - Inbox/note.md", "content": "# Hello"}` |

### Obsidian Note Usage
For Obsidian vault operations, follow these conventions:

- **Inbox Path:** `0 - Inbox/note.md` (pending review)
- **Documentation Path:** `0 - Projects/Cobalt/...` (final destination)
- **Content Format:** Standard Markdown with YAML frontmatter where applicable

## Key Features

| Feature | Description |
|---------|-------------|
| **Documentation Expertise** | Specializes in clean, well-formatted Markdown documentation |
| **Strict Tool Syntax** | Enforces `ACTION:` prefix for all tool invocations |
| **Zero-Trust Workflow** | Respects human-in-the-loop approval for file modifications |
| **Markdown Focus** | Outputs pristine Markdown without code blocks or backticks |

## Inheritance
```
OpsDepartment → BaseDepartment
```

## See Also
- [`BaseDepartment`](brain_base.md) - Abstract base class for all departments
- [`EngineeringDepartment`](engineering.md) - Code generation department  
- [`Scribe`](scribe.md) - Skill class for Obsidian integration