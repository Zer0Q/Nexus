---
title: "Inference Engines for LLMs & Local AI Hardware (2026 Edition)"
source: "https://x.com/TheAhmadOsman/status/2057183854444843202"
author: "@TheAhmadOsman"
published: 2026-05-20
type: article
---

# Inference Engines for LLMs and Local AI Hardware

## Summary
Comprehensive guide to LLM inference engines, arguing you pick hardware strategy and workload shape first, then the engine follows. Covers four engine families (portable, Apple, consumer CUDA, production), real bottlenecks (memory bandwidth, KV cache, interconnect, scheduler), benchmarking methodology, and hardware-specific recipes.

## Core Concepts
- [[concepts/Memory-Bandwidth-Bottleneck]] -- decode speed tracks bandwidth, not compute
- [[concepts/KV-Cache-Growth]] -- KV cache grows with batch size and context length
- [[concepts/Prefill-vs-Decode]] -- two phases with different resource profiles
- [[concepts/PagedAttention]] -- KV cache memory management via block partitioning
- [[concepts/Continuous-Batching]] -- scheduler quality determines throughput
- [[concepts/Disaggregated-Prefill-Decode]] -- separating compute and memory phases
- [[concepts/Interconnect-Bottleneck]] -- communication cost dominates multi-GPU
- [[concepts/Quantization-Format-Portability]] -- formats are engine-specific, not interchangeable
- [[concepts/Speculative-Decoding]] -- draft cheap tokens, verify in parallel
- [[concepts/Unified-Memory-Tradeoff]] -- capacity superpower with bandwidth tradeoffs
- [[frameworks/Hardware-First-Engine-Selection]] -- engine follows hardware strategy, not vice versa
- [[frameworks/Benchmarking-Workload-Shape]] -- proper benchmarking requires full context

## Key Insights
- Inference performance is memory movement plus scheduling, not raw compute
- VRAM determines fit, bandwidth determines speed -- they are not the same
- Without NVLink, pipeline parallelism can outperform tensor parallelism
- PagedAttention, prefix caching, KV quantization are not optional at scale
- Small runtime overheads (tokenizer, HTTP, sampling) compound at high scale
- The right quantization format is the one your engine has optimized kernels for
- Never benchmark with single-user tokens per second alone

## Open Questions
- How do SGLang and vLLM compare on real-world MoE workloads?
- Does disaggregated prefill/decode become standard or remain niche?
- Will Ollama evolve beyond local convenience?
- How does Thunderbolt RDMA compare to NVLink for Apple multi-node?
