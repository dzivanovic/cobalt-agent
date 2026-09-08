---
title: "ADR-004 Zero Trust Security"
status: Active 
priority: P0
module: [Security]
phase: 1
complexity: M
tags: [cobalt, security, architecture, documentation, adr]
created: 2026-02-23
---

# ADR-004: Zero Trust Security

## Status: ACCEPTED

## Decision

We implement a **Zero Trust Security Model** with three layers:

```
                    ┌───────────────────┐
                    │  Human-In-The-Loop │
                    │  Proposal Engine   │
                    └────────────┬──────┘
                                │
                    ┌───────────▼───────────┐
                    │  Docker Seccomp       │
                    │  Sandbox              │
                    └───────────┬───────────┘
                                │
                    ┌───────────▼───────────┐
                    │  VaultManager         │
                    │  AES-256 Secret Store │
                    └───────────────────────┘
```

## Layer 1: Human-In-The-Loop (HITL) Proposal Engine

### Overview
All high-risk operations require human approval before execution.

### Approval Flow
```
1. Agent proposes action
   ├─ Trade execution
   ├─ Code execution
   └─ Credential access

2. Generate approval request (Pydantic model)
   ├─ Action type
   ├─ Parameters
   ├─ Risk assessment
   └─ Justification

3. Wait for human approval (via Mattermost/CLI)
   ├─ Timeout: 5 minutes
   └─ Auto-reject if no response

4. Execute only if approved
```

### Pydantic Models
```python
class ApprovalRequest(BaseModel):
    request_id: str
    action_type: str  # "TRADE", "CODE_EXEC", "CREDENTIAL_ACCESS"
    parameters: Dict[str, Any]
    risk_level: str   # "LOW", "MEDIUM", "HIGH"
    justification: str
    timestamp: datetime

class ApprovalResponse(BaseModel):
    approved: bool
    approver: str
    timestamp: datetime
    comments: Optional[str]
```

## Layer 2: Docker Seccomp Sandboxes

### Overview
All code execution runs in isolated Docker containers with strict seccomp profiles.

### Container Configuration
```yaml
security_opt:
  - seccomp:./seccomp/profile.json
  - no-new-privileges:true

read_only: true

network_mode: none

privileged: false

user: "1000:1000"
```

### Seccomp Profile
- Only allows: `read`, `write`, `open`, `close`, `stat`, `fstat`
- Blocks: `socket`, `connect`, `execve`, `ptrace`
- Allows network only for specific tools (browser, search)

## Layer 3: VaultManager AES-256 Secret Store

### Overview
Credentials are managed via our custom **VaultManager** implementation using AES-256 encryption. Secrets are never stored in plaintext and are retrieved just-in-time with full audit logging.

### VaultManager Architecture
```
┌─────────────────────────────────────────────────────┐
│                  VaultManager                       │
├─────────────────────────────────────────────────────┤
│  • AES-256-GCM encryption (cryptography library)   │
│  • Local encrypted vault (SQLite-backed)            │
│  • Master key derived from OS X Keychain            │
│  • Just-in-time decryption with automatic expiry    │
│  • Full audit trail (who, when, why)                │
└─────────────────────────────────────────────────────┘
```

### VaultManager Flow
```
1. Agent requests credential access
2. VaultManager decrypts using master key:
   ├─ Master key retrieved from OS X Keychain
   ├─ Vault encrypted with AES-256-GCM
   └─ Decryption performed in memory only

3. VaultManager returns credential (TTL enforced):
   ├─ Valid for configured TTL (default: 5 minutes)
   ├─ Single-use or limited uses configurable
   └─ Audit log entry created

4. Credential used and discarded:
   ├─ Credential zeroed from memory after use
   └─ Audit log updated with usage timestamp
```

