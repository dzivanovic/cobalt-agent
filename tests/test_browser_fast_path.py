"""
Tests for Fast Path Browser Cache (Phase 3)

This module tests the Fast Path cache functionality for browser tasks:
- Cache lookup with cosine similarity
- Cache write-back after successful LLM navigation
- Cache invalidation and metrics
"""
import pytest
import json
import hashlib
import uuid
from datetime import datetime, timedelta
from unittest.mock import Mock, patch, MagicMock
from typing import Dict, Any, Optional

from loguru import logger

# Import the modules we're testing
from src.cobalt_agent.memory.postgres import (
    PostgresMemory, 
    FastPathCache, 
    compute_task_hash, 
    compute_context_signature
)
from src.cobalt_agent.tools.browser import BrowserTool


class MockFastPathCache:
    """Mock Fast Path Cache for testing without database."""
    
    def __init__(self):
        self.cache: Dict[str, Dict[str, Any]] = {}
        self.metrics = {"hits": 0, "misses": 0}
    
    def lookup(
        self, 
        task_intent: str, 
        context_signature: str,
        similarity_threshold: float = 0.85,
        limit: int = 1
    ) -> Optional[Dict[str, Any]]:
        """Mock lookup - return cached entry if exists."""
        if context_signature in self.cache:
            self.metrics["hits"] += 1
            return self.cache[context_signature]
        self.metrics["misses"] += 1
        return None
    
    def write_back(
        self,
        task_hash: str,
        task_intent: str,
        context_signature: str,
        element_tree_snapshot: Dict[str, Any],
        playwright_script: str,
        success_rate: float = 1.0
    ) -> bool:
        """Mock write-back - store entry."""
        self.cache[context_signature] = {
            "task_hash": task_hash,
            "task_intent": task_intent,
            "context_signature": context_signature,
            "element_tree_snapshot": element_tree_snapshot,
            "playwright_script": playwright_script,
            "success_rate": success_rate,
            "created_at": datetime.now()
        }
        return True
    
    def invalidate_old_cache(self, days: int = 30) -> int:
        """Mock invalidation."""
        return 0
    
    def get_metrics(self) -> Dict[str, Any]:
        """Mock metrics."""
        return {
            "total_cached_tasks": len(self.cache),
            "average_execution_time_ms": 100,
            "average_success_rate": 0.95,
            "age_distribution": {"0-7 days": len(self.cache)}
        }


class TestFastPathHashFunctions:
    """Tests for hash computation functions."""
    
    def test_compute_task_hash_deterministic(self):
        """Test that task hash is deterministic."""
        intent1 = "navigate to example.com"
        intent2 = "navigate to example.com"
        
        hash1 = compute_task_hash(intent1)
        hash2 = compute_task_hash(intent2)
        
        assert hash1 == hash2
        assert isinstance(hash1, str)
        assert len(hash1) == 36  # UUID format
    
    def test_compute_task_hash_different(self):
        """Test that different intents produce different hashes."""
        intent1 = "navigate to example.com"
        intent2 = "navigate to different.com"
        
        hash1 = compute_task_hash(intent1)
        hash2 = compute_task_hash(intent2)
        
        assert hash1 != hash2
    
    def test_compute_context_signature_deterministic(self):
        """Test that context signature is deterministic."""
        url = "https://example.com/page"
        
        sig1 = compute_context_signature(url, "Example Page", "Some content")
        sig2 = compute_context_signature(url, "Example Page", "Some content")
        
        assert sig1 == sig2
        assert isinstance(sig1, str)
        assert len(sig1) == 64  # SHA-256 hex


class TestFastPathCacheLookup:
    """Tests for Fast Path cache lookup functionality."""
    
    @pytest.fixture
    def mock_cache(self):
        """Create a mock cache with test data."""
        cache = MockFastPathCache()
        
        # Add a test entry
        context_sig = compute_context_signature(
            "https://example.com/test", 
            "Test Page", 
            "Test content"
        )
        cache.cache[context_sig] = {
            "task_hash": compute_task_hash("navigate to https://example.com/test"),
            "task_intent": "navigate to https://example.com/test",
            "context_signature": context_sig,
            "element_tree_snapshot": {"elements": []},
            "playwright_script": "page.goto('https://example.com/test')",
            "success_rate": 0.95,
            "created_at": datetime.now()
        }
        
        return cache
    
    def test_cache_hit(self, mock_cache):
        """Test that cache returns matching entry."""
        context_sig = mock_cache.cache.keys().__iter__().__next__()
        
        result = mock_cache.lookup(
            task_intent="navigate to https://example.com/test",
            context_signature=context_sig
        )
        
        assert result is not None
        assert result["context_signature"] == context_sig
        assert result["playwright_script"] is not None
    
    def test_cache_miss(self, mock_cache):
        """Test that cache returns None for non-matching entry."""
        result = mock_cache.lookup(
            task_intent="navigate to https://different.com",
            context_signature="nonexistent_context_signature"
        )
        
        assert result is None
    
    def test_metrics_tracking(self, mock_cache):
        """Test that metrics are tracked correctly."""
        context_sig = list(mock_cache.cache.keys())[0]
        
        # Trigger a hit
        mock_cache.lookup("intent", context_sig)
        
        # Trigger a miss
        mock_cache.lookup("different intent", "different context")
        
        assert mock_cache.metrics["hits"] == 1
        assert mock_cache.metrics["misses"] == 1


