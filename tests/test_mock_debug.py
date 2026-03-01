"""
Debug test to verify the MockConnection setup is correct.
"""
import os
import pytest
from unittest.mock import patch, MagicMock

from cobalt_agent.memory.postgres import PostgresMemory


class MockCursor:
    """Mock cursor for testing database operations."""
    
    def __init__(self):
        self.rowcount = 0
        self.execute_calls = []
        self._data = {}
        self._edges = {}
        self._properties = {}
    
    def execute(self, query: str, params: tuple = None):
        """Mock execute method that parses and handles SQL queries."""
        self.execute_calls.append((query, params))
        self._params = params
        return self
    
    def fetchone(self):
        """Mock fetchone method."""
        return getattr(self, '_current_row', None)
    
    def fetchall(self):
        """Mock fetchall method."""
        return getattr(self, '_all_rows', [])
    
    def commit(self):
        """Mock commit method."""
        pass


class MockConnection:
    """Mock connection for testing database operations."""
    
    def __init__(self, cursor: MockCursor):
        self.cursor = cursor
        
    def cursor(self):
        return self.cursor
    
    def __enter__(self):
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        pass
    
    def execute(self, query: str, params: tuple = None):
        """Mock execute method that delegates to cursor."""
        return self.cursor.execute(query, params)
    
    def commit(self):
        """Mock commit method."""
        pass


@pytest.fixture
def mock_config():
    """Create a mock config with the required fields for PostgresMemory."""
    mock = MagicMock()
    
    postgres = MagicMock()
    postgres.host = "localhost"
    postgres.port = 5432
    postgres.db = "cobalt_memory_test"
    postgres.user = "postgres"
    postgres.password = "cobalt_password"
    
    mock.postgres = postgres
    
    browser = MagicMock()
    browser.allowed_domains = ["finviz.com", "tradingview.com"]
    mock.browser = browser
    
    network = MagicMock()
    network.nodes = {
        "cortex": MagicMock(role="primary_inference"),
        "edge_mobile": MagicMock(role="client"),
    }
    mock.network = network
    
    mock.system = MagicMock(debug_mode=True, version="0.5.0")
    mock.llm = MagicMock(model_name="gemini/gemini-1.5-pro")
    mock.persona = MagicMock(name="Cobalt", roles=[], skills=[], tone=[], directives=[])
    mock.trading_rules = None
    mock.active_profile = None
    mock.models = None
    mock.mattermost = MagicMock(approval_channel="cobalt-approvals", approval_team="cobalt-team")
    mock.vault = None
    mock.prompts = MagicMock(system=None, scheduler=None, ops=None, engineering=None, proposal=None, routing=None, orchestrator=None)
    
    return mock


def test_mock_connection_debug(mock_config):
    """Test that the mock connection is properly set up."""
    os.environ["POSTGRES_PASSWORD"] = "cobalt_password"
    
    mock_cursor = MockCursor()
    mock_conn = MockConnection(mock_cursor)
    
    # Patch psycopg.connect in the cobalt_agent.memory.postgres module
    with patch("cobalt_agent.memory.postgres.psycopg.connect", return_value=mock_conn):
        pm = PostgresMemory()
        # Store reference to mock_cursor on pm for tests to access
        pm._mock_cursor = mock_cursor
        
    # Check how many execute calls were made
    print(f"\nExecute calls: {len(pm._mock_cursor.execute_calls)}")
    for i, (query, params) in enumerate(pm._mock_cursor.execute_calls):
        print(f"  Call {i}: {query[:80] if len(query) > 80 else query}...")
    
    # Verify graph_nodes table was created
    query_strings = [q[0] for q in pm._mock_cursor.execute_calls]
    query_text = " ".join(query_strings).upper()
    
    assert "GRAPH_NODES" in query_text, f"graph_nodes table should be created. Queries: {query_strings}"
    assert "HITL_PROPOSALS" in query_text, f"hitl_proposals table should be created"


if __name__ == "__main__":
    pytest.main([__file__, "-v", "-s"])