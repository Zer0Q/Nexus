---
title: "Here is how I moved my entire AI Workflow Offline: Obsidian + LM Studio + Local LLM Plugins"
source: "https://x.com/KanikaBK/status/2059177736648987072"
author:
  - "[[@KanikaBK]]"
published: 2026-05-26
created: 2026-06-04
description: "A complete guide to moving your AI workflow offline using Obsidian, LM Studio, and local LLM plugins. Covers Smart Connections, BMO Chatbot,..."
tags:
  - "clippings"
summary:
---
![Imatge](https://pbs.twimg.com/media/HIdCGYlaMAAM27M?format=jpg&name=large)

**A complete guide to moving your AI workflow offline using Obsidian, LM Studio, and local LLM plugins. Covers Smart Connections, BMO Chatbot, Mini-RAG, cloud vs local comparison, and a one-hour setup guide.**

There was one moment that changed everything for me.

I had just pasted a confidential client brief into Claude to help me rewrite it. It took three seconds to get a great result. Then I sat there and thought about where that brief just went.

A server. Somewhere. Trained on.

That was the day I decided to move my entire AI workflow offline.

This is the full story of how I did it, what I use, how it works, and why local AI has become more capable than most people realize.

## The problem with cloud AI (That Nobody Talks About)

Cloud AI tools are extraordinary. Claude, ChatGPT, Gemini - they are powerful, fast, and constantly improving. But every prompt you send them is a data transfer. Your notes, your ideas, your client work, your research - all of it leaves your device the moment you hit send.

For most casual use, that is fine. But for anyone doing serious knowledge work - research, writing, consulting, legal, medical, financial, or just deeply personal thinking - the privacy tradeoff starts to feel uncomfortable.

The question is not whether AI companies are trustworthy. **The question is whether your most important thinking should live on someone else's server at all.**

For me, the answer became no.

## The Stack: Three tools, One private system

Moving offline does not mean downgrading. It means choosing the right tools. My offline AI workflow runs on three pieces:

- **Obsidian:** the knowledge base and interface layer.
- **LM Studio:** the local model runner that replaces the cloud API.
- **Local LLM Plugins:** the bridge that connects the two.

Each one does a specific job. Together, they replicate everything I was doing with cloud AI - without a single byte leaving my device.

## PART 1: LM Studio - Your Local AI Engine

LM Studio is a free desktop application that lets you download and run large language models completely offline on your own Mac, Windows, or Linux machine. It has a clean interface, supports most major open-source models, and runs a local server that other apps can connect to exactly like they would connect to OpenAI or Anthropic's API.

**How to set it up:**

1. Download LM Studio from [lmstudio.ai](http://lmstudio.ai/) and install it.
2. Open the app and go to the **Discover** tab.
3. Search for a model. Good starting points are: **Mistral 7B** - fast, capable, runs on most laptops. **Llama 3 8B** - excellent all-round model for notes and writing. **Phi-3 Mini** - extremely lightweight, great for older machines. **DeepSeek Coder** - best for code-related tasks.
4. Download your chosen model (files range from 4–8GB).
5. Go to the **Local Server** tab and click **Start Server**.

LM Studio now runs a local API at http://localhost:1234 - identical in format to the OpenAI API. Any tool that can connect to OpenAI can now connect to your local model instead.

**Hardware reality check:**

- MacBook with Apple Silicon (M1/M2/M3) - runs 7B–13B models smoothly.
- Windows or Linux with 16GB RAM - runs 7B models well.
- Windows or Linux with 32GB RAM + GPU - runs 13B–34B models comfortably.

**You do not need a $5,000 machine. A modern laptop runs this well.**

## PART 2: Obsidian setup for local AI

Obsidian is where your knowledge lives. Now this is my 1000th time same dialouge.

The goal is to turn it into an interface that lets you chat with your vault, summarize notes, generate content, and ask questions - all powered by your local LM Studio model.

**Install these plugins from Settings → Community Plugins:**

## Plugin 1: Smart Connections

This is the most important plugin in the stack. Smart Connections creates embeddings of every note in your vault and lets you ask questions across your entire knowledge base using a chat interface inside Obsidian.

In the plugin settings:

- Set **API provider** to Local.
- Set the **API base URL** to **http://localhost:1234/v1.**
- Set **Model** to the name of whatever model you have running in LM Studio.

Once configured, open the Smart Connections panel and type any question. It searches your vault, finds the most relevant notes, and generates a grounded answer using only your own content.

This is the "chat with your vault" feature - and it is entirely on-device.

## Plugin 2: BMO Chatbot (Private AI Chat)

BMO Chatbot adds a full chat interface inside Obsidian that connects directly to your local LM Studio server. It feels like Claude or ChatGPT, but everything runs locally.

In settings:

- Set **API URL** to **http://localhost:1234/v1.**
- Set **Model** to your active LM Studio model.
- Disable any cloud fallback options.

Use it to: draft notes, rewrite paragraphs, generate ideas, summarize content, or ask questions - all without leaving Obsidian, offline.

## Plugin 3: Copilot

Copilot adds an inline AI assistant that lets you select text and ask the model to summarize, expand, rewrite, or improve it. It also supports slash commands inside notes.

Connect it to LM Studio the same way - point it to **http://localhost:1234/v1** and set your model name.

## PART 3: Mini-RAG - Chatting With Your Entire Vault

RAG stands for Retrieval-Augmented Generation. It is the technique that lets an AI search through a large collection of documents and answer questions grounded in that specific content - rather than guessing from general training data.

Mini-RAG is a lightweight implementation of this that runs entirely on your device. Combined with Smart Connections, it gives you a system where you can ask:

- "What did I learn about productivity last month?"
- "Summarize everything I have saved about AI agents."
- "What projects am I currently blocking?"

And the model answers using only your actual vault notes — not the internet, not its training data.

**How the pipeline works:**

1. Smart Connections reads every note in your vault and creates local embeddings (a mathematical representation of each note's meaning).
2. When you ask a question, it finds the most semantically similar notes.
3. It passes those notes as context to your local LM Studio model.
4. The model generates an answer grounded in your actual content.
5. Everything happens on your machine. Nothing leaves.

![Imatge](https://pbs.twimg.com/media/HIc-IVXagAAZBG7?format=jpg&name=large)

Cloud vs Local: The Honest Comparison

The honest truth is that frontier cloud models like Claude 3.7 and GPT-5 are still more capable than the best open-source local models for complex reasoning and creative tasks. If you are writing a book or doing advanced research, cloud AI is still stronger.

## What My Daily Workflow Looks Like Now

My offline AI workflow runs in three modes:

**Mode 1: Deep work (fully offline)** LM Studio running Llama 3 8B. Obsidian open with Smart Connections. I ask questions across my vault, generate drafts, and process notes — all on-device. No internet needed, no data leaving my machine.

**Mode 2: Research and writing (hybrid)** Obsidian for knowledge base. Cloud AI (Claude via API) for heavy reasoning, complex rewrites, and research synthesis. Sensitive context stays local. General questions go to cloud.

**Mode 3: Confidential work (strict local)** Everything local. LM Studio only. Vault stays private. This mode for client work, financial notes, personal research.

## Why this matters more than it used to

A year ago, running AI locally was a hobbyist project. The models were weak, the setup was painful, and the results were disappointing.

That has changed. **Models like Llama 3, Mistral, and DeepSeek have closed the gap significantly. LM Studio has made the setup accessible to anyone who can install an app. And Obsidian's plugin ecosystem has made the integration seamless.**

You do not have to choose between powerful AI and private AI anymore. With this stack, you can have both.

## Getting Started in One Hour

If you want to try this today, here is the minimum viable setup:

1. Download and install LM Studio → download Llama 3 8B → start local server.
2. Open Obsidian → install Smart Connections plugin → point it to **http://localhost:1234/v1.**
3. Open the Smart Connections chat panel → ask a question about your vault.

**That is it. You now have a private, offline AI that knows everything in your Obsidian vault and answers questions grounded in your own content.**

Everything else in this article is an upgrade on top of that foundation.

**Understand this thing, the cloud is powerful. But your most important thinking deserves to stay on your machine.**

Hope you like the article.

I'm Kanika ([@KanikaBK](https://x.com/@KanikaBK)), specializing in AI tools, emerging trends, and niche applications.

**Follow for in-depth analyses, strategic insights, and professional updates to elevate your AI knowledge.**