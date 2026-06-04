# LP-Measure (Link Prediction Measure)

Evaluates intrinsic graph quality by analyzing structural consistency and logical redundancy. The algorithm controllably removes a subset of relationships (triples) from the graph and mathematically evaluates whether a link prediction engine can successfully recover the removed edges based solely on the remaining network topology. Audits graph consistency without requiring a human-curated reference standard.

- Tests whether graph topology is logically coherent (missing edges should be predictable from remaining structure)
- No ground truth needed -- self-evaluating metric
- High recovery rate = high structural consistency

See also: [[concepts/Entity-Resolution]], [[concepts/KGTtm]]