### VaultManager Implementation
```python
from cryptography.hazmat.primitives.ciphers.aead import AESGCM
import os

class VaultManager:
    def __init__(self, vault_path: str):
        self.vault_path = vault_path
        self.master_key = self._get_master_key()  # From OS X Keychain
        
    def _get_master_key(self) -> bytes:
        """Retrieve master key from OS X Keychain."""
        # Uses security find-generic-password to retrieve encrypted key
        pass
    
    def encrypt(self, plaintext: str, metadata: dict) -> bytes:
        """Encrypt secret with AES-256-GCM."""
        nonce = os.urandom(12)
        aesgcm = AESGCM(self.master_key)
        ciphertext = aesgcm.encrypt(nonce, plaintext.encode(), metadata)
        return nonce + ciphertext
    
    def decrypt(self, encrypted_data: bytes, metadata: dict) -> str:
        """Decrypt secret with AES-256-GCM."""
        nonce = encrypted_data[:12]
        ciphertext = encrypted_data[12:]
        aesgcm = AESGCM(self.master_key)
        plaintext = aesgcm.decrypt(nonce, ciphertext, metadata)
        return plaintext.decode()
    
    def get_credential(self, vault_id: str, justification: str) -> Credential:
        """Retrieve credential with audit logging."""
        # 1. Look up encrypted credential from vault
        encrypted = self._lookup_vault_id(vault_id)
        
        # 2. Log audit entry before decryption
        self._audit_log(vault_id, justification, "DECRYPT")
        
        # 3. Decrypt and return
        credential = self.decrypt(encrypted, {"vault_id": vault_id})
        
        # 4. Return credential with TTL enforcement
        return Credential(
            value=credential,
            ttl_minutes=5,
            vault_id=vault_id
        )
    
    def revoke_credential(self, vault_id: str):
        """Immediately invalidate a credential."""
        self._audit_log(vault_id, "MANUAL_REVOKE", "REVOKE")
        self._delete_from_vault(vault_id)
```

### VaultManager Configuration (config.yaml)
```yaml
vault:
  encryption: "AES-256-GCM"
  master_key_source: "osx_keychain"
  vault_path: "/Users/cobalt/.cobalt/vault.enc"
  default_ttl_minutes: 5
  audit_log_path: "/Users/cobalt/.cobalt/audit.log"
```

### Security Features
1. **AES-256-GCM Encryption**: Authenticated encryption with built-in integrity verification
2. **OS X Keychain Integration**: Master key never touches disk, stored in secure enclave
3. **Just-In-Time Decryption**: Secrets only decrypted when needed, immediately zeroed after use
4. **Audit Trail**: Every decrypt operation logged with timestamp, user, and justification
5. **TTL Enforcement**: Automatic credential expiry prevents stale secret exposure

## Implementation Details

### Approval Engine
- Runs as separate module in Cortex
- Uses Mattermost as approval interface
- Tracks approval status in memory

### Docker Sandbox
- Uses `docker-py` SDK
- Creates containers on-demand
- Cleans up after execution

### VaultManager Secret Store
- Custom AES-256-GCM implementation using `cryptography` library
- OS X Keychain integration for master key storage
- SQLite-backed encrypted vault with automatic cleanup

## Trade-offs

| Option | Pros | Cons |
|--------|------|------|
| LastPass JIT (Deprecated) | Managed service, easy setup | External dependency, cloud-based secrets |
| HashiCorp Vault | Enterprise features, complex | Overkill for single-node, operational overhead |
| VaultManager (Chosen) | Full control, local-only, no external deps | Requires maintenance of encryption logic |

## Next Steps

1. Implement Pydantic approval models
2. Create Mattermost approval UI
3. Build Docker sandbox runner
4. Deploy VaultManager with OS X Keychain integration

## References

- [Docker Seccomp Documentation](https://docs.docker.com/engine/security/seccomp/)
- [cryptography.io - AESGCM](https://cryptography.io/en/latest/hazmat/primitives/ciphers/aead/)
- [OS X Keychain Command Line](https://ss64.com/osx/security-find-generic-password.html)
- [src/cobalt_agent/security/vault.py](../../../src/cobalt_agent/security/vault.py)