# KV Cache Growth

## Definition
The KV (key-value) cache stores intermediate attention states for every token in the context window. It grows linearly with batch size × context length and is often the real memory bottleneck.

## Why It Matters
Long-context workloads can run out of memory even when model weights fit. KV cache can exceed weight memory at high concurrency.

## Key Ideas
- Each new token adds to the KV cache for every request in the batch
- At scale, KV cache dominates GPU memory usage over model weights
- Mitigations: PagedAttention (block partitioning), prefix caching, KV quantization, offload
- PagedAttention partitions KV cache into blocks, increasing utilization and supporting larger batches

## Tradeoffs
- KV quantization saves memory but may degrade quality on very long contexts
- Offloading KV cache to system memory adds latency

## Related
- [[concepts/Memory-Bandwidth-Bottleneck]]
- [[concepts/PagedAttention]]
- [[concepts/Prefill-vs-Decode]]

## Source
[[source-notes/TheAhmadOsman-Inference-Engines-and-Local-AI-Hardware]]
