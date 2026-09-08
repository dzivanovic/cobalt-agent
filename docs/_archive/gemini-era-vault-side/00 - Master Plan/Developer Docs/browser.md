---
title: "Browser Tool Documentation"
status: Active
module: Tool
type: Class
dependencies:
  - "[[tool_manager]]"
  - "[[aom]]"
  - "[[maps]]"
  - "[[vault]]"
  - "[[postgres]]"
location: "src/cobalt_agent/tools/browser.py"
tags: [cobalt, dev_docs, browser, playwright, aom]
created: 2026-02-23
updated: 2026-02-27
---

# Browser Tool Module

**Location:** `src/cobalt_agent/tools/browser.py`

## Overview

Browser Tool executes browser automation tasks using Playwright and Chrome DevTools Protocol (CDP). Replaces legacy HTML scraping with compressed AOM element trees for reliable element referencing. Integrates with Vault for zero-knowledge credential injection and PostgreSQL for Fast Path memory caching.

### Key Features
- **Playwright Browser Automation** - Full headless browser control
- **AOM Extraction** - Compressed element trees with stable numeric IDs
- **Zero-Trust Security** - Domain whitelist enforcement via `ALLOWED_DOMAINS`
- **Vault Integration** - Zero-knowledge credential injection via `VaultManager`
- **Fast Path Cache** - pgvector-based macro execution via task hashing
- **Dual-Path Routing** - Intelligent fast path via llms.txt, fallback to Playwright

---

## Dual-Path Routing / Pre-Flight Protocol

### Overview

The Dual-Path Routing system enables Cobalt to intelligently choose between two execution paths:
1. **Fast Path**: Direct llms.txt markdown via HTTP (sub-millisecond to milliseconds)
2. **Fallback Path**: Playwright browser automation for complex interactions

This architecture dramatically reduces latency for read-only web content retrieval while maintaining full interactivity for complex tasks.

### Pre-Flight Protocol Flow

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                          Dual-Path Routing                                  │
├─────────────────────────────────────────────────────────────────────────────┤
│ 1. Request: URL without actions (read-only)                                 │
│ 2. Pre-Flight Check:                                                         │
│    - HTTP GET domain.com/llms.txt (Accept: text/markdown)                   │
│    - HTTP GET domain.com/llms-full.txt (Accept: text/markdown)              │
│    - HTTP GET url (Accept: text/markdown)                                   │
│ 3. If llms.txt HIT: Return markdown directly (no Playwright)                │
│ 4. If llms.txt MISS: Launch Playwright (full automation)                    │
└─────────────────────────────────────────────────────────────────────────────┘
```

### Fast Path Endpoints

The Pre-Flight Protocol checks for llms.txt files in the following order:

| Endpoint | Priority | Description |
|--|--|--|
| `https://domain.com/llms.txt` | High | Short markdown summary |
| `https://domain.com/llms-full.txt` | Medium | Full markdown content |
| `https://url` (Accept: text/markdown) | Low | Direct URL with markdown header |

### HTTP Headers

**Accept Header:** `Accept: text/markdown`

The Fast Path requests include `Accept: text/markdown` to signal to the Agentic Web that:
- The client can handle markdown responses
- JavaScript/rendering is not required
- The request is from an automated agent

**User-Agent Header:** `Cobalt-Watcher/1.0`

Identifies the request as coming from the Cobalt agent for rate-limiting and analytics.

### Implementation: `_execute_preflight_fast_path(url: str) -> Optional[str]`

```python
def _execute_preflight_fast_path(self, url: str) -> Optional[str]:
    """Check llms.txt endpoints before launching Playwright."""
    domain = extract_domain(url)
    
    fast_path_urls = [
        f"https://{domain}/llms.txt",
        f"https://{domain}/llms-full.txt",
    ]
    
    for fast_path_url in fast_path_urls:
        response = requests.get(fast_path_url, headers={
            "Accept": "text/markdown",
            "User-Agent": "Cobalt-Watcher/1.0"
        })
        
        if response.status_code == 200:
            content = response.text
            if is_markdown(content):
                return content  # Fast Path HIT
    
    return None  # Fall back to Playwright
```

### Path Decision Matrix

| Scenario | Path Used | Latency | Use Case |
|--|--|--|--|
| URL without actions, llms.txt exists | Fast Path | 5-50ms | News articles, docs, static content |
| URL without actions, llms.txt missing | Playwright | 1-5s | Interactive pages, dynamic content |
| URL with actions (click/type) | Playwright | 1-5s | Form filling, navigation, clicks |
| Rate-limited (429) | Playwright | 1-5s | Fallback on llms.txt overload |

