# Self-Improvement Loop

## Definition
The continuous feedback cycle where Hermes Agent reviews every completed task — what worked, what didn't, the optimal path — and saves those learnings as skills in ~/.hermes/skills/. The next time a similar task arrives, it uses the proven procedure instead of rediscovering it from scratch.

## Why It Matters
This is the compounding mechanism that separates Hermes from other agents. Where ChatGPT and Claude start from zero each session, Hermes gets better every single session. After six months, it knows your workflows, formatting preferences, and optimal shortcuts better than a human assistant would.

## Key Ideas
- **Cycle**: Give task → execute → review → save skill → reuse next time
- Skills live as transparent markdown files in ~/.hermes/skills/
- You correct it once; it never makes that mistake again
- Six months in: knows how you format things, which tools work, your tone preferences
- Updates add new skills automatically without breaking existing ones
- Distinct from [[Self-Evolving-Skills]] which focuses on the skill file mechanics; this covers the broader behavioral loop

## Tradeoffs
- Agent may save suboptimal approaches (self-congratulation tendency)
- Requires occasional manual review of auto-generated skills
- Skill bloat without [[Agent-Skill-Curator]] maintenance

## Related
- [[Self-Evolving-Skills]] -- the skill file mechanics that power this loop
- [[Agent-Skill-Curator]] -- garbage collection for skills
- [[Compounding-Knowledge-Context]] -- memory + skills compound over time
- [[Hermes-Dashboard]] -- skills visible and editable in the Skills tab

## Source
[[IBuzovskyi-Hermes-Agent-Complete-Guide]]
