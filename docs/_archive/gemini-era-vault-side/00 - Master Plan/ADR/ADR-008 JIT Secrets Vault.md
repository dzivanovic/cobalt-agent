---
title: "ADR-008 JIT Secrets Vault"
status: Active
priority: P0
module: [Security, Core]
phase: 4
complexity: M
tags: [cobalt, architecture, security, secrets]
created: 2026-02-24
---

# ADR-008: Just-In-Time (JIT) Secrets Architecture

## Status: ACCEPTED

## Decision
We will transition away from static `.env` files for high-privilege API keys (e.g., TradeStation, OpenAI). Instead, we will implement a local, encrypted "Vault" service. The Cobalt Agent will request credentials "Just-In-Time" at runtime, hold them in RAM only for the duration of the execution context, and never log or write them to disk.

## Context
While the `.env` file is excluded from Git, storing static, long-lived credentials on the hard drive represents a single point of failure. By moving to a Vault architecture, we ensure that if the Cobalt script is hijacked, the attacker only gains access to an isolated process, not the master keys to the financial or cloud infrastructure.

## Implementation Details
1. **The Vault Daemon:** A highly restricted, independent process running on the Mac Studio that holds the encrypted keys.
2. **The Request Protocol:** Cobalt's `config.py` will be modified to request keys via an internal socket/API rather than reading `os.getenv`.
3. **RAM Only:** Credentials will be explicitly scrubbed from Pydantic models when serialized, ensuring they never leak into the Postgres Memory database.

## Trade-offs
| Option | Pros | Cons |
|--------|------|------|
| HashiCorp Vault | Industry standard | Overkill/too heavy for local node |
| Local Encrypted Daemon | Lightweight, fast | Requires custom implementation |

*Decision:* We will build a lightweight Local Encrypted Daemon specifically tuned for the Cobalt architecture.