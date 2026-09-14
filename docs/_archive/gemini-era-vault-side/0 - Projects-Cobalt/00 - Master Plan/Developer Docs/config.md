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
The Configuration Management system provides type-safe, multi-source configuration for the Cobalt Agent using Pydantic Settings and YAML files. It supports environment variable overrides, vault-based secret injection, and Zero-Trust config routing for distributed node topology.

## Core Components

### Configuration Loading Priority (highest to lowest)
1. **Environment Variables** - via `.env` file and OS environment (using `COBALT_` prefix)
2. **Secure Vault** - AES-256 encrypted secrets dynamically injected at runtime via `COBALT_MASTER_KEY`
3. **YAML Configuration Files** - All `configs/*.yaml` files are merged alphabetically
4. **Default Values** - Pydantic model defaults

### Environment Variable Naming Convention
- Simple fields: `COBALT_SYSTEM__DEBUG_MODE` → `system.debug_mode`
- Nested fields: `COBALT_POSTGRES__HOST` → `postgres.host` (using `env_nested_delimiter="__"`)
- All environment variables must be prefixed with `COBALT_` to avoid conflicts

## Classes

### `CobaltSettings` (Main Configuration Class)
Pydantic Settings class that loads YAML config and allows ENV overrides.

**Configuration Source (in priority order):**
1. `.env` file and OS environment variables
2. Secure Vault (AES-256 encrypted, injected at runtime)
3. All YAML files in `configs/` directory (merged alphabetically)
4. Default values defined in Pydantic models

**Attributes:**
| Field | Type | Description |
|-------|------|-------------|
| `system` | `SystemConfig` | System-level configuration (debug, version, Obsidian vault path) |
| `llm` | `LLMConfig` | LLM provider settings (model name, API key) |
| `persona` | `PersonaConfig` | Agent persona (name, roles, skills, tone, directives) |
| `keys` | `Dict[str, Any]` | Decrypted secrets storage (runtime only, not persisted) |
| `trading_rules` | `Optional[TradingRules]` | Trading strategy parameters (momentum, RSI, ATR rules) |
| `active_profile` | `Optional[dict[str, str]]` | Active profile configuration |
| `models` | `Optional[dict[str, Any]]` | Model registry definitions |
| `network` | `Optional[NetworkConfig]` | Network topology for distributed nodes |
| `postgres` | `PostgresConfig` | PostgreSQL database configuration |
| `mattermost` | `MattermostConfig` | Mattermost communication settings |
| `vault` | `Optional[VaultConfig]` | Vault configuration (path, enabled flag) |
| `prompts` | `PromptsConfig` | Prompt templates for all system components |
| `browser` | `Optional[BrowserConfig]` | Browser/Playwright configuration (allowed domains) |
| `strategies` | `Optional[dict[str, StrategyConfig]]` | Strategy playbooks with filters, execution, scoring |
| `departments` | `Optional[dict[str, Any]]` | Cortex routing departments |

### Core Schema Definitions

#### `SystemConfig`
| Field | Type | Default | Description |
|-------|------|---------|-------------|
| `debug_mode` | `bool` | `False` | Enable debug logging |
| `version` | `str` | `"0.1.0"` | Application version |
| `obsidian_vault_path` | `str` | `"/Users/cobalt/cobalt/docs"` | Path to Obsidian vault (from `OBSIDIAN_VAULT_PATH` env) |

#### `LLMConfig`
| Field | Type | Default | Description |
|-------|------|---------|-------------|
| `model_name` | `str` | `"gemini/gemini-1.5-pro"` | LLM model identifier |
| `api_key` | `Optional[str]` | `None` | API key (from vault or env) |

#### `PersonaConfig`
| Field | Type | Default | Description |
|-------|------|---------|-------------|
| `name` | `str` | `"Cobalt"` | Agent name |
| `roles` | `list[str]` | `[]` | Agent roles |
| `skills` | `list[str]` | `[]` | Agent capabilities |
| `tone` | `list[str]` | `[]` | Communication tone |
| `directives` | `list[str]` | `[]` | Core behavioral rules |

