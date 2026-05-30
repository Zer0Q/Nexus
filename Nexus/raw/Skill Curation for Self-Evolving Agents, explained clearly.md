---
title: "Skill Curation for Self-Evolving Agents, explained clearly"
source: "https://x.com/neural_avb/status/2053873358853591435"
author:
  - "[[@neural_avb]]"
published: 2026-05-11
created: 2026-05-31
description: "Google's latest paper introduces SkillOS, a framework designed to help LLM agents evolve by learning to manage their own \"memories\" in the f..."
tags:
  - "clippings"
---
![Imatge](https://pbs.twimg.com/media/HIDRf9Aa4AAlWgb?format=jpg&name=large)

Google's latest paper introduces **SkillOS**, a framework designed to help LLM agents evolve by learning to manage their own **"memories"** in the form of reusable skills.

> i.e. automatically go Experiences -> Memories -> Skills

SkillOS treats skill management like an operating system (OS).

> It handles files and organizes and refines a persistent **SkillRepo.** The most interesting part of this method is how skills are discovered using a trainable module called the **Curator.** (Spoiler: They use RL)

![Imatge](https://pbs.twimg.com/media/HIDRpWIbEAA_GtU?format=jpg&name=large)

This article explains Google's new SkillOS paper. It was written by AVB (myself) with help from GPT-5.5 inside the Paper Breakdown harness.

## There are 3 things you should know about...

1. **Agent Executor (Frozen):** This is just an "actor" LLM that retrieves skills from the **SkillRepo** to solve a task. It is "frozen" during training, meaning we do not update it's weights at all. Its performance is improved purely by providing it with better skills.
2. **Skill Curator (Trainable):** This is another LLM that observes the Executor's trajectories and decides how to update the SkillRepo. It can perform operations like Insert (add a new skill), Update (refine an existing one), or Delete (remove redundant or useless skills).
3. **SkillRepo:** A repository of skills stored as structured **Markdown files**. Each skill includes its name, a description, code snippets, and usage guidelines, making it easy for the Executor to understand and apply.

![Imatge](https://pbs.twimg.com/media/HIDQe9YaUAAiRmD?format=jpg&name=large)

## You probably already know what skills are.

If not you can learn about skills from this original Anthropic post: [https://anthropic.skilljar.com/introduction-to-agent-skills/434525](https://anthropic.skilljar.com/introduction-to-agent-skills/434525)

> In the most basic sense, **skills** are just lazily loaded prompts.

It is just a YAML or MD file that contains a title and a description. Looks like this:

```markdown
---
name: frontend-design
description: techniques and instructions to write good UI code
---

instructions: <an essay about frontend patterns>
```

Imagine a directory full of skill files like these covering various topics (frontend-design, programming-patterns, marketing-skills, etc). Each skill is written in a different markdown file, and each skill contains a name and description in the header.

```text
(cmd) ➜ tree ~/.agents/skills
~/.agents/skills
├── copywriting
│   ├── references
│   │   ├── copy-frameworks.md
│   │   └── natural-transitions.md
│   └── SKILL.md
├── programming-patterns
│   └── SKILL.md
├── frontend-design
│   └── SKILL.md
├── marketing-psychology
│   └── SKILL.md
└── web-design-guidelines
    └── SKILL.md
```

Your agent harness (Claude Code, Codex, etc) receives a list of available skills at the top of it's system prompt. Then when you ask it to perform a specific task (say "help me create UI for this webpage"), it deduces that it should read the \`frontend-design\` skill completely before proceeding with your request. The agent then does a file-read operation (~/.AGENTS/skills/frontend-design/SKILL.md) and loads the full instruction into it's context.

> The goal of this paper is the skill creation phase. Generating clear and actionable instructions that increases agent performance in specific tasks. **The Curator LLM performs this task of maintaining the Skill Repository.**

> The Executor agent is purposefully left bland. It just performs the same as any other harness - receives skill headers as input, task request, and reads one of more skills via tool calls. There is no contribution by Google to the executor agent - the entire focus is on the Curator and the Skill Repository.

Note that original Anthropic skills architecture also included things like resource files, and executable code. These are not part of Google's SkillOS work, although they do mention future work is possible along that avenue. SkillOS only learns the text/prose portion of skills.

# How skills are discovered organically

SkillOS learns skills/instruction through exploration. Broadly, speaking the LLM agent goes and explores in an environment, and then we distill it's experiences into instructions and skills.

Let's break down each step to clearly understand how it works.

## Stage 1: The Agent Executor Runs

Before any skill is created, the **frozen Agent Executor** must first attempt to solve a task x​. It does this by:

1. Retrieving the top-k most relevant existing skills from the **SkillRepo** via **BM25 keyword matching** on YAML descriptions.
2. Running its multi-step interaction with the environment, producing a trajectory: A trajectory is a sequence of observations and actions.

At the end of trajectory, an **LLM-as-a-Judge** (a separate Qwen3-32B model) determines whether the task was completed successfully, emitting a correctness signal.

This trajectory, the correctness signal, and the previously retrieved skills StSt​ are then handed off to the Curator.

## Stage 2: Curator Input

The **Skill Curator**​ receives a structured prompt containing four key pieces of information:

1. **Task Description:** What the agent was trying to accomplish.
2. **Past Skills:** The list of previously retrieved relevant skills (names + content) that were available during execution.
3. **Agent Trajectory:** The full step-by-step trace showing what happened.
4. **Result:** Whether the agent succeeded or failed.

The curator's role, as stated directly in its system prompt, is:

> "to convert past experiences of agent task execution into reusable, general skills, so that they can benefit and inspire future tasks."

## Stage 3: Curator Output

The Curator then generates a sequence of **structured function calls.** It is a ReAct (Reasoning and Acting module) that contains the below tools:

**1\. new\_skill\_insert**

Creates a brand new skill. The Curator provides:

- skill\_name (string): A human-readable identifier
- content (string): The full Markdown body of the skill

When the trajectory reveals a generalizable strategy not yet represented in the SkillRepo, this is used! Specifically useful early in training when the repo is empty.

**2\. skill\_update**

Modifies an existing skill. The Curator provides:

- **skill\_name**: The exact name of the skill to update (must match exactly!)
- **new\_name**: A rename if needed
- **new\_content**: Full replacement content

**3\. skill\_delete**

Removes an existing skill by its skill\_name.

Useful when a skill is redundant, misleading, or superseded.

Here is the full system prompt for the Curator

![Imatge](https://pbs.twimg.com/media/HIDRIdmaMAANfxl?format=jpg&name=large)

## Every skill follows a simple format:

**YAML Frontmatter (Mandatory)**

```markdown
---
name: <Human-readable skill name>
description: <One-sentence what/when/why/how summary, concise and actionable>
---
```

The description field is **critical** as it is used by BM25 at retrieval time to match tasks to skills. It must be concise and actionable!

**Markdown Body**

Follows immediately after the frontmatter. Suggested sections include:

- **Workflow:** Step-by-step instructions
- **When NOT to use:** Negative conditions to avoid misapplication
- Additional sections like worked examples, formulas, or edge cases

Here is an example of a skill.

![Imatge](https://pbs.twimg.com/media/HIDDpePbsAEH5sT?format=jpg&name=large)

The Curator is explicitly instructed to obey these rules:

- **No Specifics:** Remove specific numbers/names, replace with variables/concepts
- **No Hallucination:** Only include facts supported by the actual trajectory
- **Atomic & Modular:** Each skill must be self-contained and reusable in isolation
- **Actionable:** The body must give concrete guidance, not vague advice

# That's fine, but how do we improve the skills?

> That's where RL comes in. We train the curator to write better skills by rewarding it on successful skills.

The Curator's training loop is the most technically sophisticated part of SkillOS. It solves a fundamentally hard RL problem: **how do you train an agent whose decisions only pay off in the future, through another agent?**

Standard RL assumes you can measure the effect of an action quickly. But curation is different:

> "The main challenge is indirect and delayed feedback for curation decisions, which is only revealed through skill performance on future relevant tasks."

If the Curator writes a bad skill after task t, you won't know it was bad until task t+5 fails because of it. The paper addresses this with two core mechanisms: **grouped training instances** and a **composite reward**.

## Phase 1: Grouped Training Instance Construction (most important)

Before any training happens, the dataset must be pre-processed into **groups of related tasks**. This is a two-stage pipeline. I won't get into too much details about this here, but the basic gist is this:

1. In Stage 1, we do **Latent Attribute Annotation.** Basically, they use Gemini-2.5-Pro to annotate every task in the dataset by it's type.
2. In Stage 2, we do **Group Construction** where given the annotated datasets we build groups of tasks. Each task also has a difficulty ranking so there is a natural curriculum in each task group.

Google tested with group size is **10 tasks** on ALFWorld and WebShop environment. And **random(5, 12)** for reasoning tasks (Math, GPQA, etc).

The group structure ensures that skills curated from early tasks are **directly testable** on later tasks in the same group.

## Phase 2: The Skill Creation Loop

During each training step, we first sample a task group, init an empty SkillRepo, and follow the skill creation process described earlier. Recap:

1. **Executor runs:** The frozen executor​ retrieves top-5 skills via BM25, solves task and produces trajectory​
2. **Correctness judged:** An LLM-judge evaluates whether task succeeded​​
3. **Curator:**​ reads trajectory and invokes tool calls to update skill repo​

## Phase 3: The Composite Reward

After a full group rollout completes, the composite reward is computed. It has **four components** combined as:

**1\. Task Outcome Reward**

The first task uses an empty SkillRepo, before any curator update occurs. As we create skills through completion of tasks, we must track how successful (or unsuccessful) the skills curated from these tasks are.

This is the main learning signal: did the skills curated from earlier tasks help later tasks succeed?

**2\. Function Call Reward**​

Measures what **fraction of generated function calls are syntactically valid and successfully execute** against the SkillRepo. This is an intermediate format reward that prevents the Curator from producing malformed JSON or calling skill\_update on a skill that doesn't exist.

**3\. Compression Reward​**

This **penalizes verbatim trajectory copying** and rewards skills that are genuinely compressed, distilled knowledge. Without this, the Curator would learn to just dump raw trajectories into the repo.

**4\. Content Quality Reward**

Assigned by **Qwen3-32B acting as a judge:** it reads the curated skills and scores them on whether they are:

- Semantically meaningful
- Likely to be useful for future tasks
- Faithful and actionable

This provides a dense intermediate signal independent of actual downstream task success.

> All of these rewards are combined (weighted average) to calculate the final group reward.

## Phase 4: GRPO Policy Optimization

We use GRPO to train the Curator model. For each group, we sample N=8 independent rollouts, each producing a composite reward for each. Then we follow standard GRPO optimization to update the network (normalize advantage, and clipped surrogate PPO objective)

Importantly, the KL divergence penalty is **discarded** from the standard GRPO formulation. his is intentional to **encourage policy exploration** during skill curation learning.

![Imatge](https://pbs.twimg.com/media/HIDQl9-boAAqQPG?format=jpg&name=large)

> In RL training, a **rollout** is simply one complete run through a task (or sequence of tasks) - the model acts, receives feedback, and that entire trajectory is used for learning.

> In SkillOS, the training unit isn't a single task. It's a **task group** (e.g., 10 related tasks solved one after another). A **rollout** here means **running through that entire group from start to finish, once**.

**What Makes Each Rollout Independent?**

Each of the 8 rollouts is an **independent parallel attempt** at the same task group:

- **Rollout 1**: Curator makes curation decisions c1,c2,…,cn→ SkillRepo evolves one way
- **Rollout 2**: Curator makes different curation decisions → SkillRepo evolves differently
- ... and so on for all 8 rollouts

Each rollout produces a **different version of the SkillRepo** because the curator's stochastic sampling leads to different insert/update/delete decisions

GRPO computes a **relative reward** across the 8 rollouts. For rollout k at task position i, the reward r\_k​ reflects how well that curation sequence helped solve future tasks.

> Rollouts that led to better skill curation (higher reward) get **positive advantage** and are reinforced. Poor rollouts get **negative advantage** and are suppressed.

![Imatge](https://pbs.twimg.com/media/HIDQyxbbkAIV8Tf?format=jpg&name=large)

# Results

Here are the **big-stroke takeaways and results** from SkillOS:

**1\. SkillOS Beats All Baselines Consistently**

Across **multi-turn agentic tasks** (ALFWorld, WebShop) and **single-turn reasoning tasks** (AIME math), SkillOS outperforms both **Memory-free** baselines (no memory at all), and **Strong memory-based** baselines (e.g., ReasoningBank, MemP)

![Imatge](https://pbs.twimg.com/media/HIDQ8ycbUAEM1r8?format=jpg&name=large)

**2\. The Curator Generalizes to Unseen Executors**

The curator is trained with **Qwen3-8B** as executor. But at test time, it works with completely different models it has never seen:

- **Open-source**: Qwen3-8B, Qwen3-32B
- **Frontier**: Gemini-2.5-Pro

> A key insight: using Gemini-2.5-Pro directly as the curator (SkillOS-gemini) actually **underperforms** the trained SkillOS curator especially for weaker executors.

> Stronger reasoning alone doesn't guarantee good curation. RL-trained curation is **grounded in the executor's actual capacity**.

**3\. Every Reward Component Matters (Ablations)**

Removing any piece of the training recipe hurts performance:

- **Full SkillOS: 61.2**
- w/o content-quality reward: 58.6
- w/o compression reward: 60.0
- w/o task grouping: 57.3

The **biggest drop** comes from removing **task grouping.** Confirming that learning from related sequential tasks is the core insight of the whole approach.

Study the full paper here: [https://arxiv.org/abs/2605.06614](https://arxiv.org/abs/2605.06614)

Study the paper on Paper Breakdown: [http://paperbreakdown.com/abs/2605.06614](http://paperbreakdown.com/abs/2605.06614)