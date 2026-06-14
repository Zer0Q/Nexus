---
title: "How to Run 300 AI Agents From One Prompt. 10 Workflows Most People Skip"
source: "https://x.com/eng_khairallah1/status/2062461939318730818"
author:
  - "[[@eng_khairallah1]]"
published: 2026-06-04
created: 2026-06-14
description: "Here is what happens every single day.Save this :)Most people still use AI the way they used Google in 2010: type a query, read the answer, ..."
tags:
  - "clippings"
---
![Imatge](https://pbs.twimg.com/media/HJ6hqcZWAAAd477?format=jpg&name=large)

Here is what happens every single day.

Save this :)

Most people still use AI the way they used Google in 2010: type a query, read the answer, type the next one.A single thread you feed one item at a time.

But a model that can plan and call tools doesn't have to be used one item at a time. Hand it 100 PDFs and the obvious move isn't to walk through them in sequence: it's to open 100 of them at once, one reader per file, and have a coordinator stitch the readings back together. The prompt stays the same length. The work fans out behind it. You go from a single thread to a fan: one instruction in, a hundred workers spawned, one assembled deliverable out.

That is the whole shift, and it is the difference between reading 100 papers over a weekend and reading them over a coffee. The rest of this is the cost math, the setup, the prompts, the repos, the workflows, and the places where this quietly falls apart.

## The Real Cost Picture

This is where most people give up before they start. They assume running 300 agents must cost a fortune. It does not.

Take a real task: 100 PDF research papers analyzed into a single literature review with citations.

**Sequential approach with Claude Opus 4.8:** Roughly 6 hours of agent wall time at $5 per million input tokens and $25 per million output. Estimated cost: $40 to $60 per run depending on document length. Plus your time supervising.

**Parallel approach with the Kimi K2.6 agent swarm:** 100 agents spin up simultaneously, each handling one paper. Coordinator merges. Wall time: 12 to 18 minutes. Cost: $3 to $5 per run.

That is a 15x speed multiplier and a 10x cost multiplier on the same task. The math is not even close.

Now scale that. 50 support tickets analyzed for patterns. 100 cold outreach emails personalized to specific prospects. 40 academic PDFs turned into a 100,000-word literature review with citations. 30 brick-and-mortar businesses scraped and turned into individual landing pages. Every one of these used to require either a team of contractors or an entire day of sequential work.

Now it is one prompt, one coffee break, under $10.

**A solo operator with this stack is not competing with other solo operators. They are competing with agencies.**

## What Actually Changed in April

Three things landed in the same month that made this real for the first time.

**Kimi K2.6 dropped April 20.** Built by Moonshot AI, open-source under a Modified MIT License. The model was natively trained to coordinate up to 300 sub-agents across 4,000 coordinated steps from a single prompt. That is triple the limit of K2.5. The orchestration is not bolted onto a chat interface, it is baked into the model layer. 1 trillion total parameters, 32 billion active per token, 256k context window, 65,536 max output tokens per response. Pricing: $0.80 per million input tokens, $3.60 per million output. Roughly 8x cheaper than Claude Opus 4.8.

The numbers that matter most: 80.2% on SWE-bench Verified, 92.5% on DeepSearchQA, 66.7% on Terminal-Bench 2.0, 58.6% on SWE-bench Pro (tied with GPT-5.5). Hallucination rate dropped from 65% in K2.5 to 39%, which is essentially on par with Opus 4.8 at 36%.

In real-world testing, K2.6 autonomously overhauled an 8-year-old financial matching engine over 13 hours, iterated through 12 optimization strategies, made over 1,000 tool calls, modified more than 4,000 lines of code, and delivered a 185% throughput improvement. One of Moonshot's own teams ran it as an autonomous agent for five days straight, managing monitoring, incident response, and system operations without human intervention.

**Claude Opus 4.8 dropped April 16.** Sub-agent reliability improved significantly. New xhigh effort tier makes complex agent chains more deterministic. SWE-bench Pro lead at 64.3%. Vision jumped from 54.5% to 98.5% after a resolution upgrade. Still the gold standard for production code quality and legal-grade precision. Still $5/$25 per million tokens.

**GPT-5.5 dropped April 23.** Computer use jumped to 78.7% on OSWorld-Verified, meaning agents can now actually operate real GUIs without breaking. Long-context retrieval at 74% versus Claude's 32.2% on the same benchmark. Web research at 90.1% on BrowseComp. Pricing $5/$30 per million but uses fewer output tokens per task in practice.

