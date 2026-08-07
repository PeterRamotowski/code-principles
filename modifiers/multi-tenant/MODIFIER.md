# Multi-tenant Modifier

## Activation

Activate when separate security principals share execution, storage, caches, queues, credentials, or operational infrastructure.

## Required effects

Select `contracts-and-errors: safety-critical` and `state-and-side-effects: single-owner-mutation`. Derive tenant identity from an authoritative context and propagate it through every data and effect boundary. Enforce tenant-scoped authorization, storage, caches, jobs, rate limits, observability, support access, export, deletion, and recovery. Define noisy-neighbor budgets.

## Prohibitions and review

Do not trust caller-selected tenant identifiers or use unscoped queries, cache keys, queues, logs, or administrative paths. Review cross-tenant failure and operational workflows as well as ordinary requests.
