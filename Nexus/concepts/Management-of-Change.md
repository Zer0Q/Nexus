---
type: Concept
title: Management of Change
description: A formal process for reviewing, approving, and documenting modifications
  to alarm systems before they are implemented. Ensures that changes to alarms (setpoi...
tags:
- concepts
timestamp: '2026-06-16T13:58:58Z'
---

# Management of Change

## Definition
A formal process for reviewing, approving, and documenting modifications to alarm systems before they are implemented. Ensures that changes to alarms (setpoints, priorities, classifications, additions, deletions) are evaluated against the alarm philosophy and do not degrade system integrity.

## Why It Matters
Processes continually change — raw materials, product specifications, debottlenecking, new regulations, plant trials. Without formal MOC, alarm modifications accumulate untracked, eroding the benefits of rationalization and creating silent failures in the alarm system.

## Key Ideas
- **MOC loop in lifecycle:** connects monitoring (which detects unmanaged changes) to maintenance (which implements controlled changes)
- **Different approval levels:** alarms from engineering studies or functional safety may require higher approval levels than general alarms
- **HMA strictness:** Highly Managed Alarms have stricter MOC requirements
- **Fast-track MOC:** simplified process for low-risk changes — common but must be controlled
- **Common failure mode:** maintenance transferring alarms in/out of service without structured expectations and schedules
- **Monitoring detects violations:** performance monitoring reveals when changes occurred without following MOC procedures
- **Documented in philosophy:** MOC procedures must be defined in the alarm philosophy

## Tradeoffs
- Strict MOC can slow necessary operational changes
- Balance between control and agility is essential

## Related
- [[concepts/Alarm-Management-Lifecycle]]
- [[concepts/Highly-Managed-Alarm]]
- [[concepts/Alarm-Monitoring-and-Assessment]]
- [[concepts/Alarm-Philosophy]]

## Source
[[summaries/Fitzpatrick-Alarm-Lifecycle-and-Classes]]
