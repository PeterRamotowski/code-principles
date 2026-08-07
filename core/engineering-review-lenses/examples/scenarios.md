# Engineering Review Lens Examples

## Positive example — evidence-bearing architecture review

- Context: a redesign changes ownership and a widely observed response shape.
- Mode: `architecture-review`.
- Decision: inspect consumer telemetry, failure history, incremental migration, and ownership before choosing the boundary.
- Why it fits: each lens changes a decision or verification step.

## Negative example — slogan theater

- Context: a local helper rename has no systemic effect.
- Mode: `lightweight`.
- Bad decision: reject it by citing multiple named laws without evidence.
- Better decision: review the local compatibility and clarity impact directly.
