---
title: "Post by @karpathy on X"
source: "https://x.com/karpathy/status/2039805659525644595"
author: "@karpathy"
published: "2026-04-02"
type: article
---

# Karpathy LLM Knowledge Bases

## Summary
Karpathy describes his workflow for using LLMs to build personal knowledge bases: raw data ingest into a directory, LLM compilation into a structured wiki of markdown files, Obsidian as the IDE frontend, and the LLM auto-maintaining index files and summaries. At ~100 articles and 400K words, the wiki becomes queryable with complex questions. Outputs can be filed back into the wiki, compounding knowledge over time.

## Core Concepts
- [[Write-Time-Knowledge-Systems]] -- LLM compiles knowledge once, keeps it current
- [[Compilation-Agent]] -- LLM reads raw sources and writes/maintains wiki pages
- [[Knowledge-Source-of-Truth]] -- raw/ is immutable source of truth
- [[Browsable-Knowledge]] -- Obsidian as IDE for viewing compiled wiki
- [[Error-Compounding]] -- filed outputs can propagate errors
- [[LLM-Wiki-Pattern]] -- incremental wiki maintenance by LLM

## Key Insights
- LLM as wiki maintainer eliminates the bookkeeping bottleneck
- Index files maintained by LLM work better than RAG at small-to-medium scale
- Filing query outputs back into the wiki makes explorations compound
- LLM health checks catch inconsistencies, missing data, orphan pages
- The pattern suggests synthetic data generation + fine-tuning for larger scale

## Open Questions
- At what scale does the index-file approach break down?
- How does this compare to embedding-based RAG at 1000+ pages?
