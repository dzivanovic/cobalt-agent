"""
Tests for the PostgreSQL Memory module.
Verifies secret scrubbing functionality.
"""
import pytest
import os
from pathlib import Path


class TestSecretScrubber:
    """Test the _scrub_secrets method in PostgresMemory."""
    
    def test_scrub_secrets_basic_redaction(self):
        """Test basic secret redaction functionality."""
        from cobalt_agent.memory.postgres import PostgresMemory
        
        # Create instance
        memory = object.__new__(PostgresMemory)
        
        # Mock secrets to scrub - the config.keys should contain actual values to scrub
        test_secret = "my_test_secret_value_12345"
        memory.config = type('MockConfig', (), {
            'keys': {'TEST_KEY': test_secret},
            'postgres': type('MockPostgres', (), {'host': 'localhost', 'port': 5432, 'db': 'test', 'user': 'test'})()
        })()
        
        # Temporarily patch get_config to return our mock
        import cobalt_agent.memory.postgres as postgres_module
        original_get_config = postgres_module.get_config
        postgres_module.get_config = lambda: memory.config
        
        try:
            # Test the scrubbing
            test_text = f"Message contains {test_secret} here."
            result = memory._scrub_secrets(test_text)
            
            assert "[REDACTED_SECRET]" in result, f"Expected redaction, got: {result}"
            assert test_secret not in result, f"Secret should be removed: {result}"
        finally:
            # Restore original function
            postgres_module.get_config = original_get_config
    
    def test_scrub_secrets_no_secrets(self):
        """Test that text without secrets remains unchanged."""
        from cobalt_agent.memory.postgres import PostgresMemory
        
        memory = object.__new__(PostgresMemory)
        memory.config = type('MockConfig', (), {
            'keys': {},
            'postgres': type('MockPostgres', (), {'host': 'localhost', 'port': 5432, 'db': 'test', 'user': 'test'})()
        })()
        
        import cobalt_agent.memory.postgres as postgres_module
        original_get_config = postgres_module.get_config
        postgres_module.get_config = lambda: memory.config
        
        try:
            test_text = "This is a normal message with no secrets."
            result = memory._scrub_secrets(test_text)
            
            # Without any secrets, text should remain unchanged
            assert result == test_text, f"Expected no change, got: {result}"
        finally:
            postgres_module.get_config = original_get_config
    
    def test_scrub_secrets_multiple_secrets(self):
        """Test that multiple secrets are all redacted."""
        from cobalt_agent.memory.postgres import PostgresMemory
        
        memory = object.__new__(PostgresMemory)
        memory.config = type('MockConfig', (), {
            'keys': {
                'KEY1': 'secret_one',
                'KEY2': 'secret_two',
            },
            'postgres': type('MockPostgres', (), {'host': 'localhost', 'port': 5432, 'db': 'test', 'user': 'test'})()
        })()
        
        import cobalt_agent.memory.postgres as postgres_module
        original_get_config = postgres_module.get_config
        postgres_module.get_config = lambda: memory.config
        
        try:
            test_text = "Contains secret_one and secret_two here."
            result = memory._scrub_secrets(test_text)
            
            assert "[REDACTED_SECRET]" in result, f"Expected redaction, got: {result}"
            assert "secret_one" not in result, f"secret_one should be removed: {result}"
            assert "secret_two" not in result, f"secret_two should be removed: {result}"
        finally:
            postgres_module.get_config = original_get_config
    
    def test_scrub_secrets_case_sensitive(self):
        """Test that matching is case-sensitive."""
        from cobalt_agent.memory.postgres import PostgresMemory
        
        memory = object.__new__(PostgresMemory)
        memory.config = type('MockConfig', (), {
            'keys': {'KEY': 'secretValue'},
            'postgres': type('MockPostgres', (), {'host': 'localhost', 'port': 5432, 'db': 'test', 'user': 'test'})()
        })()
        
        import cobalt_agent.memory.postgres as postgres_module
        original_get_config = postgres_module.get_config
        postgres_module.get_config = lambda: memory.config
        
        try:
            # Uppercase version should not be redacted
            test_text = "Contains SECRETVALUE here."
            result = memory._scrub_secrets(test_text)
            
            # Should remain unchanged (case sensitive)
            assert result == test_text, f"Expected no change for case mismatch, got: {result}"
        finally:
            postgres_module.get_config = original_get_config
    
    def test_scrub_secrets_partial_match_is_redacted(self):
        """Test that partial substring matches are also redacted (substring replacement)."""
        from cobalt_agent.memory.postgres import PostgresMemory
        
        memory = object.__new__(PostgresMemory)
        memory.config = type('MockConfig', (), {
            'keys': {'KEY': 'secret123'},
            'postgres': type('MockPostgres', (), {'host': 'localhost', 'port': 5432, 'db': 'test', 'user': 'test'})()
        })()
        
        import cobalt_agent.memory.postgres as postgres_module
        original_get_config = postgres_module.get_config
        postgres_module.get_config = lambda: memory.config
        
        try:
            # Partial substring match should be redacted
            test_text = "Contains secret1234 (extra digit)."
            result = memory._scrub_secrets(test_text)
            
            # The substring 'secret123' should be replaced, leaving '4' behind
            assert "[REDACTED_SECRET]" in result, f"Expected redaction of substring: {result}"
            assert "secret123" not in result, f"secret123 should be removed: {result}"
            assert "4" in result, f"Trailing character should remain: {result}"
        finally:
            postgres_module.get_config = original_get_config
    
    def test_scrub_secrets_with_vault_manager(self):
        """Test secret redaction using VaultManager when vault is unlocked."""
        from cobalt_agent.memory.postgres import PostgresMemory
        from cobalt_agent.security.vault import VaultManager
        
        # Create a mock vault manager that is unlocked with secrets
        vault = VaultManager()
        vault._is_unlocked = True  # Manually unlock for testing
        vault._secrets = {"API_KEY": "vault_secret_value_123"}
        
        memory = object.__new__(PostgresMemory)
        memory.config = type('MockConfig', (), {
            'keys': {},
            'postgres': type('MockPostgres', (), {'host': 'localhost', 'port': 5432, 'db': 'test', 'user': 'test'})()
        })()
        
        import cobalt_agent.memory.postgres as postgres_module
        original_get_config = postgres_module.get_config
        original_vault_manager = postgres_module.VaultManager
        
        # Mock VaultManager to return our test vault
        postgres_module.VaultManager = lambda: vault
        
        try:
            test_text = "Contains vault_secret_value_123 here."
            result = memory._scrub_secrets(test_text)
            
            assert "[REDACTED_SECRET]" in result, f"Expected redaction from vault, got: {result}"
            assert "vault_secret_value_123" not in result, f"Secret from vault should be removed: {result}"
        finally:
            postgres_module.get_config = original_get_config
            postgres_module.VaultManager = original_vault_manager


if __name__ == "__main__":
    pytest.main([__file__, "-v"])