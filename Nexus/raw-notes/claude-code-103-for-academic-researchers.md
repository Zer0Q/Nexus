---
title: "Claude Code 103 for Academic Researchers"
source: "https://x.com/MushtaqBilalPhD/status/2057033643973865585"
author:
  - "[[@MushtaqBilalPhD]]"
published: 2026-05-20
created: 2026-05-31
description: "This is the third installment in a series of tutorials I am doing for academic researchers. You can read Claude Code 101 here and Claude Cod..."
tags:
  - "clippings"
---
![Imatge](https://pbs.twimg.com/media/HIwNAHjWkAA7Up8?format=jpg&name=large)

This is the third installment in a series of tutorials I am doing for academic researchers. You can read [Claude Code 101 here](https://x.com/MushtaqBilalPhD/status/2052338632426467550) and [Claude Code 102 here](https://x.com/MushtaqBilalPhD/status/2053829787219595725).

I am writing these tutorials in simple and accessible language. You don’t need any coding or technical skills to understand these tutorials or use Claude Code.

That said, you will need to be a little patient and attentive as we move towards complex workflows and powerful features of Claude Code.

# Part 1: Chaining Subagents into a Research Pipeline

In Claude Code, you can not only create subagents (AI assistants for a specialized task) but also chain them together so that when Subagent 1 is done, it hands over its output to Subagent 2. And when Subagent 2 is done, it hands over its output to Subagent 3, and so on.

Think of it a relay race in which one runner hands the baton to the next one after completing their assigned task.

To create subagents and chain them together, you don’t need any coding skills whatsoever. As long as you can read and in plain English, you are good to go.

## 1.1 What is a Subagent?

A subagent is a specialized assistant with three characteristics. First, it is designed for doing one very specific task. Second, it has its own working memory. Third, it exists as a file that Claude Code creates on your computer.

The separate memory feature of a subagent is important because when you invoke a subagent in the middle of a session, it doesn’t clog up your session. Instead, it accomplishes what it’s supposed to and gives you the result as a file in your working folder.

![Imatge](https://pbs.twimg.com/media/HIwN1_mXgAAf0ke?format=png&name=large)

## 1.2 Why Chain Subagents?

A subagent can only do a very specific task within the whole academic writing and research process. If you have multiple subagents, you will want to chain them together so that the output of one subagent feeds into the next.

Let’s say you have a subagent called “First-Drafter” that takes transcription of your raw voice notes, removes redundant words from them, and gives you a cohesive draft as 01\_firstdraft.

![Imatge](https://pbs.twimg.com/media/HIwN6RBWAAAm1ip?format=png&name=large)

You have a second subagent called “Literature-Discoverer” that takes your 01\_firstdraft, looks up relevant papers, and gives you a list as 02\_relevantpapers.

Now what you want is to chain the two subagents together, so that when you upload your transcripts, “First-Drafter” hands over 01\_firstdraft to “Literature-Discoverer” and you get the final product, a list of relevant papers.

## 1.3 Setting Up a Research Pipeline

To set up a research pipeline, let’s consider the example of the systematic review process. I am taking this as an example because a systematic review has clearly demarcated stages that are easily understood.

We will build a research pipeline with the following subagents:

- **Importer-Deduplicator Subagent:** removes duplicates from imported files (RIS, PubMed, txt, etc.) and create 01\_deduplicated.csv
- **Title/Abstract Screener Subagent:** screens titles and abstracts in 01\_deduplicated.csv according to your inclusion/exclusion and save the results in 02\_title\_abstract\_screen.csv
- **Full-Text Screener Subagent:** screens full texts of studies included in 02\_title\_abstract\_screen.csv according to the criteria and save the results in 03\_fulltext\_screen.csv
- **Data Extractor Subagent:** pulls the predefined fields (population, design, sample size, outcomes) from each included study in 03\_fulltext\_screen.csv and save the results in 04\_extraction\_table.csv

![Imatge](https://pbs.twimg.com/media/HIwN9v-WkAA3dJq?format=png&name=large)

Before you start creating subagents, figure out the kind of pipeline that will work for the task you want to accomplish.

Since we are taking the example of a systematic review, we will also need a protocol with inclusion and exclusion criteria.

## 1.4 Setting Up a Project Folder

Create a new folder on your computer titled “Systematic Review with Subagents.” In this folder, create a protocol.md file containing your inclusion/exclusion criteria.

Also, create a subfolder called “Imported Papers” in which you will add RIS, PubMed, BibTeX, etc. files containing the metadata of papers. Almost all databases let you download the metadata as RIS files.

![Imatge](https://pbs.twimg.com/media/HIwOBD1XsAAh5C_?format=png&name=large)

## 1.5 Building Subagents One at a Time

Start by building and testing one subagent at a time. This way if there is any error or problem in the workflow, you will be able to figure it out easily.

Open your “Systematic Review with Subagents” folder in Claude Code and type:

> Create a subagent called Importer-Deduplicator. It jobs is to read every file in the “Imported Papers” folder, combine them into one single list, and remove duplicate paper. It should look at DOIs and paper titles to remove duplicates. After it’s done, it should save the results in a file titled 01\_deduplicated.csv. It must show how many records it started with, how many duplicates it removed, and how many remain. It must never edit, modify, or delete any files in “Imported Papers.”

Claude Code may ask you follow-up questions after which it will tell you when the subagent is ready to use. You may have to restart the session, so the subagent loads properly.

![Imatge](https://pbs.twimg.com/media/HIwOIctWMAApEnS?format=png&name=large)

Start a session and type the following:

> Use Importer-Deduplicator on all files in “Imported Papers” folder.

The subagent will deduplicate the studies and create a file tiled 01\_deduplicated.csv.

At this stage, you want to open 01\_deduplicated.csv in Excel and see for yourself if the deduplicator subagent worked properly or not. If it didn't work as expected, simply tell Claude Code to update the subagent according to your requirements.

Once you are satisfied with your first subagent, move on to the next one, Title/Abstract Screener. Type the following in your session:

> Create a subagent for me called TA-Screener. It should read 01\_records.csv and protocol.md. Then it should evaluate every paper in 01\_records.csv according to the screening criteria in protocol.md and mark every paper as include, exclude, or unclear. It should save the results in a new file called 02\_title\_abstract\_screen.csv, which contains the titles and abstracts of every study and a screening decision. It must never change, edit, or delete 01\_records.csv or protocol.md.

Once your subagent is ready to deploy, type the following:

> Run TA-Screener on 01\_records.csv

The subagent will screen the studies and will give you 02\_title\_abstract\_screen.csv. Go through this file to see if the subagent worked properly.

Follow the similar workflow to create and test two more subagents: Full-Text Screener and Data Extractor.

You can use the following prompts to create these two subagents.

> **Full-Text Screener**

> Create a subagent called Full-Text Screener. It should read 02\_title\_abstract\_screen.csv and take only the records marker include. Then it should match each record against PDFs in the Full Texts folder. The it should evaluate the full text PDFs against the screening criteria in protocol.md. After it’s done, it should save the results in a new file 03\_fulltext\_screen.csv. It must never modify, edit, or delete any existing files including 02\_title\_abstract\_screen.csv and protocol.md.

> **Data Extractor**

> Create a subagent for me called Data Extractor. It should read 03\_fulltext\_screen.csv and take only the studies marked include and match them against PDFs in the Full Texts folder. Then it should extract the following information from the included PDFs: title, study design, objectives, sample size, country, interventions. If there is no relevant information available for a field in a paper, it should mark it “Not available.” It must never guess or extrapolate. It must never modify, edit, or delete any existing files.

## 1.6 Chaining Subagents

Once you are satisfied with the performance of your individual subagents, you can chain them together. Please make sure there is no mismatch between the file names you give to your subagents, because such a mismatch will break the chain.

Before you chain the subagents, you should switch to Plan Mode. This way Claude Code will give you a complete plan before executing anything. If you spot an error, you can easily ask Claude Code to rectify it.

![Imatge](https://pbs.twimg.com/media/HIwOL2sW0AA5kfg?format=png&name=large)

Take an RIS file containing 20-50 studies and add it to your “Imported Papers” folder. Then type the following:

> Run the systematic review pipeline on “Imported Papers” folder in the following order: Importer-Deduplicator, then TA-Screener. Stop after each stage and give me an update.

Since this is your first time orchestrating such a chain of subagents, you want to make sure that each subagent is handing over the required to file to the next one.

Once you are satisfied that the subagents are working properly, you can chain all four of them and run the pipeline on a larger set of studies.

## 1.7 What Not to Do

Do not give one subagent several tasks. Each subagent must have only specific task, the completion of which generates your desired output.

Do not chain a subagent without testing it individually first.

Do not overlook the file names. They are crucial for the chain to work.

Do not give your subagent pipeline a huge task right out the gate without testing it first on a smaller scale.

Do not let any subagent edit, modify, or delete any existing files.

![Imatge](https://pbs.twimg.com/media/HIwOPxHWQAIXRyd?format=png&name=large)

# Part 2: Version Control for Academic Projects

Let’s say, one Tuesday afternoon, you revised a section of Chapter 4, edited a figure in your data folder according to the revisions, and deleted a couple of interview transcripts you thought the revisions had rendered unnecessary. This is a complex workflow spread across multiple documents and folders.

A couple of weeks later, you realize that the revisions are not working the way you had hoped and would like to revert to earlier version. Now you will need to undo multiple changes in the draft, in the data folder, and in transcripts folder. This is a cumbersome process prone to errors.

We can automate this process by using an app called Git.

## 2.1 What is Git?

Git is a free and open-source application that helps you control different versions of your project. Think of it as a camera that takes photos of your entire project (your drafts, reading materials, raw data, etc.) at once and keeps them in a folder.

This is the main difference between having a version history of a single Word file or a Google Doc. For example, a Word file will show you how your draft looked last Monday before you started revising it. Git, on the other hand, will tell you how your whole project (dissertation, research paper, etc.) looked a specific point in time.

![Imatge](https://pbs.twimg.com/media/HIwOUBPWMAAR4MX?format=png&name=large)

## 2.2 Setting Up Git in Your Project

To set up Git, go to [git-scm.com](https://git-scm.com/). Download the application on your computer and install it just like you would any other application.

Open your project (e.g. a folder titled “My Dissertation”) in Claude Code and type:

> Set up Git in this folder and create an initial commit with all my current files.

A commit is a snapshot of your folder at a given point in time.

Claude Code will take a snapshot and save it. From this point on, your project has a version history, and you have complete control over it.

![Imatge](https://pbs.twimg.com/media/HIwOW9GW0AA9BfT?format=png&name=large)

One thing you may want to keep in mind is that Git does not store a version of your project in the same format as the files in your folder. For example, a .docx file is not saved as a .docx file.

Git saves a snapshot of your project as a worktree in a hidden folder called .git.

You don’t need to know or understand how Git saves snapshots of your projects or what is in the .git folder. All you need to know is how to save a snapshot and how to recall one if needed.

## 2.3 Saving Snapshots

After you are done with a work session, the kind where you made substantial changes to your drafts and added new reading materials, ask Claude Code the following:

> Commit the current state of the project with the note “Revised Chapter 4, aligned introduction with figure, and added new reading materials.”

![Imatge](https://pbs.twimg.com/media/HIwOaBdXgAEL37Q?format=png&name=large)

Git will take a snapshot of the current state of your project and save it. The note is a commit message that will tell your future self about what was accomplished in a given work session.

It would be good practice to commit a git (or take a snapshot of your whole project) after every meaningful session in which you make substantial changes across documents.

## 2.4 Retrieving an Earlier Version of the Whole Project

The great thing about Git is that you don’t have to remember anything to retrieve an earlier version of your project.

You can simply ask Claude Code:

> Show me the last ten commits with their dates and notes.

![Imatge](https://pbs.twimg.com/media/HIwOc1YXcAABUqC?format=png&name=large)

Claude Code will give you a dated list with your commit notes. Every commit (snapshot) will have a unique alphanumeric ID. Find the date or version you want to retrieve and type:

> Restore the whole project to \[Commit ID\] and save it as “Restored Project \[Date\].”

Git will restore that version of your project, and you will have access to everything in it: the drafts, the PDFs, and so on.

## 2.5 What Not to Do?

Don’t label your commits vaguely with words like “Updates.” After a few times, you will have too many commits with Updates, and you won’t be able to see what exactly a given version contains. Instead, ask Claude Code to add a descriptive note mentioning what was accomplished in a given work session.

![Imatge](https://pbs.twimg.com/media/HIwOgStXsAA1xMb?format=png&name=large)

Don’t treat commits as something you’d do occasionally. Instead, make it a habit to take snapshots regularly.

Don’t assume that Git is a backup. Git saves a snapshot of your project at a given point in time and saves it on your computer. If your computer crashes, you lose access to these versions. You should keep a backup of your project on cloud or a separate drive.