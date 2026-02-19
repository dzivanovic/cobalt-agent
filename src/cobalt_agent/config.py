"""
Configuration Management for Cobalt Agent
Pydantic Settings-based configuration with environment variable overrides.

Loading Priority (highest to lowest):
1. Environment Variables (via .env file and OS env)
2. YAML Configuration Files (configs/*.yaml)

Environment Variable Mapping:
- Simple fields: UPPER_CASE converts to lower_case_with_underscores
- Nested fields: NODES_CORTEX_IP maps to network.nodes.cortex.ip
"""

import os
from pathlib import Path
from typing import List, Optional, Dict, Any
from collections.abc import Mapping

import yaml
from dotenv import load_dotenv
from loguru import logger
from pydantic import BaseModel, Field, ConfigDict
from pydantic_settings import BaseSettings, PydanticBaseSettingsSource

# Load environment variables from .env file
load_dotenv()


# --- 1. Modular Schema Definitions ---


class MomentumRules(BaseModel):
    """Schema for momentum trading rules."""
    rvol_alert_threshold: float
    rvol_strong_threshold: float


class RSIRules(BaseModel):
    """Schema for RSI trading rules."""
    period: int
    overbought: int
    oversold: int


class ATRRules(BaseModel):
    """Schema for ATR trading rules."""
    period: int
    expansion_multiplier: float
    extension_multiplier: float


class TradingRules(BaseModel):
    """
    Schema for 'trading_rules' section.
    We are strict here to ensure trading logic is type-safe.
    """
    momentum: Optional[MomentumRules] = None
    moving_averages: Optional[dict] = None
    rsi: Optional[RSIRules] = None
    atr: Optional[ATRRules] = None


class SystemConfig(BaseModel):
    """Schema for system-level configuration."""
    debug_mode: bool = False
    version: str = "0.1.0"
    obsidian_vault_path: str = "/default/obsidian/vault/path"


class LLMConfig(BaseModel):
    """Schema for LLM configuration."""
    model_name: str = "gemini/gemini-1.5-pro"
    api_key: Optional[str] = None


class PersonaConfig(BaseModel):
    """Schema for agent persona configuration."""
    name: str = "Cobalt"
    roles: List[str] = Field(default_factory=list)
    skills: List[str] = Field(default_factory=list)
    tone: List[str] = Field(default_factory=list)
    directives: List[str] = Field(default_factory=list)


class NodeConfig(BaseModel):
    """Schema for network node configuration."""
    role: str
    ip: str = "127.0.0.1"
    port: int = 8080
    protocol: str = "http"


class NetworkConfig(BaseModel):
    """Schema for network topology configuration."""
    nodes: Dict[str, NodeConfig]


# --- 2. Main Configuration Class with ENV Override Support ---


class CobaltSettings(BaseSettings):
    """
    Pydantic Settings class that loads YAML config and allows ENV overrides.
    
    Environment variable naming convention:
    - Top-level keys: UPPER_SNAKE_CASE
    - Nested keys: NODES_CORTEX_IP (all caps, dots -> underscores)
    
    YAML is loaded first, then ENV variables recursively override values.
    """
    model_config = ConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="allow",  # Allow extra fields not defined in schema
    )

    # Core Sections
    system: SystemConfig = Field(default_factory=SystemConfig)
    llm: LLMConfig = Field(default_factory=LLMConfig)
    persona: PersonaConfig = Field(default_factory=PersonaConfig)
    
    # Optional Known Sections
    trading_rules: Optional[TradingRules] = None
    active_profile: Optional[Dict[str, str]] = None
    models: Optional[Dict[str, Any]] = None
    network: Optional[NetworkConfig] = None

    @classmethod
    def settings_customise_sources(
        cls,
        settings_cls: type[BaseSettings],
        init_settings: PydanticBaseSettingsSource,
        env_settings: PydanticBaseSettingsSource,
        dotenv_settings: PydanticBaseSettingsSource,
        file_secret_settings: PydanticBaseSettingsSource,
    ) -> tuple[PydanticBaseSettingsSource, ...]:
        """
        Custom source order: ENV overrides YAML config.
        We load YAML first, then ENV overrides.
        """
        return (init_settings, env_settings, dotenv_settings, file_secret_settings)


# --- 3. Configuration Loader with YAML + ENV Merging ---


