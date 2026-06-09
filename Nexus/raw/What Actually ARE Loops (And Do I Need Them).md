---
title: "What Actually ARE Loops? (And Do I Need Them?)"
source: "https://x.com/tonbistudio/status/2063861151524643291"
author:
  - "[[@tonbistudio]]"
published: 2026-06-08
created: 2026-06-09
description: "Two statements about \"loops\" went around recently and pulled a lot of attention. People keep quoting them, but I saw a lot of confusion sinc..."
tags:
  - "clippings"
summary:
---
![Imatge](https://pbs.twimg.com/media/HKRNmOoaoAA8VTw?format=jpg&name=large)

Two statements about "loops" went around recently and pulled a lot of attention. People keep quoting them, but I saw a lot of confusion since there was no "step-by-step" tutorial to setting these things up. In fact the term "loop" has been used so often with coding agents that many people didn't even know what they were talking about. So I want to fix that.

The first came from Boris Cherny ([@bcherny](https://x.com/@bcherny)), who works on Claude Code at Anthropic:

> "At that point I was running maybe five, 10 Claudes in parallel and my coding was prompting Claude to write code. Now it's actually leveled up, I think, again to the next abstraction where I don't prompt Claude anymore. I have loops that are running. They're the ones that are prompting Claude and kind of figuring out what to do. My job is to write loops. And this is this kind of next transition that I think we're going to see in the next few months, maybe through the rest of the year."

The second came from Peter Steinberger ([@steipete](https://x.com/@steipete)), the creator of openclaw:

> "Here's your monthly reminder that you shouldn't be prompting coding agents anymore. You should be designing loops that prompt your agents."

Two different companies, two different tools, same message. Stop prompting your agent. Start building the thing that prompts your agent for you.

That sounds great on a slide. It's also super confusing if you don't already know what they mean. So I did some digging into both of these men's talks and writings to get a more concrete answer to this core question: What's a loop and what's it used for? This article is going to lay out what a loop actually is, whether you personally need to care, and then how each of these two sets them up in practice with real examples. Boris first, then Peter. I'll save my own take for the end.

And if you like this article and want to see me making my own loops and agentic workflows, check out my YouTube Channel at [www.youtube.com/@TonbisAIGarage](https://www.youtube.com/@TonbisAIGarage)

## What is a loop?

Forget the for-loop from your first programming class. That's not what they are talking about.

A loop here is a recurring, tool-using, self-verifying agent process. Something kicks it off. The agent does work. The agent checks its own work against some signal. Then it either runs again or stops and tells a human. You write that structure one time, and from then on the machine is the thing prompting the model.

Boris puts it on a ladder of abstractions. His grandfather used punch cards. His dad wrote assembly. Boris wrote Python, then moved to autocomplete in an IDE, then uninstalled the IDE entirely once he was living in Claude Code. After that he was running five to ten Claudes in parallel and prompting each one by hand. Loops are the next step up. He no longer writes the prompts. He writes the system that writes the prompts.

Peter comes at it from the opposite direction and lands in the same place. His version is simpler to picture. An agent builds a feature, says it's done, and Peter opens the browser to check it, then tells the agent what's broken, and the agent fixes it. After doing that loop by hand enough times he asks the obvious question.

"Why am I the one looking at the browser?"

The agent should take the screenshot itself. That single realization is the whole philosophy. If you keep doing the same observation or check for your agent, build a tool so the agent can do it without you.

Both descriptions share one skeleton. A trigger, some context, tools to act with, a way to verify the result, a repeat condition, and a rule for when to stop and call a human. The verification piece is the part people skip, and it's the part that matters most. Skip it and you don't have a loop. You have a token bonfire with a calendar invite.

## Does everyone need to be using them?

No. And I think that's worth saying plainly before anyone panic buys 100 MAX Claude subs.

Loops pay off when the work has two properties. It repeats, and the agent can check whether it got the answer right. PR maintenance repeats. Flaky tests repeat. Profiling against a memory target gives a clean pass or fail. Those are loop-shaped problems, and if that's your day, you are leaving a lot on the table by babysitting every step.

If your work is mostly one-off, exploratory, or hard to verify without a human eye, a loop is the wrong tool. If it requires human creativity, or the ability to glance at a design and say "yeah that's trash," stick to prompts. Wiring up a recurring job to do something you'll do once is just extra plumbing. You also need real guardrails before you let one run unattended, which means auto-verification and a sane stop condition, not blind trust.

So the honest answer is that loops are a frontier skill, not a daily requirement. Boris and Peter live in codebases with thousands of agent-hours and constant inbound signal, so loops are obviously worth it for them. Most people are not there yet. But the shape of the skill is worth understanding now, because the tools are clearly heading this direction.

## Boris: loops as the next programming interface

**His view**

Boris's core claim is that the valuable skill is shifting. It used to be crafting the perfect prompt. Now it's designing a repeatable system that keeps working without you steering every step. In his words, his job is to write loops.

He's blunt about how unglamorous this is. He describes Claude Code's /loop as "the simplest thing that works." There's no magic. Under the hood it's Claude using cron to schedule a job, marking it as recurring, and running it on whatever interval you pick. Every minute, every five minutes, every day, whatever fits.

So the formula is almost boring. Claude plus cron plus a recurring prompt plus tools plus a little memory of what it already tried. That's a loop.

**How he sets them up**

A few details make his version actually work at scale.

First, self-verification is non-negotiable. He says you can only push to hundreds of agents in parallel if each one can check itself, because otherwise the human becomes the bottleneck and the whole thing stalls. The goal of every loop is to produce enough proof that a human can glance at it and merge with confidence.

Second, there's a server-side version called routines. Same idea as /loop, except it runs on the server instead of your laptop, so it keeps going after you close the lid. Local for quick stuff, routines for things that should never stop.

Third, the model is starting to reach for loops on its own. He gave an example where he asked Claude to pull a data query, Claude noticed the data changes over time, and Claude offered to send him a report every 30 minutes. He then asked it to deliver that over Slack, and it wired up the Slack integration itself. The agent recognized a recurring task and proposed monitoring it without being told.

Fourth, loops compound through memory. Every time the agent trips over the same thing, that lesson goes into Claude.md. Build commands, how to run tests, how to read CI errors, prior gotchas. Each failure becomes future context, so the loop gets smarter every cycle instead of repeating the same mistake.

He also makes a point about not burning tokens forever. A mature loop should turn repeated steps into actual scripts and tools rather than calling the model for the same operation a thousand times. Have the model write the program once, then run the program for free.

**Examples**

Boris gives several concrete loops he runs.

1\. **PR babysitter.** Every few minutes it checks his open PRs, finds CI failures, merge conflicts, and stale branches, fixes what's safe, pushes the update, and flags anything that needs a human.

2\. **CI health.** It watches for flaky and broken tests, reproduces them when it can, patches or quarantines them, and reruns CI.

3\. **Feedback clustering.** Every 30 minutes it pulls new Twitter feedback, clusters it by theme, and summarizes what changed since the last run.

4\. **Idea mining at scale.** He's had a couple hundred Claudes reading Twitter, GitHub issues, and Slack at once, figuring out what to build next. Most ideas are bad, but he says roughly 20% are good, and that's the point of letting it run wide.

The strongest example isn't even his own. He points to Robo Bun, built by Jarred Sumner from Bun, as a real production loop with teeth. When someone files a GitHub issue, the bot fires automatically, tries to reproduce the bug, writes a failing test, fixes the code, and opens a PR. The PR has to include a test that fails on the old version and passes on the fix. Review bots critique it, the fix agent responds, and only then does a human decide to merge. That's not "ask Claude to fix a bug." It has proof gates.

He calls the underlying primitive hill climbing. Give Claude a target and a way to measure progress, tell it to iterate until it's done, and it just goes. Jarred told it to "make it faster than sharp," and Claude ran the benchmark, found the bottleneck, patched the code, reran, and kept climbing until it hit the target. Target plus metric plus the ability to change things plus the ability to measure equals an autonomous improvement loop.

If you want his short checklist for running an agent unattended for hours, it's five things. Auto mode for permissions so it stops asking. Dynamic workflows so it can orchestrate many agents. /goal or /loop to keep it going. Cloud Claude Code so you can close your laptop. And above all, a way for it to verify its own work end to end.

## Peter: remove yourself from the feedback path

**His view**

Peter's framing is a little different and, honestly, the cleaner mental model for getting started. He says your job is no longer to figure out how you build software faster. Your job is to figure out what you can do to help your agent build software faster. He calls it closing the loop.

The method is one sentence. Every time you catch yourself doing repetitive observation, judgment, routing, or verification for the agent, build a tool that hands that job to the agent. Remove yourself from the feedback path.

And he gives you a signal for finding these moments. Listen when you're annoyed. Annoyance means you're doing something a machine should be doing, which means it's ready to be automated. That's the trigger for building a new loop.

**How he sets them up**

Peter's loops lean less on cron and more on tooling and policy.

The policy layer is a vision.md file. It's the project's constitution. The agent reads it to know what the project wants, what it rejects, and which direction to push. Without that document, a loop just optimizes toward whatever random contributors happen to ask for, which is a mess.

The behavior layer is agents.md, where he writes invariants. When an agent misunderstands the project, he doesn't lecture it in chat. He writes the rule into the instructions so future sessions inherit it. There's a clever twist here. He doesn't write those instructions himself. He asks the agent to rewrite the guidance for the next agent, then periodically asks it what in the file is confusing and cleans up the contradictions. The agents improve the instructions that control future agents.

One warning he gives is worth repeating. Agents will over-defend against imaginary edge cases unless you tell them what actually matters, so you have to tune your invariants or you'll drown in pointless defensive code.

**Examples**

A handful of Peter's loops show the range.

1\. **Issue and PR reaper.** He treats an issue or a PR as the same thing, a signal that someone wants a change. An agent reads vision.md, decides whether the request fits the project's direction, then comments, groups, or closes it. He reruns this at least weekly, daily if he wants to spend the tokens.

2\. **Maintainer report.** It crawls Discord, issues, and PRs, correlates complaints with open work, picks the top five things people are screaming about, matches them against vision.md, selects the ones agents can handle alone, and dispatches agents in parallel. Community pain in, prioritized agent work out.

3\. **Mantis, the video proof loop.** Ping the agent on a PR, it spins up machines, records a video of the bug, fixes it, then records a video of the fix. The agent watches the video to verify, and Peter watches it to press merge. It's the cleanest proof loop in his whole talk.

4\. **Auto Review.** This is his answer to running /review by hand over and over. Before a commit lands, Codex calls Codex with fresh context and runs many rounds of review, fixing valid issues until it's clean. He set it up with a single line in agents.md telling the agent to run auto review before it commits.

A few of his other builds exist purely to let agents verify things themselves, which is the same instinct from a different angle. Crab Box spins up remote Linux test boxes in the cloud to run tests in parallel when local testing got too slow. A VNC setup lets an agent open a real browser, screenshot, click, and reproduce UI bugs without him touching the mouse. He even built a controlled fake messaging platform because real services kept blocking his agents with CAPTCHAs, so he made a smaller world the agent could actually test in.

Same pattern every time. He was the bottleneck, he got annoyed, and he built the agent a tool so it could do that part alone.

## So, to loop or not to loop?

I hope this article at least gives you a better image of what a loop is, and when you should be using them. I myself use two types of loops right now: multi-agent workflows and goals.

If you watched my video last week, you'll have seen my multi-agent workflow using Hermes Agent Kanban (I have another coming tomorrow). That is a pretty autonomous loop, I set a cron schedule, my agents do research, decide if anything needs to be done, build out a plan, and I verify it, then they get to work, and finally verify their work. Then the whole thing starts again at the next cron.

The more traditional loop comes from /goal, which I use for larger, multi-component projects or my own ML experiments (where I also incorporate auto-research). I create a very specific goal.md file that sets the purpose of this task, a list of deliverables I expect at the end (the goal objective), specific rules about what can and cannot be adjusted in the work (I'll give them leeway with tech stack choices, not with completely rewriting the focus of the project), and perhaps most importantly an escape hatch so they aren't stuck in a never-ending loop. Usually something like "if you get blocked and cannot resolve it in 3 attempts on a critical element of the project, stop."

I find these goal.md files are crucial or you'll burn a ton of tokens and time with useless work. When you get it to work though, it's like magic.

So to loop or not to loop? I think understanding loops is important and experimenting with them in places where they'll actually be useful is a good thing, but I don't think you need to rush out to adopt these exact approaches or force loops into stuff that'll just be better off with normal prompting. We don't all have unlimited tokens, and that's okay. You won't be banished to the permanent underclass, you won't be hopelessly left behind, you'll be fine. Just build a loop for yourself: learn, experiment, verify, design, execute, review. Then loop it.