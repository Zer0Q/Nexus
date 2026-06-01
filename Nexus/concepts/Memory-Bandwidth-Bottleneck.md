# Memory Bandwidth Bottleneck

## Definition
LLM decode speed is limited by memory bandwidth (how fast weights and KV cache can be read), not by raw compute throughput.

## Why It Matters
Explains why a machine with more VRAM can be slower than one with less VRAM but higher bandwidth. Fit is not speed. Capacity is not bandwidth.

## Key Ideas
- Decode phase repeatedly reads weights + KV cache per token → memory-bound
- Prefill phase computes attention over the full prompt → compute-bound
- Apple unified memory: high capacity (819 GB/s on M3 Ultra), low bandwidth vs HBM (3.35 TB/s on H100 SXM)
- HBM lets you serve faster when the model fits; unified memory lets you fit models that would not fit in consumer VRAM

## Tradeoffs
- Unified memory enables larger models on consumer hardware at the cost of slower decode
- HBM gives speed but requires expensive datacenter GPUs

## Related
- [[concepts/Prefill-vs-Decode]]
- [[concepts/Unified-Memory-Tradeoff]]
- [[concepts/KV-Cache-Growth]]

## Source
[[source-notes/TheAhmadOsman-Inference-Engines-and-Local-AI-Hardware]]
