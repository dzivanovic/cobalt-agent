"""
Postgres Graph Memory Tests
Tests the Entity-Relationship (ER) Graph structure implementation.

Graph Database Schema:
- graph_nodes: Stores entities (Ticker, Material, Strategy, etc.)
- graph_edges: Stores relationships between nodes (TRIGGERED_STRATEGY, IS_USED_IN, etc.)
"""
import os
import uuid
import json
import pytest
from typing import Optional, List, Tuple, Any
from unittest.mock import patch, MagicMock, Mock, call

from cobalt_agent.memory.postgres import PostgresMemory


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


class MockCursor:
    """Mock cursor for testing database operations."""
    
    def __init__(self):
        self.rowcount = 0
        self._data = {}  # In-memory storage for graph nodes: (entity_type, name) -> {id, properties}
        self._edges = {}  # In-memory storage for graph edges: (source_id, target_id, relationship) -> edge_id
        self._current_row = None
        self._all_rows = []
        self.execute_calls = []
        self._properties = {}  # In-memory storage for node properties
    
    def execute(self, query: str, params: Tuple = None):
        """Mock execute method that parses and handles SQL queries."""
        self.execute_calls.append((query, params))
        self._params = params
        self._current_row = None
        self._all_rows = []
        
        # Normalize query for comparison (handle multi-line and different casing)
        query_upper = query.upper()
        
        # Handle INSERT INTO graph_nodes - store the generated ID and properties
        if "INSERT INTO GRAPH_NODES" in query_upper and params:
            node_id = params[0]  # First param is the UUID
            entity_type = params[1]
            name = params[2]
            properties = params[3]  # Fourth param is the properties (JSONB)
            self._data[(entity_type, name)] = node_id
            self._properties[node_id] = json.loads(properties) if properties else {}
        
        # Handle INSERT INTO graph_edges - store the generated ID
        elif "INSERT INTO GRAPH_EDGES" in query_upper and params:
            edge_id = params[0]  # First param is the UUID
            source_id = params[1]
            target_id = params[2]
            relationship = params[3]
            self._edges[(source_id, target_id, relationship)] = edge_id
        
        # Handle UPDATE graph_nodes
        elif "UPDATE GRAPH_NODES" in query_upper and params:
            # Update the properties in our mock storage
            if len(params) >= 3 and params[2] in self._properties:
                self._properties[params[2]] = json.loads(params[0]) if params[0] else {}
        
        # Handle UPDATE graph_edges
        elif "UPDATE GRAPH_EDGES" in query_upper and params:
            # params are: properties, created_at, id
            pass
        
        # Simulate SELECT queries for upsert_node first check
        elif "SELECT ID FROM GRAPH_NODES" in query_upper and "WHERE ENTITY_TYPE" in query_upper and params:
            entity_type = params[0] if len(params) > 0 else None
            name = params[1] if len(params) > 1 else None
            if entity_type and name:
                node_key = (entity_type, name)
                if node_key in self._data:
                    self._current_row = (uuid.UUID(self._data[node_key]),)
                else:
                    self._current_row = None
            else:
                self._current_row = None
        
        # Simulate SELECT for get_node
        elif "SELECT ID, ENTITY_TYPE, NAME, PROPERTIES, CREATED_AT, UPDATED_AT" in query_upper and params:
            entity_type = params[0]
            name = params[1]
            node_key = (entity_type, name)
            if node_key in self._data:
                node_id = self._data[node_key]
                properties = self._properties.get(node_id, {})
                self._current_row = (
                    uuid.UUID(node_id),
                    entity_type,
                    name,
                    json.dumps(properties),
                    None,
                    None
                )
            else:
                self._current_row = None
        
        # Simulate SELECT for upsert_edge first check
        elif "SELECT ID FROM GRAPH_EDGES" in query_upper and params:
            source_id = str(params[0]) if params and len(params) > 0 else ""
            target_id = str(params[1]) if params and len(params) > 1 else ""
            relationship = str(params[2]) if params and len(params) > 2 else ""
            
            edge_key = (source_id, target_id, relationship)
            if edge_key in self._edges:
                self._current_row = (uuid.UUID(self._edges[edge_key]),)
            else:
                self._current_row = None
        
        # Simulate SELECT for get_edges
        elif "SELECT ID, SOURCE_ID, TARGET_ID, RELATIONSHIP, PROPERTIES, CREATED_AT" in query_upper and params:
            self._all_rows = []
            
            if params:
                node_id = str(params[0]) if params else ""
                
                # Check if query is for 'out' direction (WHERE source_id = %s)
                if "WHERE SOURCE_ID =" in query_upper and "OR" not in query_upper:
                    for edge_key, edge_id in self._edges.items():
                        src, tgt, rel = edge_key
                        if src == node_id:
                            self._all_rows.append((
                                uuid.UUID(edge_id),
                                uuid.UUID(src),
                                uuid.UUID(tgt),
                                rel,
                                '{}',
                                None
                            ))
                
                # Check if query is for 'in' direction (WHERE target_id = %s)
                elif "WHERE TARGET_ID =" in query_upper and "OR" not in query_upper:
                    for edge_key, edge_id in self._edges.items():
                        src, tgt, rel = edge_key
                        if tgt == node_id:
                            self._all_rows.append((
                                uuid.UUID(edge_id),
                                uuid.UUID(src),
                                uuid.UUID(tgt),
                                rel,
                                '{}',
                                None
                            ))
                
                # Check if query is for 'both' direction (WHERE source_id = %s OR target_id = %s)
                elif "WHERE SOURCE_ID =" in query_upper and "OR TARGET_ID =" in query_upper:
                    for edge_key, edge_id in self._edges.items():
                        src, tgt, rel = edge_key
                        if src == node_id or tgt == node_id:
                            self._all_rows.append((
                                uuid.UUID(edge_id),
                                uuid.UUID(src),
                                uuid.UUID(tgt),
                                rel,
                                '{}',
                                None
                            ))
            
            self._current_row = None
            
        return self
    
    def fetchone(self) -> Optional[Any]:
        """Mock fetchone method."""
        return self._current_row
    
    def fetchall(self) -> List[Any]:
        """Mock fetchall method."""
        return self._all_rows
    
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
    
    def execute(self, query: str, params: Tuple = None):
        """Mock execute method that delegates to cursor."""
        return self.cursor.execute(query, params)
    
    def commit(self):
        """Mock commit method."""
        pass


