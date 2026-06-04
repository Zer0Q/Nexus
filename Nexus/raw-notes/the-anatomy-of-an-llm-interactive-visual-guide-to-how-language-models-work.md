---
title: "The Anatomy of an LLM | Interactive Visual Guide to How Language Models Work"
source: "https://www.royvanrijn.com/anatomy-of-an-llm/"
author:
  - "[[Roy van Rijn]]"
published:
created: 2026-05-31
description: "An interactive visual explainer for developers showing how LLMs work, from tokenization and embeddings to attention, transformers, training, KV cache, and quantization."
tags:
  - "clippings"
---
## Introduction

Large language models can feel like black boxes. You type a prompt, something smart comes back, and somewhere in the middle billions of parameters supposedly did "AI".

This guide opens that box.

We will follow one chain from beginning to end. First, text is split into tokens. Those tokens become vectors. The vectors move through layers of attention and feed-forward networks. At the end, the model produces scores for possible next tokens, and a decoding strategy chooses what comes out.

The goal is not to memorize every formula. The goal is to understand what changes at each step, and why that step exists at all.

If you are looking for how LLMs work, how transformers work, or how attention, tokenization, KV cache, and quantization fit together, this page keeps those ideas connected in one visual path.

By the end, you should be able to trace the full path:

And once you can trace that path, the black box becomes a lot smaller.

What you get

Concrete visuals, small numbers first, and interactive controls that make each transformation inspectable.

How to use it

Scroll top to bottom as a single narrative, or jump between chapters for a specific concept.

Who made this

