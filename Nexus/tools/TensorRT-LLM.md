---
type: Tool
title: TensorRT-LLM
description: NVIDIA's maximum-performance inference stack. Optimized, specialized,
  powerful, and not pretending to be portable.
tags:
- tools
timestamp: '2026-06-16T13:58:58Z'
---

# TensorRT-LLM

## Definition
NVIDIA's maximum-performance inference stack. Optimized, specialized, powerful, and not pretending to be portable.

## Why It Matters
Absolute performance on NVIDIA datacenter hardware (H100, B200, GB200). Trade portability for speed.

## Key Ideas
- Custom kernels for attention, GEMMs, MoE
- FP4 on B200, FP8 on H100+ (double performance, half memory vs 16-bit)
- Prefill-decode disaggregation, Wide Expert Parallelism, speculative decoding
- Integrated with NVIDIA Dynamo and Triton Inference Server
- Python and C++ runtimes

## Tradeoffs
- NVIDIA-only (no AMD, Apple, Intel portability)
- Awkward for fast-changing experimental models
- Tuning complexity higher than vLLM/SGLang
- Less features, more performance

## Related
- [[tools/Inference-Engine-Families]]
- [[concepts/Quantization-Format-Portability]]

## Source
[[summaries/TheAhmadOsman-Inference-Engines-and-Local-AI-Hardware]]
