---
type: Concept
title: World Model Renderer
description: Tipo de world model que produce observaciones visuales (píxeles) optimizadas
  para fidelidad visual, no para comprensión estructural 3D.
tags:
- concepts
timestamp: '2026-06-16T13:58:58Z'
---

# World Model Renderer

## Definition
Tipo de world model que produce observaciones visuales (píxeles) optimizadas para fidelidad visual, no para comprensión estructural 3D.

## Why It Matters
Es la categoría más madura comercialmente — text-to-video, image generation — pero tiene un techo: outputs visualmente perfectos que no pueden usarse para diseñar edificios o entrenar robots porque carecen de precisión física.

## Key Ideas
- Output: frames/píxeles condicionados a prompts de texto o user input
- Métrica principal: visual fidelity, no accuracy física
- Ejemplos: Google Genie 3, RTFM, Nano Banana
- No lleva comprensión explícita de estructura 3D — los edificios pueden verse perfectos desde arriba pero colapsar al intentar navegar por ellos
- Se está volviendo action-conditioned: renderers que generan frames en tiempo real condicionados a input del usuario

## Tradeoffs
- Visual plausibility vs physical accuracy — optimizar para uno sacrifica el otro
- No puede ser usado como training ground para robots o simulación de ingeniería

## Related
- [[concepts/World-Model-Simulator]]
- [[concepts/World-Model-Planner]]
- [[concepts/World-Models]]

## Source
[[summaries/DrFeifei-A-Functional-Taxonomy-of-World-Models]]
