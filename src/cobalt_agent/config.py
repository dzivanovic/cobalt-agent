"""
Configuration Management for Cobalt Agent
Pydantic Settings-based configuration with environment variable overrides.

Loading Priority (highest to lowest):
1. Environment Variables (via .env file and OS env)
2. YAML Configuration Files (configs/*.yaml)

Environment Variable Mapping:
- Simple fields: COBALT_SYSTEM_DEBUG_MODE -> system.debug_mode
- Nested fields: COBALT_POSTGRES__HOST -> postgres.host (using env_nested_delimiter="__")
"""

import json
import os
from pathlib import Path
from typing import Any, Optional

import yaml
from dotenv import load_dotenv
from loguru import logger
from pydantic import BaseModel, Field, ConfigDict
from pydantic import AliasChoices
from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic_settings.sources import PydanticBaseSettingsSource

from cobalt_agent.security.vault import VaultManager

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
    obsidian_vault_path: str = Field(
        default="/default/obsidian/vault/path",
        validation_alias=AliasChoices("OBSIDIAN_VAULT_PATH", "COBALT_SYSTEM__OBSIDIAN_VAULT_PATH")
    )


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
    host: str = Field(default="localhost", validation_alias=AliasChoices("COBALT_POSTGRES__HOST", "POSTGRES_HOST"))
    port: int = Field(default=5432, validation_alias=AliasChoices("COBALT_POSTGRES__PORT", "POSTGRES_PORT"))
    user: str = Field(default="postgres", validation_alias=AliasChoices("COBALT_POSTGRES__USER", "POSTGRES_USER"))
    password: Optional[str] = Field(default=None, validation_alias=AliasChoices("COBALT_POSTGRES__PASSWORD", "POSTGRES_PASSWORD"))
    db: str = Field(default="cobalt_memory", validation_alias=AliasChoices("COBALT_POSTGRES__DB", "POSTGRES_DB"))


class MattermostConfig(BaseModel):
    """Schema for Mattermost communication configuration."""
    url: Optional[str] = None
    token: Optional[str] = None
    scheme: str = "http"
    port: int = 8065
    approval_channel: str = "cobalt-approvals"
    approval_team: str = "cobalt-team"


class BrowserConfig(BaseModel):
    """Schema for browser/Playwright configuration."""
    allowed_domains: list[str] = Field(default_factory=lambda: ["example.com"])


class StrategyTimeWindow(BaseModel):
    """Schema for strategy time window configuration."""
    start: str
    end: str


class StrategyFiltersLiquidity(BaseModel):
    """Schema for liquidity filter configuration."""
    min_average_daily_volume: int
    min_price: float


class StrategyFiltersCorrelation(BaseModel):
    """Schema for correlation filter configuration."""
    check_sector: bool
    check_spy: bool


class StrategyFilters(BaseModel):
    """Schema for strategy filter configuration."""
    min_atr: Optional[float] = None
    day1_close_zone: Optional[float] = None
    max_gap: Optional[float] = None
    min_rvol_day1: Optional[float] = None
    trend_indicator: Optional[str] = None
    baseline_indicator: Optional[str] = None
    min_volume_ratio: Optional[float] = None
    pattern: Optional[str] = None
    volume_break: Optional[str] = None
    volume_retest: Optional[str] = None
    liquidity: Optional[StrategyFiltersLiquidity] = None
    correlation: Optional[StrategyFiltersCorrelation] = None


class StrategyExecution(BaseModel):
    """Schema for strategy execution configuration."""
    entry_trigger: Optional[str] = None
    stop_buffer: Optional[float] = None
    target_multiplier: Optional[float] = None
    stop_rule: Optional[str] = None
    target_rule: Optional[str] = None
    exit_strategy: Optional[str] = None


class StrategyScoring(BaseModel):
    """Schema for strategy scoring configuration."""
    base_score: int
    
    # RVOL Logic
    high_rvol_threshold: float
    high_rvol_points: int
    base_rvol_points: int
    
    # Price Action Logic
    gap_up_points: int
    
    # Ion (Real-Time) Modifiers
    live_rvol_multiplier: float
    spy_correlation_weight: float
    resistance_penalty: float
    time_decay_per_min: float


class StrategyConfig(BaseModel):
    """Schema for a single strategy configuration."""
    name: str
    active: bool
    direction: str
    description: Optional[str] = None
    time_window: StrategyTimeWindow
    filters: StrategyFilters
    execution: StrategyExecution
    scoring: Optional[StrategyScoring] = None