@pytest.fixture
def postgres_memory(mock_config):
    """Create a PostgresMemory instance with mocked database connection.
    
    This fixture uses the autouse fixture's patched psycopg.connect to ensure
    all database operations use the mocked connection without making real DB calls.
    """
    os.environ["POSTGRES_PASSWORD"] = "cobalt_password"
    
    # Create mock cursor for executing queries
    mock_cursor = MockCursor()
    
    # Create a mock connection object that behaves like psycopg connection
    mock_conn = MockConnection(mock_cursor)
    
    # Patch psycopg.connect to return our mock connection (this is what _get_conn uses)
    with patch('cobalt_agent.memory.postgres.psycopg.connect', return_value=mock_conn):
        pm = PostgresMemory()
        # Store reference to mock_cursor on pm for tests to access
        pm._mock_cursor = mock_cursor
        yield pm


class TestGraphDatabaseSchema:
    """Test suite for Graph Database Schema."""

    def test_graph_tables_initialized(self, postgres_memory):
        """Test that graph tables (graph_nodes, graph_edges) are properly initialized."""
        pm = postgres_memory
        
        # Verify that _init_graph_tables was called during __init__
        # During init, we execute CREATE TABLE statements
        assert len(pm._mock_cursor.execute_calls) > 0, "At least one execute call should be made"
        
        query_strings = [q[0] for q in pm._mock_cursor.execute_calls]
        query_text = " ".join(query_strings).upper()
        
        # Check that CREATE TABLE statements were executed
        assert "GRAPH_NODES" in query_text, "graph_nodes table should be created"
        assert "GRAPH_EDGES" in query_text, "graph_edges table should be created"
        
        # Check for UNIQUE constraints in CREATE statements
        graph_nodes_create = [q for q in query_strings if "graph_nodes" in q.lower()]
        assert any("UNIQUE" in q.upper() and "entity_type" in q and "name" in q for q in graph_nodes_create), \
            "graph_nodes should have UNIQUE constraint on (entity_type, name)"
        
        graph_edges_create = [q for q in query_strings if "graph_edges" in q.lower()]
        assert any("UNIQUE" in q.upper() and "source_id" in q and "target_id" in q for q in graph_edges_create), \
            "graph_edges should have UNIQUE constraint on (source_id, target_id, relationship)"


