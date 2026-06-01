# Runtime Overhead

## Definition
Small per-token overheads (CUDA graphs, kernel fusion, sampling, tokenizer, HTTP, LoRA switching, structured decoding) that compound at high scale and become significant bottlenecks.

## Why It Matters
At low scale, 2% overheads are invisible. At high scale, they form a union and can dominate latency. Optimization shifts from model compute to system plumbing.

## Key Ideas
- CUDA graphs reduce kernel launch overhead but increase memory usage
- Tokenizer overhead matters at high concurrency (thousands of tokens/sec)
- Structured decoding (JSON schema, grammar constraints) adds per-token cost
- LoRA switching adds weight materialization overhead between requests
- HTTP/API layer overhead becomes non-negligible at 10K+ RPS

## Tradeoffs
- Every optimization adds complexity; the goal is to minimize the union of overheads

## Related
- [[concepts/Continuous-Batching]]
- [[concepts/Prefill-vs-Decode]]

## Source
[[source-notes/TheAhmadOsman-Inference-Engines-and-Local-AI-Hardware]]
