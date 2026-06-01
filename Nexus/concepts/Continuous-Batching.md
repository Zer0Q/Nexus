# Continuous Batching

## Definition
Scheduler technique that interleaves prefill and decode phases across requests, allowing new requests to enter the batch while others are still decoding.

## Why It Matters
Traditional batching waits for all requests to finish before starting new ones. Continuous batching keeps the accelerator busy, dramatically improving throughput.

## Key Ideas
- Good schedulers decide which requests enter the batch, how prefill/decode share the accelerator, and how to avoid starvation
- Requires PagedAttention or equivalent KV cache management
- Chunked prefill breaks long prompts into smaller chunks to avoid blocking short decodes
- Supporting batching is not the same as production-ready scheduling

## Tradeoffs
- Complex scheduler logic adds runtime overhead
- Fairness vs throughput tradeoff: long prompts can starve short requests

## Related
- [[concepts/PagedAttention]]
- [[concepts/Prefill-vs-Decode]]
- [[concepts/Runtime-Overhead]]

## Source
[[source-notes/TheAhmadOsman-Inference-Engines-and-Local-AI-Hardware]]
