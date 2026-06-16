---
type: Concept
title: Display Hierarchy
description: A four-level display structure that organizes HMI information from broad
  situational awareness to detailed diagnostics, allowing operators to navigate from
  o...
tags:
- concepts
timestamp: '2026-06-16T13:58:58Z'
---

# Display Hierarchy

## Definition
A four-level display structure that organizes HMI information from broad situational awareness to detailed diagnostics, allowing operators to navigate from overview to specific data points without losing context.

## Why It Matters
Without hierarchy, operators either see too much (overview cluttered with details) or too little (detail without context). Proper hierarchy ensures operators have overall situational awareness while maintaining the ability to drill down for troubleshooting.

## Key Ideas
- **Level 1 — Situational awareness:** overview of the operator's entire realm of control; concise process status with KPIs
- **Level 2 — Unit operation overview:** one unit operation or major task; based on P&IDs but focused on operator realm of control
- **Level 3 — Equipment detail:** task detail display including major control modules; specific equipment data
- **Level 4 — Diagnostics:** detailed information for troubleshooting; accessed when needed
- **Most plants lack L2/L3:** end users don't know how to design them; ISA-101 provides style guides
- **Navigation:** easy-to-find buttons between levels maintain operator context
- **Not based on P&ID alone:** overview displays focus on status and KPIs, not just graphical process representation

## Tradeoffs
- Requires redesign effort for legacy systems
- Balancing detail vs. simplicity at each level

## Related
- [[concepts/High-Performance-HMI]]
- [[concepts/Operator-Situational-Awareness]]
- [[concepts/ISA-101-Standard]]

## Source
[[summaries/RealPars-High-Performance-HMI]]
