# KV Cache

Key-value cache storing intermediate attention states for every token in the context window. Grows linearly with batch size and context length. Often the dominant memory consumer at scale.

- Partitioned by PagedAttention into fixed-size blocks
- Can be quantized or offloaded to system memory
- Prefix caching reuses blocks for shared prompt prefixes

See also: [[KV-Cache-Growth]], [[PagedAttention]], [[Prefill-vs-Decode]]
