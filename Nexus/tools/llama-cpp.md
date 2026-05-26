# llama.cpp

## Definition
The most portable LLM inference runtime. Runs on Apple Silicon, x86, RISC-V, CUDA, AMD HIP, Vulkan, SYCL, CPU+GPU hybrid offload. Written in C/C++.

## Why It Matters
Owning the "just make it run" lane. When hardware is weird, constrained, offline, or edge-oriented, llama.cpp is the default answer.

## Key Ideas
- Supports GGUF quantization format (industry standard for portable local models)
- llama-server provides OpenAI-compatible routes, Anthropic Messages API, continuous batching, multimodal, JSON schema constraints, function calling, speculative decoding
- CPU+GPU hybrid offload: run parts of the model on CPU, parts on GPU
- NOT designed for multi-node production serving (RPC backend is proof-of-concept, fragile, insecure)

## Tradeoffs
- Portability comes at the cost of peak performance on any single platform
- Multi-GPU support is weak; use vLLM or ExLlamaV2 instead

## Related
- [[Inference-Engine-Families]]
- [[Unified-Memory-Tradeoff]]
- [[Quantization-Format-Portability]]

## Source
[[TheAhmadOsman-Inference-Engines-and-Local-AI-Hardware]]
