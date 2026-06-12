# Persona Prompting

## Definition
Defining agent identity through behavioral constraints (tone, brevity, action-orientation) rather than capability descriptions. A persona turns a helpful assistant into a specific character — terse, certain, allergic to filler.

## Why It Matters
A generic assistant answers your question. A persona answers like someone who works for you. The same model produces dramatically different output quality when constrained by identity: "Never open with 'Certainly' or 'Great question.' Default to action. Report results, not intentions."

## Key Ideas
- Four dimensions: personality (who the agent is), style (how it sounds), constraints (what to avoid), technical posture (decision preferences)
- SOUL.md in Hermes Agent occupies slot #1 of the system prompt — the durable identity that replaces the built-in default
- JARVIS persona example: "Talk like a calm operator. One breath. No filler. When I'm wrong, say so in one line."
- Persona effects compound over conversation history — the agent stays in character across turns
- The single-rule safety net: "Never send money to anyone without explicit confirmation" covers most personal-use risk

## Tradeoffs
- Overly strict personas can make agents unhelpful in edge cases where flexibility is needed
- Persona drift can occur in long conversations where the model forgets early constraints
- Different tasks may benefit from different personas — switching requires context management

## Related
- [[concepts/SOUL-MD]]
- [[concepts/Voice-Activation-Assistant]]
- [[concepts/System-Prompt]]

## Source
[[summaries/0xChaseTM-How-to-Build-Your-Own-JARVIS]]
