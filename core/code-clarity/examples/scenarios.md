# Code Clarity Decision Examples

## Positive example — visible critical behavior

- Context: a consequential workflow applies eligibility rules and records a state transition.
- Mode: `explicit-critical-path`.
- Decision: name each eligibility result, keep the transition and audit action visible, and return distinct
  failure outcomes.
- Why it fits: the reader can trace decisions and effects without knowing hidden conventions.
- Rejected alternative: compress the workflow into a chained expression with implicit defaults.

## Negative example — extraction by size

- Context: a balanced local change touches one cohesive operation.
- Mode: `balanced`.
- Bad decision: split every few lines into generic helpers to satisfy a size target.
- Why it fails: navigation increases while names add no domain meaning or independent reuse.
- Better decision: extract only coherent named operations and leave short connective flow together.