#### `PostgresConfig`
| Field | Type | Default | Description |
|-------|------|---------|-------------|
| `host` | `str` | `"localhost"` | Database host (`COBALT_POSTGRES__HOST` or `POSTGRES_HOST`) |
| `port` | `int` | `5432` | Database port (`COBALT_POSTGRES__PORT` or `POSTGRES_PORT`) |
| `user` | `str` | `"postgres"` | Database user (`COBALT_POSTGRES__USER` or `POSTGRES_USER`) |
| `password` | `Optional[str]` | `None` | Database password (`COBALT_POSTGRES__PASSWORD` or `POSTGRES_PASSWORD`) |
| `db` | `str` | `"cobalt_memory"` | Database name (`COBALT_POSTGRES__DB` or `POSTGRES_DB`) |

#### `MattermostConfig`
| Field | Type | Default | Description |
|-------|------|---------|-------------|
| `url` | `Optional[str]` | `None` | Mattermost server URL |
| `token` | `Optional[str]` | `None` | Authentication token |
| `scheme` | `str` | `"http"` | URL scheme |
| `port` | `int` | `8065` | Server port |
| `approval_channel` | `str` | `"cobalt-approvals"` | HITL approval channel |
| `approval_team` | `str` | `"cobalt-team"` | HITL approval team |

#### `BrowserConfig`
| Field | Type | Default | Description |
|-------|------|---------|-------------|
| `allowed_domains` | `list[str]` | `["example.com"]` | Whitelist of allowed domains for browser automation |

#### `VaultConfig`
| Field | Type | Default | Description |
|-------|------|---------|-------------|
| `path` | `str` | `"data/.cobalt_vault"` | Vault file path |
| `enabled` | `bool` | `True` | Enable vault functionality |

#### `NetworkConfig`
| Field | Type | Default | Description |
|-------|------|---------|-------------|
| `nodes` | `dict[str, NodeConfig]` | Required | Network node definitions |

#### `NodeConfig`
| Field | Type | Default | Description |
|-------|------|---------|-------------|
| `role` | `str` | Required | Node role (e.g., "orchestrator", "worker") |
| `ip` | `str` | `"127.0.0.1"` | Node IP address |
| `port` | `int` | `8080` | Node port |
| `protocol` | `str` | `"http"` | Communication protocol |

### Trading Rules Schema

#### `MomentumRules`
| Field | Type | Description |
|-------|------|-------------|
| `rvol_alert_threshold` | `float` | RVOL alert threshold |
| `rvol_strong_threshold` | `float` | Strong RVOL threshold |

#### `RSIRules`
| Field | Type | Description |
|-------|------|-------------|
| `period` | `int` | RSI period |
| `overbought` | `int` | Overbought threshold |
| `oversold` | `int` | Oversold threshold |

#### `ATRRules`
| Field | Type | Description |
|-------|------|-------------|
| `period` | `int` | ATR period |
| `expansion_multiplier` | `float` | Expansion multiplier |
| `extension_multiplier` | `float` | Extension multiplier |

#### `TradingRules`
| Field | Type | Description |
|-------|------|-------------|
| `momentum` | `Optional[MomentumRules]` | Momentum trading rules |
| `moving_averages` | `Optional[dict]` | Moving average settings |
| `rsi` | `Optional[RSIRules]` | RSI rules |
| `atr` | `Optional[ATRRules]` | ATR rules |

### Strategy Configuration Schema

#### `StrategyTimeWindow`
| Field | Type | Description |
|-------|------|-------------|
| `start` | `str` | Strategy start time (ISO format) |
| `end` | `str` | Strategy end time (ISO format) |

#### `StrategyFiltersLiquidity`
| Field | Type | Description |
|-------|------|-------------|
| `min_average_daily_volume` | `int` | Minimum ADX volume requirement |
| `min_price` | `float` | Minimum price threshold |

#### `StrategyFiltersCorrelation`
| Field | Type | Description |
|-------|------|-------------|
| `check_sector` | `bool` | Enable sector correlation check |
| `check_spy` | `bool` | Enable SPY correlation check |

