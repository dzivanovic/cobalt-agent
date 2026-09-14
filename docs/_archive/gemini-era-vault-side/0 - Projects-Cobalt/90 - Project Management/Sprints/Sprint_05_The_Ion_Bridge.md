---
title: "Sprint 05: The Ion Bridge"
date: 2026-03-10
sprint: 5
status: To Do
tags: [cobalt, sprint, ion-bridge, zeromq, cross-platform]
---

# Sprint 05: The Ion Bridge

## Focus

Establish a ZeroMQ PUB/SUB link between the Mac Studio (Spotter) and Windows environment (Sniper) to transmit JSON math payloads. Architecture pending.

## Overview

This sprint establishes the foundational cross-platform communication channel for Cobalt's distributed architecture. The Ion Bridge enables seamless data exchange between the Mac Studio development environment and Windows-based trading infrastructure using ZeroMQ's PUB/SUB pattern.

## Sprint Goals

1. Design and document the Ion Bridge architecture
2. Implement ZeroMQ PUB/SUB server on Mac Studio (Spotter)
3. Implement ZeroMQ SUB client on Windows environment (Sniper)
4. Define JSON payload schema for math/trading operations
5. Establish connection health monitoring and reconnection logic

## Deliverables

### 3.1 Ion Bridge Architecture Document
- **File:** `docs/0 - Projects/Cobalt/00 - Master Plan/Developer Docs/ion_bridge.md`
- **Content:**
  - ZeroMQ PUB/SUB pattern justification
  - Network topology and security considerations
  - Payload schema definition
  - Failure mode handling

### 3.2 Ion Bridge Server (Mac Studio)
- **File:** `src/cobalt_agent/services/ion_bridge.py`
- **Functionality:**
  - ZeroMQ PUB socket for broadcasting JSON payloads
  - Topic-based message routing
  - Connection state management
  - Logging and metrics

### 3.3 Ion Bridge Client (Windows)
- **File:** `src/cobalt_agent/services/ion_bridge_client.py`
- **Functionality:**
  - ZeroMQ SUB socket for receiving messages
  - Topic filtering and subscription management
  - Automatic reconnection on disconnect
  - Message validation and parsing

### 3.4 JSON Payload Schema
- **File:** `src/cobalt_agent/schemas/ion.py`
- **Models:**
  ```python
  class IonMessage(BaseModel):
      message_id: UUID
      timestamp: datetime
      topic: str
      payload: dict
      signature: str  # For integrity verification
  
  class MathPayload(BaseModel):
      operation: str  # e.g., "calculate", "analyze"
      parameters: dict
      correlation_id: UUID
  ```

## Testing Plan

- [ ] End-to-end message delivery between Mac Studio and Windows
- [ ] Topic-based subscription filtering
- [ ] Reconnection logic after network interruption
- [ ] Payload serialization/deserialization validation
- [ ] Load testing with concurrent subscribers

## Success Criteria

1. ZeroMQ PUB/SUB channel established between Mac Studio and Windows
2. JSON math payloads transmitted successfully with <100ms latency
3. Automatic reconnection within 5 seconds of disconnection
4. Message integrity verified via signature validation
5. Architecture document approved and version-controlled

## Dependencies

- Network connectivity between Mac Studio and Windows environments
- ZeroMQ library availability on both platforms
- Firewall configuration for inter-machine communication

## Risks & Mitigations

| Risk | Impact | Mitigation |
|------|--------|------------|
| Network firewall blocks ZeroMQ ports | High | Document required ports; provide SSH tunnel fallback |
| Windows environment unavailable | Medium | Implement graceful degradation with local queue |
| Message ordering issues | Medium | Use sequence numbers and acknowledgment protocol |