class VaultConfig(BaseModel):
    """Schema for vault configuration."""
    path: str = "data/.cobalt_vault"
    enabled: bool = True


# --- 2. Main Configuration Class ---


class PromptsConfig(BaseModel):
    """Schema for prompts configuration."""
    system: Optional[dict] = None
    scheduler: Optional[dict] = None
    ops: Optional[dict] = None
    engineering: Optional[dict] = None
    proposal: Optional[dict] = None
    routing: Optional[dict] = None
    orchestrator: Optional[dict] = None


class CobaltSettings(BaseSettings):
    """
    Pydantic Settings class that loads YAML config and allows ENV overrides.
    
    Environment Variable Naming Convention:
    - Nested keys: POSTGRES_HOST -> postgres.host (using env_nested_delimiter="__")
    - The env_nested_delimiter setting allows Pydantic to automatically
      map POSTGRES_HOST to postgres.host via the "__" delimiter.
    - All environment variables must be prefixed with COBALT_ to avoid conflicts.
    """
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",  # Ignore extra fields not defined in schema (prevents env hijacking)
        env_prefix="COBALT_",  # All env vars must be prefixed with COBALT_
        env_nested_delimiter="__",  # Use double underscore to separate nested keys
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
    vault: Optional[VaultConfig] = Field(default_factory=VaultConfig)
    prompts: PromptsConfig = Field(default_factory=PromptsConfig)
    browser: Optional[BrowserConfig] = Field(default_factory=BrowserConfig)
    
    # Strategy Playbooks - validated via Pydantic models
    strategies: Optional[dict[str, StrategyConfig]] = None

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


