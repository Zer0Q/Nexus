# Local AI Hardware Index

## Overview
Hardware strategies for local AI: DGX Spark, unified memory architectures, cloud GPU cost recovery, and local inference tradeoffs.

## Core Concepts
- [[DGX-Spark]] -- NVIDIA's consumer-grade AI workstation ($2,999)
- [[DGX-Spark-Specs]] -- technical specifications and capabilities
- [[DGX-OS-Stack]] -- software stack running on DGX Spark
- [[Unified-Memory-Advantage-DGX]] -- shared memory pool for CPU and GPU
- [[Unified-Memory-Tradeoff]] -- capacity vs. bandwidth compromises
- [[Cloud-GPU-Cost-Recovery]] -- payback period analysis for local hardware
- [[Hardware-Reality-of-Local-AI]] -- what consumer hardware can actually run
- [[Local-AI-Mindset-Shift]] -- thinking differently about local vs. cloud AI
- [[Local-AI-Privacy]] -- keeping sensitive data on your machine
- [[Ollama-Local-Serving]] -- local model serving framework
- [[Open-WebUI-Local-Chat]] -- local chat interface for self-hosted models
- [[Memory-Bandwidth-Bottleneck]] -- decode speed tracks bandwidth, not compute
- [[KV-Cache-Growth]] -- memory pressure from long contexts
- [[Prefill-vs-Decode]] -- two inference phases with different resource profiles
- [[Interconnect-Bottleneck]] -- communication cost in multi-GPU setups
- [[Quantization-Format-Portability]] -- format compatibility across engines
- [[Speculative-Decoding]] -- acceleration via draft model
- [[Continuous-Batching]] -- efficient multi-request serving
- [[Disaggregated-Prefill-Decode]] -- splitting inference across GPUs
- [[PagedAttention]] -- efficient KV cache management
- [[Runtime-Overhead]] -- latency costs of local inference
- [[Cloud-Handoff]] -- routing sensitive tasks locally, heavy tasks to cloud
- [[Model-Selection-Tiers]] -- choosing models by hardware capability

## Frameworks
- [[Hardware-First-Engine-Selection]] -- engine follows hardware strategy
- [[Inference-Engine-Families]] -- four categories of inference engines
- [[Benchmarking-Workload-Shape]] -- proper benchmarking methodology
- [[Hybrid-AI-Workflow]] -- mixing local and cloud based on sensitivity

## Tools
- [[LM-Studio]] -- local model runner (Mistral, Llama, DeepSeek)
- [[llama-cpp]] -- most portable inference runtime (GGUF, CPU/GPU hybrid)
- [[vLLM]] -- default open-source production server
- [[SGLang]] -- complex serving (long context, MoE, disaggregation)
- [[TensorRT-LLM]] -- NVIDIA max-performance stack
- [[ExLlamaV2-and-V3]] -- consumer CUDA quant engines
- [[MLX-and-MLX-LM]] -- Apple Silicon native ML stack
- [[BMO-Chatbot]] -- local chat interface in Obsidian

## Glossary
- [[HBM]] -- High Bandwidth Memory
- [[GGUF]] -- GPT-Generated Unified Format
- [[KV-Cache]] -- Key-Value cache for attention
- [[MoE]] -- Mixture of Experts
- [[FP4]] -- 4-bit floating point quantization
- [[LPDDR5x]] -- low-power DDR5 for edge devices
- [[GB10]] -- NVIDIA GPU architecture
- [[ConnectX-7]] -- NVIDIA networking interconnect
- [[NeMo]] -- NVIDIA model optimization framework
- [[NIM]] -- NVIDIA Inference Microservice
- [[Local-LLM]] -- locally-hosted language model
- [[RAG]] -- Retrieval-Augmented Generation
- [[Embeddings]] -- vector representations of text
- [[Nous-Portal]] -- model distribution platform

## Sources
- [[w1nklerr-DGX-Spark-Cost-Recovery]]
