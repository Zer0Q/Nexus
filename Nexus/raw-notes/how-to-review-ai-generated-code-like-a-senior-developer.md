---
title: "How to Review AI-Generated Code Like a Senior Developer"
source: "https://x.com/Tech_girlll/status/2068009335909761161"
author:
  - "[[@Tech_girlll]]"
published: 2026-06-19
created: 2026-06-22
description: "I'm sure by now, we already know this: \"AI can write a working feature in seconds.\" The code looks clean, sounds good, and 90% of the time, ..."
tags:
  - "clippings"
summary:
---
![Imatge](https://pbs.twimg.com/media/HLMKoUtWsAAhqYr?format=jpg&name=large)

I'm sure by now, we already know this: "AI can write a working feature in seconds." The code looks clean, sounds good, and 90% of the time, runs. But running and being safe to ship are not the same thing, and the distance between them is where most of the work now sits.

The numbers back this up. One 2026 study found that only about 35% of AI-generated backend code was both secure and correct. A separate test by Veracode ran over 100 models across 80 tasks and found that nearly half of the code they produced shipped with a known security weakness in it. None of this code looked broken. It compiled, it passed the obvious tests, and the problems were sitting underneath where a quick read never reaches.

So reviewing AI code turns out to be its own skill, and it is not the same skill as writing code. The code shows up without the thinking that should come with it. The model guessed its way there based on patterns it had seen, and it genuinely cannot tell you why it made the choices it made. That means checking that it works is not enough. You have to go through the layers underneath, which is what an experienced reviewer does almost without noticing.

I review a lot of AI-generated code, both my own and other people's, and over time, the process has settled into a rough order. This guide is in that order. For each step, you get what the idea actually means, why it bites you if you skip it, and how to deal with it, plus a link if you want to go deeper.

## Three things to know about AI before you start

Almost every habit below traces back to one of these.

The first is that these tools are built to give you a believable answer quickly. That is the whole optimization. Believable and correct overlap a lot of the time, which is exactly what makes the gap dangerous, because you stop expecting it.

The second is that when your request leaves something out, the model does not stop to ask. It fills the gap with whatever was most common in its training data. So you get the popular framework, the standard folder structure, the default everything, regardless of whether your situation calls for it.

The third is the one that catches people: the model sounds exactly as sure when it is wrong as when it is right. There is no tell. You cannot lean on its confidence, which means you have to actually check the things that matter, especially names, numbers, and anything in a domain you do not know well enough to catch the error yourself.

## Step 1: Start with the problem, not the code

Before you can judge whether a code is good, you need to know what it was supposed to do. Sounds obvious. Almost nobody does it first.

Here is why it matters. AI can solve the wrong problem flawlessly. Ask for "an endpoint to update invoices," and you get clean, working update logic, usually with no check for whether the person calling it is allowed to. The code is correct. It just answers a question nobody should have asked. And you can sign off on something genuinely well-written and still ship a mistake, because you never confirmed it was the right thing in the first place.

So find the requirement before you read the implementation. A ticket, a spec, a sentence someone wrote down, anything. If all that existed was a one-line prompt, be extra suspicious, because the model filled every unstated gap with a guess, and you are now reviewing those guesses, too. Then read the code as a comparison: here is what was asked for, here is what got built, do they match? If you cannot state in one sentence what the code was meant to solve, you are not ready to review it yet.

Atlassian has a short, practical guide to writing requirements if you want a starting point: [https://www.atlassian.com/agile/product-management/requirements](https://www.atlassian.com/agile/product-management/requirements)

## Step 2: Question the engineering decisions

Every piece of code carries decisions inside it. Which framework, which database, how to structure the thing. A real engineering decision weighs options against each other and picks one for a reason. The model usually skips that part and reaches for the common default, and your job is to notice when the default does not fit.

I will give you the example that taught me to watch for this. I work mostly in Django, and Django is excellent, so I am not knocking it. But say the task is a small service that has to handle a lot of requests at once and spends most of its time waiting on other services. That is a shape where something async-first, like FastAPI, can fit more naturally. Ask an AI for it and you will very often get Django anyway, because "Python web backend" maps to "Django" in the training data more than anything else. The model did not weigh the tradeoff. It pattern-matched. And six months later someone is fighting the framework with no idea why it was picked, because the honest answer is that nobody picked it.

The same thing shows up when a relational database gets used for data that is really just loose documents, or when some heavyweight design pattern appears because it is common in example code, not because the problem needs it.

The fix is one stubborn question on every major choice: does this fit my case, or is it just the popular answer? Make the code earn the decision. "Because it is common" does not count. When you cannot find a real reason a choice fits, that is worth flagging.

Dan McKinley's "Choose Boring Technology" is the best thing I have read on weighing these tradeoffs: [https://boringtechnology.club/](https://boringtechnology.club/)

## Step 3: Read the logic, not the spelling

Two different things often get lumped together here, so quickly: syntax is the spelling and grammar of code, the brackets and keywords. Logic is whether the thing actually does what it should, the order of operations and conditions and how data moves through. This step is entirely about the second one.

The reason is simple economics. Syntax errors get caught for free by the compiler and the linter, the tools that automatically flag broken or sloppy code. Those are the cheap bugs. The expensive ones live in the logic, and they slip through a quick read precisely because the code looks polished on the surface. Polished and correct are not related.

So trace it the way you would on a whiteboard. Follow the data from where it comes in to where it goes out, and check the behavior against the requirement, not against what merely looks reasonable. The questions that actually turn up bugs are about the edges: What happens with an empty list, a zero, a negative number, the largest possible value, the count that is off by one? What happens when two things run at the same time and step on each other, which is called a race condition, and almost never shows up in a calm read? And what is the failure path for each step, not just the success path?

Generated code is tuned to look right on the one path the prompt described. The edges are where it quietly falls apart, because the edges are exactly what the prompt left out.

If boundary thinking is new to you, this is a decent primer: [https://www.geeksforgeeks.org/software-testing/boundary-value-analysis-in-software-testing/](https://www.geeksforgeeks.org/software-testing/boundary-value-analysis-in-software-testing/)

## Step 4: Hunt the hidden assumptions

This is the step that has caught the most real bugs for me, so I want to spend a minute on it.

An assumption is something the code quietly needs to be true in order to work. The hidden ones are the assumptions nobody wrote down: that the input will be valid, that the other service will respond, that the user actually exists. The code is complete, but only for a world where all of that is always true, and that world is kinder than the one your code runs in.

These are invisible in a calm read because the code genuinely works while the assumptions hold, and they hold most of the time. Then on an ordinary Tuesday a third-party API goes slow, or someone sends a malformed request, and the assumption nobody checked turns into an incident. The usual suspects:

- **Inputs are always valid.** Nothing checks or cleans the incoming data, so the malformed request a real user will absolutely send either breaks something or opens a hole.
- **External services always answer.** A call goes out, the response gets used, and there is no plan for a timeout, an error, or a half-finished reply.
- **The record always exists.** A user or row or file gets fetched and used right away, with no branch for when it simply is not there.
- **The network always works.** No retries, no time limits, no acknowledgment that a connection can just drop mid-request.

Read the code asking the same question over and over: what is this taking for granted? Every time you find an assumption, add the path that handles it being false. Validate the input. Handle the failed call. Check the record exists. Set a timeout. An unchecked assumption is just an incident that has not happened yet.

Google's Site Reliability Engineering book has a free, readable chapter on building for failure: [https://sre.google/sre-book/embracing-risk/](https://sre.google/sre-book/embracing-risk/)

## Step 5: Go through the security, deliberately

This is the one step I will not let myself rush, and the reason is that the model will happily hand you code that works perfectly and is wide open at the same time. Those two facts have nothing to do with each other as far as the model is concerned.

A handful of failures come up again and again, so here is each one in plain terms.

**Authentication** is checking who someone is. A gap here means the code does its job but never actually confirms the identity of the caller, so anyone can walk in. **Authorization** is the next question: what is this person allowed to do? This is the big one. The latest OWASP Top 10, the industry's standard list of the most common web vulnerabilities, ranks broken access control at number one, and in their testing, 100% of applications had some form of it. Models are good at writing the business logic and bad at consistently enforcing who is allowed to run it. That invoice endpoint from Step 1 is the classic case: you get the update logic and the permission check is just missing, so one customer can edit another customer's data by changing a number in the URL. I have built auth systems with JWT and TOTP-based two-factor, and the part the AI consistently underweights is not the token logic, which it handles fine, but the boring per-endpoint "is this specific person allowed to do this specific thing" check. That is where the holes are.

The rest, quickly. **Input validation** is checking that incoming data is what you expect before you trust it; skip it, and you have left the door open for bad data and injection. **Exposed secrets** are passwords, API keys, and tokens that the model sometimes hardcodes straight into the source, where anyone with repo access can read them. And **SQL injection** is when user input gets pasted directly into a database query, letting an attacker rewrite that query to, say, dump or wipe your database; the fix is parameterized queries, where input is passed separately and can never be treated as a command.

One newer risk worth knowing by name: **hallucinated dependencies.** A dependency is an outside package your code pulls in. Models sometimes invent package names that do not exist, and if you run the suggested install without looking, an attacker who registered that made-up name first can ship malicious code into your project. People call this slopsquatting. Verify every AI-suggested package against the real registry before installing. This takes ten seconds and has no downside.

When you do the security pass, go item by item rather than glancing over the whole thing. Is identity checked? Are permissions enforced on the server, not just hidden in the UI? Is input validated? Are there secrets in here that belong in environment variables? Are the queries parameterized? Does every imported package actually exist?

And one thing that cuts the other direction, because it is easy to forget while you are busy reviewing the AI's output: watch what you put into the tool. Pasting real keys, credentials, or proprietary logic into a prompt is its own leak. Strip that stuff out before you ask.

The OWASP Top 10 is the reference worth bookmarking, and the broken-access-control entry specifically: [https://owasp.org/www-project-top-ten/](https://owasp.org/www-project-top-ten/) — [https://owasp.org/Top10/2025/A01\_2025-Broken\_Access\_Control/](https://owasp.org/Top10/2025/A01_2025-Broken_Access_Control/)

## Step 6: Check how it behaves with real data

Performance problems hide in development because your test database has twelve rows in it. The classic one is the N+1 query, and it is worth seeing rather than describing, because it slips past review constantly.

The pattern is this: the code runs one query to get a list, then fires off another query for every single item in that list. Here is the kind of thing an AI produces for a web view:

\# Generated code: looks fine, scales badly def post\_list(request): posts = Post.objects.all() for post in posts: print([post.author.name](https://post.author.name/)) # hits the database once PER post

One query for the posts, then one more for each post to get its author. Ten posts, eleven queries. Ten thousand posts, ten thousand and one queries, and the page that felt instant in testing now takes ten seconds. The fix is a single method:

\# Reviewed: one query, using a JOIN def post\_list(request): posts = [Post.objects.select](https://post.objects.select/)\_related('author').all() for post in posts: print([post.author.name](https://post.author.name/)) # no extra queries

select\_related grabs the author in the same query by joining the tables, for one-to-one and foreign-key relationships. For many-to-many relationships, prefetch\_related does the same job in a second query. The other things in this category are missing indexes (an index lets the database find rows without scanning the whole table, so filtering on an unindexed column is fine on a small table and painful on a real one), too many separate calls when one would do, and over-fetching whole rows when the code needs two fields.

The mindset is to read database code, asking what it costs when the table is large. Look for queries inside loops first, since that is the N+1 signature. Most frameworks have a tool that shows you every query a page runs, which makes these obvious the moment you look.

Django's own docs explain this well, and the idea carries to any framework: [https://docs.djangoproject.com/en/stable/ref/models/querysets/#select-related](https://docs.djangoproject.com/en/stable/ref/models/querysets/#select-related)

> Before we continue with step 7, my name is Mari, I am a backend developer and technical writer. I help tech and AI companies explain their products in the simplest way possible. DM or email me: nnannamari@gmail.com let's talk.

## Step 7: Cut the overengineering

People expect AI to cut corners. It does. What surprises them is that it also does the opposite, and that is its own problem.

Overengineering means solving something more complicated than the problem you actually have, by adding layers and abstractions and flexibility for situations that may never arrive. There is a name for the principle that pushes back on it: YAGNI, "You Aren't Gonna Need It," from Martin Fowler. Build for the requirement in front of you, not the one you are imagining.

AI overengineers because it pattern-matches on the big, complicated codebases in its training data, so it reaches for structures that look professional: extra wrappers, service layers, configuration for things that never get configured. It looks impressive. But if your task was simple, you now have to thread every small change through three layers of indirection for no reason. That is not free. It is more code to read, more places for bugs to hide, and a slower, riskier time for whoever touches it next, including you.

The test for each abstraction is whether a real, current requirement justifies it. An abstraction earns its keep when it absorbs change that is actually happening. If it is there "in case we need it later," cut it. You can add it when the need is real, and usually that is cheap.

Fowler's article on YAGNI is short and worth reading in full: [https://martinfowler.com/bliki/Yagni.html](https://martinfowler.com/bliki/Yagni.html)

## Step 8: Look for the error handling

Generated code spends almost all its lines on the happy path, the version where everything works, and very little on what happens when something fails, unless you push it to. So it breezes through the demo and then falls over the first time a downstream call errors, often silently, which is the worst kind.

What to look for:

- **No failure path at all** for an operation that can fail.
- **A catch-all** that swallows every error and hides the real problem. (An exception is the signal a program raises when something goes wrong; handling it means deciding what to do instead of crashing.)
- **External calls with no plan** for when they error, so one failure spreads quietly through the system.
- **No fallback** when something breaks: no retry, no safe default, it just stops.

For every operation that can fail, ask what happens when it does, and make the code answer. Catch specific errors rather than everything at once, log enough that you can debug it later, retry where retrying makes sense, fall back to something safe where you can.

A solid language-agnostic overview of the patterns: [https://www.geeksforgeeks.org/software-engineering/exception-handling-best-practices/](https://www.geeksforgeeks.org/software-engineering/exception-handling-best-practices/)

## Step 9: Ask whether you could maintain it

Code gets read far more than it gets written, and most of its life is spent being changed by someone who was not there when it was created. That someone is often you, six months later, with no memory of the prompt that produced it.

AI code makes this harder in two specific ways. It can be clever in ways that are tough to follow, and it tends to be inconsistent when it was generated across several prompts, so styles get mixed inside a single file. Let enough of that accumulate and you end up with a codebase nobody fully understands, where the speed you gained early gets paid back later as slow, nervous, error-prone maintenance.

Three questions settle it. Would I understand this in six months cold? Could someone who has never seen it maintain it without a walkthrough? Is it simple enough to debug fast when it breaks at a bad time? A "no" to any of these is a finding. Fix it now, while renaming, simplifying, and commenting are cheap, instead of later when they are not.

A beginner-friendly take on writing maintainable code: [https://www.freecodecamp.org/news/clean-coding-for-beginners/](https://www.freecodecamp.org/news/clean-coding-for-beginners/)

## How to actually think about all this

The thread running through every step is that your job is not to confirm that the code runs. It is to decide whether it is safe and correct to ship, which is a judgment the model cannot make for you because it cannot see your system, your users, or the page that goes off at 3am.

A habit that helps: spend more time reviewing the code than it took to generate. That ratio feels wrong the first few times and then feels obviously right. Treat every generated snippet as a draft from a contributor who is fast and confident and occasionally careless, because that is exactly what it is.

## The mistakes that come up most

- Reviewing the code before knowing the requirement. You cannot judge whether it did the job if you do not know the job.
- Trusting how confident it sounds. It sounds the same whether it is right or wrong.
- Signing off because it runs.
- Installing suggested packages without checking whether they exist.
- Pasting secrets into the prompt.
- Reading only the happy path.
- Waving through the complexity you do not need.

## A checklist for before you merge

- **Requirement:** Do I know what this was supposed to solve, and does it?
- **Decisions:** Is each framework, database, and pattern choice reasoned for this case, or just the default?
- **Logic:** Have I traced the flow and checked the edges and failure paths?
- **Assumptions:** What does this take for granted about inputs, services, records, and the network?
- **Security:** Authentication, authorization, input validation, exposed secrets, SQL injection, made-up packages?
- **Performance:** N+1 queries, missing indexes, too many calls, over-fetching?
- **Complexity:** Is every layer earning its place?
- **Error handling:** Where are the failure paths, fallbacks, and retries?
- **Maintainability:** Will this make sense to someone else in six months?
- **My own inputs:** Did I keep secrets out of the prompt?

## Wrapping up

AI writes the code. You decide what is safe and correct to ship. Those have always been separate jobs, and only one of them got automated.

The review starts before the code, with the requirement it is meant to satisfy, and runs through every decision it made, every assumption it leaned on, every failure path it skipped. When you stop treating the output as a finished answer and start treating it as a fast, confident draft from someone who does not know your context, you start catching the bugs that pass the tests. You ship less of what should not have been shipped.

The skill was never the generation. It is the judgment about what to keep. Stop generating code blindly and start previewing them.