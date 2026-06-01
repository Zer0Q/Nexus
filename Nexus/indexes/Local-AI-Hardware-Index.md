# Local AI Hardware Index

## Overview
Hardware strategies for local AI: DGX Spark, unified memory architectures, cloud GPU cost recovery, and local inference tradeoffs.

## Core Concepts
- [[concepts/DGX-Spark]] -- NVIDIA's consumer-grade AI workstation ($2,999)
- [[concepts/DGX-Spark-Specs]] -- technical specifications and capabilities
- [[concepts/DGX-OS-Stack]] -- software stack running on DGX Spark
- [[concepts/Unified-Memory-Advantage-DGX]] -- shared memory pool for CPU and GPU
- [[concepts/Unified-Memory-Tradeoff]] -- capacity vs. bandwidth compromises
- [[concepts/Cloud-GPU-Cost-Recovery]] -- payback period analysis for local hardware
- [[concepts/Hardware-Reality-of-Local-AI]] -- what consumer hardware can actually run
- [[concepts/Local-AI-Mindset-Shift]] -- thinking differently about local vs. cloud AI
- [[concepts/Local-AI-Privacy]] -- keeping sensitive data on your machine
- [[concepts/Ollama-Local-Serving]] -- local model serving framework
- [[concepts/Open-WebUI-Local-Chat]] -- local chat interface for self-hosted models
- [[concepts/Memory-Bandwidth-Bottleneck]] -- decode speed tracks bandwidth, not compute
- [[concepts/KV-Cache-Growth]] -- memory pressure from long contexts
- [[concepts/Prefill-vs-Decode]] -- two inference phases with different resource profiles
- [[concepts/Interconnect-Bottleneck]] -- communication cost in multi-GPU setups
- [[concepts/Quantization-Format-Portability]] -- format compatibility across engines
- [[concepts/Speculative-Decoding]] -- acceleration via draft model
- [[concepts/Continuous-Batching]] -- efficient multi-request serving
- [[concepts/Disaggregated-Prefill-Decode]] -- splitting inference across GPUs
- [[concepts/PagedAttention]] -- efficient KV cache management
- [[concepts/Runtime-Overhead]] -- latency costs of local inference
- [[concepts/Cloud-Handoff]] -- routing sensitive tasks locally, heavy tasks to cloud
- [[concepts/Model-Selection-Tiers]] -- choosing models by hardware capability

## Frameworks
- [[frameworks/Hardware-First-Engine-Selection]] -- engine follows hardware strategy
- [[frameworks/Inference-Engine-Families]] -- four categories of inference engines
- [[frameworks/Benchmarking-Workload-Shape]] -- proper benchmarking methodology
- [[frameworks/Hybrid-AI-Workflow]] -- mixing local and cloud based on sensitivity

## Tools
- [[tools/LM-Studio]] -- local model runner (Mistral, Llama, DeepSeek)
- [[tools/llama-cpp]] -- most portable inference runtime (GGUF, CPU/GPU hybrid)
- [[tools/vLLM]] -- default open-source production server
- [[tools/SGLang]] -- complex serving (long context, MoE, disaggregation)
- [[tools/TensorRT-LLM]] -- NVIDIA max-performance stack
- [[tools/ExLlamaV2-and-V3]] -- consumer CUDA quant engines
- [[tools/MLX-and-MLX-LM]] -- Apple Silicon native ML stack
- [[tools/BMO-Chatbot]] -- local chat interface in Obsidian

## Glossary
- [[glossary/HBM]] -- High Bandwidth Memory
- [[glossary/GGUF]] -- GPT-Generated Unified Format
- [[glossary/KV-Cache]] -- Key-Value cache for attention
- [[glossary/MoE]] -- Mixture of Experts
- [[glossary/FP4]] -- 4-bit floating point quantization
- [[glossary/LPDDR5x]] -- low-power DDR5 for edge devices
- [[glossary/GB10]] -- NVIDIA GPU architecture
- [[glossary/ConnectX-7]] -- NVIDIA networking interconnect
- [[glossary/NeMo]] -- NVIDIA model optimization framework
- [[glossary/NIM]] -- NVIDIA Inference Microservice
- [[glossary/Local-LLM]] -- locally-hosted language model
- [[glossary/RAG]] -- Retrieval-Augmented Generation
- [[glossary/Embeddings]] -- vector representations of text
- [[glossary/Nous-Portal]] -- model distribution platform

## Sources
- [[source-notes/w1nklerr-DGX-Spark-Cost-Recovery]]
