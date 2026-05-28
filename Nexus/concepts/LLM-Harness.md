---
created: 2026-05-28
type: concept
tags:
  - ai
  - llm
  - infrastructure
  - prompting
---

# LLM Harness

The harness is the software layer between the user's prompt and the language model — managing context, coordinating intermediate steps, and assembling the final response.

## What the Harness Does
- **Context Management** -- loads, filters, and prioritizes context windows
- **Step Coordination** -- chains intermediate reasoning steps
- **Response Assembly** -- combines model outputs with tools, search, and memory
- **Tool Integration** -- connects models to external APIs, code execution, file systems

## Impact on Prompting
- Complex prompts are less necessary — the harness does work users used to do manually
- Three elements still matter: expected deliverable, end use case, output format
- Specifying the "how" usually worsens results — the harness's internal method is often superior
- [[Prompt-Validation-Over-Construction]] -- effort shifts from building prompts to validating results

## Related
- [[Multi-Agent-Development]] -- harnesses orchestrate agent workflows
- [[Context-Explosion]] -- harnesses help manage but don't eliminate context limits
- [[Skill-Based-AI-Agents]] -- skills are harness-level abstractions

## Sources
- [[DavidHurtado-Harness-and-Prompting]]
