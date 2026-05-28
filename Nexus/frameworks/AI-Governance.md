---
created: 2026-05-28
type: framework
tags:
  - ai
  - governance
  - standards
  - iso
---

# AI Governance

AI Governance establishes the shared language, frameworks, and accountability structures for managing AI systems. ISO/IEC 22989:2022 provides the foundational terminology.

## Key Principles
- **Shared Vocabulary** -- "Babel Syndrome" (lack of common AI terms) is a compliance and security risk
- **Human-Defined Objectives** -- AI systems must have objectives defined by the business, not the model
- **Trustworthiness** -- decomposed into Robustness, Explainability, Transparency

## Governance Ecosystem
| Standard | Role |
|---|---|
| ISO/IEC 22989:2022 | Foundational terminology and AI lifecycle model |
| ISO/IEC 23894:2023 | Risk management engine |
| ISO/IEC 42001 | AI Management System (AIMS) |
| ISO/IEC 38507 | Board-level governance guidance |

## AI vs Traditional SDLC
| Feature | Traditional SDLC | AI System Lifecycle |
|---|---|---|
| Logic Origin | Human-written code | Learned from data |
| Performance | Stable until code change | Dynamic (model drift) |
| Validation | Functional testing | Continuous V&V |
| Governance | Version control | Bias detection, ethical alignment |
| Retirement | Hardware/OS end-of-life | Performance degradation or ethical thresholds |

## Related
- [[AI-Risk-Management]] -- risk framework operationalizing governance vocabulary
- [[AI-System-Life-Cycle]] -- lifecycle stages for accountability
- [[Trustworthiness]] -- verifiable AI characteristics

## Sources
- [[RamiroCid-ISO-22989-AI-Governance]]
