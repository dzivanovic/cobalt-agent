---
title: "AOM Maps Documentation"
status: Active
module: Tools
type: Class
dependencies:
  - "[[aom]]"
  - "[[browser]]"
  - "[[postgres]]"
location: "src/cobalt_agent/tools/maps.py"
tags: [cobalt, dev_docs, maps, elements, playwright]
created: 2026-02-27
---

# AOM Maps Module

**Location:** `src/cobalt_agent/tools/maps.py`

## Overview

The Maps module provides stateful mapping between numeric AOM IDs and Playwright ElementHandles. This enables reliable element referencing across browser interactions while preventing stale element reference errors through tree refresh management.

### Key Features
- **Numeric ID to ElementHandle Mapping** - Stable references for agent actions
- **Tree Refresh on Navigation** - Invalidates stale elements when page changes
- **Thread-Safe Access** - Lock-based concurrency control (optional)
- **Singleton Pattern** - Global instance for consistent state across tool calls

---

## Class: `Maps`

Manages the mapping between AOM numeric IDs and Playwright ElementHandles.

### Constructor

```python
Maps()
```

Initializes with empty cache and no page reference.

### Attributes

| Attribute | Type | Description |
|--|--|--|
| `_element_cache` | `Dict[int, Dict[str, Any]]` | Maps element IDs to reference data |
| `_current_url` | `Optional[str]` | Current page URL being mapped |
| `_page` | `Optional[Page]` | Current Playwright Page object |
| `_lock` | `Optional[threading.Lock]` | Optional thread-safety lock |

### Reference Data Structure

Each cached element stores:

```python
{
    "id": int,              # AOM numeric ID
    "selector": str,        # CSS selector for Playwright
    "created_at": float,    # Timestamp of mapping creation
    "valid": bool,          # Whether element is still valid
    "has_handle": bool      # Whether ElementHandle was captured (not pickled)
}
```

---

## Methods

### `add_element(element_id: int, selector: str, element: Optional[ElementHandle] = None) -> None`

Add or update an element mapping.

