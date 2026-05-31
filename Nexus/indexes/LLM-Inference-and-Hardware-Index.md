# LLM Inference and Hardware Index

## Overview
How LLMs work internally, how to run them efficiently, and the hardware that powers local AI.

## Core Concepts
- [[PagedAttention]] -- vLLM's memory-efficient attention implementation
- [[Continuous-Batching]] -- processing multiple requests simultaneously
- [[Prefill-vs-Decode]] -- two phases of LLM inference
- [[Speculative-Decoding]] -- faster generation with draft models
- [[Binary-Embeddings]] -- 32x memory reduction for RAG vectors
- [[Quantization-Format-Portability]] -- running large models on limited hardware
- [[Memory-Bandwidth-Bottleneck]] -- GPU memory bandwidth limits
- [[KV-Cache-Growth]] -- managing cache size in long conversations

## Hardware
- [[Unified-Memory-Advantage-DGX]] -- DGX Spark unified memory benefits
- [[Interconnect-Bottleneck]] -- GPU-to-GPU communication limits

## Tools
- [[vLLM]] -- high-throughput serving engine
- [[SGLang]] -- structured language model serving
- [[TensorRT-LLM]] -- NVIDIA inference optimization
- [[LM-Studio]] -- local model serving GUI
- [[llama-cpp]] -- C++ GGUF inference

## Glossary
- [[KV-Cache]]
- [[GGUF]]
- [[MoE]]
- [[FP4]]
- [[HBM]]
- [[NIM]]

## Sources
- [[RoyvanRijn-anatomy-llm-interactive-visual-language-models-work]]
- [[TheAhmadOsman-llms-101-practical-2026-edition]]
- [[avichawla-make-rag-32x-memory-efficient-explained-code]]
- [[w1nklerr-DGX-Spark-Cost-Recovery]]
