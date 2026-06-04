# SOUL-MD Configuration

## Definition
The instruction layer file that governs how Hermes interprets everything it reads in your vault. Beyond personality and tone, it defines your research methodology, what you expect from the agent, hard rules, and boundaries. A well-written SOUL.md makes Hermes read your notes through the lens of who you are and what you are trying to do.

## Why It Matters
Without SOUL.md, Hermes reads your vault as a generic content library. With a specific SOUL.md, it produces answers that sound like they came from inside your operation. The difference in output quality is significant -- the same vault query with generic SOUL.md produces capable but generic answers.

## Key Ideas
- Defines identity, role, tone, standards, and boundaries
- Equivalent of CLAUDE.md but for the agent layer
- Three critical sections most people skip: current obsessions, challenge instructions, negative constraints
- Vague SOUL.md files produce vague outputs
- Takes ~30 minutes to write well; matters more than technical setup

## Tradeoffs
- Too restrictive: limits agent adaptability
- Too vague: personality drifts across sessions
- Requires iteration: first draft is rarely right

## Related
- [[concepts/Agent-Identity-Layer]] -- the broader concept
- [[concepts/SOUL-MD-Current-Obsessions]] -- telling Hermes your active research
- [[concepts/SOUL-MD-Challenge-Instructions]] -- how you want to be challenged
- [[concepts/SOUL-MD-Negative-Constraints]] -- what you never want

## Source
[[summaries/DamiDefi-Hermes-Obsidian-Vault-Integration]]
