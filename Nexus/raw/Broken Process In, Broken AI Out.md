---
title: "Broken Process In, Broken AI Out"
source: "https://www.linkedin.com/pulse/broken-process-ai-out-sergio-gellida-hpuze/"
author:
published: 29 de mayo de 2026
created: 2026-05-29
description:
tags:
  - "clippings"
summary:
---
*Why AI doesn’t fix a weak process, it amplifies it.*

Twenty years ago, a single large monitor fixed a data problem that no amount of training had solved.

I was working in an automotive plant in the UK, and we had just rolled out a CMMS to manage our machinery and spare parts. The process was simple. When something broke down, a supervisor walked to a terminal and created a work order. A technician picked up the job, fixed the issue, and closed the order. That gave us downtime per machine and a record of every repair.

Except nobody did it properly. Work orders went uncreated, jobs went unlogged, and within weeks the data was so unreliable that people stopped opening the reports altogether. We had a system, a process, and a dataset that were all technically working and practically useless.

We didn’t fix it with more training or a sternly worded memo. We applied a Lean technique called *visual management*: making the problem impossible to ignore. We put a large monitor in the operations office showing, in real time, exactly what was happening on the shop floor: what was broken, what was being worked on, what was sitting untouched. The bad data disappeared almost overnight. Not because people suddenly cared about data quality, but because the gap between what they did and what everyone could see had closed.

That, to me, is one of the most important moves in any transformation: make the process and the data issues *visible.* You can’t fix what you can’t see, and most broken processes survive precisely because nobody can see them breaking.

I think about that monitor constantly now that every project I work with is trying to implement AI. Because the lesson scales, and so does the mistake.

### Your AI problem is probably not (just) a data problem

When companies start implementing AI, we hear the same sentence on repeat: *garbage in, garbage out.* And of course it’s true. Feed AI poor, incomplete, or inconsistent data and it will struggle to deliver anything reliable.

But across different sectors I worked in, I’ve found that poor data is rarely the real root cause. Poor data is a symptom of something that happened much earlier.

Data doesn’t appear in a system by accident. It’s created by a process, entered by a person, supported by a system, maintained through master data, and quietly modified by the workarounds, spreadsheets, emails, and local habits that were never part of the official design. So when an AI initiative reaches a certain level of automation and stalls, the limitation usually isn’t the technology. It’s the process underneath the data.

A field is blank because the system let the transaction continue without it. A phone number is outdated because nobody owns that information. A cost center is wrong because users pick a generic “Other” when the right option doesn’t exist. A master data list is obsolete because three teams maintain three versions. The process looks clean on paper, but in reality it runs on exceptions handled through inboxes and informal knowledge.

At that point the question is not *how do we clean the data faster?* It’s *why is the process generating this data in the first place?*

### The real risk: AI amplifies whatever it sits on

Here’s why the stakes are higher now than they were with that CMMS.

A broken manual process fails slowly and locally. One supervisor forgets a work order, one machine’s downtime is wrong, and the damage stays small. A broken *automated* process fails fast and at scale. AI doesn’t fix a weak process, but it can amplifie it.

That’s the real danger of automating on top of a shaky foundation. You’re not just preserving the existing mess, you’re industrializing it.

### Bad data is free diagnostic information

This reframes how we should treat “bad” data entirely.

EDA (Exploratory Data Analysis) is genuinely useful for surfacing missing values, outliers, and inconsistencies. But if we stop at cleaning, we treat the symptom and discard the most valuable signal we have. Because every “Other” selection, every workaround spreadsheet, every blank mandatory field is the process confessing exactly where it breaks.

Companies pay consultants serious money to locate those failure points. Their own data is volunteering them for free. Delete the bad records and the model looks better tomorrow morning, but the system that produced them is still running, still generating the same problem.

Lean thinking teaches us to go upstream to the root cause instead. If invoices are missing a cost centre, the answer isn’t “the user made a mistake, drop those rows.” It’s a series of harder questions. Did the system allow the omission? Was the field optional when it shouldn’t have been? Was the correct cost centre even available? Had a generic “Other” become everyone’s shortcut? Was the master data maintained? Was the user forced to trade accuracy for speed under operational pressure?

Only once you understand the real cause can you design a process that stops creating the problem.

### Error-proofing beats training, almost every time

