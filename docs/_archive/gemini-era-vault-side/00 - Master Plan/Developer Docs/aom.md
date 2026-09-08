---
title: "AOM (Accessibility Object Model) Extractor Documentation"
status: Active
module: Tools
type: Class
dependencies:
  - "[[tool_manager]]"
  - "[[browser]]"
  - "[[config]]"
location: "src/cobalt_agent/tools/aom.py"
tags: [cobalt, dev_docs, aom, cdp, accessibility]
created: 2026-02-27
---

# AOM (Accessibility Object Model) Extractor

**Location:** `src/cobalt_agent/tools/aom.py`

## Overview

The AOM Extractor module uses Chrome DevTools Protocol (CDP) to extract the DOM tree from web pages and convert it to a compressed accessibility object model format. This replaces fragile HTML parsing with stable numeric element IDs for reliable agent navigation.

### Key Features
- **CDP Snapshot Extraction** - Uses `DOMSnapshot.captureSnapshot` for complete DOM access
- **Compressed Dictionary Schema** - `id, role, name, state` for minimal token usage
- **Domain Whitelist Security** - Zero-Trust enforcement via `ALLOWED_DOMAINS` config
- **Ephemeral Context** - No persistent storage state between extractions

---

## Security: Domain Whitelist

### `ALLOWED_DOMAINS` Configuration

All HTTP/HTTPS URLs are validated against a whitelist defined in `configs/config.yaml`:

```yaml
browser:
  allowed_domains:
    - "example.com"
    - "wikipedia.org"
    - "github.com"
```

### URL Validation Logic

- **File URLs (`file://`)** - Always allowed for local file access
- **HTTP/HTTPS URLs** - Extracted domain validated against whitelist
- **Port Handling** - Ports are stripped before comparison (e.g., `example.com:8080` → `example.com`)

### `SecurityViolation` Exception

Raised when a URL fails domain whitelist validation:

```python
from cobalt_agent.tools.aom import SecurityViolation

try:
    extractor.extract("https://malicious-site.com")
except SecurityViolation as e:
    logger.error(f"Blocked: {e}")
```

---

## Class: `AOMExtractor`

Extracts DOM tree via CDP and converts to compressed format.

### Constructor

```python
AOMExtractor()
```

Initializes with domain whitelist from config (defaults to `["example.com"]` if not set).

### Attributes

| Attribute | Type | Description |
|--|--|--|
| `allowed_domains` | `list[str]` | Whitelisted domains from config |
| `_extracted_tree` | `Optional[dict]` | Most recently extracted tree |

### Methods

#### `extract(url: str, timeout_ms: int = 15000) -> list[dict]`

Extract the DOM tree from a URL using CDP.

**Parameters:**
- `url`: The URL to extract AOM from
- `timeout_ms`: Timeout in milliseconds (default 15000)

**Returns:** List of compressed element dictionaries

**Raises:**
- `SecurityViolation`: If domain is not whitelisted
- `Exception`: For browser/CDP errors

**Workflow:**
1. Validate URL against domain whitelist
2. Launch headless Chromium with Playwright
3. Create ephemeral context (no storage state)
4. Navigate to URL with `wait_until="domcontentloaded"`
5. Wait 2 seconds for dynamic content to settle
6. Create CDP session via `context.new_cdp_session(page)`
7. Call `CDP.send("DOMSnapshot.captureSnapshot", ...)`
8. Parse snapshot into compressed element format

---

## Compressed Element Schema

Each element in the returned list follows this schema:

```python
{
    "id": int,               # Stable numeric ID for referencing
    "role": str,             # Accessibility role (button, link, heading, etc.)
    "name": str,             # Accessible name (aria-label, text content, etc.)
    "state": dict,           # Actionable state properties
    "aria": dict,            # Optional aria-* attributes
    "value": str,            # Optional value (for inputs)
}
```

### Element `state` Dictionary

| Key | Type | Description |
|--|--|--|
| `enabled` | `bool` | Element is not disabled |
| `visible` | `bool` | Element is not hidden/aria-hidden |
| `editable` | `bool` | Element accepts text input |
| `clickable` | `bool` | Element has click handler or role |
| `name` | `str` | Accessible name override |

### Element `aria` Dictionary

Contains all `aria-*` attributes found on the element:

```python
{
    "aria-label": "Close dialog",
    "aria-describedby": "error-message",
    "aria-hidden": "false"
}
```

---

## Role Mapping

The extractor maps DOM node types to accessibility roles:

