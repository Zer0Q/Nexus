# Local AI Index

## Overview
This index maps the concepts, tools, and workflows related to running AI models locally for privacy and data sovereignty.

## Core Concepts
- [[concepts/Local-AI-Privacy]] -- keeping sensitive thinking on your machine
- [[concepts/On-Device-Knowledge-Base]] -- all processing happens locally
- [[concepts/Local-LLM-API-Compatibility]] -- OpenAI-compatible local endpoints
- [[concepts/RAG-Retrieval-Augmented-Generation]] -- grounded answers from your content
- [[concepts/Embedding-Based-Vault-Search]] -- semantic search without cloud
- [[concepts/Hardware-Reality-of-Local-AI]] -- consumer hardware is sufficient
- [[concepts/Three-Mode-AI-Workflow]] -- deep work, research, confidential
- [[concepts/Memory-Bandwidth-Bottleneck]] -- decode speed tracks bandwidth, not compute
- [[concepts/KV-Cache-Growth]] -- KV cache grows with batch size and context
- [[concepts/Prefill-vs-Decode]] -- two phases with different resource profiles
- [[concepts/Unified-Memory-Tradeoff]] -- capacity superpower with bandwidth tradeoffs
- [[concepts/Interconnect-Bottleneck]] -- communication cost dominates multi-GPU
- [[concepts/Quantization-Format-Portability]] -- formats are engine-specific

## Frameworks
- [[tools/Hybrid-AI-Workflow]] -- mixing local and cloud based on sensitivity
- [[tools/Hardware-First-Engine-Selection]] -- engine follows hardware strategy
- [[tools/Inference-Engine-Families]] -- four engine categories
- [[tools/Benchmarking-Workload-Shape]] -- proper benchmarking methodology

## Tools
- [[tools/LM-Studio]] -- local model runner (Mistral, Llama, DeepSeek)
- [[tools/llama-cpp]] -- most portable inference runtime (GGUF, CPU/GPU hybrid)
- [[tools/Smart-Connections-Plugin]] -- vault search with local embeddings
- [[tools/BMO-Chatbot]] -- local chat interface in Obsidian
- [[tools/Copilot-Plugin]] -- inline AI assistant in Obsidian
- [[tools/ExLlamaV2-and-V3]] -- consumer CUDA quant engines
- [[tools/vLLM]] -- default open-source production server
- [[tools/SGLang]] -- complex serving (long context, MoE, disaggregation)
- [[tools/TensorRT-LLM]] -- NVIDIA max-performance stack
- [[tools/MLX-and-MLX-LM]] -- Apple Silicon native ML stack

## Hardware
- Apple Silicon M1/M2/M3: 7B-13B models
- 16GB RAM: 7B models
- 32GB RAM + GPU: 13B-34B models
- RTX 3090/4090/5090: ExLlamaV2 for local, vLLM for serving
- H100/H200: vLLM or SGLang, TensorRT-LLM for max performance

## Glossary
- [[concepts/Local-LLM]]
- [[concepts/RAG]]
- [[concepts/Embeddings]]
- [[concepts/KV-Cache]]
- [[concepts/MoE]]
- [[concepts/HBM]]
- [[concepts/GGUF]]

## Sources
- [[summaries/KanikaBK-Offline-AI-Workflow]]
- [[summaries/TheAhmadOsman-Inference-Engines-and-Local-AI-Hardware]]
