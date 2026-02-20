"""
Configuration Management for Cobalt Agent
Pydantic Settings-based configuration with environment variable overrides.

Loading Priority (highest to lowest):
1. Environment Variables (via .env file and OS env)
2. YAML Configuration Files (configs/*.yaml)

Environment Variable Mapping:
- Simple fields: UPPER_CASE converts to lower_case_with_underscores
- Nested fields: POSTGRES_HOST maps to postgres.host via env_nested_delimiter="_"
"""

import os
from pathlib import Path
from typing import Any, Optional

import yaml
from dotenv import load_dotenv
from loguru import logger
from pydantic import BaseModel, Field, ConfigDict
from pydantic_settings import BaseSettings
from pydantic_settings.sources import PydanticBaseSettingsSource

# Load environment variables from .env file (explicit path)
# Get the directory where config.py is located
config_dir = Path(__file__).parent
# Look for .env in the project root (parent of src/)
env_path = config_dir.parent.parent / ".env"
if env_path.exists():
    load_dotenv(env_path)
else:
    # Fallback to current working directory
    load_dotenv()  # Fallback to default behavior (looks in cwd)


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
    roles: list[str] = Field(default_factory=list)
    skills: list[str] = Field(default_factory=list)
    tone: list[str] = Field(default_factory=list)
    directives: list[str] = Field(default_factory=list)


class NodeConfig(BaseModel):
    """Schema for network node configuration."""
    role: str
    ip: str = "127.0.0.1"
    port: int = 8080
    protocol: str = "http"


class NetworkConfig(BaseModel):
    """Schema for network topology configuration."""
    nodes: dict[str, NodeConfig]


class PostgresConfig(BaseModel):
    """Schema for PostgreSQL database configuration."""
    host: str = "localhost"
    port: int = 5432
    db: str = "cobalt_memory"
    user: str = "postgres"
    password: Optional[str] = None


class MattermostConfig(BaseModel):
    """Schema for Mattermost communication configuration."""
    url: Optional[str] = None
    token: Optional[str] = None
    scheme: str = "http"
    port: int = 8065


# --- 2. Main Configuration Class ---


class CobaltSettings(BaseSettings):
    """
    Pydantic Settings class that loads YAML config and allows ENV overrides.
    
    Environment Variable Naming Convention:
    - Nested keys: POSTGRES_HOST -> postgres.host (using env_nested_delimiter="_")
    - The env_nested_delimiter setting allows Pydantic to automatically
      map POSTGRES_HOST to postgres.host via the "_" delimiter.
    """
    model_config = ConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="allow",  # Allow extra fields not defined in schema
        env_prefix="",  # No prefix for environment variables
        env_nested_delimiter="_",  # Use underscore to separate nested keys
    )

    # Core Sections with defaults from YAML
    system: SystemConfig = Field(default_factory=SystemConfig)
    llm: LLMConfig = Field(default_factory=LLMConfig)
    persona: PersonaConfig = Field(default_factory=PersonaConfig)
    
    # Optional Known Sections
    trading_rules: Optional[TradingRules] = None
    active_profile: Optional[dict[str, str]] = None
    models: Optional[dict[str, Any]] = None
    network: Optional[NetworkConfig] = None
    postgres: PostgresConfig = Field(default_factory=PostgresConfig)
    mattermost: MattermostConfig = Field(default_factory=MattermostConfig)

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
        Custom source order: ENV variables override YAML values.
        Source order (highest to lowest priority):
        1. ENV settings (including .env file)
        2. File secret settings
        3. Init settings (YAML data passed as kwargs)
        """
        return (env_settings, dotenv_settings, file_secret_settings, init_settings)


# --- 3. Helper Functions ---


def _load_yaml_config(yaml_path: Path) -> dict[str, Any]:
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


def _deep_merge(base: dict[str, Any], update: dict[str, Any]) -> dict[str, Any]:
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
    1. Environment variables (via Pydantic's env_nested_delimiter)
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

    # 4. Create Pydantic Settings Object
    # Pydantic will automatically handle ENV overrides via env_nested_delimiter="_"
    try:
        logger.debug(f"Final merged configuration: {master_data}")
        return CobaltSettings(**master_data)
    except Exception as e:
        logger.error(f"Configuration Validation Error: {e}")
        return CobaltSettings()


# Convenience function for direct access
def get_config() -> CobaltSettings:
    """Get the singleton configuration instance."""
    return Config.get_instance().load()