def parse_json_credentials(json_string: str) -> dict[str, Any]:
    """
    Parse JSON credentials string into a dictionary.
    
    Handles grouped credentials like URLs and Tokens together.
    Example input: '{"url": "https://api.example.com", "token": "secret123"}'
    
    Args:
        json_string: A JSON-formatted string containing credentials.
        
    Returns:
        A dictionary with the parsed credentials.
        
    Raises:
        json.JSONDecodeError: If the input is not valid JSON.
    """
    try:
        credentials = json.loads(json_string)
        if not isinstance(credentials, dict):
            logger.warning("JSON credentials parsed to non-dict type, wrapping in dict")
            credentials = {"data": credentials}
        return credentials
    except json.JSONDecodeError as e:
        logger.error(f"Failed to parse JSON credentials: {e}")
        raise


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
    """Singleton configuration manager with integrated VaultManager."""
    _instance = None
    _vault_manager: Optional[VaultManager] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Config, cls).__new__(cls)
            # Initialize _config - either from load_config or as a placeholder
            try:
                cls._instance._config = load_config()
            except Exception:
                # If load_config fails (e.g., no configs found), use defaults
                cls._instance._config = CobaltSettings()
        return cls._instance

    @staticmethod
    def get_instance():
        """Get the singleton configuration instance."""
        if Config._instance is None:
            Config._instance = Config()
        return Config._instance

    @property
    def vault_manager(self) -> Optional[VaultManager]:
        """Get or create the VaultManager instance."""
        if Config._vault_manager is None:
            config = self._config
            vault_config = config.vault if config.vault else None
            vault_path = vault_config.path if vault_config else "data/.cobalt_vault"
            Config._vault_manager = VaultManager(vault_path)
        return Config._vault_manager

    def load(self) -> CobaltSettings:
        """Load and return the configuration."""
        return self._config

    def unlock_vault(self, master_key: str) -> bool:
        """
        Unlock the vault and inject secrets into the runtime configuration.
        
        Args:
            master_key: The AES-256 Fernet key to decrypt the vault.
            
        Returns:
            True if vault was successfully unlocked, False otherwise.
        """
        vault_mgr = self.vault_manager
        if vault_mgr is None:
            logger.error("Failed to unlock vault: VaultManager not initialized")
            return False
            
        success = vault_mgr.unlock(master_key)
        if success:
            logger.info("🔐 Vault unlocked successfully. Secrets injected into runtime configuration.")
        return success

    def lock_vault(self) -> None:
        """Lock the vault and wipe secrets from memory."""
        vault_mgr = self.vault_manager
        if vault_mgr is not None:
            vault_mgr.lock()
            Config._vault_manager = None
            logger.info("🔒 Vault locked. Secrets wiped from RAM.")

    def inject_secrets(self, config: CobaltSettings) -> CobaltSettings:
        """
        Inject secrets from the vault into the runtime configuration.
        This replaces sensitive fields (like API keys and tokens) with values from the vault.
        
        Args:
            config: The configuration object to inject secrets into.
            
        Returns:
            The configuration object with secrets injected from the vault.
        """
        vault_mgr = self.vault_manager
        if vault_mgr is None:
            logger.warning("Vault is locked or not initialized. Skipping secret injection.")
            return config
            
        if not vault_mgr._is_unlocked:
            logger.warning("Vault is locked. Cannot inject secrets.")
            return config

        # Create a mutable copy of the configuration
        config_data = config.model_dump()
        
        # Inject LLM API keys from vault
        llm_config = config_data.get('llm', {})
        vault_keys = vault_mgr.list_secrets()
        
        # Check for common API key names in vault
        llm_key_mapping = {
            'openai_api_key': 'api_key',
            'anthropic_api_key': 'api_key',
            'gemini_api_key': 'api_key',
            'openrouter_api_key': 'api_key',
        }
        
        for vault_key, config_field in llm_key_mapping.items():
            if vault_key in vault_keys:
                secret_value = vault_mgr.get_secret(vault_key)
                if secret_value:
                    llm_config[config_field] = secret_value
                    logger.debug(f"Injected {vault_key} into LLM config")
        
        # Inject Mattermost credentials (URL and Token together)
        mattermost_config = config_data.get('mattermost', {})
        if 'mattermost_url' in vault_keys and 'mattermost_token' in vault_keys:
            vault_mgr.get_secret('mattermost_url') and None  # Access to verify
            mattermost_url = vault_mgr.get_secret('mattermost_url')
            mattermost_token = vault_mgr.get_secret('mattermost_token')
            if mattermost_url and mattermost_token:
                mattermost_config['url'] = mattermost_url
                mattermost_config['token'] = mattermost_token
                logger.debug("Injected Mattermost URL and token from vault")
        
        # Update the config with injected secrets
        config_data['llm'] = llm_config
        config_data['mattermost'] = mattermost_config
        
        # Create new config object with injected secrets
        return CobaltSettings(**config_data)


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

    # --- VAULT INTEGRATION (NEW) ---
    master_key = os.getenv("COBALT_MASTER_KEY")
    if master_key:
        logger.info("🔑 COBALT_MASTER_KEY detected. Unlocking secure vault...")
        vault = VaultManager()
        if vault.unlock(master_key):
            # Ensure base sections exist
            if 'keys' not in master_data: master_data['keys'] = {}
            if 'mattermost' not in master_data: master_data['mattermost'] = {}

            for key_name in vault.list_secrets():
                secret_val = vault.get_secret(key_name)
                
                # Skip None values
                if secret_val is None:
                    continue
                
                # Try to parse as JSON for grouped credentials
                try:
                    parsed_val = json.loads(secret_val)
                except (ValueError, TypeError):
                    parsed_val = secret_val # Fallback to flat string
                
                # Routing logic
                if key_name == "MATTERMOST_CREDS" and isinstance(parsed_val, dict):
                    master_data['mattermost'].update(parsed_val)
                else:
                    # Default flat keys (OpenAI, Gemini, etc.)
                    master_data['keys'][key_name] = parsed_val
                    # Inject into runtime environment for external libraries (LiteLLM)
                    if isinstance(parsed_val, str):
                        os.environ[key_name] = parsed_val
                    
            vault.lock()
            logger.info("🔒 Vault secrets loaded into runtime RAM and vault locked.")
        else:
            logger.error("Failed to unlock vault with provided Master Key!")
    else:
        logger.warning("⚠️ No COBALT_MASTER_KEY found. Running in degraded/unsecure mode.")
    # -------------------------------

    # 4. Validate and Transform Strategies
    # Validate the strategies dictionary through Pydantic models
    if "strategies" in master_data:
        validated_strategies: dict[str, StrategyConfig] = {}
        for strategy_name, strategy_data in master_data["strategies"].items():
            try:
                validated_strategies[strategy_name] = StrategyConfig(**strategy_data)
                logger.debug(f"Validated strategy: {strategy_name}")
            except Exception as e:
                logger.error(f"Failed to validate strategy '{strategy_name}': {e}")
                raise
        master_data["strategies"] = validated_strategies

    # 5. Create Pydantic Settings Object
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