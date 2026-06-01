# High-Performance HMI

## Definition
A standardized approach to HMI graphics design that replaces poorly designed, colorful, cluttered interfaces with information-driven, operator-centered displays. Based on ISA-101 guidelines: grayscale backgrounds, color as attention-getter, simplified graphics, and hierarchical navigation.

## Why It Matters
Poorly designed HMIs have been identified as contributing factors in industrial accidents. They cause operator fatigue, poor situational awareness, and "running by the alarms" (reacting without understanding root cause). High-Performance HMI results in 48% improvement in detecting abnormal situations before alarms occur.

## Key Ideas
- **Grayscale base:** screen uses grayscale for normal state; color reserved exclusively for abnormal conditions
- **"No color = normal plant":** quick glance confirms normal operations without studying the screen
- **Information over data:** normal range indicators alongside process variables — "900 psi" becomes meaningful with context
- **Simplified graphics:** ISA-standard valve and pump symbols, no decorative elements (bulkhead fittings, flanges, 3D pipes)
- **Status colors:** dark gray = stopped, white = running, medium gray = no feedback (replaces red/green)
- **Embedded trends:** always-visible trends on important variables enable proactive adjustments
- **Standardized across vendors:** ISA-101 provides platform-independent guidelines
- **Operator reception:** operators are "eager and excited" to implement High-Performance HMI when shown the concepts

## Tradeoffs
- Migration cost: up to $10,000 per HMI page for legacy redesign
- Cultural resistance: operators accustomed to colorful legacy HMIs
- Requires training: new display hierarchy changes operator workflow

## Related
- [[concepts/Grayscale-HMI-Design]]
- [[concepts/Display-Hierarchy]]
- [[concepts/Operator-Situational-Awareness]]
- [[concepts/ISA-101-Standard]]

## Source
[[source-notes/RealPars-High-Performance-HMI]]
