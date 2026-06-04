# Self-Evolving Skills

## Definition
Agent-authored procedural playbooks (SKILL.md files) created autonomously after completing complex tasks, overcoming errors, or discovering non-trivial workflows. The agent saves successful approaches so it can follow proven procedures instead of rediscovering them from scratch.

## Why It Matters
Without self-evolving skills, agents repeat the same trial-and-error cycles every session. With them, experience compounds — the agent gets faster and more reliable at tasks it has encountered before.

## Key Ideas
- Triggered by: complex tasks (5+ tool calls), error recovery, user corrections, novel workflows
- Format: Markdown with YAML frontmatter (name, description, version, author, platforms)
- Actions: create, patch (preferred — token-efficient), edit, delete, write_file, remove_file
- Progressive disclosure: Level 0 (names + descriptions, ~3k tokens), Level 1 (full content), Level 2 (reference files)
- Problem → solve → save as skill → load next time instead of rediscovering

## Tradeoffs
- Agent tends toward self-congratulation — may save suboptimal approaches
- Can overwrite manual customizations with worse versions
- Requires maintenance (Curator) to prevent skill bloat

## Related
- [[concepts/Agent-Skill-Curator]] -- garbage collection for agent-created skills
- [[concepts/GEPA-Prompt-Evolution]] -- offline optimization to fix bad skills
- [[concepts/Agent-Identity-Layer]] -- skills created through the lens of identity

## Source
[[summaries/AkshayPachaar-Hermes-Agent-Masterclass]]
