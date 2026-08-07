# Real Time Modifier

## Activation

Activate only when missing a deadline is a correctness failure and the critical path has explicit deterministic timing constraints.

## Required effects

Select `contracts-and-errors: safety-critical`, `performance-and-resources: hard-real-time`, and `state-and-side-effects: single-owner-mutation`. Define deadlines, worst-case work, allocation, blocking, synchronization, interrupt or callback behavior, failure states, and target-environment verification. Bound every critical-path operation.

## Prohibitions and review

Do not use mean or percentile latency as worst-case proof, allocate or block unpredictably, or introduce ownership ambiguity on the critical path. This modifier does not claim certification; external assurance requirements remain explicit constraints.
