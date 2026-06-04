# Quality Benchmarks — Reference Examples

Use these as calibration points when scoring notes.

---

## HIGH QUALITY — Score: 23-25/25

### Example 1: `w1nklerr-DGX-Spark-Cost-Recovery.md`
**Why it scores high:**
- **Summary:** 3 sentences of original synthesis. Covers hardware, ROI, and mindset shift.
- **Concepts:** 8 concepts, each with specific description (specs, numbers, definitions).
- **Insights:** 6 concrete insights with data ($1,900/month, 1.6 months, 128GB, 405B params).
- **Questions:** 3 specific questions about GB10 vs 5090, thermal profile, ConnectX-7.
- **Density:** Every line carries information. ~2.3KB of pure signal.

### Example 2: `NeilXBT-Obsidian-Knowledge-Graph-Learning.md`
**Why it scores high:**
- **Summary:** References concepts with wikilinks. Synthesizes the 5-module system.
- **Concepts:** 11 concepts, all with concrete one-line definitions.
- **Insights:** 8 insights, each a complete thought. Uses specific data (15-20% improvement).
- **Questions:** 3 questions referencing concepts from the note with wikilinks.
- **Density:** ~2.8KB. No empty sections.

### Example 3: `AkshayPachaar-Hermes-Agent-Masterclass.md`
**Why it scores high:**
- **Summary:** Dense 2-sentence synthesis covering architecture, memory, skills, GEPA, profiles.
- **Concepts:** 9 concepts, each defined with specificity ("SOUL.md as the fixed personality frame").
- **Insights:** 5 insights with comparisons (vs OpenClaw, vs agent self-congratulation).
- **Questions:** 2 specific questions about skill transfer and Curator token cost.
- **Density:** ~1.8KB, zero filler.

---

## LOW QUALITY — Score: 1-10/25

### Example 1: `NainsiDwiv50980-rag-doesn-learn-karpathy-llm-wiki-changes.md`
**Score: ~7/25 — FAIL**
- **Summary (1/5):** Single fragmented sentence. Reads like truncated source text.
- **Concepts (2/5):** All 5 use `-- related concept`. Zero definitions.
- **Insights (1/5):** Empty section.
- **Questions (2/5):** Generic template: "How does this approach scale in production?"
- **Density (1/5):** ~940 bytes, mostly empty structure.

### Example 2: `zachlloydtweets-introducing-multi-harness-orchestration.md`
**Score: ~8/25 — FAIL**
- **Summary (1/5):** Verbatim copy of source marketing text: "Today, we're launching major upgrades..."
- **Concepts (2/5):** All 5 use `-- related concept`.
- **Insights (2/5):** Section headers without content: "More agent harnesses in the cloud:", "Automate more complex..."
- **Questions (2/5):** Same generic template as other notes.
- **Density (1/5):** ~1.2KB but content is hollow.

### Example 3: `NCSC-CAF-Collection-Introduction.md`
**Score: ~9/25 — FAIL**
- **Summary (1/5):** "Artículo sobre introduction to the caf collection" — lazy meta-description.
- **Concepts (3/5):** 2 concepts, one defined, one OK — but only 2 for a standards article.
- **Insights (1/5):** "Refer to extracted concepts for details" — lazy placeholder.
- **Questions (1/5):** Empty.
- **Density (2/5):** ~720 bytes. Thin.

---

## SCORING QUICK REFERENCE

| Dimension | 5 (Excellent) | 3 (OK) | 1 (Fail) |
|-----------|---------------|--------|----------|
| SYNTHESIS | Original 2-3 sentence synthesis | Partial synthesis, some copied text | Verbatim copy or "Artículo sobre..." |
| CONCEPTS | Every concept has WHAT + WHY | Mix of defined and vague | All `-- related concept` |
| INSIGHTS | 5+ with data/quotes/numbers | 2-3, some concrete | Empty or "Refer to extracted..." |
| QUESTIONS | Specific to article, reference concepts | Tangentially related | Generic template (identical across notes) |
| DENSITY | Every line is signal | Some empty sections | Mostly empty structure, <500 bytes |

**PASS threshold: 15/25 | WARN: 11-14 | FAIL: 1-10**
