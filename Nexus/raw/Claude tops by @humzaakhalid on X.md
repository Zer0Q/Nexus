---
title: "Post by @humzaakhalid on X"
source: "https://x.com/humzaakhalid/status/2061337794740637883"
author:
  - "[[@humzaakhalid]]"
published: 2026-05-24
created: 2026-06-02
description: "Andrej Karpathy broke down exactly what Claude Code keeps doing wrong. A creator created a repo that hit 110K GitHub stars in under 3 month"
tags:
  - "clippings"
summary:
---
Andrej Karpathy broke down exactly what Claude Code keeps doing wrong.

A creator created a repo that hit 110K GitHub stars in under 3 months and stayed at number 1 trending for 28 days straight.

Here is every principle inside it:

☑️ The Origin Story

→ Karpathy coined vibe code, ex-Tesla AI Director, and OpenAI co-founder.

→ Forrest Chang distilled his X thread into one CLAUDE. MD file

→ It got 5,828 stars in a single day. 110,000+ in under 3 months.

↳ Why it went viral: The 4 principles are not novel. Every developer recognised their own frustrations instantly.

☑️ The 4 Karpathy Failure Patterns

→ Models make wrong assumptions on your behalf

→ They overcomplicate code, build 1000 lines when 100 would do.

→ They change code they do not understand, even when unrelated to the task.

→ LLMs loop until they meet goals, but need those goals explicitly defined.

☑️ The 4 Principles Inside the File

✦ 1. Think Before Coding:

State assumptions before implementing. If uncertain, ask. Never pick silently.

✦ 2. Simplicity First:

Minimum code that solves the problem. Nothing speculative. If you wrote 200 lines and it could be 50, rewrite it.

✦ 3. Surgical Changes:

Touch only what you must. Clean up only your own mess. Every changed line must trace directly to the request.

✦ 4. Goal-Driven Execution:

Define success criteria before starting any multi-step task. Strong criteria mean Claude loops independently. Weak criteria mean constant clarification.

☑ How to Use It Today:

✦ Claude code Users:

→ Drop CLAUDE. md into your project root folder.

→ Claude reads it automatically at every session start.

✦ Cursor users:

→ The repo includes .cursor/rules/karpathy-guidelines.mdc and works across any project without re-adding the file.

✦ Claude. ai users:

→ Paste the 4 principles into your project instructions and add them to your SKILL as a negative instructions block.

↳ Get it at: http://github.com/forrestchang/andrej-karpathy-skills…

☑ The Dos and Don'ts

→ Do: State assumptions before writing a single line of code.

→ Do: Write the minimum code that solves the problem. Then stop.

→ Do: Define success criteria before starting any multi-step task.

→ Do: Ask clarifying questions before implementing, not after making mistakes.

→ Never: Make silent assumptions. It is the number 1 failure mode.

→ Never: Add features, flexibility, or abstractions nobody asked for.

→ Never: Refactor or improve adjacent code. It creates collateral damage.

→ Never: Use weak goals like "make it work." Claude will guess endlessly.

For more AI systems like this: 👇

→ Go to https://substack.com/@humzakhalid

→ Subscribe to my free newsletter (don't pay anything)

→ Get more free and daily cheatsheets

Which of the 4 failure patterns are you seeing most in your own Claude sessions right now? Drop it below.

♻️ Repost to give your network an unfair advantage.

> **Hamza Khalid @humzaakhalid** · 2026-05-24
> 
> ![Imatge](https://pbs.twimg.com/media/HJtXzFgawAA1veO?format=png&name=large) ![Imatge de portada de l'article](https://pbs.twimg.com/media/HJA4l1kb0AAZ1-S?format=jpg&name=large)