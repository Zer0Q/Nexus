---
type: workflow
related:
- Connection-Surface-Workflow
- Knowledge-Graph-Learning
- Pattern-Identification-Across-Notes
description: A post-study-session workflow that finds non-obvious connections between
  newly added concept notes and existing ones. Runs after adding 3-5 new concept notes...
tags:
- concepts
---


# Connection-Protocol

## Definition
A post-study-session workflow that finds non-obvious connections between newly added concept notes and existing ones. Runs after adding 3-5 new concept notes, producing three connections with specific relationship descriptions and integration test questions.

## Why It Matters
Non-obvious connections are where understanding changes. Without this protocol, Claude finds only obvious links (concept A is similar to concept B). The non-obvious connection is the one where understanding the relationship changes how you understand both concepts individually.

## Key Steps
1. After adding 3-5 new concept notes in a session, trigger the protocol
2. Claude reads all new concepts and all existing concepts in the vault
3. Finds three non-obvious connections missed during sequential study
4. For each connection: names the two concepts, writes the relationship in one precise sentence, explains why it matters for deep understanding, generates a question answerable only by someone who understands both concepts and their relationship
5. Non-obvious means: not mentioned in either concept note, not immediately apparent from surface descriptions, produces an insight neither concept produces alone

## Tradeoffs
- Requires Claude to read across the full vault; context limits may apply for large vaults
- Quality of connections depends on the diversity and depth of existing concept notes

## Related
- [[concepts/Connection-Surface-Workflow]]
- [[concepts/Knowledge-Graph-Learning]]
- [[concepts/Pattern-Identification-Across-Notes]]
- [[concepts/Knowledge-Graph-as-Semantic-Layer]]
- [[concepts/Synthesis-Session]]

## Source
[[summaries/NeilXBT-Obsidian-Knowledge-Graph-Learning]]
