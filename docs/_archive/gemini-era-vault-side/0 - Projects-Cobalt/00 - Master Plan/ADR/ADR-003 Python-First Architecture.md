---
title: "ADR-003 Python-First Architecture"
status: Active 
priority: P0
module: [Architecture]
phase: 1
complexity: M
tags: [cobalt, architecture, documentation, adr]
created: 2026-02-23
---

# ADR-003: Python-First Architecture

## Status: ACCEPTED

## Decision

We will use **Python (FastAPI)** for the Cobalt agent and **Rust** for the Ion HUD client.

* **Cobalt (Mac)**: Python FastAPI for the core agent system (orchestration, LLM integration, routing, tool execution)
* **Ion (Windows)**: Rust for the real-time trading visualization and UI
* **Reasoning**: Python provides the fastest development velocity and best LLM integration ecosystem. Rust provides safe, high-performance UI rendering.

## Architecture

```
                    ┌───────────────┐
                    │    Mac        │
                    │   Cobalt      │
                    │   (Python)    │
                    └───┬───┬───────┘
                        │   │
              ┌─────────▼───▼───────┐
              │   Message Broker    │
              │   (Redis/ZeroMQ)    │
              └───┬───┬──────┬──────┘
                  │   │      │
    ┌──────────┐  │   └─┐    │
┌───▼────┐  ┌───▼────┐  │ ┌──▼─────┐
│ Ion    │  │ Ion    │  │ │  Ion   │
│ (Rust) │  │ (Rust) │  │ │ (Rust) │
│ Windows│  │ Windows│  │ │ Windows│
└────────┘  └────────┘  │ └────────┘
                        │
                  ┌─────▼──────┐
                  │   Redis    │
                  │  Pub/Sub   │
                  └────────────┘
```

## Implementation Details

### Cobalt (Python)
- FastAPI for HTTP endpoints
- LangChain for LLM integration
- Pydantic for data validation
- Redis/ZeroMQ for IPC with Ion

### Ion (Windows - Rust)
- tauri or egui for GUI
- High-performance rendering
- Windows API access for system integration
- Redis/ZeroMQ client for communication

## Trade-offs

| Option | Pros | Cons |
|--------|------|------|
| Single Language | Simpler tooling | Limited technology choice |
| Multi-Language (Chosen) | Best of both worlds | IPC complexity |

## Next Steps

1. Implement FastAPI endpoints in Python Cobalt
2. Create Rust Ion client library
3. Add message queue for reliability
4. Implement health check/heartbeat mechanism

## References

- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [Rust GUI Documentation](https://github.com/egui-rs/egui)