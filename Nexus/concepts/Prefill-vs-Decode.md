---
type: Concept
title: Prefill vs Decode
description: 'LLM inference has two distinct phases: **prefill** (read prompt, build
  initial KV cache, compute-intensive) and **decode** (generate one token at a time,
  mem...'
tags:
- concepts
timestamp: '2026-06-16T13:58:58Z'
---

# Prefill vs Decode

## Definition
LLM inference has two distinct phases: **prefill** (read prompt, build initial KV cache, compute-intensive) and **decode** (generate one token at a time, memory-bandwidth-bound).

## Why It Matters
The dominant phase determines which hardware and engine optimizations matter. Short prompt + long answer = decode dominates. Long prompt + short answer = prefill dominates.

## Key Ideas
- Prefill: attention kernels and chunked prefill matter most
- Decode: memory bandwidth and batching matter most
- Many users: scheduler quality (continuous batching, cache paging) matters
- Long context: KV cache management dominates
- MoE: expert routing and interconnect dominate
- Multi-node: interconnect dominates

## Tradeoffs
- Optimizing for prefill can hurt decode throughput and vice versa
- Disaggregated architectures separate the two phases into specialized instances

## Related
- [[concepts/Memory-Bandwidth-Bottleneck]]
- [[concepts/KV-Cache-Growth]]
- [[concepts/Disaggregated-Prefill-Decode]]

## Source
[[summaries/TheAhmadOsman-Inference-Engines-and-Local-AI-Hardware]]
