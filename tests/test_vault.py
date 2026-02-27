"""
Vault Manager Tests
Tests AES-256 encryption, decryption, and locking functionality.
"""
import os
import json
import tempfile
import pytest
from pathlib import Path

from cobalt_agent.security.vault import VaultManager


@pytest.fixture
def temp_vault_path():
    """Create a temporary vault file path for testing (file doesn't exist initially)."""
    with tempfile.NamedTemporaryFile(suffix='.vault', delete=False) as f:
        path = f.name
    
    # Delete the file so it doesn't exist when tests run
    Path(path).unlink(missing_ok=True)
    
    yield path
    
    # Cleanup after test
    Path(path).unlink(missing_ok=True)


@pytest.fixture
def vault_manager(temp_vault_path):
    """Create a VaultManager instance."""
    return VaultManager(temp_vault_path)


@pytest.fixture
def master_key():
    """Generate a valid Fernet key for testing."""
    from cryptography.fernet import Fernet
    return Fernet.generate_key().decode()


class TestVaultManager:
    """Test suite for VaultManager."""
    
    def test_generate_master_key(self, vault_manager):
        """Test that generate_master_key produces a valid Fernet key."""
        key = vault_manager.generate_master_key()
        # Verify it's a valid Fernet key format (base64 encoded)
        assert isinstance(key, str)
        assert len(key) == 44  # Base64 encoded 32-byte key
    
    def test_unlock_empty_vault(self, vault_manager, master_key):
        """Test unlocking a non-existent vault creates an empty vault."""
        result = vault_manager.unlock(master_key)
        assert result is True
        assert vault_manager._is_unlocked is True
        assert vault_manager._secrets == {}
    
    def test_unlock_existing_vault(self, vault_manager, master_key, temp_vault_path):
        """Test unlocking an existing encrypted vault."""
        # First unlock to create the vault
        vault_manager.unlock(master_key)
        
        # Add a secret
        vault_manager.set_secret(master_key, "test_key", "test_value")
        
        # Lock the vault
        vault_manager.lock()
        assert vault_manager._is_unlocked is False
        
        # Create new vault manager instance
        new_vault = VaultManager(temp_vault_path)
        
        # Unlock with same key
        result = new_vault.unlock(master_key)
        assert result is True
        assert new_vault._is_unlocked is True
        assert new_vault.get_secret("test_key") == "test_value"
    
    def test_unlock_with_invalid_key(self, vault_manager, temp_vault_path, master_key):
        """Test that unlocking with an invalid key fails."""
        # Create vault with valid key
        vault_manager.unlock(master_key)
        vault_manager.set_secret(master_key, "test_key", "test_value")
        vault_manager.lock()
        
        # Try to unlock with invalid key
        invalid_key = "invalid_key_that_will_not_work"
        result = vault_manager.unlock(invalid_key)
        assert result is False
        assert vault_manager._is_unlocked is False
    
    def test_set_and_get_secret(self, vault_manager, master_key):
        """Test setting and retrieving a secret."""
        vault_manager.unlock(master_key)
        
        result = vault_manager.set_secret(master_key, "api_key", "secret123")
        assert result is True
        
        secret = vault_manager.get_secret("api_key")
        assert secret == "secret123"
    
    def test_get_secret_from_locked_vault(self, vault_manager, master_key):
        """Test that getting a secret from locked vault returns None."""
        vault_manager.unlock(master_key)
        vault_manager.set_secret(master_key, "api_key", "secret123")
        vault_manager.lock()
        
        secret = vault_manager.get_secret("api_key")
        assert secret is None
    
    def test_list_secrets(self, vault_manager, master_key):
        """Test listing all secret keys."""
        vault_manager.unlock(master_key)
        
        vault_manager.set_secret(master_key, "key1", "value1")
        vault_manager.set_secret(master_key, "key2", "value2")
        vault_manager.set_secret(master_key, "key3", "value3")
        
        secrets = vault_manager.list_secrets()
        assert "key1" in secrets
        assert "key2" in secrets
        assert "key3" in secrets
        assert len(secrets) == 3
    
    def test_list_secrets_from_locked_vault(self, vault_manager, master_key):
        """Test that listing secrets from locked vault returns empty list."""
        vault_manager.unlock(master_key)
        vault_manager.set_secret(master_key, "key1", "value1")
        vault_manager.lock()
        
        secrets = vault_manager.list_secrets()
        assert secrets == []
    
    def test_delete_secret(self, vault_manager, master_key):
        """Test deleting a secret."""
        vault_manager.unlock(master_key)
        
        vault_manager.set_secret(master_key, "key_to_delete", "value123")
        assert vault_manager.get_secret("key_to_delete") == "value123"
        
        result = vault_manager.delete_secret(master_key, "key_to_delete")
        assert result is True
        assert vault_manager.get_secret("key_to_delete") is None
    
    def test_delete_secret_from_locked_vault(self, vault_manager, master_key):
        """Test that deleting from locked vault fails."""
        vault_manager.unlock(master_key)
        vault_manager.set_secret(master_key, "key1", "value1")
        vault_manager.lock()
        
        result = vault_manager.delete_secret(master_key, "key1")
        assert result is False
    
    def test_lock_wipes_secrets(self, vault_manager, master_key):
        """Test that lock() properly wipes secrets from memory."""
        vault_manager.unlock(master_key)
        vault_manager.set_secret(master_key, "key1", "value1")
        vault_manager.set_secret(master_key, "key2", "value2")
        
        # Verify secrets are in memory
        assert vault_manager.get_secret("key1") == "value1"
        assert vault_manager.get_secret("key2") == "value2"
        
        # Lock the vault
        vault_manager.lock()
        
        # Verify secrets are cleared
        assert vault_manager.get_secret("key1") is None
        assert vault_manager.get_secret("key2") is None
        assert vault_manager._is_unlocked is False
    
    def test_persistence_across_instances(self, vault_manager, master_key, temp_vault_path):
        """Test that secrets persist to disk and can be loaded by new instance."""
        vault_manager.unlock(master_key)
        vault_manager.set_secret(master_key, "persist_key", "persist_value")
        vault_manager.lock()
        
        # Create new instance pointing to same vault
        new_vault = VaultManager(temp_vault_path)
        new_vault.unlock(master_key)
        
        assert new_vault.get_secret("persist_key") == "persist_value"
    
    def test_set_secret_while_locked(self, vault_manager, master_key):
        """Test that setting a secret while locked fails."""
        vault_manager.unlock(master_key)
        vault_manager.lock()
        
        result = vault_manager.set_secret(master_key, "new_key", "new_value")
        assert result is False
        assert vault_manager.get_secret("new_key") is None