---
title: "10 Upgrades for your Hermes Agent"
source: "https://x.com/zaimiri/status/2062512177295090046"
author:
  - "[[@zaimiri]]"
published: 2026-06-04
created: 2026-06-04
description: "These are the upgrades that move Hermes from agent I chat with to system I can actually rely on every day.The whole point is simple:less..."
tags:
  - "clippings"
summary:
---
![Imatge](https://pbs.twimg.com/media/HJ9g_6oXYAANnMQ?format=jpg&name=large)

These are the upgrades that move Hermes from "agent I chat with" to "system I can actually rely on every day."

The whole point is simple:

- less re-explaining
- less tab-switching
- less manual checking
- less context lost between sessions

These are 10 Hermes Agent upgrades worth doing.

**Fast setup map:**

- Telegram gateway: 10 minutes.
- Obsidian vault: 5 minutes if the folder already exists.
- Skills: 20 minutes for the first real SOP.
- Memory cleanup: 15 minutes.
- Toolsets: 10 minutes per lane.
- Cron: 30 minutes for a quiet daily check.
- Profiles: 45 minutes for 2 agents.
- MCP: 60 minutes if credentials are ready.
- Webhooks: 90 minutes for the first GitHub or Stripe route.
- Kanban: 1 hour once multiple agents are involved.

Let's dive in:

## 1\. Connect an Obsidian vault

Start with the place your notes already live.

Hermes has an Obsidian skill that can read, search, create, edit, append, and link notes inside a vault.

That means your old notes, project logs, research files, SOPs, and decisions can become working material during a run.

Example commands:

"Search my vault for notes about MCP and turn them into a setup checklist."

"Append this decision to the project log and link it to the source."

"Find every note that mentions Telegram setup and pull out the failure points."

Setup detail:

Set \`OBSIDIAN\_VAULT\_PATH\` in your Hermes env.

If you skip this, Hermes can still be useful. It just keeps too much of the work trapped inside the current chat.

## 2\. Move Hermes into Telegram

This is usually the upgrade people feel first.

The terminal is great for deep work. It is awful for random incoming work.

A lot of real tasks arrive as:

voice notes

screenshots

links

files

half-written ideas

"remind me to check this later" messages

quick approvals

Telegram gives Hermes a normal daily interface.

You can send a voice memo from your phone, drop a screenshot, approve a command, or get a cron result without opening a shell.

Clean setup:

Create the bot with BotFather.

Add the token.

Allow your user or group.

Start the Hermes gateway.

Use Telegram topics for lanes like content, research, infra, or client work.

One gotcha: Telegram privacy mode can make a bot look broken in groups. If it only sees commands, mentions, or replies, check privacy mode or make it an admin.

## 3\. Turn repeat work into skills

Skills are where Hermes starts compounding.

A skill is a markdown SOP the agent can load when a task matches.

Use one for:

- GitHub PR reviews
- client handoffs
- research briefs
- content drafting
- invoice prep
- server checks
- PDF workflows
- weekly reports

A good skill has four parts:

- when to use it
- exact steps
- common failure points
- verification checks

Every repeated correction should become a skill patch.

If Hermes keeps forgetting your review style, write the review style once.

If Hermes solved a weird setup bug, save the fix.

If a content workflow has rules, make them explicit.

This is how an agent becomes less generic over time.

## 4\. Add persistent memory

Memory is for facts you do not want to repeat every week.

Keep it small.

**Good memory:**

- preferred tone
- stable project paths
- tool quirks
- personal boundaries
- client separation rules
- environment facts

**Bad memory:**

- temporary tasks
- old PR numbers
- stale deadlines
- session progress
- anything that expires next week

Hermes stores memory in compact files and injects it at the start of new sessions.

That makes a new chat less blank.

It can already know things like:

> "Keep Telegram receipts short."

> "Typefully is draft-only."

> "This repo uses this test command."

> "Never use client credentials for personal ops."

A small memory file beats a giant messy context dump.

## 5\. Restrict toolsets by lane

More tools can make an agent better.

They can also make it sloppy.

Use toolsets like permissions.

**Research lane:**

- web
- browser
- files
- Code lane:
- terminal
- file edits
- git
- tests

**Content lane:**

- web
- files
- image tools
- Typefully draft tools
- Safe assistant lane:
- memory
- messaging
- maybe calendar or notes

Hermes lets you enable tools from the UI or start sessions with specific toolsets.

Example:

```text
\`hermes chat --toolsets web,file,terminal\`
```

The point is to give the agent the hands it needs for the job in front of it.

## 6\. Add cron jobs

Cron is where Hermes stops waiting for you.

Use it for recurring checks:

- 9am daily brief
- 2-hour blog watcher
- weekly repo cleanup
- monthly wiki health check
- content queue scan
- server status check
- research digest

**Examples:**

> "Every morning at 9, check AI news and send me a short summary."

> "Every 2 hours, check this feed and stay silent unless something changed."

> "Every Monday, inspect this backlog and draft a planning note."

The best Hermes cron jobs are quiet.

They either deliver something useful or send nothing.

No raw logs.

No fake urgency.

No "everything looks normal" spam.

**Guardrail**: keep scheduled jobs bounded. A cron run should not create more cron jobs.

## 7\. Use profiles for separate agents

Profiles keep one Hermes from becoming a junk drawer.

A profile can have its own:

- config
- API keys
- memory
- sessions
- skills
- cron jobs
- gateway state

**Useful profile split:**

- researcher
- coder
- content
- family office
- client workspace

This matters when context mixing would create mistakes.

A content profile should have different rules than a code profile.

A client workspace should have separate memory from personal ops.

A research profile does not need broad write access by default.

Profiles are a separation layer.

For hard isolation, pair them with separate credentials, restricted tools, and containers.

## 8\. Add MCP servers selectively

MCP is the external tool plug-in layer.

It lets Hermes connect to systems like GitHub, databases, internal APIs, browser tools, n8n, filesystem servers, and custom company tools.

**Useful examples:**

- GitHub MCP for repo and PR work.
- Database MCP for controlled queries.
- n8n MCP for automation handoff.
- Browser MCP for web tasks.
- Internal API MCP for company ops.

The bad version is installing every server you see on X.

The good version is picking one system you use every day and exposing only the tools Hermes needs.

MCP servers can run real code.

Treat them like software you are installing, not like harmless prompts.

## 9\. Wire webhooks and the API server

Cron is time-based.

Webhooks are event-based.

A webhook can trigger Hermes when something happens:

- GitHub PR opened
- Stripe event received
- form submitted
- support ticket changed
- build finished
- new lead arrived

The route can load a skill, pass the payload into Hermes, and deliver the result to Telegram, Slack, Discord, GitHub comments, or a local file.

**Example flow:**

1. PR opens.
2. Hermes loads a code-review skill.
3. Subagents check tests, security, and performance.
4. Summary lands in Telegram.
5. Follow-up tasks go to Kanban.

The API server is the other side.

It lets a frontend talk to Hermes through an OpenAI-compatible API.

Use auth.

Use HMAC on public webhooks.

Do not expose a write-capable agent endpoint casually.

## 10\. Use delegation and Kanban

Some work is too wide for one thread.

Hermes can delegate bounded tasks to subagents.

One agent researches.

One checks docs.

One reviews code.

One drafts options.

The parent gets the final summaries back, so the main context stays cleaner.

For work that needs to survive beyond one chat, use Kanban.

Kanban gives you:

- tasks
- statuses
- comments
- links
- worker lanes
- handoffs
- heartbeats

Use delegation for a fast split.

Use Kanban for durable coordination.

A real Hermes setup starts to look like a chain:

1. A Telegram drop comes in.
2. Hermes classifies it.
3. The right skill loads.
4. The right profile handles the lane.
5. A subagent researches the missing pieces.
6. A cron checks the follow-up tomorrow.
7. Memory keeps the stable preference.
8. Obsidian stores the final note.

This is how you create an actual system.

**I know some of you need a lazy version, just three layers:**

**1\. Telegram**

So work can enter naturally.

**2\. Skills**

So repeated work gets better instead of starting from zero.

**3\. Cron**

So useful checks happen before you remember to ask.

## A simple 7-day build path:

1. Day 1: Telegram.
2. Day 2: Obsidian & memory.
3. Day 3: First skill.
4. Day 4: Quiet cron.
5. Day 5: One profile split.
6. Day 6: One webhook.
7. Day 7: Cleanup & testing.

Do not build the entire machine at once.

You will get overwhelmed & quit.

Build one useful lane, make it reliable, then let the system compound.

**If you like AI Guides, more sure to follow** [@zaimiri](https://x.com/@zaimiri) **for more**