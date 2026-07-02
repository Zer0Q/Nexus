---
title: "15 LEVELS OF HERMES AGENT. FROM CHATBOT TO 24/7 AUTONOMOUS SYSTEM."
source: "https://x.com/IBuzovskyi/status/2068629714776756339"
author:
  - "[[@IBuzovskyi]]"
published: 2026-06-21
created: 2026-06-22
description: "Most people install Hermes Agent and use it as a chatbot. They type a prompt, get a response, close the tab. That covers maybe 10% of what t..."
tags:
  - "clippings"
summary:
---
![Imatge](https://pbs.twimg.com/media/HLU_q3TXUAAmoT2?format=jpg&name=large)

Most people install Hermes Agent and use it as a chatbot. They type a prompt, get a response, close the tab. That covers maybe 10% of what the agent can do.

This article maps every level of Hermes Agent usage, from the first prompt to a system that runs your business without you. 15 levels, grouped into three phases. Each level builds on the one before it, but you can jump to any level that fits your setup.

The structure is the same for every level: what it is, what it unlocks, how to set it up, and the mistake that trips people up at that stage.

All technical details verified against Hermes Agent v0.17.0 official documentation and source code.

Subcribe to my SubStack for more articels: [https://substack.com/@yanxbt](https://substack.com/@yanxbt)

![Imatge](https://pbs.twimg.com/media/HLU_OblWgAAIdhJ?format=jpg&name=large)

## PHASE 1 — FOUNDATION (Levels 1-3)

You are using Hermes. The agent responds to what you ask.

**LEVEL 1 — ONE-SHOT PROMPTS**

**What it is:** You installed Hermes. You type prompts. The agent responds with tool calls, file edits, web searches, terminal commands. Basic interaction.

**What it unlocks:** Hermes executes tasks across your file system, terminal, and the web. It reads files, writes code, searches the internet, runs shell commands. It does things. A chatbot talks about things.

**Setup:**

Desktop app: download from [hermes-agent.nousresearch.com](https://hermes-agent.nousresearch.com/). One-click install. CLI: **hermes setup**

Three setup modes: → Quick Setup (Nous Portal): OAuth login, model + Tool Gateway in one command → Full Setup: walk through every provider, tool, and option yourself → Blank Slate: everything starts OFF except provider, model, file tools, and terminal. No web search, no browser, no memory, no delegation, no cron, no skills, no plugins, no MCP. You enable only what you need. Nothing loads that you didn't choose, even after updates.

Blank Slate is the cleanest starting point for users who want full control over what the agent can and cannot do.

Connect a model provider. Start chatting.

**The mistake:** Treating Hermes as a search engine. "Tell me about X" wastes an agent that can DO things. "Research X, write a report, save it to ~/reports/" uses the tools.

**Example:** "research the top 5 CRMs for solo founders, compare pricing and features, save a report to ~/reports/crm-comparison.html" — agent searches, compares, writes the file. done in 3 minutes.

**LEVEL 2 — MEMORY + SOUL.MD**

**What it is:** Hermes remembers you across sessions. SOUL.md defines who the agent is. MEMORY.md and USER.md store durable facts about your projects, preferences, and business context.

**What it unlocks:** The agent stops asking you to re-explain things. Two people asking the same question get different answers because Hermes knows their different contexts. Your instructions, preferences, and business details persist across every session.

v0.17.0 added atomic memory operations: the agent can batch add, replace, and remove memory entries in one call. Memory updates no longer fail mid-edit when the budget is tight.

**Setup:**

Desktop app / Dashboard: Profile → SOUL.md → edit CLI: open **~/.hermes/SOUL.md** in any editor

Write 50-80 lines covering identity, voice, operations, and restrictions. The agent reads this on every session start.

**The mistake:** Leaving SOUL.md empty and expecting personalized output. Hermes without a SOUL.md is generic by design. The identity file is the difference between a general assistant and YOUR assistant.

**Example:** you ask "should I raise prices?" Without SOUL.md: generic advice about pricing strategy. With SOUL.md containing your business model, margins, and customer segments: "your entry tier converts at 12%. raising it $10 risks churn in segment B where you have 60% of revenue. test on segment A first."

> 11 de juny

**LEVEL 3 — SLASH COMMANDS**

**What it is:** Commands that change how the agent works mid-session. Most users never type these.

**What it unlocks:** Parallel work inside a single session. You stop waiting for one task to finish before starting the next.

**The commands:**

/background \<prompt> Fires a task in the background. Your main session stays free. Result appears as a panel when done.

/steer \<prompt> Injects a message into the current run without interrupting it. Redirects the agent mid-execution.

/queue \<prompt> Queues a follow-up. Waits until the current task finishes, then runs automatically.

/model \<name> Switches models mid-session. Start with Sonnet for planning. Switch to DeepSeek for execution. Switch to Opus for review.

v0.17.0 added grok-composer-2.5-fast via Grok OAuth: the 200K context coding model behind Cursor's Composer, accessible through your Grok subscription.

**Configure default behavior when you type while the agent is busy:**

set in Desktop app, Dashboard, or config.yaml:

> display: busy\_input\_mode: steer # or queue, or interrupt

**The mistake:** Not knowing these exist. Most users type a prompt, wait for it to finish, type another prompt. /background alone doubles your throughput per session.

**Example:** you're drafting a proposal. mid-session: **/background research \[competitor\] pricing and positioning**. you keep writing. 5 minutes later a panel appears with the competitive analysis. you paste it into the proposal without breaking flow.

## PHASE 2 — LEVERAGE (Levels 4-7)

Hermes works smarter. You stop doing tasks the agent can handle.

**LEVEL 4 — SKILLS + RIGHT MODEL PER SKILL**

**What it is:** Skills are on-demand knowledge documents and tool collections the agent loads when needed. Each skill can run on a different model.

**What it unlocks:** The agent becomes a specialist on demand. A research skill loads research methodology. A code review skill loads security patterns. Each skill uses the model best suited for its job.

**Setup:**

Desktop app / Dashboard: Skills Hub → Browse → Install CLI: **/skills search \[topic\]**

v0.17.0 rehauled the Skills Hub: connected hubs (OpenAI, Anthropic, HuggingFace, NVIDIA), featured section, full skill previews before install, and security scan on each skill.

v0.17.0 also added image editing: image\_generate now edits source images ("make this logo blue", "remove the background"). Same tool, new mode.

Assign a model per skill in the Desktop app or config.yaml:

research/web search → DeepSeek V4 Flash ($0.10/M tokens, cheapest) code review → Claude Opus 4.8 ($5/$25/M, best coding benchmarks) content writing → Claude Sonnet 4.6 ($3/$15/M, strongest prose + tool calling) coding (value) → GPT-5.5 ($2/$12/M, #1 Chatbot Arena, 2M context) research with grounding → Gemini 2.5 Pro ($1.25/$10/M, Google Search built in) bulk sub-agent work → DeepSeek V4 ($0.30/$0.50/M, 90% cache discount) /goal judge → Gemini Flash (cheapest, fast enough for binary done/not-done) self-hosted (free) → Qwen 3 8B via Ollama (8GB RAM, handles routine tasks)

MiniMax M2.7 is also worth testing. Nous Research and MiniMax are collaborating to optimize future releases for Hermes. One of the most-used models inside Hermes as of mid-2026.

**The mistake:** Running every skill on your most expensive model. A routine web search skill burning Opus tokens is money wasted. Match model cost to task complexity.

**Example:** you run a competitive research skill on DeepSeek V4 Flash instead of Opus 4.8. comparable quality for web search. 30-50x cheaper per call. over 30 runs a month the savings add up fast.

**LEVEL 5 — MCPs (CONNECT YOUR WORLD)**

**What it is:** MCP (Model Context Protocol) servers connect Hermes to external tools. Gmail, Calendar, Notion, Slack, ClickUp, GitHub, databases, APIs.

**What it unlocks:** The agent works with YOUR data, not just the open web. It reads your emails, checks your calendar, pulls from your project board, and answers questions using context from the tools you already use.

**Setup:**

Desktop app / Dashboard: MCP → Catalog → browse and install CLI: **hermes mcp**

**The mistake:** Connecting 15 MCPs at once. Every MCP adds tool schemas to the context window. 15 MCPs with 10 tools each = 150 tool definitions the model reads every turn. Install what you use. Disable what you don't. Tool Search (auto-enabled when schemas eat 10%+ context) helps manage this, but fewer MCPs is still better.

**Example:** "what happened in Slack this week while I was heads-down coding?" Agent reads your Slack channels, filters by mentions and key topics, cross-references with your goals in memory. delivers a 10-line summary. no tab switching. no scrolling through 200 messages.

**LEVEL 6 — SUB-AGENTS + PARALLEL EXECUTION**

**What it is:** delegate\_task spawns isolated sub-agents with their own context window, terminal session, and toolset.

**What it unlocks:** Parallel work across multiple agents. One researches. One critiques. One codes. Parent orchestrates. Each child can run a different model.

**Setup:**

The agent uses delegate\_task automatically when the task benefits from isolation. You can also ask directly:

"spin up a sub-agent on DeepSeek to research X while another on GPT-5.5 critiques the findings"

**Configuration:**

set in Desktop app, Dashboard, or config.yaml:

> delegation: max\_concurrent\_children: 3 # default max\_spawn\_depth: 2 # bounds recursion

**Roles:**→ leaf (default): executes, cannot re-delegate → orchestrator: can spawn its own workers

**Background mode (v0.17.0):**delegate\_task(background=true) dispatches the sub-agent and returns immediately. Your session stays live. Result re-enters as a new turn when it finishes.

**The mistake:** Using sub-agents for simple tasks. Delegation has overhead (context setup, tool allocation). A task the main agent can handle in 3 turns should not spawn a sub-agent.

**Example:** "research three competitors in parallel. one agent per competitor. use DeepSeek for research. parent on Sonnet synthesizes all three." three reports in 10 minutes instead of 30. each agent works isolated so one slow research task doesn't block the others.

**LEVEL 7 — ASYNC OPERATIONS**

**What it is:** Three features that let Hermes work without you typing.

**What it unlocks:** The shift from "I ask, it responds" to "it works, I review."

**/goal — persistent objectives:**Set a goal. A judge model evaluates after every turn: done or not done? Agent continues automatically until the goal is achieved, you pause it, or the turn budget (default 20) runs out.

> /goal find 100 clinics in Toronto, build a landing page for each, draft personalized emails to each clinic.

/subgoal adds criteria mid-run without resetting the loop.

**Cron jobs — scheduled tasks:**Gateway ticks every 60 seconds. Fires due jobs in fresh isolated sessions. Delivers results to 27+ platforms: Telegram, Discord, Slack, WhatsApp, Signal, Matrix, iMessage, Microsoft Teams, Google Chat, LINE, email, SMS, and more.

v0.17.0 additions: → WhatsApp Business Cloud API (official Meta adapter, no QR bridge) → iMessage via Photon Spectrum (no Mac relay needed) → Telegram rich messages (Bot API 10.1, native formatting) → Automation Blueprints: one-click cron templates in the Dashboard (morning briefing, weekly review, news digest, reminder). No cron syntax needed.

Three cost layers: → no\_agent mode: script IS the job, $0 forever → wakeAgent gate: script decides if LLM is needed, $0 until something changes → context\_from: chain job outputs into pipelines without a framework

**Safety net — checkpoints:**Enable checkpoints before running autonomous operations. The agent snapshots your working directory before changes. **/rollback** restores state if something goes wrong overnight.

set in Desktop app, Dashboard, or config.yaml:

> checkpoints: enabled: true

**The mistake:** Writing vague cron prompts. Every cron run starts from zero. No memory, no chat history. "Check on that server issue" means nothing. "SSH into 10.0.0.5, check nginx status, verify port 443 returns 200" works.

**Example:** 8:00 AM. Telegram pings. You didn't ask for this. Cron delivered it: "3 new arXiv papers in your niche. competitor updated their pricing page. GitHub repo you watch merged a breaking change. action: review competitor pricing before your 11am call."

> 14 de juny

## PHASE 3 — AUTONOMY (Levels 8-15)

Hermes works without you. The system compounds over time.

**LEVEL 8 — MULTI-PROFILE ARCHITECTURE**

**What it is:** Separate Hermes profiles, each with its own SOUL.md, config, memory, skills, cron jobs, and model. Fully isolated agents on one machine.

**What it unlocks:** Specialized workers instead of one overloaded generalist. A Scout profile finds signals. An Analyst profile synthesizes research. A Coder profile ships features. Each does one job well with the right model for that job.

**Setup:**

Desktop app / Dashboard: Profiles → Build (5-step wizard: Identity → Model → Skills → MCPs → Review) CLI: **hermes profile create \[name\]**

Each profile becomes its own command:

> hermes -p scout chat hermes -p analyst chat

**The mistake:** Giving every profile the same SOUL.md. The entire point is isolation. A Scout that tries to analyze wastes tokens. An Analyst that tries to find sources duplicates Scout's work. One job per profile.

**Example:** Scout found 12 sources overnight. Analyst synthesized them into 4 wiki entries by 10am. Briefer delivered a 5-bullet summary at 8am. You read it over coffee. None of them share memory. Each did one job with the right model for that job.

> 17 de juny

**LEVEL 9 — SELF-IMPROVING KNOWLEDGE BASE**

**What it is:** The LLM Wiki skill, based on Andrej Karpathy's pattern. A self-improving knowledge base built as interlinked markdown files. Ships bundled with Hermes.

**What it unlocks:** Long-term knowledge that compounds beyond the memory cap. Hermes's built-in memory handles conversational context. The wiki handles domain knowledge: articles, transcripts, meeting notes, research findings. Cross-references stay linked. Contradictions get flagged automatically.

**Setup:**

set in Desktop app, Dashboard, or config.yaml:

> WIKI\_PATH=~/obsidian-wiki

On first run, the skill asks for your domain to build SCHEMA.md with the right tag taxonomy.

Connect to Obsidian for graph view: set OBSIDIAN\_VAULT\_PATH to the same directory.

Feed it: "index this article into my wiki: \[paste URL or text\]"

**The mistake:** Never feeding the wiki. An empty knowledge base adds nothing. The value comes from accumulation. Month 1: 50 entries. Month 3: 300+ entries with cross-references. The agent gets sharper because the knowledge base got sharper.

**Example:** you ask "how does competitor X handle onboarding?" Without wiki: agent searches the web, gives you generic info. With 3 months of wiki entries: agent pulls your own research notes, meeting transcripts where a client mentioned competitor X, and an article you indexed last month. answer includes context no web search could find.

**LEVEL 10 — KANBAN ORCHESTRATION**

**What it is:** A durable SQLite task board shared across all profiles. Statuses flow from triage → todo → ready → running → blocked → done → archived. Dispatcher fires every 60 seconds.

**What it unlocks:** Complex multi-step projects with dependency chains. Each card can run its own /goal loop (goal\_mode). Cards with unfinished parent cards wait automatically. Multiple profiles pick up cards assigned to them.

**Setup:**

> /kanban create "Research 100 clinics" \\ --assignee scout --goal --goal-max-turns 15 /kanban create "Build landing pages" \\ --assignee coder --goal --goal-max-turns 20 \\ --depends-on "Research 100 clinics"

CLI: **hermes kanban** or **/kanba**n in chat.

**Kanban vs cron vs delegate\_task:**→ Kanban: durable work queue, persists across restarts, multi-profile → Cron: time-based scheduling, repeating tasks → delegate\_task: one-off parallel execution within a session

**The mistake:** Using Kanban for simple linear pipelines. Three profiles in a straight line (Scout → Analyst → Briefer) work fine with file-based coordination. Kanban adds value when you have dependency trees, parallel branches, or 10+ tasks that need tracking.

**Example:** quarterly competitive analysis as a Kanban project. 12 cards: 3 competitors × 4 dimensions (pricing, features, positioning, hiring signals). pricing card depends on web scraping card. hiring card depends on LinkedIn research card. agents pick up work as dependencies clear. you review the final synthesized report.

**LEVEL 11 — VOICE MODE**

**What it is:** Speech-to-text and text-to-speech across all messaging platforms. Six STT providers, five TTS providers.

**What it unlocks:** Talk to Hermes through voice messages on Telegram, Discord, WhatsApp. The agent transcribes, processes, and can respond with synthesized speech. Full voice conversations without typing.

**STT providers:**→ faster-whisper (free, runs on-device) → local command wrapper → Groq (fast cloud) → OpenAI Whisper API → Mistral → xAI

**TTS providers:**→ Edge TTS (free, default) → ElevenLabs (best quality, paid) → OpenAI TTS → MiniMax → NeuTTS (free)

**The mistake:** Using expensive cloud STT for routine voice messages. Local faster-whisper handles most languages well and costs nothing. Save paid STT for complex audio or noisy environments.

**Example:** driving to a meeting. voice message on Telegram: "anything from last night's research I should know before my 11am call?" Agent responds with a 30-second audio summary. you listen instead of read. hands on the wheel.

**LEVEL 12 — BROWSER AUTOMATION**

**What it is:** Hermes can control a browser to navigate websites, fill forms, extract data, and interact with web applications.

**What it unlocks:** Tasks that require a browser session: scraping dynamic pages, filling web forms, interacting with tools that have no API. The agent sees the page and acts on it.

**Setup:**

Included in Tool Gateway for Nous Portal subscribers:

> hermes setup --portal

Or configure browser automation separately through the dashboard.

**The mistake:** Using browser automation for tasks that have an API. Browser automation is slower, more fragile, and more expensive than a direct API call. Use it only when no API exists.

**Example:** competitor has no public API. agent opens their pricing page via browser, extracts current plans and pricing, compares against last month's snapshot stored in your wiki. change detected: they dropped their free tier. flagged in your morning brief.

**LEVEL 13 — API SERVER**

**What it is:** Hermes exposed as an OpenAI-compatible HTTP endpoint. Full agent with tools, memory, and skills accessible via standard API format.

**What it unlocks:** Any frontend that speaks OpenAI format connects to Hermes as a backend: Open WebUI, LobeChat, LibreChat, ChatBox, custom applications, Excel integrations. The agent becomes an API you build on top of.

**Setup:**

set in Desktop app, Dashboard, or .env:

> API\_SERVER\_ENABLED=true API\_SERVER\_KEY=your\_secret\_key

Start the gateway: Desktop app / Dashboard: Gateway → Start CLI: **hermes gateway**

Endpoint: **http://127.0.0.1:8642/v1/chat/completions**

**Multi-user setup:** Create one profile per user on different ports. Each gets isolated config, memory, and skills.

**The mistake:** Exposing the API server to the public internet without authentication. The server binds to 127.0.0.1 by default. Access remotely via SSH tunnel, not public exposure. v0.17.0 added OAuth gate on every token-required endpoint and websocket auth for the dashboard.

**Example:** your competitive research runs as an API endpoint. a custom dashboard queries Hermes for the latest intel. your team sees competitive data on a live internal page. nobody opens Telegram. the data serves itself.

**LEVEL 14 — IDE INTEGRATION (ACP)**

**What it is:** Hermes runs as an ACP (Agent Communication Protocol) server inside VS Code, Zed, and JetBrains editors.

**What it unlocks:** Chat, tool activity, file diffs, and terminal commands render inside your editor. The agent works in your project directory with your editor's context. Same agent core, same tools, same memory as CLI and gateway.

**Setup:**

> hermes acp start

In VS Code: install the ACP extension, point it to Hermes.

**What ACP includes:**→ File tools: read\_file, write\_file, patch, search\_files → Terminal execution → Chat interface inside the editor → Approval prompts for dangerous commands

**What ACP excludes (by design):**→ Messaging delivery → Cron job management → Gateway-specific features

**The mistake:** Thinking ACP replaces the gateway. ACP is for coding sessions inside an editor. Gateway handles messaging, cron, and multi-platform delivery. Both run the same agent core underneath.

**Example:** coding a pricing page. inside VS Code you ask Hermes: "how does competitor X structure their tiers?" Agent checks your Obsidian wiki, finds your research notes, gives the answer. you adjust your design without opening a browser or Telegram.

**LEVEL 15 — PROFILE DISTRIBUTIONS**

**What it is:** Package your entire agent setup as a git repo. Anyone installs your agent with one command.

**What it unlocks:** Your agent becomes a product. Sell it. Share it with your team. Distribute it to clients. Everything transfers except API keys and personal memories.

v0.17.0 also introduced the RAFT Agent Network: connect Hermes to [raft.build](https://raft.build/) as an external agent. Wake-channel bridge with privacy by contract (wake payloads carry metadata only, never message bodies). Your agent can collaborate with agents on other machines.

**What a distribution contains:**

> distribution.yaml # manifest SOUL.md # identity config.yaml # model and provider settings skills/ # custom skills cron/ # scheduled jobs mcp.json # connected tools

**Install someone else's distribution:**

> hermes profile install [github.com/user/their-agent](https://github.com/user/their-agent)

**The mistake:** Including API keys or personal data in the distribution. Credentials stay per-machine. The distribution carries personality, skills, and workflows. The user brings their own keys.

**Example:** you built a research department with Scout, Analyst, Briefer. new team member joins. they run: **hermes profile install** [github.com/you/research-dept](https://github.com/you/research-dept)**.** they have your three profiles, wiki structure, cron jobs, and SOUL.md templates. they add their own API keys and Telegram bot. running in 10 minutes.

## ONE WORKFLOW, 15 EVOLUTIONS

Competitive research. Same task. Watch how it changes at every level.

Level 1: you type "what's new in AI agents this week?" and read a wall of text.

Level 2: agent already knows your niche and competitors from SOUL.md. same question, answer is filtered to YOUR market.

Level 3: /background research competitors while you draft a proposal. results appear without breaking your flow.

Level 4: research skill runs on DeepSeek V4 Flash. analysis skill runs on Sonnet. you stop paying Opus prices for web searches.

Level 5: agent checks Slack, email, and ClickUp BEFORE answering. "competitor launched yesterday. your team discussed it in [#product](https://x.com/search?q=%23product&src=hashtag_click)."

Level 6: three sub-agents research three competitors in parallel. each on DeepSeek. parent on Sonnet synthesizes. 10 minutes instead of 30.

Level 7: you stopped asking. cron job runs at 7am. wakeAgent gate: nothing changed = $0. competitor shipped an update = agent wakes, researches, delivers brief to Telegram. you read it over coffee.

Level 8: Scout profile finds signals every 3 hours. Analyst synthesizes at 10am. Briefer delivers at 8am. three profiles. one pipeline.

Level 9: findings go to Obsidian wiki. month 3: 300+ entries. the agent surfaces patterns you didn't ask about because the wiki found connections across sources.

Level 10: quarterly analysis runs as a Kanban project. 12 cards with dependency chains. agents pick up work as dependencies clear. you review the final report.

Level 11: driving to a meeting. voice message: "anything from last night's research?" Agent responds with audio. you listen instead of read.

Level 12: competitor has no API. agent opens their pricing page via browser, compares against last month's snapshot. change detected. flagged in your brief.

Level 13: research runs as an API endpoint. a custom dashboard queries it. your team sees competitive intel on a live page.

Level 14: coding a feature. inside VS Code you ask "how does competitor X handle this?" Agent answers from your wiki without leaving the editor.

Level 15: your research setup is a git repo. new team member runs one command. Scout, Analyst, Briefer, wiki structure, cron jobs. all installed in 10 minutes.

## TOKEN ECONOMICS: HOW TO RUN ALL 15 LEVELS WITHOUT BURNING MONEY

every level above 3 costs tokens. here are the controls that keep spending predictable.

**RIGHT MODEL PER TASK (Level 4+)**

not every task needs your most expensive model. web search = DeepSeek V4 Flash ($0.10/M). synthesis = Sonnet ($3/$15/M). final review = Opus 4.8 ($5/$25/M). assign models per skill, per profile, per cron job. see Level 4 for the full model-per-task reference.

**WAKEAGENT GATES (Level 7+)**

script runs every tick for free. checks if anything changed. nothing changed = agent never wakes = $0. the agent only spends tokens when there is work to do.

**NO\_AGENT MODE (Level 7+)**

when the script IS the job. uptime checks, disk alerts, file watchers. output goes directly to Telegram. zero LLM calls. zero tokens. ever.

**PRE-RUN SCRIPTS (Level 7+)**

script gathers data for free. output injected into the prompt as context. the model summarizes what the script fetched instead of burning tool calls to find the data itself.

**LEAN TOOL SETS (Level 5+)**

set --skills web,file per cron job. fewer tool schemas in context = smaller prompt = cheaper. a news digest job does not need browser, delegation, or kanban tools.

**TOOL SEARCH (Level 5+)**

auto-enabled when tool schemas eat 10%+ of context. replaces full tool definitions with 3 bridge tools. ~300 tokens instead of thousands. the agent discovers tools on demand instead of loading all at once.

**COMPRESSION THRESHOLD (Level 7+)**

set in Desktop app, Dashboard, or config.yaml:

> compression: threshold: 0.40 # default 0.50

fires context compression earlier. keeps long /goal runs and cron sessions within token budget even at 20+ turns.

**CURATOR — FREE BY DEFAULT (v0.17.0)**

deterministic skill pruning still runs for free. LLM-powered consolidation is now opt-in only:

set in Desktop app, Dashboard, or config.yaml:

> curator: consolidate: true # opt-in, default false

routine background curation costs zero tokens. enable consolidation only when your skill library needs deep cleanup.

**LOSSLESS DENSIFICATION (PR #47866 by teknium)**

search\_files results get compressed before reaching the model. same information. fewer tokens. merged into latest Hermes. run **hermes update**.

**AUXILIARY MODELS FOR JUDGE (Level 7+)**

the /goal judge runs after EVERY turn. route it to a cheap fast model.

set in Desktop app, Dashboard, or config.yaml:

> auxiliary: goal\_judge: provider: openrouter model: google/gemini-3-flash-preview

20 judge calls on Gemini Flash vs 20 on Opus = significant savings.

**BUDGET CAPS (all levels)**

set in Desktop app, Dashboard, or config.yaml:

> budget: daily\_max\_usd: 10 session\_max\_usd: 2 monthly\_max\_usd: 200

hard limits. the agent stops when it hits the cap. set these before enabling any cron job or /goal run.

**MONITOR SPENDING**

Desktop app / Dashboard: Usage tab shows per-profile breakdown. CLI: **/usage** in any session for per-session stats.

add "end with token spend this week" to Briefer prompts for weekly cost tracking in Telegram.

the pattern across all of these: push work off the expensive model onto free code, cheap models, and compressed context. the agent reasons. everything else runs for free.

**START WITH BLANK SLATE**

if you care about token control from day one, install with Blank Slate mode (**hermes setup** → Blank Slate). everything disabled except provider, model, file tools, terminal. add features one by one as you need them. nothing loads that you didn't explicitly enable. this is the cheapest and most controlled starting point.

## WHERE MOST PEOPLE STOP

Levels 1-2. They install Hermes, write a SOUL.md, and use it as a smart chatbot. The agent saves them 30 minutes a day.

The jump from level 3 to level 7 is where daily time savings go from minutes to hours. /background, skills with the right models, cron jobs with wakeAgent gates. These compound.

The jump from level 7 to level 10+ is where the agent stops being a tool and becomes a system. Multi-profile architecture, self-improving knowledge, Kanban orchestration. You review work that happened without you.

## HOW TO IDENTIFY YOUR CURRENT LEVEL

![Imatge](https://pbs.twimg.com/media/HLUa70xWsAAjxPY?format=png&name=large)

You do not need to reach level 15. Most solo founders operate well at levels 7-10. The levels above that solve specific problems: voice for mobile workflows, browser for tools without APIs, API server for custom integrations, IDE for coding, distributions for teams.

Pick the level that matches your bottleneck. Set up that one. Move to the next when it stops being enough.

## RELATED ARTICLES

- [HERMES AGENT SOUL.MD: WHY 50 LINES MATTER MORE THAN YOUR MODEL](https://x.com/IBuzovskyi/status/2065125711401062758?s=20) — Level 2 deep dive
- [HERMES AGENT BUILDS ITSELF WHILE YOU SLEEP](https://x.com/IBuzovskyi/status/2066145326780518736?s=20) — Level 7 deep dive
- [HERMES AGENT + NOTEBOOKLM + OBSIDIAN: 3-AGENT RESEARCH DEPARTMENT](https://x.com/IBuzovskyi/status/2067313826492547483?s=20) — Level 8-9 deep dive

## OFFICIAL SOURCES

- [Features Overview](https://hermes-agent.nousresearch.com/docs/user-guide/features/overview)
- [SOUL.md](https://hermes-agent.nousresearch.com/docs/user-guide/features/soul)
- [Skills](https://hermes-agent.nousresearch.com/docs/user-guide/features/skills)
- [Cron](https://hermes-agent.nousresearch.com/docs/user-guide/features/cron)
- [Delegation](https://hermes-agent.nousresearch.com/docs/developer-guide/delegation)
- [Goals](https://hermes-agent.nousresearch.com/docs/user-guide/features/goals)
- [Profiles](https://hermes-agent.nousresearch.com/docs/user-guide/profiles)
- [Kanban](https://hermes-agent.nousresearch.com/docs/user-guide/features/kanban)
- [Voice & TTS](https://hermes-agent.nousresearch.com/docs/user-guide/features/voice)
- [Browser Automation](https://hermes-agent.nousresearch.com/docs/integrations/browser)
- [API Server](https://hermes-agent.nousresearch.com/docs/user-guide/features/api-server)
- [ACP/IDE](https://hermes-agent.nousresearch.com/docs/user-guide/features/acp)
- [Profile Distributions](https://hermes-agent.nousresearch.com/docs/user-guide/profile-distributions)
- [Integrations Overview](https://hermes-agent.nousresearch.com/docs/integrations/)

All technical details verified against Hermes Agent v0.17.0 documentation.

[@NousResearch](https://x.com/@NousResearch) [@Teknium](https://x.com/@Teknium)