#### `StrategyFilters`
| Field | Type | Description |
|-------|------|-------------|
| `min_atr` | `Optional[float]` | Minimum ATR filter |
| `day1_close_zone` | `Optional[float]` | Day 1 close zone percentage |
| `max_gap` | `Optional[float]` | Maximum gap percentage |
| `min_rvol_day1` | `Optional[float]` | Minimum Day 1 RVOL |
| `trend_indicator` | `Optional[str]` | Trend indicator symbol |
| `baseline_indicator` | `Optional[str]` | Baseline indicator symbol |
| `min_volume_ratio` | `Optional[float]` | Minimum volume ratio |
| `pattern` | `Optional[str]` | Pattern type filter |
| `volume_break` | `Optional[str]` | Volume break pattern |
| `volume_retest` | `Optional[str]` | Volume retest pattern |
| `liquidity` | `Optional[StrategyFiltersLiquidity]` | Liquidity filters |
| `correlation` | `Optional[StrategyFiltersCorrelation]` | Correlation filters |

#### `StrategyExecution`
| Field | Type | Description |
|-------|------|-------------|
| `entry_trigger` | `Optional[str]` | Entry trigger condition |
| `stop_buffer` | `Optional[float]` | Stop loss buffer percentage |
| `target_multiplier` | `Optional[float]` | Target profit multiplier |
| `stop_rule` | `Optional[str]` | Stop rule definition |
| `target_rule` | `Optional[str]` | Target rule definition |
| `exit_strategy` | `Optional[str]` | Exit strategy type |

#### `StrategyScoring`
| Field | Type | Description |
|-------|------|-------------|
| `base_score` | `int` | Base strategy score |
| `high_rvol_threshold` | `float` | High RVOL threshold |
| `high_rvol_points` | `int` | Points for high RVOL |
| `base_rvol_points` | `int` | Base RVOL points |
| `gap_up_points` | `int` | Points for gap up |
| `live_rvol_multiplier` | `float` | Live RVOL multiplier |
| `spy_correlation_weight` | `float` | SPY correlation weight |
| `resistance_penalty` | `float` | Resistance penalty |
| `time_decay_per_min` | `float` | Time decay per minute |

#### `StrategyConfig`
| Field | Type | Description |
|-------|------|-------------|
| `name` | `str` | Strategy name (unique identifier) |
| `active` | `bool` | Enable/disable strategy |
| `direction` | `str` | Strategy direction (long/short) |
| `description` | `Optional[str]` | Strategy description |
| `time_window` | `StrategyTimeWindow` | Active time window |
| `filters` | `StrategyFilters` | Filter criteria |
| `execution` | `StrategyExecution` | Execution rules |
| `scoring` | `Optional[StrategyScoring]` | Scoring configuration |

### Prompts Schema

#### `PromptsConfig`
| Field | Type | Description |
|-------|------|-------------|
| `system` | `Optional[dict]` | System prompt template |
| `scheduler` | `Optional[dict]` | Scheduler prompt template |
| `ops` | `Optional[dict]` | Operations prompt template |
| `engineering` | `Optional[dict]` | Engineering prompt template |
| `proposal` | `Optional[dict]` | Proposal engine prompt template |
| `routing` | `Optional[dict]` | Zero-Trust routing prompt template |
| `orchestrator` | `Optional[dict]` | Orchestrator prompt template |
| `research` | `Optional[dict]` | Research module prompt template |

## Functions

### `load_config(config_dir: Optional[Path | str] = None) -> CobaltSettings`
Load configuration from YAML files and merge with environment variables.

**Parameters:**
- `config_dir`: Path to configuration directory (default: `configs/`)

**Returns:**
- `CobaltSettings`: Loaded configuration object with all sections validated

### `get_config() -> CobaltSettings`
Convenience function to get singleton configuration.

**Returns:**
- `CobaltSettings`: Current configuration instance

### `get_current_node_role() -> Optional[str]`
Determine the role of the current node based on network configuration in `config.yaml`.

