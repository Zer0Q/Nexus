# Local AI Index

## Overview
This index maps the concepts, tools, and workflows related to running AI models locally for privacy and data sovereignty.

## Core Concepts
- [[Local-AI-Privacy]] -- keeping sensitive thinking on your machine
- [[On-Device-Knowledge-Base]] -- all processing happens locally
- [[Local-LLM-API-Compatibility]] -- OpenAI-compatible local endpoints
- [[RAG-Retrieval-Augmented-Generation]] -- grounded answers from your content
- [[Embedding-Based-Vault-Search]] -- semantic search without cloud
- [[Hardware-Reality-of-Local-AI]] -- consumer hardware is sufficient
- [[Three-Mode-AI-Workflow]] -- deep work, research, confidential
- [[Memory-Bandwidth-Bottleneck]] -- decode speed tracks bandwidth, not compute
- [[KV-Cache-Growth]] -- KV cache grows with batch size and context
- [[Prefill-vs-Decode]] -- two phases with different resource profiles
- [[Unified-Memory-Tradeoff]] -- capacity superpower with bandwidth tradeoffs
- [[Interconnect-Bottleneck]] -- communication cost dominates multi-GPU
- [[Quantization-Format-Portability]] -- formats are engine-specific

## Frameworks
- [[Hybrid-AI-Workflow]] -- mixing local and cloud based on sensitivity
- [[Hardware-First-Engine-Selection]] -- engine follows hardware strategy
- [[Inference-Engine-Families]] -- four engine categories
- [[Benchmarking-Workload-Shape]] -- proper benchmarking methodology

## Tools
- [[LM-Studio]] -- local model runner (Mistral, Llama, DeepSeek)
- [[llama-cpp]] -- most portable inference runtime (GGUF, CPU/GPU hybrid)
- [[Smart-Connections-Plugin]] -- vault search with local embeddings
- [[BMO-Chatbot]] -- local chat interface in Obsidian
- [[Copilot-Plugin]] -- inline AI assistant in Obsidian
- [[ExLlamaV2-and-V3]] -- consumer CUDA quant engines
- [[vLLM]] -- default open-source production server
- [[SGLang]] -- complex serving (long context, MoE, disaggregation)
- [[TensorRT-LLM]] -- NVIDIA max-performance stack
- [[MLX-and-MLX-LM]] -- Apple Silicon native ML stack

## Hardware
- Apple Silicon M1/M2/M3: 7B-13B models
- 16GB RAM: 7B models
- 32GB RAM + GPU: 13B-34B models
- RTX 3090/4090/5090: ExLlamaV2 for local, vLLM for serving
- H100/H200: vLLM or SGLang, TensorRT-LLM for max performance

## Glossary
- [[Local-LLM]]
- [[RAG]]
- [[Embeddings]]
- [[KV-Cache]]
- [[MoE]]
- [[HBM]]
- [[GGUF]]

## Sources
- [[KanikaBK-Offline-AI-Workflow]]
- [[TheAhmadOsman-Inference-Engines-and-Local-AI-Hardware]]
