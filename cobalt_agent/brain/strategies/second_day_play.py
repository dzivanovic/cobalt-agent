"""
Second Day Play Strategy (Scoring Engine)
Logic:
Generates a "Math Package" for the Ion HUD based on Day 1 analysis.
Does NOT execute trades. It defines the 'Rules of Engagement' for the day.
"""
from typing import Dict, Any
from cobalt_agent.brain.strategy import Strategy

class SecondDayPlay(Strategy):
    def analyze(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Analyzes Day 1 Data to generate a Scoring Profile.
        Returns a JSON-serializable dict defining the HUD configuration.
        """
        # Initialize the HUD Package
        profile = {
            "strategy": self.name,
            "status": "WATCH",  # Default
            "base_score": 50,   # Neutral start
            "setup_quality": "C",
            "levels": {},
            "hud_rules": {}     # The 'Math' for Ion
        }

        # 1. Check Time Window
        if not self.check_time_window():
            profile["status"] = "SLEEP"
            profile["reason"] = "Outside Execution Window"
            return profile

        # 2. Extract Data (Safe Parsing)
        try:
            prev_high = data.get('prev_high', 0)
            prev_low = data.get('prev_low', 0)
            prev_close = data.get('previous_close', 0)
            prev_vol = data.get('prev_volume', 0)
            avg_vol = data.get('avg_volume', 1) 
            atr = data.get('atr', 0)
            
            # Day 2 Open (Current Data)
            day_open = data.get('open', 0)
            # cur_price = data.get('current_price', 0) # Unused in prep phase
        except Exception as e:
            profile["status"] = "ERROR"
            profile["reason"] = f"Data Error: {e}"
            return profile

        # --- STEP A: CALCULATE BASE SCORE (Static Quality) ---
        
        score = 50 # Start at 50
        reasons = []

        # 1. RVOL Check (Momentum)
        day1_rvol = 0
        if avg_vol > 0:
            day1_rvol = prev_vol / avg_vol
            
        if day1_rvol > 2.0:
            score += 15
            reasons.append("High RVOL (>2.0)")
        elif day1_rvol > 1.5:
            score += 10
            reasons.append("Decent RVOL (>1.5)")
        else:
            score -= 10
            reasons.append("Low Volume")

        # 2. Extension Check (Closing Strength)
        day1_range = prev_high - prev_low
        if day1_range > 0:
            rel_close = (prev_close - prev_low) / day1_range
            if rel_close > 0.8:
                score += 10
                reasons.append("Strong Close (Top 20%)")
            elif rel_close < 0.5:
                score -= 20
                reasons.append("Weak Close (Bottom 50%)")

        # 3. Gap Check (Day 2 Context)
        gap_size = abs(day_open - prev_close)
        max_gap = day1_range * 0.33
        if gap_size < max_gap:
            score += 10 # Good, small gap
            reasons.append("Healthy Small Gap")
        else:
            score -= 30 # Gap too big (Chase risk)
            reasons.append("Extended Gap (Chase Risk)")

        profile["base_score"] = min(max(score, 0), 100)
        profile["reason"] = ", ".join(reasons)
        
        # Grading
        if score >= 80: profile["setup_quality"] = "A+"
        elif score >= 70: profile["setup_quality"] = "A"
        elif score >= 60: profile["setup_quality"] = "B"
        else: profile["setup_quality"] = "C"

        # --- STEP B: DEFINE HUD RULES (The Dynamic Math) ---
        # Ion will use these multipliers on live data
        
        profile["levels"] = {
            "trigger": prev_high,
            "invalidation": prev_low + (day1_range * 0.5), # Lose half the day
            "target_1": prev_high + day1_range
        }
        
        profile["hud_rules"] = {
            "rvol_multiplier": {"threshold": 3.0, "bonus": 10},
            "vwap_check": {"condition": "price > vwap", "penalty_if_false": -15},
            "proximity_alert": 0.05
        }
        
        return profile