---
title: JSON Serializers
status: Active
module: src/cobalt_agent/utils/serializers.py
tags:
  - serialization
  - json
  - utilities
  - pydantic
---

# JSON Serializers

Enterprise-grade JSON serialization utilities for RFC-compliant output.

## Overview

The `serializers` module provides custom JSON encoding functionality that handles Pydantic models, datetime objects, UUIDs, and fallback string conversion for unserializable objects such as Playwright DOM handles.

## Components

### CobaltJSONEncoder

Custom JSON encoder that extends `json.JSONEncoder` to handle specialized data types.

**Purpose:** Ensures RFC-compliant JSON output by explicitly handling all edge cases that may arise during tool execution, preventing LLM parsing hallucinations.

#### Methods

##### `default(obj)`

Override the default JSON encoder to handle additional types.

**Parameters:**
| Parameter | Type | Description |
|-----------|------|-------------|
| `obj` | Any | The object to serialize |

**Returns:** A JSON-serializable representation of the object

**Raises:** `TypeError` if the object cannot be serialized

**Handled Types:**
- `datetime.datetime` and `datetime.date` → ISO format strings via `isoformat()`
- `uuid.UUID` → String representation
- Pydantic `BaseModel` (v2+) → Dict via `model_dump()`
- Fallback objects (e.g., Playwright DOM handles) → String conversion via `str()`

### serialize_to_json

Convenience function to serialize any object to a JSON string.

**Signature:** `def serialize_to_json(obj) -> str`

**Parameters:**
| Parameter | Type | Description |
|-----------|------|-------------|
| `obj` | Any | The object to serialize |

**Returns:** A JSON-formatted string

**Raises:** `TypeError` if the object cannot be serialized

**Example Usage:**
```python
from cobalt_agent.utils.serializers import serialize_to_json

result = serialize_to_json(my_pydantic_model)
```

## Dependencies

- `json` (stdlib)
- `uuid` (stdlib)
- `datetime` (stdlib)
- `pydantic.BaseModel`