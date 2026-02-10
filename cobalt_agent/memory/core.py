"""
Memory System Core (JSON Implementation)
Manages short-term (RAM) and long-term (Disk) memory for Cobalt Agent
"""

import json
from pathlib import Path
from datetime import datetime
from typing import Any, Dict, List
from loguru import logger
from .base import MemoryProvider  # <--- IMPORT THE CONTRACT

class MemorySystem(MemoryProvider):  # <--- SIGN THE CONTRACT
    """
    Memory System for Cobalt Agent
    
    Manages:
    - Short-term memory: Last 10 interactions (RAM - Fast)
    - Long-term memory: Persistent storage in data/memory.json (Disk - Safe)
    """
    
    def __init__(self, memory_file: str = "data/memory.json"):
        self.memory_file = Path(memory_file)
        self.short_term: List[Dict[str, Any]] = [] 
        self.long_term: Dict[str, Any] = {"logs": []}
        self.load_memory()
        
    def add_log(self, message: str, source: str = "System", data: Dict = None) -> None:
        """Add a message to short-term memory AND long-term memory."""
        entry = {
            "timestamp": datetime.now().isoformat(),
            "source": source,
            "message": message,
            "data": data or {}
        }

        self.short_term.append(entry)
        
        # Keep only last 10 interactions in RAM
        if len(self.short_term) > 10:
            self.short_term.pop(0)
            
        self.long_term["logs"].append(entry)
        logger.debug(f"Memory added: [{source}] {message}")
        self.save_memory()

    def get_context(self, limit: int = 10) -> List[Dict[str, Any]]:
        """Fast retrieval of short-term memory for AI prompts."""
        return self.short_term[-limit:]

    # <--- NEW METHOD: REQUIRED BY INTERFACE
    def search(self, query: str, limit: int = 5) -> List[Dict[str, Any]]:
        """
        Simple Keyword Search (Placeholder for Vector Search).
        Finds past logs that contain the query string.
        """
        results = []
        # Search backwards (newest first) to prioritize recent context
        for entry in reversed(self.long_term["logs"]):
            if query.lower() in entry["message"].lower():
                results.append(entry)
                if len(results) >= limit:
                    break
        return results

    def save_memory(self) -> None:
        """Save long-term memory to disk."""
        try:
            self.memory_file.parent.mkdir(parents=True, exist_ok=True)
            with open(self.memory_file, 'w', encoding='utf-8') as f:
                json.dump(self.long_term, f, indent=2, ensure_ascii=False)
        except Exception as e:
            logger.error(f"Failed to save memory: {e}")
            
    def load_memory(self) -> None:
        """Load long-term memory from disk."""
        try:
            if self.memory_file.exists():
                with open(self.memory_file, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                    if isinstance(data, dict):
                        self.long_term = data
                        if "logs" not in self.long_term:
                            self.long_term["logs"] = []
                    else:
                        self.long_term = {"logs": []}

                    # Hydrate Short-Term RAM from Disk
                    self.short_term = self.long_term["logs"][-10:]
                logger.info(f"Memory loaded from {self.memory_file}")
            else:
                logger.info("Starting with empty memory")
                self.long_term = {"logs": []}
                self.short_term = []
        except Exception as e:
            logger.error(f"Failed to load memory: {e}")
            self.long_term = {"logs": []}
            self.short_term = []