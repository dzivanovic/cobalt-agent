# Ops Department (The Scribe)

## Overview
`cobalt_agent/brain/ops.py`

The `OpsDepartment` class is Cobalt's Operations and Documentation department. It inherits from `BaseDepartment` and handles journaling, formatting, reading playbooks, and Obsidian integration.

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

### System Prompt
The department uses a default prompt that enforces strict rules:

**CRITICAL RULES:**
1. You are a documentation expert. Use pristine Markdown formatting.
2. You do not write Python or application code. You write journals, summaries, and reports.
3. **YOU MUST USE THE EXACT SYNTAX BELOW TO CALL A TOOL:**
   - **CORRECT:** `ACTION: write_file {"filepath": "0 - Inbox/note.md", "content": "# Hello"}`
   - **INCORRECT:** `{"filepath": "0 - Inbox/note.md", "content": "# Hello"}`
   - **INCORRECT:** ```json\n{"filepath": "0 - Inbox/note.md", "content": "# Hello"}\n```
4. DO NOT roleplay. DO NOT say "I will create the note now." Just output the ACTION string.
5. **WAIT PROTOCOL:** If you use the `write_file` tool and the System Observation says "Action paused. Proposal sent", YOU MUST STOP. Output a final conversational message saying "I have submitted the proposal for your approval." DO NOT try to write the file again.

### Available Tools
- `read_file`: Reads a file. Syntax: `ACTION: read_file {"filepath": "docs/file.md"}`
- `list_directory`: Lists a folder. Syntax: `ACTION: list_directory {"directory_path": "0 - Inbox/"}`
- `write_file`: Modifies or creates a file. Syntax: `ACTION: write_file {"filepath": "0 - Inbox/note.md", "content": "# Hello"}`

### Inheritance
Extends `BaseDepartment` with specialized operations-focused system prompt.

## Key Features
- **Documentation Expertise:** Specializes in creating clean, well-formatted documentation
- **Tool Call Syntax:** Enforces strict ACTION: prefix for tool calls
- **Zero-Trust Workflow:** Respects human-in-the-loop approval for file modifications

## See Also
- `BaseDepartment` - Abstract base class for all departments
- `EngineeringDepartment` - Code generation department
- `Scribe` - Skill class for Obsidian integration