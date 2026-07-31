# Safe Change Decision Examples

## Positive example — compatible seam migration

- Context: a long-lived contract needs a replacement and consumers migrate independently.
- Mode: `compatibility-first`.
- Decision: introduce the new contract additively, observe adoption, migrate consumers, then remove the old
  path under explicit criteria.
- Why it fits: intermediate states remain operable and rollback is possible.
- Rejected alternative: replace the contract in one deployment because the new shape is cleaner.

## Negative example — cleanup-led rewrite

- Context: a production defect is isolated to one unfamiliar subsystem.
- Mode: `local-safe-change`.
- Bad decision: reorganize the subsystem and replace its abstractions before applying the fix.
- Why it fails: behavior, review, and rollback risks expand without being required by the outcome.
- Better decision: characterize the failing behavior, apply a bounded fix, and propose broader work separately.
