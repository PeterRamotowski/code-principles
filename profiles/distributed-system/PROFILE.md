# Distributed System Profile

## Purpose

Use when correctness depends on multiple independently failing processes. Ownership, delivery, ordering, staleness, convergence, and repair MUST be explicit.

## Priority and defaults

Correctness, reliability, and data integrity precede operability, security, and performance.

| Core Skill | Mode | Rationale |
| --- | --- | --- |
| `code-clarity` | `explicit-critical-path` | Make failure and consistency paths visible. |
| `modular-design` | `service-oriented` | Align independently operated ownership. |
| `contracts-and-errors` | `strict-boundaries` | Treat every remote boundary as untrusted. |
| `dependencies-and-boundaries` | `component-based` | Define provided and required component contracts. |
| `state-and-side-effects` | `cqrs-event-driven` | Make command ownership and projections explicit where justified. |
| `distributed-reliability` | `eventually-consistent` | Define convergence and repair. |
| `performance-and-resources` | `budget-constrained` | Bound fan-out, retries, queues, and timeouts. |
| `testing-strategy` | `integration-balanced` | Exercise failures and cross-component contracts. |

## Policy

Every fact MUST have an authoritative owner. Delivery and acknowledgement semantics, duplicate handling, ordering scope, staleness, conflict resolution, convergence, and repair MUST be documented. Retries and failover MUST be bounded. Distribution requires independent lifecycle or failure evidence; it is not a modularity shortcut.

Common modifiers are `security-sensitive`, `high-throughput`, `latency-sensitive`, and `multi-tenant`. This profile does not mandate microservices, messaging, event sourcing, or CQRS.