The pattern: three frontier models in one week, each with a clear specialty. The losers are the developers who picked one and stuck with it. The winners are the ones who route each task to the right brain.

For parallel agent swarms specifically, K2.6 is the only model trained from the ground up to coordinate at this scale at a price that lets you actually use it.

## What 300 Parallel Agents Actually Looks Like

This is the part that matters. Not the spec sheet, the actual deliverables. Every one of these is from real prompts that real people ran in April 2026.

**The literature review run.** 40 academic PDFs uploaded. Output: a 100,000-word literature review with a fully cited dataset. 40 agents, each owning one paper, coordinated through a single merge step. Total runtime under 20 minutes.

**The astrophysics paper transformation.** One astrophysics paper went in. The output was a 40-page research report, a 20,000-row supporting dataset, and 14 publication-grade charts. The entire output was then packaged as a reusable Skill the agent system can apply to every future astrophysics paper automatically. The first run took 30 minutes. Every subsequent run on a new paper now takes 12 minutes because the Skill captures the structure.

**The Google Maps to landing pages workflow.** One prompt: search Google Maps for retail stores in Los Angeles that do not currently have a website, identify 30 unique businesses, scrape storefront photos and customer reviews, build a high-conversion landing page for each one with addresses, hours, value proposition tailored to the business type, and contact details. Output: 30 individual landing pages plus an Excel spreadsheet listing all 30 stores with full metadata. Runtime: under 45 minutes.

**The job hunt automation.** 100 job descriptions matched against one CV. Output: 100 individually tailored resumes, each optimized for the specific role's requirements and language. The kind of work a freelance career coach charges $50 per resume for. Total cost of the run: under $4.

**The magazine cover series.** One prompt asking for 10 tabloid-style magazine covers with real historical headlines. Each agent researched a different historical period, generated the headlines, designed the cover. Output: 10 polished magazine covers from one input prompt.

**The five-day autonomous run.** Moonshot's internal team pointed K2.6 at their monitoring and incident response pipeline. It ran for five days straight, handling alerts, opening pull requests, posting to Slack, escalating real incidents. No human intervention. This is not a demo. This is what an autonomous on-call engineer looks like in 2026.

**If you have ever paid for batch processing work, your entire pipeline just got automated.**

## How to Actually Set This Up

You do not need to build a framework. You do not need a PhD in distributed systems. The infrastructure is already done.

**Option 1: Zero-setup web interface**

Go to kimi{.}com/agent-swarm. Describe your task. Specify the number of sub-agents. Upload any files. Run. This is the entry point. No installation, no API keys, no config. The web UI handles agent decomposition, coordination, and final output assembly.

Use this for: one-off batch tasks, document processing workflows, research projects, any time you want to test if your task is even parallelizable before investing in code.

**Option 2: API integration for production workflows**

