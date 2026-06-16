---
type: Concept
title: CLAUDE.md as Context Layer
description: A markdown file at the vault root that teaches the AI how to think alongside
  you specifically. Contains identity, projects, vault structure, thinking style,
  ...
tags:
- concepts
timestamp: '2026-06-16T13:58:58Z'
---

# CLAUDE.md as Context Layer

## Definition
A markdown file at the vault root that teaches the AI how to think alongside you specifically. Contains identity, projects, vault structure, thinking style, and hard rules. Read by the AI before every operation to calibrate outputs to your specific context.

## Why It Matters
Without it, every AI synthesis is generic. With it, outputs are calibrated to your thinking, projects, voice, and unresolved questions. The quality of CLAUDE.md directly determines the quality of AI output -- vague context produces vague results.

## Key Ideas
- Sections: identity, current projects, vault structure, thinking style, what you want from AI, hard rules
- Weekly Focus section weights all system actions toward current priorities
- Must be updated regularly (e.g., every Monday) -- stale CLAUDE.md produces stale output
- Different from schema: schema tells AI how the wiki works; CLAUDE.md tells AI who you are
- Template exists but must be filled with real specifics, not placeholders
- The most important file in the entire system
- Five-section alternative: Role, Style, Constraints, Workflow, Quality — covers all behavioral dimensions
- Without CLAUDE.md, Claude is a "smart stranger you re-explain everything to every morning"; with it, an "employee who read the handbook on day one"
- The compound effect: week 1 fixes generic output, week 2 adds pattern rules, week 3 specializes per project, week 4 enables hands-off delegation

## Tradeoffs
- Requires honest self-reflection to write well
- Needs regular maintenance to stay current
- Too vague = generic output; too specific = brittle to change
- Over-constraint risk: too many rules can make the AI rigid and uncreative

## Related
- [[concepts/Four-Layer-Vault-Architecture]]
- [[concepts/Daily-Synthesis-Workflow]]
- [[concepts/AI-Chief-of-Staff]]
- [[concepts/Compound-Effect-of-Persistent-Instructions]]
- [[concepts/System-Setup-Hierarchy]]
- [[tools/CLAUDE-MD-Five-Section-Template]]

## Source
[[summaries/DamiDefi-Claude-Vault-Integration]]
