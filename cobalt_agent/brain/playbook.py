"""
The Playbook Registry
Loads trading strategies and parameters from strategies.yaml.
Executes the strategy logic against market data.
"""
import yaml
import json
from pathlib import Path
from typing import Dict, Any, Optional
from loguru import logger

# Import your strategies here
from cobalt_agent.brain.strategies.second_day_play import SecondDayPlay

class Playbook:
    """
    Manages the active trading strategies and their parameters.
    """
    
    def __init__(self, config_path: str = "configs/strategies.yaml"):
        self.config_data = self._load_config(config_path)
        self.strategies = {}
        self._initialize_strategies()
        
    def _load_config(self, path_str: str) -> Dict[str, Any]:
        """Loads the YAML config."""
        path = Path(path_str)
        # Handle running from root or inside module
        if not path.exists():
            path = Path(__file__).parent.parent.parent / path_str
            
        if not path.exists():
            logger.warning(f"⚠️ Strategy Config not found at {path}")
            return {}

        try:
            with open(path, "r") as f:
                data = yaml.safe_load(f)
                return data.get("strategies", {})
        except Exception as e:
            logger.error(f"❌ Failed to load Playbook Config: {e}")
            return {}

    def _initialize_strategies(self):
        """Hydrates the Strategy classes with their Configs."""
        # Map YAML keys to Python Classes
        class_map = {
            "second_day_play": SecondDayPlay,
            # Future: "gap_and_go": GapAndGo
        }

        for key, params in self.config_data.items():
            if key in class_map:
                try:
                    # Instantiate the class with its specific config
                    strategy_instance = class_map[key](params)
                    self.strategies[key] = strategy_instance
                    logger.debug(f"Loaded strategy: {key}")
                except Exception as e:
                    logger.error(f"Failed to init strategy {key}: {e}")

    def get_strategy(self, name: str):
        return self.strategies.get(name)

    def list_strategies(self) -> str:
        """Returns a formatted list of ACTIVE (Loaded) strategies."""
        if not self.strategies:
            return "No strategies loaded (Check strategies.yaml)."
        
        output = "📜 **Active Playbook:**\n"
        for key, strategy in self.strategies.items():
            cfg = strategy.config
            output += f"- **{cfg['name']}**: {cfg['direction']} ({cfg['time_window']['start']}-{cfg['time_window']['end']})\n"
        return output
        
    def run_all(self, market_data: Dict[str, Any]) -> str:
        """
        Runs ALL strategies against the incoming data.
        Returns a summary string of Scoring Profiles.
        """
        results = []
        
        for name, strategy in self.strategies.items():
            try:
                # Run the math
                profile = strategy.analyze(market_data)
                
                # Format the output for the CLI
                # We show the Name, Base Score, and Quality
                status = profile.get("status", "UNKNOWN")
                base_score = profile.get("base_score", 0)
                quality = profile.get("setup_quality", "N/A")
                reason = profile.get("reason", "")
                
                # Create a mini-report
                report = f"**{name}** [{status}]\n"
                report += f"   • Score: {base_score}/100 ({quality})\n"
                report += f"   • Logic: {reason}\n"
                
                # If there are HUD rules, mention them
                if profile.get("hud_rules"):
                    rules_count = len(profile["hud_rules"])
                    report += f"   • HUD Config: {rules_count} dynamic rules active\n"
                
                results.append(report)
                
            except Exception as e:
                logger.error(f"Error running {name}: {e}")
                results.append(f"**{name}**: Error ({e})")
                
        if not results:
            return "No active strategies found."
            
        return "\n".join(results)