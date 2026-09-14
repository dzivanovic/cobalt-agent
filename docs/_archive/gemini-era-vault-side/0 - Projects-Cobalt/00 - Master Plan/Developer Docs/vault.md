---
title: "Vault Manager Documentation"
status: Active
module: Security
type: Class
dependencies:
  - "[[config]]"
  - "[[mattermost]]"
location: "src/cobalt_agent/security/vault.py"
tags: [cobalt, dev_docs, security]
created: 2026-02-24
---

# Vault Manager (Zero Trust Secrets Manager)

## Overview
The Vault Manager is a Just-In-Time (JIT) secrets manager that provides secure storage and retrieval of API keys, tokens, and credentials. It uses AES-256 encryption with **RAM-only decryption** - secrets exist only in memory during active use and are never exposed in plaintext on disk.

### Core Features
- **AES-256 Fernet encryption** for secure at-rest storage
- **RAM-only decryption** - secrets exist only in memory when vault is unlocked
- **Automatic injection** - secrets are injected into `os.environ` and config schema at runtime
- **Flat strings and JSON support** - handles both simple keys and grouped credentials
- **Manual key rotation** via `COBALT_MASTER_KEY` environment variable

---

## Class: `VaultManager`

### Constructor
```python
def __init__(self, vault_path: str = "data/.cobalt_vault")
```
Initializes the vault manager with the specified vault file path.

**Parameters:**
- `vault_path`: Path to the encrypted vault file (default: `"data/.cobalt_vault"`)

### Key Attributes
- `vault_path`: Path to the encrypted vault file on disk
- `_secrets`: Dictionary storing decrypted secrets in RAM (only populated when unlocked)
- `_is_unlocked`: Boolean indicating whether the vault is currently decrypted

### Main Methods

#### `generate_master_key() -> str`
Generates a new AES-256 Fernet key. Run this once to create your master key.

**Returns:**
- `str`: A new Fernet key for encrypting/decrypting the vault

**Usage:**
```bash
export COBALT_MASTER_KEY="your-generated-key-here"
```

#### `unlock(master_key: str) -> bool`
Decrypts the vault file into RAM. This is the only way to access secrets.

**Parameters:**
- `master_key`: The AES-256 Fernet key to decrypt the vault

**Returns:**
- `True` if decryption succeeded
- `False` if the key was invalid or data was corrupt

**Behavior:**
- Loads the encrypted vault file from disk
- Decrypts the contents using Fernet
- Stores decrypted JSON in `_secrets` dictionary
- Sets `_is_unlocked = True`
- Logs success or failure

#### `lock() -> None`
Wipes secrets from RAM and locks the vault.

**Behavior:**
- Clears the `_secrets` dictionary
- Sets `_is_unlocked = False`
- Logs the lock event

#### `get_secret(key_name: str) -> Optional[str]`
Retrieves a secret from the unlocked vault.

**Parameters:**
- `key_name`: The name of the secret to retrieve

**Returns:**
- The secret value if found and vault is unlocked
- `None` if vault is locked or key not found

#### `set_secret(master_key: str, key_name: str, secret_value: str) -> bool`
Adds or updates a secret in the vault.

**Parameters:**
- `master_key`: The encryption key (must have vault unlocked first)
- `key_name`: The name of the secret (e.g., `OPENAI_API_KEY`)
- `secret_value`: The secret value to store

**Returns:**
- `True` if the secret was saved successfully
- `False` if vault is locked or save failed

**Behavior:**
- Stores the secret in RAM
- Encrypts and saves the entire vault to disk

#### `list_secrets() -> List[str]`
Lists all secret keys currently in the vault.

**Returns:**
- List of secret names if vault is unlocked
- Empty list if vault is locked

#### `delete_secret(master_key: str, key_name: str) -> bool`
Removes a secret from the vault and updates the vault file.

**Parameters:**
- `master_key`: The encryption key
- `key_name`: The name of the secret to delete

**Returns:**
- `True` if the secret was deleted
- `False` if vault is locked or key not found

---

## CLI Utility: `manage_vault.py`

### Overview
The `manage_vault.py` script provides an interactive command-line interface for managing the vault. It requires the `COBALT_MASTER_KEY` environment variable to be set.

### Location
```
dev_utils/manage_vault.py
```

### Requirements
- **Mandatory**: `COBALT_MASTER_KEY` environment variable must be set
- **Optional**: If not set, the script will offer to generate a new key

### Usage
```bash
# Set the master key first (REQUIRED)
export COBALT_MASTER_KEY="your-fernet-key-here"

# Run the management script
python dev_utils/manage_vault.py
```

### Interactive Menu
When run, the script presents the following options:

