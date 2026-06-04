# LPDDR5x

Low-Power Double Data Rate 5x memory, the type used in the DGX Spark's 128GB unified memory pool. Offers higher capacity than consumer GPU VRAM (24-32GB) at the cost of lower bandwidth than HBM found on data-center GPUs.

- Used in DGX Spark: 128GB unified across CPU + GPU
- Bandwidth: ~819 GB/s (vs 3.35 TB/s on H100 SXM)
- Enables loading 70B-200B parameter models on desktop hardware
- Tradeoff: capacity superpower, bandwidth compromise

See also: [[concepts/Unified-Memory-Advantage-DGX]], [[concepts/HBM]], [[concepts/Memory-Bandwidth-Bottleneck]]
