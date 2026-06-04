# NVFP4

NVIDIA 4-bit floating point quantization format for model inference. Reduces numerical precision from BF16 to 4-bit FP, achieving up to 2x inference speedup with acceptable quality degradation. Used in Cosmos 3 NIM microservices.

- 4-bit floating point (not integer)
- 2x inference speedup vs BF16
- Supported in NVIDIA NIM microservices
- Tradeoff: speed vs precision

See also: [[concepts/Physical-AI]], [[tools/NVIDIA-Cosmos]]
