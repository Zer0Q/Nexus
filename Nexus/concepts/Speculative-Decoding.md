# Speculative Decoding

## Definition
Technique that drafts tokens using a small/fast model, then verifies them in parallel using the large target model, reducing decode latency.

## Why It Matters
Decode is memory-bandwidth-bound and generates one token at a time. Speculative decoding amortizes the cost by verifying multiple tokens per forward pass.

## Key Ideas
- Draft model (small, fast) proposes N tokens
- Target model verifies all N tokens in one forward pass
- Speedup depends on draft acceptance rate (typically 60-90%)
- Implemented in llama.cpp, ExLlamaV2, vLLM, SGLang, TensorRT-LLM
- Works best when draft model captures the target model's distribution well

## Tradeoffs
- Adds memory for the draft model
- Speedup diminishes if acceptance rate is low
- Not effective for highly creative/divergent outputs

## Related
- [[Prefill-vs-Decode]]
- [[Memory-Bandwidth-Bottleneck]]

## Source
[[TheAhmadOsman-Inference-Engines-and-Local-AI-Hardware]]