### Benefits

1. **Latency Reduction**: 100x faster for llms.txt-supported sites
2. **Cost Efficiency**: Less Playwright usage = fewer browser instances
3. **Resource Conservation**: CPU/memory savings from skipped browser launch
4. **Agentic Web Support**: Standard protocol for LLM-to-agent communication

### Agentic Web Integration

Websites implementing the **Agentic Web Protocol** provide llms.txt files:

```
# Example llms.txt
# cobalt-agent:https://cobalt-agent.io

## Overview
This article describes the Watcher Daemon feature...

## Key Components
- Universal Extractor: Parses LLM output into graph entities
- Delta Engine: Computes differences against existing graph state
- APScheduler: Schedules recurring watcher jobs
```

### Metrics

| Metric | Value |
|--|--|--|
| Fast Path HIT Rate | ~40-60% (typical) |
| Fast Path Latency | 5-50ms |
| Playwright Latency | 1000-5000ms |
| Cache Hit Rate | ~25% (Fast Path cache) |

---

## Security: Domain Whitelist

### `ALLOWED_DOMAINS` Configuration

All URLs are validated against a whitelist defined in `configs/config.yaml`:

```yaml
browser:
  allowed_domains:
    - "example.com"
    - "wikipedia.org"
    - "github.com"
```

### URL Validation

- **HTTP/HTTPS URLs** - Domain extracted and validated against whitelist
- **File URLs (`file://`)** - Always allowed for local file access
- **SecurityViolation** - Raised for unwhitelisted URLs

---

## Pydantic Action Schema

### `BrowserAction` Model

Discriminated union for all browser actions:

```python
from pydantic import BaseModel, Field
from typing import Literal, Union

class ClickAction(BaseModel):
    action: Literal["click"]
    id: int  # AOM element ID

class TypeAction(BaseModel):
    action: Literal["type"]
    id: int  # AOM element ID
    text: str

class NavigateAction(BaseModel):
    action: Literal["navigate"]
    url: str

class ExtractAction(BaseModel):
    action: Literal["extract"]

BrowserAction = Union[ClickAction, TypeAction, NavigateAction, ExtractAction]
```

### Action Types

| Action | ID Field | Description |
|--|--|--|
| `click` | Yes | Click element by AOM ID |
| `type` | Yes | Type text into input by AOM ID |
| `navigate` | No | Navigate to URL (no ID needed) |
| `extract` | No | Extract AOM from current page |

---

## Class: `BrowserTool`

Executes browser automation tasks with AOM integration.

### Attributes

| Attribute | Value |
|--|--|
| `name` | `"browser"` |
| `description` | `"Execute browser automation tasks. Use for interactive web operations requiring element clicking, typing, or page navigation."` |
| `allowed_domains` | `list[str]` | Whitelisted domains from config |

### Methods

#### `run(url: str, actions: list[dict]) -> dict`

Execute browser actions on a URL.

**Parameters:**
- `url`: The URL to navigate to (validated against whitelist)
- `actions`: List of action dictionaries matching `BrowserAction` schema

**Returns:** Dictionary with `status`, `extracted_elements`, and `error` (if any)

**Workflow:**
1. Validate URL against domain whitelist
2. Launch Playwright headless browser
3. Navigate to URL
4. For each action:
   - Parse action into Pydantic model
   - Execute action (click, type, or navigate)
   - If element action, lookup AOM ID in Maps
   - If extract action, call AOMExtractor
5. Return results

**Error Handling:**
- Returns dictionary with `error` field on exception
- Re-infers action on `ValidationError`

### `inject_credentials(context: Page, vault_path: str) -> None`

Inject credentials from Vault into browser context.

**Parameters:**
- `context`: Playwright Page/Context to inject into
- `vault_path`: Path to credentials in Vault (e.g., "credentials/github")

**Zero-Knowledge Flow:**
1. Retrieve credentials from VaultManager
2. Inject via `context.add_init_script()` for automatic injection on navigation
3. Credentials exist only in memory during injection

---

## Integration with AOM and Maps

### Element Referencing Flow

```python
# 1. Extract AOM to get numeric IDs
elements = extractor.extract(url)

# 2. Populate Maps with element IDs and selectors
for element in elements:
    maps.add_element(element["id"], f'[aria-label="{element["name"]}"]')

# 3. Execute actions using AOM IDs
browser.run(url, actions=[{"action": "click", "id": 123}])

# 4. BrowserTool looks up ID in Maps to get selector
selector = maps.get_element(123)["selector"]
page.click(selector)
```

### Fast Path Cache Integration

