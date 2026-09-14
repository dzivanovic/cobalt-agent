---
title: "Main Entry Point Documentation"
status: Active
module: Core
type: Class
dependencies:
  - "[[llm]]"
  - "[[memory_core]]"
  - "[[cortex]]"
  - "[[cli]]"
  - "[[mattermost]]"
  - "[[scheduler]]"
  - "[[persona]]"
  - "[[prompt]]"
location: "src/cobalt_agent/main.py"
tags: [cobalt, dev_docs]
created: 2026-02-23
---

# Main Entry Point

## Overview
The main module serves as the entry point for the Cobalt Agent application. It initializes the system, loads configuration, and starts the agent's main loop or interactive interface.

## Class: `CobaltAgent`

### Constructor
```python
def __init__(self)
```
Initializes the Cobalt Agent with all core components.

### Key Components

#### Core System
- `config`: Global configuration from `configs/config.yaml` (via `get_config()`)
- `persona`: Agent identity and role configuration (`Persona` class)
- `memory`: Primary `PostgresMemory` with fallback to local `MemorySystem`
- `cortex`: Chief of Staff for routing requests to specialized departments
- `llm`: LLM instance for reasoning and response generation
- `prompt_engine`: Dynamic prompt builder with role-based context
- `tool_manager`: Tool registry and execution handler

#### Skills & Services
- `MorningBriefing`: Daily market briefing skill
- `DeepResearch`: Long-form research capability
- `CobaltScheduler`: Background task scheduler (heartbeat)

#### Interfaces
- `CLI`: Interactive command-line interface
- `MattermostInterface`: Real-time WebSocket integration

### Methods

#### `configure_logging() -> None`
Configures loguru with dual handlers:
- **Console**: INFO level, colored output
- **File**: Rotating daily logs in `logs/agent_YYYY-MM-DD.log`, 7-day retention

#### `main() -> None`
Main entry point for interactive CLI mode.

**Behavior:**
1. Configures logging
2. Instantiates `MorningBriefing` and `DeepResearch` skills
3. Starts `CobaltScheduler` (heartbeat)
4. Builds dynamic system prompt via `PromptEngine`
5. Initializes and starts `CLI` interface
6. On exit: graceful scheduler shutdown, saves memory

#### `process_input(text: str) -> str`
Processes incoming text with dual-path routing.

**Parameters:**
- `text`: Incoming message text

**Returns:**
- Response string from routed handler or LLM

**Flow:**
1. Attempts `Cortex` routing for specialized handling
2. Falls back to direct LLM chat with dynamic prompt

#### `send_message(message: str) -> str`
Sends a message and returns the LLM response.

**Parameters:**
- `message`: Text to send

**Returns:**
- Response string from LLM

#### `start_mattermost_interface() -> None`
Starts the Mattermost WebSocket listener for HITL workflows.

**Behavior:**
1. Connects to Mattermost server
2. Initializes `ProposalEngine` for HITL approval workflow
3. Attaches `Cortex` brain to interface
4. Enters blocking listen loop
5. On exit: disconnects, stops proposal monitoring, saves memory

## Command-Line Interface

### Usage
```bash
python -m cobalt_agent
# or
uv run python -m cobalt_agent
```

### Entry Points
- `main()`: Interactive CLI mode (default when run as script)
- `start_mattermost_interface()`: Mattermost WebSocket mode

## Environment Setup

### Required Variables
- `LLM_API_KEY`: API key for the LLM provider
- `MATTERMOST_TOKEN`: (Optional) Token for Mattermost integration

### Configuration Files
- `configs/config.yaml`: Main configuration (persona, system settings)
- `configs/strategies.yaml`: Trading strategy parameters
- `configs/rules.yaml`: Business rules and overrides

## Startup Flow (Script Execution)
1. Load `.env` environment variables
2. Initialize `CobaltAgent` instance
3. Start `CobaltScheduler` (heartbeat service)
4. Call `start_mattermost_interface()` for WebSocket mode
5. On shutdown: graceful scheduler termination, memory persistence

## Error Handling
- Database failures trigger fallback to local file-based `MemorySystem`
- Missing configuration handled with safe defaults
- LLM connection errors logged and retried
- Critical interface failures trigger graceful shutdown with state persistence

## Related Documentation
- [[cortex]] - Chief of Staff routing layer
- [[persona]] - Agent identity and role configuration
- [[scheduler]] - Background task heartbeat service
- [[cli]] - Interactive command-line interface
- [[mattermost]] - WebSocket integration layer