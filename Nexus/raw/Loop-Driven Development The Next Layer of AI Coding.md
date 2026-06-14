---
title: "Loop-Driven Development: The Next Layer of AI Coding"
source: "https://x.com/bibryam/status/2065445933601435823"
author:
  - "[[@bibryam]]"
published: 2026-06-12
created: 2026-06-14
description: "Coding has always been in loops.Write code, run it, check the result, change it, repeat. That loop is older than AI. TDD made it explicit wi..."
tags:
  - "clippings"
---
![Imatge](https://pbs.twimg.com/media/HKnaFkyWEAEpo56?format=jpg&name=large)

**Coding has always been in loops.**

Write code, run it, check the result, change it, repeat. That loop is older than AI. TDD made it explicit with red, green, refactor. BDD widened it toward behaviour. Acceptance testing widened it toward user intent. CI widened it toward delivery.

So when people talk about **loop engineering**, the interesting question is not whether software has loops. It always did.

The question is: **what is inside the loop now?**

With AI coding, the unit of work keeps getting wider. It used to be a line, a function, or a failing test. Now it can be a task, a pull request, a migration, or a recurring workflow.

I think AI coding has moved rapidly through five phases.

**1\. Autocomplete Era**

The model helped with the next edit. Copilot and Cursor Tab made this mainstream. The loop was still mostly human-controlled: type, inspect, accept or reject, continue.

What got added: → model → local file context → inline completion

The benefit was speed. The limit was scope. The model helped write the next piece of code, but it did not own the task.

**2\. Prompt Engineering Era**

The model moved from completion to task steering. You could ask for a script, a test suite, an explanation, or a migration plan. The loop became: ask, generate, inspect, retry.

What got added: → goal → instructions → tools → prompt loop

The benefit was delegation. The limit was convergence. A prompt loop without good context or a clear stop condition can drift, repeat itself, or finish the wrong thing.

**3\. Context Engineering Era**

Once agents could act, the bottleneck became what they could see. A coding agent needs more than a prompt. It needs files, tests, logs, conventions, architecture notes, issue history, and current repo state. The loop became repo-aware: read context, edit files, run commands, inspect result.

What got added: → repo context → terminal access → file editing → test execution

The benefit was scope. The limit was correctness. A well-contextualized agent can still do the wrong thing if the environment cannot tell it what done means.

**4\. Harness Engineering Era**

A harness is the environment around one agent run. It includes prompts, tools, repo context, sandbox, permissions, tests, linters, type checks, CI, evals, and review gates. The loop became constrained and checkable.

What got added: → sandbox → verifier →permissions →CI and eval harness → review boundaries

The benefit was repeatability. The limit was continuity. One agent run can be made safer, but real work often continues across failures, events, reviews, schedules, and state.

**5\. Loop Engineering Era**

This is the next layer. A loop is not just automation. Automation executes fixed steps. A loop checks the result, decides whether to continue, and uses feedback to improve the next iteration.

That is where AI coding starts to look different. The engineer is no longer only writing code or prompts. The engineer is designing the system that lets an agent keep working safely.

The shift looks like this: → **Autocomplete made coding faster.** → **Prompting made generation broader.** → **Context made agents repo-aware.** → **Harnesses made agent runs checkable.** → **Loops make agent work repeatable.**

That is the move from **test-driven development** to **loop-driven development**.

Not because tests stop mattering. Because tests become one part of a larger loop. The old loop was: write test, make it pass, refactor. The new loop is: set intent, run agent, verify result, repair failure, repeat or escalate. The important word is not “AI.” The important word is **verify**. Without verification, you do not have a loop. You have repeated prompting. With verification, the loop can converge.

Software engineering was always a loop. AI is widening the loop again.

**Build the loop. Stay the engineer.**

👉 I wrote the full version with diagrams, examples, and the full evolution from autocomplete to loop engineering here:

![Imatge](https://pbs.twimg.com/media/HKnb-ufWIAEu6j2?format=jpg&name=large)

The Evolution of AI-Assisted Coding Overview

[https://generativeprogrammer.com/p/from-test-driven-to-loop-driven-development](https://generativeprogrammer.com/p/from-test-driven-to-loop-driven-development)