---
title: "A Visual Guide to LLMs (Part 1)"
source: "https://x.com/_rohit_tiwari_/status/2013580072788336643"
author:
  - "[[@_rohit_tiwari_]]"
published: 2026-01-20
created: 2026-06-08
description: "In this two part series, we will go through the core components of Large Language Model (LLM) architecture step by step, making it easy to u..."
tags:
  - "clippings"
summary:
---
![Imatge](https://pbs.twimg.com/media/G_GqwXNXgAA5DS8?format=jpg&name=large)

In this two part series, we will go through the core components of Large Language Model (LLM) architecture step by step, making it easy to understand, **even if you are new to AI.**

**Series Roadmap**

> **Part 1**: This part will show how written language is split into tokens and then turned into input embedding vectors that a model can work with. It explains tokenization, token embeddings, and positional embeddings.

> **Part 2**: This part will show how those input embedding vectors move through the transformer block to produce output. It covers self attention, multi head attention mechanisms, feedforward neural networks, how the next token is chosen, and how training slowly improves the model over time.

First of all, let us have a bird’s eye view of the Generative Pretrained Transformer (GPT) like LLM architecture.

![Vídeo incrustat](https://pbs.twimg.com/tweet_video_thumb/G_GrATxXQAAyqOX?format=jpg&name=large)

GIF

LLMs work by predicting one word or token at a time. LLMs generate text iteratively. Each predicted token is appended to the previous input to form the context for the next prediction.

For example: “Every moment is a beginning”

![Imatge](https://pbs.twimg.com/media/G_GrJD-WYAAolqt?format=png&name=large)

We can broadly divide LLM architecture into three parts:

1. Input Pipeline
2. Transformer Block
3. Output Pipeline

In Part 1, let’s deep dive into the input pipeline.

**The Fundamental Challenge: Machines Don’t Speak Human Language**

Imagine you are trying to teach a baby a new language. You can show them objects, make sounds, and use gestures. But a machine doesn’t have eyes or ears in the same way. It only understands numbers. So, the first big challenge for any LLM is translating human language (sentences or paragraphs) into a numerical format.

This translation happens in two main steps: Tokenization and Embedding.

**Step 1: Tokenization – Breaking Down the Language**

Tokenization is the process of splitting a text into smaller units called tokens. These tokens are the fundamental building blocks an LLM works with.

Tokenization algorithms can be broadly divided into three main categories.

1. Word Based Tokenization This is the simplest approach. Text is split using spaces and punctuation. **Example**: “Every moment is a beginning” **Tokens**: \[“Every,” “moment”, “is”, “a”, “beginning”\]
2. Subword Based Tokenization Instead of splitting only on spaces, the tokenizer learns common word fragments from data. **Example**: “Every moment is a beginning” **Tokens**: \[“Every,” “mo”, “ment”, “is”, “a”, “begin”, “ning”\]
3. Character Based Tokenization In character based tokenization, each character becomes a token. **Example**: “Every moment is a beginning” **Tokens**: \[“E”, “v”, “e”, “r”, “y,” “m”, “o”,…..,“n”, “i”, “n”, “g”\]

**Why Subwords?**

Subword based methods sit between word and character approaches. Most modern LLMs rely on subword based tokenization. You might wonder why we don’t just use whole words. The main reason is handling unknown words**:** What if you type a word the LLM has never seen before? If it only knew whole words, it would get stuck. Subwords solve this! By breaking down words into common prefixes, suffixes, and roots, the model can understand new or complex words by piecing together familiar subwords. For example, “unbelievable” might become “un,” “believe,” “able.”

One popular algorithm for subword tokenization is called Byte Pair Encoding (BPE). It works by finding the most common pairs of characters or subwords and merging them into new, longer subwords until a set vocabulary size is reached.

Here’s a simple visual showing tokenization:

![Vídeo incrustat](https://pbs.twimg.com/tweet_video_thumb/G_GrYXsbgAAKZyd?format=jpg&name=large)

GIF

**Input Sentence:** “Every moment is a beginning”

**Tokens:** \[“Every”, “moment”, “is”, “a”, “beginning”\]

After tokenization, each unique token is assigned a unique numerical ID.

![Imatge](https://pbs.twimg.com/media/G_GrchGWsAAl_-S?format=png&name=large)

This turns our sequence of token into a sequence of numbers.

\[“Every”, “moment”, “is”, “a”, “beginning”\] → \[15745, 4205, 382, 261, 10526\]

If you want to try a tokenizer yourself, you can use the [tiktokenizer](https://tiktokenizer.vercel.app/) tool.

![Vídeo incrustat](https://pbs.twimg.com/tweet_video_thumb/G_GrkKZXcAA9Mo-?format=jpg&name=large)

GIF

Depending on the LLM, special tokens may be added. In the example above, these include |im\_start|, |im\_sep|, and |im\_end|. They help the model identify where messages start, where parts are separated, and where messages end.

**Step 2: Embeddings – Giving Meaning to Numbers**

Now we have a list of numbers, but these numbers alone don’t carry any meaning. The ID “15745” for “Every” doesn’t tell the machine that “Every” is a determiner used to describe a noun. This is where embeddings help.

Embeddings are essentially numerical representations (vectors) of tokens. Think of them as a detailed “profile” for each token, capturing its meaning and relationship to other tokens.

Imagine a simple quiz for each token with hundreds of questions:

- “Are you a noun?” (Yes/No)
- “Are you typically associated with positive or negative emotions?” (Positive/Negative/Neutral)
- “Do you refer to a person, place, or thing?” (Person/Place/Thing)
- “How formal are you?” (Formal/Informal)

An LLM’s embedding for a token answers not just a few, but hundreds of these implicit questions, creating a long list of numbers (a vector) that describes its characteristics. For example, in GPT-3, the embedding size is 12,288 dimensions!

Here’s why embeddings are so powerful:

1. **Semantic Similarity:** Tokens with similar meanings will have similar embedding vectors. “King” and “Queen” will be numerically close.
2. **Contextual Relationships:** The embedding can even capture relationships. If you subtract the embedding of “Man” from “King” and add “Woman,” you often get a vector very close to the embedding of “Queen”.

![Vídeo incrustat](https://pbs.twimg.com/tweet_video_thumb/G_GrsjHWMAA3ctm?format=jpg&name=large)

GIF

**Positional Embeddings: Why Token Order Matters**

Imagine the sentences:

1. The dog jumps on the cat.
2. The cat jumps on the dog.

The words are the same, but the meaning is entirely different because their positions are different. Our numerical token IDs and token embeddings, by themselves, don’t tell the LLM anything about the order of words.

This is solved with Positional Embeddings.

Positional embeddings are another list of numbers (a vector) added to the token embeddings. These numbers are carefully designed to tell the LLM about the absolute or relative position of each token in the input sequence.

Think of it like adding a unique “seat number” to each token. So, “The” at the beginning of a sentence gets a different positional embedding than “the” in the middle, even though their token embeddings are identical.

Complete Input Pipeline

**Input Sentence:** “Every moment is a beginning”

**Process:**

1. **Tokenization**: \[“Every”, “moment”, “is”, “a”, “beginning”\]
2. **Token IDs:** {”Every”: 15745, “moment”: 4205, “is”: 382, “a”: 261, “beginning”: 10526}
3. **Token Embeddings (output dimension=3):** “15745”: \[-0.5880, 0.3486, 0.6603\] “4205”: \[-0.2196, -0.3792, 0.7671\] “382”: \[-1.1925, 0.6984, -1.4097\] “261”: \[ 0.1794, 1.8951, 1.3689\] “10526”: \[-1.6033, -1.3250, 0.1784\]
4. **Positional Embeddings (output dimension=3):** Position 1: \[-0.9178, 0.9045, -2.0975\] Position 2: \[1.1558, -1.2157, 0.1295\] Position 3: \[ 1.0937, 0.2066, 3.1815\] Position 4: \[ 0.0967, 1.4086, 0.1915\] Position 5: \[ -0.1562, 0.2446, 4.0124\]
5. **Final Input Vector (Sum of Embeddings + Positional Embeddings):** “15745” (position 1): \[-0.5880, 0.3486, 0.6603\] + \[-0.9178, 0.9045, -2.0975\] “4205” (position 2): \[-0.2196, -0.3792, 0.7671\] + \[1.1558, -1.2157, 0.1295\] “382” (position 3): \[-1.1925, 0.6984, -1.4097\] + \[ 1.0937, 0.2066, 3.1815\] “261” (position 4): \[ 0.1794, 1.8951, 1.3689\] + \[ 0.0967, 1.4086, 0.1915\] “10526” (position 5): \[-1.6033, -1.3250, 0.1784\] + \[ -0.1562, 0.2446, 4.0124\]

Each final input vector now has a unique numerical signature that encodes both its meaning and its location in the sentence.

![Vídeo incrustat](https://pbs.twimg.com/tweet_video_thumb/G_GrxrCXIAANCOV?format=jpg&name=large)

GIF

**What’s Next?**

Now that we understand how an LLM ingests your words, we’re ready for **A Visual Guide to LLMs** (**Part 2): Inside the Transformer Architecture** (releasing soon) we’ll open up the transformer block and explore the self attention and multi head attention mechanisms that allow LLMs to understand context, generate coherent text, and perform complex reasoning.

**Star and Clone the GitHub Repository!**

Build a ChatGPT like LLM from scratch in PyTorch, explained step by step.

**Code** → [https://github.com/analyticalrohit/llms-from-scratch](https://github.com/analyticalrohit/llms-from-scratch)