# Cost Tracking

## Definition
Logging the exact cost per run for autonomous agent workflows. Critical once agents start running 24/7, as untracked costs compound quickly across multiple models, tools, and API calls.

## Why It Matters
Autonomous loops running continuously can generate unexpected bills. Cost tracking provides visibility into which workflows, models, and tools are the most expensive, enabling optimization before costs spiral.

## Key Ideas
- Log exact cost per run -- not estimated, but actual API costs
- Breakdown by model, tool, and workflow stage
- Cost tracking becomes a constraint in workflow design -- expensive tools reserved for high-value tasks
- Use local/cheap models for scanning, summaries, brainstorming, low-risk review
- Save frontier models for planning, debugging, and hard reasoning
- Model diversity also serves cost optimization -- different providers have different price points

## Tradeoffs
- Tracking granularity vs implementation overhead
- Cost optimization vs quality -- cheaper models may produce worse results
- Budget limits vs workflow completeness -- cutting costs may mean incomplete work

## Related
- [[concepts/Model-Selection-Tiers]]
- [[concepts/Model-Diversity]]
- [[concepts/Context-Efficiency-Frontier]]

## Source
[[summaries/gkisokay-21-Mistakes-Building-AI-Agents]]
