---
type: Concept
title: Scaling Laws
description: Relaciones power-law que cuantifican cómo el loss cambia con model size,
  data size y compute — prediciendo el rendimiento de modelos antes de entrenarlos.
  Co...
tags:
- concepts
timestamp: '2026-06-16T13:58:58Z'
---

# Scaling Laws

## Definition
Relaciones power-law que cuantifican cómo el loss cambia con model size, data size y compute — prediciendo el rendimiento de modelos antes de entrenarlos. Con compute finito: L_C(N) ~ N^(-0.34). Con datos infinitos: L_inf(N) ~ N^(-0.46). La diferencia de exponentes implica que modelos grandes alcanzan loss asintótico mejor incluso con training infinito.

## Why It Matters
Permite planificar training runs: cuánto compute se necesita para alcanzar un target de loss. Chinchilla argumentó que muchos large models estaban undertrained — compute-optimal training debe escalar parameters y tokens together más cuidadosamente. El paper de Stanford/Harvard/MIT/Anthropic (2026) muestra que scaling laws ocultan una discontinuidad: modelos pequeños no alcanzan ciertas regiones de la distribución ni con datos infinitos.

## Key Ideas
- Kaplan-style scaling laws: smooth power-law relationships across several orders of magnitude
- Chinchilla: muchos models estaban undertrained — scale parameters y tokens together
- Train tiny, small y medium models y fit scaling curves es el proyecto para entenderlo
- Scaling laws aplican a pretraining — post-training (SFT, DPO, RLHF) tiene dynamics diferentes
- L_C(N) ~ N^(-0.34) vs L_inf(N) ~ N^(-0.46): el exponente mayor con datos infinitos significa que modelos grandes tienen un "floor" de loss inalcanzable para modelos pequeños
- Los beneficios de scaling son stepwise, no suaves: un modelo justo debajo del umbral de capacidad se comporta diferente en inputs raros

## Related
- [[concepts/Transformer-Architecture]]
- [[concepts/Structural-Exclusion]]
- [[concepts/Utility-Ranking-Theorem]]

## Source
[[summaries/TheAhmadOsman-Step-By-Step-LLM-Engineering-Projects]]
[[summaries/AlphaSignalAI-Smaller-Models-Structurally-Excluded]]
