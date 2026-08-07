# Latency Sensitive Modifier

## Activation

Activate when a verified response deadline or latency percentile affects correctness, usability, or a service objective.

## Required effects

Select `performance-and-resources: budget-constrained`. Define the end-to-end operation, percentile or maximum, workload, concurrency, and saturation limit. Measure critical-path contributions and bound fan-out, queues, retries, blocking, and remote calls. Preserve cancellation and overload behavior.

## Prohibitions and review

Do not optimize averages when tail behavior matters or move work to an unbounded asynchronous queue and declare success. When `high-throughput` is active, document batching and concurrency trade-offs and test both budgets together.