def _load_yaml_config(yaml_path: Path) -> Dict[str, Any]:
    """Load and return YAML configuration as dictionary."""
    if not yaml_path.exists():
        logger.warning(f"Config file not found: {yaml_path}")
        return {}
    
    try:
        with open(yaml_path, "r") as f:
            return yaml.safe_load(f) or {}
    except Exception as e:
        logger.error(f"Failed to load {yaml_path}: {e}")
        return {}


def _merge_yaml_with_env(yaml_data: Dict[str, Any]) -> Dict[str, Any]:
    """
    Merge YAML data with environment variables.
    ENV variables take precedence and recursively override YAML values.
    
    Supported ENV variable formats:
    - SYSTEM_DEBUG_MODE -> system.debug_mode
    - SYSTEM_OBSIDIAN_VAULT_PATH -> system.obsidian_vault_path
    - NETWORK_NODES_CORTEX_IP -> network.nodes.cortex.ip
    - NETWORK_NODES_CORTEX_PORT -> network.nodes.cortex.port
    - COBALT_CORTEX_IP -> network.nodes.cortex.ip (special case)
    - COBALT_VAULT_PATH -> system.obsidian_vault_path (special case)
    """
    # Get all environment variables
    env_vars = {k: v for k, v in os.environ.items() if k.isupper()}
    
    result = yaml_data.copy()
    
    # Special cases for Cobalt-specific environment variables
    special_cases = {
        "COBALT_CORTEX_IP": ("network", ["nodes", "cortex", "ip"]),
        "COBALT_CORTEX_PORT": ("network", ["nodes", "cortex", "port"]),
        "COBALT_VAULT_PATH": ("system", ["obsidian_vault_path"]),
    }
    
    # Process special cases first
    for env_key, (root_key, nested_path) in special_cases.items():
        if env_key in env_vars:
            env_value = env_vars[env_key]
            if root_key in yaml_data:
                current = result[root_key]
                for part in nested_path[:-1]:
                    if isinstance(current, dict) and part not in current:
                        current[part] = {}
                    current = current.get(part, {})
                
                if isinstance(current, dict) and nested_path[-1] not in ["", None]:
                    current[nested_path[-1]] = _convert_env_value(env_value)
                    logger.debug(f"ENV override (special): {env_key} -> {env_value}")
    
    # Process each ENV variable
    for env_key, env_value in env_vars.items():
        # Skip special cases that were already processed
        if env_key in special_cases:
            continue
            
        # Convert ENV key to nested path
        # e.g., NETWORK_NODES_CORTEX_IP -> ["network", "nodes", "cortex", "ip"]
        parts = env_key.lower().split("_")
        
        # Skip if not enough parts for nested path
        if len(parts) < 2:
            continue
        
        # Determine the root key and nested path
        # Handle special case: SYSTEM_ prefix
        if parts[0] == "system":
            root_key = "system"
            nested_path = parts[1:]
        elif parts[0] == "network":
            root_key = "network"
            nested_path = parts[1:]
        elif parts[0] == "llm":
            root_key = "llm"
            nested_path = parts[1:]
        elif parts[0] == "persona":
            root_key = "persona"
            nested_path = parts[1:]
        elif parts[0] == "trading":
            root_key = "trading_rules"
            nested_path = parts[1:]
        else:
            # General case: treat first part as root key
            root_key = parts[0]
            nested_path = parts[1:]
        
        # Skip if root key not in yaml_data
        if root_key not in yaml_data:
            continue
        
        # Navigate/create nested structure and set value
        current = result[root_key]
        
        # If nested_path is empty, set value directly on root
        if not nested_path:
            result[root_key] = _convert_env_value(env_value)
            continue
        
        # Navigate to the target location
        path_parts = nested_path[:-1]
        target_key = nested_path[-1]
        
        try:
            for part in path_parts:
                if isinstance(current, dict):
                    if part not in current:
                        current[part] = {}
                    current = current[part]
                else:
                    break
            
            if isinstance(current, dict):
                current[target_key] = _convert_env_value(env_value)
                logger.debug(f"ENV override: {env_key} -> {env_value}")
        except Exception as e:
            logger.warning(f"Failed to apply ENV override {env_key}: {e}")
    
    return result


