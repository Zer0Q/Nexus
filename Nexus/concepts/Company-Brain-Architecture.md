---
type: Concept
title: Company Brain Architecture
description: 'Sistema de 5 capas que convierte conocimiento disperso (calls, CRM,
  SOPs, Slack) en inteligencia operativa reutilizable: Capture → Retrieval → Source
  Truth →...'
tags:
- concepts
timestamp: '2026-06-16T13:58:58Z'
---

# Company Brain Architecture

## Definition
Sistema de 5 capas que convierte conocimiento disperso (calls, CRM, SOPs, Slack) en inteligencia operativa reutilizable: Capture → Retrieval → Source Truth → Permissions → Feedback Loops.

## Why It Matters
Memoria es el raw material, retrieval es el operating layer. Sin retrieval, más memoria no ayuda — los agents tienen más info pero no la correcta en el momento correcto. En Single Grain: 500K+ tokens de memoria persistente, 90+ daily crons, 2,862 Gong transcripts convertidos en playbooks.

## Key Ideas
- Layer 1 Capture: calls, CRM, content decisions, SOPs, agent outputs, daily logs, human corrections
- Layer 2 Retrieval: el agente necesita los 6 contextos relevantes, no toda la historia de la compañía
- Layer 3 Source Truth: qué fuente gana cuando hay conflictos (sales call vs CRM vs Slack vs SOP)
- Layer 4 Permissions: control de acceso por workflow — marketing no necesita HR, sales no necesita leadership notes
- Layer 5 Feedback Loops: cada corrección humana se convierte en regla futura — inteligencia → aprendizaje
- 15 calls diarios → 390 insights, 470 facts, 125 frameworks
- Un call se convierte en: objection library, sales training, positioning signal, content idea, CRM risk flag, future agent instruction

## Related
- [[concepts/Retrieval-First-Organization]]
- [[concepts/Source-Truth-Hierarchy]]
- [[concepts/Workflow-Level-Permissions]]
- [[concepts/Feedback-Loop-Knowledge-System]]
- [[Capture-Surface-Workflow]] -- needs research: workflow de captura de datos en company brain

## Source
[[summaries/EricOsiu-How-we-built-a-Single-Company-Brain]]
