"""
Configuration Management for Cobalt Agent
Dynamic Loader: Scans 'configs/' for ANY yaml file and merges them into a unified object.
Supports future extensibility (subagents, new rule sets) without code changes.
"""

import os
from pathlib import Path
from typing import List, Optional, Dict, Any

import yaml
from dotenv import load_dotenv
from loguru import logger
from pydantic import BaseModel, Field, ConfigDict

# Load environment variables
load_dotenv()

# --- 1. Modular Schema Definitions ---

# Trading Rules Schema (Matches the structure in rules.yaml -> trading_rules)
class MomentumRules(BaseModel):
    rvol_alert_threshold: float
    rvol_strong_threshold: float

class RSIRules(BaseModel):
    period: int
    overbought: int
    oversold: int

class ATRRules(BaseModel):
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

# System Schemas (Matches config.yaml)
class SystemConfig(BaseModel):
    debug_mode: bool = False
    version: str = "0.1.0"

class LLMConfig(BaseModel):
    model_name: str = "gemini/gemini-1.5-pro"
    api_key: Optional[str] = None

class PersonaConfig(BaseModel):
    name: str = "Cobalt"
    roles: List[str] = Field(default_factory=list)
    skills: List[str] = Field(default_factory=list)
    tone: List[str] = Field(default_factory=list)
    directives: List[str] = Field(default_factory=list)

# --- 2. The Dynamic Master Configuration ---

class NodeConfig(BaseModel):
    role: str
    ip: str
    port: int
    protocol: str = "http"

class NetworkConfig(BaseModel):
    nodes: Dict[str, NodeConfig]

class CobaltConfig(BaseModel):
    """
    The Unified Configuration Object.
    
    Static Fields: core system requirements (llm, system, persona).
    Dynamic Fields: trading_rules, subagents, etc.
    """
    # Allow arbitrary new keys (e.g., 'subagents', 'coding_rules') to be loaded automatically
    model_config = ConfigDict(extra='allow')

    # Core Sections (We want validation on these)
    system: SystemConfig = Field(default_factory=SystemConfig)
    llm: LLMConfig = Field(default_factory=LLMConfig)
    persona: PersonaConfig = Field(default_factory=PersonaConfig)
    
    # Optional Known Sections (Type-safe access for code that expects them)
    trading_rules: Optional[TradingRules] = None
    active_profile: Optional[Dict[str, str]] = None
    models: Optional[Dict[str, Any]] = None
    network: Optional[NetworkConfig] = None

    def __getattr__(self, item):
        """
        Fallback to allow accessing dynamic keys as attributes safely.
        Example: config.future_module_settings
        """
        return self.__dict__.get(item, None)

# --- 3. Dynamic Loading Logic ---

def _deep_merge(base: Dict[str, Any], update: Dict[str, Any]) -> Dict[str, Any]:
    """Recursively merge dictionary 'update' into 'base'."""
    for key, value in update.items():
        if isinstance(value, dict) and key in base and isinstance(base[key], dict):
            _deep_merge(base[key], value)
        else:
            base[key] = value
    return base

def get_current_node_role() -> Optional[str]:
    """
    Determine the role of the current node based on the 'network' section in config.yaml.
    Returns the role if found, otherwise returns None.
    """
    try:
        with open("configs/config.yaml", "r") as f:
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
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Config, cls).__new__(cls)
            cls._instance._config = load_config()
        return cls._instance

    @staticmethod
    def get_instance():
        if Config._instance is None:
            Config._instance = Config()
        return Config._instance

    def load(self) -> CobaltConfig:
        return self._config

def load_config(config_dir: Optional[Path | str] = None) -> CobaltConfig:
    """
    Scans the config directory, loads ALL .yaml files, and merges them.
    """
    # 1. Resolve Directory
    if config_dir is None:
        # Check Project Root first, then Package Root
        candidates = [
            Path.cwd() / "configs",
            Path(__file__).parent.parent / "configs"
        ]
        config_dir = next((p for p in candidates if p.exists()), None)

    if not config_dir:
        logger.warning("Config directory 'configs/' not found. Using defaults.")
        return CobaltConfig()

    config_dir = Path(config_dir)
    logger.info(f"Loading configuration from: {config_dir}")

    # 2. Scan for YAML
    yaml_files = sorted(list(config_dir.glob("*.yaml")) + list(config_dir.glob("*.yml")))
    
    if not yaml_files:
        logger.warning("No YAML files found in configs/. Using defaults.")
        return CobaltConfig()

    # 3. Merge All Files
    master_data = {}
    
    for file_path in yaml_files:
        try:
            with open(file_path, "r") as f:
                file_data = yaml.safe_load(f) or {}
                
            if not file_data:
                continue
                
            # Log what top-level keys we found (e.g., "Found 'trading_rules' in rules.yaml")
            keys = list(file_data.keys())
            logger.debug(f"Loaded {file_path.name} -> Keys: {keys}")
            
            # Merge into master
            _deep_merge(master_data, file_data)
            
        except Exception as e:
            logger.error(f"Failed to load {file_path.name}: {e}")

    # 4. Create Object
    try:
        # Debugging: Print the final merged configuration data
        logger.debug(f"Merged Configuration Data: {master_data}")

        # Pydantic will validate known fields (system, trading_rules) 
        # and accept unknown ones (subagents, skills) due to extra='allow'
        return CobaltConfig(**master_data)
    except Exception as e:
        logger.error(f"Configuration Validation Error: {e}")
        # Return partial/default config to prevent crash
        return CobaltConfig()
