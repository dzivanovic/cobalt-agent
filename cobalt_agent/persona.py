"""
Persona System for Cobalt Agent
Manages the AI agent's identity, roles, skills, and behavioral directives.
"""

from typing import List

from loguru import logger
from pydantic import BaseModel, Field


class PersonaConfig(BaseModel):
    """Configuration for Cobalt Agent persona."""

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


class Persona:
    """
    Persona class that manages the AI agent's identity and generates system prompts.
    """

    def __init__(self, config: PersonaConfig):
        """
        Initialize the Persona with configuration.

        Args:
            config: PersonaConfig instance containing persona settings
        """
        self.config = config
        logger.info(f"Persona '{config.name}' initialized")

    def get_system_prompt(self) -> str:
        """
        Generate a comprehensive system prompt combining all persona attributes.

        Returns:
            str: Complete system instruction string for the AI agent
        """
        prompt_parts = []

        # Introduction
        prompt_parts.append(f"You are {self.config.name}, an advanced AI agent.")
        prompt_parts.append("")

        # Roles
        if self.config.roles:
            prompt_parts.append("YOUR ROLES:")
            for role in self.config.roles:
                prompt_parts.append(f"  • {role}")
            prompt_parts.append("")

        # Skills
        if self.config.skills:
            prompt_parts.append("YOUR SKILLS:")
            for skill in self.config.skills:
                prompt_parts.append(f"  • {skill}")
            prompt_parts.append("")

        # Communication Tone
        if self.config.tone:
            prompt_parts.append("COMMUNICATION STYLE:")
            tone_description = ", ".join(self.config.tone)
            prompt_parts.append(f"  Maintain a {tone_description} approach in all interactions.")
            prompt_parts.append("")

        # Core Directives
        if self.config.directives:
            prompt_parts.append("CORE DIRECTIVES:")
            for directive in self.config.directives:
                prompt_parts.append(f"  • {directive}")
            prompt_parts.append("")

        # Mission statement
        prompt_parts.append(
            "MISSION: Execute tasks with precision, leveraging your multidisciplinary expertise "
            "to deliver optimal outcomes while adhering to core directives."
        )

        system_prompt = "\n".join(prompt_parts)
        logger.debug("System prompt generated successfully")

        return system_prompt

    def __repr__(self) -> str:
        """String representation of the Persona."""
        return (
            f"Persona(name='{self.config.name}', "
            f"roles={len(self.config.roles)}, "
            f"skills={len(self.config.skills)})"
        )
