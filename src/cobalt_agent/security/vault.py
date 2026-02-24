"""
Local Vault Manager - Just-In-Time (JIT) Secrets Manager.
AES-256 encrypted local credential storage with in-memory operations.
"""
import os
import json
from pathlib import Path
from typing import Dict, Optional, List
from loguru import logger
from cryptography.fernet import Fernet


class VaultManager:
    """
    In-memory Just-In-Time (JIT) Secrets Manager.
    Reads from an AES-256 encrypted local file. Secrets only exist in RAM.
    """
    
    def __init__(self, vault_path: str = "data/.cobalt_vault"):
        self.vault_path = Path(vault_path)
        self._secrets: Dict[str, str] = {}
        self._is_unlocked: bool = False
        
    def generate_master_key(self) -> str:
        """Generates a new AES-256 Fernet key. RUN ONCE."""
        return Fernet.generate_key().decode()

    def unlock(self, master_key: str) -> bool:
        """Decrypts the vault directly into RAM."""
        if not self.vault_path.exists():
            logger.warning("Vault file does not exist. Creating a new empty vault.")
            self._secrets = {}
            self._is_unlocked = True
            return True

        try:
            f = Fernet(master_key.encode())
            with open(self.vault_path, "rb") as file:
                encrypted_data = file.read()
            
            decrypted_data = f.decrypt(encrypted_data)
            self._secrets = json.loads(decrypted_data.decode())
            self._is_unlocked = True
            logger.info("🔐 Vault successfully unlocked into memory.")
            return True
        except Exception as e:
            logger.error(f"Vault unlock failed (Invalid Key or Corrupt Data): {e}")
            self._is_unlocked = False
            return False

    def lock(self) -> None:
        """Wipes secrets from RAM."""
        self._secrets.clear()
        self._is_unlocked = False
        logger.info("🔒 Vault locked. Secrets wiped from RAM.")

    def get_secret(self, key_name: str) -> Optional[str]:
        """JIT Secret retrieval."""
        if not self._is_unlocked:
            logger.error(f"Attempted to access secret '{key_name}' while vault is locked!")
            return None
        return self._secrets.get(key_name)

    def set_secret(self, master_key: str, key_name: str, secret_value: str) -> bool:
        """Encrypts and saves a new secret to the physical vault file."""
        if not self._is_unlocked:
            logger.error("Cannot add secret: Vault is locked.")
            return False
            
        self._secrets[key_name] = secret_value
        return self._save_vault(master_key)

    def list_secrets(self) -> List[str]:
        """Returns a list of all secret keys currently in the vault (names only)."""
        if not self._is_unlocked:
            logger.error("Cannot list secrets: Vault is locked.")
            return []
        return list(self._secrets.keys())

    def delete_secret(self, master_key: str, key_name: str) -> bool:
        """Deletes a secret from the vault and saves the updated vault."""
        if not self._is_unlocked:
            logger.error("Cannot delete secret: Vault is locked.")
            return False
            
        if key_name in self._secrets:
            del self._secrets[key_name]
            logger.info(f"Secret '{key_name}' removed from memory.")
            return self._save_vault(master_key)
        return False

    def _save_vault(self, master_key: str) -> bool:
        """Internal helper to encrypt and save the current state of RAM to disk."""
        try:
            f = Fernet(master_key.encode())
            encrypted_data = f.encrypt(json.dumps(self._secrets).encode())
            
            self.vault_path.parent.mkdir(parents=True, exist_ok=True)
            with open(self.vault_path, "wb") as file:
                file.write(encrypted_data)
                
            logger.debug("Vault successfully saved to disk.")
            return True
        except Exception as e:
            logger.error(f"Failed to encrypt and save vault: {e}")
            return False