class TestUpsertNode:
    """Test suite for upsert_node operation."""

    def test_upsert_node_creates_new(self, postgres_memory):
        """Test that upsert_node correctly creates new nodes."""
        pm = postgres_memory
        
        # Generate a mock UUID for the new node
        test_uuid = "12345678-1234-1234-1234-123456789abc"
        
        # Mock uuid.uuid4 to return our test UUID
        with patch("cobalt_agent.memory.postgres.uuid.uuid4", return_value=uuid.UUID(test_uuid)):
            node_id = pm.upsert_node('Ticker', 'TEST_TSLA', {'price': 150.0, 'sector': 'Auto'})
        
        assert node_id == test_uuid, f"Expected {test_uuid}, got {node_id}"
        
        # Verify node is stored in mock data
        assert ('Ticker', 'TEST_TSLA') in pm._mock_cursor._data
        
        # Verify INSERT query was executed
        insert_queries = [q for q in pm._mock_cursor.execute_calls if "INSERT INTO graph_nodes" in q[0]]
        assert len(insert_queries) >= 1, "INSERT query should be executed"
        
        query, params = insert_queries[0]
        assert "entity_type" in query
        assert "name" in query
        assert params[1] == 'Ticker'
        assert params[2] == 'TEST_TSLA'

    def test_upsert_node_updates_existing(self, postgres_memory):
        """Test that upsert_node updates properties when node already exists."""
        pm = postgres_memory
        
        # Manually add node to mock cursor's _data so SELECT finds it
        test_uuid = "12345678-1234-1234-1234-123456789abc"
        pm._mock_cursor._data[('Strategy', 'TEST_MORNING_GAPPER')] = test_uuid
        
        # Second upsert (should update existing)
        with patch("cobalt_agent.memory.postgres.uuid.uuid4", return_value=uuid.UUID(test_uuid)):
            updated_node_id = pm.upsert_node('Strategy', 'TEST_MORNING_GAPPER', {'score': 95, 'active': True})
        
        # Verify same ID is returned
        assert updated_node_id == test_uuid
        
        # Verify UPDATE query was executed
        update_queries = [q for q in pm._mock_cursor.execute_calls if "UPDATE graph_nodes" in q[0]]
        assert len(update_queries) >= 1, "UPDATE query should be executed for duplicate"

    def test_upsert_node_returns_same_id_for_duplicate(self, postgres_memory):
        """Test that upsert_node returns the same UUID for duplicate entity_type + name."""
        pm = postgres_memory
        
        test_uuid = "12345678-1234-1234-1234-123456789abc"
        
        # Manually add node to mock cursor's _data
        pm._mock_cursor._data[('Material', 'TEST_CELLOPHANE')] = test_uuid
        
        # Second upsert (should update existing)
        with patch("cobalt_agent.memory.postgres.uuid.uuid4", return_value=uuid.UUID(test_uuid)):
            node_id_2 = pm.upsert_node('Material', 'TEST_CELLOPHANE', {'density': 0.6})
        
        # Verify same ID is returned
        assert node_id_2 == test_uuid


