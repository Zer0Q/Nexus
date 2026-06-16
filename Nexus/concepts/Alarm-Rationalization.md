---
type: Concept
title: Alarm Rationalization
description: The systematic review and justification of potential alarms against defined
  criteria to ensure they meet the alarm definition, with documented consequences,
  ...
tags:
- concepts
timestamp: '2026-06-16T13:58:58Z'
---

# Alarm Rationalization

## Definition
The systematic review and justification of potential alarms against defined criteria to ensure they meet the alarm definition, with documented consequences, corrective actions, priorities, and classifications recorded in a Master Alarm Database (MAD).

## Why It Matters
Rationalization is the core transformation step — it removes notifications that are not truly alarms and ensures each remaining alarm has a defined consequence, response time, and operator action. Without rationalization, alarm systems remain mixed notification tools with random priorities.

## Key Ideas
- **Process:** export current alarms → build potential alarm list → review each against alarm definition → justify or remove → document attributes
- **Attributes documented:** limit, priority, classification, type, consequence, response time, operator action
- **Output:** Master Alarm Database (MAD) with configuration requirements for each alarm
- **Priority vs. classification:** not mutually exclusive — classification manages requirements, prioritization serves the operator
- **Safety alarms still rationalized:** even critical safety alarms must go through the process
- **Facilitated approach:** unit operation rationalization workshops (e.g., two weeks for one plant, three-day review for adoption at other sites)
- **Typical results:** 50% of alarms removed or added, 80% modified for priority or setpoint

## Tradeoffs
- Time-intensive: two weeks of facilitated workshops per plant
- Risk of over-rationalization: one consultant "rationalized critical alarms out of existence"
- Requires cross-functional team: operators, automation engineers, process engineers

## Related
- [[concepts/Alarm-Management]]
- [[concepts/Alarm-Philosophy]]
- [[concepts/Alarm-Classification]]
- [[concepts/ISA-18-2-Standard]]

## Source
[[summaries/Dunn-Sands-Alarm-Management-FAQ]]