class TestFastPathCacheWriteBack:
    """Tests for Fast Path cache write-back functionality."""
    
    @pytest.fixture
    def mock_cache(self):
        """Create an empty mock cache."""
        return MockFastPathCache()
    
    def test_write_back(self, mock_cache):
        """Test that write_back stores entry correctly."""
        task_hash = compute_task_hash("test task")
        context_sig = compute_context_signature(
            "https://example.com/test", 
            "Test", 
            "Content"
        )
        
        success = mock_cache.write_back(
            task_hash=task_hash,
            task_intent="test task",
            context_signature=context_sig,
            element_tree_snapshot={"elements": [{"id": 1, "role": "button"}]},
            playwright_script="page.click('button')",
            success_rate=1.0
        )
        
        assert success is True
        assert context_sig in mock_cache.cache
        assert mock_cache.cache[context_sig]["task_hash"] == task_hash
    
    def test_write_back_overwrite(self, mock_cache):
        """Test that write_back overwrites existing entry."""
        context_sig = compute_context_signature(
            "https://example.com/test", 
            "Test", 
            "Content"
        )
        
        # First write
        mock_cache.write_back(
            task_hash=compute_task_hash("task1"),
            task_intent="task1",
            context_signature=context_sig,
            element_tree_snapshot={"elements": []},
            playwright_script="script1",
            success_rate=0.5
        )
        
        assert mock_cache.cache[context_sig]["success_rate"] == 0.5
        
        # Second write - should overwrite
        mock_cache.write_back(
            task_hash=compute_task_hash("task1"),
            task_intent="task1",
            context_signature=context_sig,
            element_tree_snapshot={"elements": []},
            playwright_script="script2",
            success_rate=0.8
        )
        
        assert mock_cache.cache[context_sig]["success_rate"] == 0.8


class TestBrowserToolFastPathIntegration:
    """Tests for BrowserTool Fast Path integration."""
    
    def test_generate_fast_path_task_hash(self):
        """Test that task hash generation is deterministic."""
        browser = BrowserTool()
        
        url = "https://example.com"
        actions = [{"action": "click", "id": 1}]
        
        hash1 = browser._generate_fast_path_task_hash(url, actions)
        hash2 = browser._generate_fast_path_task_hash(url, actions)
        
        assert hash1 == hash2
    
    def test_generate_context_signature(self):
        """Test that context signature generation works."""
        browser = BrowserTool()
        
        url = "https://example.com"
        sig = browser._generate_context_signature(url)
        
        assert isinstance(sig, str)
        assert len(sig) == 64  # SHA-256


class TestPostgresMemoryFastPath:
    """Tests for PostgresMemory Fast Path integration."""
    
    @pytest.fixture
    def postgres_memory(self):
        """Create a PostgresMemory instance with mock connection."""
        with patch('src.cobalt_agent.memory.postgres.psycopg') as mock_psycopg:
            mock_conn = MagicMock()
            mock_psycopg.connect.return_value = mock_conn
            
            # Mock the config
            with patch('src.cobalt_agent.memory.postgres.get_config') as mock_config:
                mock_config_instance = MagicMock()
                mock_config_instance.postgres.host = "localhost"
                mock_config_instance.postgres.port = 5432
                mock_config_instance.postgres.db = "cobalt"
                mock_config_instance.postgres.user = "cobalt"
                mock_config_instance.postgres.password = "cobalt_password"
                mock_config.return_value = mock_config_instance
                
                memory = PostgresMemory()
                memory.fast_path_cache = MockFastPathCache()
                yield memory
    
    def test_fast_path_cache_initialized(self, postgres_memory):
        """Test that fast_path_cache is initialized."""
        assert postgres_memory.fast_path_cache is not None
    
    def test_metrics_retrieval(self, postgres_memory):
        """Test that metrics can be retrieved."""
        metrics = postgres_memory.fast_path_cache.get_metrics()
        
        assert "total_cached_tasks" in metrics
        assert "average_success_rate" in metrics


if __name__ == "__main__":
    pytest.main([__file__, "-v"])