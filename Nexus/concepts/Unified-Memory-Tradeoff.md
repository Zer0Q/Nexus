---
type: Concept
title: Unified Memory Tradeoff
description: Apple Silicon's unified memory architecture gives CPU and GPU shared
  access to the same memory pool, enabling larger model capacity at the cost of lower
  band...
tags:
- concepts
timestamp: '2026-06-16T13:58:58Z'
---

# Unified Memory Tradeoff

## Definition
Apple Silicon's unified memory architecture gives CPU and GPU shared access to the same memory pool, enabling larger model capacity at the cost of lower bandwidth than discrete GPU HBM.

## Why It Matters
Changes the local inference equation: instead of "does it fit in VRAM?" the question becomes "does it fit in memory, and can the memory system feed the GPU fast enough?"

## Key Ideas
- M3 Ultra: up to 819 GB/s unified memory bandwidth vs 3.35 TB/s on H100 SXM
- Large quantized models fit on Macs where they would be impossible on 24 GB consumer GPUs
- MLX arrays live in unified memory, no copy between CPU/GPU memory spaces
- Unified memory is a capacity superpower with bandwidth tradeoffs, not HBM replacement

## Tradeoffs
- Fit large models but decode slower than equivalent HBM systems
- Best for local/development use, not high-concurrency serving

## Related
- [[concepts/Memory-Bandwidth-Bottleneck]]
- [[tools/MLX-and-MLX-LM]]
- [[tools/llama-cpp]]

## Source
[[summaries/TheAhmadOsman-Inference-Engines-and-Local-AI-Hardware]]
