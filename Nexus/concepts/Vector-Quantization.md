---
type: Concept
title: Vector Quantization
description: Classical data compression technique that reduces the size of high-dimensional
  vectors by mapping continuous values to a smaller discrete set of symbols, use...
tags:
- concepts
timestamp: '2026-06-16T13:58:58Z'
---

# Vector Quantization

## Definition
Classical data compression technique that reduces the size of high-dimensional vectors by mapping continuous values to a smaller discrete set of symbols, used for both vector search and KV cache optimization in AI systems.

## Why It Matters
High-dimensional vectors (embeddings, KV cache entries) consume vast amounts of memory. Vector quantization addresses two critical bottlenecks: (1) faster similarity lookups in vector search engines, and (2) reduced KV cache size enabling faster attention computation and lower memory costs.

## Key Ideas
- Maps continuous values to discrete codes from a codebook
- Traditional methods require storing full-precision quantization constants per block (1-2 extra bits overhead)
- Modern approaches (TurboQuant, PolarQuant) eliminate this overhead through mathematical tricks
- Applications: KV cache compression, vector search index building, embedding storage
- Evaluated via dot product distortion and recall@k metrics

## Tradeoffs
- Compression ratio vs. accuracy tradeoff: higher compression = more distortion
- Codebook size affects both memory usage and reconstruction quality
- Traditional methods need dataset-specific tuning; newer methods (TurboQuant) are data-oblivious

## Related
- [[concepts/TurboQuant]]
- [[concepts/PolarQuant]]
- [[concepts/QJL]]
- [[concepts/KV-Cache]]

## Source
[[summaries/google-TurboQuant-Extreme-KV-Compression]]