def _convert_env_value(value: str) -> Any:
    """Convert string environment value to appropriate Python type."""
    # Boolean
    if value.lower() in ("true", "yes", "1"):
        return True
    if value.lower() in ("false", "no", "0"):
        return False
    
    # Integer
    try:
        return int(value)
    except ValueError:
        pass
    
    # Float
    try:
        return float(value)
    except ValueError:
        pass
    
    # Remove surrounding quotes if present
    if (value.startswith('"') and value.endswith('"')) or \
       (value.startswith("'") and value.endswith("'")):
        return value[1:-1]
    
    return value


def _deep_merge(base: Dict[str, Any], update: Dict[str, Any]) -> Dict[str, Any]:
    """Recursively merge dictionary 'update' into 'base'."""
    result = base.copy()
    
    for key, value in update.items():
        if isinstance(value, dict) and key in result and isinstance(result[key], dict):
            result[key] = _deep_merge(result[key], value)
        else:
            result[key] = value
    
    return result


def get_current_node_role() -> Optional[str]:
    """
    Determine the role of the current node based on the 'network' section in config.yaml.
    Returns the role if found, otherwise returns None.
    """
    try:
        config_dir = Path.cwd() / "configs"
        if not config_dir.exists():
            config_dir = Path(__file__).parent.parent / "configs"
        
        with open(config_dir / "config.yaml", "r") as f:
            config_data = yaml.safe_load(f) or {}
        
        network_config = config_data.get('network', {})
        nodes = network_config.get('nodes', {})
        
        import socket
        hostname = socket.gethostname()
        
        for node, details in nodes.items():
            if 'ip' in details and details['ip'] == socket.gethostbyname(hostname):
                return details.get('role')
    
    except Exception as e:
        logger.error(f"Failed to determine current node role: {e}")
    
    return None


class Config:
    """Singleton configuration manager."""
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Config, cls).__new__(cls)
            cls._instance._config = load_config()
        return cls._instance

    @staticmethod
    def get_instance():
        """Get the singleton configuration instance."""
        if Config._instance is None:
            Config._instance = Config()
        return Config._instance

    def load(self) -> CobaltSettings:
        """Load and return the configuration."""
        return self._config


def load_config(config_dir: Optional[Path | str] = None) -> CobaltSettings:
    """
    Load configuration from YAML files and merge with environment variables.
    
    Priority (highest to lowest):
    1. Environment variables
    2. YAML files in configs directory
    3. Default values
    
    Args:
        config_dir: Optional path to configuration directory. Defaults to 'configs/'.
    
    Returns:
        CobaltSettings: Loaded configuration object.
    """
    # 1. Resolve Directory
    if config_dir is None:
        candidates = [
            Path.cwd() / "configs",
            Path(__file__).parent.parent / "configs"
        ]
        config_dir = next((p for p in candidates if p.exists()), None)

    if not config_dir:
        logger.warning("Config directory 'configs/' not found. Using defaults.")
        return CobaltSettings()

    config_dir = Path(config_dir)
    logger.info(f"Loading configuration from: {config_dir}")

    # 2. Scan for YAML and Load
    yaml_files = sorted(list(config_dir.glob("*.yaml")) + list(config_dir.glob("*.yml")))
    
    if not yaml_files:
        logger.warning("No YAML files found in configs/. Using defaults.")
        return CobaltSettings()

    # 3. Merge All YAML Files
    master_data = {}
    
    for file_path in yaml_files:
        try:
            file_data = _load_yaml_config(file_path)
            
            if not file_data:
                continue
                
            keys = list(file_data.keys())
            logger.debug(f"Loaded {file_path.name} -> Keys: {keys}")
            
            master_data = _deep_merge(master_data, file_data)
            
        except Exception as e:
            logger.error(f"Failed to load {file_path.name}: {e}")

    # 4. Merge YAML with ENV overrides
    merged_data = _merge_yaml_with_env(master_data)
    
    # 5. Create Pydantic Settings Object
    try:
        logger.debug(f"Final merged configuration: {merged_data}")
        return CobaltSettings(**merged_data)
    except Exception as e:
        logger.error(f"Configuration Validation Error: {e}")
        return CobaltSettings()


# Convenience function for direct access
def get_config() -> CobaltSettings:
    """Get the singleton configuration instance."""
    return Config.get_instance().load()