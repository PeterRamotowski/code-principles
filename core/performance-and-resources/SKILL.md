# Performance and Resource Efficiency

## Purpose

Meet explicit latency, throughput, memory, allocation, energy, or timing needs with representative evidence. Optimization MUST protect correctness and MUST name the budget it serves.

## Decision procedure

1. Translate the need into an end-to-end metric, percentile or worst case, workload, and limit.
2. Establish a reproducible baseline with representative data and environment.
3. Locate the dominant critical path or resource source.
4. Correct algorithmic and unbounded behavior before low-level tuning.
5. Make the smallest change likely to meet the budget.
6. Measure the whole target again and check correctness and other resources.
7. Document retained complexity, assumptions, guardrails, and rollback criteria.

## Modes

### `clarity-first`

Implement clear correct behavior and instrument material risks. Speculative caches, pools, batching, and concurrency are prohibited.

### `budget-constrained`

Define measurable budgets and enforce bounded queues, buffers, fan-out, and work. Proxy metrics MUST connect to the end-to-end requirement.

### `hot-path-optimized`

Optimize a measured critical path and contain specialized code behind a clear boundary. Benchmarks MUST resemble the target workload.

### `hard-real-time`

Use worst-case bounds for execution, blocking, allocation, and resource access on critical paths. Average and percentile latency are insufficient evidence.

## Conflict decisions

- Clarity versus speed: retain clarity by default; isolate and explain measured necessary complexity.
- Validation versus timing: preserve semantic guarantees and change algorithms, staging, or prevalidation channels.
- Throughput versus memory: bound buffering and apply backpressure rather than trading one unbounded resource for another.

## Outputs and review

Produce budgets, workloads, baseline, bottleneck evidence, chosen change, post-change result, correctness checks, and operational guardrails. Review tail or worst-case behavior, queue growth, caching invalidation, and benchmark representativeness.

See [decision examples](examples/scenarios.md). Evaluations: `performance-clarity-first`, `performance-bounded-pipeline`, and `performance-speculative-cache`.

## Non-goals

This Skill does not require optimization everywhere, treat microbenchmarks as product evidence, or weaken safety because a path is called hot.
