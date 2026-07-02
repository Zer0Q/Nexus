---
title: "A Brain in a Git Repo: How GBrain Works"
source: "https://x.com/mem0ai/status/2070541048527609885"
author:
  - "[[@mem0ai]]"
published: 2026-06-26
created: 2026-06-29
description: "GBrain is an open-source brain for AI agents, built by @garrytan, president and CEO of @ycombinator, and open-sourced in April 2026.Instead ..."
tags:
  - "clippings"
summary:
---
![Imatge](https://pbs.twimg.com/media/HLwJoEzbIAA-Lj7?format=jpg&name=large)

GBrain is an open-source brain for AI agents, built by [@garrytan](https://x.com/@garrytan), president and CEO of [@ycombinator](https://x.com/@ycombinator), and open-sourced in April 2026.

Instead of keeping an agent's knowledge in a database, it stores it as markdown files in a git repo you own, then indexes those files for retrieval.

Garry runs it in production behind his own [@openclaw](https://x.com/@openclaw) and Hermes agents. By his account it holds 146,646 pages, 24,585 people, and 5,339 companies, with 66 cron jobs running autonomously that enrich and consolidate it overnight.

The design choice that makes GBrain worth understanding is its knowledge graph. It is built with plain pattern matching and zero LLM calls, and it is the single biggest driver of GBrain's retrieval quality, ahead of the vector search most systems rely on.

This article breaks down how it works: markdown as the source of truth, the self-wiring graph that costs nothing to build, the hybrid retrieval and synthesis layer on top, the overnight dream cycle that consolidates the brain while you sleep, and where a dedicated memory layer like Mem0 fits alongside it.

**Markdown is the source of truth**

![Imatge](https://pbs.twimg.com/media/HLtdwuEWUAA2G1T?format=jpg&name=large)

The core decision is that knowledge lives as markdown files in a regular git repo, the "brain repo," and nothing else is authoritative. GBrain syncs that repo into Postgres for retrieval, and a deletion in git becomes a soft-delete in the database ([README](https://github.com/garrytan/gbrain)). The index is downstream. The files are the truth.

This buys the properties that databases make awkward. Memory is diffable, so you can review what the agent learned as a pull request. It is version-controlled, so a bad write is a git revert. It is human-readable and operator-owned, sitting on your disk under your keys rather than in a vendor's store.

Two storage engines implement the same contract. The default is PGLite, Postgres 17 compiled to WebAssembly, in-process, zero-config, and ready in about two seconds, suitable for personal brains up to roughly 50,000 pages.

The scale path is Postgres plus pgvector on Supabase or self-hosted, for shared, large, or multi-machine deployments. A contract-first BrainEngine interface defines about 47 operations both engines implement, and the CLI and MCP server are generated from that one source, so the storage layer is swappable without touching anything above it ([README](https://github.com/garrytan/gbrain)).

**The self-wiring graph that costs nothing**

This is the part that makes GBrain interesting, and the part the benchmark singles out.

Every time a page is written, the put\_page operation extracts entity references from the markdown, from Obsidian-style wikilinks like \[\[wiki/people/bob\]\], and from typed-link syntax, then writes graph edges. It does this with regular expressions and string matching, zero LLM calls ([README](https://github.com/garrytan/gbrain)). The edges are typed: attended, works\_at, invested\_in, founded, advises, mentions, and more. They land in a links table as from\_page\_id, to\_page\_id, link\_type, and context, and the graph is walked with a recursive SQL traversal, exposed as gbrain graph-query for multi-hop queries ([README](https://github.com/garrytan/gbrain), [GBRAIN\_V0](https://github.com/garrytan/gbrain/blob/master/docs/GBRAIN_V0.md)).

![Imatge](https://pbs.twimg.com/media/HLtd2S1XAAAwpXC?format=jpg&name=large)

The point is what this graph does to retrieval. On BrainBench, GBrain's own evaluation, the full system scores P@5 of 49.1% and R@5 of 97.9%. Disable the graph and fall back to vector plus keyword fusion, and P@5 collapses to 17.8%. Pure vector-only retrieval scores 10.8%. The eval doc states it plainly: "the graph layer is worth 31 points P@5" ([BrainBench v0.20.0](https://github.com/garrytan/gbrain-evals/blob/main/docs/benchmarks/2026-04-23-brainbench-v0.20.0.md)). The component everyone treats as the expensive centerpiece, vector search, contributes the least of the three. The free regex graph contributes the most.

![Imatge](https://pbs.twimg.com/media/HLtd7X1W0AAX4z4?format=jpg&name=large)

The reason is the kind of question a personal brain actually gets asked. "Who at my portfolio companies is working on AI agents" is a relational query. It is not answered by finding the chunk most semantically similar to the question. It is answered by traversing edges: this person works\_at that company, that company is invested\_in by you, this person mentions agents. Vector similarity is blind to that structure. Typed edges are made of it.

![Imatge](https://pbs.twimg.com/media/HLteAq5XQAAK_Pe?format=jpg&name=large)

The honest scope on "zero LLM calls": it describes graph construction at write time only. Retrieval and synthesis still spend tokens, as the next section shows.

**Hybrid retrieval and the synthesis layer**

GBrain exposes two retrieval verbs, and the split is the product.

gbrain search returns raw pages, ranked and fast. Under the hood it is hybrid: vector search using HNSW cosine over 1,536-dimension OpenAI embeddings (text-embedding-3-large, reduced from 3,072 via the dimensions API), run in parallel with Postgres tsvector full-text keyword search (with pg\_trgm for fuzzy title matching), then fused with Reciprocal Rank Fusion using the standard 1/(60 + rank) formula, with a source-tier boost and a reranker on top ([GBRAIN\_V0](https://github.com/garrytan/gbrain/blob/master/docs/GBRAIN_V0.md)). A query is first expanded into alternative phrasings by Claude Haiku, every phrasing is embedded, both searches run, RRF merges them, and a four-layer dedup pass cleans the result: by source, by cosine similarity above 0.85, a per-type cap of 60%, and a per-page maximum.

gbrain think is the layer Tan built GBrain for. Instead of returning chunks, it composes "a synthesized answer across the results with explicit citations to the source pages AND an honest note on what the brain doesn't know yet" ([README](https://github.com/garrytan/gbrain)). That last clause is the differentiator. The system surfaces its own gaps: stale pages, uncited claims, contradictions, and holes. As GBrain frames it, search gives you raw pages; think gives you the answer, and tells you what it is unsure of.

![Imatge](https://pbs.twimg.com/media/HLteF64XkAEdXMI?format=jpg&name=large)

**The dream cycle: consolidation while you sleep**

A brain that only writes on demand drifts. Duplicate people pages accumulate, citations rot as the underlying pages change, and contradictions pile up unnoticed. GBrain's answer is a scheduled background pass it calls the dream cycle.

Cron-driven enrichment runs during quiet hours and, in Garry's words, "while you sleep: dedup people pages, fix citations, score salience, find contradictions, prep tomorrow's tasks" ([README](https://github.com/garrytan/gbrain)).

The reference deployment ships with 20-plus recurring jobs wired to a dream cycle and quiet-hours scheduling; Tan's own production brain runs 66 ([GBRAIN\_SKILLPACK](https://github.com/garrytan/gbrain/blob/master/docs/GBRAIN_SKILLPACK.md)). Contradiction-finding is concrete: gbrain eval suspected-contradictions samples retrieval pairs, applies a date pre-filter and a query-conditioned LLM judge, and surfaces conflicts between what the agent has written at different times, and it is wired into the daily dream cycle ([README](https://github.com/garrytan/gbrain)).

![Imatge](https://pbs.twimg.com/media/HLteRUiWUAA33kg?format=jpg&name=large)

There is a cost discipline underneath. From v0.14.0, deterministic cron work (API fetches, token refreshes, scrape-and-write) runs as "shell jobs" that move off the LLM gateway entirely: zero tokens per fire, and roughly 60% gateway headroom reclaimed ([GBRAIN\_SKILLPACK](https://github.com/garrytan/gbrain/blob/master/docs/GBRAIN_SKILLPACK.md)). The expensive model is reserved for the work that genuinely needs judgment.

This is the loop that makes the whole thing compound: signal arrives, the agent checks the brain first, responds with full context, writes the result as a page, auto-links it into the graph for free, and the cron sync plus the overnight dream cycle keep the index current and the knowledge clean. The agent gets sharper each day not because the model changed, but because the brain was consolidated while it was idle.

**Brain is not memory**

GBrain draws a line that explains its whole scope, and it is worth taking at face value. A brain stores "world knowledge, facts about entities external to the agent": people, companies, deals, meetings, concepts, ideas. Memory holds "how the agent operates, not facts about the world": preferences, decisions, tool config, session continuity. The rule is "world knowledge persists in the brain, operational state persists in agent memory, and the agent never puts information in the wrong layer" ([brain-vs-memory](https://github.com/garrytan/gbrain/blob/master/docs/guides/brain-vs-memory.md)).

The reason given is durability. Agent memory "doesn't survive agent resets on some platforms," so anything critical about the world must live in GBrain, which is durable by virtue of being files in git. GBrain is deliberately not trying to be the layer that remembers your preferences or carries operational continuity across tools. It is a knowledge base for an agent, not the agent's working memory.

**What the numbers actually say**

BrainBench is a real, reproducible eval, and it is also a self-administered one. The corpus is 240 fictional pages (80 people, 80 companies, 50 meetings, 30 concepts), generated by Opus, committed to the repo, and regeneratable from a seed, queried by 145 relational questions ([BrainBench v0.20.0](https://github.com/garrytan/gbrain-evals/blob/main/docs/benchmarks/2026-04-23-brainbench-v0.20.0.md)). An independent review by Vectorize checked the methodology and called it internally consistent, documented, and reproducible, and confirmed that "the typed-edge graph contributes more retrieval lift than the hybrid search alone" ([Vectorize review](https://vectorize.io/articles/gbrain-review)).

Two caveats matter. The benchmark covers only the retrieval categories, two of twelve, and the run was scoped to answer "did retrieval regress between versions," not to be a comprehensive score. And it is explicitly not comparable across systems, because the corpus is GBrain's own. There is no head-to-head here against Mem0, Zep, or Letta, and GBrain's published evals run on its own corpus rather than shared benchmarks like BEAM or LOCOMO. The production-scale figures (the 146,646 pages, the 66 cron jobs) are Tan's self-report, not independently measured.

**Where it stops**

The design's strengths set its limits. Files-on-disk is operator-owned and diffable, but it is also a bet that not everyone shares: Cloudflare, launching its own Agent Memory in April 2026, argued the opposite case directly, that "tighter ingestion and retrieval pipelines are superior to giving agents raw filesystem access," citing cost, performance, and a cleaner foundation for temporal logic and supersession ([Cloudflare](https://blog.cloudflare.com/introducing-agent-memory/)).

The free graph is only as good as the link discipline that feeds it; regex extraction needs the wikilinks and typed-link syntax to actually be present in the markdown, so a sloppily written page wires itself poorly.

And PGLite is single-writer, so a live MCP server contends with cron for the write lock, which is part of why the scale path moves to full Postgres ([README](https://github.com/garrytan/gbrain)).

**Where a memory layer fits**

GBrain itself names the gap. It is a brain, not a memory, and its own docs say operational and preference state belongs in a different layer, one that survives agent resets and follows you across tools. That is the layer [Mem0](https://mem0.ai/) is built to be.

![Imatge](https://pbs.twimg.com/media/HLtey1KXgAAVquK?format=jpg&name=large)

The two are complementary by GBrain's own taxonomy.

GBrain holds durable world knowledge as files you own, optimized for relational recall over people and companies. A memory layer holds the things that never pin to an entity page: how you like work done, a correction you stated once, the running thread of what an agent has tried across sessions and machines.

It retrieves by meaning rather than by hand-authored links, it is identity-scoped so one memory follows you across Cursor, a terminal agent, and your CLI, and it is measured at the 1M to 10M token scale that long-running agents actually reach. One keeps your knowledge sharp; the other keeps your agent consistent. The interesting systems will run both.

For how every major harness is approaching this, see State of Memory in Agent Harnesses:

> 2 de juny

**In Context #14**

This blog is part of In Context, a [@mem0ai](https://x.com/@mem0ai) blog series covering AI Agent memory and context engineering.

Mem0 is an intelligent, open-source memory layer designed for LLMs and AI agents to provide long-term, personalized, and context-aware interactions across sessions.

- Get your free API Key here:[app.mem0.ai](https://app.mem0.ai/?utm_source=x_article_mem0&utm_medium=x_article&utm_campaign=gbrain&utm_content=gbrain)
- or self-host mem0 from our[open source github repository](https://github.com/mem0ai/mem0)

**References**

- [garrytan/gbrain (GitHub README)](https://github.com/garrytan/gbrain)
- [GBrain v0 architecture doc](https://github.com/garrytan/gbrain/blob/master/docs/GBRAIN_V0.md)
- [GBrain skillpack doc](https://github.com/garrytan/gbrain/blob/master/docs/GBRAIN_SKILLPACK.md)
- [GBrain brain-vs-memory guide](https://github.com/garrytan/gbrain/blob/master/docs/guides/brain-vs-memory.md)
- [BrainBench v0.20.0 benchmark](https://github.com/garrytan/gbrain-evals/blob/main/docs/benchmarks/2026-04-23-brainbench-v0.20.0.md)
- [Vectorize: GBrain review](https://vectorize.io/articles/gbrain-review)
- [Cloudflare: Introducing Agent Memory (April 2026)](https://blog.cloudflare.com/introducing-agent-memory/)
- [Mem0](https://mem0.ai/)