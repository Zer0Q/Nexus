---
title: "How Skills Work in Hermes Agent"
source: "https://x.com/NeoAIForecast/status/2044252861710905685"
author:
  - "[[@NeoAIForecast]]"
published: 2026-04-15
created: 2026-05-31
description: "Most AI agents forget the method even when they remember the result.Hermes is different.It doesn’t just keep conversation history. It can lo..."
tags:
  - "clippings"
---
![Imatge](https://pbs.twimg.com/media/HF6cjDAasAAdmhY?format=jpg&name=large)

Most AI agents forget the method even when they remember the result.

Hermes is different.

It doesn’t just keep conversation history. It can load reusable procedural knowledge exactly when needed, keep it out of context when it isn’t, and even turn hard-won workflows into reusable skills for later.

That changes how the agent improves over time.

## What a skill actually is

A skill in Hermes is not just a prompt snippet.

It is an on-demand knowledge document that teaches Hermes how to handle a specific kind of task. That can mean a workflow, a tool-specific procedure, a troubleshooting pattern, a formatting standard, or an operational playbook.

The key idea is that skills are procedural memory.

- Memory stores durable facts.
- Sessions store what happened.
- Skills store how to do something well.

![Imatge](https://pbs.twimg.com/media/HF6kCVfasAQttZl?format=png&name=large)

That distinction matters, because it lets Hermes keep reusable know-how without stuffing every session with hundreds of pages of instructions.

Takeaway: Skills are Hermes’ reusable “how-to” layer, not its general memory layer.

## What problem skills solve

Without a skill system, an agent usually has two bad options:

**Keep everything in the prompt**

- This gets expensive fast and bloats context with instructions that may not matter for the current task.

**Hope the model remembers the right pattern**

- That works sometimes, but breaks when the task needs exact commands, known pitfalls, environment-specific steps, or a specific output style.

Hermes solves that with on-demand loading.

Instead of carrying every workflow at all times, Hermes keeps a compact index of available skills and only loads the full skill when the task actually needs it. This is one of the most practical parts of Hermes’ design.

It makes the agent more capable without making every conversation heavier.

Takeaway: Skills let Hermes stay lightweight by default and specialized when needed.

## How skills work in Hermes

Hermes uses a progressive disclosure model for skills.

At the lightest level, it knows what skills exist. When needed, it opens the full skill. If the skill has supporting reference files, it can open only those files too.

**The flow looks like this:**

**Level 0:**

- skills\_list()

Hermes sees a compact index of skill names, descriptions, and categories.

**Level 1:**

- skill\_view(name)

Hermes loads the full SKILL.md for the relevant skill.

**Level 2:**

- skill\_view(name, file\_path)

Hermes loads a specific reference, template, or script inside the skill only if it needs more detail.

This matters operationally because the agent is not dragging full skill contents into every session. It loads deeper context only when the task justifies the cost.

Takeaway: Hermes treats skills like a layered knowledge system, not a giant always-on prompt.

## Where skills live

The main source of truth is:

**~/.hermes/skills/**

That directory holds:

- bundled skills copied in on install
- hub-installed skills
- agent-created skills
- agent-updated skills

![Imatge](https://pbs.twimg.com/media/HF6hcQyasAA3mBF?format=png&name=large)

A typical structure looks like:

**~/.hermes/skills/<category>/<skill-name>/SKILL.md**

Skills can also include:

- references/
- templates/
- scripts/
- assets/

Hermes can scan external skill directories too, but when it creates or edits skills itself, it writes back to the local Hermes skills directory.

That keeps the working copy of procedural knowledge under Hermes’ own control.

Takeaway: Skills are real files in Hermes, not hidden system magic.

![Imatge](https://pbs.twimg.com/media/HF6jBZ4asAI_phv?format=png&name=large)

## What a skill contains

A Hermes skill is usually a markdown document with YAML frontmatter plus structured instructions.

In practice, a strong skill includes:

- what it is for
- when to use it
- exact procedure
- command examples
- pitfalls
- verification steps

This is why skills are more useful than vague “expert mode” prompting.

A good skill does not just tell the model the topic. It gives Hermes a tested operating pattern.

For example, a good skill does not say:

“Be good at GitHub PRs.”

It says:

- when to use this workflow
- what to inspect first
- which commands to run
- what failure modes to check
- how to verify the result before finishing

Takeaway: A skill is valuable when it captures a workflow precisely enough to reuse, not just describe.

## How you use skills in practice

Hermes makes installed skills directly usable.

You can invoke them as slash commands in chat, for example:

**/plan** Design a rollout for migrating our auth provider

**/github-pr-workflow** Create a PR for the auth refactor

**/excalidraw**

You can also work with them from the CLI:

**hermes skills list**

**hermes skills search docker**

**hermes skills install official/research/arxiv**

**hermes skills inspect openai/skills/k8s**

And in natural conversation, Hermes can decide to load a relevant skill itself when the task matches.

**That is the important part:** skills are not only manual shortcuts. They are also part of how Hermes can operate more intelligently during real work.

Takeaway: Skills can be called directly by you or loaded by Hermes when the task calls for them.

## Why this matters operationally

This is where skills become more than a convenience feature.

A skill changes Hermes from “one smart model doing its best” into “an agent with reusable procedures.”

That gives you several advantages:

**1\. Better consistency**

- If a workflow has a proven sequence, Hermes can repeat it instead of reinventing it every time.

**2\. Lower token waste**

- The full instructions stay out of context until needed.

**3\. Better specialization**

- Hermes can carry many capabilities without bloating normal conversations.

**4\. Better iteration**

- When a workflow improves, the skill can be updated instead of hoping the model remembers the new version.

**5\. Better compounding**

- Once a useful method becomes a skill, future sessions can benefit from it immediately.

This is one of the clearest places where Hermes behaves more like an agent runtime than a chatbot wrapper.

Takeaway: Skills are one of the mechanisms that let Hermes improve procedurally over time.

## Skills vs memory vs sessions

People mix these up a lot, so this is worth making explicit.

**Skills**

Store reusable procedures.

> Example: how to review a GitHub PR, how to draft an X article, how to verify a local install.

**Memory**

Stores durable facts.

> Example: user preferences, environment details, conventions, recurring corrections.

**Sessions**

Store conversation history.

> Example: what happened in a particular project thread, what was tried, what worked, what failed.

A simple rule:

- If Hermes should remember a fact, that belongs in memory.
- If Hermes should recall a past conversation, that belongs in sessions or session\_search.
- If Hermes should reuse a method, that belongs in a skill.

Takeaway: Skills are for repeatable workflows, not personal facts or raw conversation history.

## How Hermes gets better through skills

One of the strongest parts of the Hermes model is that skills are not just preinstalled static docs. Hermes can create and update skills through its skill management flow.

That means after a complex task, a tricky bug, or a non-obvious workflow, the agent can turn what it learned into a reusable skill for later.

This is important because a lot of agent systems talk about “learning,” but what they really mean is storing more context.

Hermes has a cleaner model:

- facts go to memory
- history stays in sessions
- procedures become skills

That separation makes the system more maintainable and more reusable.

Takeaway: Hermes improves best when it saves methods as skills instead of treating every lesson as generic memory.

## Final takeaway

Skills are one of the core reasons Hermes can become more useful over time without becoming more bloated over time.

They let the agent keep specialized procedures off to the side, load them only when relevant, and turn successful workflows into reusable operating knowledge.