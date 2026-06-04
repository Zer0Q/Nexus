# Mixture of Transformers

## Definition
An architecture that combines multiple transformer specializations within a single model, allowing different components to handle different modalities or tasks while sharing representations. Cosmos 3 uses MoT with two towers: a reasoner (autoregressive VLM) and a generator (diffusion-based).

## Why It Matters
MoT unifies capabilities that previously required separate models and orchestration pipelines. A single model can reason about the world and then generate actions or video, reducing complexity and inference overhead from multi-model coordination.

## Key Ideas
- Reasoner tower: autoregressive VLM that interprets multimodal observations (text, image, video, audio)
- Generator tower: diffusion-based process for physics-aware video and action outputs
- Information flows unidirectionally from reasoner to generator for guided generation
- Reasoner can be called independently; generator always activates both towers
- Eliminates orchestration between multiple models and inference pipelines

## Tradeoffs
- Larger total parameter count vs specialized single-purpose models
- Training complexity -- coordinating multiple tower specializations
- Inference overhead when both towers are active vs calling reasoner alone

## Related
- [[concepts/Physical-AI]]
- [[concepts/World-Models]]
- [[tools/NVIDIA-Cosmos]]

## Source
[[summaries/NVIDIA-Cosmos-3-Physical-AI]]
