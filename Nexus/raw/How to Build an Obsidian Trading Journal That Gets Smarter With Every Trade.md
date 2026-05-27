---
title: "How to Build an Obsidian Trading Journal That Gets Smarter With Every Trade"
source: "https://x.com/cyrilXBT/status/2059111626918269389"
author:
  - "[[@cyrilXBT]]"
published: 2026-05-26
created: 2026-05-26
description: "Most traders keep a journal the same way most people keep a diary.They write in it for three weeks. They stop. They start again after a bad ..."
tags:
  - "clippings"
---
![Imatge](https://pbs.twimg.com/media/HJL4pPyWIAAmJ_f?format=jpg&name=large)

Most traders keep a journal the same way most people keep a diary.

They write in it for three weeks. They stop. They start again after a bad month. They write in it for two weeks. They stop again.

The journal never compounds because the trader is the one doing the analysis. And the trader is also the one trading, managing positions, researching markets, and handling everything else that demands attention.

The analysis gets squeezed out by everything else that feels more urgent.

The Obsidian trading brain solves this permanently.

It does not require you to sit down and analyze your trades. It does the analysis automatically. It identifies your patterns before you can see them from inside individual positions. It tells you what your trading history actually says about your edge, your weaknesses, and the specific conditions where you consistently make money versus the conditions where you consistently lose it.

After 30 days it knows your trading better than you do.

After 90 days it is preventing you from making the same mistakes your past positions already documented.

After 180 days it has built a statistical picture of your actual edge that no discretionary self-assessment could produce.

This article is the complete build guide.

## Why Traders Fail to Learn From Their Trades

Before the architecture understand the problem.

Most traders lose not because they lack skill.

They lose because they cannot see their own patterns.

The pattern of cutting winners too early and holding losers too long is not visible from inside any individual trade. It only becomes visible when you look across 50 trades simultaneously.

The pattern of overtrading on Fridays when position P&L is negative is not something you notice in the moment. It shows up in the aggregate data.

The pattern of your best trades all sharing a specific setup condition is invisible when you are focused on executing each trade individually. It requires someone reading across all your best trades at once.

That someone is Claude.

Connected to your trading vault via MCP and running automated analysis on your complete trading history, Claude sees what you cannot see from inside your own experience.

## The Four Pillars of the Trading Brain

The trading brain has four distinct components that work together to turn raw trade data into compounding intelligence.

**Pillar 1: Trade Capture** — The system that records every trade with sufficient detail for meaningful analysis.

**Pillar 2: Performance Analysis** — The automated workflows that read your trade data and identify patterns in your results.

**Pillar 3: Pre-Trade Intelligence** — The decision support function that surfaces relevant historical patterns before you enter a position.

**Pillar 4: Market Intelligence** — The research layer that tracks the instruments, sectors, and conditions relevant to your strategy.

Each pillar feeds the others. Trade capture feeds performance analysis. Performance analysis feeds pre-trade intelligence. Market intelligence gives pre-trade intelligence the external context it needs to be genuinely useful.

## The Vault Structure

TRADING-BRAIN/ trades/ open/ \[YYYY-MM-DD\]-\[TICKER\]-open.md closed/ \[YYYY-MM-DD\]-\[TICKER\]-closed.md watchlist/ \[TICKER\]-watchlist.md analysis/ performance/ weekly/ \[YYYY-MM-DD\]-weekly-performance.md monthly/ \[YYYY-MM-DD\]-monthly-performance.md patterns/ \[YYYY-MM-DD\]-pattern-report.md edge-reports/ \[YYYY-MM-DD\]-edge-analysis.md intelligence/ instruments/ \[TICKER\]-intelligence.md sectors/ \[SECTOR\]-intelligence.md market-conditions/ \[YYYY-MM-DD\]-market-context.md pre-trade/ \[YYYY-MM-DD\]-\[TICKER\]-pre-trade-brief.md journal/ \[YYYY-MM-DD\]-trading-journal.md system/ CLAUDE.md edge-definition.md rules.md

## The Trading Brain CLAUDE.md

The CLAUDE.md is what makes every analysis specific to your strategy rather than generically useful.

\# Trading Brain — CLAUDE.md ## Trader Profile Name: \[YOUR NAME\] Trading style: \[DAY/SWING/POSITION\] Primary markets: \[CRYPTO/EQUITIES/FUTURES/FX\] Account size: \[APPROXIMATE RANGE\] Trading frequency: \[APPROXIMATE TRADES PER WEEK\] Experience: \[YEARS TRADING\] ## My Strategy \[Describe your strategy in specific terms\] \[What setups do you look for\] \[What conditions must be present for a valid setup\] \[What conditions invalidate a setup\] ## My Edge Definition \[Your best current understanding of where your edge lives\] \[This section gets updated by analysis as evidence accumulates\] Current hypothesis: \[YOUR EDGE HYPOTHESIS\] Supporting evidence: \[WHAT YOUR HISTORY SHOWS\] Contrary evidence: \[WHERE THE HYPOTHESIS HAS FAILED\] ## My Known Weaknesses \[Patterns that analysis has identified as consistent problems\] \[Updated as new patterns are confirmed\] Current known weaknesses: - \[WEAKNESS 1 WITH EVIDENCE\] - \[WEAKNESS 2 WITH EVIDENCE\] ## Performance Benchmarks Win rate target: \[YOUR TARGET\] Average R target: \[YOUR TARGET\] Maximum drawdown tolerance: \[YOUR LIMIT\] Best performing conditions: \[WHAT YOU KNOW SO FAR\] Worst performing conditions: \[WHAT YOU KNOW SO FAR\] ## Rules \[Your non-negotiable trading rules\] \[These should be specific enough that analysis can check whether each trade followed them\] Rule 1: \[RULE\] Rule 2: \[RULE\] Rule 3: \[RULE\] ## Analysis Preferences \[How you want Claude to present analysis\] \[What metrics matter most to you\] \[What questions you most want answered about your trading\]

## The Trade Capture System

The capture system is the foundation of everything. Garbage in produces garbage analysis. Rich capture produces rich insight.

Every trade gets its own note. The note follows a strict template so Claude can reliably extract structured data from it.

**Trade Open Template:**

\--- type: trade status: open ticker: \[TICKER\] direction: \[LONG/SHORT\] entry\_date: \[YYYY-MM-DD\] entry\_time: \[HH:MM\] entry\_price: \[PRICE\] position\_size: \[SIZE\] account\_percentage: \[% OF ACCOUNT\] setup\_type: \[YOUR SETUP NAME\] timeframe: \[PRIMARY TIMEFRAME\] market\_condition: \[TRENDING/RANGING/VOLATILE/CHOPPY\] thesis\_confidence: \[1-10\] --- # \[TICKER\] — \[DIRECTION\] — \[DATE\] ## Setup \[Describe exactly what you saw that made this a valid entry\] \[Be specific about the price action, indicators, or conditions\] ## Thesis \[Why do you expect this trade to work\] \[What is the catalyst or edge you are exploiting\] ## Plan Entry: \[PRICE\] Stop loss: \[PRICE\] — R risk: \[$ AMOUNT\] Target 1: \[PRICE\] — R reward: \[R RATIO\] Target 2: \[PRICE\] — R reward: \[R RATIO\] Max hold time: \[DURATION\] ## Risk Check \[Confirm you have checked your rules before entering\] Rule 1 compliance: \[YES/NO — WHY\] Rule 2 compliance: \[YES/NO — WHY\] Rule 3 compliance: \[YES/NO — WHY\] ## Mental State \[How are you feeling entering this trade\] \[Any external pressures or distractions\] \[Confidence in the setup: 1-10\]

**Trade Close Template** (add to the open note when closing):

\## Close close\_date: \[YYYY-MM-DD\] close\_time: \[HH:MM\] close\_price: \[PRICE\] result\_r: \[R MULTIPLE — e.g. +2.3R or -1R\] result\_pnl: \[$ AMOUNT\] hold\_duration: \[HOURS/DAYS\] exit\_reason: \[TARGET HIT/STOP HIT/MANUAL EXIT/TIME STOP\] ### What Happened \[Describe how the trade developed from entry to exit\] \[What did price actually do versus what you expected\] ### Execution Quality Did the trade follow the plan: \[YES/PARTIALLY/NO\] If no: \[What changed and why did you deviate\] ### What I Learned \[One specific insight from this trade\] \[Something you will look for or avoid in future trades\] ### Rule Adherence \[Did you follow all your rules throughout this trade\] \[If not: which rules and why\]

The detail level at capture time determines the insight level at analysis time. The traders who capture richly learn the most.

## The Performance Analysis Workflows

Three automated workflows process your trade data into intelligence.

Workflow 1: The Weekly Performance Analyzer

Every Sunday at 7PM this workflow reads all trades closed in the past seven days and produces a structured performance analysis.

The N8N trigger fires at 7PM Sunday. It calls the Claude API with this prompt:

Read all closed trade files from the past 7 days in TRADING-BRAIN/trades/closed/. Also read CLAUDE.md for my strategy, rules, and current edge definition. Produce a weekly performance analysis covering: RAW PERFORMANCE - Total trades: \[N\] - Win rate: \[%\] - Average winner: \[R\] - Average loser: \[R\] - Expectancy: \[R per trade\] - Total week P&L: \[$ and R\] PATTERN ANALYSIS Compare this week's trades against my historical patterns in CLAUDE.md. For each losing trade: - Which rule if any was violated - What setup type it was - What market condition it occurred in - What the exit reason was For each winning trade: - What setup type it was - What market condition it occurred in - What the hold duration was - Whether it hit target or was manually exited RULE ADHERENCE AUDIT For each trade this week check the Rule Compliance section. Produce a rule adherence score for each rule. Flag any rule that was violated more than once. SETUP PERFORMANCE BREAKDOWN Group all trades by setup type. For each setup type show: Win rate, average R, number of trades, best conditions. EDGE SIGNAL Does this week's data support or challenge my current edge hypothesis in CLAUDE.md? Provide specific evidence either way. NEXT WEEK FOCUS Based on this week's analysis identify: - One specific thing to do more of - One specific thing to do less of - One rule to pay particular attention to Save to: TRADING-BRAIN/analysis/performance/weekly/ \[DATE\]-weekly-performance.md

Workflow 2: The Monthly Edge Report

On the first of every month this workflow reads all weekly analyses from the previous month and synthesizes them into a comprehensive edge report.

Read all weekly performance analyses from the past 30 days in TRADING-BRAIN/analysis/performance/weekly/. Read all closed trades from the past 30 days. Read CLAUDE.md for current edge definition and known weaknesses. Produce a monthly edge report covering: STATISTICAL PERFORMANCE SUMMARY Full month statistics with enough trades for statistical significance assessment. At what trade count does this sample become statistically meaningful for my strategy. EDGE VALIDATION Does 30 days of data support my current edge hypothesis in CLAUDE.md? What conditions produced the best results? What conditions produced the worst results? What specific setup had the highest expectancy? WEAKNESS CONFIRMATION OR REFUTATION For each known weakness in CLAUDE.md: Did this month provide confirming or contradicting evidence? Should the weakness be maintained, updated, or removed? RULE EFFECTIVENESS ANALYSIS For each trading rule: What is the performance difference between trades that followed this rule versus trades that violated it? This answers the question: are your rules actually helping? OPTIMAL CONDITIONS ANALYSIS Identify the intersection of conditions where your results are best: - Which setup types - Which market conditions - Which timeframes - Which days of the week - Which session times This is your highest-probability trading environment. UPDATED EDGE DEFINITION Based on this month's evidence propose an updated edge definition for CLAUDE.md. Be specific about what the data actually shows. Save to: TRADING-BRAIN/analysis/edge-reports/ \[DATE\]-edge-analysis.md

Workflow 3: The Real-Time Pattern Alert

This workflow runs every time you close a trade and checks the outcome against your known patterns.

A trade was just closed: \[TRADE FILE PATH\] Read the closed trade note. Read CLAUDE.md for known patterns and weaknesses. Read the last 10 closed trades for context. Check this trade against every known pattern and weakness in CLAUDE.md. If this trade matches a known failure pattern: Create an alert note in TRADING-BRAIN/analysis/patterns/ titled PATTERN-ALERT-\[DATE\]-\[TICKER\].md The alert should include: - Which pattern matched - How this trade fits the pattern - What the historical outcome of this pattern is - What this means for similar future setups

## The Pre-Trade Intelligence Function

This is the feature that pays back the entire system cost within the first week.

Before entering any significant trade run this prompt:

I am considering entering this trade: Ticker: \[TICKER\] Direction: \[LONG/SHORT\] Setup: \[SETUP TYPE\] Market condition: \[CURRENT CONDITION\] Timeframe: \[TIMEFRAME\] Read my TRADING-BRAIN vault and tell me: HISTORICAL PRECEDENT Have I traded this setup before? If yes: what was the aggregate performance? Win rate, average R, sample size. What conditions produced winners versus losers? PATTERN MATCH Does this setup match any known patterns or weaknesses in my CLAUDE.md? If a weakness pattern: be direct about what my history shows happens in this situation. RULE CHECK Based on the trade details I have provided: Do any of my rules raise concerns about this entry? Flag any potential rule violations before I enter. MARKET CONTEXT MATCH How does the current market condition compare to the conditions where I perform best? Is this setup occurring in my highest-probability environment or a lower-probability one? MENTAL STATE CONSIDERATION Based on my recent trading journal entries: Am I in a mental state where my historical performance suggests I should be trading? VERDICT Given everything above: Is this setup in or out of my historical edge? What specific concerns should I address before entering? What would make this a higher-conviction entry? This is not a recommendation. This is my historical data applied to my current decision. I make the final call.

This prompt is the difference between trading with historical wisdom and trading with nothing but the current moment's information.

## The Market Intelligence Layer

The trading brain is not just an internal analysis system. It also tracks the external environment your trades exist within.

A weekly market intelligence workflow runs every Sunday morning before the performance analysis. It reads recent market developments, synthesizes the context relevant to your strategy, and deposits a market context note that the performance analysis can reference.

Search for significant market developments from the past week relevant to my trading universe. Based on my CLAUDE.md which covers \[YOUR MARKETS\]: Produce a market intelligence brief covering: MACRO CONTEXT What macro developments occurred this week that affect the conditions I trade in? SECTOR ROTATION Any significant shifts in capital flow between sectors or asset classes? VOLATILITY REGIME Has volatility expanded or contracted this week? What does this mean for my strategy's performance characteristics? KEY LEVELS Any significant technical levels across my primary instruments that were tested or broken this week? UPCOMING CATALYSTS Any events next week that could significantly affect the instruments I trade? Earnings, macro data, regulatory decisions. TRADING ENVIRONMENT ASSESSMENT Based on the above: is next week likely to be a favorable or unfavorable environment for my specific strategy? Save to: TRADING-BRAIN/intelligence/market-conditions/ \[DATE\]-market-context.md

## The Emotional Pattern Tracker

The most underutilized data in any trading journal is emotional data.

Most traders log what they did. The trading brain also tracks how they felt and what the correlation is between emotional state and performance.

The daily trading journal note captures this:

\# Trading Journal — \[DATE\] ## Morning State Energy level: \[1-10\] Focus level: \[1-10\] Emotional state: \[CALM/ANXIOUS/OVERCONFIDENT/FRUSTRATED/NEUTRAL\] External pressures today: \[ANYTHING AFFECTING FOCUS\] Market attitude: \[BULLISH/BEARISH/NEUTRAL/UNCERTAIN\] ## During Session Notable emotional moments: \[ANY SIGNIFICANT EMOTIONAL REACTIONS\] Decision quality: \[FELT IN CONTROL/REACTIVE/DISCIPLINED/IMPULSIVE\] ## End of Day Satisfaction with execution: \[1-10\] Biggest mental challenge today: \[WHAT TESTED YOU\] One thing to do differently tomorrow: \[SPECIFIC CHANGE\]

The monthly edge report includes an emotional performance correlation analysis:

Compare all trades where morning emotional state was ANXIOUS or FRUSTRATED versus CALM or NEUTRAL. What is the performance difference? Is there a statistically significant relationship between my emotional state and trading results? This analysis answers: should I trade differently based on my emotional state at session open?

## Building the System in One Weekend

The complete trading brain takes one weekend to build.

**Saturday Morning: Vault Structure**

Create all the folders. Write your CLAUDE.md. Write your edge-definition.md with your current best understanding of your edge. Write your rules.md.

Time required: 2 hours.

**Saturday Afternoon: Trade Templates**

Create the open and close trade templates as Obsidian templates. Test them by logging two or three historical trades from memory.

Time required: 1 hour.

**Saturday Evening: MCP Connection**

Install Claude Desktop. Configure the Filesystem MCP pointing at your trading vault. Verify Claude can read your CLAUDE.md and trade files.

Time required: 1 hour.

**Sunday Morning: First Analysis**

Manually trigger the weekly performance analysis on whatever trade history you have. Even five or ten historical trades will produce useful initial output.

Read the output. Note what surprised you.

Time required: 2 hours.

**Sunday Afternoon: N8N Workflows**

Set up N8N. Build the three automated workflows. Test each one.

Time required: 2 hours.

**Sunday Evening: First Pre-Trade Brief**

Think of a trade you are considering for next week. Run the pre-trade intelligence prompt. See what your history says about it.

If the prompt surfaces something you had not considered you just saw what the system does.

Time required: 30 minutes.

## What Happens After 90 Days

The trading brain's value does not peak at setup. It compounds.

At day 30 you have one month of structured trade data. The first monthly edge report identifies two or three patterns you had not consciously noticed. The pre-trade function has caught one or two setups that matched your known weakness patterns.

At day 60 the system has enough data to produce statistically meaningful insights about your specific setup performance. You know which setups have positive expectancy in your hands and which ones are net negative despite feeling valid. You stop trading the negative-expectancy setups.

At day 90 the emotional correlation analysis has enough data to answer whether your emotional state actually affects your results. For most traders this produces one of two outcomes: either emotional state has no measurable effect and they can stop worrying about it, or emotional state has a significant measurable effect and they have specific data on what to do about it.

Either outcome is valuable. Both require 90 days of data to produce.

At day 180 the trading brain has built a statistical portrait of your edge that is more accurate than any introspective self-assessment could produce. You know your win rate by setup type, by market condition, by day of week, by session time, and by emotional state. You know which rules are protecting you and which ones might be unnecessarily restrictive. You know the conditions where your expectancy is highest.

You trade differently because you are trading from evidence rather than belief.

Build the foundation this weekend.

The compounding starts from the first captured trade.

Follow [@cyrilXBT](https://x.com/@cyrilXBT) for the exact CLAUDE.md templates, N8N workflows, and trade capture formats that make this entire system run at its highest level.