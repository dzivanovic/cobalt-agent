# ADR-012: Drone Polymorphism & Unified ReAct

## Status
Accepted

## Context
With the introduction of the Split-Brain Orchestrator (ADR-007), the system hardcoded "The Forge" (Engineering) as the sole execution agent. To scale across multiple domains (Ops, Tactical, Intel), the Orchestrator needs to dynamically instantiate specialized Drones. Furthermore, duplicating the ReAct execution loop across multiple department classes violates DRY principles and creates maintenance debt.

## Decision
1. **Unified ReAct Engine**: We extracted the ReAct while-loop, JSON parsing, and Proposal fast-exit logic into a single `BaseDepartment` abstract class.
2. **Drone Polymorphism**: All specialized departments (`EngineeringDepartment`, `OpsDepartment`) now inherit from `BaseDepartment`. They only provide their name and default system prompts.
3. **Orchestrator Routing**: The Orchestrator will be updated to assign tasks to specific Drones based on their required capabilities.

## Consequences
- **Positive**: Bug fixes to the execution loop instantly propagate to all Drones.
- **Positive**: Creating a new Department now takes less than 20 lines of code.
- **Negative**: The Base Class becomes a critical point of failure; regressions here will break all execution capabilities.