---
status: To Do
priority: P2
module: Utils
phase: 4
complexity: S
tags: [cobalt, task, serialization]
created: 2026-03-07
---
# 44 Custom Pydantic Serializers

## Objective
Create custom Pydantic serializers for consistent JSON serialization across the Cobalt agent, particularly for state objects and tool responses.

## Description
Standardize serialization logic for complex types (datetime, UUID, custom dataclasses) used throughout the agent. This ensures reliable JSON payloads for logging, caching, and inter-process communication.

## Tasks
- [ ] Create `serializers.py` with custom JSON encoder
- [ ] Implement datetime ISO 8601 serialization
- [ ] Add UUID string conversion handler
- [ ] Support Pydantic v2 serializer decorators
- [ ] Write unit tests for edge cases

## Success Criteria
- All complex types serialize without errors
- Consistent output format across modules
- Unit test coverage > 90%