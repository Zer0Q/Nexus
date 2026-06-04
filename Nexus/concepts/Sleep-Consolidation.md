# Sleep Consolidation

## Definition
A biologically inspired mechanism where a model periodically converts recent context into persistent fast weights, then clears its key-value cache. During the sleep phase, it performs offline recurrent passes over accumulated context and updates fast weights in state-space blocks through a learned local rule.

## Why It Matters
Long-horizon agents face the quadratic cost of attention as context grows. Sleep consolidation gives a principled alternative to ever-longer context windows -- compute moves to offline sleep, while wake-time prediction keeps low latency.

## Key Ideas
- Consolidate, then clear the cache -- recent context folded into fast weights before KV cache is discarded
- Compute moves to sleep, latency stays at wake -- extra work happens offline during consolidation
- More sleep helps hardest cases -- largest gains on tasks requiring complex reasoning over long histories
- Maps cleanly onto state-space architectures already used for efficiency
- The tradeoff is explicit and controllable rather than hidden in a ballooning context window

## Tradeoffs
- Sleep duration vs wake-time responsiveness
- Fast weight capacity vs context fidelity
- When to trigger sleep -- periodic vs event-driven consolidation

## Related
- [[concepts/Agent-Aging]]
- [[concepts/KV-Cache-Growth]]
- [[concepts/Long-Horizon-Coding]]

## Source
[[summaries/DAIR-Top-AI-Papers-of-the-Week]]
