"""
Strategy Test Suite
Verifies that trading logic respects the configuration rules.
"""
import pytest
from cobalt_agent.brain.strategies.second_day_play import SecondDayPlay

# --- FIXTURES (Reusable Data) ---

@pytest.fixture
def mock_config():
    """Simulates the data from strategies.yaml"""
    return {
        "name": "Second Day Play",
        "parameters": {
            "min_rvol": 1.5,
            "gap_percentage": 2.0
        },
        "scoring": {
            "base_score": 50,
            "high_rvol_threshold": 3.0,
            "high_rvol_points": 20, # Custom value for test to verify logic
            "base_rvol_points": 10,
            "gap_up_points": 5
        }
    }

@pytest.fixture
def mock_nvda_data():
    """A perfect setup: High Volume, Gap Up."""
    return {
        "yesterday_close": 140.00,
        "yesterday_volume": 50_000_000,
        "average_volume": 10_000_000, # RVOL = 5.0 (High)
        "today_open": 141.50,         # Gap Up
        "pre_market_high": 142.00
    }

@pytest.fixture
def mock_weak_data():
    """A failed setup: Low Volume."""
    return {
        "yesterday_close": 50.00,
        "yesterday_volume": 1_200_000,
        "average_volume": 1_000_000,  # RVOL = 1.2 (Fail)
        "today_open": 50.50,
        "pre_market_high": 51.00
    }

# --- TESTS ---

def test_second_day_play_initialization(mock_config):
    """Does the strategy load the config correctly?"""
    strategy = SecondDayPlay(mock_config)
    assert strategy.params["min_rvol"] == 1.5
    assert strategy.scoring["high_rvol_points"] == 20

def test_valid_setup_scoring(mock_config, mock_nvda_data):
    """
    Test Math:
    Base (50) + High RVOL (20) + Gap Up (5) = 75
    """
    strategy = SecondDayPlay(mock_config)
    result = strategy.analyze("NVDA", mock_nvda_data)
    
    assert result["status"] == "ACTIVE_WATCH"
    assert result["scoring_engine"]["base_score"] == 75
    assert result["zones"]["entry"] == 142.05

def test_rejection_logic(mock_config, mock_weak_data):
    """Ensure weak stocks are rejected."""
    strategy = SecondDayPlay(mock_config)
    result = strategy.analyze("WEAK", mock_weak_data)
    
    assert result["status"] == "REJECTED"
    assert "Low Relative Volume" in result["reason"]