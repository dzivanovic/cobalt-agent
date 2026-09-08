---
title: "ADR-010 Sovereign Split-Brain Architecture"
status: **OBSOLETE** 
priority: P0
module: [Architecture]
phase: 4
complexity: M
tags: [cobalt, architecture, documentation, adr, multi-agent, deprecated]
created: 2026-02-26
deprecated: 2026-03-07
superseded_by: ADR-014 Unified MoE Architecture
---

# ADR-010: Sovereign Split-Brain Architecture (DEPRECATED)

## Status: OBSOLETE — Superseded by ADR-014

## Deprecation Notice

This ADR has been **deprecated** as of 2026-03-07. The parallel dense model architecture (using separate models for Architect and Drone roles via Ollama) has been **abandoned** in favor of a single Qwen 3.5 122B MoE model running locally via MLX/LM Studio with sequential persona swapping.

See **ADR-014: Unified MoE Architecture** for the current split-brain implementation.

## Why We Abandoned This Architecture

1. **Model Quality Gap**: Dense models (DeepSeek 70B, Qwen 80B) lacked the reasoning depth required for complex engineering tasks
2. **Context Window Limitations**: 128K context was insufficient for multi-step reasoning with extensive tool chains
3. **VRAM Management**: Ollama's memory management was suboptimal for Apple Silicon's unified memory architecture
4. **MoE Advantage**: The 122B MoE architecture provides superior reasoning with efficient active parameter utilization

## Migration to Unified MoE (Summary)

The new architecture retains the split-brain pattern but uses a **single Qwen 3.5 122B MoE** model that:
- Runs locally via MLX/LM Studio with full VRAM control
- Maintains sequential persona swapping (Architect → Drone) with a single "hot" model
- Leverages 256K+ context windows for complex multi-step tasks
- **Key Technical Achievement**: Bypassed Apple's 86GB VRAM limit via custom kernel override

## Original Decision (Historical Reference)

We previously implemented a Hierarchical Manager-Worker architecture using **Single-Model Sequential Persona Swapping**, utilizing our local model for both roles.

### Context (Historical)
As tasks become complex, the LLM hallucinates tool syntax because its context window is bloated with system instructions, directory arrays, and planning logic. We need an Architect to plan, and a Drone to execute.

### Technical Rationale (Historical)
Running two massive models (e.g., DeepSeek-R1 and Qwen 80B) in parallel causes VRAM thrashing on Apple Silicon (loading and unloading weights). By utilizing the *same* model for both roles, the core weights stay "hot" in memory. Python simply maintains two separate KV Caches (Conversation Histories) and injects different System Prompts (Personas) sequentially.

### Future Extension (High Throughput) — ABANDONED
While the initial implementation will be a synchronous state machine, this architecture paves the way for advanced local throughput techniques:
1. **Speculative Decoding**: Accelerating the Manager's planning phase using a tiny draft model.
2. **Nginx Clustering**: Spinning up multiple `llama-server` instances to allow the Manager to execute parallel Fan-Out tasks to multiple Drones simultaneously without bottlenecking.

### Consequences (Historical)
* **Positive**: Massive reduction in LLM confusion and syntax errors. Zero loss of local privacy. No VRAM thrashing. Lays the groundwork for future async clustering.
* **Negative**: Increased latency per total task completion in the short term, as Python must wait for the Architect to finish generating the plan before the Drone can start typing code.

## References

- [ADR-014 Unified MoE Architecture](./ADR-014%20Unified%20MoE%20Architecture.md) — Current strategy
- [Qwen 3.5 Documentation](https://qwenlm.github.io/blog/qwen2.5-coder/)
- [MLX Framework](https://ml-explore.github.io/mlx/)