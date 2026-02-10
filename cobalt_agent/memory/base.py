"""
Memory Interface (The Contract)
Defines how Agents interact with memory, regardless of storage (JSON vs Postgres).
"""
from abc import ABC, abstractmethod
from typing import List, Dict, Any

class MemoryProvider(ABC):
    """
    Abstract Base Class for Memory.
    Any memory system (JSON, SQL, Vector) MUST implement these methods.
    """

    @abstractmethod
    def add_log(self, message: str, source: str = "System", data: Dict = None):
        """Record an event or thought."""
        pass

    @abstractmethod
    def get_context(self, limit: int = 10) -> List[Dict[str, Any]]:
        """Get recent conversation history (Short Term RAM)."""
        pass

    @abstractmethod
    def search(self, query: str, limit: int = 5) -> List[Dict[str, Any]]:
        """
        Find relevant memories based on meaning/content.
        (For JSON, this will be keyword search. For Postgres, Vector search.)
        """
        pass