```python
# Compute task hash from intent + context signature
task_hash = compute_task_hash(task_intent, context_signature)

# Query pgvector for similar cached tasks
cached_script = fast_path_cache.get(task_hash, threshold=0.85)

if cached_script:
    # Execute cached macro natively (millisecond latency)
    execute_script(cached_script)
else:
    # Execute LLM inference
    action = llm.infer(task_intent, elements)
    # Store result in Fast Path cache
    fast_path_cache.add(task_hash, action)
```

---

## Utility Functions

### `validate_url(url: str) -> bool`

Check if a URL is allowed by the domain whitelist.

```python
from cobalt_agent.tools.browser import validate_url

if validate_url(url):
    # Safe to navigate
    pass
```

### `compute_task_hash(intent: str, context_signature: str) -> str`

Compute SHA-256 hash for task identification.

**Parameters:**
- `intent`: Task description (e.g., "click login button")
- `context_signature`: Page context (URL + title + visible text preview)

**Returns:** Hex string of SHA-256 hash

---

## Example Usage

### Basic Navigation and Click

```python
from cobalt_agent.tools.browser import BrowserTool

browser = BrowserTool()
result = browser.run(
    url="https://example.com",
    actions=[
        {"action": "navigate", "url": "https://example.com/login"},
        {"action": "click", "id": 123},  # Click by AOM ID
    ]
)
```

### Type into Form and Submit

```python
result = browser.run(
    url="https://example.com",
    actions=[
        {"action": "type", "id": 456, "text": "username"},
        {"action": "type", "id": 789, "text": "password"},
        {"action": "click", "id": 101},  # Submit button
    ]
)
```

### Extract AOM Elements

```python
result = browser.run(
    url="https://example.com",
    actions=[
        {"action": "extract"},  # Extract AOM from current page
    ]
)

elements = result["extracted_elements"]
for element in elements:
    print(f"{element['role']}: {element['name']} (id={element['id']})")
```

### With Vault Credential Injection

```python
from cobalt_agent.tools.browser import BrowserTool
from cobalt_agent.security.vault import VaultManager

vault = VaultManager()
browser = BrowserTool()

# Inject credentials before navigation
with browser._get_context() as context:
    browser.inject_credentials(context, "credentials/github")

# Now login will use injected credentials
browser.run(
    url="https://github.com/login",
    actions=[...]
)
```

---

## Configuration

No additional configuration required. Uses global configuration from `configs/config.yaml`:

```yaml
browser:
  allowed_domains:
    - "example.com"
    - "wikipedia.org"
  headless: true  # Default
  timeout_ms: 30000  # Default
```

---

## Related Modules

- **AOM** (`src/cobalt_agent/tools/aom.py`) - Extracts compressed element trees
- **Maps** (`src/cobalt_agent/tools/maps.py`) - Maps AOM IDs to Playwright selectors
- **Vault** (`src/cobalt_agent/security/vault.py`) - Zero-knowledge credential storage
- **Postgres** (`src/cobalt_agent/memory/postgres.py`) - Fast Path cache with pgvector
- **Config** (`src/cobalt_agent/config.py`) - Domain whitelist and settings

---

## Migration from Legacy HTML Scraping

| Aspect | Legacy | New (AOM) |
|--|--|--|
| Element Reference | CSS/XPath selectors (fragile) | Numeric IDs (stable) |
| Page Content | Full HTML (high token usage) | Compressed element tree |
| State Management | None | Maps with invalidation |
| Error Handling | Selector not found | Element ID invalidation |

**Deprecation Note:** Raw HTML scraping is no longer used. All browser interactions use AOM element trees with numeric IDs.

---

## Performance

### Timing Metrics

| Operation | Typical Duration |
|--|--|
| Browser launch | ~500ms |
| Navigation | ~1-3s |
| AOM extraction | ~500ms |
| Element lookup (Maps) | ~1ms |
| Fast Path cache hit | ~5-10ms |
| LLM inference | ~1-3s |

### Latency Targets

| Scenario | Target Latency |
|--|--|
| Fast Path cache hit | <20ms |
| AOM extraction | <2s |
| First interaction | <5s |

---

## Debugging

Enable debug logging:

```python
import logging
logging.basicConfig(level=logging.DEBUG)

browser = BrowserTool()
browser.run(url="https://example.com", actions=[...])
```

### Log Messages

| Level | Message | Meaning |
|--|--|--|
| DEBUG | "Validating URL against whitelist" | URL validation check |
| INFO | "Executing action: click on element ID X" | Action execution |
| WARNING | "Element ID X not found in Maps" | Element not mapped |
| INFO | "Fast Path cache hit" | Cached macro used |
| WARNING | "Fast Path cache miss" | LLM inference needed |