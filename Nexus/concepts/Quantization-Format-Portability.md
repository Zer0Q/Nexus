---
type: Concept
title: Quantization Format Portability
description: Quantization formats (GGUF, EXL2, EXL3, AWQ, GPTQ, FP8, FP4, MLX, ONNX)
  are engine-specific and not interchangeable. The right format is the one your target
  ...
tags:
- concepts
timestamp: '2026-06-16T13:58:58Z'
---

# Quantization Format Portability

## Definition
Quantization formats (GGUF, EXL2, EXL3, AWQ, GPTQ, FP8, FP4, MLX, ONNX) are engine-specific and not interchangeable. The right format is the one your target engine has optimized kernels for.

## Why It Matters
Using the wrong quantization format can degrade performance by 2-5x even if the model loads. Portability and performance are often mutually exclusive.

## Key Ideas
- GGUF: optimized for llama.cpp, portable across backends
- EXL2/EXL3: optimized for ExLlamaV2/V3, consumer CUDA
- FP8/FP4: optimized for TensorRT-LLM on H100/B200
- AWQ/GPTQ: widely supported but not always the fastest
- MLX format: Apple Silicon native
- ONNX: cross-platform but adds conversion overhead

## Tradeoffs
- Portable formats (GGUF) sacrifice peak performance
- Engine-optimized formats (FP4 on TensorRT) sacrifice portability

## Related
- [[concepts/Memory-Bandwidth-Bottleneck]]
- [[tools/llama-cpp]]
- [[tools/TensorRT-LLM]]

## Source
[[summaries/TheAhmadOsman-Inference-Engines-and-Local-AI-Hardware]]
