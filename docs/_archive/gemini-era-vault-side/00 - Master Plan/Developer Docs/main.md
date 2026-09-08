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
Initializes the Cobalt Agent with all components.

### Key Components

#### Core System
- `config`: Global configuration from `configs/config.yaml`
- `llm`: LLM instance for reasoning
- `cortex`: Chief of Staff for routing requests to departments
- `memory`: Memory system for storing and retrieving conversation history

#### Departments
- `Tactical`: Market data and trading strategies (Strategos)
- `Intel`: Research and news analysis
- `Ops`: Logging and documentation (Scribe)
- `Engineering`: Development tools and utilities

#### Interfaces
- `CLI`: Command-line interface
- `Mattermost`: Real-time chat integration

### Main Methods

#### `run() -> None`
Starts the main agent loop.

**Behavior:**
- Loads configuration
- Initializes all components
- Starts interactive loop or service

#### `route(user_input: str) -> Optional[str]`
Convenience method to route input through Cortex.

**Parameters:**
- `user_input`: User's message or command

**Returns:**
- Response from the appropriate department

## Command-Line Interface

### Usage
```bash
python -m cobalt_agent
# or
uv run python -m cobalt_agent
```

### Options
- `--debug`: Enable debug logging
- `--config-dir`: Specify custom configuration directory

## Environment Setup

### Required Variables
- `LLM_API_KEY`: API key for the LLM provider
- `MATTERMOST_TOKEN`: (Optional) Token for Mattermost integration

### Configuration Files
- `configs/config.yaml`: Main configuration
- `configs/strategies.yaml`: Trading strategy parameters
- `configs/rules.yaml`: Business rules and overrides

## Startup Flow
1. Load `.env` file
2. Load YAML configuration files
3. Initialize LLM
4. Initialize Memory System
5. Initialize Cortex (Chief of Staff)
6. Register Departments
7. Register Tools
8. Start CLI or Mattermost listener

## Error Handling
- Missing configuration defaults to safe values
- LLM connection failures are logged and retried
- Department initialization failures are logged
- Agent continues with partial functionality when possible