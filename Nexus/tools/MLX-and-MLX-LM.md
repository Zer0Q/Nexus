# MLX and MLX-LM

## Definition
Apple's array framework (MLX) and LLM package (MLX-LM) for Apple Silicon. A Mac-first ML stack that leverages unified memory.

## Why It Matters
Enables large quantized models on Macs where they would be impossible on 24 GB consumer GPUs. Unified memory changes the local inference tradeoff.

## Key Ideas
- MLX arrays live in unified memory, no CPU/GPU memory copy
- Hugging Face Hub integration, quantization, LoRA and full fine-tuning
- Distributed inference via MPI, Ring over TCP, JACCL (RDMA over Thunderbolt), NCCL
- CUDA and CPU-only packages available for Linux
- Server explicitly warns: not recommended for production

## Tradeoffs
- Slower decode than equivalent HBM systems
- Server lacks production security, observability, autoscaling

## Related
- [[Unified-Memory-Tradeoff]]
- [[Inference-Engine-Families]]

## Source
[[TheAhmadOsman-Inference-Engines-and-Local-AI-Hardware]]
