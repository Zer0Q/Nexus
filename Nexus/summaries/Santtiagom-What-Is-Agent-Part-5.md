---
title: Post by @santtiagom_ on X
author: '@santtiagom_'
published: '2026-06-14'
type: article
resource: https://x.com/santtiagom_/status/2067369367783081485
timestamp: '2026-06-14T00:00:00Z'
description: '@santtiagom_ explica los guardrails de seguridad para agentes AI: sandboxing,
  validación de output, límites de tokens, límites de scope y human-in-the-loop. ...'
tags:
- summaries
---


# Agent Guardrails and Safety

## Summary
@santtiagom_ explica los guardrails de seguridad para agentes AI: sandboxing, validación de output, límites de tokens, límites de scope y human-in-the-loop. Más autonomía requiere más guardrails para evitar caos costoso.

## Core Concepts
- [[concepts/Agent-Guardrails]] -- Conjunto de mecanismos de seguridad: sandboxing, validación de output, límites de tokens y scope
-  -- Aislar la ejecución del agente para prevenir daño al sistema o datos
-  -- Verificar que la salida del agente cumple con reglas antes de aplicarla
-  -- Límites de tokens para controlar costos y prevenir loops infinitos
-  -- Intervención humana para decisiones críticas o cuando el agente sale de scope
- [[concepts/Agent-Architecture]] -- Diseño que balancea autonomía con seguridad

## Key Insights
- Los guardrails no son estrictamente "anatomía" del agente pero son cruciales
- Más autonomía = más necesidad de guardrails
- Sandbox: aislar ejecución para prevenir daño al sistema
- Output validation: verificar resultados antes de aplicarlos al mundo real
- Token limits: prevenir loops infinitos y controlar costos
- Scope limits: definir claramente qué el agente puede y no puede hacer
- Human-in-the-loop: intervención humana para decisiones críticas

## Open Questions
- ¿Cómo se implementan los guardrails en Claude Code vs Hermes Agent?
- ¿Qué mecanismos de sandboxing son más efectivos para agentes de código?
- ¿Cuándo es apropiado reducir los guardrails para mayor autonomía?

## Source
- **Raw note:** [[raw-notes/santtiagom-what-is-an-agent-part-5]]
- **Original URL:** https://x.com/santtiagom_/status/2067369367783081485
