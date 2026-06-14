---
title: "Cómo crear Loops con Claude"
source: "https://x.com/angeldot_/status/2065145486890164524"
author: "@angeldot_"
published: "2026-06-11"
type: article
---

# Cómo crear Loops con Claude

## Summary

Explicación en español sobre Loop Engineering y el experimento de Anthropic con Fable 5. El artículo compara Fable 5 vs Opus 4.7 en Parameter Golf (entrenar mejor modelo en 16MB en <10min sobre 8 GPUs H100) donde Fable 5 mejoró ~6x más. Analiza las 5 etapas de un loop (DESCUBRIR→PLANIFICAR→EJECUTAR→VERIFICAR→ITERAR), la regla de oro "el que hace no es el que juzga", los 5 niveles de memoria, y la distinción entre loops abiertos y cerrados.

## Core Concepts

- [[concepts/Loop-Engineering]] -- diseño de sistemas donde agentes iteran autónomamente mediante feedback loops verificables en vez de prompts secuenciales
- [[concepts/Fable-5]] -- modelo de Anthropic optimizado para Loop Engineering: superó a Opus 4.7 6x en Parameter Golf y 0.839 vs 0.700 en Continual Learning Bench
- [[concepts/Parameter-Golf]] -- benchmark de Anthropic: entrenar mejor modelo posible en 16MB en <10min sobre 8 GPUs H100
- [[concepts/Continual-Learning-Bench]] -- benchmark de aprendizaje secuencial donde memoria compartida entre sesiones determina performance
- [[concepts/Memory-Levels]] -- 5 niveles de uso de memoria en agentes: fallar→investigar→verificar→destilar→consultar regla
- [[concepts/Maker-Checker-Split]] -- regla de que el que ejecuta no es el que juzga: subagente verificador independiente con su propio contexto
- [[concepts/Open-vs-Closed-Loop]] -- distinción entre loops abiertos (objetivo amplio) y cerrados (condiciones verificables específicas)
- [[concepts/Single-vs-Fleet-Loop]] -- loop individual vs fleet: un agente iterando vs múltiples agentes coordinados

## Key Insights

- "El prompt ha muerto como unidad de trabajo" — lo nuevo es Loop Engineering
- Los loops pasan por 5 etapas: DESCUBRIR → PLANIFICAR → EJECUTAR → VERIFICAR → ITERAR
- La clave es que la verificación sea "verificable" — no "haz una landing bonita" sino "todos los tests de /auth pasan"
- Fable 5 mejoró ~6x más que Opus 4.7 en Parameter Golf porque apostó por cambios estructurales grandes en vez de tocar parámetros
- Opus 4.7 encontró una pequeña mejora y repitió la misma plantilla 20x — Fable 5 aguantó una regresión que fue su mayor victoria
- La regla de oro: "el que hace no es el que juzga" — los modelos son malos criticando su propio trabajo
- Fable 5: 0.839 score en Continual Learning Bench vs Opus 4.7: 0.700 vs Sonnet 4.6: 0.364
- Sonnet 4.6 se queda en nivel 1 (apunta fallos), Opus 4.7 llega al nivel 3 (crea referencias), Fable 5 completa el ciclo (verifica 73% y convierte en reglas)
- "El modelo olvida entre sesiones. El archivo de memoria no." — esa es la diferencia entre agente que empieza de cero y uno que acumula conocimiento
- Los 5 niveles de memoria: 1) fallar y documentarlo, 2) investigar por qué, 3) verificar la causa, 4) destilar en regla general, 5) consultar regla en vez de rederivar
- El verificador de Anthropic no dejó parar a Fable 5 hasta cumplir 9 criterios de la rúbrica
- `/goal` en Claude Code: condición medible + modelo independiente decide si se cumplió
- En Claude Managed Agents: rúbrica con criterios evaluables + subagente que corrige en cada iteración

## Open Questions
- ¿Qué diferencia arquitectónico entre Fable 5 y Opus 4.7 permite mejor loop engineering?
- ¿Cómo se implementan los 5 niveles de memoria en Hermes Agent con skills y cron jobs?
- ¿Cuándo usar loop abierto vs cerrado en práctica con Claude Code?

## Source
- **Raw note:** [[raw-notes/como-crear-loops-con-claude]]
- **Original URL:** https://x.com/angeldot_/status/2065145486890164524