class TestUpsertEdge:
    """Test suite for upsert_edge operation."""

    def test_upsert_edge_creates_new(self, postgres_memory):
        """Test that upsert_edge successfully creates new edges."""
        pm = postgres_memory
        
        source_id = "11111111-1111-1111-1111-111111111111"
        target_id = "22222222-2222-2222-2222-222222222222"
        test_edge_uuid = "33333333-3333-3333-3333-333333333333"
        
        with patch("cobalt_agent.memory.postgres.uuid.uuid4", return_value=uuid.UUID(test_edge_uuid)):
            edge_id = pm.upsert_edge(source_id, target_id, 'TRIGGERED_STRATEGY', {'confidence': 0.95})
        
        assert edge_id == test_edge_uuid
        
        # Verify edge is stored in mock data
        edge_key = (source_id, target_id, 'TRIGGERED_STRATEGY')
        assert edge_key in pm._mock_cursor._edges
        
        # Verify INSERT query was executed
        insert_queries = [q for q in pm._mock_cursor.execute_calls if "INSERT INTO graph_edges" in q[0]]
        assert len(insert_queries) >= 1, "INSERT query should be executed"
        
        query, params = insert_queries[0]
        assert "source_id" in query
        assert "target_id" in query
        assert "relationship" in query
        assert params[1] == source_id
        assert params[2] == target_id
        assert params[3] == 'TRIGGERED_STRATEGY'

    def test_upsert_edge_updates_existing(self, postgres_memory):
        """Test that upsert_edge updates properties when edge already exists."""
        pm = postgres_memory
        
        source_id = "11111111-1111-1111-1111-111111111111"
        target_id = "22222222-2222-2222-2222-222222222222"
        test_edge_uuid = "33333333-3333-3333-3333-333333333333"
        
        # Manually add edge to mock cursor's _edges so SELECT finds it
        pm._mock_cursor._edges[(source_id, target_id, 'TRIGGERED_STRATEGY')] = test_edge_uuid
        
        # Second upsert (should update existing)
        with patch("cobalt_agent.memory.postgres.uuid.uuid4", return_value=uuid.UUID(test_edge_uuid)):
            updated_edge_id = pm.upsert_edge(source_id, target_id, 'TRIGGERED_STRATEGY', {'confidence': 0.85, 'notes': 'updated'})
        
        # Verify same ID is returned
        assert updated_edge_id == test_edge_uuid
        
        # Verify UPDATE query was executed
        update_queries = [q for q in pm._mock_cursor.execute_calls if "UPDATE graph_edges" in q[0]]
        assert len(update_queries) >= 1, "UPDATE query should be executed for duplicate"

    def test_upsert_edge_returns_same_id_for_duplicate(self, postgres_memory):
        """Test that upsert_edge returns the same UUID for duplicate edge."""
        pm = postgres_memory
        
        source_id = "11111111-1111-1111-1111-111111111111"
        target_id = "22222222-2222-2222-2222-222222222222"
        
        # Manually add edge to mock cursor's _edges
        edge_key = (source_id, target_id, 'TRIGGERED_STRATEGY')
        pm._mock_cursor._edges[edge_key] = "33333333-3333-3333-3333-333333333333"
        
        # Second upsert (should update existing)
        with patch("cobalt_agent.memory.postgres.uuid.uuid4", return_value=uuid.UUID("44444444-4444-4444-4444-444444444444")):
            edge_id_2 = pm.upsert_edge(source_id, target_id, 'TRIGGERED_STRATEGY', {'confidence': 0.85})
        
        assert edge_id_2 == pm._mock_cursor._edges[edge_key]


class TestGetNode:
    """Test suite for get_node operation."""

    def test_get_node_exists(self, postgres_memory):
        """Test that get_node retrieves an existing node."""
        pm = postgres_memory
        
        node_id = "12345678-1234-1234-1234-123456789abc"
        
        # Add the node to the mock cursor's data first
        pm._mock_cursor._data[('Ticker', 'TEST_TSLA')] = node_id
        
        node = pm.get_node('Ticker', 'TEST_TSLA')
        
        assert node is not None
        assert node['entity_type'] == 'Ticker'
        assert node['name'] == 'TEST_TSLA'
        assert node['id'] == node_id
        assert isinstance(node['properties'], dict)

    def test_get_node_not_exists(self, postgres_memory):
        """Test that get_node returns None for non-existent node."""
        pm = postgres_memory
        
        node = pm.get_node('Ticker', 'NON_EXISTENT_TICKER')
        
        assert node is None


