---
status: Wont-Do
priority: P1
module: Security
phase: 3
complexity: L
tags: [cobalt, task]
created: 2026-02-23
---
# 40 Tool LastPass Integration
# Task: Tool LastPass Integration

**Status**: To Do  
**Priority**: High  
**Tags**: security, secrets, tool  
**Created**: 2026-02-22

## Description

Add secure secrets retrieval integration with LastPass API using Just-In-Time (JIT) credential management. This enables the agent to access credentials without storing them in plaintext.

## Objectives

- Integrate LastPass API for credential retrieval
- Implement credential caching with TTL expiration
- Create audit logging for all credential access
- Securely handle credentials in memory

## Tasks

- [ ] Set up LastPass API credentials
- [ ] Create lastpass.py module in tools directory
- [ ] Implement get_credential(vault_id: str, justification: str) function
- [ ] Implement credential caching with 5-minute TTL
- [ ] Add audit logging for all credential access
- [ ] Create credential cleanup function

## Success Criteria

- Credentials retrieved via LastPass JIT API
- Credentials expire after 5 minutes
- All access logged for audit trail
- Credentials never written to disk

---
**Note**: Superseded by custom VaultManager.
