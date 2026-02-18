"""
Cobalt Agent - Main Entry Point
Project Cobalt: Autonomous AI Chief of Staff & Trading System
"""

import sys
from loguru import logger
from datetime import datetime, timedelta

from cobalt_agent.config import load_config
from cobalt_agent.memory.postgres import PostgresMemory
from cobalt_agent.memory import MemorySystem  # Keep this as fallback
from cobalt_agent.persona import Persona
from cobalt_agent.interface import CLI
from cobalt_agent.llm import LLM
from cobalt_agent.prompt import PromptEngine
from cobalt_agent.tool_manager import ToolManager
from cobalt_agent.brain.cortex import Cortex
from cobalt_agent.core.scheduler import AgentScheduler
from cobalt_agent.skills.productivity.briefing import MorningBriefing
from cobalt_agent.skills.research.deep_dive import DeepResearch

class CobaltAgent:
    def __init__(self):
        self.configure_logging()
        self.config = load_config()
        self.persona = Persona(self.config.persona)
        
        try:
            self.memory = PostgresMemory()
        except Exception as e:
            logger.warning(f"Database offline, falling back to local file: {e}")
            self.memory = MemorySystem()

        self.cortex = Cortex()
        self.scheduler = AgentScheduler(self.cortex)
        self.scheduler.start()
        
        briefing = MorningBriefing()
        researcher = DeepResearch() 

        # This sets it to run every morning at 8:00 AM
        self.scheduler.add_job(briefing.run, 'cron', hour=8, minute=0)

        logger.info("Cobalt Agent - System Initialized")
        logger.info(f"Python Version: {sys.version}")
        logger.info(f"Configuration Loaded: Debug Mode = {self.config.system.debug_mode}")

        # Initialize the Brain (LLM) with Intent-Based Routing
        self.llm = LLM(role="default")
        logger.info("Brain Initialized: Role-Based Routing Active (default)")

        # Initialize Tool Manager
        self.tool_manager = ToolManager()

        # Initialize Prompt Engine instead of static string
        self.prompt_engine = PromptEngine(self.config.persona)
        
        tools_list = self.tool_manager.get_tool_descriptions()
        system_prompt = self.prompt_engine.build_system_prompt(tools=tools_list)
        self.system_prompt = system_prompt

        # Log System Start to Memory
        self.memory.add_log("Cobalt Agent System Initialized", source="System")
        self.memory.add_log(f"Persona '{self.config.persona.name}' loaded", source="System")

        logger.info(f"Persona: {self.persona}")
        logger.info(f"Persona Roles: {', '.join(self.config.persona.roles)}")

        logger.info("=" * 80)
        logger.info("SYSTEM PROMPT:")
        logger.info("=" * 80)
        logger.info(f"\n{self.system_prompt}\n")
        logger.info("=" * 80)

        logger.info("Memory System online")

    def configure_logging(self):
        """Configure loguru logging with INFO level and file rotation."""
        # Remove default handler
        logger.remove()
        
        # Add console handler with INFO level
        logger.add(
            sys.stderr,
            level="INFO",
            format="<green>{time:YYYY-MM-DD HH:mm:ss.SSS}</green> | <level>{level: <8}</level> | <cyan>{name}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan> - <level>{message}</level>",
            colorize=True,
        )
        
        # Add file handler with rotation
        logger.add(
            "logs/agent_{time:YYYY-MM-DD}.log",
            level="INFO",
            format="{time:YYYY-MM-DD HH:mm:ss.SSS} | {level: <8} | {name}:{function}:{line} - {message}",
            rotation="00:00",  # Rotate daily at midnight
            retention="7 days",  # Keep logs for 7 days
            compression="zip",  # Compress rotated logs
        )
    def main(self):
        """Main entry point for Cobalt Agent."""
        self.configure_logging()
        
        briefing = MorningBriefing()
        researcher = DeepResearch() 

        logger.info("=" * 80)
        logger.info("Starting interactive CLI interface...")
        logger.info("=" * 80)

        cli = CLI(
            memory_system=self.memory, 
            llm=self.llm, 
            system_prompt=self.system_prompt,
            tool_manager=self.tool_manager,
            cortex=self.cortex
        )
  
        try:
            cli.start()
        except Exception as e:
            logger.error(f"Critical Error: {e}")
        finally:
            # Save memory to disk after exiting
            logger.info("Exiting Cobalt Agent")
            
            self.scheduler.stop()
        
            self.memory.add_log("CLI session ended", source="System")
        
            self.memory.save_memory()

    def send_message(self, message):
        """Send a message using the LLM."""
        try:
            response = self.llm.generate_response(
    system_prompt=self.system_prompt,
    user_input=message,
    memory_context=[],
    search_context=""
)
            logger.info(f"Message sent: {message}")
            logger.info(f"Response received: {response}")
            return response
        except Exception as e:
            logger.error(f"Failed to send message: {e}")

if __name__ == "__main__":
    agent = CobaltAgent()
    agent.main()