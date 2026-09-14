---
status: To Do
priority: P1 (High)
module: Ops
phase: 5 (Ops)
complexity: M
tags: [cobalt, task, chat]
created: 2026-02-11
---

# 33 Mattermost C2 Integration

## Objective
Connect Cobalt to the "Red Phone" (Mattermost) for remote command and control.

## Requirements
* [ ] Create a Mattermost Bot Account ("Cobalt").
* [ ] Implement **Incoming Webhooks** for alerts (Trade Signals).
* [ ] Implement **Outgoing Webhooks** (or Slash Commands) for user commands.
* [ ] **Kill Switch:** Create a command `/cobalt stop` that halts all trading instantly.
* [ ] **Approval Flow:** Interactive buttons for "Approve Trade?" messages.
