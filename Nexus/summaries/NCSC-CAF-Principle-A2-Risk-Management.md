---
title: "Principle A2 Risk Management"
source: "https://www.ncsc.gov.uk/collection/cyber-assessment-framework/caf-objective-a-managing-security-risk/principle-a2-risk-management"
author: "NCSC"
published: "2024-04-18"
type: article
---

# NCSC CAF Principle A2 — Risk Management

## Summary
NCSC CAF Principle A2 covers risk management for network and information systems supporting essential functions across three sub-principles: A2.a Risk Management Process (identify, analyse, prioritise, manage risks), A2.b Understanding Threat (threat actor capabilities, methods, techniques), and A2.c Assurance (confidence in security effectiveness). Physical risks (hardware failure, power, fire, flood) are explicitly included alongside cyber threats.

## Core Concepts
- [[concepts/NCSC-CAF]] -- UK National Cyber Security Centre's Cyber Assessment Framework for organisations with essential functions
- [[concepts/Risk-Management-Process]] -- systematic process to identify, analyse, prioritise and manage security risks; outputs clear security requirements aligned to organisational approach
- [[concepts/Threat-Analysis]] -- understanding threat actor capabilities, methods, and techniques; developing plausible attack scenarios from threat actor perspective
- [[concepts/Security-Assurance]] -- gaining confidence in security effectiveness through validation; methods chosen, strengths/limitations understood, deficiencies remedied
- [[concepts/Physical-Risk-Management]] -- policies for physical infrastructure risks: single points of failure, hardware failure, power failure, environmental hazards (fire, flood)
- [[concepts/IT-OT-Dependency-Risk]] -- systems assessed with consideration of dependencies and interactions between IT and OT environments

## Key Insights
- "Not achieved" includes: risk assessments not based on defined threat assumptions, outputs too complex for decision-makers, one-off assessments, systems assessed in isolation, security requirements arbitrary from control catalogues, risks unresolved on registers for prolonged periods
- "Partially achieved" A2.b: understand common threats and attack methods; "Achieved": detailed analysis including capable/well-resourced threat actors, threat actor perspective analysis, plausible scenarios, step-by-step attack path mapping
- Assurance pitfalls: treating products as "silver bullets", taking vendor claims at face value, assuming security because no known problems exist
- Physical risks are explicitly in scope: hardware failure, power failure, fire, flood, physical damage — not just cyber
- Risk assessments must be triggered by significant events: system replacement, new/emergent technologies, changes in threat landscape
- IT/OT interaction is specifically called out as a common failure mode — systems assessed in isolation miss cross-environment risks

## Open Questions
- How does the NCSC expect [[concepts/Threat-Analysis]] to differ between critical infrastructure sectors (energy vs healthcare vs transport)?
- What's the expected frequency for reassessing risks under [[concepts/Risk-Management-Process]] — is it event-driven or periodic?
- How do [[concepts/Security-Assurance]] methods balance penetration testing risks in live OT environments?
