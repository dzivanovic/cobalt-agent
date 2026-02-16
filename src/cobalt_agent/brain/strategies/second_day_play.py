"""
Second Day Play - Strategy Logic
Author: Cobalt AI
Context: Phase 3 (Tactical)

Refactored to pull scoring rules and thresholds dynamically from strategies.yaml.
"""
from datetime import datetime

class SecondDayPlay:
    def __init__(self, config: dict = None):
        # Fallback to empty dict if None, but usually this comes from strategies.yaml
        self.config = config or {}
        
        # Load Parameters from Config (or defaults if missing)
        self.params = self.config.get("parameters", {})
        self.scoring = self.config.get("scoring", {})
        
        self.name = self.config.get("name", "SecondDayPlay")
        self.version = "1.1"

    def analyze(self, ticker: str, market_data: dict) -> dict:
        """
        Takes raw market data and returns the Scoring Profile (JSON).
        """
        
        # 1. UNPACK DATA
        y_close = market_data.get('yesterday_close', 0)
        y_vol = market_data.get('yesterday_volume', 0)
        avg_vol = market_data.get('average_volume', 1) 
        today_open = market_data.get('today_open', 0)
        pm_high = market_data.get('pre_market_high', 0)
        
        # 2. VALIDATION (The Gatekeeper)
        y_rvol = y_vol / avg_vol if avg_vol else 0
        
        # Rule: Min RVOL (from config)
        min_rvol = self.params.get("min_rvol", 1.5)
        if y_rvol < min_rvol:
            return {
                "ticker": ticker,
                "strategy": self.name,
                "status": "REJECTED",
                "reason": f"Low Relative Volume Yesterday (RVOL: {y_rvol:.2f} < {min_rvol})"
            }

        # Rule: Gap Down Rejection
        if today_open < (y_close * 0.98):
             return {
                "ticker": ticker,
                "strategy": self.name,
                "status": "REJECTED",
                "reason": "Gap Down - Momentum Lost"
            }

        # 3. CALCULATE ZONES
        entry_price = pm_high + 0.05
        stop_loss = y_close - 0.20
        risk = entry_price - stop_loss
        target = entry_price + (risk * 2)

        # 4. SCORING ENGINE (Dynamic)
        # Instead of hardcoding "50" or "+10", we look them up.
        current_score = self.scoring.get("base_score", 50)
        
        # RVOL Modifiers
        high_rvol_thresh = self.scoring.get("high_rvol_threshold", 3.0)
        
        if y_rvol >= high_rvol_thresh:
            current_score += self.scoring.get("high_rvol_points", 15)
        elif y_rvol >= min_rvol:
            current_score += self.scoring.get("base_rvol_points", 10)
            
        # Gap Modifiers
        if today_open > y_close:
            current_score += self.scoring.get("gap_up_points", 10)
        
        # 5. CONSTRUCT THE MATH PACKAGE
        return {
            "timestamp": datetime.now().isoformat(),
            "ticker": ticker,
            "strategy": self.name,
            "status": "ACTIVE_WATCH",
            "direction": "LONG",
            "zones": {
                "entry": round(entry_price, 2),
                "stop": round(stop_loss, 2),
                "target": round(target, 2),
                "risk_per_share": round(risk, 2)
            },
            "scoring_engine": {
                "base_score": current_score,
                # Pass instructions to Ion (Windows)
                "modifiers": {
                    "live_rvol_multiplier": self.scoring.get("live_rvol_multiplier", 5.0),
                    "spy_correlation_weight": self.scoring.get("spy_correlation_weight", 10.0),
                    "resistance_penalty": self.scoring.get("resistance_penalty", -20.0),
                    "time_decay_per_min": self.scoring.get("time_decay_per_min", -0.5)
                }
            },
            "abort_conditions": [
                f"price < {stop_loss}",
                "volume_run_rate < 50%" 
            ]
        }