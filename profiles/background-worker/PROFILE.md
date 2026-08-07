# Background Worker Profile

## Purpose

Use for scheduled, polled, or delivered jobs outside a synchronous request lifecycle. Delivery, acknowledgement, concurrency, shutdown, and retry semantics dominate.

## Priority and defaults

Correctness, reliability, and data integrity precede operability, performance, and maintainability.

| Core Skill | Mode | Rationale |
| --- | --- | --- |
| `code-clarity` | `explicit-critical-path` | Show job lifecycle and acknowledgement. |
| `contracts-and-errors` | `strict-boundaries` | Parse job payloads and authority at ingress. |
| `state-and-side-effects` | `single-owner-mutation` | Coordinate effect and acknowledgement ownership. |
| `dependencies-and-boundaries` | `framework-native` | Preserve the worker runtime lifecycle. |
| `performance-and-resources` | `budget-constrained` | Bound concurrency, queues, and job resources. |
| `distributed-reliability` | `idempotent-ingress` | Make redelivery safe. |
| `testing-strategy` | `integration-balanced` | Exercise retries, cancellation, and handoff. |
| `safe-change` | `local-safe-change` | Preserve in-flight and persisted job behavior. |

## Policy

Acknowledgement MUST prove the required durable effect or handoff. Retries MUST be bounded and safe for duplicate execution. Concurrency MUST respect downstream and local budgets. Shutdown MUST stop intake, bound draining, and leave each job either safely acknowledged or available for recovery.

Common modifiers are `high-throughput`, `memory-sensitive`, and `security-sensitive`. This profile does not prescribe a queue, scheduler, or worker pool.
