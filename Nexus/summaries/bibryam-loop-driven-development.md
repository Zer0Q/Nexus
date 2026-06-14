---
title: "Loop-Driven Development: The Next Layer of AI Coding"
source: "https://x.com/bibryam/status/2065445933601435823"
author: "@bibryam"
published: "2026-06-12"
type: article
---

# Loop-Driven Development

## Summary

Evolución de AI-assisted coding en 5 fases: autocomplete → prompting → context engineering → harness engineering → loop engineering. La tesis central: no es sobre "AI" sino sobre "verify" — sin verificación, no tienes un loop, tienes repeated prompting. El engineer deja de escribir código para diseñar el sistema que permite al agent trabajar safely. La unidad de trabajo se amplía: line → function → test → task → PR → migration → recurring workflow.

## Core Concepts

- [[concepts/Loop-Driven-Development]] -- evolución del test-driven development donde la unidad de trabajo es el loop completo (intent→run→verify→repair→repeat) en vez de solo tests
- [[concepts/Harness-Engineering]] -- diseño del environment alrededor de un agent run: prompts, tools, sandbox, permissions, tests, linters, CI, evals, review gates
- [[concepts/Context-Engineering]] -- bottleneck de lo que los agents pueden ver: files, tests, logs, conventions, architecture notes, issue history
- [[concepts/Verify-First]] -- principio de que verification es el requisito mínimo para un loop funcional; sin ella, repeated prompting en vez de iterative improvement
- [[concepts/Unit-of-Work]] -- concepto que evoluciona: line → function → test → task → PR → migration → workflow

## Key Insights

- "Coding has always been in loops. Write code, run it, check the result, change it, repeat. That loop is older than AI."
- TDD made the loop explicit (red, green, refactor). BDD widened it toward behavior. CI widened it toward delivery.
- Phase 1 (Autocomplete): model helped with next edit. Copilot/Cursor Tab. Benefit: speed. Limit: scope.
- Phase 2 (Prompting): model moved from completion to task steering. Benefit: delegation. Limit: convergence.
- Phase 3 (Context): bottleneck became what agents can see. Repo-aware: read context, edit files, run commands, inspect result.
- Phase 4 (Harness): environment around one agent run. Benefit: repeatability. Limit: continuity.
- Phase 5 (Loop): loop checks result, decides whether to continue, uses feedback to improve next iteration.
- "The engineer is no longer only writing code or prompts. The engineer is designing the system that lets an agent keep working safely."
- "Without verification, you do not have a loop. You have repeated prompting. With verification, the loop can converge."
- "Build the loop. Stay the engineer."

## Open Questions
- ¿Cómo se implementa Loop-Driven Development en Hermes Agent con kanban workers?
- ¿Qué verifica un loop de Hermes vs un loop de Claude Code?
- ¿Cuándo un loop se convierte en runaway y necesita escalation?

## Source
- **Raw note:** [[raw-notes/loop-driven-development-the-next-layer-of-ai-coding]]
- **Original URL:** https://x.com/bibryam/status/2065445933601435823
