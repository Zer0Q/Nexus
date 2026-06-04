# LLM Inference and Hardware Index

## Overview
How LLMs work internally, how to run them efficiently, and the hardware that powers local AI.

## Core Concepts
- [[concepts/PagedAttention]] -- vLLM's memory-efficient attention implementation
- [[concepts/Continuous-Batching]] -- processing multiple requests simultaneously
- [[concepts/Prefill-vs-Decode]] -- two phases of LLM inference
- [[concepts/Speculative-Decoding]] -- faster generation with draft models
- [[concepts/Binary-Embeddings]] -- 32x memory reduction for RAG vectors
- [[concepts/Quantization-Format-Portability]] -- running large models on limited hardware
- [[concepts/Memory-Bandwidth-Bottleneck]] -- GPU memory bandwidth limits
- [[concepts/KV-Cache-Growth]] -- managing cache size in long conversations

## Hardware
- [[concepts/Unified-Memory-Advantage-DGX]] -- DGX Spark unified memory benefits
- [[concepts/Interconnect-Bottleneck]] -- GPU-to-GPU communication limits

## Tools
- [[tools/vLLM]] -- high-throughput serving engine
- [[tools/SGLang]] -- structured language model serving
- [[tools/TensorRT-LLM]] -- NVIDIA inference optimization
- [[tools/LM-Studio]] -- local model serving GUI
- [[tools/llama-cpp]] -- C++ GGUF inference

## Glossary
- [[concepts/KV-Cache]]
- [[concepts/GGUF]]
- [[concepts/MoE]]
- [[concepts/FP4]]
- [[concepts/HBM]]
- [[concepts/NIM]]

## Sources
- [[summaries/RoyvanRijn-anatomy-llm-interactive-visual-language-models-work]]
- [[summaries/TheAhmadOsman-llms-101-practical-2026-edition]]
- [[summaries/avichawla-make-rag-32x-memory-efficient-explained-code]]
- [[summaries/w1nklerr-DGX-Spark-Cost-Recovery]]
