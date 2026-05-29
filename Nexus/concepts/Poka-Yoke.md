# Poka-Yoke

## Definition
Error-proofing: designing systems so the right action is the easiest action, making it difficult or impossible to make mistakes. From Lean manufacturing — "poka" (mistake) + "yoke" (avoid).

## Why It Matters
Training is a weak control — it relies on memory and willpower under pressure, and both fail predictably. People change roles, get busy, forget, and find shortcuts. A good system does the work that training can't. System design beats human discipline every time.

## Key Ideas
- **Make right action easiest:** if only certain values are valid, the system guides the user to them
- **Block wrong actions:** if a field is critical, the process can't continue without it
- **Own critical data:** if a master data table drives automation, it gets a clear owner
- **Fix taxonomy, not behavior:** if "Other" is one of your most-selected options, your taxonomy is broken and no workshop will fix it
- **Real example:** replaced long dropdown list with a tree organized how technicians think about their work — selecting the correct option became faster than selecting the wrong one
- **System + people:** design the system so the right path is easy, AND give people a real stake in the system — neither half works alone
- **Applies to AI:** AI systems inherit the same principle — design interfaces and workflows that prevent bad input rather than relying on user diligence

## Tradeoffs
- Over-constraint can frustrate legitimate edge cases
- Requires upfront design investment and understanding of actual user workflows

## Related
- [[Visual-Management]]
- [[Gemba]]
- [[People-Process-Technology-Sequence]]

## Source
[[Gellida-Broken-Process-Broken-AI]]
