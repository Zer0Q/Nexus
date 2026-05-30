---
title: "How to Steer Hermes Agent Mid-Task Without Interrupting It"
source: "https://x.com/NeoAIForecast/status/2052162023207977262"
author:
  - "[[@NeoAIForecast]]"
published: 2026-05-07
created: 2026-05-31
description: "Some AI agents are awkward once they start working.You ask them to inspect a repo, run tests, debug an error, or research something.Then hal..."
tags:
  - "clippings"
---
![Imatge](https://pbs.twimg.com/media/HHq6fbsb0AAs3Dc?format=jpg&name=large)

Some AI agents are awkward once they start working.

You ask them to inspect a repo, run tests, debug an error, or research something.

Then halfway through, you notice something:

- it is looking in the wrong folder
- it is over-focusing on one file
- it missed an important constraint
- you want the next task ready
- you do not want to fully interrupt it

In most tools, you have two choices:

```plaintext
Wait.
Or stop the agent.
```

Hermes gives you a third option:

```plaintext
Steer the current run.
```

Takeaway: Hermes lets you guide a running task without destroying the current tool loop

## The problem with normal interrupts

Interrupting sounds simple.

But in agent workflows, interruption is expensive.

If Hermes is in the middle of a tool-heavy task, it may already have:

- inspected files
- run tests
- started a server
- collected logs
- narrowed the bug
- prepared the next tool call

A hard interrupt can break that flow. Sometimes you do want that.

But often, you only want to add one constraint:

```plaintext
Focus on the auth module.
Do not edit files yet.
Check the failing test first.
Ignore the docs folder.
Use the Telegram gateway logs.
```

That should not require killing the whole run.

Takeaway: Not every correction deserves a full stop. Some corrections should become mid-run context.

## The key command: /steer

Hermes has a slash command for this:

```plaintext
/steer <prompt>
```

Example:

```plaintext
/steer focus on the gateway code, not the CLI
```

What it does:

Hermes waits for the current tool call to finish, then injects your note into the agent’s current loop.

\>It is not a new user turn

\>It is not a hard interrupt

\>It is a mid-run nudge.

The agent sees the steering note after the next tool result and can adjust its next step.

Takeaway: Use /steer when Hermes is working, but you want to change direction without resetting momentum.

## When to use /steer

Use /steer for course corrections.

Good examples:

```plaintext
/steer only inspect files, do not modify anything yet
```

```plaintext
/steer the bug happens after suspend, focus on gateway reconnect logic
```

```plaintext
/steer skip frontend for now, the issue is probably in the API route
```

```plaintext
/steer if tests fail, capture the exact error before trying fixes
```

This is ideal when Hermes is already doing the right kind of work, but needs a sharper constraint.

Takeaway: /steer is for nudging the current task, not starting a new one.

## The second command: /queue

Sometimes you do not want to affect the current task at all.

You just want to line up the next instruction.

Use:

```plaintext
/queue <prompt>
```

Example:

```plaintext
/queue after this, write a short summary of what changed
```

/queue does not interrupt the current run.

It waits until Hermes finishes, then sends your queued prompt as the next turn.

This is useful when you are multitasking with the agent and do not want to forget the next step.

Takeaway: Use /queue when the current task is fine and you want to preload the next task.

## /steer vs /queue

Here is the simple rule:

```plaintext
Use /steer to affect the current run.
Use /queue to affect the next run.
```

Examples:

Current task is debugging a failing test.

Use /steer:

```plaintext
/steer inspect the test fixture before changing application code
```

Use /queue:

```plaintext
/queue once fixed, explain the root cause in 5 bullets
```

One changes the agent’s current decision path.

The other schedules the next instruction.

Takeaway: /steer changes direction. /queue sets up what comes after.

## The CLI power move: /busy

In the Hermes CLI, there is another feature:

```plaintext
/busy
```

This controls what pressing Enter does while Hermes is already working.

Modes include:

```plaintext
/busy queue
/busy steer
/busy interrupt
/busy status
```

If you set:

/busy steer

```plaintext
/busy steer
```

then typing while Hermes is busy becomes a steering message by default.

If you set:

```plaintext
/busy queue
```

then typing while Hermes is busy queues the next turn.

If you set:

```plaintext
/busy interrupt
```

then typing while Hermes is busy interrupts immediately.

Check the current behavior:

```plaintext
/busy status
```

Takeaway: /busy lets you choose your default interaction style while Hermes is running.

## My recommended setup

For most technical workflows, I would use:

```plaintext
/busy steer
```

Why?

Because the most common mid-run action is not “stop.”

It is “slightly correct course.”

If Hermes is running tests, searching files, or inspecting logs, you can type:

```plaintext
look at the gateway logs too
```

And with busy mode set to steer, that becomes a mid-run correction instead of an accidental interrupt or new turn.

For content writing, I prefer:

```plaintext
/busy queue
```

Because the current draft should finish, and I usually want to stack the next instruction:

```plaintext
next make it punchier
```

For risky system operations, use:

```plaintext
/busy interrupt
```

That makes it easier to stop fast if Hermes is about to go somewhere you do not want

Takeaway: Use steer for coding/debugging, queue for writing, interrupt for risky ops.

## Why this matters

This feature sounds small.

It is not.

The difference between a toy agent and a useful operator is not only tool access.

It is control.

You need ways to:

- nudge without stopping
- stop when needed
- queue future work
- inspect progress
- keep the agent aligned during long tasks

Hermes treats this as part of the runtime.

That matters because real agent work is messy.

You rarely know every constraint upfront.

Takeaway: Good agent UX is not just autonomy. It is steering.

## Final thought

Most people think agent control means prompts. Hermes shows a better model.

Control is not just what you say before the run starts. It is what you can do while the run is happening.

/steer, /queue, and /busy make Hermes feel less like a chatbot and more like an operator you can guide in real time.

That is the kind of small feature that changes how you work.