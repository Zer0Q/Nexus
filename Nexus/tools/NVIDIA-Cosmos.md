# NVIDIA Cosmos

## Definition
NVIDIA's frontier foundation model for physical AI. Cosmos 3 unifies physical reasoning, world generation, and action generation in a single Mixture-of-Transformers architecture. Available in Nano (16B, workstation GPUs) and Super (64B, datacenter GPUs) variants.

## Why It Matters
Cosmos 3 is the first open-source model to combine reasoning, generation, and action in one architecture for physical AI. It leads on multiple benchmarks (VANTAGE-Bench, PAI-Bench, R-Bench, Physics-IQ, RoboLab) and ships with open training scripts, datasets, and NIM deployment.

## Key Ideas
- Two-tower MoT: autoregressive reasoner (VLM) + diffusion generator
- Supports multiple modalities: text, image, video, audio, action inputs/outputs
- Deployable via NIM microservices with BF16, FP8, or NVFP4 quantization
- Built on vLLM serving stack with continuous batching and paged attention
- Efficient Video Sampling (EVS) reduces video tokens for faster inference
- Open post-training scripts for domain adaptation (SFT, action post-training)

## Tradeoffs
- Nano vs Super: efficiency vs quality tradeoff
- NIM deployment (easier inference) vs GitHub repo (post-training workflows)
- Quantization speedup (NVFP4: 2x) vs precision loss

## Related
- [[concepts/Physical-AI]]
- [[concepts/World-Models]]
- [[concepts/Mixture-of-Transformers]]

## Source
[[summaries/NVIDIA-Cosmos-3-Physical-AI]]
