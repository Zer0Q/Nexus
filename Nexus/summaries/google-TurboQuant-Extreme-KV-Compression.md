---
title: 'TurboQuant: Redefining AI efficiency with extreme compression'
author: Amir Zandieh, Vahab Mirrokni (Google Research)
published: '2026-03-24'
type: article
resource: https://research.google/blog/turboquant-redefining-ai-efficiency-with-extreme-compression/
timestamp: '2026-03-24T00:00:00Z'
description: Google Research introduces TurboQuant, a two-stage quantization algorithm
  combining PolarQuant (random rotation + polar coordinate quantization) with QJL
  (Qu...
tags:
- summaries
---


# TurboQuant: Extreme KV Cache Compression

## Summary
Google Research introduces TurboQuant, a two-stage quantization algorithm combining PolarQuant (random rotation + polar coordinate quantization) with QJL (Quantized Johnson-Lindenstrauss, a 1-bit error-correction step) to achieve 3-bit KV cache compression with zero accuracy loss. TurboQuant eliminates the memory overhead that plagues traditional vector quantization (which adds 1-2 extra bits per number for quantization constants), achieving up to 8x speedup over 32-bit unquantized keys on H100 GPUs while maintaining optimal dot product distortion and recall rates.

## Core Concepts
- [[concepts/TurboQuant]] -- two-stage compression: PolarQuant for high-quality main compression + QJL for 1-bit residual error elimination, achieving 3-bit KV cache with zero accuracy loss
- [[concepts/PolarQuant]] -- converts vectors to polar coordinates (radius + angle), eliminating the need for data normalization and removing memory overhead from quantization constants; presented at AISTATS 2026
- [[concepts/QJL]] -- Quantized Johnson-Lindenstrauss, reduces each vector number to a single sign bit (+1/-1) with zero memory overhead, acts as mathematical error-checker eliminating bias in attention scores; presented at AAAI 2026
- KV-Cache-Compression -- reducing the size of key-value pairs in the transformer cache to lower memory costs and enable faster attention computation
- [[concepts/Vector-Quantization]] -- classical data compression technique that reduces high-dimensional vector size, used for both vector search and KV cache optimization
- Johnson-Lindenstrauss-Transform -- mathematical technique that shrinks high-dimensional data while preserving essential distances and relationships between data points

## Key Insights
- Traditional vector quantization introduces memory overhead (1-2 extra bits per number for quantization constants), partially defeating the compression purpose
- TurboQuant quantizes KV cache to just 3 bits without requiring training or fine-tuning and causing zero accuracy compromise
- 4-bit TurboQuant achieves up to 8x performance increase over 32-bit unquantized keys on H100 GPUs
- Evaluated on LongBench, Needle In A Haystack, ZeroSCROLLS, RULER, and L-Eval benchmarks using Gemma and Mistral models
- TurboQuant achieves optimal 1@k recall ratio on GloVe dataset (d=200) compared to PQ and RabbiQ baselines, despite those baselines using large codebooks and dataset-specific tuning
- PolarQuant's recursive polar transformation: pairs of coordinates are mapped to polar, radii are gathered in pairs for recursive transformation, distilling to a single final radius + collection of angles
- QJL's special estimator balances high-precision queries with low-precision simplified data for accurate attention score calculation
- All three techniques are provably efficient and operate near theoretical lower bounds, not just empirical improvements

## Open Questions
- How does [[concepts/TurboQuant]] interact with existing [[concepts/KV-Cache]] optimization techniques like PagedAttention and Grouped-Query-Attention?
- Can the polar coordinate approach in [[concepts/PolarQuant]] be extended beyond KV cache to weight quantization for full model compression?

## Source
- **Raw note:** [[raw-notes/turboquant-redefining-ai-efficiency-with-extreme-compression]]
- **Original URL:** https://research.google/blog/turboquant-redefining-ai-efficiency-with-extreme-compression/
