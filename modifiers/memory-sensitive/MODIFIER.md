# Memory Sensitive Modifier

## Activation

Activate for large or unbounded inputs, constrained devices or processes, high allocation pressure, or an explicit memory ceiling.

## Required effects

Select `performance-and-resources: budget-constrained`. Define peak, steady-state, and per-unit budgets. Stream or chunk uncertain inputs, bound buffers and queues, make ownership and lifetimes explicit, and give every cache an accounting, eviction, and invalidation policy. Measure representative worst cases.

## Prohibitions and review

Do not materialize unbounded inputs, retain duplicate representations without evidence, or use a cache without a bound. Avoid trading memory savings for uncontrolled I/O or latency; verify all active resource budgets together.
