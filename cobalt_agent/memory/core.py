"""
Memory System Core
Manages short-term (RAM) and long-term (Disk) memory for Cobalt Agent
"""

import json
from pathlib import Path
from datetime import datetime  # <--- ADDED: For timestamps
from typing import Any, Dict, List
from loguru import logger


class MemorySystem:
    """
    Memory System for Cobalt Agent
    
    Manages:
    - Short-term memory: Last 10 interactions (RAM - Fast)
    - Long-term memory: Persistent storage in data/memory.json (Disk - Safe)
    """
    
    def __init__(self, memory_file: str = "data/memory.json"):
        """
        Initialize the Memory System.
        
        Args:
            memory_file: Path to the long-term memory storage file
        """
        self.memory_file = Path(memory_file)
        
        # <--- CHANGED: Initialize RAM memory
        self.short_term: List[Dict[str, Any]] = [] 
        # OLD: self.short_term: List[str] = []
        
        # <--- CHANGED: Initialize Disk memory structure
        self.long_term: Dict[str, Any] = {"logs": []}
        # OLD: self.long_term: Dict[str, Any] = {}
        
        # Load existing memory if available
        self.load_memory()
        
    def add_log(self, message: str, source: str = "System", data: Dict = None) -> None: # <--- CHANGED: Added source and data args
    # OLD: def add_log(self, message: str) -> None:
        """
        Add a message to short-term memory AND long-term memory.
        
        Args:
            message: The message to log
            source: The origin (User, System, Tool)
            data: Optional structured data
        """
        # <--- ADDED: Create structured entry
        entry = {
            "timestamp": datetime.now().isoformat(),
            "source": source,
            "message": message,
            "data": data or {}
        }

        # <--- CHANGED: Add to Short-Term (RAM)
        self.short_term.append(entry)
        # OLD: self.short_term.append(message)
        
        # Keep only last 10 interactions
        if len(self.short_term) > 10:
            # <--- CHANGED: Remove oldest
            self.short_term.pop(0)
            # OLD: self.short_term = self.short_term[-10:]
            
        # <--- ADDED: Add to Long-Term (Disk Buffer)
        self.long_term["logs"].append(entry)

        logger.debug(f"Memory added: [{source}] {message}")
        # OLD: logger.debug(f"Added to short-term memory: {message}")
        
        # <--- ADDED: Auto-save to ensure persistence
        self.save_memory()

    def get_context(self) -> List[Dict[str, Any]]: # <--- ADDED: New method
        """
        Fast retrieval of short-term memory for AI prompts.
        Returns the data from RAM, avoiding slow disk reads.
        """
        return self.short_term

    def save_memory(self) -> None:
        """
        Save long-term memory to disk.
        Creates the data directory if it doesn't exist.
        """
        try:
            # Ensure the data directory exists
            self.memory_file.parent.mkdir(parents=True, exist_ok=True)
            
            # Save memory to file
            with open(self.memory_file, 'w', encoding='utf-8') as f:
                json.dump(self.long_term, f, indent=2, ensure_ascii=False)
                
            # logger.info(f"Memory saved to {self.memory_file}")
            
        except Exception as e:
            logger.error(f"Failed to save memory: {e}")
            
    def load_memory(self) -> None:
        """
        Load long-term memory from disk.
        Creates an empty memory if the file doesn't exist.
        """
        try:
            if self.memory_file.exists():
                with open(self.memory_file, 'r', encoding='utf-8') as f:
                    # <--- CHANGED: Handle loading and hydrating RAM
                    data = json.load(f)
                    
                    if isinstance(data, dict):
                        self.long_term = data
                        if "logs" not in self.long_term:
                            self.long_term["logs"] = []
                    else:
                        self.long_term = {"logs": []}
                    # OLD: self.long_term = json.load(f)

                    # <--- ADDED: Hydrate Short-Term RAM from Disk
                    # This restores context after a restart
                    self.short_term = self.long_term["logs"][-10:]
                    
                logger.info(f"Memory loaded from {self.memory_file}")
            else:
                logger.info("No existing memory file found, starting with empty memory")
                # <--- CHANGED: Default structure
                self.long_term = {"logs": []}
                self.short_term = []
                # OLD: self.long_term = {}
                
        except Exception as e:
            logger.error(f"Failed to load memory: {e}")
            self.long_term = {"logs": []}
            self.short_term = []