"""
The Strategos Agent (Tactical Department Head)
Responsible for:
1. Market Data Retrieval (FinanceTool)
2. Strategy Execution (Playbook)
"""
from typing import Optional
from loguru import logger
from cobalt_agent.tools.finance import FinanceTool
from cobalt_agent.brain.playbook import Playbook

class Strategos:
    """
    The Quantitative Trading Engine.
    Routes raw data requests or executes full strategy scans.
    """
    
    def __init__(self):
        self.finance = FinanceTool()
        self.playbook = Playbook() 
        logger.info(f"⚔️ Strategos Online | Strategies Loaded: {len(self.playbook.strategies)}")

    def run(self, task: str) -> str:
        """
        The main entry point for the Tactical Department.
        
        Args:
            task: The ticker symbol (e.g., 'NVDA') or a specific command.
        """
        # 1. Clean the input (extract ticker)
        ticker = task.split()[0].strip(".,!?").upper()
        
        logger.info(f"Strategos analyzing: {ticker}")
        
        try:
            # CHECK: If user asks for "Strategies", show the menu
            if "STRATEGY" in ticker or "PLAYBOOK" in ticker:
                return self.playbook.list_strategies()
            
            # STEP 1: Get Raw Market Data (The Finance Tool)
            market_data_obj = self.finance.run(ticker)
            
            # STEP 2: Convert to Dictionary
            # The Strategy Engine needs a clean dict, not a Pydantic model
            if hasattr(market_data_obj, 'dict'):
                market_data_dict = market_data_obj.dict()
            elif hasattr(market_data_obj, 'model_dump'):
                market_data_dict = market_data_obj.model_dump()
            else:
                market_data_dict = market_data_obj.__dict__

            # STEP 3: RUN THE PLAYBOOK ENGINE
            # This loops through all active strategies and calculates scores
            strategy_output = self.playbook.run_all(market_data_dict)
            
            # STEP 4: Return Combined Intelligence
            return f"{market_data_obj}\n\n[⚔️ Strategy Scan]\n{strategy_output}"
            
        except Exception as e:
            logger.error(f"Strategos failed on {ticker}: {e}")
            return f"Tactical Error: {e}"