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
The `PromptEngine` class constructs dynamic system prompts for the Cobalt Agent. It assembles structured templates that define agent identity, operational context, memory protocols, directives, and tool capabilities. The engine ensures consistent LLM behavior through carefully formatted prompt templates.

## Class: `PromptEngine`

### Constructor
```python
def __init__(self, persona_config: PersonaConfig)
```
Initializes the Prompt Engine with a `PersonaConfig` instance containing agent identity parameters.

**Parameters:**
- `persona_config`: `PersonaConfig` instance from `cobalt_agent.config`, providing:
  - `name`: Agent identity name
  - `roles`: List of agent roles (e.g., "Financial Analyst", "Quantitative Researcher")
  - `tone`: List of tone descriptors (e.g., "professional", "concise")
  - `directives`: List of custom operational directives

---

## System Prompt Construction Flow

The `build_system_prompt()` method orchestrates template assembly through five distinct phases:

```
┌─────────────────────┐
│  build_system_prompt│
│    (persona_config) │
└──────────┬──────────┘
           │
    ┌──────▼───────┐
    │ 1. Identity  │ ← Agent name, roles, tone
    └──────┬───────┘
           │
    ┌──────▼───────────┐
    │ 2. Core Directives│ ← Operational rules, constraints
    └──────┬───────────┘
           │
    ┌──────▼──────────┐
    │ 3. Memory Protocol│ ← Context handling instructions
    └──────┬──────────┘
           │
    ┌──────▼─────────────┐
    │ 4. Tool Capabilities│ ← Available functions summary
    └──────┬─────────────┘
           │
    ┌──────▼────────────┐
    │ 5. Output Format  │ ← Response structure guidelines
    └───────────────────┘
```

---

## Method: `build_system_prompt()`

### Purpose
Constructs a complete system prompt by combining persona configuration with predefined template sections. This method is the primary entry point for generating LLM instructions.

### Implementation Details
The method follows a sequential assembly pattern:

1. **Identity Section**: Injects agent name, roles, and tone from `persona_config`
2. **Core Directives**: Appends operational rules and behavioral constraints
3. **Memory Protocol**: Adds instructions for context management and state awareness
4. **Tool Capabilities**: Summarizes available tool functions and their purposes
5. **Output Format**: Defines expected response structure and formatting requirements

### Return Value
Returns a formatted string containing the complete system prompt ready for LLM consumption.

---

## Template Construction Principles

### 1. Modular Sections
Each prompt component is isolated into distinct sections, enabling:
- Easy maintenance and updates
- Reusability across different agent configurations
- Clear separation of concerns

### 2. Dynamic Context Injection
Templates support variable substitution for:
- Agent persona attributes (name, roles, tone)
- Operational directives from configuration
- Runtime context parameters

### 3. Structured Formatting
The prompt structure follows a consistent hierarchy:
```markdown
# [AGENT NAME] - [ROLES]

## Identity
- Tone: [TONE DESCRIPTORS]

## Core Directives
[OPERATIONAL RULES]

## Memory Protocol
[CONTEXT HANDLING INSTRUCTIONS]

## Capabilities
[AVAILABLE TOOLS AND FUNCTIONS]

## Output Format
[RESPONSE STRUCTURE GUIDELINES]
```

---

## System Instruction Formatting

### Header Section
The system prompt begins with a clear identity declaration:
```
# [Agent Name] - [Primary Role]

Tone: [tone descriptors joined by commas]
```

### Directive Blocks
Operational directives are formatted as bulleted lists:
```markdown
## Core Directives
- [Directive 1]
- [Directive 2]
```

### Memory Protocol Instructions
Context handling guidelines are presented as structured instructions:
```markdown
## Memory Protocol
- Maintain awareness of conversation history
- Reference relevant context from previous exchanges
- Preserve state across interactions
```

---

## Dynamic Context Handling

The PromptEngine supports dynamic context injection through:

### Variable Substitution
Templates use Python f-string formatting for variable interpolation:
```python
f"# {self.persona_config.name} - {', '.join(self.persona_config.roles)}"
```

### Context Assembly
Dynamic context is assembled by:
1. Extracting relevant persona attributes
2. Formatting according to template structure
3. Concatenating sections with consistent delimiters

---

## Integration Points

### With Persona Module
The PromptEngine depends on `PersonaConfig` from `cobalt_agent.persona`:
```python
from cobalt_agent.config import PersonaConfig

class PromptEngine:
    def __init__(self, persona_config: PersonaConfig):
        self.persona_config = persona_config
```

### With LLM Interface
Generated prompts are passed to the LLM service:
```python
system_prompt = prompt_engine.build_system_prompt()
response = llm.generate(system_prompt=system_prompt, user_input=user_message)
```

---

## Best Practices

1. **Configuration-Driven Prompts**: All prompt content should derive from configuration files, not hardcoded strings
2. **Consistent Formatting**: Maintain uniform section headers and delimiter patterns
3. **Documentation**: Keep template sections well-documented for maintainability
4. **Testing**: Validate prompt output against expected structure and content requirements

---

## Example Output Structure

```
# Cobalt - Financial Analyst, Quantitative Researcher

Tone: professional, concise, analytical

## Core Directives
- Provide accurate financial analysis
- Cite sources for data points
- Maintain objectivity in recommendations

## Memory Protocol
- Track conversation context
- Reference prior discussions when relevant
- Maintain state across sessions

## Capabilities
- Browser automation for web research
- Financial data extraction and analysis
- Document processing and summarization

## Output Format
- Use markdown for formatting
- Structure responses with clear headings
- Include actionable recommendations when applicable
```

---

## Related Documentation
- [[persona]] - Agent persona configuration and management
- [[llm]] - LLM interface and generation capabilities
- [[config]] - Configuration loading and management