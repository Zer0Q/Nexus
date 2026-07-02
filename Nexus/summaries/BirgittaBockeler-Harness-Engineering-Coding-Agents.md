---
type: Article
title: "Harness engineering for coding agent users"
description: "A bounded-context model of coding-agent harnesses built from feedforward guides, feedback sensors, and human steering."
resource: "https://martinfowler.com/articles/harness-engineering.html"
tags: [harness-engineering, coding-agents, software-quality]
timestamp: "2026-06-23T00:00:00Z"
author: "Birgitta Bockeler"
---

# Harness Engineering for Coding Agents

## Summary
Bockeler narrows harness engineering to the user-built outer harness around coding agents: guides that steer before action and sensors that observe after action. The article's important distinction is that harnesses regulate different qualities (maintainability, architecture fitness, behavior), using both deterministic computational controls and probabilistic inferential controls, with humans still steering what matters.

## Core Concepts
- [[concepts/Harness-Engineering]] -- designing the controls around an agent so it produces better work and self-corrects earlier.
- [[concepts/Feedforward-and-Feedback-Controls]] -- guides prevent bad output before action; sensors detect issues after action.
- [[concepts/Fitness-Function-Driven-Development]] -- architecture fitness functions become sensors for coding agents.
- [[concepts/Harnessability]] -- some codebases are easier to regulate because they expose types, boundaries, tests, and tooling.
- [[concepts/Human-Comparative-Advantage]] -- human judgment remains needed for goals, tradeoffs, organizational memory, and taste.

## Key Insights
- Feedback-only agents repeat mistakes, while feedforward-only agents never learn whether their rules worked.
- Computational controls are cheap and deterministic; inferential controls add semantic judgment but are slower and probabilistic.
- Maintainability is the easiest harness category because tests, linters, type systems, structural checks, and coverage tools already exist.
- Behavior harnessing remains hardest because passing AI-generated tests does not prove the product behaves correctly.
- Harness templates may become the next evolution of service templates: topology plus guides and sensors for a specific stack.

## Open Questions
- How can [[concepts/Harnessability]] be measured before choosing a stack for AI-heavy development?
- What evaluation methods test the quality of a harness itself, analogous to test coverage or mutation testing?
- How should teams keep [[concepts/Feedforward-and-Feedback-Controls]] coherent as guides and sensors grow?

## Source
[[raw-notes/harness-engineering-for-coding-agent-users]]
