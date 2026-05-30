---
title: "Claude Code 104: Building Your AI-Powered Research Management System"
source: "https://x.com/MushtaqBilalPhD/status/2058888916858544472"
author:
  - "[[@MushtaqBilalPhD]]"
published: 2026-05-25
created: 2026-05-31
description: "This is the fourth installment in a series of tutorials that I am doing on Claude Code for non-technical academic researchers. You can read ..."
tags:
  - "clippings"
---
![Imatge](https://pbs.twimg.com/media/HJKkVyeXAAAHxFW?format=jpg&name=large)

This is the fourth installment in a series of tutorials that I am doing on Claude Code for non-technical academic researchers. You can read the first three tutorials by clicking the following links – [101](https://x.com/MushtaqBilalPhD/status/2052338632426467550), [102](https://x.com/MushtaqBilalPhD/status/2053829787219595725), [103](https://x.com/MushtaqBilalPhD/status/2057033643973865585).

All these tutorials are standalone, which is to say that you don’t need to read the 101 tutorial to understand 102, although reading them in chronological order will make things easier for you.

I am writing these tutorials in simple and accessible language. You don’t need any coding or technical skills to understand these tutorials or use Claude Code.

# 1: Building Your Personal Research Management System

As researchers, we interact with all sorts of documents from PDFs to Word files to webpages to datasets, and so on. Most of us keep these documents in a folder or several folders on our computers.

The challenge here is not to gather these documents or even to read them. The real challenge is to build relevant connections across these materials. For example, which are the papers that support or refute my argument and how do I find the relevant data to strengthen my argument. This is not a linear process and often we have to go back to papers we have already read or to revise our argument because new evidence recently came to light.

Building an AI-powered research management system helps you find relevant connections across a vast corpus very easy and convenient. You will need to set up your research management system only once, and after that it will automate considerable amount of academic labor for you.

## Understanding Your Research Management System

Your personal research management system will use two folders: a raw folder and a wiki folder. You’d want to put these two folders in your main project folder. For the purpose of this tutorial, we will name our main folder “MyWiki.”

As the names suggest, the raw folder will contain any and everything you collect from PDFs to webpages to datasets. Think of it as the inbox of your system. The wiki folder is where we will use Claude Code to find relevant connected between materials in your raw folder and to extract synthesized notes.

A wiki is a collection of notes linked bidirectionally that forms a connected web of knowledge. Wikipedia is the most well-known example of this organizing scheme. It has millions of articles, each focused on one specific topic, but linked to the other articles so you can jump from one to the next and come back to the original article.

Think of this research management system as if you are building a Wikipedia-like app but based on your research materials.

# Part 2: Installing Obsidian and Getting Started

To set up your personal research management system, you will need an app called Obsidian in addition to Claude Code. Obsidian is a free desktop app used to take and organize notes.

![Vídeo incrustat](https://pbs.twimg.com/amplify_video_thumb/2058886215550517248/img/JMXvQoQ8ZEoYzHLJ?format=jpg&name=large)

0:02

To use Obsidian, you will need to download it from obsidian.md and install it just like you would install an app like Zoom or Zotero. Obsidian lets you create bidirectional links between concepts and ideas, which over time evolve into your personal navigable web of knowledge rather than individual papers and notes.

## Creating an Obsidian Vault

Once you have installed Obsidian on your computer, it will prompt you to create a “vault.” A vault is nothing but a folder on your computer. Create a folder called “MyWiki” and save it to your documents.

![Vídeo incrustat](https://pbs.twimg.com/amplify_video_thumb/2058886568924827648/img/aEUkJanfauc3nlyJ?format=jpg&name=large)

0:11

Within MyWiki, create two subfolders: raw and wiki.

![Vídeo incrustat](https://pbs.twimg.com/amplify_video_thumb/2058886680220778496/img/yfZjLP2NbG7JBAuZ?format=jpg&name=large)

0:11

Anything you create in your Obsidian vault will also appear in your MyWiki folder on your computer and vice versa. Think of Obsidian as a better graphic interface for your folder.

![Vídeo incrustat](https://pbs.twimg.com/amplify_video_thumb/2058886904225972224/img/AlL3sthvHVpYHZEG?format=jpg&name=large)

0:08

## Part 3: Filling Up Your raw Folder

The simplest way to fill your raw folder is to drop a bunch of documents (PDFs, Word files) into it. Go ahead and add 20-odd PDFs relevant to your current project in the raw folder.

![Vídeo incrustat](https://pbs.twimg.com/amplify_video_thumb/2058887025860734977/img/nSGRVsSmYYm4SpXZ?format=jpg&name=large)

0:10

You can add PDFs to the folder, but this way, you won’t be able to save webpages or at least you won't be able to save them conveniently. For that we will need a browser plugin called Obsidian Web Clipper.

## Obsidian Web Clipper

Run a Google search for “Obsidian Web Clipper,” and click the first link. Add the Clipper to your browser and then pin it so it’s easily accessible.

![Vídeo incrustat](https://pbs.twimg.com/amplify_video_thumb/2058887184782856192/img/bK8_CGUgFvk5umQe?format=jpg&name=large)

0:09

The Clipper takes any webpage and saves it as a text file (in markdown) to your computer. But you don’t want the Clipper to save relevant webpages randomly on your computer. You want it to save everything in your raw folder. You will need to instruction the Clipper to save everything in the raw folder.

Open the Clipper and click the gear icon to open Settings. Scroll down and click “Reset default template.” Look for “Note location” in the template. Delete “Clippings” and instead type “raw.”

![Vídeo incrustat](https://pbs.twimg.com/amplify_video_thumb/2058887287883079680/img/w7kmkZA3ecj_zbvd?format=jpg&name=large)

0:19

Now every webpage you clip will be saved in your raw folder automatically. Open a webpage and use the Clipper to see if it has been set up correctly.

Now clip 20-odd webpages relevant to your project using the Clipper.

![Vídeo incrustat](https://pbs.twimg.com/amplify_video_thumb/2058887424478945280/img/ZWDtOS8RWhO77K9G?format=jpg&name=large)

0:12

# Part 4: Setting Up Your Instructions: AGENTS md and Index md

To make Claude Code organize materials in your raw folder, you will need two different sets of instructions: AGENTS.md and Index.md

- AGENTS.md is a set of instructions that tells Claude Code how you want your research system organized.
- Index.md is, as the name shows, the table of contents for your wiki.

To create an AGENTS.md file, open the “MyWiki” folder in Claude Code. Copy the following template, fill in the relevant details, and ask it to create an AGENTS.md file for you:

```text
I am setting up a personal research knowledge system using Obsidian and Claude Code.
Here is how it works: I have a folder (an Obsidian vault) with two subfolders. A "raw" folder where I dump source material — research papers, clipped web pages, PDFs, and notes. And a "wiki" folder where Claude Code builds organized notes based on that raw material.
I need you to write an AGENTS.md file. This is a plain-English instruction file that Claude Code will read every time it organizes my material. It tells Claude Code how I want my knowledge base structured.
About me and my research:
- My field: [e.g., comparative literature / public health / quantitative sociology]
- What I study: [describe your topic in 1-3 sentences]
- The kinds of sources in my raw folder: [e.g., journal articles, interview transcripts, datasets, book chapters, news articles]
- How I think about my topic — the main themes, questions, or categories I'd use to file things: [list a few, or say "help me figure this out"]
Before you write the file, ask me up to five short questions if anything is unclear.
Then write a complete AGENTS.md that covers:
1. A short description of me and my research, so Claude Code understands the context.
2. How to read and interpret everything in the raw/ folder.
3. How to organize the wiki/ folder — what kinds of notes to create (for example, one note per theme, per author, or per concept), how to name them, and whether to use subfolders.
4. Linking conventions: Claude Code should connect related notes using Obsidian's [[double-bracket]] wiki-links so my knowledge base becomes a connected web.
5. How to handle citations and sources, so every wiki note points back to the original item in raw/.
6. A short "rules" section: never edit, move, or delete anything in raw/; never fabricate facts or sources; mark anything uncertain clearly.
Write it in plain English. I am not a programmer. Keep it clear enough that I can read and edit it myself later.
```

Claude Code will create an AGENT.md file for you. Look it up in the folder to ensure it’s there.

Then copy the following template, customize it according to your personal requirements, and ask Claude Code to create an Index.md file for you.

```text
I am building a personal research wiki in Obsidian, organized for me by Claude Code. I need you to write an index.md file — the main map or table of contents for my wiki folder.
About me and my research:
- My field: [your field]
- What I study: [1-3 sentences]
- The main themes or categories I expect my wiki to be organized around: [list a few, or say "propose some based on what I told you"]
Before you write the file, ask me up to three short questions if anything is unclear.
Then write a complete index.md that:
1. Opens with a one-paragraph overview of what this wiki is and what research it supports.
2. Lists my main themes or categories as sections, with a one-line description of each.
3. Under each section, leaves space (using Obsidian [[double-bracket]] links) for the individual wiki notes that will live there — so the index works as a navigation hub.
4. Includes a short note at the bottom explaining that this index is a living document: Claude Code should update it whenever it adds new notes to the wiki.
Write it in plain English, clean and easy to scan. I am not a programmer, and I want to be able to read and edit this myself.
```

Both these prompts will make Claude Code ask follow-up questions. Simply respond to them according to your preferences and Claude Code will tailor these files accordingly.

# Part 5: Ask Claude Code to Build Your Wiki

Once you have enough materials in your raw folder and your instructions have been set up, you can simply run the following prompt in Claude Code:

```text
Read AGENTS.md, look at everything in the raw folder and build the initial wiki structure.
```

Claude Code will read your instructions, go through everything in the raw folder, and create an organized wiki in the wiki folder.

Open the wiki folder in Obsidian and you will see structured notes based on the raw materials linked bidirectionally.

![Vídeo incrustat](https://pbs.twimg.com/amplify_video_thumb/2058888603988533248/img/P7W0bGZ34Ip1gAg9?format=jpg&name=large)

0:36

Now your personal research management system is set up. All you need to do is to add materials and to the raw folder and ask Claude Code to create wikis for you.

# What Not to Do

Don’t worry about creating an organized raw folder. You should just dump everything relevant into it and let Claude Code take care of organizing.

Don’t skip reading AGENTS.md and Index.md files once Claude Code creates them for you. You don’t have to read them closely, but a quick look through their contents is a good idea.

Don’t treat AGENT.md as finished product. As your project evolves, you will need to update it too.