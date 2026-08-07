# Engineering Review Lenses

## Purpose

Use broad laws and umbrella concepts to ask concrete questions about change, failure, consumers, evolution, and organizations. A named lens MUST produce evidence, a risk, or a reconsideration trigger; it MUST NOT decide by slogan.

## Decision procedure

1. State the decision, scope, authority, and protected qualities.
2. Select only lenses with a plausible causal relationship to that decision.
3. Convert each lens into a falsifiable question.
4. Gather repository, operational, consumer, historical, and organizational evidence.
5. Record the risk, decision impact, and uncertainty separately.
6. Assign mitigation or a reconsideration trigger to material risks.
7. Remove lens observations that do not change the decision or verification.

## Modes

### `lightweight`

Ask what can fail, why the current structure exists, and whether the change adds unnecessary scope. Keep the result proportional to a local decision.

### `architecture-review`

Examine incremental evolution, accidental consumer contracts, failure modes, operational simplicity, and the evidence behind claimed qualities.

### `organizational-review`

Examine ownership, communication paths, coordination load, staffing transitions, and feedback. Organization structure informs risk but MUST NOT automatically dictate architecture.

## Conflict decisions

- Historical caution versus improvement: investigate purpose and current consequence, then preserve, migrate, or remove explicitly.
- Ecosystem observation versus intentional API: assess real reliance without declaring every observable detail permanently supported.
- Organizational fit versus technical cohesion: surface misalignment and choose ownership and interfaces from both causal and domain evidence.

## Outputs and review

Produce scoped questions, evidence, systemic risks, decision impacts, mitigations, uncertainties, and reconsideration triggers. Review for slogans, unfalsifiable claims, duplicated Core Skill decisions, and analysis that does not affect action.

See [decision examples](examples/scenarios.md). Evaluations: `review-lightweight-change`, `review-architecture-evolution`, and `review-slogan-theater`.

## Non-goals

This Skill does not replace specialist review, make umbrella concepts enforceable checklists, or infer causation from a law's name.