For programmatic access and integration into your own pipelines, use the Moonshot API directly with the K2.6 endpoint. Documentation lives at [github.com/moonshotai/Kimi-K2](http://github.com/moonshotai/Kimi-K2).

```bash
pip install moonshotai
```

Spin up a parallel job by setting the agent\_swarm parameter to true and the max\_agents value up to 300. The model handles the decomposition natively. You provide the task description and any reference files, K2.6 handles the rest.

For self-hosting, the official repo has full deployment guides for vLLM and SGLang. Weights are on Hugging Face. You can run this entirely on your own infrastructure if you need to.

**Option 3: LangGraph orchestration with K2.6 backend**

For full control over the orchestration logic while keeping K2.6's pricing, use LangGraph as the orchestration layer and route model calls to K2.6 through OpenRouter.

```bash
pip install langgraph langchain-openai
```

Point the model parameter at the Kimi K2.6 endpoint, route through OpenRouter for unified billing across all your model providers. This is what production teams are running.

When to use this: you have a complex stateful workflow with custom branching logic, conditional routing between sub-agents, or human-in-the-loop checkpoints. LangGraph gives you the graph structure, K2.6 gives you the pricing and parallel execution capacity.

**Option 4: Claude Code Router for mixed-model swarms**

[github.com/musistudio/claude-code-router](http://github.com/musistudio/claude-code-router) lets you run Claude Code's interface but route specific sub-agents to whichever model fits the task best. Coordinator on Opus 4.8 for high-reliability planning, bulk sub-agents on K2.6 for cost-efficient parallel execution, computer-use sub-agents on GPT-5.5 for GUI navigation.

This is the most cost-efficient parallel stack you can build today. The coordinator handles maybe 5% of the total tokens and needs maximum reliability. The 300 sub-agents handle 95% of the tokens and need maximum cost efficiency. Routing each layer to the right model cuts total cost by another 60% compared to running everything on a single model.

## The Prompts to Install Right Now

Three system prompts. One for the coordinator, one for the sub-agents, one for the validator. Install these as persistent system prompts in your swarm config or paste them at the start of any session.

**For the coordinator agent:**

```markdown
You are a coordinator orchestrating a swarm of parallel sub-agents.

Your job: decompose the user's request into the smallest number of 
independent parallel tasks that fully cover the goal, dispatch them 
to sub-agents, and merge the results into one coherent deliverable.

Rules:
- Identify the smallest unit of parallelizable work
- Each sub-task must be fully independent, no cross-dependencies
- Specify the exact output format every sub-agent must return
- Define the merge logic before dispatching anything
- If sub-tasks have dependencies, sequence them in phases instead of 
  forcing false parallelism
- Spawn no more sub-agents than the task requires

When merging:
- Resolve contradictions explicitly, do not paper over them
- Preserve attribution of which sub-agent produced which output
- Verify the merged output against the original request before 
  returning

Success: the final deliverable is coherent, complete, and traceable 
back to specific sub-agent outputs.
```

**For each sub-agent in the swarm:**

```markdown
You are a specialist sub-agent inside a larger swarm.

Your job: complete exactly one assigned sub-task and return your 
output in the exact format the coordinator specified.

Rules:
- Read the full sub-task spec before doing anything
- Do not expand scope beyond what was assigned
- Return your output in the exact requested format, no preamble, 
  no commentary
- If you hit a blocker, return a clear flag instead of guessing
- If your sub-task requires information outside your assigned scope, 
  flag it for the coordinator instead of trying to fill it yourself
- Verify your output against the spec before returning

Success: your output plugs directly into the merge step without 
requiring the coordinator to clean it up.
```

**For the validator pass at the end:**

```markdown
You are the validator for a completed swarm output.

Your job: check whether the merged deliverable actually satisfies 
the original user request.

Rules:
- Compare the final output against the original request, not against 
  the coordinator's plan
- Flag any gap between what was asked and what was delivered
- Identify contradictions in the merged output
- Identify any sub-agent outputs that were dropped or misinterpreted 
  in the merge
- Do not soften findings, surface every real issue

If the output is incomplete: list exactly what is missing.
If the output is wrong: identify which sub-agent's output caused it.
If the output is complete and correct: confirm and pass through.

Success: nothing broken or incomplete makes it past your check.
```

These three prompts are the difference between a swarm that produces coherent deliverables and one that produces 300 fragments you have to manually stitch together.

## The Repos You Need

This is the most important section. Bookmark every single one.

**For the swarm itself:**

[github.com/moonshotai/Kimi-K2](http://github.com/moonshotai/Kimi-K2) is the official repo. Weights, deployment guides for vLLM and SGLang, API documentation, full setup for self-hosting or API integration. Start here.

[github.com/chongdashu/cc-kimi-k2-thinking-prompts](http://github.com/chongdashu/cc-kimi-k2-thinking-prompts) shows how to use K2.6 through the Claude Code CLI by swapping a single environment variable. Claude Code's full agent loop with K2.6's brain doing the work at a fraction of the cost.

[github.com/dnnyngyen/kimi-agent-internals](http://github.com/dnnyngyen/kimi-agent-internals) has the extracted system prompts for all six of Kimi's built-in agent types including Base Chat, OK Computer, Docs, Sheets, Slides, and Websites, plus the full Skill definitions and tool schemas. This is the closest thing to a reverse-engineered playbook for how Moonshot's own agents are built.

**For orchestration:**

[github.com/langchain-ai/langgraph](http://github.com/langchain-ai/langgraph) is the open-source orchestration framework most production parallel-agent teams are running. Mature, stateful, full control over the graph.

[github.com/joaomdmoura/crewAI](http://github.com/joaomdmoura/crewAI) is the easier entry point if you want role-based agent definition without writing graph logic yourself. Less powerful, much friendlier on-ramp.

[github.com/microsoft/autogen](http://github.com/microsoft/autogen) is Microsoft's framework for conversation-based multi-agent collaboration. Best for workflows where agents debate or refine each other's outputs rather than running in pure parallel.

[github.com/musistudio/claude-code-router](http://github.com/musistudio/claude-code-router) is the missing piece for mixed-model swarms. One interface, multiple model backends, routing logic per sub-agent type.

**For the prompts and patterns:**

[github.com/asgeirtj/system\_prompts\_leaks](http://github.com/asgeirtj/system_prompts_leaks) has the leaked system prompts for K2.6, Opus 4.8, and GPT-5.5 in one place. Studying how each company shapes its model's behavior is one of the highest-leverage prompt engineering exercises you can do.

[github.com/f/awesome-chatgpt-prompts](http://github.com/f/awesome-chatgpt-prompts) at 143k+ stars is the canonical prompt library. Works across all three models, gives you templates for almost any agent pattern.

[github.com/CheswickDEV/claude-opus-4.8-prompt-optimizer](http://github.com/CheswickDEV/claude-opus-4.8-prompt-optimizer) is a meta-prompt that transforms raw prompts into production-grade XML-structured prompts optimized for the new xhigh effort tier. Useful when your coordinator runs on Opus.

## Skills: The Quiet Force Multiplier

Most people will skip this section. They should not.

K2.6's swarm has a feature called Skills. You upload any document, any PDF, any spreadsheet, any deck, and the swarm extracts its structural and stylistic DNA into a reusable template.

The astrophysics paper example earlier became a Skill. So now every future astrophysics paper run takes 12 minutes instead of 30 because the swarm already knows the output structure, the chart styles, the citation format, the section hierarchy.

Real Skills people are running right now:

A WEF-style report Skill that takes any research input and produces a fully formatted institutional research publication with proper typography, color palette, two-column layouts, figure numbering, and methodology appendix.

An ink-wash presentation Skill that converts any content into elegant black-and-white shuimo-style slide decks with hand-painted illustrations, monochrome watercolor aesthetics, and asymmetrical layouts.

A pitch deck Skill that converts your raw business idea into a polished investor-ready deck.

The pattern is the same every time: upload one example of your best output, the swarm captures the DNA, every future task in that domain inherits that quality automatically.

**This is where the leverage compounds. You stop reinventing the structure of your work every time. Each Skill makes every future run cheaper, faster, and more consistent.**

If you do nothing else from this entire article, build three Skills this week from your three best pieces of past work. Your output quality and speed will permanently shift.

## Real Workflows You Can Build This Weekend

These are not hypothetical. Every single one of these is running in production right now.

**1\. The competitive intelligence pipeline.** 50 agents pointed at 50 competitor websites. Each one extracts pricing, features, positioning, recent updates, customer reviews. Coordinator merges into a single competitive landscape report. Run it weekly. You will know the market better than anyone in your industry. Runtime: 20 minutes. Cost: under $5.

**2\. The content production assembly line.** 20 agents researching different angles of one topic. One coordinator merges findings into an outline. One writer agent drafts. One editor agent refines. Four hours of human work becomes 15 minutes of agent runtime. Build a Skill from your best article, every future article inherits the structure.

**3\. The cold outreach personalization stack.** Upload 100 prospect names and companies. 100 agents each research one prospect, find their recent work, identify a relevant pain point, draft a custom outreach message in your voice. Not generic AI slop. Real personalization executed in parallel. Cost per message: under 5 cents.

**4\. The legacy codebase audit.** Spin up agents that each analyze a different module of a large codebase. One agent produces architecture documentation. Another finds dead code. Another flags security issues. Another suggests refactor candidates. Coordinator produces a single audit report. The kind of audit a consultancy bills $50,000 for. Now runs overnight for under $50.

**5\. The bulk freelance service automation.** Have a service business? Cover letter writing, resume tailoring, proposal drafting, market research, ad copy variations. Build a swarm that processes each job from intake to delivery. One operator can handle the volume of an entire agency.

**6\. The documentation generation pipeline.** Point agents at every file in your codebase. Each one generates documentation for its assigned module. Coordinator merges into a single docs site. Maintained automatically on every commit.

**7\. The autonomous monitoring agent.** Point a long-running K2.6 agent at your error logs and deployment pipeline. When something breaks it identifies the relevant commits, opens a draft fix, posts to Slack with context. Your on-call engineer reviews a pull request instead of staring at a blank terminal at 3am.

**8\. The product launch coordination swarm.** One agent writes the PRD. One designs mockups. One writes the launch blog post. One drafts the social media campaign. One builds the landing page. One drafts the press outreach. All in parallel, all merged into one coordinated launch package.

**9\. The market research at depth.** Spin up 30 to 50 agents on a single research question, each covering a different angle. Coordinator merges and resolves contradictions. Structured report with full citations in the time it used to take to read 10 articles.

**10\. The SaaS prototype assembly.** Describe the product, stack, and feature list. K2.6 scaffolds the frontend, backend, DevOps config, database schema, and authentication layer in parallel. Hand the output to Opus 4.8 to harden the production-critical paths. A weekend MVP that used to take a month.

## The Model Routing for Maximum Leverage

The smartest move is not running everything through K2.6's swarm. The smartest move is routing each layer of the swarm to the model that fits.

**Coordinator on Opus 4.8.** The coordinator handles maybe 5% of total tokens and 95% of the strategic decisions. Reliability matters more than cost. Use the best.

**Bulk sub-agents on K2.6.** The 300 sub-agents handle 95% of total tokens. Cost efficiency matters most. K2.6 is the only model that makes 300 parallel agents economically viable.

**Web research sub-agents on GPT-5.5.** When a sub-agent needs to browse and synthesize web information, GPT-5.5's 90.1% BrowseComp score and superior long-context retrieval pulls ahead of everything else. Route browsing sub-agents to GPT-5.5 specifically.

**Vision sub-agents on Opus 4.8.** Any sub-agent that needs to interpret images, design layouts, or work with visual references should route to Opus 4.8's 98.5% visual acuity score.

**Computer use sub-agents on GPT-5.5.** GUI operation, browser automation, anything requiring actual interface control. GPT-5.5's 78.7% OSWorld-Verified score is the highest in the market.

Set this up once. Use Claude Code Router to handle the routing logic. Your total swarm cost drops another 40 to 60% versus single-model execution.

**This is what mastery looks like in 2026. Not loyalty to one tool, ruthless routing to the best tool for each layer of the work.**

## The Honest Caveat

I am going to give you the unvarnished version because hype helps nobody.

Parallel agent orchestration is still fragile on the most complex long-horizon tasks. If your workflow requires deep sequential reasoning where each step depends on the last in non-obvious ways, parallelization does not help and can actively hurt. The merge step starts producing contradictions when sub-tasks are not actually independent.

Use swarms where work genuinely parallelizes: research, batch generation, multi-document analysis, content production at scale, anything with embarrassingly parallel structure where 50 inputs become 50 outputs through the same transformation.

For sequential reasoning, single-file debugging, novel architecture decisions, or any task where reliability over hundreds of dependent steps matters more than throughput, you still want a single high-quality model like Opus 4.8 working linearly.

Other real caveats:

Orchestration overhead is non-zero. Spinning up 300 agents takes a few minutes of coordination time. For tasks under 10 minutes of equivalent sequential work, the overhead eats the benefit. Do not throw swarms at small jobs.

Tool-schema retry rates are slightly higher on K2.6 than on Anthropic or OpenAI. If your sub-agents rely heavily on calling structured tool APIs, you will see occasional retries that you would not see with Opus.

K2.6 does not lead on pure math. If your sub-agents need to do heavy numerical reasoning, route them to GPT-5.5 specifically.

No image input on the K2.6 API yet. Image-heavy sub-tasks need to route to Opus or GPT-5.5.

**Parallel agents are not magic. They are leverage for the right kind of task. The wins are massive when the task fits. The losses are real when it does not.**

## The Mental Model Shift

For the last two years, the question for every AI workflow was: which model is best for this task?

That was the right question when models were sequential and the differences between them were significant.

The question in 2026 is different. Can this task be parallelized? If it can, what is the cheapest model that handles each sub-task at acceptable quality?

That is a completely different way of thinking about AI work.

The 10x operator is not the one with the best single model. The 10x operator is the one who decomposed the work into 50 parallel sub-tasks while everyone else was still running one prompt at a time, then routed each sub-task to the right model for the job.

Most people will read this article, find it interesting, and keep working sequentially. The infrastructure is too new and the mental shift is too uncomfortable. That is fine. That is also the opportunity.

The ones who actually rewire their workflow this week will be operating on a completely different level within 30 days. Not because they will be smarter. Because they will be running 50 to 100 times more attempts per day than anyone they are competing with.

**More attempts means more learning. More learning means more output. More output means more leverage.**

That compounds.

The infrastructure is here. The pricing is here. The tooling is here. The repos are public, the docs are written, the prompts are above.

The only question is whether you build the parallel agent stack now or wait until everyone else does first.

The people who pull ahead in AI in 2026 are not the ones with the most expensive subscriptions. They are the ones who understood the shift to parallel agent swarms before it became obvious.

**I break down every major AI workflow and tool stack so you do not have to figure it out alone.**

**Follow me** [@eng\_khairallah1](https://x.com/@eng_khairallah1) **for more AI courses, tools, and workflows. New content every week.**

**hope this was useful for you, Khairallah** **❤️**