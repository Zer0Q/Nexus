---
title: "Every AI company needs a context layer. Nobody agrees what that is."
source: "https://www.linkedin.com/pulse/every-ai-company-needs-context-layer-nobody-agrees-what-bou-balust-p3mve/"
author: "Bou Balust"
published: "2026-06-03"
type: article
---

# Context Layer Landscape

## Summary
The context layer is the critical infrastructure every AI company needs, but the space fragments into three distinct problem spaces depending on what kind of context you're dealing with: an agent's own memory and instructions, a company's scattered institutional knowledge, or enterprise systems of record. Within each tier, tools fall on a spectrum from pure retrieval (RAG) to full ontologies, with governance requirements compounding as you move up. The common failure mode is misidentifying your tier — overshooting into enterprise ontology when retrieval suffices, or undershooting and starving agents of needed context.

## Core Concepts
- [[concepts/Context-Layer-Taxonomy]] -- three-tier classification of context problems: Agent's Context, Institutional Knowledge, Systems of Record, each with distinct tool requirements
- [[concepts/Context-Maturity-Spectrum]] -- progression from pure RAG retrieval through hybrid semantic layers to graph-native knowledge bases to full ontologies with inference rules
- [[concepts/Surface-Owners-vs-Neutral-Layers]] -- strategic divide: platforms that already own where context is created (Slack, Notion) versus neutral indexers that connect across everything
- [[concepts/Governance-Tax]] -- access control, data versioning, lineage, and audit requirements that emerge as context scale and user count grow, not as a separate stage

## Key Insights
- The phrasing "how do we make our context usable for agents?" is universal, but what companies actually mean underneath varies dramatically by their context tier
- Company size is a rough proxy for tier (bucket 1 = agent products, bucket 2 = startups on own data, bucket 3 = enterprises), but the actual determinant is the KIND of context, not size
- Glean sells to large enterprises yet operates almost entirely in bucket 2 (institutional knowledge), proving size ≠ tier
- Governance is "less a stage than a tax that kicks in with scale" — smaller setups can ignore it; larger ones cannot
- Within each bucket, the same spectrum applies: pure RAG → hybrid retrieval → graph-native → full ontology
- The Karpathy LLM-wiki / Obsidian-vault pattern is cited as the reference for graph-native agent memory
- Palantir Foundry + AIP is the enterprise reference for full ontology with governance and audit by design
- Modern Relay positions as the "anti-lock-in" answer to Palantir: context graph in code, runs on your own infrastructure, open-source core (Omnigraph)
- Edra is built by Palantir FDE (Forward Deployed Engineer) creators, reverse-engineering business models from data exhaust
- The deepest moat is tacit context — workarounds, real escalation paths, judgment in people's heads — that was never written down

## Open Questions
- How do tools like Mnemosyne Labs (bucket 1, hybrid) evolve when an agent accumulates enough context to cross into bucket 2 territory?
- Can the surface-owner vs neutral-layer dichotomy converge, or are they fundamentally competing approaches to the same problem?
- How does [[concepts/Context-Graph-RAG]] map onto the three-tier taxonomy — does it belong in bucket 2 or bucket 3?

## Source
- **Raw note:** [[raw-notes/every-ai-company-needs-a-context-layer-nobody-agrees-what-that-i]]
- **Original URL:** https://www.linkedin.com/pulse/every-ai-company-needs-context-layer-nobody-agrees-what-bou-balust-p3mve/
