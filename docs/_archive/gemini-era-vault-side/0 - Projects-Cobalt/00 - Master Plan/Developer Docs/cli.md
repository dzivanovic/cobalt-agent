---
title: "CLI Interface Documentation"
status: Active
module: Interface
type: Class
dependencies:
  - "[[main]]"
  - "[[memory_core]]"
  - "[[tool_manager]]"
  - "[[cortex]]"
location: "src/cobalt_agent/interfaces/cli.py"
tags: [cobalt, dev_docs]
created: 2026-02-23
---

# CLI Interface Module

**Location:** `src/cobalt_agent/interfaces/cli.py`

## Overview

Interactive Command-Line Interface for Cobalt Agent with centralized routing and RAG (Retrieval Augmented Generation).

## Class: `CLI`

Interactive command-line interface for Cobalt Agent.

### Constructor

```python
CLI(memory_system, llm, system_prompt, tool_manager, cortex=None)
```

**Parameters:**
- `memory_system`: Memory system for storing conversation history
- `llm`: LLM instance for inference
- `system_prompt`: System prompt for the agent
- `tool_manager`: ToolManager instance for tool execution
- `cortex`: Optional Cortex instance for routing

### Methods

#### `start()`
Start the interactive CLI loop. Displays agent info and prompts for user input.

#### `_handle_chat(user_input: str)`
Autonomous Agent Loop (ReAct Pattern) for general analysis.

1. Retrieve long-term memory (RAG)
2. Inject memory into system prompt
3. Run LLM with tool execution loop (max 5 turns)
4. Handle tool calls and observations

#### `_retrieve_long_term_memory(query: str) -> str`
Fetches relevant past memories from the memory system for RAG.

**Parameters:**
- `query`: User query to search for relevant memories

**Returns:** Formatted string of top 5 unique memories

#### `_format_tool_output(output: Any) -> str`
Helper to convert Pydantic models/Lists to clean strings.

---

## Features

- **Centralized Routing**: Delegates to Cortex for specialized tasks
- **RAG Integration**: Retrieves relevant long-term memory for context
- **Auto-Tool**: LLM can trigger tool calls automatically
- **Memory Management**: Maintains short-term RAM (10 entries) and long-term storage

---

## Usage

```python
from cobalt_agent.interfaces.cli import CLI

cli = CLI(memory_system, llm, system_prompt, tool_manager, cortex)
cli.start()