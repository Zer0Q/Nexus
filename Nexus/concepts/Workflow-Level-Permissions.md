---
type: Concept
title: Workflow-Level Permissions
description: Control de acceso a información a nivel de workflow — el sistema sabe
  qué puede usar una tarea antes de empezar a generar respuestas.
tags:
- concepts
timestamp: '2026-06-16T13:58:58Z'
---

# Workflow-Level Permissions

## Definition
Control de acceso a información a nivel de workflow — el sistema sabe qué puede usar una tarea antes de empezar a generar respuestas.

## Why It Matters
Company intelligence se vuelve peligroso cuando cada agent puede ver todo. Marketing agent no necesita private HR details, content agent no necesita client financials. Sin permission boundaries early, o se leak cosas o se neutra el sistema hasta que es inútil.

## Key Ideas
- No es un big brain sin walls — es el brain correcto para el workflow correcto
- Especialmente crítico para agencies y services companies con client context, internal context, prospect context, financial context y strategy context viviendo cerca
- Debe construirse antes de escalar — añadir permissions después es mucho más costoso
- El goal es granularidad: workflow-level, no solo user-level

## Related
- [[concepts/Company-Brain-Architecture]]
- [[concepts/Source-Truth-Hierarchy]]
- [[concepts/Scoped-Vault-Access]]

## Source
[[summaries/EricOsiu-How-we-built-a-Single-Company-Brain]]
