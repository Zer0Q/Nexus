# Agent System Prompt

## Definition
Set of instructions configuring LLM behavior before user input is processed. Defines the agent's purpose, specialization, tone, and guardrails. Can be static or dynamic.

## Why It Matters
The system prompt is the primary mechanism for steering agent behavior. Well-crafted system prompts are more effective than trying to constrain behavior through user prompts alone.

## Key Ideas
- Defines agent role, purpose, and constraints
- Can be static (fixed at creation) or dynamic (generated per request)
- Dynamic instructions access dependencies for context-aware prompts
- Should include: role, task scope, output format, guardrails, examples
- Too long: wastes tokens and dilutes focus
- Too short: insufficient guidance

## Tradeoffs
- Longer prompts cost more tokens
- Over-constraining can limit agent flexibility

## Related
- [[concepts/Agent-Dependency-Injection]]
- [[concepts/Augmented-LLM]]

## Source
[[summaries/KusCamara-PydanticAI-Agent-Creation]]
