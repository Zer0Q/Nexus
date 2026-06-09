---
title: "Every AI company needs a context layer. Nobody agrees what that is."
source: "https://www.linkedin.com/pulse/every-ai-company-needs-context-layer-nobody-agrees-what-bou-balust-p3mve/?trackingId=ZDIR6UtGQhuHq7fUr%2Fj3aw%3D%3D"
author:
published: 3 de junio de 2026
created: 2026-06-09
description:
tags:
  - "clippings"
summary:
---
Many companies come to us asking for advice about private context. They all start the same way: "how do we make our context usable for agents?" The phrasing is always the same. What's underneath it never is.

The moment you look closely, it breaks apart into several very different problems that only look alike from a distance. This post is usually the wall of words I'd give them in a call. I'm writing it down here so others can use it too.

A caveat up front: I'll probably miss companies, and my knowledge is partial. I haven't been able to test all of these myself. If something's misrepresented, tell me and I'll correct it.

What actually sorts this space is the **kind of context you're dealing with:** because that decides what exists to work with and which tools are even on the table.

Each builds on the one before:

1. **Agent’s Context** (*what you tell your agent)***:** The agent's own conversational context: its instruction files and conversation history. Self-contained; no company stack behind it.
2. **Institutional Knowledge** (*how your company operates)* — mostly unstructured: the docs, chats, notes, and tickets a company already lives in, scattered across the apps where work happens.
3. **Systems of Record** *(your company operating records)* — the structured stuff too: warehouses, databases, ledgers, CRM, across multiple stacks that were never built to talk to each other.

The tricky part is knowing which one you're in. Company size is the usual shortcut: bucket 1 is typically someone building an assistant or an agent product; bucket 2, a startup putting agents on top of their own data (automating GTM, support..); bucket 3, a large enterprise doing the same across many systems.

These are just typical cases, not strict rules. A startup automating finance might touch a system of record; Glean sells to large enterprises yet works almost entirely on institutional knowledge. The context and your needs are what sort you, not your size.

There's one more thing that matters more as you move up the buckets: governance. As your context grows and more people touch it, you start needing what the smaller setups can ignore: access control, data versioning, lineage, audit. It's less a stage than a tax that kicks in with scale.

### 1\. Agent’s Context

*(mostly for agentic products and assistants, leaving out of this memory built specifically for coding agents, since that’s a different beast )*

When the consumer is an agent, there's no company stack behind it, but that doesn't mean there's nothing to work with. There are usually guidelines, process docs, and markdown files describing how the agent should operate and what it needs to reference ([AGENTS.md](http://agents.md/), a [CLAUDE.md](http://claude.md/),… a set of instructions). And there's the interaction trace itself: what was said, decided, and corrected over time. Both are real context. The body of material is just narrower and more self-contained than in a company: it's the agent's own operating manual plus its accumulated memory, rather than a sprawl of systems.

So the players here are answering two related questions: how do you persist the agent's memory across sessions, and how do you keep its operating knowledge (those guidelines and docs) structured and usable rather than a flat dump? You could argue here that depending on the amount of context/memory accumulated, you could get away with a compiled set of flattened files accessible through RAG, or you would need a fully-fledged ontology.

I think the answer is it's a spectrum, and where a tool sits on it is mostly a bet about how much accumulated context it expects you to have. At the low end, you barely model anything; at the high end, you model everything and pay for it. Running left to right:

