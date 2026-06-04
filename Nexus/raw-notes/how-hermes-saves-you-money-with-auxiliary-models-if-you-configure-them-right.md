---
title: "How Hermes Saves You Money With Auxiliary Models, If You Configure Them Right"
source: "https://x.com/NeoAIForecast/status/2046892204518785296"
author:
  - "[[@NeoAIForecast]]"
published: 2026-04-17
created: 2026-05-31
description: "Most Hermes users optimize the wrong model.They spend hours comparing Opus vs Sonnet vs GPT-5 for the main agent, then ignore the quieter la..."
tags:
  - "clippings"
---
![Imatge](https://pbs.twimg.com/media/HGeejIAaUAADd8x?format=jpg&name=large)

Most Hermes users optimize the wrong model.

They spend hours comparing Opus vs Sonnet vs GPT-5 for the main agent, then ignore the quieter layer that keeps burning tokens in the background: auxiliary models.

Hermes uses separate model slots for side work like vision, web extraction, compression, session search, approvals, memory flushing, and more. If you leave those on expensive defaults or worse, let premium models handle cheap side tasks you can quietly overpay every day.

The good news: Hermes now makes this easier to manage through

hermes model > Configure auxiliary models

![Imatge](https://pbs.twimg.com/media/HGee_--bEAAvgxi?format=png&name=large)

This is one of the cleanest operator upgrades in Hermes because it teaches the right runtime mindset:

Use expensive intelligence where it matters, and cheap fast models where it doesn’t.

## Most people optimize the wrong layer

When people talk about running Hermes efficiently, the conversation usually starts and ends with the main model.

That makes sense on the surface. The main model handles the primary conversation, tool orchestration, and task reasoning. If you use Hermes for serious coding, research, or operations, that choice matters a lot.

But that is only part of the bill.

Hermes also runs a set of auxiliary tasks behind the scenes, things that support the main workflow without being the main conversation itself. Those calls are easy to miss because they feel like part of the product, not part of your model-routing strategy.

That is the operator mistake.

If you run a premium frontier model for the main experience and let background tasks inherit similarly expensive behavior or fail to route them intentionally you can spend premium money on work that does not need premium reasoning.

Takeaway: The expensive part of Hermes is not only your main model. It is also the sum of all the smaller supporting calls you forgot to optimize.

## What auxiliary models in Hermes actually do

Hermes Agent have auxiliary models that are lightweight models used for side tasks like image analysis, web summarization, and browser screenshot analysis. The current config/docs also show additional auxiliary routing for a wider set of runtime tasks.

From the current Hermes configuration and code paths, auxiliary routing can cover tasks like:

- vision > image and screenshot analysis
- web\_extract > web-page summarization
- compression > summarizing long conversations
- session\_search > summarizing past-session matches
- approval > classifying dangerous commands
- mcp > MCP helper reasoning
- flush\_memories > memory consolidation
- skills\_hub > skill search/matching
- title\_generation > session titles

That list matters because it changes the mental model.

Hermes is not “one model with a UI.” It is a runtime with different model slots for different jobs.

Some jobs need serious reasoning. Some need speed. Some need Multimodal capability.

Some just need fast, cheap, structured extraction.

Treating all of them like they deserve the same model is like paying a senior architect to rename your files and sort your receipts.

Takeaway: Auxiliary models are the difference between “Hermes as one assistant” and “Hermes as a routed runtime.”

## Why this saves real money

The easiest way to waste money in Hermes is to use a premium model everywhere.

That sounds obvious, but it happens in subtle ways:

- context compression fires again and again during long sessions
- web extraction runs whenever you summarize pulled pages
- session search creates summaries over retrieved history
- memory flushes happen across ongoing usage
- vision can get expensive per call when images or screenshots are involved

These are not usually the glamorous calls people brag about.

But they are exactly the calls that compound.

A helpful recent YouTube deep dive on Hermes auxiliary models made this point well: the biggest quiet cost center is often compression, because it can trigger repeatedly across long, high-context workdays. That is the kind of task where paying frontier-model prices can become silly fast.

> 17 d’abr.
> 
> Today's video was on a little-known feature of Hermes Agent, but one that can save you a lot! You can actually set different models (including local llms) to handle the background tasks you don't even notice! Check it out! @NousResearch @Teknium

The right question is not:

> What is the smartest model I can afford?

It is:

> Which tasks actually justify expensive reasoning, and which ones just need to be fast, decent, and cheap?

That is the whole operator game.

Takeaway: Savings do not come from downgrading Hermes. They come from routing low-value background work away from premium models.

## Hermes now has a cleaner way to manage this

This is why the new setup flow matters.

In the current Hermes codebase, the **hermes model** picker now includes:

**Configure auxiliary models...**

That is a deceptively important addition.

Why?

Because it makes auxiliary routing feel like a first-class operational control surface rather than a buried YAML trick.

And the implementation detail matters too: this flow does not re-run full credential setup. It is for routing already-configured providers/models to auxiliary tasks. In other words, it is designed for operators who already have providers set up and want to tune where specific side-task traffic goes.

That is exactly the right UX for this feature.

You should not have to think of auxiliary routing as an obscure expert-only hack. If Hermes wants serious operators, it should expose serious runtime controls. This does.

Takeaway: **hermes model > Configure auxiliary models...** is not just convenience. It is Hermes making runtime-level cost control more legible.

## The core routing pattern

Hermes uses a simple, reusable configuration pattern for auxiliary model slots:

- provider
- model
- base\_url

That pattern is powerful because it gives you three clear operating modes.

1\. Leave it on **auto**

This is the easiest path.

Auxiliary models default to Gemini Flash via auto-detection. That is fine for many users because it gives a low-friction, cheap-ish default without demanding per-task tuning.

2\. Route an auxiliary task to a specific provider/model

If you know a task needs a certain model, you can set it directly.

For example, the docs show patterns like:

```yaml
auxiliary:
  vision:
    provider: "openrouter"
    model: "moonshotai/kimi-k2.6"
```

That is useful when a task has distinctive needs, especially vision.

3\. Route to a direct custom or local endpoint

This is where serious savings can kick in.

Hermes lets **base\_url** override provider, which means you can point an auxiliary task at a local or custom OpenAI-compatible endpoint:

```yaml
auxiliary:
  vision:
    base_url: "http://localhost:1234/v1"
    api_key: "local-key"
    model: "qwen2.5-vl"
```

That is one of the cleanest operator moves in the whole system:

keep your premium main model for high-value work, and push side tasks onto cheaper or local infrastructure where appropriate.

Takeaway: Hermes auxiliary routing is simple on purpose. The power comes from using the same pattern repeatedly across different side-task slots.

## Which tasks should stay cheap

This is where the money gets saved. Not every auxiliary task deserves a premium model. In fact, most do not.

Best candidates for cheaper/faster routing

- compression
- session\_search
- skills\_hub
- approval
- flush\_memories
- much of web\_extract, depending on quality needs

These tasks often benefit more from:

- speed
- consistency
- low cost
- decent summarization
- structured extraction

They usually do not need the full power of your most expensive reasoning model.

That is why cheap fast models or even local ones can be such a strong fit here.

If you are using Hermes heavily for coding or research, compression is the first place I would inspect. It is exactly the kind of recurring background behavior that can quietly become a tax.

Takeaway: The highest-ROI optimization is usually not your main model. It is the repeated auxiliary task you barely notice.

## Which tasks deserve more careful model choice

Not every auxiliary task should be pushed to the cheapest option. Vision is the clearest exception

Vision is different because it is not only about cost. It is also about capability.

Hermes uses auxiliary routing for:

- image analysis
- browser screenshot analysis
- visual inspection flows

That means vision often deserves its own intentional model choice. A strong multimodal model may be worth paying for here even if you aggressively cheap out elsewhere.

Web extraction can go either way

If you use Hermes for a lot of research, web extraction can matter more than people think.

A weak summarizer can:

- flatten nuance
- miss caveats
- distort technical claims
- reduce trust in downstream outputs

So if one auxiliary task is worth slightly more spend for research-heavy operators, it may be web\_extract.

Compression needs a balance

Compression is one of the biggest cost levers, but it is also important for conversation quality. If you make it too weak, later context can degrade.

That means compression is usually the best place to optimize—but not recklessly.

Takeaway: Cheap is not the same as correct. The winning move is to match model quality to task sensitivity.

## A practical low-cost setup

If I wanted a clean, sensible budget-conscious Hermes setup, I would do something like this:

Main model

Use your premium model for the actual agent conversation:

- Claude Sonnet / Opus
- GPT-5 class models
- whatever strong frontier model you prefer

Auxiliary defaults

Start with:

- compression > cheap but competent summarizer
- session\_search > cheap fast summarizer
- approval > cheap classifier
- skills\_hub > cheap fast model
- flush\_memories > cheap structured extractor

Separate vision

Set vision independently if you care about screenshots, interfaces, or image quality.

Consider local routing next

If you already run a local OpenAI-compatible endpoint, auxiliary tasks are one of the safest and highest-value places to use it first.

That gives you a staged rollout:

1. keep main model premium
2. cheapen the frequent aux tasks
3. separate vision if needed
4. move selected auxiliary tasks to local infra later

That is much cleaner than trying to move your whole Hermes stack to local models in one jump.

Takeaway: Auxiliary models are the easiest place to start optimizing without degrading the main Hermes experience.

## Save-worthy framework

The Hermes Auxiliary Model Tuning Ladder

Tier 1 = Leave it alone

Use auto if:

- you are new to Hermes
- your costs are low
- you do not yet know which side tasks dominate usage

Tier 2 = Optimize the repeat offenders

Tune first:

- compression
- web\_extract
- flush\_memories
- session\_search

These are the likeliest places for quiet spend.

Tier 3 = Split out vision

Configure vision separately if screenshots, image inspection, or multimodal quality matters.

Tier 4 = Push some auxiliary tasks local

Use base\_url for local/self-hosted OpenAI-compatible endpoints on tasks that are frequent and low-risk.

Tier 5 = Revisit quality after savings

Do not just optimize cost. Check whether summaries, memory extraction, or visual analysis got worse.

Takeaway: Tune auxiliary models in stages. First visibility, then savings, then specialization.

## Final thought

If you only optimize your main model, you are missing the more interesting half of Hermes.

The operator win is not “pick the smartest model.”

It is:

route the expensive model only where expensive intelligence actually matters.

Hermes now gives you a cleaner path to do that through hermes model > Configure auxiliary models..., plus a consistent config pattern if you want to tune things directly.

That means you can keep the premium experience where it counts and stop paying premium rates for background work that should have been cheap all along.