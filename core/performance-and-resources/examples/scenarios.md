# Performance and Resource Decision Examples

## Positive example — bounded measured pipeline

- Context: large inputs exceed a verified memory limit.
- Mode: `budget-constrained`.
- Decision: measure peak memory, process bounded chunks, apply backpressure, and verify throughput and correctness.
- Why it fits: the implementation directly serves stated budgets.

## Negative example — speculative cache

- Context: no latency target or measurement identifies repeated expensive work.
- Mode: `clarity-first`.
- Bad decision: add a shared cache with invalidation and synchronization complexity.
- Better decision: keep clear computation and instrument it if performance becomes material.
