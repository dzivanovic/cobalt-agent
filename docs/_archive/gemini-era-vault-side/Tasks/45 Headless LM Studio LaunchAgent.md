---
status: To Do
priority: P1
module: Services
phase: 4
complexity: M
tags: [cobalt, task, llm, launchagent]
created: 2026-03-07
---
# 45 Headless LM Studio LaunchAgent

## Objective
Create a macOS LaunchAgent to automatically manage the headless LM Studio LLM server lifecycle, ensuring local-first AI capability without manual intervention.

## Description
Implement a system-level LaunchAgent that monitors and maintains the LM Studio server process. This enables Cobalt to operate fully offline with local LLM inference, aligned with the Local-First Architecture (PRD-009).

## Tasks
- [ ] Create LaunchAgent plist at `~/Library/LaunchAgents/com.cobalt.lmstudio.plist`
- [ ] Write launch agent script to start/monitor LM Studio server
- [ ] Implement automatic restart on process failure
- [ ] Add logging to `~/Library/Logs/cobalt/lmstudio.log`
- [ ] Create CLI commands to start/stop/status the agent

## Success Criteria
- LM Studio server auto-starts on login
- Process monitored with automatic recovery
- No manual intervention required for normal operation