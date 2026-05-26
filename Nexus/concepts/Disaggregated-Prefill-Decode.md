# Disaggregated Prefill Decode

## Definition
Architecture pattern that separates compute-intensive prefill from memory-intensive decode into specialized instances, transferring KV cache between them.

## Why It Matters
Prevents long prefill batches from interrupting decode, reducing token latency spikes and improving overall system stability.

## Key Ideas
- Prefill instances are compute-optimized (more FLOPs, less memory)
- Decode instances are memory-optimized (more bandwidth, less compute)
- KV cache is transferred between instances after prefill completes
- Implemented in vLLM and SGLang
- Particularly effective for workloads with mixed prompt lengths

## Tradeoffs
- KV cache transfer adds communication overhead
- Adds operational complexity (two instance types to manage)
- Not beneficial for workloads with uniformly short prompts

## Related
- [[Prefill-vs-Decode]]
- [[KV-Cache-Growth]]
- [[SGLang]]

## Source
[[TheAhmadOsman-Inference-Engines-and-Local-AI-Hardware]]