| Node Type | Tag/Type | Role |
|--|--|--|
| 1 | `button` | `button` |
| 1 | `a` | `link` |
| 1 | `input` | `input` |
| 1 | `h1`-`h6` | `heading` |
| 1 | `img` | `image` |
| 1 | `table` | `table` |
| 1 | `li` | `listitem` |
| 3 | Text node | `text` |
| 8 | Comment node | `comment` |
| 9 | Document node | `document` |
| 1 | Generic element | `generic` |

---

## Utility Functions

### `extract_aom(url: str) -> list[dict]`

Convenience function to extract AOM from a URL.

```python
from cobalt_agent.tools.aom import extract_aom

elements = extract_aom("https://example.com")
```

### `is_url_allowed(url: str) -> bool`

Check if a URL is allowed by the domain whitelist.

```python
from cobalt_agent.tools.aom import is_url_allowed

if is_url_allowed(url):
    # Safe to extract
    pass
```

---

## CDP Snapshot Structure

The raw CDP snapshot contains:

```python
{
    "nodes": list,           # Array of node data (flat list)
    "strings": list[str],    # String table for node attributes
    "window_ids": list[int], # Window IDs
    "root_indices": list[int], # Root node indices
    "backend_node_ids": list[int], # Backend node IDs
}
```

### Node Encoding

Nodes are stored as a flat list where each node's data is a list:

```python
# Node structure (variable length):
[node_type, name_string_idx, value_string_idx, attr1_key, attr1_value, attr2_key, attr2_value, ...]

# Example node:
[1, 5, -1, 12, "button", 15, "click me"]  # Button element
```

---

## Example Usage

### Basic Extraction

```python
from cobalt_agent.tools.aom import AOMExtractor

extractor = AOMExtractor()
elements = extractor.extract("https://example.com")

for element in elements:
    print(f"{element['role']}: {element['name']} (id={element['id']})")
```

### Using Extracted IDs with Maps

```python
from cobalt_agent.tools.aom import AOMExtractor
from cobalt_agent.tools.maps import get_maps

extractor = AOMExtractor()
elements = extractor.extract("https://example.com")

# Update Maps with the new elements
maps = get_maps()
for element in elements:
    maps.add_element(element['id'], f"[id='{element['id']}']")
```

### Error Handling

```python
from cobalt_agent.tools.aom import AOMExtractor, SecurityViolation

extractor = AOMExtractor()

try:
    elements = extractor.extract("https://unauthorized-site.com")
except SecurityViolation as e:
    logger.error(f"Domain not whitelisted: {e}")
except Exception as e:
    logger.exception(f"AOM extraction failed: {e}")
```

---

## Performance Considerations

1. **Ephemeral Context** - Each extraction uses a fresh browser context with no persistent storage
2. **Dynamic Wait** - 2-second wait after navigation for JavaScript to settle
3. **CDP Session** - Created per-extraction; closed when browser context exits
4. **Timeout** - 15-second default; configurable per-extraction

### Timing Metrics

| Operation | Typical Duration |
|--|--|
| Browser launch | ~500ms |
| Navigation | ~1-3s |
| Wait for content | 2s |
| CDP snapshot | ~500ms |
| Parsing | ~100ms |
| **Total** | ~4-6s |

---

## Debugging

Enable debug logging for detailed CDP extraction info:

```python
import logging
logging.basicConfig(level=logging.DEBUG)

extractor = AOMExtractor()
elements = extractor.extract("https://example.com")
```

### Common Issues

| Issue | Symptom | Solution |
|--|--|--|
| Domain blocked | `SecurityViolation` | Add domain to `config.yaml` |
| CDP timeout | Browser hangs | Increase `timeout_ms` parameter |
| Empty snapshot | No elements returned | Check page loads correctly in headless mode |
| Node parsing error | `IndexError` in `_process_node` | Check CDP snapshot structure |

---

## Configuration

No additional configuration required. Domain whitelist is read from `configs/config.yaml`:

```yaml
browser:
  allowed_domains:
    - "example.com"
    - "wikipedia.org"
```

### Default Values

| Setting | Default |
|--|--|
| `allowed_domains` | `["example.com"]` |
| `timeout_ms` | `15000` |
| Dynamic wait | `2000ms` |

---

## Related Modules

- **Maps** (`src/cobalt_agent/tools/maps.py`) - Maps numeric IDs to Playwright ElementHandles
- **Browser** (`src/cobalt_agent/tools/browser.py`) - High-level browser tool using AOM IDs
- **Config** (`src/cobalt_agent/config.py`) - Domain whitelist configuration