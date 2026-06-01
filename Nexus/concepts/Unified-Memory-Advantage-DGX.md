# Unified Memory Advantage DGX

## Definition
The DGX Spark's 128GB LPDDR5x unified memory shared between CPU and GPU, enabling it to load models up to 200B parameters — sizes that physically won't fit in the 24-32GB VRAM of top consumer GPUs like the RTX 4090 or 5090.

## Why It Matters
Memory capacity is the hard ceiling for local model size. When a model is fatter than your VRAM, CUDA throws an out-of-memory error and the model simply won't load. The DGX Spark's 128GB removes this ceiling for most practical use cases.

## Key Ideas
- RTX 4090: 24GB VRAM, RTX 5090: 32GB VRAM — both cap out around 30B squeezed models
- DGX Spark: 128GB unified memory — loads 70B at full BF16 precision, stretches to 200B quantized
- Two units linked over ConnectX-7: 405B parameters on your desk
- Memory is shared between CPU and GPU — no copy overhead between memory spaces
- The spec that actually changes your life, not the petaflop rating

## Tradeoffs
- LPDDR5x bandwidth (~819 GB/s) lower than HBM on data-center GPUs
- Raw decode speed trails a 5090 on models that fit in its 32GB VRAM
- Not suitable for high-concurrency serving of thousands of users

## Related
- [[concepts/DGX-Spark-Specs]] -- detailed hardware specs
- [[concepts/Unified-Memory-Tradeoff]] -- Apple Silicon's similar approach (different hardware context)
- [[concepts/Memory-Bandwidth-Bottleneck]] -- the bandwidth tradeoff behind unified memory
- [[concepts/Hardware-Reality-of-Local-AI]] -- broader hardware comparison

## Source
[[source-notes/w1nklerr-DGX-Spark-Cost-Recovery]]
