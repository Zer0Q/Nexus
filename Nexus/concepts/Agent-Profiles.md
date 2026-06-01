# Agent Profiles

## Definition
Fully isolated agent instances, each with its own config, memory, skills, sessions, and identity file. Profiles share nothing by default, enabling specialized agents with different personalities and capabilities running on the same machine.

## Why It Matters
A single generalist agent can't optimize for conflicting roles (e.g., creative designer vs. terse engineer). Profiles let you run specialized agents that each excel at their domain without cross-contamination.

## Key Ideas
- Created via `hermes profile create <name> --clone` (copies default config + .env)
- Each profile has its own SOUL.md, MEMORY.md, USER.md, skills/, sessions/
- Each profile can connect to a separate messaging bot (e.g., distinct Telegram bots)
- Customization patterns: route execution through external tools (Claude Code), teach visual style via reference images, schedule recurring tasks
- Switch profiles with `hermes -p <name>`

## Tradeoffs
- More profiles = more API keys, more bots, more maintenance
- Skills don't transfer between profiles by default
- Memory isolation means agents can't share learned facts

## Related
- [[concepts/Agent-Identity-Layer]] -- each profile has its own SOUL.md
- [[concepts/Multi-Agent-Development]] -- broader concept of coordinating multiple agents
- [[concepts/Agent-Cron-Scheduler]] -- each profile can have its own scheduled jobs

## Source
[[source-notes/AkshayPachaar-Hermes-Agent-Masterclass]]
