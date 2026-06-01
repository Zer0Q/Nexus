# PagedAttention

## Definition
Memory management technique that partitions the KV cache into fixed-size blocks (pages), reducing fragmentation and enabling larger batch sizes.

## Why It Matters
KV cache fragmentation was the #1 cause of wasted GPU memory. PagedAttention increases utilization from ~40% to ~90%, directly enabling higher throughput.

## Key Ideas
- Inspired by virtual memory paging in OS
- KV cache stored in non-contiguous blocks, managed by a page table
- Enables continuous batching by freeing blocks when requests complete
- Implemented in vLLM, SGLang (RadixAttention variant), ExLlamaV2
- Prefix caching extends the idea: reuse KV blocks for shared prompt prefixes

## Tradeoffs
- Page table management adds small overhead
- Block size tuning matters: too small = overhead, too large = fragmentation

## Related
- [[concepts/KV-Cache-Growth]]
- [[concepts/Continuous-Batching]]
- [[concepts/Prefill-vs-Decode]]

## Source
[[source-notes/TheAhmadOsman-Inference-Engines-and-Local-AI-Hardware]]
