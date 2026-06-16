---
title: How to Run 300 AI Agents From One Prompt. 10 Workflows Most People Skip
author: '@eng_khairallah1'
published: '2026-06-04'
type: article
resource: https://x.com/eng_khairallah1/status/2062461939318730818
timestamp: '2026-06-04T00:00:00Z'
description: 'Guía práctica sobre fan-out de prompts: en vez de procesar items secuencialmente,
  se spawn 100+ workers paralelos desde un solo prompt con un coordinator que...'
tags:
- summaries
---


# 300 AI Agents From One Prompt

## Summary

Guía práctica sobre fan-out de prompts: en vez de procesar items secuencialmente, se spawn 100+ workers paralelos desde un solo prompt con un coordinator que mergea resultados. Compara costos reales: 100 PDFs analizados en $40-60/hora (Opus 4.8 sequential) vs $3-5/12min (Kimi K2.6 parallel). Analiza 3 modelos frontier (Kimi K2.6, Claude Opus 4.8, GPT-5.5) y sus especialidades. Presenta 10 workflows de fan-out que la mayoría skip.

## Core Concepts

- [[concepts/Fan-Out-Pattern]] -- patrón de paralelización donde un single prompt spawn workers paralelos que procesan items independientes y un coordinator mergea resultados
- [[concepts/Kimi-K26]] -- modelo de Moonshot AI nativamente entrenado para coordinar hasta 300 sub-agents: 80.2% SWE-bench Verified, 39% hallucination rate, 8x más barato que Opus 4.8
- [[concepts/Parallelization]] -- ejecución paralela de tareas independientes para speed multiplier (15x) y cost multiplier (10x) vs enfoque secuencial
- [[concepts/Model-Specialization]] -- estrategia de usar diferente modelo para cada tipo de task en vez de sticking a uno solo
- [[concepts/Coordinator-Pattern]] -- patrón de arquitectura donde un agent central orchestrates workers y mergea sus outputs

## Key Insights

- Kimi K2.6: 80.2% SWE-bench Verified, 92.5% DeepSearchQA, 66.7% Terminal-Bench 2.0, 58.6% SWE-bench Pro (tied con GPT-5.5)
- Hallucination rate de K2.6: 39% vs 65% en K2.5 — esencialmente par con Opus 4.8 en 36%
- En testing real: K2.6 overhauled un financial matching engine de 8 años en 13 horas, 12 optimization strategies, 1000+ tool calls, 4000+ lines modified, 185% throughput improvement
- Claude Opus 4.8: xhigh effort tier, 64.3% SWE-bench Pro lead, vision 98.5%
- GPT-5.5: computer use 78.7% OSWorld-Verified, long-context retrieval 74%, web research 90.1% BrowseComp
- "A solo operator with this stack is not competing with other solo operators. They are competing with agencies."
- Los 3 modelos landing en misma semana cada uno con specialty clara — los winners son los que route cada task al right model
- Cost math: 100 PDFs en $40-60/hora (sequential) vs $3-5/12min (parallel) — 15x speed, 10x cost multiplier
- El prompt se mantiene same length mientras el work fans out behind it

## Open Questions
- ¿Qué workflows específicos de fan-out son más útiles para research curation?
- ¿Cómo se maneja error recovery cuando workers fallan en un fan-out?
- ¿Cuándo no usar fan-out (tasks que requieren contexto compartido entre workers)?

## Source
- **Raw note:** [[raw-notes/how-to-run-300-ai-agents-from-one-prompt-10-workflows-most-peopl]]
- **Original URL:** https://x.com/eng_khairallah1/status/2062461939318730818
