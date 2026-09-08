---
title: "ADR-001 Hybrid Compute Strategy"
status: **OBSOLETE** 
priority: P0
module: [Architecture]
phase: 1
complexity: M
tags: [cobalt, architecture, documentation, adr, deprecated]
created: 2026-02-23
deprecated: 2026-03-07
superseded_by: ADR-014 Unified MoE Architecture
---

# ADR-001: Hybrid Compute Strategy (DEPRECATED)

## Status: OBSOLETE — Superseded by ADR-014

## Deprecation Notice

This ADR has been **deprecated** as of 2026-03-07. The parallel dense model architecture (Dayshift/Nightshift using Ollama with Qwen 8B + DeepSeek 70B) has been **abandoned** in favor of a single Qwen 3.5 122B MoE model running locally via MLX/LM Studio.

See **ADR-014: Unified MoE Architecture** for the current compute strategy.

## Why We Abandoned This Architecture

1. **VRAM Inefficiency**: Loading/unloading two separate dense model weights caused memory thrashing on Apple Silicon
2. **Context Limitations**: 128K context was insufficient for complex multi-step reasoning tasks
3. **Model Quality**: Dense models struggled with nuanced technical documentation and code generation
4. **Ollama Limitations**: Limited control over memory management and model quantization

## Migration to Unified MoE (Summary)

The new architecture uses a **single Qwen 3.5 122B MoE** model that:
- Runs locally via MLX/LM Studio with full VRAM control
- Leverages 122B parameter MoE architecture for superior reasoning
- Supports 256K+ context windows for complex tasks
- Eliminates model-switching overhead (single "hot" model in memory)

**Key Technical Achievement**: Bypassed Apple's 86GB VRAM limit via custom kernel override, enabling full model load on M3 Ultra.

## Original Decision (Historical Reference)

We previously implemented a **Hybrid Compute Strategy** with two distinct LLM paths:

### Dayshift (Fast Path) — ABANDONED
- **Model**: Local 8B + Qwen 3 Coder (via Ollama)
- **Use Cases**: Chat interactions, tool routing, simple queries

### Nightshift (Deep Reasoning Path) — ABANDONED
- **Model**: DeepSeek 70B (via Ollama)
- **Use Cases**: Strategy backtesting, complex analysis

## References

- [ADR-014 Unified MoE Architecture](./ADR-014%20Unified%20MoE%20Architecture.md) — Current strategy
- [Qwen 3.5 Documentation](https://qwenlm.github.io/blog/qwen2.5-coder/)
- [MLX Framework](https://ml-explore.github.io/mlx/)