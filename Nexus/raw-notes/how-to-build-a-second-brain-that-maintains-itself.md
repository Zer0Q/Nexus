---
title: "How to Build a Second Brain That Maintains Itself"
source: "https://x.com/Axel_bitblaze69/status/2059053069762228313"
author:
  - "[[@Axel_bitblaze69]]"
published: 2026-05-26
created: 2026-05-31
description: "Your AI is brilliant. But every great answer it gives you dies in chat history.Try finding what Claude told you 3 weeks ago about that token..."
tags:
  - "clippings"
---
![Imatge](https://pbs.twimg.com/media/HJM5dsHakAAWinE?format=jpg&name=large)

Your AI is brilliant. But every great answer it gives you dies in chat history.

Try finding what Claude told you 3 weeks ago about that token thesis. Try asking GPT what you discussed last quarter about anything. The conversation ends, the insight ends with it.

but there's a setup that fixes this.

This AI reads your sources, organizes them into a personal wiki on your machine, and keeps it current.. automatically. You stop losing the work AI does for you.

I went deep on this over the last two weeks and built a working setup from scratch. The graph view alone surfaces connections between articles I would have missed manually.

In this guide, I'll walk you through what this setup is, how to build it in under 10 minutes, the 5 workflows that make it self-maintaining, and what your knowledge stack looks like 90 days in.

By the time you're done, you'll have a personal knowledge base that gets sharper every time you use it.

Let's get into it.

𝗪𝗵𝗮𝘁 𝗶𝘀 𝗮 𝗦𝗲𝗹𝗳-𝗠𝗮𝗶𝗻𝘁𝗮𝗶𝗻𝗶𝗻𝗴 𝗦𝗲𝗰𝗼𝗻𝗱 𝗕𝗿𝗮𝗶𝗻?

𝗜𝗻 𝗼𝗻𝗲 𝗹𝗶𝗻𝗲: Obsidian is your second brain on disk. AI is the librarian that reads, organizes, and queries it for you.

Most AI chats are like talking to someone with amnesia. You explain something, they answer, the conversation ends, the knowledge disappears.

This setup is different. The AI reads your sources, builds a structured wiki of markdown files, and updates it every time you add something new. Knowledge gets compiled once and kept current.. not re-derived on every query.

For example: drop 6 months of articles, podcasts, and X posts about Ethereum into your vault.

The AI reads each one, creates pages for Restaking, Validators, Layer 2s, cross-references everything, and surfaces narrative shifts when you ask. A single ingest touches 10-15 pages in one pass.

Think of it this way: Obsidian is where you read. The AI is who writes. The wiki is what gets built.

𝗛𝗼𝘄 𝘁𝗼 𝗦𝗲𝘁 𝗨𝗽 𝗬𝗼𝘂𝗿 𝗩𝗮𝘂𝗹𝘁 𝗶𝗻 <𝟭𝟬 𝗠𝗶𝗻𝘂𝘁𝗲𝘀

This is the part to bookmark. Every working setup follows the same shape.

𝗦𝘁𝗲𝗽 𝟭: Download Obsidian (obsidian.md). Free, local-first, works offline.

𝗦𝘁𝗲𝗽 𝟮: Create a new vault on your desktop. Call it whatever fits.. research-vault, alpha-vault, brain.

𝗦𝘁𝗲𝗽 𝟯: Inside the vault folder, build this exact structure:

```text
your-vault/
├── raw/                    ← source files you collect
├── wiki/
│   ├── entities/          ← people, projects, tokens, accounts
│   ├── concepts/          ← frameworks, narratives, theses
│   ├── sources/           ← AI-written summaries of raw files
│   └── analysis/          ← your queries-turned-pages
├── hot.md                 ← rolling 500-char context cache
├── index.md               ← live catalog of everything
├── log.md                 ← chronological action log
└── CLAUDE.md              ← schema + rules for the AI
```

𝗦𝘁𝗲𝗽 𝟰: Inside CLAUDE.md, paste this template (this is the brain of your vault every AI session reads this first):

```text
𝗖𝗟𝗔𝗨𝗗𝗘.𝗺𝗱 — 𝗠𝘆 𝗞𝗻𝗼𝘄𝗹𝗲𝗱𝗴𝗲 𝗩𝗮𝘂𝗹𝘁

𝗜𝗱𝗲𝗻𝘁𝗶𝘁𝘆
I work on AI tools and crypto markets. My focus:
- Daily alpha research from X and on-chain sources
- AI workflows (Claude, agents, prompting)
- Content creation and trading research

𝗩𝗮𝘂𝗹𝘁 𝗔𝗿𝗰𝗵𝗶𝘁𝗲𝗰𝘁𝘂𝗿𝗲
- raw/ — Source documents (immutable, never modify)
- wiki/entities/ — People, projects, tokens, X accounts
- wiki/concepts/ — Frameworks, narratives, theses
- wiki/sources/ — Your summaries of raw files
- wiki/analysis/ — Queries-turned-pages worth keeping
- hot.md — Rolling cache of recent context (500 chars max)
- index.md — Live catalog of all wiki pages
- log.md — Append-only record of all actions

𝗖𝗼𝗻𝘃𝗲𝗻𝘁𝗶𝗼𝗻𝘀
- Kebab-case filenames (andrej-karpathy.md, not "Andrej Karpathy.md")
- YAML frontmatter on every wiki page:

  type: entity | concept | source | analysis
  created: YYYY-MM-DD
  tags: [tag1, tag2]

- Use [[wiki-links]] for every cross-reference. Non-negotiable.
- Every page ends with a ## Sources section linking back to raw/

𝗢𝗽𝗲𝗿𝗮𝘁𝗶𝗼𝗻𝘀

𝗜𝗻𝗴𝗲𝘀𝘁
When I drop a source in raw/:
1. Read carefully, extract entities + concepts
2. Create new pages for anything not yet in wiki/
3. Update existing pages with new claims
4. Create wiki/sources/[name].md summary
5. Update index.md and log.md
A single ingest touches 5-15 pages.

𝗤𝘂𝗲𝗿𝘆
1. Check hot.md first for recent context
2. Read index.md for relevant pages
3. Follow [[links]] to drill in
4. Synthesize with citations like (see [[entity-name]])
5. If non-trivial, save to wiki/analysis/

𝗟𝗶𝗻𝘁
- Find contradictions, orphans, stale claims, missing pages
- Output to wiki/analysis/[date]-lint-report.md

𝗛𝗼𝘁 𝗖𝗮𝗰𝗵𝗲 𝗨𝗽𝗱𝗮𝘁𝗲
After every meaningful session, update hot.md with:
[date] | [topic] | [key facts discussed in 500 chars max]

𝗢𝗽𝗲𝗿𝗮𝘁𝗶𝗻𝗴 𝗥𝘂𝗹𝗲𝘀
- Never delete files. Use status: archived in frontmatter.
- Never edit raw/ files. They are sources of truth.
- Always cite sources at the bottom of wiki pages.
- When uncertain about placement, use wiki/analysis/ and flag it.

𝗦𝘁𝘆𝗹𝗲 𝗳𝗼𝗿 𝗚𝗲𝗻𝗲𝗿𝗮𝘁𝗲𝗱 𝗖𝗼𝗻𝘁𝗲𝗻𝘁
- Concise. One claim per sentence.
- No corporate jargon. No "let's dive in."
- Parallel structure ("A. B. C.") liberally.
```

𝗦𝘁𝗲𝗽 𝟱: Install the Obsidian Web Clipper Chrome extension. Set the default folder to raw/. Now you can clip any web article into your vault with one click.

𝗦𝘁𝗲𝗽 𝟲: Open Claude Code in your terminal and cd into the vault folder. Run:

```text
"Read my CLAUDE.md. Then guide me through ingesting my first source."
```

Claude reads your CLAUDE.md and walks you through the rest. Total setup time: under 10 minutes.

𝗧𝗵𝗲 𝟱 𝗪𝗼𝗿𝗸𝗳𝗹𝗼𝘄𝘀 𝗧𝗵𝗮𝘁 𝗠𝗮𝗸𝗲 𝗜𝘁 𝗦𝗲𝗹𝗳-𝗠𝗮𝗶𝗻𝘁𝗮𝗶𝗻𝗶𝗻𝗴

The vault only compounds if you actually run it. Five workflows handle everything.

Listed in reverse order. #1 is where the real leverage lives.

#𝟱: 𝗜𝗻𝗴𝗲𝘀𝘁

Drop a source into raw/. Tell the AI to process it.

The AI reads the source, extracts entities and concepts, creates new wiki pages, updates existing ones, and logs the action. A single ingest touches 10-15 wiki pages.

Try this:

```text
"I just clipped a Vitalik post about staking economics 
into raw/. Ingest it following the CLAUDE.md conventions."
```

#𝟰: 𝗤𝘂𝗲𝗿𝘆

Ask questions across the entire vault.

The AI checks hot.md for recent context, reads index.md for relevant pages, follows backlinks, and synthesizes an answer with citations. Good answers get filed back as new pages under wiki/analysis/.

Try this:

```text
"What's the consensus on Restaking across my saved sources
in the last 30 days? Cite specific pages. Save the answer
to wiki/analysis/restaking-may-consensus.md."
```

#𝟯: 𝗟𝗶𝗻𝘁

Weekly health check on the vault.

The AI scans for contradictions between pages, orphan pages with no links, stale claims, and concepts mentioned in passing but lacking their own page. Output is a lint report.

Try this:

```text
"Run a lint pass on the vault. Save findings to
wiki/analysis/2026-05-26-lint-report.md. Flag the top
3 most important gaps to fill this week."
```

#𝟭: 𝗧𝗵𝗲 𝗛𝗼𝘁 𝗖𝗮𝗰𝗵𝗲

The most underrated piece in the entire setup.

That hot.md file in your vault root is a rolling 500-character cache of your most recent context.. the topic you're focused on, the last thing you ingested, the question you just asked.

For routine queries, the AI checks hot.md first instead of crawling the full wiki. Cuts token usage on day-to-day queries by 80-90%.

The CLAUDE.md template above already has the "Hot Cache Update" rule baked in. The AI maintains it automatically after every meaningful session.

Stack the five. Ingest feeds Query. Query feeds Lint. Lint surfaces the next Ingest. Your vault sharpens itself.

𝗣𝗿𝗼 𝗧𝗶𝗽𝘀 𝗮𝗻𝗱 𝗖𝗼𝗺𝗺𝗼𝗻 𝗠𝗶𝘀𝘁𝗮𝗸𝗲𝘀

A few things worth knowing before you start.

𝗣𝗿𝗼 𝘁𝗶𝗽: One page = one claim. Atomic notes beat essays. Cross-referencing works 2-3x better when each page is tightly focused.

𝗣𝗿𝗼 𝘁𝗶𝗽: Install the Dataview plugin. Add YAML frontmatter to wiki pages. Dataview turns frontmatter into dynamic tables — "all active projects with deadlines this month" becomes a one-line query.

𝗣𝗿𝗼 𝘁𝗶𝗽: The vault is just a git repo. Run git init in the folder. Commit daily. Free version history and instant rollback when the AI does something weird.

𝗠𝗶𝘀𝘁𝗮𝗸𝗲: Never manually edit files inside wiki/. That's the AI's layer. If you want to add information, drop it in raw/ or update CLAUDE.md.

𝗠𝗶𝘀𝘁𝗮𝗸𝗲: One mega memory file. Split into one file per workflow.. memory-trading.md, memory-content.md, memory-research.md. Easier to inject only what's relevant.

𝗠𝗶𝘀𝘁𝗮𝗸𝗲: Skipping the weekly lint. Without it, your wiki silently rots. Set a Sunday calendar reminder.

𝗞𝗲𝗲𝗽 𝗶𝗻 𝗺𝗶𝗻𝗱: This setup works beautifully up to a few hundred notes. Past 500K total tokens, plain markdown search starts hitting a wall on multi-hop questions. When queries start returning generic answers or you find yourself searching for things you know are in the vault, that's the signal to graduate to a graph-based setup. But that's a problem for month 6, not day 1.

𝗪𝗵𝗮𝘁 𝟵𝟬 𝗗𝗮𝘆𝘀 𝗜𝗻 𝗔𝗰𝘁𝘂𝗮𝗹𝗹𝘆 𝗟𝗼𝗼𝗸𝘀 𝗟𝗶𝗸𝗲

Here's the timeline if you ship this weekend:

𝗗𝗮𝘆 𝟬 (𝘁𝗼𝗱𝗮𝘆): Set up the vault. 10 minutes.

𝗪𝗲𝗲𝗸 𝟭: Ingest 3-5 sources. Get used to dropping articles into raw/ and asking the AI to process them.

𝗪𝗲𝗲𝗸 𝟰: 30-50 sources. Patterns start emerging in the graph view. The AI starts surfacing connections you didn't know existed.

𝗗𝗮𝘆 𝟵𝟬: 200+ cross-referenced sources. Your daily alpha brief is generated from a knowledge network the AI maintains. Questions that used to take 30 minutes of scrolling take 30 seconds. The AI knows your voice, your watchlist, your trading biases. The vault is the smartest version of you that's ever existed.

That's the moat. not the markdown files, the network of relationships between them that you couldn't possibly maintain manually.

Build the foundation this weekend. The compounding starts the first time you ingest something.

I hope you found this guide valuable.

If you did, be sure to follow me [@axel\_bitblaze69](https://x.com/@axel_bitblaze69) I post articles like this on AI and crypto 2-3x/week.

Lastly, if you can, please Like/Repost this article so others can find it. 💙