Roy van Rijn working at [openvalue](https://www.openvalue.eu/)

Table of contents

## Tokenization

Before a model can think about text, the text has to become numbers.

A language model does not read words and sentences the way we do. It reads a sequence of token IDs: integers produced by a tokenizer.

That makes tokenization the real entrance to the model. Everything after this point works with numbers, not raw characters.

A token can be a whole word, part of a word, punctuation, whitespace, or a piece of something strange like code, emoji, or a name. This is why tokenization often looks a bit weird when you first see it. The tokenizer is not trying to split text the way a human would. It is trying to represent text efficiently using a fixed vocabulary.

If every token were a full word, the vocabulary would explode. If every token were a single character or byte, every sentence would become very long. Modern tokenizers live between those extremes.

Slicing up the text

Before text can enter a language model, it has to be rewritten as numbers.

Tokenization is the step that does this. It splits text into small reusable pieces called **tokens**. A token can be a whole word, part of a word, punctuation, a number, or even a space plus the start of the next word.

Each token has an entry in the tokenizer's vocabulary and is replaced by its corresponding integer ID. From that point on, the model is no longer working with characters directly. It sees an ordered list of token IDs.

Why not just use words?

Whole words are too rigid. New names, typos, code, inflections, compound words, and multilingual text would constantly produce words the model has never seen before.

Why not just use letters or bytes?

That solves the "unknown word" problem, but makes every input much longer. More pieces means more work for the model and less context fits in the same window. Subword tokens are the reasonable compromise: common text stays compact, while unusual text can still be built from smaller pieces.

Below you can experiment with OpenAI's `o200k_base` tokenizer. Try switching sentences and watch where the boundaries land.

Later in this explainer, when the model predicts the *next* token, it predicts over this same vocabulary.

Technical note: the examples below are generated with [`tiktoken`](https://github.com/openai/tiktoken) using the `o200k_base` encoding.

Raw sentence

If the human brain were so simple that we could understand it, we would be so simple that we couldn't.

**102** characters

**22** tokens

**5** chars/token on average

Tokenized result

If

#3335

·the

#290

·human

#5396

·brain

#12891

·were

#1504

·so

#813

·simple

#4705

·that

#484

·we

#581

·could

#2023

·understand

#4218

·it

#480

,

#11

·we

#581

·would

#1481

·be

#413

·so

#813

·simple

#4705

·that

#484

·we

#581

·couldn't

#21149

.

#13

Important takeaway

Tokenization is not just preprocessing. It determines what the model can see in one context window, how expensive your text is, and which pieces the model is allowed to predict next.

One word is not one token

Different models use different tokenizers. The same sentence can become a different number of tokens depending on the model.

## Vector Embeddings

Token IDs are just labels. Embeddings turn those labels into something the network can work with.

After tokenization, every token is represented by an integer ID. But an ID by itself has no useful geometry. Token `15339` is not "close to" token `15340` in any meaningful way. The numbers are just labels, like row numbers in a table.

The embedding layer solves this by turning each token ID into a vector: a list of learned numbers. Technically, this is a lookup. The model has an embedding matrix, and each token ID selects one row from that matrix.

Conceptually, this is the moment where discrete symbols enter a continuous space. Once tokens become vectors, the model can compare them, combine them, rotate them, project them, and gradually reshape them.

The values inside these vectors are learned during training. Tokens that appear in similar contexts often end up with related vectors, but this is not a clean dictionary of meanings. It is more like a messy, high-dimensional coordinate system full of useful signals.

The initial embedding is mostly context-free. The token "bank" starts with the same embedding in "river bank" and "investment bank". Later layers use surrounding tokens to rewrite that vector into something more specific.

From token ID to embedding vector

Embedding lookup

After tokenization, each token ID is used as an index into an embedding table. The selected row is a high-dimensional vector that becomes the model's starting representation for that token.

For readability, this chapter uses a toy embedding width of 24 dimensions. Real model widths are usually much larger, common production widths include 768, 1024, 1536, 3072, and even higher.

An embedded vector is just a list of floating point numbers: dog = \[0.7292, -0.3786, 0.1065, 0.3674, 0.1902, -0.7881,... \]

If

\->

token ID #3335

\->

embedding row 3335

Embedding values (24 dimensions)

This explainer shows all 24 values from the toy vector.

`0.2173`

`0.5424`

`0.264`

`-0.9419`

`-0.5084`

`0.0872`

`-0.6438`

`0.164`

`-0.2094`

`0.6078`

`0.9056`

`-0.5944`

`0.1676`

`-0.0086`

`-0.6874`

`-0.5004`

`-0.4561`

`-0.168`

`0.443`

`-0.6566`

`-0.184`

`-0.4863`

`0.679`

`-0.044`

The same token ID always maps to the same embedding vector.

In real models, these embedding values are learned during training. Tokens that appear in similar contexts are gradually moved to useful regions of vector space, so the vectors end up encoding patterns the model can build on.

Tokens that often play similar roles get nudged in similar directions. For example, the tokens cat, dog, and rabbit often appear in sentence templates like "The \_\_\_ is sleeping", "I fed the \_\_\_", or "The \_\_\_ ran away". Because they appear in similar contexts, their vectors may end up close together.

But cat and car usually appear in very different contexts, so their vectors tend to end up farther apart.

The embedding space is not hand-designed. Nobody tells the model “put animals over here” or “put verbs over there”. Those patterns emerge because moving the vectors that way helps the model predict text better.

2D analogy intuition

Distances between embedding vectors often similar if they have a similar relationship.

<svg viewBox="0 0 360 140" role="img" aria-label="2D relation offset analogy" style="max-width: 100%;"><defs><marker id="arrowhead" markerWidth="5" markerHeight="5" refX="4.3" refY="2.5" orient="auto"><polygon points="0 0, 5 2.5, 0 5" fill="#9ca3af"></polygon></marker></defs><line x1="78.40831222698239" y1="100.71769373739926" x2="147.5916877730176" y2="65.28230626260074" stroke="#9ca3af" stroke-width="1.7" stroke-dasharray="3 3" stroke-linecap="round" marker-end="url(#arrowhead)"></line><line x1="208.37798705401713" y1="95.65914963837199" x2="279.6220129459829" y2="58.340850361628014" stroke="#9ca3af" stroke-width="1.7" stroke-dasharray="3 3" stroke-linecap="round" marker-end="url(#arrowhead)"></line><circle cx="72" cy="104" r="5.6" fill="#64748b" stroke="#475569" stroke-width="0.9"></circle><circle cx="154" cy="62" r="5.6" fill="#64748b" stroke="#475569" stroke-width="0.9"></circle><circle cx="202" cy="99" r="5.6" fill="#64748b" stroke="#475569" stroke-width="0.9"></circle><circle cx="286" cy="55" r="5.6" fill="#64748b" stroke="#475569" stroke-width="0.9"></circle><text x="49" y="120">puppy</text> <text x="147" y="52">dog</text> <text x="178" y="115">kitten</text> <text x="278" y="45">cat</text></svg>

Important takeaway

An embedding is the token's starting representation, not its final meaning. The rest of the model will keep rewriting that vector as context flows through the network.

Toy scale

In this explainer we use small vectors because they fit on screen. Real models use much wider vectors: hundreds, thousands, or more dimensions per token.

## Neuron Activation

A weighted sum is not enough. The non-linearity is where the network gets expressive.

A neuron takes inputs, multiplies them by weights, adds them together, and produces a number. But if that were the whole story, deep learning would not be very deep.

Without activation functions, stacking layers would still behave like one large linear transformation. You could multiply matrices together and collapse the whole stack into a single matrix.

The activation function breaks that linearity. It decides how much of a signal passes through. Some values are amplified, some are softened, some are pushed toward zero.

This lets the network build curved, conditional, non-linear transformations instead of only scaling and rotating vectors. Real models do this in huge batches using matrix operations, with millions of activations happening at once.

Single-neuron transformation

A neuron takes inputs, applies weights, and then runs the result through an activation function. This non-linear step is what lets networks model richer patterns.

`z = w1*x1 + w2*x2 + w3*x3`

`output = activation(z)`

Neuron diagram

<svg viewBox="0 0 620 200" role="img" aria-label="Three inputs with weighted edges into one neuron and one output" style="max-width: 100%;min-height: 170px;min-height: 170px;"><line x1="117.5" y1="52.7" x2="289.0" y2="90.5" stroke="currentColor" stroke-opacity="0.2"></line><line x1="118.0" y1="100.0" x2="288.0" y2="100.0" stroke="currentColor" stroke-opacity="0.2"></line><line x1="117.5" y1="147.3" x2="289.0" y2="109.5" stroke="currentColor" stroke-opacity="0.2"></line><text x="182" y="64" fill="currentColor">w1=1.10</text> <text x="182" y="96" fill="currentColor">w2=-0.85</text> <text x="182" y="146" fill="currentColor">w3=0.55</text> <circle cx="96" cy="48" r="22" fill="none" stroke="currentColor"></circle><circle cx="96" cy="100" r="22" fill="none" stroke="currentColor"></circle><circle cx="96" cy="152" r="22" fill="none" stroke="currentColor"></circle><text x="96" y="44" text-anchor="middle" fill="currentColor">x1</text> <text x="96" y="59" text-anchor="middle" fill="currentColor">0.70</text> <text x="96" y="96" text-anchor="middle" fill="currentColor">x2</text> <text x="96" y="111" text-anchor="middle" fill="currentColor">-0.25</text> <text x="96" y="148" text-anchor="middle" fill="currentColor">x3</text> <text x="96" y="163" text-anchor="middle" fill="currentColor">0.45</text> <circle cx="332" cy="100" r="44" style="fill-opacity:0.554;" fill="none" stroke="currentColor"></circle><text x="332" y="95" text-anchor="middle" fill="currentColor">Σ</text> <text x="332" y="112" text-anchor="middle" fill="currentColor">z=1.23</text> <line x1="376" y1="100" x2="488" y2="100" stroke="currentColor" stroke-opacity="0.2"></line><text x="408" y="86" fill="currentColor">GELU</text> <circle cx="520" cy="100" r="32" fill="none" stroke="currentColor"></circle><text x="520" y="95" text-anchor="middle" fill="currentColor">out</text> <text x="520" y="110" text-anchor="middle" fill="currentColor">1.10</text></svg>

Inputs

Weights

Activation

Smoothly gates values by magnitude instead of hard clipping. Common in transformer blocks; a bit heavier to compute than ReLU.

Neuron output **1.0953**

Activation curve

<svg viewBox="0 0 520 220" role="img" aria-label="Activation function curve with current marker" style="max-width: 100%;"><line x1="26" y1="194" x2="494" y2="194" stroke="currentColor" stroke-opacity="0.2"></line><line x1="26" y1="26" x2="26" y2="194" stroke="currentColor" stroke-opacity="0.2"></line><line x1="260" y1="26" x2="260" y2="194" stroke="currentColor" stroke-opacity="0.2"></line><line x1="26" y1="187.02443764337252" x2="494" y2="187.02443764337252" stroke="currentColor" stroke-opacity="0.2"></line><path d="M 26.00 187.03 L 30.68 187.03 L 35.36 187.03 L 40.04 187.03 L 44.72 187.04 L 49.40 187.04 L 54.08 187.05 L 58.76 187.06 L 63.44 187.07 L 68.12 187.08 L 72.80 187.10 L 77.48 187.13 L 82.16 187.16 L 86.84 187.19 L 91.52 187.24 L 96.20 187.30 L 100.88 187.37 L 105.56 187.45 L 110.24 187.56 L 114.92 187.68 L 119.60 187.82 L 124.28 187.98 L 128.96 188.17 L 133.64 188.38 L 138.32 188.62 L 143.00 188.89 L 147.68 189.19 L 152.36 189.51 L 157.04 189.86 L 161.72 190.24 L 166.40 190.63 L 171.08 191.05 L 175.76 191.47 L 180.44 191.89 L 185.12 192.31 L 189.80 192.71 L 194.48 193.08 L 199.16 193.40 L 203.84 193.68 L 208.52 193.88 L 213.20 193.99 L 217.88 194.00 L 222.56 193.89 L 227.24 193.64 L 231.92 193.25 L 236.60 192.69 L 241.28 191.95 L 245.96 191.02 L 250.64 189.89 L 255.32 188.56 L 260.00 187.02 L 264.68 185.28 L 269.36 183.32 L 274.04 181.16 L 278.72 178.80 L 283.40 176.26 L 288.08 173.53 L 292.76 170.64 L 297.44 167.60 L 302.12 164.42 L 306.80 161.13 L 311.48 157.73 L 316.16 154.24 L 320.84 150.68 L 325.52 147.07 L 330.20 143.41 L 334.88 139.73 L 339.56 136.02 L 344.24 132.31 L 348.92 128.61 L 353.60 124.91 L 358.28 121.23 L 362.96 117.56 L 367.64 113.93 L 372.32 110.32 L 377.00 106.73 L 381.68 103.18 L 386.36 99.65 L 391.04 96.15 L 395.72 92.68 L 400.40 89.23 L 405.08 85.80 L 409.76 82.39 L 414.44 79.01 L 419.12 75.64 L 423.80 72.28 L 428.48 68.93 L 433.16 65.60 L 437.84 62.28 L 442.52 58.96 L 447.20 55.65 L 451.88 52.34 L 456.56 49.04 L 461.24 45.75 L 465.92 42.45 L 470.60 39.16 L 475.28 35.87 L 479.96 32.58 L 484.64 29.29 L 489.32 26.00" fill="none" stroke="currentColor"></path><circle cx="331.95500000000004" cy="142.03166640809968" r="5.5" fill="none" stroke="currentColor"></circle><text x="266" y="210" fill="currentColor">x = 0</text> <text x="32" y="181.02443764337252" fill="currentColor">y = 0</text></svg>

Marker position updates live as the weighted input `z` changes.

Important takeaway

The activation function is not decoration. It is what lets stacked layers become more than one big linear calculation.

Modern choices

Modern transformer models may use GELU, SiLU, or gated variants like SwiGLU. The exact choice changes both the forward signal and how gradients flow during training.

## Feed-Forward Neural Network

A real layer is not one neuron. It is many simple computations running in parallel.

A single neuron is a useful teaching tool, but models do not process one neuron at a time. A feed-forward network applies many learned transformations in parallel.

Instead of drawing every neuron and every connection, implementations usually express the same thing as matrix multiplication. The friendly diagram says inputs flow through neurons. The implementation says multiply a matrix, apply an activation, multiply another matrix.

Those are the same story at different scales.

In transformer blocks, the feed-forward part usually works position by position. Each token vector is expanded into a wider hidden representation, passed through a non-linearity, and projected back to the model width.

Attention moves information between positions. The feed-forward network transforms the information inside each position.

Dense layer math, visually

Instead of training a full network here, we focus on one forward pass. A dense layer simply means every node in one layer connects to every node in the next layer.

The same math from one neuron is now done in parallel using matrices:

`X(1x2) · W1(2x3) = Z1(1x3)`, then `A1 = activation(Z1)`, then `A1(1x3) · W2(3x2) = Z2(1x2)`.

Matrix multiplication is just many weighted sums at once. Each output column is one neuron, and each row in the input contributes through its matching weight row.

Fully connected view

<svg viewBox="0 0 390 220" role="img" aria-label="input hidden output dense layer graph" style="max-width: 100%;min-height: 190px;min-height: 190px;"><text x="55" y="18" text-anchor="middle" fill="currentColor">X</text> <text x="122" y="18" text-anchor="middle" fill="currentColor">W1</text> <text x="195" y="18" text-anchor="middle" fill="currentColor">A1</text> <text x="265" y="18" text-anchor="middle" fill="currentColor">W2</text> <text x="335" y="18" text-anchor="middle" fill="currentColor">A2</text> <circle cx="55" cy="70" r="13" fill="none" stroke="currentColor"></circle><text x="55" y="74" text-anchor="middle" fill="currentColor">x1</text> <circle cx="55" cy="150" r="13" fill="none" stroke="currentColor"></circle><text x="55" y="154" text-anchor="middle" fill="currentColor">x2</text> <text x="195" y="49" text-anchor="middle" fill="currentColor">h1</text> <text x="195" y="109" text-anchor="middle" fill="currentColor">h2</text> <text x="195" y="169" text-anchor="middle" fill="currentColor">h3</text> <circle cx="335" cy="90" r="13" fill="none" stroke="currentColor"></circle><text x="335" y="94" text-anchor="middle" fill="currentColor">o1</text> <circle cx="335" cy="140" r="13" fill="none" stroke="currentColor"></circle><text x="335" y="144" text-anchor="middle" fill="currentColor">o2</text><line x1="68" y1="70" x2="182" y2="45" stroke="currentColor" stroke-opacity="0.2"></line><line x1="68" y1="70" x2="182" y2="105" stroke="currentColor" stroke-opacity="0.2"></line><line x1="68" y1="70" x2="182" y2="165" stroke="currentColor" stroke-opacity="0.2"></line><line x1="68" y1="150" x2="182" y2="45" stroke="currentColor" stroke-opacity="0.2"></line><line x1="68" y1="150" x2="182" y2="105" stroke="currentColor" stroke-opacity="0.2"></line><line x1="68" y1="150" x2="182" y2="165" stroke="currentColor" stroke-opacity="0.2"></line><line x1="208" y1="45" x2="322" y2="90" stroke="currentColor" stroke-opacity="0.2"></line><line x1="208" y1="45" x2="322" y2="140" stroke="currentColor" stroke-opacity="0.2"></line><line x1="208" y1="105" x2="322" y2="90" stroke="currentColor" stroke-opacity="0.2"></line><line x1="208" y1="105" x2="322" y2="140" stroke="currentColor" stroke-opacity="0.2"></line><line x1="208" y1="165" x2="322" y2="90" stroke="currentColor" stroke-opacity="0.2"></line><line x1="208" y1="165" x2="322" y2="140" stroke="currentColor" stroke-opacity="0.2"></line></svg>

Hover the top labels to inspect matrices. Green border means firing, red means suppressed.

Matrix inspector

Hover one of the top labels (`X`, `W1`, `A1`, `W2`, `A2`) to inspect that matrix and the multiplication step.

How multiplication maps to connections

Column `j` in `W1` contains weights feeding hidden neuron `j`. Row `i` corresponds to input feature `i`. So each hidden pre-activation is: `z1_j = x1*w1_1j + x2*w1_2j`.

The second layer repeats that pattern with `A1` as input: `z2_k = a1_1*w2_1k + a1_2*w2_2k + a1_3*w2_3k`. This is exactly the graph computation, just vectorized.

In matrix form, we avoid writing each neuron separately: `[x1 x2] · W1 = [z1_1 z1_2 z1_3]`, then activation applies element-wise to produce `A1`. That `A1` row is then multiplied by `W2` to produce both output neurons at once.

Example from the current sliders: `z1_1 = +0.80*+0.70 + -0.30*+0.10 = +0.53`. If activation suppresses this value (for example ReLU on negative values), that path contributes less or zero to the next layer.

Important takeaway

The feed-forward network is where each token vector gets rewritten. It is not about moving information between tokens; it is about transforming the representation at each token position.

Matrix view

The matrix view is not a less intuitive version of the neuron diagram. It is the scalable version of the same computation.

## Logits and Sampling

The model does not directly output a word. It outputs scores for possible next tokens.

After the model has processed the input, it still has not chosen a word. What it has produced is a vector of raw scores: one score for every token in the vocabulary. These scores are called logits.

A logit is not a probability. It is just an unnormalized score. Higher usually means "the model thinks this token fits better here", but the numbers do not yet add up to 100%.

To turn logits into probabilities, we apply softmax. Then comes decoding: the policy for choosing the next token from that distribution.

Greedy decoding always picks the most likely token. Temperature changes the shape of the distribution. Top-k limits the choice to the k most likely tokens. Top-p, also called nucleus sampling, chooses from the smallest group of tokens whose total probability passes a threshold.

The model produces the distribution. The decoder decides how adventurous we are when sampling from it.

From logits to generated output

A model converts the final hidden vector into one score per vocabulary token. Those raw scores are logits. Softmax turns them into probabilities, and sampling chooses the next token.

Logits

calm `0.81`

inside `0.34`

outside `0.49`

cold `-0.45`

angry `-0.84`

. `-0.06`

, `-0.03`

Probabilities (after softmax)

calm `27.3%`

inside `17.1%`

outside `19.6%`

cold `7.7%`

angry `5.2%`

. `11.4%`

, `11.7%`

Sampled output

Generated sequence (10 tokens): `(click generate)`

Important takeaway

The model usually does not contain one fixed answer. At each generation step, it produces a probability distribution over possible next tokens.

Token by token

A chatbot answer is built one token at a time. After each sampled token, the new token is added to the context and the process repeats.

## Backpropagation

To learn, the model needs to know which parameters helped cause the mistake.

Training starts with a simple question: how wrong was the model?

The model predicts a distribution over the next token. We know which token actually came next in the training text. The loss measures how far the prediction was from that target.

But measuring the loss is not enough. The model has billions of parameters. Which ones should change? And by how much?

Backpropagation answers that question. It sends the error signal backward through the computation graph and calculates gradients: how sensitive the loss is to each parameter.

The core idea is the chain rule. Every operation only needs to know how its output changes with respect to its input. By chaining those local derivatives together, training can calculate how a tiny change deep inside the model would affect the final loss.

Error becomes learning signal

We will train on one tiny example and reveal each step in order: forward prediction, backward gradients, then the weight update.

Step 1 - Predict from input

Three, two, one... \_\_\_

Important takeaway

Backpropagation is not a second mysterious intelligence inside the model. It is an efficient way to calculate gradients through a large composed computation.

Three passes

Forward pass: make a prediction. Backward pass: calculate how to change the parameters. Optimizer step: actually change them.

## Optimizers

Gradients point downhill. Optimizers decide how to walk.

A gradient tells us which direction should reduce the loss. But it does not fully answer how to update the model.

How big should the step be? Should we trust the current gradient completely? Should we remember previous gradients? What if different parameters have wildly different gradient scales?

That is the job of the optimizer.

SGD, or stochastic gradient descent, is the simplest common version. It looks at a small batch of training examples, calculates the gradient, and takes one step in the direction that should reduce the loss. It is direct and easy to understand, but each step can be noisy because it only sees a slice of the training data.

Momentum improves on this by remembering direction. If gradients keep pointing roughly the same way, momentum builds speed. If they zigzag, momentum smooths the path.

Adam tracks both a moving average of the gradients and a moving estimate of their scale. That lets it adapt update sizes per parameter.

The optimizer is not just a detail after backpropagation. It is part of the learning behavior.

Different update rules, same gradients

Backprop gives gradients. Optimizers decide how to turn those gradients into actual parameter updates.

Optimizer trajectories on one toy loss surface

<svg viewBox="0 0 380 220" role="img" aria-label="optimizer path comparison" style="max-width: 100%;min-height: 250px; touch-action: none;min-height: 250px; touch-action: none;"><ellipse cx="190" cy="112" rx="154" ry="82" fill="none" stroke="currentColor"></ellipse><ellipse cx="190" cy="112" rx="114" ry="60" fill="none" stroke="currentColor"></ellipse><ellipse cx="190" cy="112" rx="78" ry="42" fill="none" stroke="currentColor"></ellipse><ellipse cx="190" cy="112" rx="48" ry="26" fill="none" stroke="currentColor"></ellipse><circle cx="190" cy="112" r="3.2" fill="none" stroke="currentColor"></circle><path d="M296.0,166.8 L285.9,153.9 L276.3,144.4 L267.4,137.1 L259.3,131.7 L251.9,127.6 L245.2,124.4 L239.1,122.0 L233.6,120.1 L228.8,118.6 L224.4,117.5 L220.5,116.6 L217.0,115.8 L213.9,115.2 L211.2,114.8 L208.8,114.4 L206.6,114.0 L204.7,113.7 L203.0,113.5" fill="none" stroke="currentColor"></path><path d="M296.0,166.8 L294.8,165.2 L292.5,162.4 L289.3,158.5 L285.3,153.7 L280.7,148.4 L275.5,142.8 L269.9,137.0 L263.9,131.2 L257.7,125.7 L251.3,120.5 L244.9,115.8 L238.4,111.7 L232.0,108.1 L225.8,105.2 L219.7,102.9 L213.9,101.2 L208.4,100.1 L203.2,99.6" fill="none" stroke="currentColor"></path><path d="M296.0,166.8 L288.0,162.3 L280.0,157.8 L272.1,153.3 L264.2,148.9 L256.4,144.5 L248.7,140.2 L241.2,136.0 L233.8,132.0 L226.6,128.0 L219.6,124.2 L212.9,120.6 L206.5,117.3 L200.5,114.1 L194.8,111.3 L189.6,108.7 L184.9,106.4 L180.6,104.5 L176.9,102.9" fill="none" stroke="currentColor"></path><circle cx="203.0146033729061" cy="113.5141031122607" r="3" fill="none" stroke="currentColor"></circle><circle cx="203.206062358282" cy="99.56022705230924" r="3" fill="none" stroke="currentColor"></circle><circle cx="176.93340602277695" cy="102.91419484191464" r="3" fill="none" stroke="currentColor"></circle><g><circle cx="296.00667559008605" cy="166.76568619515137" r="6.5" fill="none" stroke="currentColor"></circle><circle cx="296.00667559008605" cy="166.76568619515137" r="12" fill="none" stroke="currentColor"></circle></g><text x="190" y="102" text-anchor="middle" fill="currentColor">min</text></svg>

SGD

loss start: `2.8313`

loss end: `0.0176`

delta: `-2.8137`

Momentum

loss start: `2.8313`

loss end: `0.1429`

delta: `-2.6884`

Adam

loss start: `2.8313`

loss end: `0.0670`

delta: `-2.7643`

All optimizers see the same gradients. Their update rules differ, so their paths differ.

Important takeaway

Gradients tell the model where improvement may be. The optimizer decides how aggressively and in what style the model moves there.

Same gradients, different path

SGD, Momentum, and Adam can start from the same point and see the same gradients, yet follow different paths because each optimizer keeps different internal state.

## Attention: Q, K, and V

Attention lets tokens pull useful information from other tokens.

Embeddings alone are too context-free. Take a word like "mole". It might mean a small animal, a mark on skin, a spy, or a unit in chemistry. The starting embedding is the same token representation, but the meaning depends on the surrounding words.

The model needs a way for tokens to talk to each other. That is what attention does.

For each token, the model creates three learned views: query, key, and value. The query represents what this token is looking for. The key represents what this token can be matched on. The value represents the information this token can contribute.

The model compares queries to keys to produce attention scores. Those scores are turned into weights, and the weights are used to mix the value vectors. So Q and K decide where information flows. V is the information that flows.

How tokens exchange information

Right now we only have tokens. But sentences encode extra meaning through relationships between nearby words and references.

Select one token to inspect which key tokens it matches with (arrows), then how those weights mix into one updated value representation.

Context Scenario

A blue car crashed into a concrete wall, it was speeding.

Sentence Tokens

Pick any token to compute attention links and value mixing.

Important takeaway

Attention is information routing. Query and key determine relevance; value carries the content that gets mixed in.

Self-attention

In self-attention, tokens attend to other tokens in the same sequence. In a decoder-only LLM, causal masking prevents a token from attending to future tokens during generation.

## Multi-Head Attention

One attention pattern is useful. Many attention patterns in parallel are much more powerful.

A sentence contains many kinds of relationships at once. An adjective may modify a noun. A pronoun may refer to something earlier. A closing bracket may match an opening bracket. A verb may depend on the subject.

One attention head can learn one way of routing information. But one routing pattern is not enough. Multi-head attention runs several attention heads in parallel. Each head has its own learned projections, so each head can learn a different kind of relationship.

After the heads produce their outputs, those outputs are combined and projected back into the model dimension. This does not mean every head has a clean human-readable job. Attention weights are useful clues, not perfect explanations.

Modern models often use grouped-query attention. Groups of query heads share key/value heads, reducing memory use during inference, especially in the KV cache, while keeping much of the benefit of many query heads.

Raw scores -> softmax weights -> value mixing

We also introduce **multi-head attention** here. In modern Transformer models each block doesn't just have a single attention head, but multiple. Different heads can learn different routing patterns, then their outputs are combined.

Each token creates three learned views of itself:

`Q` - the question this token asks.

`K` - what this token advertises about itself.

`V` - the information this token contributes.

For one selected query token, we compare its `Q` vector with every `K` vector.

Only after softmax do these scores become attention weights. Those weights decide how much of each V vector is mixed into this token’s next representation.

Tensor Shapes

We start with token vectors, project them into `Q`, `K`, and `V`, compute query-key compatibility scores, then convert those scores into attention weights and mix values.

`Q = XWq` -> `K = XWk` -> `V = XWv` -> `scores = QK^T / sqrt(d_k)` -> `weights = softmax(scores)` -> `output = weights·V`

This example uses unmasked self-attention, so every token can attend to every token. A GPT-style causal decoder would mask future tokens.

Which token is asking a question?

Selected token: `blue`

Its query asks: "Which other tokens help me understand `blue`?"

Emphasizes modifiers routing to the noun they describe (for example blue -> car).

Q View

`blue` embedding `[+0.200, +0.900, +0.400]`

↓ multiply by `Wq`

`Q_blue = [+0.310, +0.720, +0.650]`

K View

Each token embedding times `Wk` gives its advertised key vector.

`K_The`, `K_blue`, `K_car`, `K_hit`, `K_the`, `K_wall`

V View

Each token embedding times `Wv` gives value content to mix if attended.

`V_The`, `V_blue`, `V_car`, `V_hit`, `V_the`, `V_wall`

Raw Query-Key Scores (Not Attention Yet)

| Q \\ K | The | blue | car | hit | the | wall |
| --- | --- | --- | --- | --- | --- | --- |
| The | +0.212 | +0.191 | +0.276 | +0.366 | +0.190 | +0.297 |
| blue | +0.307 | +0.384 | +2.270 | +0.703 | +0.284 | +0.261 |
| car | +0.425 | +1.293 | +1.122 | +0.988 | +0.393 | +1.124 |
| hit | +0.400 | +0.503 | +0.739 | +0.846 | +0.363 | +0.798 |
| the | +0.193 | +0.184 | +0.265 | +0.339 | +0.173 | +0.283 |
| wall | +0.415 | +0.730 | +1.047 | +0.978 | +0.382 | +1.473 |

Step 1 · Selected Query Dot Keys

`blue` query · `The` key = `+0.307`

`blue` query · `blue` key = `+0.384`

`blue` query · `car` key = `+2.270`

`blue` query · `hit` key = `+0.703`

`blue` query · `the` key = `+0.284`

`blue` query · `wall` key = `+0.261`

Step 2 · Softmax To Attention Weights

`softmax([+0.307, +0.384, +2.270, +0.703, +0.284, +0.261])`

The `7.9%`

blue `8.6%`

car `56.4%`

hit `11.8%`

the `7.7%`

wall `7.6%`

Row sum: `7.9 + 8.6 + 56.4 + 11.8 + 7.7 + 7.6 = 100.0%`

Step 3 · Weighted Value Mix

Attention decides which value vectors get mixed into this token's next representation.

`output[1] = sum_i weights[1,i] * V[i]`

`head_output_blue = [+0.587, +0.970, +0.680]`

Highest attention target: `car` (56.4%).

Important takeaway

Multi-head attention gives the model several ways to route information at the same time. Grouped-query attention is a practical modern variant that makes this cheaper during inference.

Interpretation caveat

Attention heads are not little thought modules. They are learned projections that may specialize, overlap, or behave in ways that are hard to summarize cleanly.

## RoPE

Attention needs to know order. RoPE gives position information directly to the attention mechanism.

Attention compares tokens by content. But language also depends on order. "Dog bites man" and "man bites dog" contain the same words, but they do not mean the same thing.

Older transformer explanations often describe positional encodings as vectors added to token embeddings. That works, but many modern decoder-only models use something more integrated with attention: RoPE, or Rotary Positional Embeddings.

RoPE rotates parts of the query and key vectors based on their token positions. When attention compares a query with a key, the comparison should depend on both content and relative position.

Because RoPE modifies Q and K, it changes the attention scores. It does not directly rotate the value vectors, and it does not decide attention by itself. It changes which query/key pairs line up well.

Relative position through rotation

**Problem.** Attention sees tokens, but it also needs word order. `dog bites man` and `man bites dog` contain the same words, but positions change meaning.

**Naive idea.** One option is to add a position vector to each token. RoPE does something different.

**RoPE idea.** RoPE makes attention position-aware by rotating `Q` and `K` vectors according to token position before their dot product is computed. It does not rotate `V`.

Word Order Matters

`dog bites man` **is not the same as** `man bites dog`

Same tokens, different positions. RoPE makes `Q·K` sensitive to that position change.

Same Token, Different Position

Example sentence: `The small dog chased the ball.`

In this visual, clicking a word temporarily treats that word as relative index `0`. RoPE is relative in this sense: if you look from a different token, the position offsets change, so the rotations you compare change too.

Click any token to make it the reference frame. That token stays unrotated while all other tokens rotate relative to it.

Relative offset insight

The selected token `The` is the anchor. Other tokens rotate by their position difference to this anchor. In the dot product, the important angle is `theta_m - theta_n`, so compatibility depends on relative offset `m - n`.

In this toy pair, `dot(before rotation) = +0.734` and `dot(after RoPE rotation) = -0.157`. As positions change, relative angle changes, and the query-key dot product changes too.

Multi-frequency pairs

Real vectors have many dimension pairs. Different pairs rotate at different speeds: fast pairs capture nearby offsets, while slow pairs preserve longer-range position patterns.

Connect back to attention

RoPE changes the score matrix before softmax. It does not directly decide attention by itself; it changes which `Q/K` pairs are compatible at different relative positions. RoPE gives attention a position-dependent bias, and the model still has to learn how to use it.

Important takeaway

RoPE injects position into attention by rotating query and key vectors. It helps the model reason about relative position while computing attention.

Compatibility, not payload

RoPE affects compatibility, not payload. Q and K are rotated; V is not the main carrier of positional rotation here.

## Transformer Block

This is where the pieces become the repeated structure of the model.

A transformer is built by stacking blocks. Each block takes in a sequence of token vectors and returns a sequence of token vectors with the same basic shape. The rows still correspond to token positions. The width is still the model dimension.

What changes is the information inside those vectors.

A modern decoder block usually normalizes the input, applies attention so tokens can exchange information, adds the result back through a residual connection, normalizes again, applies a feed-forward network, and adds that result back too.

The residual stream is the running representation that moves through the network. Attention mixes information between positions. The feed-forward network transforms each position. Normalization helps keep values stable. Residual connections preserve a path for information and gradients through many layers.

Layer by layer, the initially context-free embeddings become rich context-aware representations.

One modern decoder block, end-to-end

This chapter combines what we learned into one full transformer block: normalization, multi-headed attention, residual paths, and a feed-forward network.

Let's look at an actual example of how all these elements are combined to build one Transformer block in a modern decoder-only model.

Click any block part to inspect its role, input/output dimensions, and jump back to the chapter where that part was introduced in detail.

<svg viewBox="0 0 420 760" role="img" aria-label="transformer block diagram" style="max-width: 100%;min-height: 300px;min-height: 360px;min-height: 300px;min-height: 360px;"><defs><marker id="arrow" markerWidth="10" markerHeight="10" refX="8" refY="5" orient="auto"><path d="M0,0 L10,5 L0,10 z" fill="rgba(71,85,105,0.8)"></path></marker></defs><g style="touch-action: manipulation;touch-action: manipulation;"><rect x="110" y="30" width="200" height="58" rx="12" fill="none" stroke="currentColor"></rect><text x="210" y="65" text-anchor="middle" fill="currentColor">Input X</text></g> <line x1="210" y1="88" x2="210" y2="122" marker-end="url(#arrow)" stroke="currentColor" stroke-opacity="0.2"></line><g style="touch-action: manipulation;touch-action: manipulation;"><rect x="125" y="122" width="170" height="56" rx="12" fill="none" stroke="currentColor"></rect><text x="210" y="156" text-anchor="middle" fill="currentColor">RMSNorm 1</text></g> <line x1="210" y1="178" x2="210" y2="214" marker-end="url(#arrow)" stroke="currentColor" stroke-opacity="0.2"></line><g style="touch-action: manipulation;touch-action: manipulation;"><rect x="85" y="214" width="250" height="86" rx="12" fill="none" stroke="currentColor"></rect><text x="210" y="248" text-anchor="middle" fill="currentColor">Causal GQA + RoPE</text> <text x="210" y="272" text-anchor="middle" fill="currentColor">Q/K/V -&gt; scores -&gt; mix</text></g> <line x1="210" y1="300" x2="210" y2="344" marker-end="url(#arrow)" stroke="currentColor" stroke-opacity="0.2"></line><g style="touch-action: manipulation;touch-action: manipulation;"><rect x="135" y="344" width="150" height="56" rx="12" fill="none" stroke="currentColor"></rect><text x="210" y="378" text-anchor="middle" fill="currentColor">+ Residual</text></g> <line x1="310" y1="59" x2="355" y2="59" stroke="currentColor" stroke-opacity="0.2"></line><line x1="355" y1="59" x2="355" y2="372" stroke="currentColor" stroke-opacity="0.2"></line><line x1="355" y1="372" x2="285" y2="372" marker-end="url(#arrow)" stroke="currentColor" stroke-opacity="0.2"></line><text x="360" y="224" fill="currentColor">skip</text> <line x1="210" y1="400" x2="210" y2="438" marker-end="url(#arrow)" stroke="currentColor" stroke-opacity="0.2"></line><g style="touch-action: manipulation;touch-action: manipulation;"><rect x="125" y="438" width="170" height="56" rx="12" fill="none" stroke="currentColor"></rect><text x="210" y="472" text-anchor="middle" fill="currentColor">RMSNorm 2</text></g> <line x1="210" y1="494" x2="210" y2="530" marker-end="url(#arrow)" stroke="currentColor" stroke-opacity="0.2"></line><g style="touch-action: manipulation;touch-action: manipulation;"><rect x="90" y="530" width="240" height="82" rx="12" fill="none" stroke="currentColor"></rect><text x="210" y="562" text-anchor="middle" fill="currentColor">SwiGLU MLP</text> <text x="210" y="586" text-anchor="middle" fill="currentColor">4096 -&gt; 14336 -&gt; 4096</text></g> <line x1="210" y1="612" x2="210" y2="654" marker-end="url(#arrow)" stroke="currentColor" stroke-opacity="0.2"></line><g style="touch-action: manipulation;touch-action: manipulation;"><rect x="135" y="654" width="150" height="56" rx="12" fill="none" stroke="currentColor"></rect><text x="210" y="688" text-anchor="middle" fill="currentColor">+ Residual</text></g> <line x1="285" y1="372" x2="355" y2="372" stroke="currentColor" stroke-opacity="0.2"></line><line x1="355" y1="372" x2="355" y2="682" stroke="currentColor" stroke-opacity="0.2"></line><line x1="355" y1="682" x2="285" y2="682" marker-end="url(#arrow)" stroke="currentColor" stroke-opacity="0.2"></line><text x="360" y="536" fill="currentColor">skip</text> <line x1="210" y1="710" x2="210" y2="742" marker-end="url(#arrow)" stroke="currentColor" stroke-opacity="0.2"></line><text x="222" y="748" fill="currentColor">Y</text></svg>

How This Scales In A Full Model

One block is rarely used alone. Decoder-only Transformers repeat this block many times before the final output projection over the vocabulary. In a Llama-8B-style setup, this is typically around `32` stacked blocks (layers).

<svg viewBox="0 0 900 140" role="img" aria-label="stacked transformer blocks pipeline" style="max-width: 100%;min-width: 560px;min-width: 560px;"><defs><marker id="arrowStack" markerWidth="10" markerHeight="10" refX="8" refY="5" orient="auto"><path d="M0,0 L10,5 L0,10 z" fill="rgba(71,85,105,0.8)"></path></marker></defs><rect x="20" y="45" width="130" height="50" rx="10" fill="none" stroke="currentColor"></rect><text x="85" y="75" text-anchor="middle" fill="currentColor">Input Tokens</text> <line x1="150" y1="70" x2="215" y2="70" marker-end="url(#arrowStack)" stroke="currentColor" stroke-opacity="0.2"></line><rect x="215" y="35" width="150" height="70" rx="10" fill="none" stroke="currentColor"></rect><text x="290" y="67" text-anchor="middle" fill="currentColor">Transformer</text> <text x="290" y="86" text-anchor="middle" fill="currentColor">Block 1</text> <line x1="365" y1="70" x2="422" y2="70" marker-end="url(#arrowStack)" stroke="currentColor" stroke-opacity="0.2"></line><rect x="422" y="35" width="150" height="70" rx="10" fill="none" stroke="currentColor"></rect><text x="497" y="67" text-anchor="middle" fill="currentColor">Transformer</text> <text x="497" y="86" text-anchor="middle" fill="currentColor">Block 2</text> <line x1="572" y1="70" x2="622" y2="70" marker-end="url(#arrowStack)" stroke="currentColor" stroke-opacity="0.2"></line><rect x="622" y="35" width="90" height="70" rx="10" fill="none" stroke="currentColor"></rect><text x="667" y="77" text-anchor="middle" fill="currentColor">...</text><line x1="712" y1="70" x2="770" y2="70" marker-end="url(#arrowStack)" stroke="currentColor" stroke-opacity="0.2"></line> <rect x="770" y="45" width="110" height="50" rx="10" fill="none" stroke="currentColor"></rect><text x="825" y="75" text-anchor="middle" fill="currentColor">Logits</text></svg>

Important takeaway

A transformer block keeps the sequence shape mostly stable while repeatedly changing what each token vector represents.

Modern decoder details

In Llama-like models, you also see choices such as RMSNorm, RoPE, SwiGLU-style feed-forward layers, causal attention, and grouped-query attention.

## Training Phases

Training is not magic. It is many small prediction errors turned into parameter updates.

From the outside, training often looks like one smooth curve going down. Reality is messier.

At the basic level, pretraining is simple to describe: show the model a lot of text and train it to predict the next token. It makes a prediction, measures the loss, computes gradients, and updates parameters.

Repeat that billions or trillions of times, and the model slowly becomes better at modeling text. But "loss goes down" is not the whole story.

Some patterns are learned early. Others appear much later. A model can improve on training data before it generalizes well. Sometimes better generalization arrives surprisingly late.

For large language models, training is also a scaling problem. Model size, dataset size, data quality, sequence length, optimizer settings, batch size, and compute budget all interact.

How behavior changes across training

Training is often staged, not perfectly smooth: fast fitting first, slower consolidation, and sometimes delayed generalization.

This chart is an illustrative curve, not a claim about one exact production run.

Toy training curve (loss vs optimization steps)

<svg viewBox="0 0 820 280" role="img" aria-label="training and validation loss phases" style="max-width: 100%;min-height: 180px;min-height: 180px;"><rect x="0" y="0" width="820" height="280" rx="10" fill="rgba(255,255,255,0.82)"></rect><line x1="40" y1="230" x2="760" y2="230" stroke="currentColor" stroke-opacity="0.2"></line><line x1="40" y1="40" x2="40" y2="230" stroke="currentColor" stroke-opacity="0.2"></line><rect x="40" y="40" width="252" height="190" fill="none" stroke="currentColor"></rect><rect x="292" y="40" width="252" height="190" fill="none" stroke="currentColor"></rect><rect x="544" y="40" width="216" height="190" fill="none" stroke="currentColor"></rect><path d="M40.0,54.4 L49.0,59.8 L58.0,65.8 L67.0,72.1 L76.0,78.2 L85.0,83.8 L94.0,88.7 L103.0,93.0 L112.0,96.9 L121.0,100.9 L130.0,105.5 L139.0,110.9 L148.0,117.0 L157.0,123.5 L166.0,130.0 L175.0,135.9 L184.0,140.6 L193.0,144.1 L202.0,146.3 L211.0,147.8 L220.0,149.0 L229.0,150.3 L238.0,152.1 L247.0,154.4 L256.0,157.1 L265.0,159.7 L274.0,161.8 L283.0,163.2 L292.0,164.0 L301.0,164.4 L310.0,164.8 L319.0,165.8 L328.0,167.8 L337.0,170.9" fill="none" stroke="currentColor"></path><path d="M40.0,48.4 L49.0,50.2 L58.0,52.4 L67.0,55.0 L76.0,57.9 L85.0,60.9 L94.0,63.9 L103.0,66.6 L112.0,69.1 L121.0,71.1 L130.0,72.7 L139.0,74.1 L148.0,75.3 L157.0,76.4 L166.0,77.6 L175.0,79.0 L184.0,80.6 L193.0,82.4 L202.0,84.3 L211.0,86.3 L220.0,88.0 L229.0,89.4 L238.0,90.3 L247.0,90.5 L256.0,90.1 L265.0,89.0 L274.0,87.4 L283.0,85.0 L292.0,82.6 L301.0,80.2 L310.0,78.2 L319.0,76.8 L328.0,76.0 L337.0,75.8" fill="none" stroke="currentColor"></path><circle cx="40" cy="50.38586942086394" r="2.1" fill="none" stroke="currentColor"></circle><circle cx="49" cy="53.686772174541346" r="2.1" fill="none" stroke="currentColor"></circle><circle cx="58" cy="61.36495516201492" r="2.1" fill="none" stroke="currentColor"></circle><circle cx="67" cy="72.4088214643809" r="2.1" fill="none" stroke="currentColor"></circle><circle cx="76" cy="83.41941829690566" r="2.1" fill="none" stroke="currentColor"></circle><circle r="2.1" cx="85" cy="90.78402240782913" fill="none" stroke="currentColor"></circle><circle r="2.1" cx="94" cy="92.52214135899561" fill="none" stroke="currentColor"></circle><circle r="2.1" cx="103" cy="91.31075918095542" fill="none" stroke="currentColor"></circle><circle r="2.1" cx="112" cy="91.71611375126804" fill="none" stroke="currentColor"></circle><circle r="2.1" cx="121" cy="96.52307581959488" fill="none" stroke="currentColor"></circle><circle r="2.1" cx="130" cy="104.7891648315033" fill="none" stroke="currentColor"></circle><circle r="2.1" cx="139" cy="113.16138790266388" fill="none" stroke="currentColor"></circle><circle r="2.1" cx="148" cy="119.1024193680506" fill="none" stroke="currentColor"></circle><circle r="2.1" cx="157" cy="123.05215377942264" fill="none" stroke="currentColor"></circle><circle r="2.1" cx="166" cy="127.616993087385" fill="none" stroke="currentColor"></circle><circle r="2.1" cx="175" cy="134.64012351689558" fill="none" stroke="currentColor"></circle><circle r="2.1" cx="184" cy="142.96083110297855" fill="none" stroke="currentColor"></circle><circle r="2.1" cx="193" cy="149.05383251018975" fill="none" stroke="currentColor"></circle><circle r="2.1" cx="202" cy="150.1020934217238" fill="none" stroke="currentColor"></circle><circle r="2.1" cx="211" cy="146.77508852967728" fill="none" stroke="currentColor"></circle><circle r="2.1" cx="220" cy="143.1326834035915" fill="none" stroke="currentColor"></circle><circle r="2.1" cx="229" cy="143.56089506160106" fill="none" stroke="currentColor"></circle><circle r="2.1" cx="238.00000000000003" cy="149.27979512786487" fill="none" stroke="currentColor"></circle><circle r="2.1" cx="246.99999999999997" cy="157.4008666564551" fill="none" stroke="currentColor"></circle><circle r="2.1" cx="256" cy="163.3408633069452" fill="none" stroke="currentColor"></circle><circle r="2.1" cx="265" cy="164.51927879914356" fill="none" stroke="currentColor"></circle><circle r="2.1" cx="274" cy="162.20418253401215" fill="none" stroke="currentColor"></circle><circle r="2.1" cx="283" cy="160.04459855190697" fill="none" stroke="currentColor"></circle><circle r="2.1" cx="292" cy="160.73750310767798" fill="none" stroke="currentColor"></circle><circle r="2.1" cx="301" cy="163.84614226817553" fill="none" stroke="currentColor"></circle><circle r="2.1" cx="310" cy="166.64946557985604" fill="none" stroke="currentColor"></circle><circle r="2.1" cx="319" cy="167.1131356742896" fill="none" stroke="currentColor"></circle><circle r="2.1" cx="328" cy="166.14829956944226" fill="none" stroke="currentColor"></circle><circle r="2.1" cx="337" cy="166.99179924761756" fill="none" stroke="currentColor"></circle><line x1="337" y1="40" x2="337" y2="230" stroke="currentColor" stroke-opacity="0.2"></line><circle cx="337" cy="170.85197720226574" r="4.5" fill="none" stroke="currentColor"></circle><circle cx="337" cy="75.80695110681603" r="4.5" fill="none" stroke="currentColor"></circle><text x="760" y="252" fill="currentColor">steps</text> <text x="12" y="46" fill="currentColor">loss</text></svg>

Train loss Validation loss

Auto-detected phase summary

### Phase 2: Generalization plateau

**Train:** Training loss keeps dropping.

**Validation:** Validation barely moves.

Looks like overfitting, but training continues.

What is being learned in this phase

In large-scale pre-training, the model is mostly learning broad structure: world knowledge, language regularities, code patterns, and reasoning traces from text continuation.

This is why early improvements can look mostly statistical, while later improvements reflect better internal representations. The model is not yet being optimized for assistant behavior such as refusal style or helpful tone.

Where alignment and safety enter

Alignment behavior is primarily shaped after pre-training. Post-training adds objectives such as following instructions, refusing unsafe requests, formatting answers clearly, asking clarifying questions, and staying helpful.

So this chapter is mostly about capability learning dynamics; the next chapter focuses on behavior shaping.

Important takeaway

Pretraining teaches broad capability through next-token prediction. The loss curve is a useful signal, but it is only one view of what the model is learning.

Loss is not the whole story

A lower loss generally means better prediction. It does not automatically mean better reasoning, better honesty, or better assistant behavior.

## Post-Training

Pretraining gives the model capability. Post-training shapes how that capability behaves.

A pretrained language model has learned a huge amount about text. It can continue patterns, imitate styles, answer some questions, write code, and represent many facts and concepts.

But that does not automatically make it a good assistant. A base model is trained to predict likely next tokens. If you ask it a question, it might answer, but it might also continue the prompt, imitate a webpage, produce messy completions, or behave inconsistently.

Post-training teaches the model how we want it to respond. Instruction tuning shows the model examples of prompts and good task-oriented answers. Preference tuning compares possible answers and trains the model toward the ones people prefer: clearer, safer, more useful, better formatted, less rambling.

Different systems use different methods: supervised fine-tuning, RLHF, DPO, constitutional approaches, and many variations. The details differ, but the high-level goal is the same.

From capability to assistant behavior

Pre-training creates broad capability; post-training shapes behavior. The same underlying model can respond very differently depending on which training stage it has gone through.

In practice, we can think of this as: pre-training learns *knowledge and patterns*, while post-training learns *assistant behavior*.

Capability vs Behavior

Pre-training

world knowledge, language, code, reasoning patterns

Post-training

follows instructions, refuses unsafe requests, formats answers, asks clarifying questions, uses a helpful tone

Three-stage pipeline

→ →

### 1\. Base model (after pre-training)

**Objective:** Predict next token over large text/code corpora.

**Signal:** Web, books, code, and other broad unlabeled text.

Key message: pre-training gives broad latent capability, while instruction and preference tuning mostly steer behavior, format, and alignment.

Alignment and safety are not one switch; they are reinforced through multiple post-training signals, evaluations, and policy constraints.

Example prompt:

`Explain why the sky is blue.`

`Sunlight passes through the atmosphere and shorter blue wavelengths scatter more than longer wavelengths. This process is called Rayleigh scattering and makes the sky appear blue from most viewing angles.`

Not every model is trained with RLHF-style preference optimization. Some models stop at supervised instruction tuning, while others add direct preference objectives.

The goal is to make outputs more helpful, safer, and better aligned with human expectations when multiple answers are all technically plausible.

In short: pre-training teaches what the model *can* say, while preference tuning helps steer what it *should* say in assistant contexts.

How RLHF-Style Preference Tuning Works

Step 1 · Candidate answers

For one prompt, generate multiple candidate responses from the current model.

Step 2 · Pairwise ranking

Human raters (or policy-based systems) choose which answer is better in pairs. Example: `A > B` for helpfulness and safety.

Step 3 · Preference objective

Train a preference signal from those comparisons, then optimize the model so preferred responses become more likely.

Mini pairwise example

**Prompt:** `How can I recover a deleted file?`

**Answer A:** Gives clear, cautious, platform-specific recovery steps.

**Answer B:** Vague and omits safety checks.

**Ranking:** `A > B` (more useful and safer).

Important takeaway

Pretraining mostly teaches what the model can do. Post-training strongly influences how, when, and in what style the model does it.

Assistant behavior

A post-trained assistant is not just a base model with more facts. It is a base model whose behavior has been shaped toward following instructions and user preferences.

## Context and KV Cache

Generating text one token at a time would be painfully wasteful without caching.

Decoder-only language models generate text autoregressively: one token at a time. Each new token depends on the tokens before it. So after generating a token, the model appends it to the context and runs another step to predict the next one.

Naively, this would repeat a lot of work. If the prompt has already been processed, why recompute the same keys and values for all earlier tokens again and again?

The KV cache solves that. During attention, the model computes key and value vectors for each token. These are exactly the things future tokens need when they attend back to previous context. So the model stores them.

During generation, each new token only needs to compute its own new keys and values and attend to the cached previous ones. The cache saves compute, but it uses memory. The longer the context, the larger the KV cache becomes.

It helps to separate two phases: prefill processes the prompt and builds the initial cache; decode generates new tokens one by one while reusing the cache.

Compute-memory tradeoff during inference

Decoding is autoregressive: each new token is generated after all previous tokens. KV cache changes the cost by reusing key/value tensors from earlier steps instead of recomputing them every time.

Decode setup

Autoregressive decode loop

Compute reduction from caching

**62.8x** less repeated attention work in this toy estimate

Without cache

At each step, recompute attention keys/values for the full seen sequence.

Relative compute: `668,619`

Memory behavior: lower KV storage, higher repeated compute.

With cache

Reuse stored K/V from previous tokens; compute only for the new token each step.

Relative compute: `10,644`

Estimated KV memory: `34.1 MB` for `10,644` seen tokens.

Without cache

668,619

With cache

10,644

KV memory

34.1 MB

These values are illustrative relative estimates. Exact memory and speed depend on architecture, precision, head counts, and runtime implementation.

Important takeaway

The KV cache is not a summary of the conversation. It is stored attention data that avoids recomputing previous keys and values during generation.

Speed vs memory

KV cache speeds up repeated attention over previous tokens, but it increases memory use as the context grows.

## Quantization

Big models are often limited by memory. Quantization makes them smaller by storing numbers with fewer bits.

Neural networks are mostly numbers. A large language model contains billions of weights, and during inference it also creates intermediate activations and KV-cache tensors. Storing all of that at high precision takes a lot of memory.

Quantization reduces that memory pressure by representing numbers with fewer bits. Instead of storing a weight as a 16-bit or 32-bit floating-point value, we may store an approximation using 8 bits, 4 bits, or another compact format.

The basic trade-off is simple: less precision -> less memory -> often faster or cheaper inference -> some approximation error.

But "4-bit" or "8-bit" is not the whole story. Different quantization methods make different choices. Some quantize only weights. Some also quantize activations. Some protect outlier channels. Some target the KV cache.

This is why two 4-bit models can behave differently. For local inference, quantization can be the difference between a model that does not fit in memory and a model that runs comfortably.

Bit-width vs quality and memory

Quantization stores model weights with fewer bits. The goal is to reduce memory and make local inference more practical, while accepting a small quality trade-off.

Quantization selector

**FP32:** Maximum precision, largest memory footprint.

**Bits per value:** `32` bits

Stored directly as floating-point values.

Weight Matrix (FP32)

Quantized values at selected precision

| +0.18371234 | \-1.20491236 | +0.00712091 | +2.91823411 | \-0.55291337 |
| --- | --- | --- | --- | --- |
| +0.44204588 | \-0.99123817 | +1.33100214 | \-0.22345518 | +0.07620133 |
| +3.12019843 | \-2.01444274 | +0.55193302 | \-0.04721129 | +1.77231055 |
| \-0.80911403 | +2.20133044 | \-1.48320182 | +0.19441726 | \-0.00990127 |
| +0.61544281 | \-0.33611945 | +1.00993218 | \-2.44211706 | +0.43120572 |

**Unique values in this 5×5 matrix:** `25`

**Value range:** `-2.44211706` to `+3.12019843`

8B Model Size (Guestimate)

FP32 baseline

32.0 GB

FP32 estimate

32.0 GB

Saved

0.0 GB

Reduction

0%

Tradeoff: lower precision can slightly reduce accuracy or response quality, but it is often the key enabler for running strong models locally on consumer hardware.

Why numbers still look like floats in INT8/INT4: the model stores compact integers, then runtime kernels dequantize them back to approximate floating-point values during compute.

This chapter uses simplified estimates and symmetric quantization for intuition; real runtimes also include metadata, activation precision choices, and kernel-specific optimizations.

Important takeaway

Quantization is controlled approximation. It reduces memory and often improves practical inference, but the quality depends on what is quantized and how.

A family of trade-offs

Quantization is not one technique. It is a family of compression and inference trade-offs.