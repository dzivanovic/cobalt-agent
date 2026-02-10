"""
Cobalt Agent - Main Entry Point
Project Cobalt: Autonomous AI Chief of Staff & Trading System
"""

import sys
from loguru import logger

from cobalt_agent.config import load_config
from cobalt_agent.memory.postgres import PostgresMemory
from cobalt_agent.memory import MemorySystem # Keep this as fallback
from cobalt_agent.persona import Persona
from cobalt_agent.interface import CLI
from cobalt_agent.llm import LLM
from cobalt_agent.prompt import PromptEngine
from cobalt_agent.tool_manager import ToolManager
from cobalt_agent.brain.cortex import Cortex

def configure_logging():
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
        "logs/cobalt_agent_{time:YYYY-MM-DD}.log",
        level="INFO",
        format="{time:YYYY-MM-DD HH:mm:ss.SSS} | {level: <8} | {name}:{function}:{line} - {message}",
        rotation="00:00",  # Rotate daily at midnight
        retention="7 days",  # Keep logs for 7 days
        compression="zip",  # Compress rotated logs
    )


def main():
    """Main entry point for Cobalt Agent."""
    # Configure logging
    configure_logging()
    
    # Load configuration
    config = load_config()
    
    # Initialize Persona System
    persona = Persona(config.persona)
    
    # Initialize Memory System
    try:
        # Try to connect to the Database
        memory = PostgresMemory()
    except Exception as e:
        # Fallback to JSON if Docker is down
        logger.warning(f"Database offline, falling back to local file: {e}")
        memory = MemorySystem()
    
    # Initialize Cortex
    cortex = Cortex()

    # Log initialization
    logger.info("Cobalt Agent - System Initialized")
    logger.info(f"Python Version: {sys.version}")
    logger.info(f"Configuration Loaded: Debug Mode = {config.system.debug_mode}")
    
    # Initialize the Brain (LLM)
    # We pass the model name from config. API key is handled automatically by env vars.
    llm = LLM(model_name=config.llm.model_name)
    logger.info(f"Brain Initialized: {config.llm.model_name}")

    # <--- ADDED: Initialize Tool Manager
    tool_manager = ToolManager()

    # Initialize Prompt Engine instead of static string
    prompt_engine = PromptEngine(config.persona)
    
    # <--- CHANGED: Pass REAL tools to the Prompt Engine
    # Get the list of tools from the manager
    tools_list = tool_manager.get_tool_descriptions()
    system_prompt = prompt_engine.build_system_prompt(tools=tools_list)
    # OLD: system_prompt = prompt_engine.build_system_prompt(tools=[])

    # Log System Start to Memory
    memory.add_log("Cobalt Agent System Initialized", source="System")
    memory.add_log(f"Persona '{config.persona.name}' loaded", source="System")
    
    # Log Persona information
    logger.info(f"Persona: {persona}")
    logger.info(f"Persona Roles: {', '.join(config.persona.roles)}")
    
    # Generate and log the system prompt
    #system_prompt = persona.get_system_prompt()
    logger.info("=" * 80)
    logger.info("SYSTEM PROMPT:")
    logger.info("=" * 80)
    logger.info(f"\n{system_prompt}\n")
    logger.info("=" * 80)
    
    # Test memory system
    logger.info("Memory System online")
    
    # Initialize and start the interactive CLI
    logger.info("=" * 80)
    logger.info("Starting interactive CLI interface...")
    logger.info("=" * 80)
    
    # Pass tool_manager to CLI
    cli = CLI(
        memory_system=memory, 
        llm=llm, 
        system_prompt=system_prompt,
        tool_manager=tool_manager,
        cortex=cortex  # <--- ADD THIS LINE
    )
  
    # Enter interactive mode
    try:
        cli.start()
    except Exception as e:
        logger.error(f"Critical Error: {e}")
    finally:
        # Save memory to disk after exiting
        logger.info("Exiting Cobalt Agent")
        
        # Added source
        memory.add_log("CLI session ended", source="System")
        
        memory.save_memory()


if __name__ == "__main__":
    main()