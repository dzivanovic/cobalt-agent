"""
Test suite for the Universal Extractor (Phase 2 - Watcher Daemon)

This module tests:
1. Pre-Flight Protocol with fast path fallback
2. LLM-powered extraction into Graph entities
3. Delta engine for computing new edges

All tests use proper mocking to avoid external dependencies.
"""
import pytest
import sys
import os
from unittest.mock import Mock, patch, MagicMock
from pydantic import ValidationError, BaseModel

# Add src to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

# Import all extractor classes at module level for delta tests
from cobalt_agent.tools.extractor import (
    GraphNode,
    GraphEdge,
    compute_delta
)


class TestPreFlightProtocol:
    """Tests for the Pre-Flight Protocol (Fast Path routing)"""
    
    def test_preflight_import_exists(self):
        """Test that Pre-Flight Protocol methods exist in browser tool"""
        with patch('cobalt_agent.config.Config.get_instance') as mock_get_instance:
            mock_instance = Mock()
            mock_instance.load.return_value = Mock()
            mock_get_instance.return_value = mock_instance
            
            from cobalt_agent.tools.browser import BrowserTool
            browser = BrowserTool()
            
            # Verify the preflight method exists
            assert hasattr(browser, '_execute_preflight_fast_path')
    
    def test_preflight_fast_path_returns_markdown(self):
        """Test that fast path returns Markdown content without Playwright"""
        with patch('cobalt_agent.config.Config.get_instance') as mock_get_instance:
            mock_instance = Mock()
            mock_instance.load.return_value = Mock()
            mock_get_instance.return_value = mock_instance
            
            with patch('cobalt_agent.tools.browser.requests.get') as mock_get:
                # Mock successful response with Markdown
                mock_response = Mock()
                mock_response.status_code = 200
                mock_response.headers = {'Content-Type': 'text/markdown'}
                mock_response.text = "# Test Content\n\nThis is **markdown**."
                mock_get.return_value = mock_response
                
                from cobalt_agent.tools.browser import BrowserTool
                browser = BrowserTool()
                
                # Simulate the fast path behavior
                result = browser._execute_preflight_fast_path("https://example.com")
                
                assert result is not None
                assert "# Test Content" in result


class TestLLMExtraction:
    """Tests for LLM-powered extraction into Graph entities"""

    def test_extract_nodes_from_markdown(self):
        """Test extracting nodes from Markdown text"""
        with patch('cobalt_agent.config.Config.get_instance') as mock_get_instance:
            mock_instance = Mock()
            mock_instance.load.return_value = Mock()
            mock_get_instance.return_value = mock_instance
            
            from cobalt_agent.tools.extractor import (
                UniversalExtractor,
                GraphNode,
                GraphEdge
            )
            
            markdown_text = """
# Company Analysis

## Overview
Acme Corp is a technology company founded in 2020.

## Products
- Widget Pro - Main product
- Widget Plus - Advanced version
"""
            
            extractor = UniversalExtractor()
            result = extractor.extract(markdown_text)
            
            # Should return a GraphExtractionOutput object
            assert hasattr(result, 'nodes')
            assert hasattr(result, 'edges')
            # At minimum, should have nodes and edges (even if empty due to mock LLM)
            assert isinstance(result.nodes, list)
            assert isinstance(result.edges, list)
            
    def test_extract_with_strategy_entity(self):
        """Test extracting strategy-related entities"""
        with patch('cobalt_agent.config.Config.get_instance') as mock_get_instance:
            mock_instance = Mock()
            mock_instance.load.return_value = Mock()
            mock_get_instance.return_value = mock_instance
            
            from cobalt_agent.tools.extractor import (
                UniversalExtractor,
                GraphNode,
                GraphEdge
            )
            
            markdown_text = """
# Trading Strategy: Morning Gapper

The Morning Gapper strategy triggers when TSLA gaps up by more than 3%.
Strategy parameters: score_threshold = 80, position_size = 100.
"""
            
            extractor = UniversalExtractor()
            result = extractor.extract(markdown_text)
            
            assert result is not None
            assert isinstance(result.nodes, list)
            assert isinstance(result.edges, list)


