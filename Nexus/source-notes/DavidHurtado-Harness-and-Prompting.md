---
title: "Harness y por qué los prompts complejos están perdiendo sentido"
source: "https://davidhurtado.substack.com/p/harness-y-por-que-los-prompts-complejos"
author: "David Hurtado"
published: "2026-05-27"
type: article
---

# Harness and the Decline of Complex Prompts

## Summary
The harness — the software layer between the user's prompt and the model — is doing more of the work that used to require complex prompt engineering. Users should define what, why, and format, but not the how. Validation, not prompt construction, is now the primary skill.

## Core Concepts
- [[concepts/LLM-Harness]] -- software layer managing context, intermediate steps, and response assembly
- [[concepts/Prompt-Validation-Over-Construction]] -- effort shifts from building prompts to validating results
- [[glossary/Metaprompt]] -- asking the AI to draft its own optimal prompt for a task
- [[concepts/Context-Explosion]] -- harnesses help manage context, but large specs still degrade quality

## Key Insights
- Complex prompts are less necessary because harnesses handle context management and step coordination
- Three elements still matter: expected deliverable, end use case, output format
- Specifying the "how" usually worsens results — the AI's internal method is often better than the user's
- AI generates responses that look better than they are — validation requires clear success criteria
- Iteration (ask, check, refine) beats rewriting the original prompt

## Open Questions
- How do harnesses handle multi-agent orchestration?
- Can validation criteria be formalized as automated quality gates?
