---
title: "ADR-009 Agentic Browser Loop & Zero Trust"
status: Active
priority: P1
module: [Architecture, Tools, Security]
phase: 5
complexity: L
tags: [cobalt, architecture, documentation, adr, playwright, accessibility-object-model, cdn, pgvector, zero-trust]
created: 2026-02-25
updated: 2026-02-27
---

# ADR-009: Agentic Browser Loop & Zero Trust Architecture

## Status: ACCEPTED

## Decision
We will implement an **Agentic Browser Loop** that uses the **Accessibility Object Model (AOM)** via Chrome DevTools Protocol (CDP) to extract interactive elements from web pages. The LLM will operate on a compressed element tree with numeric IDs rather than raw HTML. To enable millisecond-latency execution for repeated tasks, we will implement a **pgvector "Fast Path" memory cache**. All browser operations will enforce **Zero-Trust constraints**: domain whitelisting, ephemeral browser contexts, and zero-knowledge credential injection via VaultManager.

## Context
The legacy scraping approach failed on Single Page Applications (SPAs) and sites requiring basic interaction. The initial JSON-based DSL approach was insufficient for complex, real-world web navigation where elements are dynamically generated and DOM structures change frequently.

The Agentic Browser Loop architecture enables autonomous, multi-step web interactions by:
1. **AOM/CDP Snapshot**: Extracting accessibility tree data and converting it to a compressed interactive element tree with numeric IDs, allowing the LLM to operate on stable identifiers rather than fragile CSS selectors.
2. **Fast Path Memory**: Using pgvector to cache task intents and associated Playwright scripts, bypassing LLM inference for repeated tasks and enabling millisecond-latency execution.
3. **Zero-Trust Security**: Enforcing domain whitelisting, ephemeral browser contexts for each session, and credential injection via VaultManager without storing sensitive data in the agent's memory.

## Implementation Details

### Phase 1: AOM Extractor
1. **Engine:** Playwright Chromium (Headless) with CDP session enabled.
2. **AOM Extraction:** Use `dom.snapshotter.takeDomSnapshot()` to extract the full DOM accessibility tree.
3. **Element Compression:** Convert the accessibility tree to a compressed interactive element tree containing:
   - Numeric ID (stable identifier for LLM reference)
   - Accessibility role (button, link, input, etc.)
   - Accessible name (label, placeholder, or text content)
   - Actionable state (enabled, visible, editable)
   - Optional: aria-label, aria-describedby, value (for inputs)

### Phase 2: LLM Interface & Pydantic Schema
1. **LLM Input**: The compressed element tree (JSON-serializable) with numeric IDs.
2. **LLM Output**: A Pydantic-constrained schema with actions:
   - `click(id: int)`: Click element by numeric ID
   - `type(id: int, text: str)`: Type text into element by numeric ID
   - `navigate(url: str)`: Navigate to URL (only if whitelisted)
3. **Validation**: Pydantic schema enforces strict action types; invalid outputs raise validation errors.

### Phase 3: Fast Path Memory (pgvector)
1. **Hash Computation**: Compute SHA-256 hash of task intent (user request + context).
2. **Lookup**: Query pgvector for similar task intents in the memory table.
3. **Cache Hit**: Execute stored Playwright script natively without LLM inference.
4. **Cache Miss**: Execute LLM inference, store resulting script in pgvector with intent hash.

### Phase 4: Zero-Trust Enforcement
1. **Domain Whitelisting**: Before navigation, check URL against `ALLOWED_DOMAINS` from config. Raise `SecurityViolation` if not whitelisted.
2. **Ephemeral Contexts**: Create a new `browser.new_context()` for each session; no cookies or storage persist between runs.
3. **Vault Credential Injection**: 
   - Retrieve credentials from VaultManager using vault_path from config
   - Inject credentials via `context.add_cookies()` or direct form filling
   - Never expose credentials to LLM or persistent storage

## Trade-offs
| Option | Pros | Cons |
|--------|------|
| HTML Parsing | Simple to implement, no browser needed | Fails on SPAs, fragile selectors, no dynamic interaction |
| JSON DSL | LLM can specify actions | Requires CSS selector generation, brittle to DOM changes |
| AOM/CDP Snapshot (Chosen) | Stable numeric IDs, accessible tree, works on all sites | Requires CDP session, more complex extraction logic |
| pgvector Fast Path | Millisecond latency for repeated tasks | Requires vector storage infrastructure |
| Zero-Trust | Security first, ephemeral sessions | More complex orchestration |

*Decision:* The AOM/CDP approach provides stable numeric IDs that the LLM can reference regardless of DOM structure changes. The pgvector Fast Path enables near-zero latency for repeated tasks, and Zero-Trust ensures Cobalt operates within strict security boundaries.

## Files Changed
- `src/cobalt_agent/tools/browser.py` - Complete rewrite with AOM extraction, Fast Path, and Zero-Trust
- `src/cobalt_agent/memory/postgres.py` - Add pgvector table for task intent caching
- `src/cobalt_agent/security/vault.py` - Integrate VaultManager for credential injection

## Dependencies Added
- `playwright` (via `uv add playwright`)
- `chromium` browser binaries (via `uv run playwright install chromium`)
- `pgvector` (via `uv add pgvector`)
- `sqlalchemy` (via `uv add sqlalchemy`)

## Security Considerations
1. **Domain Whitelisting**: All navigation requests are validated against `ALLOWED_DOMAINS` config.
2. **Ephemeral Contexts**: Each browser session creates a new context with `storage_state=None`.
3. **Zero-Knowledge Credentials**: VaultManager retrieves credentials on-demand; credentials are never stored in memory longer than necessary.
4. **HITL Boundary**: All mutation actions (navigation, form filling, clicking) require human-in-the-loop approval unless explicitly whitelisted.
