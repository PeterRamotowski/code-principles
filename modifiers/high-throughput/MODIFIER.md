# High Throughput Modifier

## Activation

Activate only from a verified sustained or burst throughput target or overload requirement, not anticipated popularity.

## Required effects

Select `performance-and-resources: budget-constrained`. Define representative workload, units, duration, saturation behavior, and acceptable resource cost. Bound queues, concurrency, fan-out, batches, and retries. Apply backpressure or admission control and measure end-to-end completed useful work.

## Prohibitions and review

Do not hide overload with unbounded buffering or optimize a synthetic operation unrelated to the system target. When `latency-sensitive` is also active, record the throughput/latency trade-off and verify both budgets under saturation.
