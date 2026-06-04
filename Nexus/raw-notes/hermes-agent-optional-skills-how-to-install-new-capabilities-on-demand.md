---
title: "Hermes Agent Optional Skills: How to Install New Capabilities on Demand"
source: "https://x.com/NeoAIForecast/status/2051802880114639067"
author:
  - "[[@NeoAIForecast]]"
published: 2026-05-06
created: 2026-05-31
description: "Most AI agents have a scaling problem.The more workflows you teach them, the more instructions they carry around all the time. That means mo..."
tags:
  - "clippings"
---
![Imatge](https://pbs.twimg.com/media/HHlt7uHbgAA9G9k?format=jpg&name=large)

Most AI agents have a scaling problem.

The more workflows you teach them, the more instructions they carry around all the time. That means more prompt weight, more context clutter, and more chances for irrelevant behavior to leak into a task.

Hermes Agent handles this differently.

Instead of forcing every capability into the core prompt, Hermes uses skills: on-demand Markdown instruction packs that teach the agent how to do specific things.

Some skills ship enabled by default. Others are official optional skills, shipped with Hermes but inactive until you explicitly install them.

Takeaway: Hermes does not need to be huge to be powerful. It can stay lean, then load expertise only when the job needs it.

## What optional skills are

A Hermes skill is a reusable procedure.

It can tell the agent:

- when to use a workflow
- which commands to run
- which APIs or CLIs are required
- what pitfalls to avoid
- how to verify the result
- which reference files, scripts, or templates to load later

Optional skills are the same idea, but they are not active by default.

They live in the Hermes Agent repo under:

[https://github.com/NousResearch/hermes-agent/tree/main/optional-skills](https://github.com/NousResearch/hermes-agent/tree/main/optional-skills)

When you install one, Hermes copies it into your local skill library:

```bash
~/.hermes/skills/
```

After that, the skill becomes available like any other installed skill.

Takeaway: Optional skills are official Hermes capabilities you can add without changing Hermes core.

## Why Hermes keeps them optional

Not every user needs every workflow.

- A local LLM builder may want skills for Flash Attention, vLLM, TensorRT-LLM, Qdrant, or PEFT fine-tuning.
- A researcher may want DuckDuckGo search, domain intelligence, bioinformatics, drug discovery, or scraping tools.
- A creator may want Blender MCP, meme generation, concept diagrams, or video orchestration.
- A security-focused user may want 1Password, Sherlock, or OSS forensics.

If all of that loaded by default, the agent would get noisy.

Optional skills solve the trade-off:

- keep the default agent lightweight
- make advanced workflows discoverable
- install only what you actually use
- avoid polluting every session with niche instructions
- let Hermes grow without forcing every user into the same setup

Takeaway: Optional skills are how Hermes gets broader without becoming bloated.

## How to browse optional skills

Use the skills hub.

From your terminal:

```bash
hermes skills browse --source official
```

![Imatge](https://pbs.twimg.com/media/HHlvIWtaAAAQX7W?format=png&name=large)

If you want more results on one page:

```bash
hermes skills browse --source official --size 80
```

Inside a Hermes chat session, you can also use:

```bash
/skills browse
```

![Imatge](https://pbs.twimg.com/media/HHlvlMVaUAAmIpV?format=png&name=large)

To search for something specific:

```bash
hermes skills search docker
hermes skills search qdrant
hermes skills search whisper
hermes skills search solana
```

![Imatge](https://pbs.twimg.com/media/HHlv1lJbgAAaP4p?format=png&name=large)

Takeaway: Start with browse when exploring. Use search when you already know the capability you want.

## How to inspect before installing

You do not have to install blindly.

Preview a skill first:

```text
hermes skills inspect official/research/duckduckgo-search
```

![Imatge](https://pbs.twimg.com/media/HHlwkfRbQAECdxM?format=png&name=large)

Inspection is useful because a skill may require a local CLI, an API key, or a specific setup path.

For example:

- Docker management expects Docker workflows.
- 1Password expects the op CLI.
- Blender MCP expects Blender plus the MCP add-on.
- Parallel CLI expects vendor setup.
- Some MLOps skills expect Python, CUDA, GPU tooling, or cloud credentials.

Takeaway: Inspect first if the skill might require credentials, local tools, or external services.

## How to install an official optional skill

The install pattern is simple:

```bash
hermes skills install official/<category>/<skill>
```

Example:

```bash
hermes skills install official/mlops/tensorrt-llm
```

![Imatge](https://pbs.twimg.com/media/HHlyAtgbEAAqXxd?format=png&name=large)

Once installed, the skill is copied into:

```bash
~/.hermes/skills/
```

Then it appears in:

```text
hermes skills list
```

![Imatge](https://pbs.twimg.com/media/HHlzOqHboAAHoBv?format=png&name=large)

## When installed skills take effect

After installing a skill, start a new session or reset the current one.

In chat:

```bash
/reset
```

Or just start Hermes again

Why?

Hermes protects prompt caching. It does not constantly mutate the active skill index mid-session unless you explicitly ask it to.

There is also a **\--now** option in some skill flows that can invalidate the prompt cache immediately, but the clean habit is simple:

![Imatge](https://pbs.twimg.com/media/HHl06vBboAAv3fU?format=jpg&name=large)

Takeaway: If a newly installed skill does not appear immediately, reset the session.

## How to uninstall optional skills

If you no longer need one:

```bash
hermes skills uninstall tensorrt-llm
```

![Imatge](https://pbs.twimg.com/media/HHl1cn9agAA21tK?format=png&name=large)

Takeaway: Install with the official path. Uninstall with the local skill name.

## How skills differ from tools

This is the key mental model.

A tool gives Hermes an action surface.

Examples:

- terminal
- file editing
- browser automation
- image generation
- cron jobs
- memory
- web search
- MCP

A skill teaches Hermes how to use capabilities well.

Examples:

- how to manage Docker safely
- how to run a Qdrant vector search workflow
- how to query Solana wallets
- how to set up 1Password CLI
- how to use FastMCP
- how to structure a code review
- how to fine-tune with PEFT

Tools are hands.

Skills are playbooks.

Takeaway: Tools let Hermes act. Skills teach Hermes how to act correctly.

## The best optional skills to install first

For most technical users, I would start with a small set.

If you do AI research:

```bash
hermes skills install official/research/duckduckgo-search
hermes skills install official/research/domain-intel
hermes skills install official/research/parallel-cli
```

If you build local LLM systems:

```text
hermes skills install official/mlops/qdrant-vector-search
hermes skills install official/mlops/chroma
hermes skills install official/mlops/peft-fine-tuning
hermes skills install official/mlops/tensorrt-llm
hermes skills install official/mlops/optimizing-attention-flash
```

If you do infrastructure:

```bash
hermes skills install official/devops/docker-management
hermes skills install official/mcp/fastmcp
hermes skills install official/mcp/mcporter
```

If you care about security and secrets:

```bash
hermes skills install official/security/1password
hermes skills install official/security/oss-forensics
hermes skills install official/security/sherlock
```

If you create visual or media content:

```text
hermes skills install official/creative/concept-diagrams
hermes skills install official/creative/blender-mcp
hermes skills install official/creative/meme-generation
```

Takeaway: Do not install everything. Install the skill clusters that match your actual workflows.

## Installing from outside the official catalog

Official optional skills are only one source.

Hermes can also install skills from:

- [skills.sh](https://skills.sh/)
- well-known skill endpoints
- direct GitHub sources
- custom GitHub taps
- direct SKILL.md URLs
- community marketplaces such as ClawHub or LobeHub

Examples:

```text
hermes skills search react --source skills-sh
hermes skills inspect skills-sh/vercel-labs/json-render/json-render-react
hermes skills install skills-sh/vercel-labs/json-render/json-render-react
```

Install directly from a URL:

```text
hermes skills install https://example.com/SKILL.md --name my-skill
```

Add a custom GitHub skill source

```text
hermes skills tap add myorg/skills-repo
```

Then browse or install from it.

Takeaway: Hermes skills are not locked to one registry. Official skills are the safest starting point, but the system is open.

## Security model

Hermes scans hub-installed skills.

The scanner checks for patterns like:

- data exfiltration
- prompt injection
- destructive commands
- suspicious supply-chain behavior
- dangerous instructions

Official optional skills use trusted official provenance.

![Imatge](https://pbs.twimg.com/media/HHl3UpYawAAShsA?format=png&name=large)

Community skills get stricter treatment. Some warnings can be overridden with:

```bash
hermes skills install <identifier> --force
```

But dangerous scan verdicts are not meant to be bypassed.

Use this rule:

```plaintext
Official skill: generally safe to install
Trusted source: inspect first
Community source: inspect carefully
Unknown URL: treat like running code from the internet
```

Takeaway: Skills are powerful because they can teach workflows. That also means provenance matters.

## Final thought

Optional skills are one of Hermes Agent’s most underrated design choices.

They make the agent extensible without making it bloated.

They let advanced users add deep workflow knowledge without forcing casual users to carry it.

And they create a clean path for Hermes to grow into a serious operating layer: not by hardcoding every behavior, but by letting capabilities become modular, installable, inspectable, and reusable.

The future of agents is not one giant prompt. It is a small core with a library of skills that load exactly when needed.

Takeaway: Hermes optional skills are how you turn a general agent into your agent.