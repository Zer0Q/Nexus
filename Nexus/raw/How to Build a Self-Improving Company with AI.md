---
title: "How to Build a Self-Improving Company with AI"
source: "https://www.youtube.com/watch?v=X_JsIHUfUjc"
author:
  - "[[Y Combinator]]"
published: 2026-05-21
created: 2026-06-21
description: "In this recent batch talk, YC General Partner Tom Blomfield breaks down how to build a self-improving company using AI. He'll cover how to create a series of recursive, self-improving AI loops and exp"
tags:
  - "clippings"
---
![](https://www.youtube.com/watch?v=X_JsIHUfUjc)

In this recent batch talk, YC General Partner Tom Blomfield breaks down how to build a self-improving company using AI. He'll cover how to create a series of recursive, self-improving AI loops and explain why the founders who get this right will run companies that can improve while they sleep.  
  
Chapters:  
  
00:00 — Companies Are Roman Legions  
00:54 — Copilots Are the Wrong Mental Model  
01:55 — Extract the Domain Knowledge  
02:24 — The Recursive Self-Improving Loop  
04:12 — The Holy Shit Moment at YC  
05:50 — Self-Optimizing Product and Support Loops  
06:29 — Burn Tokens, Not Headcount  
07:23 — Middle Management Is Over  
08:05 — Make Everything Legible to AI  
09:40 — Regenerating the YC User Manual  
11:19 — Software Is Ephemeral, Context Is Valuable  
12:18 — Where Humans Still Matter  
  
Apply to Y Combinator: https://www.ycombinator.com/apply  
Work at a startup: https://www.ycombinator.com/jobs

## Transcript

### Las empresas son legiones romanas

**0:00** · This is based a little bit off a talk Diana gave. There's a video up over the weekend, which is super cool. Um Jack Dorsey was tweeting some stuff like two or three weeks ago that I thought was super cool. And I've kind of um stolen a bunch of those ideas and shoved them in here. This talk is like pretty conceptual and high-level about thinking about how to build companies. So, the Roman legions were designed to project power over two continents or something from Rome at the center to like these people on Hadrian's Wall up in Scotland.

**0:31** · And the idea was um this nested hierarchies with consistent spans of control. And you had like named individuals with spans of control to pass orders down and send information back up the hierarchy. And if you think about most companies today, they are organized like a Roman legion, where human beings are the conduit for information flowing up and down.

**0:52** · And so, Jack Dorsey's tweet that I thought was great was this like this underlying assumption that hierarchically organized companies are the are the way that we should be organizing like our economic units of value. And I think AI basically breaks that. If you talked to people a year ago about how AI was useful, they talked about productivity. Like co-pilots making engineers 20% more productive, adding co-pilots to workflows, shipping more software.

### El modelo mental erróneo es el de los copilotos

**1:21** · But I think that is actually a broken way of thinking about AI. That's like P had a great blog post where basically just like taking the old way of working and adding like a more powerful engine onto it. And instead of that, I think you can reimagine like what a company is and how it acts. And so, as Gary's talking, like he I genuinely believe can produce more code than an entire engineering team.

**1:44** · The thing that's really stuck with me is this idea of like extracting the domain knowledge from your company and defining it as a as like context or a set of skills or whatever you want to call it.

**1:54** · But like this idea that there's domain knowledge or business knowledge or like some know-how that's inside the heads of people and in Slack messages and in emails and in Notion, all of this like information together defines how your company works.

### Extraer el conocimiento del dominio

**2:11** · And if you can make that legible, you suddenly can can move from this hierarchical organization to a sort of intelligent AI-powered organization with AI-native software. AI isn't the something It's not something you bolt onto the side of a company. It's not like a tool you give to engineers to make them more productive. But I think you can reimagine what a company is as a set of recursive self-improving AI loops.

### El ciclo recursivo de auto-mejora

**2:35** · I think this is really, really, really important because when it gets there, I think the company starts to self-improve even when you're sleeping.

**2:45** · So let me give you an example. Diane's talk talks about this as well. This AI loop, you start with like a sensor layer which is like That's a fancy word, but really it might be like emails from your customers. Might be support tickets, code changes, people canceling their subscription, uh product telemetry. It's like sensor data to get information from the outside world. And then a a policy layer, decision layer, like rules about what you can do, what it has to ask a human permission for, what it must log.

**3:13** · A tool layer that's kind of Gary's skills and code, like the tool layer is Gary's code. It's basically deterministic APIs, things like query my database or look at my calendar. Um a set of tools that the the AI can call. A quality gate, like that might be eval's deterministic checks, safety filters, human review for high-risk stuff. And then a learning mechanism. It's like your system interacts with the real world, picks up where it doesn't work and loops back into the top again.

**3:42** · And if you can run every single step of that without human intervention without with minimal human intervention, your system gets better and better and better while you're are And I can give you actual examples of this that are live right now. We started with an agent that you can ask and if it has deterministic tools to query our database. Pretty simple, like when did I last have office hours with this company? Then it got a little bit smarter, which was like, for this company I'm doing office hours with right now, they need introductions for anyone in petrochemicals or something.

### El momento de asombro en YC

**4:12** · And it could query the database in different ways and use rag and all sorts of stuff to like come up with five relevant founders for you to meet. But again, this is like this is a sidekick, right? This is an agent. This is like the old This is last year's version of how a how AI is making me better as a group partner. It's making me 20 or 30% more effective.

**4:29** · The aha moment for me came when we put a monitoring agent on top of that, which looked at every single query every single YC employee was doing and saw when it worked and when it did not work.

**4:42** · And when it did not work, it's like, oh, why not? What would have made this query work? Do we need different deterministic tools? Do we need to update the skills file? Do we need a different database for you? Do we need a new index? And this happened This literally happens overnight now. Let's write the code, put in a merge request to the YC code base, have an agent review it, and merge it, and deploy it. So, when a human comes the next day to ask the same query, it will now succeed. For me, that was like the holy \[ \_\_ \] \[ \_\_ \] But that's not just AI making you 20 or 30% more valuable, it is the AI going through this loop to figure out how to self-improve.

**5:15** · And I think basically, if you can identify parts of your company that work like this and eliminate as much of have the human in kind of a monitoring or supervisory capacity, you can just throw tokens at this problem and your company will get better.

**5:32** · And so, other examples might be, if you have product analytics, having an agent go through your product analytics to to figure out what part of your sales funnel is presenting the highest amount of friction, researching best practices, putting in place an AB test, running it for a week, picking the best version, and deploying it. Then doing that again and again and again for your product. So you have a self-optimizing like product loop. Or you do it with customer service queries. You have customer suggestions coming in and in and in.

### Ciclos de auto-optimización de productos y soporte

**5:56** · You triage it with a kind of You have to have an agent which is like your chief product officer and your chief technology officer who make kind of judgment calls about Okay, this is a suggestion which we just don't want to do. We'll discard it. But no, this is a suggestion which is now in line with our road map. Um we can do it overnight.

**6:12** · Let's write the code. Let's deploy it.

**6:14** · Let's ship it to the customer without a human being involved.

**6:17** · So I think if you can think about each part of your company as a self-improving like recursive AI loop, it becomes very very different to this like hierarchically organized Roman legion of a company. So what? So like if you want to do this, what are the implications?

### Quemar tokens, no personal

**6:29** · One is like burn tokens, not head count.

**6:32** · We are seeing companies get to demo day with about 5x more revenue per employee than they did 18 months ago. And I think that's going to continue to series A and series B.

**6:43** · And so I think you're going to be constrained on token usage, not on head count, really really soon. The blunt measure now is just like measuring everyone's token usage, which is obviously like dumb and gameable at the extreme, but directionally I think is correct. We're in the phase of like what is possible right now. And so everyone should be experimenting to the max to figure out what we can even do with this crazy new intelligence we have. As soon as you turn it into a leaderboard and people get promoted or fired based on it, obviously it gets gamed. Obviously that's dumb.

**7:13** · But I think directionally figuring out who in the organization is token maxing, who is not, is like a good way to think about which employees you should be spending your time with. I think middle management is done. I just don't think you need middle management for this coordination problem. I think AI should be doing it. And for me, there are two roles. Jack Dorsey has three. I actually don't like the third one, so I deleted it. But there are two roles that really, really matter for me. I think everyone just has to be an IC now, a builder, an operator. And I think crucially having directly responsible individuals to get anything done, I think you need a named human.

### La gerencia intermedia ha terminado

**7:45** · Not a committee, not a group of people, just a single person.

**7:48** · And I think you can build companies based on ICs effectively. I I think just middle management is is over. So, building the self-improving company, that's the dream. And by the way, I think like people are at the bleeding edge of this right now.

**8:01** · I'd be interested to see where you all are, but it feels like people are like exploring the boundaries here. I'm not sure anyone has a truly self-improving company in every function.

### Hacer que todo sea legible para la IA

**8:10** · I might be wrong. You might prove me wrong. What would I do? First of all, this is really, really important. I would make the entire organization legible to AI. What does that mean? It means you've got to record everything.

**8:21** · Um simplistically, all of our um partner emails, now if you email a YC partner, that email is in the YC database. Every Slack message, every DM, every office hour we've started recording for the last three or four months. Every single thing that happens, if it is recorded, it happened to the AI. If it did not get recorded, it is it did not happen to your intelligence. You know what I mean? And so, I was talking with some founders over here um just now, and we're having like really good conversations about their company.

**8:48** · But I every conversation I had, I was like, "Fuck, I need to be recording this conversation." Because some guy wanted an introduction to I can't even remember who the introduction was now. Uh who was that?

**9:01** · I was talking to someone about and I promised you an introduction. I said, "Yes." And I said, "Email me afterwards cuz I would I I'm going to forget this.

**9:07** · I'm going to talk to 20 people." Yeah, so it needs to be on my phone or a or or smart glasses. Or we deck out every room with like microphones. But basically, everything needs to be recorded so that it can be legible to the AI. And then as Garry talked about like diarization, you cannot pump in 100,000 hours worth of recordings into context window. So, you have to diarize it. You have to basically aggregate it down, synthesize it into the important parts, and then give the AI breadcrumbs.

**9:31** · So, like okay, so here's an example.

**9:33** · Who's read the user manual, the YC user manual? Hopefully, everyone in this room has at least opened the user manual at one point in time, right? Like it's fine. It was written 5 to 10 years ago, most of it. It's kind of out of date.

### Regenerando el manual de usuario de YC

**9:45** · So, Harj thought uh last weekend, since now we've got about 2,000 hours of recorded office hours from the last 3 months, why don't we regenerate the user manual?

**9:53** · And so, you can click like you give it a set of instructions, you basically diarize it down, synthesis like categorize it into certain areas like fundraising, hiring, co-founder disputes, whatever, and then write me a new user manual.

**10:06** · And by the end of the weekend, he had a 150 page user manual, which is dramatically better than the existing user manual. And now we can also update it every single month. So, our user manual becomes self-improving. Every new piece of advice we give, it's compared with the existing user manual and either incorporated or thrown away. So, the user manual becomes this up-to-date living brain of the advice we give to founders.

**10:28** · And obviously, it doesn't stop as a user manual, you then pump it in as context to an AI agent, and suddenly you can ask a superintelligent AI and get the combined wisdom of 16 YC partners in one.

**10:39** · But only if it's legible. So, you have to record everything. The second point is kind of the same, right? Like if it creates an artifact that can self-improve, it's legible. If it doesn't, you throw it away. The third point then is that every function can generate This used to say dashboards.

**10:54** · It's not just dashboards, it's on-demand software. Codex 55 is now good enough you can one-shot most simple like most internal software dashboards you can one-shot to a pretty high level of quality. I tried it over the weekend on a bunch of our stuff. It's just unreal.

**11:09** · So, all of your internal operations teams should be sitting on this layer of like kind of intelligence understanding, and then creating their own dashboards and their own workflows. And I would see that those as entirely disposable. I would very preciously store all the data. So, as Garry said, he puts it all all of his emails in markdown. Never throw anything away, but then treat these the software as ephemeral. You can you can generate it.

### El software es efímero, el contexto es valioso

**11:35** · You can regenerate it. The valuable part is like the comprehension inside people's heads of like this is how the function works. This is how we run a YC event, whatever. The software to actually run the event you can generate for the event. You can throw it away.

**11:47** · The the models get smarter in a month or two. Throw the software away. Give it your original set of instructions and regenerate the software.

**11:54** · So I think the business context and and skills are the valuable part. I think the software on top of it is ephemeral.

**12:01** · So what what are humans for in this world? I think basically we're talking about a company brain. And I know a bunch of people in this room are building this. But the bit in the middle, like all of your data, all of your emails, your DMs, the skills, the know-how, that is like the company brain. And I think the humans sit around the edge of this interfacing with the real world.

### Donde los humanos aún importan

**12:22** · So it's where this intelligence makes contact with reality.

**12:26** · Human beings reach into places the models can't go yet. That might be like a conference. It might be a I'm trying to think of examples. I I would say a phone call, but I think the AI can reach into phone calls pretty easily now.

**12:37** · Um I think it's like novel situations, ethical considerations, high-stakes moments. You know, it's like it's where the founder comes to us and is like thinking about breaking up with their co-founder. Right? It's like those real high-stakes, high-emotion moments where you really want a human being. I think that's where the human fits. For all of you, like sales conversations. I think that's a human being in the room for the next 20 years.

**13:01** · So the humans live I think around the edge.

**13:03** · And I'm over time and Kulveer should bullhorn me. I will leave you this one question. If you were building your company today, would you start it in this shape?

**13:14** · For most of you, you're small enough to build it right. And so I don't think you have any excuse. And I know there are a few of you who are in the process of ripping up and rebuilding your company.

**13:23** · So with that I will stop and will hand over to Pete. Thank you for listening.