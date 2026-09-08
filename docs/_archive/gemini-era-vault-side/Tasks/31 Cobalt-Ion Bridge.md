---
status: To Do
priority: P0 (Critical)
module: Core
phase: 4 (Ion HUD)
complexity: M
tags: [cobalt, task, network]
created: 2026-02-11
---

# 31 Cobalt-Ion Bridge

## Objective
Create the low-latency communication link between **Cobalt (Mac)** and **Ion (Windows)**.

## Requirements
* [ ] Implement **ZeroMQ (ZMQ)** PUB/SUB pattern.
* [ ] **Publisher:** Cobalt (Mac) broadcasting strategy signals.
* [ ] **Subscriber:** Ion (Windows) listening for HUD updates.
* [ ] Define the JSON payload schema (Ticker, Action, Confidence, Price).
* [ ] Secure the connection over **Tailscale IP**.

## Technical Notes
* Latency target: < 50ms.
* Use `zmq.asyncio` for non-blocking I/O.
