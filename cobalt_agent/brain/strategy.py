"""
The Strategy Interface (The Contract)
All trading strategies must inherit from this class.
This enforces a standard structure for the Backtester and Live Engine.
"""
from abc import ABC, abstractmethod
from typing import Dict, Any, Optional
from datetime import datetime

class Strategy(ABC):
    """
    Abstract Base Class for all Cobalt Strategies.
    """
    
    def __init__(self, config: Dict[str, Any]):
        """
        Initialize with specific parameters from strategies.yaml.
        """
        self.config = config
        self.name = config.get("name", "Unknown Strategy")

    @abstractmethod
    def analyze(self, market_data: Any) -> Dict[str, Any]:
        """
        The Core Logic.
        Args:
            market_data: A clean object containing Price, Volume, VWAP, etc.
        Returns:
            Dict containing:
            - 'signal': 'BUY', 'SELL', or 'WAIT'
            - 'confidence': 0.0 to 1.0 (The 'T-Shirt Size')
            - 'stop_loss': Price level
            - 'target': Price level
            - 'reason': Text explanation
        """
        pass

    def check_time_window(self, current_time_str: str = None) -> bool:
        """
        Helper: Checks if we are allowed to trade right now.
        """
        if not current_time_str:
            current_time_str = datetime.now().strftime("%H:%M")
            
        window = self.config.get("time_window", {})
        start = window.get("start", "00:00")
        end = window.get("end", "23:59")
        
        # Simple string comparison works for HH:MM format (24h)
        return start <= current_time_str <= end