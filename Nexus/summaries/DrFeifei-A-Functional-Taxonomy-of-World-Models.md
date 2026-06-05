---
title: "A Functional Taxonomy of World Models"
source: "https://x.com/drfeifei/status/2062247238143996275"
author: "@drfeifei"
published: "2026-06-03"
type: article
---

# A Functional Taxonomy of World Models

## Summary
Propuesta de taxonomía funcional para los "world models" en AI, clasificándolos en tres funciones según qué parte del loop POMDP (agent-action-state-observation) producen: Renderers (output observaciones/píxeles, fidelidad visual), Simulators (output estado, precisión geométrica/física) y Planners (output acciones, cierra el loop percepción-acción). La simulación es el puente entre render y plan — el conocimiento subyacente (geometría, física, dinámica) es el mismo para los tres. Las fronteras se están colapsando hacia un world model unificado.

## Core Concepts
- [[concepts/World-Models]] -- modelos que aprenden la estructura estadística de espacio y tiempo, no solo texto
- [[concepts/World-Model-Renderer]] -- produce observaciones visuales (píxeles) con alta fidelidad visual pero sin comprensión 3D explícita
- [[concepts/World-Model-Simulator]] -- produce estado geométrico/físico fiel, usado para training de robots, arquitectura, digital twins
- [[concepts/World-Model-Planner]] -- produce acciones dadas observación + goal, cierra el loop percepción-acción
- [[concepts/POMDP]] -- Partially Observable Markov Decision Process, marco formal donde los world models tienen su significado técnico
- [[concepts/Sim-to-Real-Gap]] -- diferencia entre comportamiento en simulación vs realidad, problema abierto en robótica
- [[concepts/Gaussian-Splats]] -- representación 3D para exploración visual, output de World Labs Marble junto con collision meshes
- [[concepts/Action-Conditioned-World-Model]] -- world model que genera frames condicionados a input del usuario en tiempo real

## Key Insights
- El término "world model" viene de Kenneth Craik (1943) — "small-scale models" de la realidad — llevado a redes neuronales en los 80s-90s
- Los renderers son los más maduros comercialmente (Google Nano Banana, Genie 3, RTFM) pero no pueden usarse para diseñar edificios o entrenar robots
- Los planners son los más intrigantes pero más inmaduros — demos recientes están confinados a setups de laboratorio con objetos limitados y horizontes cortos
- La simulación es el linchpin: NVIDIA Omniverse apunta a más de $1 billón en factories, warehouses, supply chains y digital twins
- World Labs Marble genera Gaussian splats (visual) + collision meshes (physics) desde prompts multimodales (text, image, video, spatial sketch)
- Los datos 3D con geometría explícita, propiedades de materiales y anotaciones físicas son órdenes de magnitud más escasos que video de internet
- Generative simulators introducen nuevo riesgo: geometría generada por AI puede verse correcta pero contener self-intersections o escala errónea
- La convergencia ya está en marcha: tres hilos que antes eran programas de investigación separados comienzan a comportarse como uno

## Open Questions
- ¿Cómo resolver el tradeoff entre optimizar para belleza visual vs precisión física dentro de una arquitectura unificada?
- ¿Qué cantidad y tipo de datos 3D se necesitan para entrenar simulators comparado con los renderers que usan video de internet?

## Source
- **Raw note:** [[raw-notes/a-functional-taxonomy-of-world-models]]
- **Original URL:** https://x.com/drfeifei/status/2062247238143996275
