# Data Pipeline Profile

## Purpose

Use when ingestion, staged transformation, validation, and publication of data dominate. Data meaning, provenance, restartability, and bounded resources are correctness concerns.

## Priority and defaults

Data integrity and correctness precede reliability, performance, maintainability, and operability.

| Core Skill | Mode | Rationale |
| --- | --- | --- |
| `code-clarity` | `explicit-critical-path` | Expose stage and failure behavior. |
| `modular-design` | `data-oriented` | Organize around transformations and data ownership. |
| `contracts-and-errors` | `trusted-internal-pipeline` | Validate provenance changes, then rely on stage invariants. |
| `state-and-side-effects` | `single-owner-mutation` | Give checkpoints and outputs an owner. |
| `performance-and-resources` | `budget-constrained` | Bound memory, buffering, and throughput work. |
| `distributed-reliability` | `idempotent-ingress` | Make restarts and redelivery safe. |
| `testing-strategy` | `integration-balanced` | Verify stage contracts and representative data. |
| `safe-change` | `local-safe-change` | Bound schema and transformation changes. |

## Policy

Each stage MUST define input meaning, output meaning, provenance, invalid-data handling, and replay behavior. Checkpoints MUST correspond to durable output guarantees. Large or uncertain input MUST use bounded processing and backpressure. Schema evolution requires downstream compatibility analysis and observable quarantine or failure.

Common modifiers are `memory-sensitive`, `high-throughput`, and `strict-backward-compatibility`. This profile does not select an engine, storage system, or file format.
