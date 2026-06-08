# TurboQuant

## Definition
Two-stage quantization algorithm combining PolarQuant (random rotation + polar coordinate quantization) with QJL (Quantized Johnson-Lindenstrauss, 1-bit error correction) to achieve 3-bit KV cache compression with zero accuracy loss.

## Why It Matters
Eliminates the memory overhead that plagues traditional vector quantization (1-2 extra bits per number for quantization constants), achieving up to 8x speedup over 32-bit unquantized keys on H100 GPUs while maintaining optimal dot product distortion and recall rates.

## Key Ideas
- Stage 1: PolarQuant — random rotation + polar coordinate quantization captures main vector structure
- Stage 2: QJL — 1-bit residual error elimination removes bias from attention scores
- No training or fine-tuning required; works out of the box with existing models
- Evaluated on LongBench, Needle In A Haystack, ZeroSCROLLS, RULER, L-Eval
- Optimal 1@k recall ratio on GloVe dataset vs. PQ and RabbiQ baselines
- Provably efficient, operates near theoretical lower bounds

## Tradeoffs
- Primarily designed for KV cache compression and vector search; not a general weight quantization method
- Requires random rotation step which adds computational overhead during encoding
- Speedup benefits are most pronounced on high-dimensional vectors (d >> 100)

## Related
- [[concepts/PolarQuant]]
- [[concepts/QJL]]
- [[concepts/KV-Cache]]
- [[concepts/Vector-Quantization]]

## Source
[[summaries/google-TurboQuant-Extreme-KV-Compression]]
