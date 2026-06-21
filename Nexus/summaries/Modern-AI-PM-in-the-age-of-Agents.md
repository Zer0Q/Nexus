---
type: article
title: "The Modern AI PM in the age of Agents"
description: "How the PM role shifts when agents can produce working code: problem shaping, context curation, and evaluation taste become the core skills."
resource: "https://x.com/Saboo_Shubham_/status/2008742211194913117"
timestamp: 2026-01-07
tags:
  - product-management
  - ai-agents
  - problem-shaping
  - context-engineering
---

## Synthesis

The author, a PM at Google, describes how the PM role is fundamentally shifting as agents compress the translation layer between customer needs and implementation. The spec is becoming the product — when agents can take a well-formed problem and produce working code, the PM's job shifts from translating for engineers to forming intent clearly enough that agents can act on it directly.

Three new core PM skills emerge:

**Problem shaping.** Taking an ambiguous customer pain point and shaping it into something clear enough that an agent or team of agents can act on it. The spec is no longer a document — it's a well-formed problem with clear boundaries.

**Context curation.** The quality of what an agent produces is directly proportional to the context fed to it. Effective context docs include: the user (real details, not personas), the problem in their words (direct quotes), what good looks like (examples), what you've tried and why it failed, constraints that shape the solution, and how you'll know it worked.

**Evaluation and taste.** When agents produce output quickly and in bulk, taste becomes the most important skill. Is this actually solving the problem? Does it handle the edge cases? Is this the version we should ship or just the version that runs?

The mental model shift: old PM figures out what to build -> writes spec -> engineers build it -> PM reviews. New model: PM figures out what to build -> PM builds it with agents -> PM evaluates -> iterate quickly -> hand to engineers for production.

The speed of shipping is accelerating. Cycle times compress from quarterly planning to continuous deployment of ideas. When the implementation barrier drops, the bottleneck shifts upstream: the scarce resource is knowing what's actually worth building.

## Key Insights

- "If your job was mostly translating customer needs into documents for engineers, that's a workflow. Workflows get automated."
- Hold ambiguity longer. Don't collapse to a solution too early. Let agents help you understand the solution space before committing.
- Build two or three completely different approaches in parallel just to see which one feels right. That used to be expensive; now it's a Tuesday afternoon.
- The best PMs understand problems so deeply that the solution becomes obvious to them and to the agents they work with.

## Questions

- How does this map to [[Agentic-Engineering]] maturity levels?
- What context curation patterns generalize beyond PMs to other roles?
- How does the "spec is the product" concept relate to [[Spec-Driven-Development]]?