1. **List All Secret Names** - Shows all keys currently stored in the vault
2. **Retrieve a Secret** - Displays the value of a specified secret
3. **Add/Update a Secret** - Store a new secret (supports flat strings or JSON)
4. **Delete a Secret** - Remove a secret from the vault
5. **Exit and Lock Vault** - Save changes and lock the vault

### Secret Value Formats

The CLI supports both flat strings and JSON strings for different use cases:

| Format | Example | Use Case |
|--------|---------|----------|
| Flat String | `sk-proj-abc123...` | Simple API keys (OPENAI_API_KEY, GEMINI_API_KEY) |
| JSON String | `{"url":"...", "user":"...", "pass":"..."}` | Grouped credentials (MATTERMOST_CREDS) |

### Error Handling
- **No Master Key**: Script generates a new key and prompts user to save it
- **Invalid Key**: Error message displayed, script exits
- **Corrupt Vault**: Warning logged, empty vault created

---

## Configuration Integration

### Loading Priority (Highest to Lowest)
1. **Environment Variables** - Strictly for node/Docker specific data (POSTGRES_HOST, etc.)
2. **Secure Vault** - API keys and tokens injected dynamically at runtime
3. **YAML Configuration Files** - Static configuration (trading_rules, persona, etc.)

### How Secrets Are Injected

When `COBALT_MASTER_KEY` is present, the configuration loader:

1. **Unlocks the vault** using the provided key
2. **Lists all secrets** in the vault
3. **Attempts JSON parsing** for each secret value
4. **Routes secrets based on name**:
   - `MATTERMOST_CREDS` → Parsed as JSON, injected into `mattermost` config
   - Other secrets → Injected into `keys` section and `os.environ`

### Example Runtime Injection

```python
# When vault is unlocked:
vault.list_secrets()  # ['OPENAI_API_KEY', 'MATTERMOST_CREDS']

# Flat string injection:
os.environ['OPENAI_API_KEY'] = 'sk-proj-abc123'  # Also in config.keys

# JSON injection:
os.environ['MATTERMOST_URL'] = 'https://mattermost.example.com'
os.environ['MATTERMOST_TOKEN'] = 'xyz789token'
# Also in config.mattermost: {'url': '...', 'token': '...'}
```

### Security Guarantees
- **Zero disk persistence** of decrypted secrets
- **Automatic lock** after configuration load completes
- **Environment variable isolation** - secrets only in `os.environ` during active use
- **Type-safe schema** - secrets mapped to specific config fields

---

## Security Best Practices

1. **Never commit the master key** - Use `.env.example` to document required variables
2. **Rotate keys regularly** - Generate new `COBALT_MASTER_KEY` periodically
3. **Lock vault when idle** - Secrets are automatically locked after config loading
4. **Use environment-specific vaults** - Separate vaults for dev/staging/production
5. **Audit secret access** - Log all vault unlock/access events

---

## File Structure

```
data/
└── .cobalt_vault          # Encrypted vault file (AES-256)
    └── plaintext in RAM   # Decrypted secrets (JSON) - RAM-only
```

### Vault File Format (Encrypted)
```json
{
  "OPENAI_API_KEY": "sk-proj-abc123...",
  "MATTERMOST_CREDS": "{\"url\":\"https://mattermost.example.com\",\"token\":\"xyz789\"}"
}
```

### Environment Variable Mapping

| Vault Key | Environment Variable | Config Field |
|-----------|---------------------|--------------|
| `OPENAI_API_KEY` | `OPENAI_API_KEY` | `llm.api_key` |
| `ANTHROPIC_API_KEY` | `ANTHROPIC_API_KEY` | `llm.api_key` |
| `MATTERMOST_CREDS` | `MATTERMOST_URL`, `MATTERMOST_TOKEN` | `mattermost.url`, `mattermost.token` |

---

## Example Usage

### Initialize Vault (One-Time Setup)
```bash
python dev_utils/manage_vault.py
# Follow prompts to generate a new master key
# Save the key: export COBALT_MASTER_KEY="..."
```

### Add a Secret
```bash
export COBALT_MASTER_KEY="your-fernet-key"
python dev_utils/manage_vault.py
# Select option 3, enter secret name and value
```

### Use in Application Code
```python
from cobalt_agent.config import load_config

# Configuration automatically unlocks vault if COBALT_MASTER_KEY is set
config = load_config()

# Secrets are injected into config and os.environ
# config.llm.api_key contains the vault value
# os.environ['OPENAI_API_KEY'] contains the vault value
```

### Lock Vault Manually
```python
from cobalt_agent.config import Config

config = Config.get_instance()
config.lock_vault()  # Wipes secrets from RAM