---
type: Tool
title: ExLlamaV2 and V3
description: Consumer CUDA quantization engines optimized for RTX 3090/4090/5090.
  V2 for single-GPU local inference, V3 for multi-GPU (2-4) and MoE.
tags:
- tools
timestamp: '2026-06-16T13:58:58Z'
---

# ExLlamaV2 and V3

## Definition
Consumer CUDA quantization engines optimized for RTX 3090/4090/5090. V2 for single-GPU local inference, V3 for multi-GPU (2-4) and MoE.

## Why It Matters
Best performance per dollar for enthusiast local setups. Makes quantized models fast on consumer NVIDIA hardware.

## Key Ideas
- **V2:** paged attention, dynamic batching, prompt caching, KV dedup, speculative decoding, EXL2 format
- **V3:** EXL3 format (QTIP-based), tensor-parallel and expert-parallel inference, continuous dynamic batching, multimodal
- Best fits: local coding assistant, local chat, prosumer workstation
- Not designed for production serving or fleet orchestration

## Tradeoffs
- V3 has rougher edges and not all models support tensor/expert parallelism
- CUDA-only, no Apple/AMD portability

## Related
- [[tools/Inference-Engine-Families]]
- [[concepts/Quantization-Format-Portability]]

## Source
[[summaries/TheAhmadOsman-Inference-Engines-and-Local-AI-Hardware]]
