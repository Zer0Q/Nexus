---
type: Concept
title: GGUF
description: '- Supports multiple quantization levels (Q4_K_M, Q5_K_S, Q8_0, etc.)
  - Portable across backends (CPU, CUDA, Metal, Vulkan, HIP) - Not always the fastest
  form...'
tags:
- concepts
timestamp: '2026-06-16T13:58:58Z'
---

# GGUF

General GPU Format -- open quantization format optimized for llama.cpp. Industry standard for portable local models.

- Supports multiple quantization levels (Q4_K_M, Q5_K_S, Q8_0, etc.)
- Portable across backends (CPU, CUDA, Metal, Vulkan, HIP)
- Not always the fastest format for a given engine

See also: [[concepts/Quantization-Format-Portability]], [[tools/llama-cpp]]
