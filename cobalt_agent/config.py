"""
Configuration Management for Cobalt Agent
Handles loading and validation of configuration from YAML files.
"""

import os  # <--- ADDED: Needed to read environment variables
from pathlib import Path
from typing import List, Optional

import yaml
from dotenv import load_dotenv  # <--- ADDED: Automatically loads .env file
from loguru import logger
from pydantic import BaseModel, Field

# <--- ADDED: Load environment variables at module level
load_dotenv()

class SystemConfig(BaseModel):
    """System configuration settings."""

    debug_mode: bool = Field(default=False, description="Enable debug mode")
    version: str = Field(default="0.1.0", description="System version")


class LLMConfig(BaseModel):
    """LLM configuration settings."""

    # CHANGED: Default to your actual model
    model_name: str = Field(default="gemini/gemini-1.5-pro", description="LLM model name")
    #model_name: str = Field(default="openrouter/anthropic/claude-3.5-sonnet", description="LLM model name")
    
    # <--- CHANGED: Removed default_factory logic. 
    # We now default to None so LiteLLM can check os.environ itself.
    api_key: Optional[str] = Field(default=None, description="API key (optional if using standard env vars)")

class PersonaConfig(BaseModel):
    """Persona configuration settings."""

    name: str = Field(default="Cobalt", description="Agent name")
    roles: List[str] = Field(
        default_factory=list, description="List of roles the agent fulfills"
    )
    skills: List[str] = Field(
        default_factory=list, description="List of agent skills and capabilities"
    )
    tone: List[str] = Field(
        default_factory=list, description="Communication tone characteristics"
    )
    directives: List[str] = Field(
        default_factory=list, description="Core behavioral directives"
    )


class CobaltConfig(BaseModel):
    """Main configuration class for Cobalt Agent."""

    system: SystemConfig = Field(default_factory=SystemConfig)
    llm: LLMConfig = Field(default_factory=LLMConfig)
    persona: PersonaConfig = Field(default_factory=PersonaConfig)

    @classmethod
    def from_yaml(cls, config_path: Path | str) -> "CobaltConfig":
        """
        Load configuration from a YAML file.

        Args:
            config_path: Path to the YAML configuration file

        Returns:
            CobaltConfig: Loaded and validated configuration

        Raises:
            FileNotFoundError: If config file doesn't exist
            ValueError: If config file is invalid
        """
        config_path = Path(config_path)

        if not config_path.exists():
            logger.warning(
                f"Configuration file not found at {config_path}. Using default configuration."
            )
            return cls()

        try:
            with open(config_path, "r") as f:
                config_data = yaml.safe_load(f)

            if config_data is None:
                logger.warning(
                    f"Configuration file {config_path} is empty. Using default configuration."
                )
                return cls()

            logger.info(f"Configuration loaded from {config_path}")
            return cls(**config_data)

        except yaml.YAMLError as e:
            logger.error(f"Error parsing YAML configuration: {e}")
            logger.warning("Using default configuration due to parsing error.")
            return cls()

        except Exception as e:
            logger.error(f"Unexpected error loading configuration: {e}")
            logger.warning("Using default configuration due to error.")
            return cls()


def load_config(config_path: Optional[Path | str] = None) -> CobaltConfig:
    """
    Load the Cobalt configuration.

    Args:
        config_path: Optional path to config file. Defaults to 'config.yaml' in project root.

    Returns:
        CobaltConfig: Loaded configuration instance
    """
    if config_path is None:
        # Default to config.yaml in project root
        config_path = Path(__file__).parent.parent / "config.yaml"

    return CobaltConfig.from_yaml(config_path)
