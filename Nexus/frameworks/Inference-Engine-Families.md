# Inference Engine Families

## Definition
LLM inference engines fall into four broad families: portable local runtimes, Apple/unified-memory runtimes, consumer CUDA quant engines, and production serving engines.

## Why It Matters
Each family optimizes for a different axis. Picking from the wrong family is the most common mistake in local AI setups.

## Key Ideas
- **Portable:** llama.cpp, MLC LLM, ONNX Runtime GenAI, OpenVINO -- "make it run here"
- **Apple:** MLX, MLX-LM -- "use big shared memory and Apple's stack well"
- **Consumer CUDA:** ExLlamaV2/V3 -- "make my RTX box scream with low-bit weights"
- **Production:** vLLM, SGLang, TensorRT-LLM -- concurrent users, KV cache, batching, observability
- **Orchestration:** NVIDIA Dynamo -- sits above engines, coordinates fleets

## Related
- [[Hardware-First-Engine-Selection]]
- [[llama-cpp]]
- [[vLLM]]

## Source
[[TheAhmadOsman-Inference-Engines-and-Local-AI-Hardware]]
