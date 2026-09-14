# PRD-011: Zero Trust Security

**Status:** ✅ Implemented  
**Priority:** P0 - Critical Infrastructure  
**Author:** Cobalt Engineering Team  
**Date:** 2025-02-23  

---

## Executive Summary

Cobalt implements a **Zero Trust security model** with Just-In-Time (JIT) secrets management and Human-in-the-Loop (HITL) approval gates. No action executes without proper authorization, and all secrets are encrypted at rest with AES-256.

---

## Technical Implementation

### Core Components

#### 1. VaultManager (JIT Secrets Manager)
**File:** `src/cobalt_agent/security/vault.py`

AES-256 encrypted local credential storage with in-memory operations.

**Key Features:**
- **AES-256 Encryption**: Uses Fernet (cryptography library) for symmetric encryption
- **In-Memory Operations**: Secrets exist only in RAM when unlocked
- **JIT Access**: Secrets decrypted on-demand, never persisted unencrypted

```python
# Vault lifecycle
vault = VaultManager()
vault.generate_master_key()  # Run once to create key
vault.unlock(master_key)     # Decrypt vault into RAM
secret = vault.get_secret("API_KEY")  # Retrieve secret
vault.lock()                 # Wipe secrets from RAM
```

**Security Properties:**
| Operation | Behavior |
|-----------|----------|
| `generate_master_key()` | Creates new Fernet AES-256 key |
| `unlock(key)` | Decrypts vault file into `_secrets` dict |
| `get_secret(name)` | Returns secret from RAM only if unlocked |
| `set_secret(key, name, value)` | Encrypts and saves to disk |
| `lock()` | Calls `.clear()` on `_secrets` dict (RAM wipe) |

### 2. Mattermost HITL Proposal Engine
**File:** `src/cobalt_agent/core/proposals.py`

Human-in-the-Loop approval system for high-risk actions.

**Workflow:**
1. **Intercept**: Cortex identifies high-risk action (delete, modify, etc.)
2. **Pause**: Action execution halted before tool call
3. **Propose**: Proposal stored in PostgreSQL with `pending` status
4. **Broadcast**: Card sent to Mattermost approval channel
5. **Approve/Reject**: Admin responds with `approve [id]` or `reject [id]`
6. **Execute**: If approved, tool executes; if rejected, abort

```python
# Proposal lifecycle
engine = ProposalEngine()
task_id = engine.create_proposal("delete_file", {"path": "secret.txt"})
# Sends to Mattermost: "Action paused. Proposal [abc12345] sent to Admin"

# Admin approval flow
result = engine.handle_approval_response("approve abc12345", channel_id)
# Returns tool payload for execution
```

### 3. HITL Bouncer (Tool Interceptor)
**File:** `src/cobalt_agent/tools/tool_manager.py`

Intercepts tool calls requiring human approval.

**Protected Actions:**
- File system modifications (delete, write)
- Browser automation with side effects
- Any action flagged in `config.yaml`

```python
# Tool execution with HITL check
result = ToolManager().execute_tool(
    name="filesystem", 
    args={"action": "delete", "path": "secret.txt"},
    bypass_hitl=False  # Default: check for approval
)

# Returns HITL status if approval required
if result.get("status") == "requires_approval":
    # Proposal created, awaiting human approval
```

---

## Security Architecture

### Defense in Depth Layers

1. **Layer 1: Vault Encryption**
   - Secrets encrypted at rest with AES-256
   - Master key never stored (user-provided)

2. **Layer 2: HITL Interceptor**
   - High-risk actions paused before execution
   - Human approval required via Mattermost

3. **Layer 3: Secret Scrubbing**
   - Memory system scrubs secrets before storage
   - `_scrub_secrets()` uses VaultManager to detect patterns

4. **Layer 4: Principle of Least Privilege**
   - Tools operate with minimal permissions
   - No elevated system access

### HITL Decision Matrix

| Action Type | Risk Level | HITL Required? |
|-------------|------------|----------------|
| Read file | Low | No |
| Write file | Medium | Yes (configurable) |
| Delete file | High | **Yes** |
| Browser navigation | Low | No |
| Form submission | Medium | Yes (configurable) |
| System commands | Critical | **Yes** |

---

## Integration Points

### Dependencies
- `cryptography` - AES-256 Fernet encryption
- `pydantic` - Structured proposal validation
- `psycopg` - PostgreSQL for HITL persistence

### Environment Configuration

Required environment variables:
```bash
# Vault master key (stored securely, not in repo)
VAULT_MASTER_KEY=your_master_key

# Mattermost for HITL notifications
MATTERMOST_URL=https://mattermost.example.com
MATTERMOST_TOKEN=bot_token
MATTERMOST_APPROVAL_TEAM=admins
```

---

## API Reference

### VaultManager Methods

```python
# Initialize vault
vault = VaultManager(vault_path="data/.cobalt_vault")

# Generate master key (run once)
master_key = vault.generate_master_key()  # Save this securely!

# Unlock vault (decrypt into RAM)
vault.unlock(master_key)

# Store secrets
vault.set_secret(master_key, "API_KEY", "secret_value")

# Retrieve secrets
api_key = vault.get_secret("API_KEY")

# List all secret names (not values)
secret_names = vault.list_secrets()

# Delete secrets
vault.delete_secret(master_key, "API_KEY")

# Lock vault (wipe RAM)
vault.lock()
```

### ProposalEngine Methods

```python
# Create new proposal (returns task_id)
task_id = engine.create_proposal("delete_file", {"path": "secret.txt"})

# Handle admin approval response
result = engine.handle_approval_response("approve abc12345", channel_id)

# Connect to Mattermost for broadcasting
engine.connect_mattermost()

# Send proposal card (called internally)
engine.send_proposal(proposal_obj)
```

---

## Acceptance Criteria

- [x] VaultManager encrypts secrets with AES-256 Fernet
- [x] Secrets exist only in RAM when vault is unlocked
- [x] `lock()` method wipes secrets from memory
- [x] High-risk actions trigger HITL proposal creation
- [x] Proposal cards formatted for Mattermost display
- [x] Admin approval/rejection properly handled
- [x] HITL Bouncer intercepts tool calls before execution
- [x] Secret scrubbing prevents storage of sensitive values

---

## Security Audit Checklist

- [x] No hardcoded secrets in source code
- [x] All credentials loaded from environment or vault
- [x] Memory system scrubs secrets before persistence
- [x] HITL approval required for destructive actions
- [x] Vault encryption uses industry-standard Fernet (AES-256)
- [x] Master key never persisted to disk

---

## Future Enhancements

1. **Hardware Security Module (HSM)**: Integration with YubiKey or similar
2. **Multi-Signature Approval**: Require multiple approvers for critical actions
3. **Audit Logging**: Immutable log of all HITL decisions
4. **Time-Limited Tokens**: Automatic expiration of approved actions

---

## Related Documents

- [ADR-008: JIT Secrets Vault](../ADR/ADR-008%20JIT%20Secrets%20Vault.md)
- [ADR-014: Unified MoE Architecture](../ADR/ADR-014%20Unified%20MoE%20Architecture.md)
- [PRD-007: Sovereign Split-Brain Orchestration](./PRD-007%20Sovereign%20Split-Brain%20Orchestration.md)