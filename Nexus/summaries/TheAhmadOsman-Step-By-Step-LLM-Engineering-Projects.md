---
title: Step-By-Step LLM Engineering Projects (2026 Edition)
author: '@TheAhmadOsman'
published: '2026-05-25'
type: article
resource: https://x.com/TheAhmadOsman/status/2058745340895870985
timestamp: '2026-05-25T00:00:00Z'
description: Roadmap de 34 proyectos prácticos para aprender LLM engineering construyendo
  el stack desde cero. Organizado en 21 parts que van desde tokenizers hasta siste...
tags:
- summaries
---


# Step-By-Step LLM Engineering Projects

## Summary
Roadmap de 34 proyectos prácticos para aprender LLM engineering construyendo el stack desde cero. Organizado en 21 parts que van desde tokenizers hasta sistemas completos: representaciones, atención, Transformer blocks, objetivos de training, decoding, KV cache, long context, MoE, quantization, serving, evaluation, RAG, agents, multimodal, interpretability. El principio central es "Build → Plot → Break → Explain → Ship" — implementar el primitivo, graficar comportamiento, ablatar a propósito, explicar qué cambió, publicar el artefacto.

## Core Concepts
- [[concepts/Tokenization]] -- decisión de cómo el mundo se convierte en símbolos, afecta compresión, multilingual, rare words, code, math, latency y calidad del modelo
- [[concepts/Transformer-Architecture]] -- reemplazó recurrence con attention, permitiendo paralelizar training sobre secuencias
- [[concepts/KV-Cache]] -- almacena past keys/values durante autoregressive inference, diferencia práctica clave entre training e inference
- [[concepts/Multi-Query-Attention]] -- comparte keys y values across query heads para reducir memory bandwidth
- [[concepts/Grouped-Query-Attention]] -- middle ground entre multi-head y multi-query, preserva más calidad mientras mejora eficiencia
- [[concepts/Mixture-of-Experts]] -- modelos sparse que activan subset de expertos por token (DeepSeek-V3: 671B total, 37B activados)
- [[concepts/Speculative-Decoding]] -- modelo draft pequeño propone tokens que modelo grande verifica, acelerando generación
- [[concepts/FlashAttention]] -- reduce reads/writes de high-bandwidth-memory, FlashAttention-3 optimiza para NVIDIA Hopper con FP8
- [[concepts/Scaling-Laws]] -- relaciones power-law entre loss, model size, data size y compute (Kaplan, Chinchilla)
- [[concepts/RLHF]] -- Reinforcement Learning from Human Feedback para razonamiento, GRPO reduce overhead de memoria evitando critic model separado

## Key Insights
- BPE maneja rare words componiéndolas de subword units; SentencePiece hace tokenization trainable directamente desde raw text
- RoPE codifica posición relativa through rotations en embedding space; ALiBi biases attention scores basado en distancia para mejorar length extrapolation
- YaRN muestra que context extension con RoPE es más data/compute-efficient que approaches previos
- Infini-attention introduce mecanismo de memoria compresiva para escalar a longitudes ilimitadas con memoria/computación bounded
- DeepSeek-V2 introdujo Multi-head Latent Attention (MLA), compresión KV low-rank; DeepSeek-V3 lo combinó con sparse MoE scaling
- Mamba introdujo selective state-space models con linear-time sequence scaling; Mamba-2 conectó state-space y attention through duality
- LLaDA entrenó diffusion-style language model desde scratch con masking y denoising, desafiando que language modeling debe ser autoregressive
- FineWeb: 15-trillion-token dataset de Common Crawl con filtering y deduplication; DataComp-LM muestra cómo data curation standardized mejora calidad sustancialmente
- Chinchilla argumentó que muchos large models estaban undertrained — compute-optimal training debe escalar parameters y tokens together
- vLLM introdujo PagedAttention para reducir waste de KV-cache memory; SGLang enfatiza fast structured generation con RadixAttention y prefix caching
- Para cada proyecto: producir 5 artefactos (implementation con tests, notebook reproducible, 3+ plots, failure gallery, short write-up)
- Plan de 12 weeks: Weeks 1-2 (representations+attention), 3-4 (training+objectives), 5-6 (inference systems), 7-8 (long context+MoE+data), 9-10 (post-training+evaluation), 11-12 (capstone)

## Open Questions
- ¿Cómo adaptar este roadmap de 12 weeks para alguien con experiencia en ML pero nuevo en LLMs específicamente?
- ¿Qué proyectos de los 34 son absolutamente necesarios vs opcionales dependiendo del objetivo final (research vs engineering vs product)?

## Source
- **Raw note:** [[raw-notes/step-by-step-llm-engineering-projects-2026-edition]]
- **Original URL:** https://x.com/TheAhmadOsman/status/2058745340895870985