class TestDeltaEngine:
    """Tests for the Delta Engine (computing new edges)"""

    @patch('cobalt_agent.tools.extractor.PostgresMemory')
    def test_compute_delta_new_edges(self, mock_postgres):
        """Test delta computation with new edges"""
        # Create mock database instance with all required methods
        mock_db = Mock()
        # Use a side effect to return different IDs for different node names
        node_id_counter = {"count": 1}
        def upsert_node_side_effect(entity_type, name, properties=None):
            node_id = f"node-uuid-{node_id_counter['count']}"
            node_id_counter['count'] += 1
            return node_id
        mock_db.upsert_node.side_effect = upsert_node_side_effect
        mock_db.upsert_edge.return_value = "edge-uuid-456"
        # Return empty list for get_edges (no existing edges)
        mock_db.get_edges.return_value = []
        mock_postgres.return_value = mock_db
        
        # Create test nodes and edges
        nodes = [
            GraphNode(entity_type="company", name="Acme Corp", properties={}),
            GraphNode(entity_type="product", name="Widget", properties={})
        ]
        edges = [
            GraphEdge(
                source_name="Acme Corp",
                target_name="Widget",
                relationship="produces",
                properties={}
            )
        ]
        
        result = compute_delta(nodes, edges, mock_db)
        
        assert result is not None
        assert isinstance(result, dict)
        # All edges should be in new_edges since db is empty
        assert len(result.get("new_edges", [])) == 1
        assert result.get("existing_count", 0) == 0

    @patch('cobalt_agent.tools.extractor.PostgresMemory')
    def test_compute_delta_no_new_edges(self, mock_postgres):
        """Test delta computation when no new edges exist"""
        # Create mock database with all required methods
        mock_db = Mock()
        
        # Track node IDs by name using a dict
        node_ids = {"Acme Corp": "node-uuid-acme", "Widget": "node-uuid-widget"}
        node_id_counter = {"count": 1}
        def upsert_node_side_effect(entity_type, name, properties=None):
            # Return existing ID if already seen, otherwise generate new one
            if name not in node_ids:
                node_ids[name] = f"node-uuid-{node_id_counter['count']}"
                node_id_counter['count'] += 1
            return node_ids[name]
        
        mock_db.upsert_node.side_effect = upsert_node_side_effect
        mock_db.upsert_edge.return_value = "edge-uuid-456"
        
        # Mock get_edges to return existing edge when source_id is node-uuid-acme
        def get_edges_side_effect(source_id, direction='both'):
            if source_id == "node-uuid-acme":
                return [{
                    "source_id": "node-uuid-acme",
                    "target_id": "node-uuid-widget",
                    "relationship": "produces"
                }]
            return []
        mock_db.get_edges.side_effect = get_edges_side_effect
        
        mock_postgres.return_value = mock_db

        nodes = [
            GraphNode(entity_type="company", name="Acme Corp", properties={}),
            GraphNode(entity_type="product", name="Widget", properties={})
        ]
        edges = [
            GraphEdge(
                source_name="Acme Corp",
                target_name="Widget",
                relationship="produces",
                properties={}
            )
        ]

        result = compute_delta(nodes, edges, mock_db)

        assert result is not None
        assert isinstance(result, dict)
        assert len(result.get("new_edges", [])) == 0
        assert result.get("existing_count", 0) == 1

    @patch('cobalt_agent.tools.extractor.PostgresMemory')
    def test_compute_delta_partial_new_edges(self, mock_postgres):
        """Test delta computation with mix of new and existing edges"""
        # Create mock database with all required methods
        mock_db = Mock()
        
        # Track node IDs by name using a dict
        node_ids = {"Acme Corp": "node-uuid-acme", "Widget": "node-uuid-widget", "Tech": "node-uuid-tech"}
        node_id_counter = {"count": 1}
        def upsert_node_side_effect(entity_type, name, properties=None):
            # Return existing ID if already seen, otherwise generate new one
            if name not in node_ids:
                node_ids[name] = f"node-uuid-{node_id_counter['count']}"
                node_id_counter['count'] += 1
            return node_ids[name]
        
        mock_db.upsert_node.side_effect = upsert_node_side_effect
        mock_db.upsert_edge.return_value = "edge-uuid-456"
        
        # Mock get_edges to return existing edge when source_id is node-uuid-acme
        def get_edges_side_effect(source_id, direction='both'):
            if source_id == "node-uuid-acme":
                return [{
                    "source_id": "node-uuid-acme",
                    "target_id": "node-uuid-widget",
                    "relationship": "produces"
                }]
            return []
        mock_db.get_edges.side_effect = get_edges_side_effect
        
        mock_postgres.return_value = mock_db
        
        nodes = [
            GraphNode(entity_type="company", name="Acme Corp", properties={}),
            GraphNode(entity_type="product", name="Widget", properties={}),
            GraphNode(entity_type="industry", name="Tech", properties={})
        ]
        edges = [
            # Existing edge
            GraphEdge(
                source_name="Acme Corp",
                target_name="Widget",
                relationship="produces",
                properties={}
            ),
            # New edge
            GraphEdge(
                source_name="Acme Corp",
                target_name="Tech",
                relationship="operates_in",
                properties={}
            )
        ]
        
        result = compute_delta(nodes, edges, mock_db)
        
        assert result is not None
        assert isinstance(result, dict)
        assert len(result.get("new_edges", [])) == 1  # Only the "operates_in" edge is new
        assert result.get("existing_count", 0) == 1  # The "produces" edge already exists


if __name__ == "__main__":
    pytest.main([__file__, "-v"])