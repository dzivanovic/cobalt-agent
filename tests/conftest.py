"""
Pytest Configuration
Allows tests to import modules from the main directory and loads Environment Variables.
"""
import sys
import os
import pytest
from dotenv import load_dotenv

# 1. LOAD SECRETS (Crucial Step)
# This forces the test runner to read your .env file
load_dotenv()

# 2. ADD SOURCE CODE TO PATH
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

@pytest.fixture
def mock_config():
    """Provides a standard mock configuration for tests."""
    return {
        "strategies": {
            "second_day_play": {
                "active": True,
                "scoring": {
                    "base_score": 50,
                    "high_rvol_threshold": 3.0,
                    "high_rvol_points": 20, 
                    "base_rvol_points": 10,
                    "gap_up_points": 5,
                    "live_rvol_multiplier": 5.0,
                    "spy_correlation_weight": 10.0,
                    "resistance_penalty": -20.0,
                    "time_decay_per_min": -0.5
                }
            }
        }
    }