**Pure RAG — files + similarity search.** Extract facts, embed them, retrieve the similar-looking ones. Cheapest to stand up, and enough when the memory is "what did the user tell me." This is where [Mem0](https://www.linkedin.com/company/mem0/) *(hosted)* and [Hyperspell](https://www.linkedin.com/company/hyperspell/) *(hosted)* sit; Hyperspell also pulls in your own accounts (Slack, Gmail, Notion), which drags it toward bucket 2. The fully-local equivalent is a single file on your machine, no infrastructure: **SQLite AI**, **memweave**, **sqlite-memory**, AgentDB *(all local)*. If you're already in the [LangChain](https://www.linkedin.com/company/langchain/) stack, LangMem is its built-in option here.

**Hybrid retrieval — RAG plus light structure.** Still file-backed, but it keeps some facts and relationships alongside the embeddings. This is the sweet spot a lot of the practitioner enthusiasm lands on right now. [Mnemosyne Labs](https://www.linkedin.com/company/mnemosynelabs/) *(local, open-source)* is the one doing the rounds, lightweight, fully local, and with structured support. **Signet AI** and **agentmemory** are close neighbors: a semantic layer with optional graph extraction.

**Graph-native — an interlinked knowledge base you own.** The agent doesn't just store facts, it compiles its accumulated context into a self-maintained web of entities and relationships. The **Karpathy LLM-wiki /** [Obsidian](https://www.linkedin.com/company/obsidianmd/) **\-vault** pattern is the reference, and [Garry Tan](https://www.linkedin.com/in/garrytan/) 's **Gbrain** *(local)* is a shipping take where the graph *is* the architecture: the difference from Mnemosyne, where the graph is present but secondary.

**Full Ontology — The far end**. A true ontology adds rules over the entities, so the system can *infer* facts that were never written down. Almost nothing in conversational memory goes that far: once you need it you've usually crossed into the bucket-3 / enterprise problem. [cognee](https://www.linkedin.com/company/cognee-ai/) *(open-source)* is reaching toward it: a graph+vector engine built against plain RAG, with an optional ontology layer that grounds the graph against a real schema. On the hosted side, [Zep AI](https://www.linkedin.com/company/zep-ai/) sits here too, and adds temporal context, modeling factual validity: "true from / true until".

### 2\. Institutional Knowledge

*(the docs, chats, notes and transcripts you already live in)*

This is the bucket most people actually mean. The context isn't in a clean database, it's scattered across the apps where work happens: Drive, Slack, Notion, Granola, email, and the assistant you talk to (Claude, ChatGPT). The job is to make that mess usable to an agent.

The defining dynamic here is a land-grab: **almost everyone is trying to be the unifier:** the layer that sits on top of your scattered unstructured data so agents query *them*, and everything else connects underneath. Slack says it out loud; Notion makes the same claim from the other side.

They're coming at it from two directions. **Surface-owners** already own a place where context gets *created* and add connectors to pull in the rest; **Neutral layers** own no surface of their own and just index across everything. The bet is different: surface-owners lead with distribution and native data, neutral layers with breadth and not competing with your tools.

**Surface-owners** — [Slack](https://www.linkedin.com/company/tiny-spec-inc/) (conversation), [Notion](https://www.linkedin.com/company/notionhq/) (docs/wiki), [Granola](https://www.linkedin.com/company/meetgranola/) (meetings), Claude / ChatGPT (assistant). Work already happens there, so they have the data natively; most now expose it to outside agents via MCP.

**Neutral layers:** own no surface of their own and index across everything. They fall on the same spine as bucket 1 — how much they model, from plain retrieval to a real graph:

- **Pure RAG — index and fetch.** Connect the sources, retrieve the relevant bits, no model of how anything connects. [**Onyx AI**](https://www.linkedin.com/article/edit/7467965747697238018/#) is the open-source reference here (MIT, 40+ connectors, self-hostable, hybrid vector + keyword search). **GoSearch** sits alongside it but federated-first: instead of copying everything into a central index, it queries data where it lives: Lighter but typically more limited in what it can rank or reason over, because there's no unified index to work from.
- **Hybrid — retrieval plus light structure.** Still retrieval at its core, but with a semantic layer on top so agents act on the knowledge rather than just fetch it. [Dust](https://www.linkedin.com/article/edit/7467965747697238018/#) is the one here, agent-first, connecting Notion, Drive, GitHub, Slack, Salesforce... open-source core plus hosted.
- **Graph-native — model the company, not just the documents.** The agent doesn't just retrieve, it reads a graph of your entities and how they connect. [Glean](https://www.linkedin.com/article/edit/7467965747697238018/#) is the enterprise end: it builds a knowledge graph of people, projects and customers and their relationships, with entity resolution. The broadest connector library, permission-aware throughout. [Hyperspell](https://www.linkedin.com/article/edit/7467965747697238018/#) is the lighter, developer-facing take: a per-user context graph from connected accounts (Slack, Gmail, Notion, Drive), surfaced as one memory layer (also in bucket 1).

### 3\. Systems of record

*(structured + unstructured, across many systems)*

This is the hardest bucket, the only one where every problem shows up at once. The context spans structured sources (warehouses, transactional systems) and unstructured ones (docs, wikis, tickets), across systems that were never built to talk to each other. And it usually carries a requirement the other two buckets don't: governance, access control, lineage, auditability.

Like bucket 2, it splits into **surface-owners** and **neutral layers** — but here the surface-owners can't win the bucket on their own.

**Surface-owners —** **own the structured layer.** They want to own the *structured* layer the way Slack and Notion own the unstructured one: Your data already lives in us, governed in place, point your agents here. But the warehouse holds your tables, not your docs, your Slack, your tickets — and it doesn't connect the two worlds. So they solve the structured half cleanly and leave the rest untouched. They can own their layer and still not solve the full problem. [Snowflake](https://www.linkedin.com/company/snowflake-computing/),[Databricks](https://www.linkedin.com/company/databricks/), and [Microsoft Fabric](https://www.linkedin.com/company/microsoft-fabric-world/) are the three; **dbt** and **Cube** add a semantic layer defining what the metrics *mean*, still structured-only.

**Neutral layers — connect across both worlds.** The only camp that can actually solve the full bucket: they own no data, they sit on top of structured *and* unstructured and build one model an agent reads across them. Same as the other buckets, they sort by **how much they actually model** — from lightly cataloging what things mean to fully modeling the business. (One property worth tagging: whether a tool *centralizes* or *federates*, leaving data where it lives and querying in place.)

- [Atlan](https://www.linkedin.com/company/atlan-hq/) — the lightest: it models the *metadata*, not the business. It unifies what everything *means* across your stack — definitions, ownership, lineage, policy — into one governed layer an agent reads to know what exists and what it's allowed to touch. Covers structured and unstructured, but at the level of meaning, not the entities themselves.
- [Palantir Technologies](https://www.linkedin.com/company/palantir-technologies/) **Foundry** **\+ AIP** *(centralizes)* — the heavyweight and the reference: a full ontology mapping data to real operational objects, with governance and audit by design.
- [Edra](https://www.linkedin.com/company/edra-ai/) *(centralizes)* — the automated take: built by the creators of Palantir's FDE role, it reverse-engineers how the business runs from its data exhaust into a self-updating model.
- [Modern Relay](https://www.linkedin.com/company/modern-relay/) *(centralizes)* — a "context graph" that models your operations (people, policies, data, decisions) in code, but runs entirely on infrastructure you own: the anti-lock-in answer to Palantir. Leans into multi-agent coordination: governing writes and approvals when several agents act on the same state. (Open-source core, Omnigraph.)
- [Stardog](https://www.linkedin.com/company/stardog-union/) *(centralizes / can virtualize)* — RDF/OWL knowledge graph for reasoning across connected data at query time; the established own-it-yourself option.
- [Timbr.ai](https://www.linkedin.com/company/timbr-ai/) *(federates)* — ontology depth for SQL-native teams, sitting over your existing sources without rebuilding the stack.
- [Prometheux](https://www.linkedin.com/company/prometheux/) *(federates)* — makes an ontology operational across your existing databases and warehouses, no migration.
- [Denodo](https://www.linkedin.com/company/denodo-technologies/) *(federates)* — general-purpose data virtualization; the broad "query in place" case.
- [Vega](https://www.linkedin.com/company/vega-security-io/) *(federates)* — the same federated idea, security-specific for now.

That's the map. Its job is to tell you how far up the stack you actually need to go: just the agent's own context, that plus your institutional knowledge, or all the way to your systems of record. The common mistake is getting the level wrong in either direction: overshooting into bucket-3 when files and retrieval would have carried you, or undershooting and starving an agent of the context it actually needs. Either way it's the application layer on top that pays for it: build too thin and the agent can't do the job, too heavy and you're maintaining an ontology to answer questions a vector search could have handled. Find your level first, and build for it.

And there's still the piece none of them fully reach: the most valuable context in any company was never written down: the workarounds, the real escalation paths, the judgment in people's heads. Hardest to capture, and probably where the deepest moat sits. That's a whole post on its own.:)

Whatever bucket you're in, trying to solve this is the right instinct — there's no real AI company without it. We've been deep in it ourselves, and we're always happy to talk it through.