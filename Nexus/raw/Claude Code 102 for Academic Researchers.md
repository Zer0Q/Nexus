---
title: "Claude Code 102 for Academic Researchers"
source: "https://x.com/MushtaqBilalPhD/status/2053829787219595725"
author:
  - "[[@MushtaqBilalPhD]]"
published: 2026-05-07
created: 2026-05-31
description: "This is the second part of a series of tutorials that I am doing on Claude Code for academic researchers.This tutorial builds on the first t..."
tags:
  - "clippings"
---
![Imatge](https://pbs.twimg.com/media/HICpfw7WkAADwlz?format=jpg&name=large)

This is the second part of a series of tutorials that I am doing on Claude Code for academic researchers.

This tutorial builds on the first tutorial, Claude Code 101, which went viral with more than 4M views. You can read it below:

> 7 de maig

I am writing these tutorials in a simple and accessible language. You don’t need any technical skills to understand these tutorials or use Claude Code. If you can write sentences in English, you can use Claude Code.

## Quick Recap of Claude Code 101

In the first tutorial, you learned how to open a single folder, add your PDFs, and give Claude Code a CLAUDE.md file, which contains instruction for Claude Code. That kind of a set up works for a shorter project or when you are starting on Claude Code.

But as academic researchers, our projects run over months and even years accumulating hundreds of papers and several drafts.

In this tutorial, we will learn how to structure a longer academic project with the help of Claude Code.

# Part 1: Structing a Long Project

Let’s assume that we are working on a project like a dissertation, a monograph, or a research paper. If you organize a project like this in one folder with only one CLAUDE.md file, Claude will end up giving you the same kind of results. It won’t be able to give you precise and customized results suitable for your work.

Think of it this way, if you want your (human) research assistant to draft a section of your paper, clean a dataset, or annotate an article, you will give them a different set of instructions for each of these task.

We can use this exact organizing scheme in Claude Code by creating subfolders.

## 1.1 Subfolders for Better Organization

Let’s say you are working on a dissertation for which you have a main folder called “My Dissertation.” Inside the main folder, create subfolders:

- **Literature** for PDFs and notes on published scholarship
- **Chapters** for drafts of your chapters
- **Data** for datasets
- **Notes** for meeting notes and ideas
- **Correspondence** for advisor emails, co-author exchanges, reviewer reports

This kind of organization will help both you and Claude Code. If you have to work on a draft of a chapter, you can go straight to the Chapters folder.

Similar is the case with Claude Code. If you ask it a question about, say, a certain data point, it will know to look for it in the Data folder.

![Imatge](https://pbs.twimg.com/media/HICpjNoWsAAuexw?format=png&name=large)

## 1.2 CLAUDE.md files for Subfolders

In the 101 tutorial, we wrote a CLAUDE.md file, which is a set of instructions that Claude Code reads every time it starts a session.

In your main dissertation, write a CLAUDE.md file that tells Claude Code about you and your project in general terms. We’ll call this “global” CLAUDE.md file.

It doesn’t mean you should be vague. Be precise but give it the big picture. We will have time for specificity later. Treat this CLAUDE.md as your project’s constitution.

Inside each subfolder, put another CLAUDE.md file that applies only to that particular subfolder. We’ll call these “local” CLAUDE.md files. The purpose of local CLAUDE.md files in subfolder is to give Claude Code specific instructions about these tasks without bloating the main CLAUDE.md file.

![Imatge](https://pbs.twimg.com/media/HICpr-PW0AEWgbd?format=png&name=large)

For example, you’re the CLAUDE.md file in your Chapters subfolder might say:

> If I ask you to critique my draft, follow the structure: argument, evidence, literature, counterargument. Always use MLA 9th edition citation style unless I specify otherwise.

You CLAUDE.md for the Data subfolder may contain an instruction like:

> Treat all CSV files and Excel sheets as raw data unless I specify otherwise. Never overwrite any raw files. Save the cleaned versions with \_clean added at the end of file names.

And your CLAUDE.md file for the Correspondence folder might say:

> Always prioritize points that are common between the review reports and co-author exchanges.

## 1.3 Nested CLAUDE.md Files

When Claude Code works in a subfolder, it reads two CLAUDE.md files: one, which is in the subfolder and the other, which is in the main folder. These nested CLAUDE.md files give Claude Code a clear about what your overall project is about and how to respond to specific questions precisely.

![Imatge](https://pbs.twimg.com/media/HICp1ohW4AAHYj2?format=png&name=large)

## 1.4 Output Styles for Local CLAUDE.md Files

You should also consider adding a brief instruction about output style in each local CLAUDE.md file.

For example, in the Literature subfolder, you can ask Claude Code to give you a table with columns for argument, evidence, relevance to your project when you ask it to summarize a paper. Similarly, in the Notes subfolder, you can ask it to respond in bullet points.

You can always go back and revise these instructions.

![Imatge](https://pbs.twimg.com/media/HICp4tzWQAEIsxn?format=png&name=large)

## 1.5 Practical Example/Exercise

Open your main dissertation folder in Claude Code and type the following prompt:

> Read the five papers that I added to the Literature subfolder today and tell me which ones support or refute my arguments in “Chapter 3 – Outline.md” in the Chapters subfolder.

Claude Code will read the global CLAUDE.md file and two local CLAUDE.md files in the Literature and Chapters subfolders and tells you which paper supports or refutes your arguments.

![Imatge](https://pbs.twimg.com/media/HICp7anWQAAl1_K?format=png&name=large)

## 1.6 What Not to Do

Don’t duplicate instructions in global and local CLAUDE.md files. It’s unnecessary and will lead Claude Code to process more tokens.

The local CLAUDE.md files in subfolders should not contradict instructions in the global CLAUDE.md file. If there is a contradiction, Claude Code will follow the more specific instruction, but you will end up confused.

![Imatge](https://pbs.twimg.com/media/HICp-aDWcAAA7xN?format=png&name=large)

# Part 2: Plan Mode and Custom Slash Commands

A long academic project like a dissertation or a research paper involves certain repetitive tasks. For example, you may be screening papers for literature review over and over. You will have to write an outline every time you start drafting a chapter. If you write zero drafts (also known as free writing), you will need to “clean” them up almost on a daily basis.

But there are also tasks that complex and not repetitive. For example, responding to reviewers’ feedback requires a serious engagement with their critical feedback followed by rewriting your manuscript.

Claude Code can help you with both types of tasks. For complex, one-off tasks, Claude Code offers a Plan Mode and for repetitive tasks, it has Custom Slash Commands.

## 2.1 Plan Mode

Generally, when you give Claude Code a task, it immediately gets to work. For small, low-stakes tasks, it works fine. For example, you ask Claude Code to rename all PDFs in your Literature subfolder using their titles and author names. Claude Code does that immediately.

But this approach does not produce desirable results for complex tasks. Suppose you have your raw notes on thirty-five research papers, and you ask Claude Code to synthesize your notes. If Claude Code misunderstands an instruction for any reason, you will only realize once it has completed the task.

![Imatge](https://pbs.twimg.com/media/HICqBZ2WkAEr2vx?format=png&name=large)

The Plan Mode gives you more control over Claude Code. Instead of acting immediately, it writes out a step-by-step plan of what it is going to do. You read the plan if you don’t agree with something, you ask it to amend the plan accordingly.

You can find the Plan Mode in the permissions menu under the chat bar. You can also open by using Ctrl + Shift + M. Or you can simply ask Claude Code to show you the plan in the prompt before executing anything.

## 2.2 When to Use Plan Mode

The Plan Mode is best suited for complex tasks involving three or more steps, a task that involves with more than one subfolder, or a task that produces a length output. Examples may include, synthesizing your notes, screening studies for a systematic review, or cleaning a dataset and producing a codebook.

![Imatge](https://pbs.twimg.com/media/HICqEC1WYAATNfr?format=png&name=large)

You will not ask your (human) research assistant to just go and “draft chapter three” without asking them about their plan. The Plan Mode in Claude Code works the same way.

## 2.3 Custom Slash Commands

A Slash Command is a shortcut. Claude Code has several inbuilt Slash Commands. Open your Claude Code and type in forward slash, and it will show you a list of inbuilt Slash Commands. When you type in, for example the inbuilt Slash Command, /schedule, Claude Code will create a scheduled task that can run on demand or automatically.

A Slash Command is nothing more than a set of instructions written in plain English that Claude Code follows. You can think of it as a lengthy prompt that don’t have to type every time you want to use it for a repetitive task.

![Imatge](https://pbs.twimg.com/media/HICqG6ZWUAAGznD?format=png&name=large)

Recall, in Part 5 of the 101 tutorial, we learned to create a Skill both manually and automatically. If we create a Skill automatically, it will give us a Custom Slash Command.

When you create a Custom Slash Command, Claude Code will create an .md file in .claude/commands folder on your computer. You need to know this path so that if you have to edit the .md file, you’d know where to find it.

## 2.4 Creating First Custom Slash Command

The simplest way to create a Custom Slash Command is to ask Claude Code to create one for you. For example, you can open Claude Code, and type in the following:

> Create a Slash Command called /firstdraft that converts my raw notes in my Notes folder into cohesive and coherent paragraphs without any redundant words of phrases.

![Imatge](https://pbs.twimg.com/media/HICqK4ZXsAAZ59W?format=png&name=large)

Claude Code will write a set of instructions in an .md file and put it in the .claude/commands folder. Once Claude Code is done create the Slash Command, restart the session and type in forward slash. You will see /firstdraft in the menu.

You can build a library of Custom Slash Commands written specifically for your project.

## 2.5 What Not to Do

Do not write Slash Commands for tasks you do once every six months. Those Commands will crowd your Slash Menu and will likely get outdated as your project evolves.

Do not add lengthy instructions involving multi-step processes in a Slash Command file. Keep one Slash Command for one specific, repetitive task. If your instructions exceed fifteen lines, you most likely need two Slash Commands.

For longer, complex tasks, do not skip the Plan Mode.

![Imatge](https://pbs.twimg.com/media/HICqNuSXoAAuCIn?format=png&name=large)

# Part 3: Subagents for Parallel Research Task

Up till now, we have only looked at tasks that can be done in a single Claude Code session either in Plan Mode or with Custom Slash Commands. You have one AI assistant that you work with in the main panel.

But for a longer project like a dissertation or a research paper, you may need multiple AI assistants. That’s where subagents come in.

## 3.1 Why One Assistant Is Not Enough

In longer projects, we come across two problems while using an AI agent like Claude Code.

If you ask Claude Code to read through twenty PDFs in your Literature folder, every page of every paper becomes part of the conversation for Claude Code. You ask it several questions, and it answers you.

![Imatge](https://pbs.twimg.com/media/HICqUFFXoAAeAU-?format=png&name=large)

Now all the text in the papers and your conversations is part of Claude Code’s memory for that session. Now if you ask it draft an outline for Chapter 4 of your dissertation, it’s responses will become slow and lack clarity because of all the context. This is called “context clutter.”

Secondly, in a single session, you can only assign Claude Code tasks sequentially. If you want three different critiques of your manuscript (one from a theorist, one from an informationist, and one from Reviewer 2), you can’t run them sequentially in a single session because each critique will influence the next one because of context clutter.

You want three independent sessions for a task like this.

## 3.2 What is a Subagent?

Think of a subagent as a specialist version of Claude Code with its own instructions and, more importantly, its own context window. Context window is Claude Code’s working memory for a single conversation. Everything Claude Code can “see” at any give moment from your files to your prompts to its own responses to instructions in CLAUDE.md sits inside the context window. When you ask a question, Claude Code uses its context window to answer.

Like Custom Slash Commands, a subagent also exists as an .md file. But unlike a Slash Command, which has no context window, a subagent has one.

Another important difference between a Slash Command and a subagent is that unlike a Slash Command, a subagent does not read the CLAUDE.md file. It has its own instructions in an .md file and that’s about it.

![Imatge](https://pbs.twimg.com/media/HICqW9SXcAA7NSc?format=png&name=large)

A subagent will have a very specific role, for example, a “Citation Checker” or a “Critical Reviewer.” And each agent has its own context. When you delegate a task from your main session to a subagent, its reading and reasoning will stay inside the subagent. You will only get the final answer. This way you can keep your main session from getting context clutter.

## 3.3 Subagents for Researchers

While the exact type of subagents that you need would depend on your project, following are a few general examples.

- Literature Reviewer Subagent: reads every new PDF added to the Literature folder and gives you structured summaries with regard to your argument.
- Citation Checker Subagent: takes a draft chapter and verifies every cited source against papers in the Literature folder and points out missing references.
- Methodology Auditor Subagent: for empirical projects, checks if your methods section is consonant with data and analyses.
- Reviewer 2 Subagent: critiques your drafts as a hostile reviewer.

![Imatge](https://pbs.twimg.com/media/HICqZsqWsAA4Abm?format=png&name=large)

## 3.4 Creating a Subagent

Just like creating Custom Slash Commands, the easiest way to create a subagent is to ask Claude Code to make one. Open a session and type:

> Create a subagent called Citation Checker. It will take a draft from the Chapters folder, list every in-text citation, verify each one against papers in the Literature folder. Then it will create a markdown file with missing references. The subagent must never edit or change the draft.

Claude Code will create a file citation-checker.md and put it in the Agents folder inside your .claude folder.

![Imatge](https://pbs.twimg.com/media/HICqcowXIAAXHo8?format=png&name=large)

Restart the session and your subagent is ready to use. To deploy a subagent, simply ask Claude Code to use it. For example, “Use Citation Checker on chapter\_4.md in the Chapters folder.”

If you want, you can always go and edit the subagent .md file to suit your requirements.

## 3.5 Example: Parallel Critique

Suppose you have finished drafting a chapter and now you want feedback on it before you send it out to your supervisor or colleague. Open a session and type:

> In parallel, get Methodology Auditor and Reviewer 2 to read and critique chapter\_4 in the Chapters folder and give me review reports. Save the two reports as chatper\_4\_critiques under the subagent’s name in the same folder.

![Imatge](https://pbs.twimg.com/media/HICqfESXsAAOhTv?format=png&name=large)

Both the subagents will use their own respective contexts to read and evaluate your draft. Once it’s done, you will have the two critiques as two separate files. Your main session never had to add your draft, or anything related in its context window.

Please note this may take a few minutes depending on the model you may be using.

## 3.6 What Not to Do

Do not create a subagent for minor tasks.

Do not give your subagents overlapping responsibilities.

Never let your subagent to edit your drafts. A subagent should always produce its reports as separate files.

![Imatge](https://pbs.twimg.com/media/HICqkdgXMAAVOZv?format=png&name=large)

# Part 4: Connecting Claude Code to Other Apps

Until now, now your project has remained within Claude Code with no integration with any other app. Everything Claude Code reads, edits, writes exists inside your project folder.

But academic projects like dissertations and research papers involve complex organizational and structural processes that are spread across various applications. For example, your citations are in Zotero, your drafts in Google Drive, and your meeting notes in Zoom.

How do we integrate these apps with our Claude Code?

In 2024, Anthropic introduced a method called Model Context Protocol (MCP) that lets users integrate apps like Zoom and Google Drive with Claude Code.

You don’t need to bother about what MCP is and how it works. You only need to know how to connect different apps using MCP.

## 4.1 How to Connect and App with Claude Code

Open your Claude Code and in the top-left corner, you will see an option “Customize.” Click on it and then select “Connect your apps” on the following screen.

This will show you Connectors, a list of apps approved by Anthropic to be used in Claude Code. Look for apps like Zoom or Google Drive and click on “Connect” on the following screen.

You will be prompted to grant Claude Code permissions. Once you do that your app will be connected with Claude Code.

![Imatge](https://pbs.twimg.com/media/HICqpkqWIAAKiQ2?format=png&name=large)

## 4.2 Practical Example

Connect your Zoom with Claude Code, open a session and type:

> Pull the transcript of the three recent calls I had with my colleague. Extract all comments related to Chapter 4 in Drafts. Save all extracted comments in a new file in the Correspondence folder with today’s date.

![Imatge](https://pbs.twimg.com/media/HICqs4qWcAAQ-TE?format=png&name=large)

## 4.3 Connectors and Subagents

As your project evolves, you can use a combination of Connectors and subagents to make your processes efficient.

For example, you can set up a subagent called Literature Reviewer that uses PubMed or arxiv databases available in the list of Connectors.

![Imatge](https://pbs.twimg.com/media/HICqvVKXsAA1Hp4?format=png&name=large)

## 4.4 What Not to Do

Do not install too many Connectors. Be selective and install only the ones related to your project.

Do not connect apps that may have confidential information that you don’t want to share with AI. For example, if your Slack contains messages with unpublished confidential data, don’t connect it.

![Imatge](https://pbs.twimg.com/media/HICqzTuXwAAae5G?format=png&name=large)

## Part 5: Hooks and Scheduled Tasks

One of the most important parts of any research project is to have a backup of all your files. You don’t want to have a single copy of your dissertation on a computer that crashes three days before your defense is due.

## 5.1 What is a Hook?

Hooks in Claude Code can automate the process of creating backups. A Hook is a short set of instructions that fires automatically when a specific event happens in Claude Code. Once you set up Hook, you won’t need to remember to use it. Claude Code will use it on its own.

![Imatge](https://pbs.twimg.com/media/HICq1q8XkAAUttD?format=png&name=large)

## 5.2 Creating Your First Hook

The easiest way to create a Hook is to simply ask Claude Code to create one. Open a Claude Code session and type:

> Set up a pre-edit safety hook that copies a chapter and saves its current version before it starts editing it.

This Hook will create a backup version of any chapter that you ask Claude Code to edit.

Once the Hook is ready to use, ask Claude Code the following

> Edit Chapter\_4.md in Drafts in light of the comments in the transcript of today’s Zoom meeting.

Claude Code will create a backup of the original file, place it in a backup folder, and edit a copy of it in the Drafts folder.

![Imatge](https://pbs.twimg.com/media/HICq5bMXsAAsCb7?format=png&name=large)

## 5.3 What are Scheduled Tasks

Longer academic writing projects involve tasks that need to be done at regular intervals. For example, you want to run literature scans every week to stay abreast of the latest publications.

You can set up Scheduled Tasks just like Hooks in Claude Code. Simply describe what should happen and when and Claude Code will write a routine for that. Scheduled Tasks will use the Connectors and subagents that we discussed in earlier parts.

![Imatge](https://pbs.twimg.com/media/HICq73JXsAAdHtk?format=png&name=large)

## 5.4 Use Cases for Scheduled Tasks

As a researcher, you would like to schedule a regular backup of your drafts. You can ask Claude Code to create a Draft Backup task that copies everything in the Drafts folder and saves it to backup folder with a date stamp.

![Imatge](https://pbs.twimg.com/media/HICq_2-W8AAzQDh?format=png&name=large)

## 5.5 Example

Open a Claude Code session and type:

> Create a Scheduled Task that runs every Monday morning at 9am. It should use the PubMed MCP to pull new papers on social media and mental health published in the last week. It should then hand over the papers to the Literature Review subagent to screen them. Save the screening table to a subfolder called Weekly Scans in the Literature folder.

## 5.6 What Not to Do

Do not set up Hooks or Scheduled Tasks involving deletion of any file.

Do not create too many Hooks so that you have difficulty remembering them. Or you can maintain a list of Hooks separately to remind you.

Do not set up a Hook or a Scheduled Task for something that you have not done at least four times manually.