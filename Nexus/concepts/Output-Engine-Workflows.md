# Output Engine Workflows

## Definition
Five scheduled or triggered workflows running on top of a knowledge vault that transform raw capture into shippable, billable output. Each workflow is a prompt file stored in the system folder. Four workflows feed the fifth, which produces revenue directly.

## Why It Matters
Without automated workflows, a vault is a library. With them, it becomes a production engine. The five workflows ensure every capture is classified, synthesized, connected, and ultimately transformed into output -- closing the gap between passive collection and active creation.

## Key Ideas
- **Workflow 1 -- Nightly Processor (2 AM)**: Classifies day's captures by note type, moves from CAPTURE to CONTEXT, adds frontmatter. Pure mechanical work.
- **Workflow 2 -- Morning Brief (6 AM)**: Reads last 7 days of context, writes a 400-word briefing surfacing patterns, contradictions, and non-obvious connections.
- **Workflow 3 -- Connection Surface (Sundays)**: Looks across 30 days of context, returns 3 connections you would not find by deliberate search.
- **Workflow 4 -- Project Updater (Weekly, manual)**: Reads latest captures relevant to each active project, updates project doc, suggests next moves.
- **Workflow 5 -- Output Generator (On-demand, manual)**: The money workflow. Reads relevant notes from CONTEXT and PROJECTS, produces a complete draft in your voice, saves to OUTPUT.
- Workflows 1-4 feed Workflow 5. Only Workflow 5 produces revenue directly.

## Tradeoffs
- Token costs scale with capture volume and workflow frequency
- Each workflow requires prompt tuning for your specific voice and domain
- Over-automation risks producing output that sounds generic rather than personal

## Related
- [[concepts/Four-Zone-Monetization-Vault]] -- workflows drive content through the four zones
- [[concepts/Daily-Synthesis-Workflow]] -- similar to Workflow 2 (Morning Brief)
- [[concepts/Output-Generator-Prompt]] -- the specific prompt for Workflow 5
- [[concepts/Automated-Capture-Pipeline]] -- handles the mechanical routing Workflow 1 performs

## Source
[[source-notes/Zeuuss-Weaponize-Obsidian-Claude-For-Revenue]]
