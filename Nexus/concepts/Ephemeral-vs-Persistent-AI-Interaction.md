# Ephemeral vs Persistent AI Interaction

## Definition
Two paradigms for AI interaction: ephemeral (chat-per-session, context disappears) vs. persistent (rulebook that survives across sessions, tasks, and agents).

## Why It Matters
Ephemeral interaction means re-explaining everything every session — style preferences, constraints, workflows. Persistent interaction encodes these once and inherits them automatically. The difference is between a "smart stranger you re-explain everything to every morning" and "an employee who read the handbook on day one."

## Key Ideas
- **Ephemeral model:** sign up → open chat → type question → get answer → repeat tomorrow with zero memory
- **Persistent model:** write rules once → Claude follows them every session, every task, every spawned agent
- Prompting is a conversation; conversations end and context disappears
- CLAUDE.md is infrastructure; it persists and compounds
- The distinction is "tool vs. system" — tools are used, systems are operated

## Tradeoffs
- Ephemeral: zero setup, maximum flexibility, zero accumulation
- Persistent: setup cost, less flexible per-session, accumulates value over time

## Related
- [[concepts/CLAUDE-MD-as-Context-Layer]]
- [[concepts/Compound-Effect-of-Persistent-Instructions]]
- [[concepts/Agent-Identity-Layer]]

## Source
[[source-notes/Hanakoxbt-CLAUDE-MD-Second-Employee]]
