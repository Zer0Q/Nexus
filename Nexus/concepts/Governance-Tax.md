# Governance Tax

## Definition
Access control, data versioning, lineage tracking, and audit requirements that emerge as context layers scale in size and user count. Not a separate stage but a cost that compounds with scale — smaller setups can ignore it; larger ones cannot.

## Why It Matters
Governance is the differentiator between bucket 2 (institutional knowledge) and bucket 3 (systems of record) in the [[concepts/Context-Layer-Taxonomy]]. A startup automating support tickets doesn't need it; a financial services company connecting agents to CRM, warehouse, and compliance docs does. Ignoring it at scale means agents accessing data they shouldn't, acting on stale versions, or making decisions without audit trails.

## Key Ideas
- Governance is "less a stage than a tax that kicks in with scale"
- Four dimensions: access control (who can touch what), data versioning (which version is current), lineage (where did this data come from), audit (who did what and when)
- Tools that handle governance natively: Palantir Foundry (governance by design), Glean (permission-aware throughout), Atlan (policy as metadata)
- Tools that lack governance: Mem0, SQLite AI, Onyx AI — fine for bucket 1-2, insufficient for bucket 3
- The governance requirement is what pushes organizations toward full ontologies (Level 4 of the [[concepts/Context-Maturity-Spectrum]])

## Tradeoffs
- Governance adds complexity and maintenance overhead
- Lightweight tools (bucket 1-2) are faster to deploy but hit a ceiling
- Enterprise tools (bucket 3) solve governance but require significant investment

## Related
- [[concepts/Context-Layer-Taxonomy]]
- [[concepts/Context-Maturity-Spectrum]]
- [[concepts/Enterprise-Context-Layer]]
- [[concepts/Context-Graph-RAG]]

## Source
[[summaries/BouBalust-Context-Layer-Landscape]]