**Returns:**
- `str`: Node role if found, otherwise `None`

### `parse_json_credentials(json_string: str) -> dict[str, Any]`
Parse JSON credentials string into a dictionary.

**Parameters:**
- `json_string`: JSON-formatted string containing credentials

**Returns:**
- `dict[str, Any]`: Parsed credentials dictionary

## Configuration File Structure

### YAML Files in `configs/`
All YAML files are merged alphabetically. Key files include:

**config.yaml** - Main configuration
```yaml
system:
  debug_mode: false
  version: "0.1.0"

llm:
  model_name: "gemini/gemini-1.5-pro"

persona:
  name: "Cobalt"
  roles: ["Market Analyst", "Trading Assistant"]

postgres:
  host: "localhost"
  port: 5432
  db: "cobalt_memory"

mattermost:
  url: "http://localhost:8065"
  approval_channel: "cobalt-approvals"

network:
  nodes:
    mainframe:
      role: "orchestrator"
      ip: "127.0.0.1"
      port: 8080

vault:
  path: "data/.cobalt_vault"
  enabled: true
```

**strategies.yaml** - Strategy playbooks with Zero-Trust routing
```yaml
strategies:
  gap_and_go:
    name: "Gap and Go"
    active: true
    direction: "long"
    time_window:
      start: "09:30"
      end: "16:00"
    filters:
      min_rvol_day1: 2.0
      pattern: "gap_up"
    execution:
      entry_trigger: "volume_confirmation"
```

**prompts.yaml** - Prompt templates (automatically nested under `prompts` section)
```yaml
system:
  role: "You are Cobalt, a financial AI agent..."

routing:
  system_prompt: "Route requests to appropriate department..."
```

## Zero-Trust Config Routing Structure

The system implements a Zero-Trust routing mechanism through the `prompts.routing` configuration section. This enables dynamic department-based request routing:

### Routing Configuration
```yaml
prompts:
  routing:
    system_prompt: |
      Analyze the request and route to the appropriate department.
      Available departments: {departments}
    department_mappings:
      engineering: ["code", "infrastructure", "deployment"]
      research: ["market analysis", "financial data", "scanners"]
```

### Node Role Detection
The `get_current_node_role()` function determines the current node's role by:
1. Reading `network.nodes` from `config.yaml`
2. Matching the local IP against configured node IPs
3. Returning the matched role (e.g., "orchestrator", "worker")

This enables distributed deployment where each node loads only the configuration relevant to its role.

## Vault Integration (Zero-Trust Security)

### Secret Injection Flow
1. On startup, if `COBALT_MASTER_KEY` is set, the vault is unlocked
2. Secrets are decrypted and injected into runtime configuration (RAM only)
3. Vault is immediately relocked after injection
4. Secrets are never persisted to disk

### Vault Key Mapping
| Vault Key | Injected Into |
|-----------|---------------|
| `MATTERMOST_CREDS` (JSON) | `mattermost.url`, `mattermost.token` |
| `openai_api_key` | `llm.api_key` |
| `anthropic_api_key` | `llm.api_key` |
| `gemini_api_key` | `llm.api_key` |
| `openrouter_api_key` | `llm.api_key` |

## Error Handling
- Invalid YAML files are logged and skipped with warnings
- Missing configuration files fall back to defaults
- Environment variable parsing errors are logged via `loguru`
- Configuration validation errors return default `CobaltSettings()` instance
- Vault unlock failures result in degraded (unsecure) mode with warnings

## Usage Example

```python
from cobalt_agent.config import get_config

# Load configuration
config = get_config()

# Access settings
print(f"Debug mode: {config.system.debug_mode}")
print(f"LLM Model: {config.llm.model_name}")
print(f"Postgres Host: {config.postgres.host}")

# Check node role
from cobalt_agent.config import get_current_node_role
role = get_current_node_role()
print(f"Current node role: {role}")

# Unlock vault with master key
from cobalt_agent.config import Config
config_instance = Config.get_instance()
config_instance.unlock_vault(master_key="your-fernet-key")