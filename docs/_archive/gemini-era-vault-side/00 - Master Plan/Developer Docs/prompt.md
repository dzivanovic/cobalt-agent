---
title: "Prompt Engine Documentation"
status: Active
module: Brain
type: Class
dependencies:
  - "[[main]]"
  - "[[persona]]"
  - "[[llm]]"
location: "src/cobalt_agent/prompt.py"
tags: [cobalt, dev_docs]
created: 2026-02-23
---

# Prompt Engine

## Overview
The Prompt Engine constructs dynamic system prompts for the LLM based on context, tools, and temporal information. It ensures the agent maintains proper behavior, memory protocol, and tool usage guidelines.

## Class: `PromptEngine`

### Constructor
```python
def __init__(self, persona_config: PersonaConfig)
```
Initializes the Prompt Engine with persona configuration.

**Parameters:**
- `persona_config`: `PersonaConfig` instance containing agent identity and directives

### Main Methods

#### `build_system_prompt(tools: List[Any] = None) -> str`
Constructs the complete system prompt by combining all components.

**Parameters:**
- `tools`: Optional list of tool objects available to the agent

**Returns:**
- `str`: Complete system prompt

**Components:**
1. Identity & Role (Header)
2. Operational Context (Time/Date)
3. Memory Protocol
4. Directives (Rules)
5. Tool Capabilities

## Prompt Components

### 1. Header (`_build_header()`)
Contains agent identity information:
- Agent name
- Roles
- Directives
- Tone

**Format:**
```
### IDENTITY
You are {name}.

### ROLES
Your roles are: {roles}.

### OPERATIONAL DIRECTIVES
{directives}

### TONE
Maintain a tone that is: {tone}.
```

### 2. Context (`_build_context()`)
Provides temporal and environmental context:
- Current date/time
- Operating system
- User identity

### 3. Memory Protocol (`_build_memory_protocol()`)
Defines rules for memory recall and stale data handling:
- **PREFERENCE** memories: Keep forever (e.g., "I like TSLA")
- **MARKET CONTEXT** memories: Expire after 24 hours
- Instructions to use memory when available

### 4. Directives (`_build_directives()`)
Core operating rules:
- Agent is autonomous (not a chat bot)
- Must use tools for real-time data
- Strict data adherence (no hallucination)
- Tool usage format (ACTION: syntax)

### 5. Tool Descriptions (`_build_tool_descriptions()`)
Lists available tools with their capabilities for the LLM.

## Tool Usage Protocol

### Action Format
The agent must use the `ACTION:` prefix when invoking tools:

```
User: What is the price of Apple?
You: ACTION: finance AAPL
System: [Observation: AAPL is $150]
You: Apple is trading at $150.
```

### Key Rules
1. **No internal knowledge**: Cannot answer without tools
2. **Start with ACTION:** When data is needed
3. **Trust tool results**: Use provided values, don't interpret
4. **Strict data adherence**: Reference exact periods from tool data (e.g., "RSI (20)", not "RSI (14)")

## Configuration Integration
The Prompt Engine uses `PersonaConfig` from the global configuration system, ensuring consistency across the agent's behavior and documentation.

## Example Output
```python
engine = PromptEngine(persona_config)
prompt = engine.build_system_prompt(tools=[search_tool, finance_tool])
print(prompt)
# Full system prompt for LLM