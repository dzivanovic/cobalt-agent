---
title: "PRD-006: Agentic Browser Loop & Fast Path"
status: Approved
priority: P1
module: [Requirements, Architecture, Security]
phase: 5
complexity: L
tags: [cobalt, prd, requirements, accessibility-object-model, cdn, pgvector, zero-trust, playwright]
created: 2026-02-27
---

# PRD-006: Agentic Browser Loop & Fast Path

## 1. Executive Summary
**The Vision:** Give Cobalt "hands" to navigate the modern, dynamic web with millisecond latency for repeated tasks.
**The Problem:** Traditional scraping fails on Single Page Applications (SPAs) and interactive sites. Even with Playwright and JSON DSL, the LLM cannot reliably generate CSS selectors for dynamic DOM structures, and every task incurs full LLM inference latency.
**The Solution:** Implement an **Agentic Browser Loop** that extracts interactive elements from the Accessibility Object Model (AOM) via Chrome DevTools Protocol (CDP). The LLM operates on a compressed element tree with numeric IDs rather than HTML. For repeated tasks, a **pgvector "Fast Path"** caches task intents and executes stored Playwright scripts natively, achieving millisecond latency. All operations enforce **Zero-Trust**: domain whitelisting, ephemeral contexts, and zero-knowledge credential injection.

## 2. User Stories

### Story A: The Fast Path Cache
**As a** Daily Analyst,
**I want** Cobalt to remember how I navigate to my finance dashboard,
**So that** my daily task completes in milliseconds without re-inferencing the page structure.

### Story B: The Dynamic Navigation
**As a** Researcher,
**I want** Cobalt to read data from a modern web app (like TradingView or SEC Edgar),
**So that** I can get accurate data even if the HTML body is initially empty and requires JavaScript to render.

### Story C: The Vault-Secured Login
**As a** Chief of Staff,
**I want** Cobalt to securely retrieve credentials from VaultManager, navigate to a data portal, fill out the login form, and extract the dashboard text,
**So that** I can automate daily data extraction behind paywalls without exposing my passwords to the LLM or plain text logs.

## 3. Core Requirements

### 3.1 AOM Extraction (Phase 1)
1. **Engine:** Playwright Chromium (Headless) with CDP session enabled.
2. **DOM Snapshot:** Use `dom.snapshotter.takeDomSnapshot()` to extract the full DOM accessibility tree.
3. **Element Compression:** Convert the accessibility tree to a compressed interactive element tree containing:
   - `id`: Numeric ID (stable identifier for LLM reference)
   - `role`: Accessibility role (button, link, input, textarea, etc.)
   - `name`: Accessible name (label, placeholder, or text content)
   - `state`: Actionable state (enabled, visible, editable)
   - Optional: `aria-label`, `aria-describedby`, `value` (for inputs)

### 3.2 Pydantic Schema Constraint (Phase 2)
1. **LLM Input:** The compressed element tree (JSON-serializable) with numeric IDs.
2. **LLM Output:** A Pydantic-constrained schema with actions:
   - `click(id: int)`: Click element by numeric ID
   - `type(id: int, text: str)`: Type text into element by numeric ID
   - `navigate(url: str)`: Navigate to URL (only if whitelisted)
   - `extract()`: Return current page text after cleanup
3. **Validation:** Pydantic schema enforces strict action types; invalid outputs raise `ValidationError` and trigger re-inference.

### 3.3 Maps (Phase 2)
1. **AOM Maps:** Maintain a persistent mapping from numeric ID → DOM node, allowing the agent to execute actions without re-extracting the tree between steps.
2. **Tree Refresh:** After navigation, refresh the AOM tree and remap IDs. If an ID is no longer valid, re-infer the target element.

### 3.4 Vault Credential Injection (Phase 2)
1. **Credential Retrieval:** Use VaultManager to retrieve credentials based on `vault_path` from config.
2. **Credential Injection:** Inject credentials via:
   - `context.add_cookies()` for session-based auth
   - Direct form filling for explicit credentials (with Zero-Trust safeguards)
3. **Zero-Knowledge:** Credentials are never exposed to the LLM or logged; they exist only in memory during injection.

## 4. Performance Requirement: Fast Path Memory (Phase 3)

### 4.1 Fast Path Macro
1. **Hash Computation:** Compute SHA-256 hash of task intent (user request + context signature).
2. **Lookup:** Query pgvector memory table for similar task intents (cosine similarity threshold: 0.85).
3. **Cache Hit:** Execute stored Playwright script natively without LLM inference. This achieves **<50ms latency** for repeated tasks.
4. **Cache Miss:** Execute full LLM inference pipeline, then store resulting script in pgvector with:
   - Task intent hash
   - Compressed element tree snapshot
   - Playwright script
   - Success/failure metrics

### 4.2 Memory Schema (pgvector)
```python
Table: browser_fast_path
- task_hash (UUID)
- task_intent (TEXT)
- context_signature (TEXT)
- element_tree_snapshot (JSONB)
- playwright_script (TEXT)
- execution_time_ms (INTEGER)
- success_rate (FLOAT)
- created_at (TIMESTAMP)
```

## 5. Security Protocol: Zero-Trust Enforcement

### 5.1 Domain Whitelisting
1. **Validation:** Before any navigation, check URL against `ALLOWED_DOMAINS` from config.
2. **Strict Match:** Implement exact domain match (e.g., `finance.google.com` only if explicitly whitelisted).
3. **Violation:** Raise `SecurityViolation` exception if URL is not whitelisted; abort execution.

### 5.2 Ephemeral Browser Contexts
1. **New Context:** Create a new `browser.new_context()` for each session.
2. **No Persistence:** `storage_state=None` - no cookies, localStorage, or cache persist between runs.
3. **Isolation:** Each task runs in a completely clean environment.

### 5.3 HITL Boundary for Mutations
1. **Mutation Actions:** Navigation, form filling, clicking elements that alter state.
2. **Approval Required:** All mutations require human-in-the-loop approval unless:
   - URL is in `AUTO_APPROVED_DOMAINS` (from config)
   - Element is in `AUTO_APPROVED_ELEMENTS` (from config)
3. **Non-Mutation:** Reading page text is always allowed.

## 6. Technical Constraints
- Must run headlessly to avoid interrupting the user's primary desktop experience.
- Must include hard timeouts to prevent infinite hanging on broken selectors (default: 30 seconds).
- Must spoof User-Agent strings to minimize bot detection.
- Fast Path lookup must complete in <10ms (pgvector with vector index on task_hash).
- All LLM requests must use Pydantic response models with strict validation.

## 7. Failure Modes
| Mode | Response |
|------|----------|
| AOM extraction fails | Re-try once; if still fails, abort with `BrowserError` |
| LLM output invalid | Re-infer with error message in context; retry up to 3 times |
| Cache lookup timeout | Fall back to LLM inference |
| Domain not whitelisted | Raise `SecurityViolation`; abort execution |
| Credential injection fails | Raise `SecurityViolation`; abort execution |
| Element ID not found | Re-extract AOM tree; if still not found, abort with `ElementNotFoundError` |