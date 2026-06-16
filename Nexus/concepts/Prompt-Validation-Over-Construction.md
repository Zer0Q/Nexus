---
created: 2026-05-28
type: concept
tags:
- ai
- prompting
- methodology
description: '## Related - [[concepts/LLM-Harness]] -- harnesses enable simpler prompts
  by handling context - [[concepts/Metaprompt]] -- shortcut when prompts get complex'
---


# Prompt Validation Over Construction

The primary prompting skill has shifted from constructing elaborate prompts to validating AI-generated results.

## Three Elements That Still Matter
1. **Expected Deliverable** -- the concrete output, not the general topic
2. **End Use Case** -- what the result is for changes how the AI prioritizes
3. **Output Format** -- format, length, tone, success criteria

## What to Drop
- Step-by-step instructions on how the AI should work internally
- Role assignments and elaborate context framing (the harness handles this)

## Validation Process
1. Before execution, define how you know the result is good
2. Check the result against those criteria
3. If something fails, ask the AI to explain its process and correct specifically
4. Iterate (ask, check, refine) rather than rewriting the original prompt

## Why Iteration Beats Rewriting
- Rewriting a prompt is "trying again" — hoping the AI does it right the first time
- Iteration forces you to study and understand the result
- Specific corrections are more effective than general prompt changes

## Related
- [[concepts/LLM-Harness]] -- harnesses enable simpler prompts by handling context
- [[concepts/Metaprompt]] -- shortcut when prompts get complex

## Sources
- [[summaries/DavidHurtado-Harness-and-Prompting]]
