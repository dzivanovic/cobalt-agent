"""
Pytest Configuration
Allows tests to import modules from the main directory and loads Environment Variables.
"""
import sys
import os
import pytest
from unittest.mock import patch, MagicMock
from dotenv import load_dotenv

# 1. LOAD SECRETS (Crucial Step)
# This forces the test runner to read your .env file
load_dotenv()

# 2. ADD SOURCE CODE TO PATH
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

@pytest.fixture(autouse=True)
def mock_postgres_memory():
    """Automatically mock PostgresMemory to prevent live DB connections in tests.
    
    This fixture patches the psycopg.connect function at the module level to prevent
    actual database connections. Tests that need database functionality should use
    the postgres_memory fixture in test_postgres_graph.py which provides more
    granular mocking.
    """
    with patch('cobalt_agent.memory.postgres.psycopg.connect') as mock_connect:
        # Create a mock connection that can be used by tests
        mock_cursor = MagicMock()
        mock_cursor.execute.return_value = mock_cursor
        mock_cursor.fetchone.return_value = None
        mock_cursor.fetchall.return_value = []
        mock_conn = MagicMock()
        mock_conn.cursor.return_value = mock_cursor
        mock_conn.execute.return_value = mock_cursor
        mock_conn.commit.return_value = None
        mock_connect.return_value = mock_conn
        yield mock_conn


@pytest.fixture
def temp_vault_path():
    """Create a temporary vault file path for testing (file doesn't exist initially)."""
    import tempfile
    from pathlib import Path
    
    with tempfile.NamedTemporaryFile(suffix='.vault', delete=False) as f:
        path = f.name
    
    # Delete the file so it doesn't exist when tests run
    Path(path).unlink(missing_ok=True)
    
    yield path
    
    # Cleanup after test
    Path(path).unlink(missing_ok=True)


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


# Note: The postgres_memory fixture in test_postgres_graph.py handles psycopg.connect mocking
# This autouse fixture only mocks what's needed for other tests that don't use postgres_memory
# @pytest.fixture(autouse=True)
# def mock_postgres_memory():
#     """Automatically mock PostgresMemory to prevent live DB connections in tests."""
#     with patch('cobalt_agent.memory.postgres.PostgresMemory.__init__', return_value=None):
#         with patch('cobalt_agent.memory.postgres.PostgresMemory._init_db'):
#             with patch('cobalt_agent.memory.postgres.PostgresMemory._get_conn'):
#                 yield
