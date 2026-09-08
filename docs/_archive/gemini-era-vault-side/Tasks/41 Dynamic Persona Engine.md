---
status: Done
priority: P0
module: Brain
phase: 4
complexity: M
tags: [cobalt, task, split-brain]
created: 2026-02-26
---
# 41 Dynamic Persona Engine

## Objective
Refactor `prompt.py` and `persona.py` to allow Cortex to inject dynamic, highly restricted `.clinerules`-style personas into the Worker agents (e.g., stripping trading rules from the Engineering drone).

## Acceptance Criteria
- [ ] PromptEngine accepts dynamic persona overrides.
- [ ] The Forge initializes with a strictly limited "Mindless Drone" persona.