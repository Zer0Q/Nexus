---
title: "Master 97% of Codex in 30 Minutes (Full Course)"
source: "https://x.com/0xCodez/status/2061795739575963935"
author:
  - "[[@0xCodez]]"
published: 2026-06-02
created: 2026-06-03
description: "Most people open Codex, see the chat window, and treat it like ChatGPT with a fancier sidebar. 9 out of 10 users miss 97% of what it actuall..."
tags:
  - "clippings"
summary:
---
![Imatge](https://pbs.twimg.com/media/HJzuprgWUAAHBb4?format=jpg&name=large)

Most people open Codex, see the chat window, and treat it like ChatGPT with a fancier sidebar. **9** out of 10 users miss 97% of what it actually does.

They **don’t build Skills**, **don’t deploy to live URLs**, **don’t run automations while they sleep**. This is the 14-step roadmap that takes you from blank folder to a working AI workflow in 30 minutes.

> Follow my Substack to get best AI alpha: [movez.substack.com](https://movez.substack.com/)

Codex is OpenAI’s agentic coding platform - not the deprecated 2021 code-completion API, the new one. It launched as a CLI in April 2025, grew into a desktop app, an IDE extension for VS Code/Cursor/Windsurf, and a cloud agent.

Sam Altman confirmed in April 2026 it had ~4 million weekly active users. It is now the closest direct competitor to Claude Code.

If you’ve used Claude Code, the mental model transfers in one sentence: **a folder on your computer, a markdown configuration file, an agent that reads everything in the folder, plus an extension layer of Skills, MCP servers, automations, and a built-in browser**.

Different harness. Different model. Same pattern.

![Imatge](https://pbs.twimg.com/media/HJzvGzNW0AAPPli?format=png&name=large)

**14 steps. 3 tiers. One folder that runs your workflows.**

**PART 1 · The Setup**

## 01\. Project folder on your computer.

Codex doesn’t have its own database, its own file system, or its own “workspace.” A Codex project is a regular folder anywhere on your machine. When you start a new project, Codex opens a file picker.

You pick the folder. From that moment on, every file inside is fair game: read, write, edit, organize, move.

This single design choice changes everything downstream:

- **Your project is portable.** The same folder opens in Codex CLI, the Codex app, the IDE extension for VS Code/Cursor/Windsurf - or Claude Code, or Cursor. The harness changes; the work doesn’t.
- **You version-control it like any code.** Git, GitHub, Vercel - standard tools, no special integrations needed.
- **You back it up, share it, and move it** the same way you handle any other folder on disk.

![Imatge](https://pbs.twimg.com/media/HJzwvAfWMAERbJP?format=jpg&name=large)

**By default Codex runs in Agent mode** - it can read, edit, and run commands inside the working directory automatically. Anything outside the folder, and any network access, still requires your approval. The folder is the trust boundary.

## 02\. Write an AGENTS.md. The onboarding doc Codex reads first.

This is the single most under-used file in Codex. AGENTS.md sits in the project root. Codex reads it every time you open a new chat in that folder.

It tells the agent who you are, what the project is, what the goal looks like, and what constraints matter.

The trick: **don’t write it from scratch**. Tell Codex the project goal in plain English. Ask it to draft an AGENTS.md. You get a structured file you then edit. Faster, more complete, less likely to miss something.

```python
# Project: YouTube Comment Intelligence

## Context
I run a YouTube channel about AI tools. I want to understand
what viewers are asking, what they want to see, and what tools
they’re comparing — without reading every comment manually.

## Goal
Build a workflow that pulls recent comments, classifies them,
surfaces patterns, and visualizes the result on a live dashboard.

## Constraints
- Use the YouTube Data API v3 with an API key (not OAuth).
- Keep credentials in .env.local, never commit them.
- Output target: Excel workbook for analysis + web dashboard.
- Deploy dashboard to Vercel.
- Refresh data weekly via automation.

## Conventions
- Save failed approaches to project memory so we never retry them.
- Always confirm a plan before writing code.
```

What makes a good AGENTS.md:

- **Context - one paragraph.** Who you are and why this project exists. Saves you re-explaining yourself every session.
- **Goal - one paragraph.** The end state, not the steps. Steps belong in plan mode (step 3).
- **Constraints - bullet list.** Hard rules. API choices, languages to avoid, security boundaries, output formats. The shorter and more specific, the better.
- **Conventions - bullet list.** “Save lessons to memory.” “Always confirm a plan first.” “Never run X.” These compound into reliable behavior.

OpenAI’s own best-practices guide makes this explicit: “Codex works best when you treat it less like a one-off assistant and more like a teammate you configure and improve over time. Start with the right task context, use AGENTS.md for durable guidance, configure Codex to match your workflow.”

![Imatge](https://pbs.twimg.com/media/HJzxY6ZXgAA3MaW?format=jpg&name=large)

## 03\. Start every build in Plan mode

Plan mode means Codex doesn’t execute anything. It brainstorms, asks clarifying questions, surfaces tradeoffs, and produces a numbered plan you approve before it writes code. **Skipping plan mode is the single biggest reason builds go sideways.**

![Imatge](https://pbs.twimg.com/media/HJzxzOpW4AAGfCY?format=jpg&name=large)

The pattern that works:

- **Describe the goal, not the steps.** “Pull recent comments from my YouTube channel and turn them into an Excel report” - not “use Python to call the YouTube API and write to xlsx.”
- **Let it ask questions.** Codex in plan mode usually returns 3-5 clarifying questions. Answer them honestly. Each one is a future bug avoided.
- **Approve the plan before it executes.** Read the steps. If anything looks wrong — missing edge case, weird tool choice, unnecessary complexity — push back. Cheaper to fix in plan mode than after the code is written.

Plan mode pairs especially well with AGENTS.md: the constraints in your config file shape what plans Codex even proposes. The two together cut wrong approaches by an order of magnitude.

## 04\. Set up .env.local for API keys.

Every API key, every secret, every credential goes into .env.local in your project root. **The dot at the front of the filename is not decoration** - it’s how Codex (and git) know to exclude the file from public commits.

Two rules that prevent painful mistakes:

- **Never paste keys into a random secrets.txt** or worse, directly into a chat message. Both end up in version control. Both become public the moment you push.
- **Always test the key after adding it.** Ask Codex to make a minimal API call to confirm the key works. Surface auth errors before they cost you a build.

![Imatge](https://pbs.twimg.com/media/HJzyOtOXwAAAueF?format=png&name=large)

If a key ever does end up in a commit. Rotate the key immediately at the provider (Google Cloud, OpenAI, etc.). **Don’t just delete it from the file and push the deletion** - the old commit still has the key, and bots scrape GitHub commits for leaked secrets within minutes. The only safe fix is rotating the credential.

**PART 2 · Connect & Build**

## 05\. Connect MCP servers and plugins.

Codex speaks the **Model Context Protocol (MCP)** - the same open standard Claude Code uses. That means most existing MCP servers work in Codex too: GitHub, Slack, Notion, Linear, Drive, Figma, plus dozens of community-built ones.

![Imatge](https://pbs.twimg.com/media/HJzz82jXEAAojID?format=png&name=large)

What this unlocks: instead of describing your data to Codex, you let it read your data. Instead of describing actions for Codex to suggest, you let it perform them. The conversation shifts from “here’s what’s in my repo” to “create a PR with this fix and tag the owner.”

Three patterns that pay back fastest:

- **GitHub MCP** - read repos, create branches, open PRs, comment on issues. The single biggest day-one win for any dev.
- **Vercel MCP** - deploy, check status, roll back. Pair with GitHub for a complete “build → commit → deploy” loop.
- **Notion or Drive MCP** - pull internal docs as context, write decisions back to a central log. Codex stops being a black box, becomes part of the team’s memory.

## 06\. When no plugin exists, ask Codex to set up the API

Not every service has an MCP server. YouTube Data API doesn’t. Internal company APIs don’t. Niche SaaS tools usually don’t.

When that happens, you don’t hunt for a third-party wrapper. **You ask Codex.** In plan mode, tell it the integration goal - “pull recent comments from my YouTube channel.”

It will return options (API key vs OAuth), recommend one, and produce a step-by-step plan to set up credentials, enable the relevant API, and test the connection.

The pattern that compounds over time:

- **Try the first approach.** Codex picks one based on tradeoffs. Let it.
- **When something fails, save the lesson.** “PowerShell hit a TLS error, Python worked. Save that to project memory so we never retry the broken path.” The next session inherits the knowledge.
- **Lock the working pattern.** Once an integration is solid, turn it into a Skill (step 9). You never repeat the setup.

This is the single most important habit in agentic work. **Try, fail, save the failure, never fail the same way twice.** Codex agents have short memory by default - what they learn this session is gone tomorrow unless you write it down.

Tell Codex to update AGENTS.md or project memory whenever something teaches it a real lesson. The system gets sharper every time you use it.

## 07\. Build a real deliverable with specific prompts.

The point of any tool is the deliverable. For most users, the first one is something concrete - an Excel report, a script that automates something tedious, a dashboard, a generated document. The thing that proves the tool earns its keep.

The single rule that determines whether your first build is great or generic: **specificity in the prompt**. “Analyze my YouTube comments” produces an Excel sheet with categories like “positive,” “negative,” “neutral.” Useless. “Analyze my YouTube comments and classify them by: tool comparison, content request, technical question, general feedback - then rank by reply priority for me as a creator” produces a workbook you actually use.

Two patterns that lift output quality fast:

- **State the role of the output** - “for me as a creator,” “for a board update,” “for my engineering team.” The audience shapes the structure.
- **Enumerate the categories or buckets you care about.** Don’t leave classification to default judgment. Tell Codex your taxonomy.

If the first version is OK but not great, don’t throw it out. Add more specificity and re-run. Three rounds of iteration with sharper prompts beats starting over five times.

## 08\. Use gpt-image-2 for concept art before building UI.

Codex has built-in image generation through **gpt-image-2** - the OpenAI image model. Invoke it explicitly with [$imagegen](https://x.com/search?q=%24imagegen&src=cashtag_click) in your prompt, or just describe what you need and Codex will pick it up.

![Imatge](https://pbs.twimg.com/media/HJz0_jiWwAAO09U?format=jpg&name=large)

Generated images become project assets the rest of the build can reference.

The pattern that unlocks this: **generate concept art before the UI code**. Ask Codex to mock up the dashboard look in one or two images first. Save them to the project.

Then ask it to build the dashboard, referencing the concept art. The visual output comes out sharper than letting the model freestyle the design from a text spec.

## 09\. Turn workflows into Skills

A Skill is a reusable recipe Codex loads on demand. Once you’ve built a workflow that works - pulling comments, generating a report, deploying a dashboard - you turn it into a Skill so the next run is one command.

Skills in Codex are markdown files in a folder. The directory has a SKILL.md file with frontmatter (name + description) and a body of instructions. Optionally include scripts and reference files alongside.

```python
---
name: youtube-comment-insights
description: Pull recent YouTube comments via the Data API,
  classify them by content category and tool mentions,
  rank by reply priority, and output an Excel workbook
  with summary tabs and charts. Trigger whenever I ask
  for "comment insights" or "weekly youtube report."
---

# YouTube comment insights

## Setup
- Read YOUTUBE_API_KEY from .env.local.
- Fetch ~200 most recent comments across the last 10 videos.

## Classification
- Categories: tool comparison, content request, technical question,
  general feedback, off-topic.
- Tool mention tracking: Codex, Claude Code, Cursor, API, GPT, etc.
- Priority signal: questions > high-engagement comments > other.

## Output
- Workbook tabs: Summary, Categories, Tool Mentions,
  Priority Replies, Content Ideas, Raw.
- Charts on Summary tab: category mix, tool ranking.
```

**Two storage levels worth knowing:**

- **Global Skills** - stored at ~/.agents/skills/. Available in every Codex project on your machine.
- **Project-level Skills** - stored inside the project folder itself. Only available there. Useful for client-specific or project-specific recipes.

![Vídeo incrustat](https://pbs.twimg.com/tweet_video_thumb/HJz3EVvWgAABQyW?format=jpg&name=large)

GIF

Three things that determine whether a Skill actually triggers when you need it:

- **The description is everything.** Codex matches your task against the description text alone for implicit invocation. Front-load the key use case and trigger words; vague descriptions never fire.
- **Two ways to invoke.** Explicit (/skills in CLI/IDE, or [$skillname](https://x.com/search?q=%24skillname&src=cashtag_click) mention), or implicit (Codex picks the skill when your prompt matches the description).
- **Open standard.** Skills launched for Codex in December 2025 and are now part of the cross-platform Agent Skills standard - same format works in Codex, Claude Code, Gemini CLI, Cursor. Write once, run anywhere.

## 10\. Deploy localhost to a live URL. GitHub → Vercel → production.

The Excel sheet was the backend. A dashboard is the frontend. Localhost is the development URL. None of these are shippable.

To go from localhost to live, you wire up two services: GitHub for the repo, Vercel for the host. **Codex orchestrates the whole flow.**

```python
> Connect this project to GitHub. Create a private repo
  named "yt-comments-dashboard" and push the codebase.
▲ Codex  authenticating with gh CLI…
  - created github.com/you/yt-comments-dashboard (private)
  - initial commit pushed
✓ repo ready

> Connect Vercel to the same GitHub account.
  Import this repo. Deploy.
▲ Codex  connecting Vercel…
  - vercel project created
  - build succeeded in 38s
✓ live at https://yt-comments-dashboard.vercel.app
```

The killer detail: **GitHub and Vercel keep talking to each other after the initial connect.** Every push to main triggers an automatic Vercel deploy. You never log back into Vercel. You work in Codex, Codex pushes to GitHub, Vercel deploys. Three tools, one workflow.

## 11\. Set up Automations - and explicitly set the model.

The Codex app has an Automations tab. Scheduled prompts that run on a cron. Combined with Skills, this is what turns a dashboard into “a thing that updates itself while you sleep.”

A real Sunday-evening automation: pull fresh comments, run the insights Skill, update the Excel file, push the new data, let Vercel auto-deploy. End-to-end refresh, untouched. By Monday morning the dashboard is current.

![Imatge](https://pbs.twimg.com/media/HJz2Zs_XQAEbpvW?format=jpg&name=large)

The model picker inside the Automations panel **does NOT inherit from your active chat**. A new automation defaults to whatever the panel default is, which may be slower and cheaper than what you actually want for production runs.

**Set the model explicitly per automation**, or you’ll wonder why a 7-minute job suddenly takes 40 minutes. Same problem if you have a file open locally that Codex needs to overwrite - close it first.

## 12\. Pick the right thread mode - Local, Worktree, or Cloud.

Each thread in the Codex app runs in one of three modes. Picking the right one is the difference between safe iteration and rage-quitting after a bad merge.

- **Local** - works directly in your current project directory. Fastest, easiest, but every change touches the live working tree. Good for small, contained edits when you trust the agent.
- **Worktree** - isolates changes in a Git worktree (a sibling working directory tied to the same repo). The agent works in a separate branch with no risk to your main checkout. **This is the default for any meaningful build.** If the run goes wrong, throw the worktree away. Zero damage.
- **Cloud** - runs remotely in a configured cloud environment. Your laptop can be off. Pair this with Automations (step 11) for true async workflows that don’t depend on your machine being awake.

The rule of thumb: **Worktree for ambitious work, Local for small surgical edits, Cloud for long-running automated runs**. Three trust levels, picked per task.

## 13\. Use built-in Browser Use as the QA loop.

After building a dashboard, ask Codex to open it in the built-in browser, click through, try to break it, and report back. It does.

It catches things you would have missed staring at the code - broken external links, empty states that look bare, search behavior that’s too literal, accessibility gaps, minor UI inconsistencies.

![Imatge](https://pbs.twimg.com/media/HJz3XCmW4AAi_x9?format=jpg&name=large)

The pattern that turns this from a one-off into a habit: **bake the QA pass into your project memory or Skill**.

Every time you ship a new feature, the agent runs a browser pass before returning to you. You stop being the QA tester. The agent does it. You review the report.

Browser Use isn’t just for QA, though. It’s a general-purpose tool the moment an API doesn’t exist:

- **Logging into tools without APIs** - legacy admin panels, vendor portals, internal dashboards.
- **Pulling reports from dashboards that don’t expose data programmatically**\- analytics views, billing tools, status pages.
- **Automating multi-step UI workflows** you’d otherwise click through by hand. Describe the steps in natural language; Codex performs them.

## 14\. Use the UX features most people ignore.

The Codex app has a handful of UI features that turn it from “tool I use” into “workspace I live in.” They look minor in isolation. Together they compound.

- **Side chat.** Open a side thread off your main conversation. Same project context, different conversation. Ask a quick question without polluting the main session. Close it when done.
- **Slash commands.** Type / to browse: /skills to invoke a Skill explicitly, /clear, /help, and more. Slash menus surface everything Codex can do.
- **@-mentions.** Tag a specific file in your prompt: “Use [@example](https://x.com/@example).tsx as a reference to add a new page that lists items from [@resources](https://x.com/@resources).ts.” Way cleaner than pasting paths.
- **Model switcher + reasoning effort.** The switcher under the chat input swaps models per conversation. Reasoning effort controls how long Codex thinks before responding. Higher effort = better on complex tasks, more tokens, faster rate-limit drain. Match effort to task.
- [$imagegen](https://x.com/search?q=%24imagegen&src=cashtag_click) **+ Skills mentions.** Type $ to mention a skill inline. Same syntax as @ for files. Lets you compose multiple skills in one prompt.
- **Auto-context sync with IDE Extension.** If Codex IDE Extension is installed in your editor, the app and editor automatically sync when both are in the same project. You see threads running in the app inside the editor, and vice versa. Toggle “Auto context” to have Codex track files you’re viewing.
- **Full access mode.** Settings → toggle to skip approval prompts. Faster, riskier. Start on default. Switch to full access only once you trust the project boundaries.

![Imatge](https://pbs.twimg.com/media/HJz33YIXgAAlNHH?format=png&name=large)

## The habits that keep Codex at 3% of its potential

- **No AGENTS.md.** Re-explaining the project every session, getting different answers every session.
- **Skipping plan mode.** Forty-file diffs to fix a one-sentence misunderstanding.
- **Keys in chat or in secrets.txt.** Public the moment you push.
- **Never saving lessons to memory.** Failing the same way over and over because nothing got written down.
- **Vague prompts.** Generic deliverables and surprise that the output is generic.
- **One-off builds.** Rebuilding the same workflow from scratch every week instead of turning it into a Skill.
- **Local mode for everything.** A bad agent run wipes your working tree because you didn’t use a worktree.
- **Letting Automations default the model.** 40-minute runs that should take 7.
- **No QA pass.** Shipping dashboards with broken external links and empty states that look bare.
- **Tool tribalism.** Picking Codex vs Claude Code based on identity, not the job in front of you. Both win, depending.

## Conclusion:

Codex looks like a chat window. It is not a chat window. It is a folder with an agent that knows what’s in it - plus a layer of Skills, MCP, automations, and a browser, all configured through markdown files that live in the folder itself.

**That folder is portable.** Open it in Codex, Claude Code, Cursor, or any tool that speaks the Agent Skills standard. The harness changes. The work doesn’t.

Most users will keep typing questions into the chat and stop there. They’ll get answers, copy code, and move on. **The 4 million weekly active users shipping with Codex are the ones who configured the folder.**

Pick one step you weren’t doing - probably AGENTS.md, or your first real Skill - and add it tomorrow. Then the next. The output of Codex follows the configuration of Codex.

Empty folder. Workflow engine. 14 steps between them.