"""
Logic Lab - Strategy Tester (Fixed)
Simulates the 'Mac Studio' generating a Scoring Profile.
"""
import sys
import os
import json

# Fix path to allow importing from cobalt_agent
sys.path.append(os.getcwd())

from cobalt_agent.brain.strategies.second_day_play import SecondDayPlay

def run_simulation():
    print("🧪 Starting Logic Lab: Second Day Play Simulation...\n")
    
    # --- SCENARIO 1: The Perfect Setup (NVDA Earnings) ---
    mock_market_data_good = {
        "yesterday_close": 140.00,
        "yesterday_volume": 50_000_000,
        "average_volume": 10_000_000, # RVOL = 5.0 (Huge)
        "today_open": 141.50,         # Gapping Up
        "pre_market_high": 142.00     # The Breakout Level
    }

    # --- SCENARIO 2: The Failed Setup (Weak Volume) ---
    mock_market_data_bad = {
        "yesterday_close": 50.00,
        "yesterday_volume": 1_200_000,
        "average_volume": 1_000_000,  # RVOL = 1.2 (Too Low)
        "today_open": 50.50,
        "pre_market_high": 51.00
    }

    # --- THE FIX: Create a Mock Config ---
    # The Strategy class expects a configuration dictionary (usually from strategies.yaml)
    mock_config = {
        "name": "SecondDayPlay",
        "description": "Continuation breakout logic",
        "parameters": {
            "min_rvol": 1.5,
            "gap_percentage": 2.0
        }
    }

    # Initialize with the config
    try:
        strategy = SecondDayPlay(mock_config)
    except TypeError:
        # Fallback if your version doesn't take config (just in case)
        strategy = SecondDayPlay()

    # TEST 1: Run the Good Data
    print(f"🔹 Analyzing Ticker: NVDA (Scenario: Earnings Blowout)")
    profile_good = strategy.analyze("NVDA", mock_market_data_good)
    print(json.dumps(profile_good, indent=4))
    
    print("\n" + "-"*50 + "\n")

    # TEST 2: Run the Bad Data
    print(f"🔹 Analyzing Ticker: WEAK (Scenario: Low Volume Pump)")
    profile_bad = strategy.analyze("WEAK", mock_market_data_bad)
    print(json.dumps(profile_bad, indent=4))

if __name__ == "__main__":
    run_simulation()