**Parameters:**
- `element_id`: The numeric ID from AOM extraction
- `selector`: The CSS selector to locate the element
- `element`: Optional ElementHandle reference (not stored - Playwright can't serialize)

**Behavior:**
- Updates existing mapping if ID already exists
- Stores selector and creation timestamp
- Marks element as valid
- Logs debug info

### `get_element(element_id: int) -> Optional[Dict[str, Any]]`

Retrieve an element reference by its ID.

**Parameters:**
- `element_id`: The numeric ID to look up

**Returns:**
- Dictionary with reference data if found and valid
- `None` if not found or marked invalid

**Behavior:**
- Checks element validity before returning
- Logs warning if element is marked invalid

### `remove_element(element_id: int) -> bool`

Remove an element from the cache.

**Parameters:**
- `element_id`: The numeric ID to remove

**Returns:**
- `True` if element was removed
- `False` if not found

### `refresh_tree(page: Page, new_url: Optional[str] = None) -> None`

Invalidate all cached elements and update URL.

**Parameters:**
- `page`: The current Playwright Page object
- `new_url`: Optional new URL after navigation

**Behavior:**
- Marks all cached elements as `valid: False`
- Updates current URL
- Updates page reference

**Usage:**
```python
# Call after navigation
maps.refresh_tree(page, new_url)
```

### `clear() -> None`

Clear all cached elements.

Resets all state: clears cache, URL, and page reference.

### `get_all_elements() -> Dict[int, Dict[str, Any]]`

Get all cached elements.

**Returns:** Complete element cache dictionary

### `is_valid_element(element_id: int) -> bool`

Check if an element ID is valid.

**Parameters:**
- `element_id`: The numeric ID to check

**Returns:**
- `True` if element exists and is marked valid
- `False` otherwise

### `invalidate_all() -> None`

Mark all cached elements as invalid.

Does not clear the cache, just marks all elements as invalid.

### `get_current_url() -> Optional[str]`

Get the current URL being mapped.

**Returns:** Current URL or `None` if not set

### `set_page(page: Page) -> None`

Set the current Playwright page.

**Parameters:**
- `page`: The Playwright Page object

### `get_page() -> Optional[Page]`

Get the current Playwright page reference.

**Returns:** Page object or `None`

### `find_element_by_selector(selector: str) -> Optional[Dict[str, Any]]`

Find an element by its CSS selector.

**Parameters:**
- `selector`: The CSS selector to search for

**Returns:**
- Element reference data if found and valid
- `None` if not found

---

## Utility Functions

### `get_maps() -> Maps`

Get the global Maps singleton instance.

**Returns:** The Maps instance (creates if not exists)

**Usage:**
```python
from cobalt_agent.tools.maps import get_maps

maps = get_maps()
maps.add_element(123, "button#submit")
```

### `reset_maps() -> Maps`

Reset the global Maps instance.

**Returns:** A new Maps instance

**Usage:**
```python
from cobalt_agent.tools.maps import reset_maps

maps = reset_maps()  # Clears all cached elements
```

### `refresh_maps_tree(page: Page, new_url: Optional[str] = None) -> None`

Convenience function to refresh the global Maps tree.

**Parameters:**
- `page`: The current Playwright Page object
- `new_url`: Optional new URL after navigation

**Usage:**
```python
from cobalt_agent.tools.maps import refresh_maps_tree

refresh_maps_tree(page, new_url)
```

---

## Element Lifecycle

### 1. Extraction

AOM extraction generates numeric IDs:

```python
from cobalt_agent.tools.aom import AOMExtractor

extractor = AOMExtractor()
elements = extractor.extract("https://example.com")

# Each element has a numeric ID
for element in elements:
    element_id = element["id"]  # Stable numeric ID
    selector = element["aria"]["aria-label"] or element["name"]
```

### 2. Mapping

Store element references in Maps:

```python
from cobalt_agent.tools.maps import get_maps

maps = get_maps()
for element in elements:
    maps.add_element(
        element["id"],
        f'[aria-label="{element["name"]}"]'
    )
```

### 3. Action Execution

Execute actions using numeric IDs:

```python
selector = maps.get_element(element_id)["selector"]
page.click(selector)
```

### 4. Navigation Refresh

After navigation, refresh the tree:

```python
page.goto(new_url)
maps.refresh_tree(page, new_url)
```

---

## Stale Element Prevention

The Maps module prevents stale element reference errors through:

1. **Invalidation on Navigation** - All elements marked invalid on `refresh_tree()`
2. **Validation Check** - `get_element()` returns `None` for invalid elements
3. **Re-extraction** - Agent re-extracts AOM after navigation

### Error Handling Flow

```python
selector = maps.get_element(element_id)
if not selector:
    # Element no longer valid - re-extract AOM
    elements = extractor.extract(page.url)
    for element in elements:
        maps.add_element(element["id"], selector)
    selector = maps.get_element(element_id)
```

---

## Thread Safety

The Maps class supports optional thread safety:

```python
import threading
from cobalt_agent.tools.maps import Maps

maps = Maps()
maps._lock = threading.Lock()  # Enable thread safety
```

When `_lock` is set, critical sections should acquire the lock:

```python
if maps._lock:
    with maps._lock:
        # Thread-safe operation
        pass
else:
    # Non-thread-safe operation
    pass
```

---

## Integration with BrowserTool

The BrowserTool uses Maps for element referencing:

```python
from cobalt_agent.tools.browser import BrowserTool

browser = BrowserTool()
# BrowserTool automatically initializes Maps singleton

# Execute click by AOM ID
browser.run(
    url="https://example.com",
    actions=[{"action": "click", "id": 123}]
)
```

The BrowserTool handles stale element detection and re-extraction automatically.

---

## Performance Considerations

### Cache Efficiency

| Operation | Complexity | Notes |
|--|--|--|
| `add_element` | O(1) | Dictionary insert |
| `get_element` | O(1) | Dictionary lookup |
| `refresh_tree` | O(n) | Iterates all elements |
| `find_element_by_selector` | O(n) | Linear search |

### Memory Usage

Each cached element stores:
- 1 int (ID) - 28 bytes
- 1 str (selector) - ~60 bytes average
- 1 float (timestamp) - 24 bytes
- 2 bools - ~12 bytes

**Total per element:** ~124 bytes

**1000 elements:** ~124 KB

---

## Example Usage

### Complete Workflow

```python
from cobalt_agent.tools.aom import AOMExtractor
from cobalt_agent.tools.maps import get_maps
from playwright.sync_api import sync_playwright

# 1. Extract AOM
extractor = AOMExtractor()
elements = extractor.extract("https://example.com")

# 2. Populate Maps
maps = get_maps()
for element in elements:
    maps.add_element(
        element["id"],
        f'[aria-label="{element["name"]}"]'
    )

# 3. Navigate and use Maps
with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page()
    page.goto("https://example.com")
    
    # 4. Refresh Maps after navigation
    maps.refresh_tree(page, page.url)
    
    # 5. Execute action
    selector = maps.get_element(123)["selector"]
    page.click(selector)
    
    browser.close()
```

### Error Recovery

```python
from cobalt_agent.tools.maps import get_maps
from playwright.sync_api import TimeoutError as PlaywrightTimeoutError

maps = get_maps()

try:
    selector = maps.get_element(element_id)["selector"]
    page.click(selector)
except PlaywrightTimeoutError:
    # Element not found - re-extract AOM
    elements = extractor.extract(page.url)
    for element in elements:
        maps.add_element(element["id"], selector)
    # Retry with fresh elements
    selector = maps.get_element(element_id)["selector"]
    page.click(selector)
```

---

## Configuration

No configuration required. The Maps module uses default Playwright selectors and AOM extraction IDs.

---

## Related Modules

- **AOM** (`src/cobalt_agent/tools/aom.py`) - Extracts elements with numeric IDs
- **Browser** (`src/cobalt_agent/tools/browser.py`) - Uses Maps for action execution
- **Postgres** (`src/cobalt_agent/memory/postgres.py`) - Fast Path cache stores element trees

---

## Debugging

Enable debug logging to track element mappings:

```python
import logging
logging.basicConfig(level=logging.DEBUG)

maps = get_maps()
maps.add_element(123, "button#submit")
```

### Log Messages

| Level | Message | Meaning |
|--|--|--|
| DEBUG | "Adding new element mapping for ID X" | First mapping for ID |
| DEBUG | "Updating existing element mapping for ID X" | ID already mapped |
| INFO | "Refreshing Maps tree - invalidating all cached elements" | Tree refresh |
| WARNING | "Element ID X is marked as invalid" | Invalid element accessed |

### Common Issues

| Issue | Cause | Solution |
|--|--|--|
| Element not found | Tree not refreshed after navigation | Call `refresh_tree()` after navigation |
| Stale element error | Reused ElementHandle from previous page | Re-extract AOM after navigation |
| Multiple mappings | Same selector for multiple elements | Use more specific selectors |