---
title: "Top AI Papers of the Week"
source: "https://x.com/dair_ai/status/2061104052818108476"
author:
  - "[[@dair_ai]]"
published: 2026-05-31
created: 2026-06-02
description: "1. SkillOptMicrosoft Research treats a compact natural-language skill document as the trainable state of a frozen agent, then learns that do..."
tags:
  - "clippings"
summary:
---
![Imatge](https://pbs.twimg.com/media/HJle9AyWEAEANv3?format=jpg&name=large)

## 1\. SkillOpt

![Imatge](https://pbs.twimg.com/media/HJle5s9XAAMPx6w?format=png&name=large)

Microsoft Research treats a compact natural-language skill document as the trainable state of a frozen agent, then learns that document through rollouts, reflection, and bounded edits gated by held-out validation. The argument is direct: most engineers handwrite agent skill docs and hope they generalize, when the doc itself should be optimized like a parameter. SkillOpt reframes the SKILL.md file as an external parameter of a model whose weights never change.

- **The skill doc as a trainable parameter:** An optimizer model proposes validation-gated edits to the skill file, adding, deleting, or replacing instructions. A textual learning rate controls how aggressively each round rewrites the document, with batch and momentum reported in text space rather than gradient space.
- **Validation gates instead of hope:** Every edit must pass a held-out check before it is kept. This turns skill authoring into a measurable optimization loop with a real objective, rather than prompt tweaking guided by intuition.
- **52 out of 52 wins:** SkillOpt beats Trace2Skill, TextGrad, GEPA, EvoSkill, human-written skills, and one-shot skills across 6 benchmarks and 7 target models. It adds roughly +23.5 points on GPT-5.5 in direct chat, +24.8 in the Codex loop, and +19.1 in Claude Code from the no-skill baseline.
- **Why it matters:** If the skill document is the thing you optimize, the bottleneck shifts from base-model capability to how well you can train the natural-language state around a frozen agent. That is a cheap, model-agnostic lever most teams are leaving on the table.

[Paper](https://arxiv.org/abs/2605.23904) | [Tweet](https://x.com/omarsar0/status/2058936160291004483)

## 2\. Compiling Agentic Workflows into Weights

![Imatge](https://pbs.twimg.com/media/HJlfBozXAAU1G8y?format=jpg&name=large)

This paper shows that a full agentic workflow can be distilled into the weights of a small model and run at roughly two orders of magnitude lower inference cost while preserving near-frontier task quality. Instead of keeping an external orchestrator above the LLM, the procedure is compiled into the weights of a fine-tuned model, producing what the authors call a subterranean agent.

- **The whole workflow, not just the answer:** The compiled procedure includes multi-step LLM calls, tool invocations, intermediate scratchpads, and decision points. The student internalizes the orchestration logic rather than only imitating final outputs.
- **Orchestrator dissolved into the model:** Classic agent frameworks run a planner loop above the model on every request. Compiling that loop into weights removes the per-call orchestration overhead, which is where most of the cost and latency live.
- **Near-frontier quality at 100x less cost:** Across the evaluated tasks, the distilled small model stays close to the original workflow's quality while cutting inference cost by about two orders of magnitude. The savings come from collapsing many model calls into one forward pass.
- **Why it matters:** Most production agents pay repeatedly for an orchestration loop they run thousands of times a day. If that loop can be compiled once into a cheap model, the economics of deploying agentic systems change substantially, especially for high-volume narrow workflows.

[Paper](https://arxiv.org/abs/2605.22502) | [Tweet](https://x.com/dair_ai/status/2057846601843146760)

## 3\. AutoScientists

![Imatge](https://pbs.twimg.com/media/HJlfHY6WkAAkwYp?format=jpg&name=large)

AutoScientists, from Harvard, is a decentralized team of AI agents for long-running computational science that drops the central planner entirely. Rather than following one research trajectory coordinated from the top, agents self-organize around promising hypotheses, critique each other's proposals before spending experimental compute, and record both successes and failures so the system avoids redundant exploration as evidence accumulates over hours or days.

- **No central planner:** Agents interpret shared experimental state, form teams around promising directions, and reorganize when progress stalls. Coordination emerges from a common state rather than a top-level controller, which sustains parallel search instead of a single thread.
- **Evaluate before you spend:** Proposals are critiqued and scored before any experimental compute is allocated. This gating reduces wasted trials and keeps the system from repeating dead ends that an individual agent would otherwise revisit.
- **Strong results on real science tasks:** On BioML-Bench, 24 biomedical ML tasks spanning imaging, protein engineering, single-cell omics, and drug discovery, AutoScientists reaches 74.4% mean leaderboard percentile, an improvement of +8.33% over the strongest prior AI agent.
- **Why it matters:** Most multi-agent research systems still funnel decisions through a planner that becomes a bottleneck. Decentralized self-organization with explicit failure-sharing is a different blueprint for long-horizon scientific search, and it holds up on hard biomedical benchmarks.

[Paper](https://arxiv.org/abs/2605.28655) | [Tweet](https://x.com/dair_ai/status/2060028833080987668)

## 4\. Language Models Need Sleep

![Imatge](https://pbs.twimg.com/media/HJlfOijXEAUcABW?format=png&name=large)

Attention scales badly with context length, so long-horizon agents keep paying a growing cost as their context grows. This paper studies a sleep-like consolidation mechanism: the model periodically converts recent context into persistent fast weights, then clears its key-value cache. During the sleep phase it performs offline recurrent passes over the accumulated context and updates fast weights in its state-space blocks through a learned local rule.

- **Consolidate, then clear the cache:** Recent context is folded into fast weights stored in the model's SSM blocks before the KV cache is discarded. The agent keeps what it learned without carrying the full attention bill into every future step.
- **Compute moves to sleep, latency stays at wake:** The extra work happens offline during consolidation, so wake-time prediction keeps its low latency. The tradeoff is explicit and controllable rather than hidden in a ballooning context window.
- **More sleep helps the hardest cases:** Increasing sleep duration improves performance, with the largest gains precisely on tasks that require the most complex reasoning over long histories. The mechanism buys the most where naive attention struggles most.
- **Why it matters:** Long-horizon agents are the first systems to feel the quadratic cost of context. A biologically inspired consolidation step gives a principled alternative to ever-longer context windows, and it maps cleanly onto the state-space architectures already used for efficiency.

[Paper](https://arxiv.org/abs/2605.26099) | [Tweet](https://x.com/dair_ai/status/2059333792775745619)

## 5\. Adapting the Interface, Not the Model

![Imatge](https://pbs.twimg.com/media/HJlfWZjXgAApLXG?format=jpg&name=large)

When a frozen LLM agent repeatedly fails in a deterministic, rule-governed environment, do you have to retrain the model? Life-Harness argues no. Many failures come from mismatches at the model-environment interface, not from the model's reasoning, so the fix belongs in the runtime harness. Life-Harness is a lifecycle-aware harness that improves frozen agents without touching model weights or the evaluation environment.

- **Failures become reusable interventions:** Recurring errors are turned into runtime fixes across four areas: action realization, environment contracts, trajectory regulation, and procedural skills. Each fix is a harness-level patch the agent reuses on later attempts.
- **Model frozen, environment intact:** Nothing about the model or the benchmark changes. Only the interface between them adapts, which keeps the approach drop-in for any backbone and avoids the cost and risk of fine-tuning.
- **Broad, consistent gains:** Across 7 deterministic agent benchmarks and 18 model backbones, Life-Harness improves 116 of 126 model-environment settings, with an 88.5% average relative improvement. The effect holds across model scales rather than helping only weak models.
- **Why it matters:** This is more evidence for the code-as-harness thesis: a large share of agent failures are interface problems that harness engineering can fix without retraining. For builders, the leverage is in the runtime, not the model.

[Paper](https://arxiv.org/abs/2605.22166) | [Tweet](https://x.com/omarsar0/status/2058208914148389083)

## 6\. The Efficiency Frontier

![Imatge](https://pbs.twimg.com/media/HJlfbTSXQAI_uQL?format=jpg&name=large)

Context costs dominate production LLM bills, and the right strategy depends on how often preprocessing gets reused. This paper models context-strategy selection as a deployment-aware optimization problem that jointly accounts for task performance, token cost, and reuse, then uses it to compare retrieval-based and preprocessing-based approaches under realistic constraints.

- **A reuse-aware cost model:** A parameterized log-utility metric captures diminishing returns from more context while charging an amortized preprocessing cost. Varying a reuse parameter lets the framework compare strategies under different deployment patterns on equal footing.
- **Distinct operating regimes:** The analysis reveals clean transition boundaries between retrieval and preprocessing strategies. Which one wins flips depending on how many times you reuse the preprocessed context, so a single default is rarely optimal.
- **Real token savings:** On 5,000 HotpotQA instances, deployment-aware optimization cuts effective token usage by roughly 25% at comparable performance, and amortized memory compression achieves over 50% lower token cost relative to full-context.
- **Why it matters:** Most teams pick a context strategy once and pay for it on every request. Treating context management as an explicit cost-performance optimization turns a guess into a measurable decision, with double-digit savings available on common workloads.

[Paper](https://arxiv.org/abs/2605.23071) | [Tweet](https://x.com/dair_ai/status/2058948732658626789)

## 7\. Forecasting Scientific Progress with AI

![Imatge](https://pbs.twimg.com/media/HJlfe2LW0AICtRD?format=jpg&name=large)

Can frontier models predict where science is going? This work introduces CUSP, a cutoff-conditioned benchmark built from 4,760 real scientific events across multiple disciplines, each grounded against a verified knowledge cutoff. For every event, models are tested on four tasks: feasibility assessment, mechanistic reasoning, generative solution design, and temporal prediction. The headline is sobering: models recognize plausible directions but cannot forecast outcomes.

- **Recognition is not foresight:** Models can identify plausible research directions when choosing among competing candidates, but they fail to reliably predict whether an advance will actually be realized, and they systematically misestimate when it will happen.
- **Domain-dependent, and timing is hardest:** Performance is highly heterogeneous across fields, with the timing of AI progress more predictable than advances in biology, chemistry, and physics. Temporal prediction is the weakest skill across the board.
- **Not just a training-cutoff artifact:** Performance is largely insensitive to whether an event falls before or after the model's training cutoff. Extra pre-cutoff knowledge helps but does not close the gap to full-information settings, and that gap widens for high-citation advances.
- **Why it matters:** Models also show systematic overconfidence and strong response biases, which means unreliable uncertainty estimates. As labs lean on AI to triage research bets, CUSP gives a controlled way to measure where it helps, surfacing directions, and where it fails, predicting outcomes.

[Paper](https://arxiv.org/abs/2605.22681) | [Tweet](https://x.com/dair_ai/status/2058215140789797204)

## 8\. Your Agents Are Aging Too

AgingBench is a longitudinal reliability benchmark for agent lifespan engineering, built on the observation that long-lived agents are still evaluated like freshly initialized models. It organizes agent degradation into four mechanisms: compression aging, where write-time summarization drops future-relevant details; interference aging, where accumulated similar memories crowd out the target fact; revision aging, where changed or derived state is not updated correctly; and maintenance aging from routine lifecycle events. Using a temporal dependency DAG to encode cross-session structure, it produces aging curves over an operational lifetime rather than a single day-one score, and points to where repair should target.

[Paper](https://arxiv.org/abs/2605.26302) | [Tweet](https://x.com/omarsar0/status/2059689897523642510)

## 9\. Harnesses Are Not Uniformly Better

This paper studies LLM agent harnesses through the lens of inference-time trajectory alignment, separating a harness into two mechanisms: task decomposition, which structures a task into sub-goals, and guided execution, which reshapes local action distributions during execution. The key finding is that more elaborate harnesses are not uniformly better. Increasing decomposition or guidance can improve execution but can also reduce final task success, producing concrete failure modes like over-decomposition, over-pruning, and hallucinated execution. Strikingly, partial harnesses that specify only the initial steps and leave the rest to the agent can reach a higher pass rate than fully structured workflows.

[Paper](https://arxiv.org/abs/2605.21516) | [Tweet](https://x.com/dair_ai/status/2059691141302542445)

## 10\. Epicure

Epicure trains a family of multilingual ingredient embeddings from scratch on 4.14 million recipes aggregated from 11 sources across seven languages, with raw ingredient strings normalized to 1,790 canonical entries via an LLM-augmented pipeline. It ships three skip-gram (Metapath2Vec) variants that share architecture but differ in what they walk: recipe co-occurrence only, chemical-compound structure from FlavorDB only, or a blend of both, placing each model at a different point on the chemistry-versus-recipe-context spectrum. The result is a compact, downloadable map of the emergent geometry of food, a clean reminder that representation learning generalizes well beyond text into surprisingly everyday domains.

[Paper](https://arxiv.org/abs/2605.22391) | [Tweet](http://localhost:7001/)