Once you know where a process breaks, the instinct is to train people not to break it…

Training is a weak control. It relies on memory and willpower under pressure, and both fail predictably. People change roles. People get busy. People forget. People find shortcuts, because from an evolution perspective, the human brain is wired to save energy and will always look for the path of least resistance. That’s not a character flaw, it’s how attention works. Training still matters, but it should rarely be the *primary* defence for data quality.

A good system does the work that training can’t. This is *Poka-yoke*, error-proofing: making the right action the easiest action. If only certain values are valid, the system guides the user to them. If a field is critical, the process can’t continue without it. If a master data table drives automation, it gets a clear owner. And if “Other” is one of your most-selected options, your taxonomy is broken and no workshop will fix it.

Back in that same plant in the UK, we hit exactly this. When technicians closed a work order, they had to pick a category from a long drop-down list, and they routinely picked the wrong one or whatever sat at the top. The data was useless not because they were careless but because the list was. So we replaced it with a tree: a small set of logical branches that narrowed down to the right category in a few clicks, organised the way the technicians actually thought about their work. Selecting the correct option became faster than selecting a wrong one, and the data quality followed.

But we didn’t stop at the interface. We ran weekly meetings with the technicians to review the data they’d entered, so they could see what their input produced and where it fell short. That did two things. It gave them genuine ownership of the data, and it turned them from data-entry endpoints into participants improving the system itself. They flagged confusing categories, suggested better branches, and caught problems we never would have seen from a meeting room. The fix was half system design, half putting people at the centre of it, and neither half would have worked alone.

Design the system so the right path is the easy path, give the people who use it a real stake in it, and most of your data quality problems never get created.

### Go to the Gemba

There’s one more reason these problems persist: we try to solve them in the wrong room, but most importantly with the wrong people.

Most transformation projects diagnose process and data issues in meetings with managers, process owners, and strategic stakeholders. Those people matter, but they’re usually not the ones who know how the work actually happens. The person entering the first piece of data knows things no dashboard will tell you. The person handling the exception knows precisely where the process breaks. The person living in the system every day knows which fields confuse everyone, which steps get skipped, and which parts of the official process exist only in theory.

In Lean this is the *Gemba*, the place where the real work happens. If you want AI to work, sit with those users, watch the work, and bring them in from day one. Because AI transformation isn’t really a technology project. It’s change management, and people belong at the center of it.

This is also where AI earns its keep before it automates anything. An AI agent is not just a tool to do tasks faster, it’s a tool for *visual management* at scale: a way to make process problems visible (which is exactly what that monitor did, two decades early and without the AI). If critical information is missing, surface it. If the same exception repeats, report it. If the process isn’t being followed, trigger an alert. The point is never to blame people. It’s to expose the process, because once a problem is visible it can be discussed, understood, and fixed. And when people see the immediate impact of their actions, behavior changes on its own.

### People, then process, then technology

So I keep coming back to the same sequence.

People first, because they understand the real work. Process second, because automation only scales when the process underneath it is stable, clear, and owned. Technology third, because AI should be the enabler, not the starting point.

There’s a human mechanism underneath that ordering, and it’s worth being explicit about. People are wired to engage with change through two chemical rewards. Oxytocin, the hormone of belonging, is released when we feel part of a group working toward something together. Dopamine, the reward of progress, is released when we hit a goal or clear a milestone. A transformation that ignores both feels like something being *done to* people, and they resist it. A transformation that uses both feels like something they’re part of, and they drive it.

Practically, that means two things. Make people part of the change from the start, so they feel ownership rather than imposition. When something doesn’t work, and in any real transformation plenty won’t, they have a voice and a stake instead of a reason to disengage. That’s the oxytocin: the safety of being part of something bigger than themselves, which lowers the stress and defensiveness that kill change programs. Then set clear targets, share them openly, and celebrate each one you hit, the next milestone, the next process fix, the next measurable jump in data quality. That’s the dopamine: visible, repeated proof that the effort is working. Belonging makes people willing to start, progress makes them want to continue.

AI hasn’t changed the rule, it has only raised the cost of breaking it, because AI takes whatever process you give it and multiplies it faster and further than any system before it.

Maybe *garbage in, garbage out* is still true. But in a large organization, where automation multiplies whatever you give it across thousands of transactions, I think we need a sharper version:

**Broken process in, broken AI out.**