---
type: Concept
title: World Model Planner
description: 'Tipo de world model que produce acciones: dado una observación y un
  goal, responde qué debe hacer el agente a continuación. Cierra el loop percepción-acción.'
tags:
- concepts
timestamp: '2026-06-16T13:58:58Z'
---

# World Model Planner

## Definition
Tipo de world model que produce acciones: dado una observación y un goal, responde qué debe hacer el agente a continuación. Cierra el loop percepción-acción.

## Why It Matters
Es la categoría más intrigante y más inmadura. Conectada al campo de robotic learning. Un robot que puede planificar es un robot que puede trabajar — toda la industria compite por llegar primero. Pero la brecha entre demos de laboratorio y robots que trabajan fiablemente en cocinas, warehouses o quirófanos sigue siendo vasta.

## Key Ideas
- Output: acciones (qué hacer a continuación)
- Inverso del renderer: toma observaciones como input y produce acciones
- Vision-Language-Action models, model-based systems, World Action Models son intentos de planners
- Demos recientes están confinados a setups de laboratorio con object sets estrechos y task horizons cortos
- Ningún demo ha sido validado a la complejidad, variabilidad o duración que deployment real demanda

## Tradeoffs
- Más inmaduro comercialmente que renderers o simulators
- Requiere datos de robot demonstrations que son escasos
- La brecha demo-to-production es enorme

## Related
- [[concepts/World-Model-Renderer]]
- [[concepts/World-Model-Simulator]]
- [[concepts/World-Models]]
- [[concepts/Physical-AI]]

## Source
[[summaries/DrFeifei-A-Functional-Taxonomy-of-World-Models]]
