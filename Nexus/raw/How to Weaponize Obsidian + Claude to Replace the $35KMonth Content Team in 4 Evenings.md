---
title: "How to Weaponize Obsidian + Claude to Replace the $35K/Month Content Team in 4 Evenings?"
source: "https://x.com/zeuuss_01/status/2060364984052285459"
author:
  - "[[@zeuuss_01]]"
published: 2026-05-29
created: 2026-05-30
description: "The Capture/Use Gap (Why Most Vaults Earn $0)You read an interesting article. You highlight a passage. You file it under /articles. Six mont..."
tags:
  - "clippings"
---
![Imatge](https://pbs.twimg.com/media/HJfi_q7W8AQPWpv?format=jpg&name=large)

## The Capture/Use Gap (Why Most Vaults Earn $0)

You read an interesting article. You highlight a passage. You file it under /articles. Six months later you search for something vaguely related and find the note by accident. You read it, think "I should have remembered this," and move on.

**That note never became anything.**

It never became a tweet. A newsletter. A client strategy. A pricing argument. A pitch deck. A blog post. A product feature. A talking point. A consulting recommendation.

It just sat there.

The mistake is structural. Most Obsidian setups optimize the inbox. The exit is unstaffed.

- You have 4,000 notes and zero published posts.
- You have 12 capture surfaces and zero output workflows.
- You have a pretty graph view and no client deliverables.

The vault that earns money does the opposite. It is optimized backward from the output.

## The 4-Zone Vault (Built Backward From Output)

Forget the 9 folders from the last article. For monetization specifically, you collapse the vault into 4 zones:

![Imatge](https://pbs.twimg.com/media/HJfRSygXMAErfn7?format=png&name=large)

The asymmetry is the point. **Most of your day lives in 02 and 03.** Capture sits at 00. Context backs it. But the work - the billable, publishable, shippable work - lives in 02 PROJECTS and 03 OUTPUT.

You should know how many notes were generated in 03 - OUTPUT/ this week without thinking about it.

If the answer is zero, the vault is a hobby. Not a business.

## The 3 Capture Surfaces

You cannot ship from an empty vault. The capture layer needs to be aggressive enough that you literally cannot lose an idea.

Three surfaces cover every situation:

- **Surface 1 - QuickAdd (at desktop):** One keyboard shortcut. A floating input box. The note lands in today's daily note. No friction. No categorization at capture time. Claude does categorization later.
- **Surface 2 - Mobile widget (phone in hand):** Tap the home screen widget. Type or voice-to-text. Note syncs to the vault in 30 seconds.
- **Surface 3 - Telegram bot (phone NOT in hand):** Walking, in the car, mid-conversation. Voice-message to a Telegram bot. Lands in the Captures section of today's daily note.

The Telegram bot is the highest-ROI piece of infrastructure in the entire stack because it captures the ideas you would otherwise lose forever - the ones on walks, in the shower, mid-Uber.

Those ideas are disproportionately the ones that become money.

![Imatge](https://pbs.twimg.com/media/HJfR1QfXwAEUXRD?format=jpg&name=large)

## The 5-Workflow Output Engine

The vault becomes income-producing when 5 workflows run on top of it. Each one is a prompt living in 07 - SYSTEM/prompts/. Each one is scheduled or triggered. Together they turn raw capture into shippable output.

Workflow 1 - Nightly Processor (2 AM)

Classifies the day's captures by note type. Moves them from 00 - CAPTURE/ to 01 - CONTEXT/. Adds frontmatter. Pure mechanical work.

Workflow 2 - Morning Brief (6 AM)

Reads the last 7 days of context. Writes a 400-word briefing into /BRIEFINGS/. Surfaces patterns, contradictions, one non-obvious connection.

Workflow 3 - Connection Surface (Sundays)

Looks across 30 days of context. Returns 3 connections you would NOT have found by deliberate search. This is where original ideas get born.

Workflow 4 - Project Updater (Manual, weekly)

For each active project in 02 - PROJECTS/, reads the latest captures relevant to that project. Updates the project doc. Suggests next moves.

Workflow 5 - Output Generator (Manual, on demand)

The money workflow. You tell Claude what you need to ship. It reads the relevant notes from 01 and 02. It produces a complete draft of the output in your voice. Saves to 03 - OUTPUT/.

Example prompt for the Output Generator:

![Imatge](https://pbs.twimg.com/media/HJfSGOmXYAYL3ru?format=png&name=large)

This is the prompt that turns 4,000 dormant notes into shippable, billable work.

## Where the $30K Actually Comes From

Here's the math, broken out. None of these require you to be exceptional - they require you to ship consistently from a vault that compounds.

![Imatge](https://pbs.twimg.com/media/HJfSew6XoAA7j_B?format=jpg&name=large)

Two important framings:

- None of these lines require a specific skill you don't have. Each one requires **shipping from a vault that compounds**.
- You don't need all 4. Hit any 2 reliably and you're at [$13-25K](https://x.com/search?q=%2413-25K&src=cashtag_click)/month with one folder on your laptop.

## The 5-Tool Stack Around Claude

The stack that ships $30K/month from a vault has five distinct layers. Each tool owns its layer in a way nothing else replicates.

- **Claude** - the reasoning and context layer. 200K window. Holds the whole vault during synthesis. Writes drafts that sound like you.
- **Obsidian** - the memory layer. Plain markdown. Local. Yours. Survives every model swap.
- **Kimi K2.6 / open models** - the orchestration layer. Long-horizon tasks Claude doesn't have to babysit. Open-source. Free. Runs 4,000 steps without flinching.
- **Cursor** - the execution layer. For when output is code or product. Cloud handoff means your laptop can close.
- **N8N** - the automation layer. $5/mo droplet. Schedules every workflow. Routes captures. Runs the whole loop while you sleep.

The mistake almost everyone makes is using one tool for all five layers. ChatGPT for everything. Or Claude for everything.

The $30K vault uses the right tool at each layer. Claude is the brain. Obsidian is the memory. Open models scale the cheap stuff. Cursor ships when ships is required. N8N glues it.

![Imatge](https://pbs.twimg.com/media/HJfTGOOWsAMTsg-?format=jpg&name=large)

## The Output Generator Prompt That Earns the Most

Of the 5 workflows, the Output Generator is the one that produces revenue directly. The other 4 feed it.

Here is the production version of the prompt - tuned across 6 months. Drop it into 07 - SYSTEM/prompts/output-generator.md:

![Imatge](https://pbs.twimg.com/media/HJfZiueXcAQliVf?format=png&name=large)

The expected\_revenue stamp at the bottom matters. After a few weeks, you have data on which note types and which topics produce the highest-value output. The vault starts telling you what to capture more of.

## The 6-Month Revenue Curve

This is what compounds for $30K - and it does NOT happen on Day 7.

![Imatge](https://pbs.twimg.com/media/HJfZxenXwAIf_7M?format=jpg&name=large)

The 6-month curve is the moat. Anyone can install Obsidian today. Almost nobody will still be capturing in 90 days.

The people who are will own a context layer no late mover can replicate.

## The Step-By-Step Build (4 Evenings, $0)

Same 4-evening build from the last article - adapted for the income engine. Total: ~6 hours.

![Imatge](https://pbs.twimg.com/media/HJfb0qbW8AMfW4g?format=jpg&name=large)

![Imatge](https://pbs.twimg.com/media/HJfb4fjXcAQs5y3?format=jpg&name=large)

![Imatge](https://pbs.twimg.com/media/HJfb8dvXEAEqhhV?format=jpg&name=large)

![Imatge](https://pbs.twimg.com/media/HJfcAvAXEAEt1bk?format=jpg&name=large)

## The Mistake That Keeps This at $0

Most people who build the vault never reach $30K because of one mistake:

**They never ship from it.**

They capture. They run the briefings. They tweak CLAUDE.md. They post screenshots of their graph view on X.

They never open 03 - OUTPUT/. They never run the Output Generator. They never publish.

The vault is not magic. It does not produce revenue by existing.

The vault produces revenue when you run Workflow 5 and ship the result. Once a day. Or twice a week. Or once a Sunday.

The shipping cadence is what closes the gap between "I have a vault" and "I make $35K/month."

![Imatge](https://pbs.twimg.com/media/HJfcUI_XwAQy3gW?format=jpg&name=large)

## The Quiet Truth Underneath All Three Articles

None of them show you the shipping loop because that is the one part nobody can hand you. The structure is replicable. The capture is replicable. The tools are replicable.

**The shipping discipline is not.**

That is what the $35K/month operator has that the 4,000-note hobbyist does not. Not better prompts. Not a better model. Not a fancier folder structure.

A standing order with themselves to ship from the vault, every week, no matter how rough the draft.

The vault rewards that discipline disproportionately.

Six months of capturing + 6 months of shipping = a context layer AND a body of public work nobody else can copy.

That is the $35K/month moat.