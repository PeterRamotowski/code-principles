# Testing Strategy Decision Examples

## Positive example — risk-aligned levels

- Context: a workflow has pure decision logic plus a persistent boundary.
- Mode: `integration-balanced`.
- Decision: test decision outcomes at a focused public boundary and add integration evidence for persistence
  mapping and transaction behavior.
- Why it fits: each credible risk is tested at the narrowest boundary that can expose it.
- Rejected alternative: verify every outcome through a broad end-to-end environment.

## Negative example — private-structure lock-in

- Context: a refactor preserves the public behavior of a reusable component.
- Mode: `unit-focused`.
- Bad decision: assert private helper calls, internal fields, and exact collaboration order.
- Why it fails: tests reject safe restructuring without improving contract evidence.
- Better decision: assert observable outputs, errors, and documented side effects.
