---
type: Concept
title: Structural Exclusion
description: Fenómeno donde modelos pequeños no pueden aprender ciertas regiones de
  la distribución de datos, incluso con entrenamiento infinito. No es una brecha de
  efic...
tags:
- concepts
timestamp: '2026-06-16T13:58:58Z'
---

# Structural Exclusion

## Definition
Fenómeno donde modelos pequeños no pueden aprender ciertas regiones de la distribución de datos, incluso con entrenamiento infinito. No es una brecha de eficiencia de muestreo sino una limitación fundamental: hay partes de la distribución estructuralmente inaccesibles para modelos por debajo de un umbral de capacidad.

## Why It Matters
Desafía la intuición estándar de que "más datos compensan menos parámetros". Si la tarea que importa es rara en la distribución de training, el tamaño del modelo no es un dial de rendimiento sino un prerequisito. Más tiempo de training no cambia la matemática.

## Key Ideas
- Paper de Stanford/Harvard/MIT/Anthropic (2026) demuestra el fenómeno teórica y empíricamente
- L_C(N) ~ N^(-0.34) vs L_inf(N) ~ N^(-0.46): la diferencia de exponentes implica exclusion estructural
- Los beneficios de scaling son stepwise: un modelo justo debajo del umbral y uno justo encima se ven idénticos en benchmarks promedio pero se comportan diferente en inputs raros
- Post-training fine-tuning puede a veces recuperar tareas que pretraining no aprendió, pero no está garantizado
- Implicación práctica: el sizing de modelos se convierte de pregunta empírica a problema de razonamiento analítico

## Related
- [[concepts/Scaling-Laws]]
- [[concepts/Utility-Ranking-Theorem]]
- [[concepts/Update-and-Forget-Loop]]

## Source
[[summaries/AlphaSignalAI-Smaller-Models-Structurally-Excluded]]
