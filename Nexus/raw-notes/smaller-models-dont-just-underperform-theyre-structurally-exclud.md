---
title: "Smaller Models Don't Just Underperform. They're Structurally Excluded."
source: "https://x.com/AlphaSignalAI/status/2063999531621232770"
author:
  - "[[@AlphaSignalAI]]"
published: 2026-06-08
created: 2026-06-08
description: "The paper shows that larger models aren't merely better versions of smaller models. They can access different parts of the distribution.In 5..."
tags:
  - "clippings"
summary:
---
![Imatge](https://pbs.twimg.com/media/HKTMOlHbAAA0Y2h?format=jpg&name=large)

## The paper shows that larger models aren't merely better versions of smaller models. They can access different parts of the distribution.

> **In 5 minutes, you'll learn** why larger models don't just learn faster. They learn capabilities smaller models never acquire.

The standard explanation for why larger models outperform smaller ones: bigger models have more capacity. Train a smaller model longer, give it more data, it'll catch up.

A new paper from Stanford, Harvard, MIT, and Anthropic breaks that assumption.

Their argument: there are parts of the data distribution a smaller model will never learn. Not eventually. Not with more data. Never.

That's not a sample efficiency gap. That's a fundamentally different kind of failure.

## Scaling laws are hiding a discontinuity

Scaling laws tell us loss decreases predictably as models grow. Most practitioners read this as a smooth curve: smaller models are just undertrained larger models.

The paper shows this is wrong for a meaningful portion of what models need to learn.

The scaling law for a model trained with finite compute is:

**L\_C(N) proportional to N^(-0.34)**

The scaling law for a model trained with infinite data is:

**L\_inf(N) proportional to N^(-0.46)**

Since the infinite-data exponent (0.46) is larger than the finite-compute exponent (0.34), the asymptotic loss of a larger model is better than the asymptotic loss of a smaller model.

There is a part of the training distribution a smaller model fails to learn even under infinite training.

![Imatge](https://pbs.twimg.com/media/HKTJHBjbUAAOGx7?format=jpg&name=large)

The purple region in the chart is what a smaller model can reach with more data. The orange region below it is what only a larger model can reach. The smaller model isn't behind. It's excluded from that region entirely.

## The mechanism: neurons as a contested resource

Here's why, and the intuition is cleaner than the math.

During training, every task in the data mixture competes for the model's neurons. Frequent tasks generate strong, consistent gradient signals. Rare tasks generate weak, sporadic ones.

![Vídeo incrustat](https://pbs.twimg.com/amplify_video_thumb/2063996190157611009/img/IVsxvzYT4cZPtNxT?format=jpg&name=large)

0:10

In a small model, frequent tasks win that competition decisively.

A rare task signal arrives, briefly nudges some weights, then gets overwritten by the next batch of frequent task updates before it can accumulate into anything durable.

The paper calls this the update-and-forget loop:

> "In a small model, the same parameters face more competition: updates from frequent tasks undo the rare-task update before the next rare batch arrives. Rare-task learning then becomes an update-and-forget loop."

The formal result behind this is Theorem 4 in the paper, which bounds the gradient norm for a set of tasks by how much of their covariance is unexplained by the current representation, what they call the residual signal.

Once a model has fully learned the frequent tasks, their residual drops toward zero, their gradient norms become weak, and they stop interfering with everything else.

A large model has enough capacity to reach that point. A small model never does. Its frequent task gradients stay strong throughout training, perpetually overwriting rare task signals.

## What the experiments show

**Experiment 1: The phase diagram**

They train models of varying width on 32 regression tasks with controlled frequencies. The result is a clean phase diagram: orange means the task was learned, purple means it wasn't.

![Imatge](https://pbs.twimg.com/media/HKTKPH-aYAADxYS?format=jpg&name=large)

The staircase pattern is the key thing to read here. Rarer tasks sit lower on the y-axis. They only enter the orange region at larger model widths.

The dashed lines are the paper's analytic predictions from Theorem 3: features are learned in order of their utility score, defined as task frequency multiplied by feature complexity.

The predictions match the empirical boundaries almost exactly.

This isn't curve-fitting after the fact. The boundaries were predicted from the theory before the experiments ran.

**Experiment 2: Watching interference happen in real time**

They inject a rare task mid-training and track whether the model's signal accumulates or decays between injections.

![Imatge](https://pbs.twimg.com/media/HKTKdspacAAw3tR?format=jpg&name=large)

Small model (N=32): signal spikes when rare examples arrive, decays back to zero before the next injection. Flat overall trend. The model learns and forgets in a loop.

Large model (N=256): signal spikes and the baseline trends upward. Each exposure builds on the last. The model is compounding its rare task learning across thousands of frequent task updates.

This is the interference mechanism made visible.

**Experiment 3: Real language model pretraining**

They pretrain OLMo models from 4M to 4B parameters on the Dolma corpus, injecting novel tasks (modular arithmetic, comparison operations defined with randomly chosen tokens) at controlled frequencies.

Same result. Only larger models learn the infrequent tasks. Larger models also embed more task-specific Fourier features in their representations and show measurably less gradient interference between tasks, exactly as the theory predicts.

## The utility ranking theorem

The paper's Theorem 3 is worth understanding because it gives practitioners a concrete framework, not just a direction.

The theorem proves that a width-N model learns features in order of their utility score:

**utility(k, j) = task\_frequency(k) x feature\_complexity(k, j)**

Higher utility features get learned first. Lower utility features require larger models.

A rare task with many complex features has low utility scores across the board. It needs a model large enough to fully satisfy all the high-utility features first, leaving residual capacity available for the rare ones.

This turns model sizing from an empirical question into a reasoning problem. If you know the frequency of a task in your training distribution and its approximate complexity, you can reason about the minimum model size needed to learn it, rather than running ablations until something works.

## What this means if you're building with models

**Model size is a prerequisite, not a performance dial.**

If the task you care about is rare relative to your training distribution, there is a minimum model size below which it will not be learned. More training time won't change this.

**More data on rare cases is necessary but not sufficient.**

Increasing rare task frequency in your fine-tuning mixture helps by raising the utility score for those tasks. But below a certain model size, frequent task gradients still dominate and overwrite. You need both levers.

**Data mixture design is a capacity allocation problem.**

The utility framework gives you a way to reason about this explicitly. Which tasks are rare? How complex are they? What model size does that imply? These questions have approximate answers you can reason through before committing to a training run.

**Post-training can sometimes fix what pretraining missed.**

The paper notes rare tasks can sometimes be added via post-training fine-tuning even when pretraining failed to learn them. It works when the fine-tuning distribution is concentrated enough on the rare task to overcome interference.

But it's not guaranteed, and it doesn't address the underlying capacity problem.

## The deeper point

The benefits of scaling aren't smooth. They're stepwise.

A model just below the capacity threshold for frequent tasks and a model just above it can look nearly identical on average benchmarks. Their behavior on rare inputs is completely different.

The right question when evaluating a model isn't just "how is average performance?" It's "which parts of the distribution has this model actually crossed the threshold for?"

Most evaluation setups only answer the first question.

Smaller models aren't just slower to learn the long tail.

In a meaningful sense, the long tail is structurally inaccessible to them. The gradient math doesn't work in their favor, and more data won't change the math.

If the cases your system needs to handle reliably are rare in the training distribution, model size isn't a cost to minimize. It's a prerequisite to meet.