---
type: Concept
title: World Model Simulator
description: 'Tipo de world model que produce estado: representación geométrica, física
  o dinámicamente fiel del mundo que humanos y programas pueden computar e interactua...'
tags:
- concepts
timestamp: '2026-06-16T13:58:58Z'
---

# World Model Simulator

## Definition
Tipo de world model que produce estado: representación geométrica, física o dinámicamente fiel del mundo que humanos y programas pueden computar e interactuar con.

## Why It Matters
Es el linchpin entre renderers y planners. Domina simulación y puede proyectar su entendimiento tanto hacia píxeles (para humanos) como hacia predicciones de acción (para agentes encarnados). NVIDIA Omniverse apunta a más de $1 billón en factories, warehouses, supply chains y digital twins.

## Key Ideas
- Output: estado geométrico/físico, no píxeles
- Contrato estructural: geometría que resiste inspección, física que respeta leyes de Newton
- Dos consumidores: profesionales humanos (arquitectos, diseñadores) y programas (RL agents, robot controllers, autonomous vehicles)
- Datos 3D con geometría explícita, propiedades de materiales y anotaciones físicas son órdenes de magnitud más escasos que video de internet
- Generative simulators introducen riesgo: geometría AI-generated puede verse correcta pero contener self-intersections o escala errónea que producen física nonsensical
- Multi-physics simulation at scale (rigid bodies, deformable objects, fluids, cloth) sigue siendo órdenes de magnitud más caro que single-domain simulation

## Tradeoffs
- Sim-to-real gap persiste: diferencia entre comportamiento en simulación vs realidad
- Costo computacional: multi-physics simulation es enormemente más caro
- Data scarcity: datos 3D anotados son escasos comparado con video de internet

## Related
- [[concepts/World-Model-Renderer]]
- [[concepts/World-Model-Planner]]
- [[concepts/World-Models]]
- [[concepts/Sim-to-Real-Gap]]
- [[concepts/Gaussian-Splats]]

## Source
[[summaries/DrFeifei-A-Functional-Taxonomy-of-World-Models]]
