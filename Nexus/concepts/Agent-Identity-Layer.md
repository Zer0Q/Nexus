# Agent Identity Layer

## Definition
A static configuration file (SOUL.md) that defines an AI agent's personality, tone, communication style, and hard limits. Loaded as the first slot in the system prompt, before memory or skills.

## Why It Matters
Without an identity layer, every agent instance feels interchangeable — same model, same tools, different hats. SOUL.md is the fixed frame through which all learning, memory writing, and skill creation happens. It ensures consistency across sessions, projects, and interactions.

## Key Ideas
- Hand-authored and static — you write it once, tweak over time
- Occupies slot #1 in system prompt (before memory, skills, context)
- Falls back to built-in default if missing
- Defines personality, not capabilities — skills handle procedures, memory handles facts
- Acts as a filter: the agent's self-generated content reflects its identity

## Tradeoffs
- Too restrictive: limits the agent's ability to adapt to different contexts
- Too vague: personality drifts across sessions
- Requires iteration: first draft is rarely right

## Related
- [[Agent-Multi-Tier-Memory]] -- the moving parts inside the identity frame
- [[Self-Evolving-Skills]] -- skills created through the lens of identity
- [[Agent-Profiles]] -- each profile has its own SOUL.md

## Source
[[AkshayPachaar-Hermes-Agent-Masterclass]]
