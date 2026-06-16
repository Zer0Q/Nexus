---
type: Concept
title: Output Generator Prompt
description: A production-tuned prompt that reads relevant notes from the context
  and project zones of a knowledge vault, then produces a complete draft of billable
  outpu...
tags:
- concepts
timestamp: '2026-06-16T13:58:58Z'
---

# Output Generator Prompt

## Definition
A production-tuned prompt that reads relevant notes from the context and project zones of a knowledge vault, then produces a complete draft of billable output in the user's voice. It is the single highest-revenue workflow in a monetized vault.

## Why It Matters
This is the prompt that turns 4000 dormant notes into shippable, billable work. It is the only workflow that produces revenue directly; the other four workflows (nightly processor, morning brief, connection surface, project updater) exist to feed it.

## Key Ideas
- Lives in 07-SYSTEM/prompts/output-generator.md
- Reads relevant notes from 01-CONTEXT/ and 02-PROJECTS/
- Produces a complete draft in the user's voice, saved to 03-OUTPUT/
- Tuned across 6 months of production use
- Includes an expected_revenue stamp at the bottom to track which note types and topics produce highest-value output
- After a few weeks, the revenue data tells you what to capture more of
- The prompt is the money workflow; everything else is infrastructure feeding it

## Tradeoffs
- Requires a deep enough context zone to pull from (cold vault = poor output)
- Voice calibration takes weeks of iteration
- Revenue stamp tracking adds metadata overhead to each output note

## Related
- [[concepts/Output-Engine-Workflows]] -- this is Workflow 5, the revenue-producing workflow
- [[concepts/Expected-Revenue-Stamp]] -- the tracking mechanism embedded in this prompt
- [[concepts/Four-Zone-Monetization-Vault]] -- reads from zones 01 and 02, writes to zone 03

## Source
[[summaries/Zeuuss-Weaponize-Obsidian-Claude-For-Revenue]]
