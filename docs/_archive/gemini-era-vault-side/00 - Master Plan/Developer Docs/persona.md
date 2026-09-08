# Persona System

## Overview
`cobalt_agent/persona.py`

The `Persona` class manages the AI agent's identity, roles, skills, and behavioral directives. It generates system prompts for the LLM.

## Class: PersonaConfig (Pydantic Model)

### Description
Configuration for the agent's persona.

### Fields
- `name` (str): Agent name, default "Cobalt"
- `roles` (List[str]): List of roles the agent fulfills
- `skills` (List[str]): List of agent skills and capabilities
- `tone` (List[str]): Communication tone characteristics
- `directives` (List[str]): Core behavioral directives

## Class: Persona

### Description
Persona class that manages the AI agent's identity and generates system prompts.

### Constructor
```python
def __init__(self, config: PersonaConfig)
```

**Parameters:**
- `config` (PersonaConfig): Configuration containing persona settings

Initializes and logs the persona name.

### Methods

#### get_system_prompt
```python
def get_system_prompt() -> str
```

Generate a comprehensive system prompt combining all persona attributes.

**Returns:** Complete system instruction string for the AI agent

**Prompt Structure:**
1. Introduction with agent name
2. ROLES section
3. SKILLS section
4. COMMUNICATION STYLE section
5. CORE DIRECTIVES section
6. Mission statement

#### create_override
```python
def create_override(self, name: str, roles: List[str], directives: List[str]) -> "Persona"
```

Create a new Persona instance with temporary overrides for Split-Brain agents.

**Parameters:**
- `name` (str): The new name for the override persona
- `roles` (List[str]): List of roles for the override persona
- `directives` (List[str]): List of directives for the override persona

**Returns:** A new Persona instance with the specified overrides

**Use Case:** This strips away irrelevant global rules (like trading logic) for specialized tasks.

#### __repr__
```python
def __repr__() -> str
```

String representation of the Persona.

**Format:** `Persona(name='Cobalt', roles=X, skills=Y)`

## Key Components
- `PersonaConfig`: Pydantic model for structured configuration
- `get_system_prompt()`: Generates full instruction string
- `create_override()`: Creates specialized agent personas

## Split-Brain Architecture
The persona system supports the Split-Brain architecture by:
1. Allowing override personas that strip away global rules
2. Enabling specialized roles for different tasks
3. Maintaining consistent identity across operations

## See Also
- `OrchestratorEngine` - Coordinates Split-Brain architecture
- `BrainBase` - ReAct execution engine
- `OpsDepartment` - Documentation-focused drone