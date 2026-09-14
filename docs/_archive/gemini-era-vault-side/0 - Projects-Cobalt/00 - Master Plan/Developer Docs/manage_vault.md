# manage_vault.py

## Overview

The `manage_vault.py` script is an interactive CLI utility for managing Cobalt's local encrypted secret vault. It provides a user-friendly interface for generating master keys, storing secrets, retrieving credentials, and managing sensitive configuration data.

## Purpose

This script serves the following functions:
- Generates and manages the master encryption key for the vault
- Provides interactive CLI for CRUD operations on secrets
- Enables secure storage of API keys, passwords, and configuration credentials
- Supports both string and JSON-formatted secrets

## Location

```
dev_utils/manage_vault.py
```

## Dependencies

- `src/cobalt_agent/security/vault.py` - Core vault encryption/decryption logic
- `rich` library for terminal UI styling

## How It Works

The vault management process follows these steps:

1. **Master Key Check**: Verifies if `COBALT_MASTER_KEY` environment variable is set
2. **Key Generation**: If no master key exists, generates a new cryptographically secure key
3. **Vault Unlock**: Uses the master key to decrypt and unlock the vault
4. **Interactive Menu**: Provides CLI menu for secret management operations

### Interactive Menu Options

| Option | Action | Description |
|--------|--------|-------------|
| 1 | List All Secret Names | Displays all stored secret keys |
| 2 | Retrieve a Secret | Fetches and displays a secret by name |
| 3 | Add/Update Secret | Creates or updates a secret (string or JSON) |
| 4 | Delete a Secret | Removes a secret with confirmation |
| 5 | Exit and Lock Vault | Closes session and locks the vault |

## Usage

### Prerequisites

1. Ensure `src/cobalt_agent/security/vault.py` is properly configured
2. Have a secure password manager ready to store the master key

### Running the Script

From the project root:

```bash
uv run dev_utils/manage_vault.py
```

### First-Time Setup

On first run, the script will:
1. Detect no master key in environment
2. Generate a new cryptographically secure master key
3. Display the key with instructions to save it

**CRITICAL**: Save the generated master key in your password manager. Run:
```bash
export COBALT_MASTER_KEY='your_generated_key'
```

Then re-run the script to unlock the vault.

### Interactive Operations

#### Listing Secrets
```
Choice: 1
Displays all stored secret names
```

#### Retrieving a Secret
```
Choice: 2
Enter Secret Name to retrieve: BROKER_CREDS
Displays the decrypted secret value
```

#### Adding/Updating a Secret
```
Choice: 3
Enter Secret Name (e.g., BROKER_CREDS): MY_API_KEY
Enter Secret Value: [password-protected input]
```

Supports both flat strings and JSON objects:
```json
{"url": "https://api.example.com", "user": "admin", "pass": "secret"}
```

#### Deleting a Secret
```
Choice: 4
Enter Secret Name to delete: OLD_CREDENTIALS
Confirm: y
```

## Expected Output

On successful execution, the script will display:
- Master key generation with export instructions (first run)
- Menu-driven interface for vault operations
- Confirmation messages for each operation

On failure, it will provide:
- "Failed to unlock vault" if master key is incorrect
- "Secret not found" for missing keys during retrieval/deletion

## Troubleshooting

| Issue | Possible Cause | Solution |
|-------|---------------|----------|
| No COBALT_MASTER_KEY found | Environment variable not set | Generate new key or export existing one |
| Failed to unlock vault | Incorrect master key | Verify the key matches what was used to encrypt |
| Vault is empty | No secrets stored yet | Use option 3 to add secrets |

## Security Considerations

- Master key must be stored securely (password manager recommended)
- Secrets are encrypted at rest using the master key
- Vault automatically locks when session ends (option 5)
- Deletion requires explicit confirmation to prevent accidents

## Related Documentation

- [Vault](vault.md) - Core vault security implementation
- [Zero Trust Security](../../../90 - Project Management/Requirements/PRD-011 Zero Trust Security.md) - Security requirements

## Maintenance Notes

This script should be used:
- During initial Cobalt setup to establish secure credential storage
- When adding new API keys or service credentials
- For auditing stored secrets and cleaning up obsolete credentials
- When onboarding team members to secure credential management