---
title: "Configuration Management Documentation"
status: Active
module: Core
type: Class
dependencies:
  - "[[persona]]"
location: "src/cobalt_agent/config.py"
tags: [cobalt, dev_docs]
created: 2026-02-23
---

# Configuration Management

## Overview
The Configuration Management system provides type-safe, multi-source configuration for the Cobalt Agent using Pydantic Settings and YAML files. It supports environment variable overrides and dynamic config loading.

## Core Components

### Configuration Loading Priority
1. **Environment Variables** (highest priority) - Strictly for node/Docker specific data like `POSTGRES_HOST`, `NODE_ID`, etc.
2. **Secure Vault** (dynamically injected) - API keys and tokens injected from the VaultManager at runtime
3. **YAML Configuration Files** (configs/*.yaml) - Static configuration like `trading_rules`, `persona`, etc.
4. **Default Values** (lowest priority)

### Environment Variable Mapping
- Simple fields: `UPPER_CASE` converts to `lower_case_with_underscores`
- Nested fields: `POSTGRES_HOST` maps to `postgres.host` via `env_nested_delimiter="_"`

## Classes

### `CobaltSettings` (Main Configuration Class)
The primary configuration class that loads from YAML and environment variables.

**Configuration Source (in priority order):**
1. `.env` file and OS environment variables (for node-specific values)
2. Secure Vault (AES-256 encrypted, injected at runtime via `COBALT_MASTER_KEY`)
3. `configs/config.yaml` and other YAML files (static configuration)
4. Default values defined in Pydantic models

**Attributes:**
- `system`: System-level configuration
- `llm`: LLM provider settings
- `persona`: Agent personality and behavior
- `trading_rules`: Trading strategy parameters
- `postgres`: PostgreSQL database settings
- `mattermost`: Mattermost communication settings

### `SystemConfig`
System-level configuration settings.

| Field | Type | Default | Description |
|-------|------|---------|-------------|
| `debug_mode` | `bool` | `False` | Enable debug logging |
| `version` | `str` | `"0.1.0"` | Application version |
| `obsidian_vault_path` | `str` | `"/default/obsidian/vault/path"` | Path to Obsidian vault |

### `LLMConfig`
Universal Model Registry configuration. The system now uses a single frontier-class local Mixture of Experts model via LM Studio.

| Field | Type | Default | Description |
|-------|------|---------|-------------|
| `model_name` | `str` | `"mainframe"` | Local MoE model identifier (Qwen 3.5 122B) |
| `api_key` | `str` | Required | LM Studio API key (`LM_STUDIO_API_KEY`) |
| `base_url` | `str` | `"http://localhost:1234/v1"` | LM Studio endpoint |
| `temperature` | `float` | `0.7` | Reasoning temperature for consistent outputs |
| `max_tokens` | `int` | `-1` | Unlimited token budget for deep reasoning |

### `PersonaConfig`
Agent persona configuration.

| Field | Type | Default | Description |
|-------|------|---------|-------------|
| `name` | `str` | `"Cobalt"` | Agent name |
| `roles` | `list[str]` | `[]` | Agent roles |
| `skills` | `list[str]` | `[]` | Agent capabilities |
| `tone` | `list[str]` | `[]` | Communication tone |
| `directives` | `list[str]` | `[]` | Core behavioral rules |

### `PostgresConfig`
PostgreSQL database connection settings.

| Field | Type | Default | Description |
|-------|------|---------|-------------|
| `host` | `str` | `"localhost"` | Database host |
| `port` | `int` | `5432` | Database port |
| `db` | `str` | `"cobalt_memory"` | Database name |
| `user` | `str` | `"postgres"` | Database user |
| `password` | `Optional[str]` | `None` | Database password |

### `MattermostConfig`
Mattermost communication settings.

| Field | Type | Default | Description |
|-------|------|---------|-------------|
| `url` | `Optional[str]` | `None` | Mattermost URL |
| `token` | `Optional[str] | `None` | Authentication token |
| `scheme` | `str` | `"http"` | URL scheme |
| `port` | `int` | `8065` | Port number |

## Functions

### `load_config(config_dir: Optional[Path | str] = None) -> CobaltSettings`
Load configuration from YAML files and merge with environment variables.

**Parameters:**
- `config_dir`: Path to configuration directory (default: `configs/`)

**Returns:**
- `CobaltSettings`: Loaded configuration

### `get_config() -> CobaltSettings`
Convenience function to get singleton configuration.

**Returns:**
- `CobaltSettings`: Current configuration

### `get_current_node_role() -> Optional[str]`
Determine the role of the current node based on network configuration.

**Returns:**
- `str`: Node role if found, otherwise `None`

## Configuration File Structure

### `configs/config.yaml`
Main configuration file with the following sections:

```yaml
system:
  debug_mode: false
  version: "0.1.0"
  obsidian_vault_path: "/path/to/vault"

llm:
  model_name: "mainframe"
  api_key: "${LM_STUDIO_API_KEY}"
  base_url: "http://localhost:1234/v1"
  temperature: 0.7
  max_tokens: -1

persona:
  name: "Cobalt"
  roles:
    - "Market Analyst"
    - "Trading Assistant"
  tone:
    - "Professional"
    - "Analytical"
  directives:
    - "Use tools for real-time data"
    - "Trust tool results over assumptions"

postgres:
  host: "localhost"
  port: 5432
  db: "cobalt_memory"

mattermost:
  url: "https://mattermost.example.com"
  token: "${MATTERMOST_TOKEN}"
```

## Error Handling
- Invalid YAML files are logged and skipped
- Missing configuration files use defaults
- Environment variable parsing errors are logged
- Configuration validation errors are caught and reported