class TestGetEdges:
    """Test suite for get_edges operation."""

    def test_get_edges_out_direction(self, postgres_memory):
        """Test that get_edges returns outgoing edges for 'out' direction."""
        pm = postgres_memory
        
        node_id = "12345678-1234-1234-1234-123456789abc"
        
        # Add edges to mock cursor
        edge1_id = "11111111-1111-1111-1111-111111111111"
        edge2_id = "22222222-2222-2222-2222-222222222222"
        
        pm._mock_cursor._edges[(node_id, "22222222-2222-2222-2222-222222222222", "TRIGGERED_STRATEGY")] = edge1_id
        pm._mock_cursor._edges[(node_id, "33333333-3333-3333-3333-333333333333", "ALSO_TRIGGERS")] = edge2_id
        
        edges = pm.get_edges(node_id, 'out')
        
        assert len(edges) == 2
        for edge in edges:
            assert edge['source_id'] == node_id

    def test_get_edges_in_direction(self, postgres_memory):
        """Test that get_edges returns incoming edges for 'in' direction."""
        pm = postgres_memory
        
        node_id = "22222222-2222-2222-2222-222222222222"
        source_node_id = "11111111-1111-1111-1111-111111111111"
        edge_id = "33333333-3333-3333-3333-333333333333"
        
        # Store edge where source_node_id -> node_id
        pm._mock_cursor._edges[(source_node_id, node_id, "TRIGGERED_STRATEGY")] = edge_id
        
        edges = pm.get_edges(node_id, 'in')
        
        assert len(edges) == 1
        for edge in edges:
            assert edge['target_id'] == node_id
            assert edge['source_id'] == source_node_id

    def test_get_edges_both_direction(self, postgres_memory):
        """Test that get_edges returns both incoming and outgoing edges for 'both' direction."""
        pm = postgres_memory
        
        node_id = "22222222-2222-2222-2222-222222222222"
        edge1_id = "55555555-5555-5555-5555-555555555555"
        edge2_id = "66666666-6666-6666-6666-666666666666"
        
        # Add edges with valid UUIDs
        pm._mock_cursor._edges[("11111111-1111-1111-1111-111111111111", node_id, "TRIGGERED_STRATEGY")] = edge1_id
        pm._mock_cursor._edges[(node_id, "44444444-4444-4444-4444-444444444444", "IS_USED_IN")] = edge2_id
        
        edges = pm.get_edges(node_id, 'both')
        
        assert len(edges) == 2
        edge_ids = {e['id'] for e in edges}
        assert edge1_id in edge_ids
        assert edge2_id in edge_ids

    def test_get_edges_empty_node(self, postgres_memory):
        """Test that get_edges returns empty list for node with no edges."""
        pm = postgres_memory
        
        edges = pm.get_edges("12345678-1234-1234-1234-123456789abc", 'both')
        
        assert edges == []


class TestGraphTraversal:
    """Test suite for graph traversal scenarios."""

    def test_full_graph_workflow(self, postgres_memory):
        """Test a complete workflow: create nodes, link them, and traverse the graph."""
        pm = postgres_memory
        
        # Step 1: Create Ticker node
        ticker_id = pm.upsert_node('Ticker', 'TSLA', {'price': 175.50, 'sector': 'Auto'})
        assert ticker_id is not None
        
        # Step 2: Create Strategy node
        strategy_id = pm.upsert_node('Strategy', 'Morning Gapper', {'score_threshold': 80})
        assert strategy_id is not None
        
        # Step 3: Create edge between them
        edge_id = pm.upsert_edge(ticker_id, strategy_id, 'TRIGGERED_STRATEGY', {'confidence': 0.92})
        assert edge_id is not None
        
        # Step 4: Verify node retrieval
        ticker_node = pm.get_node('Ticker', 'TSLA')
        assert ticker_node is not None
        assert ticker_node['id'] == ticker_id
        
        # Step 5: Traverse outgoing edges from Ticker
        outgoing_edges = pm.get_edges(ticker_id, 'out')
        assert len(outgoing_edges) == 1
        assert outgoing_edges[0]['relationship'] == 'TRIGGERED_STRATEGY'
        assert outgoing_edges[0]['target_id'] == strategy_id
        
        # Step 6: Traverse incoming edges to Strategy
        incoming_edges = pm.get_edges(strategy_id, 'in')
        assert len(incoming_edges) == 1
        assert incoming_edges[0]['source_id'] == ticker_id
        
        # Step 7: Update Ticker properties
        updated_ticker_id = pm.upsert_node('Ticker', 'TSLA', {'price': 178.25, 'sector': 'Auto'})
        assert updated_ticker_id == ticker_id  # Same ID
        
        ticker_node = pm.get_node('Ticker', 'TSLA')
        assert ticker_node['properties']['price'] == 178.25
        
        # Step 8: Update edge properties
        updated_edge_id = pm.upsert_edge(ticker_id, strategy_id, 'TRIGGERED_STRATEGY', {'confidence': 0.95, 'notes': 'Price surge'})
        assert updated_edge_id == edge_id  # Same ID


if __name__ == '__main__':
    pytest.main([__file__, '-v'])