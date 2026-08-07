# Distributed Reliability

## Purpose

Make partial failure, delivery, duplication, ordering, timeout, and convergence explicit whenever work crosses a failure boundary. A retry MUST NOT be added until the effect of duplicate execution is known.

## Decision procedure

1. Identify failure boundaries, authoritative owners, operations, and externally visible effects.
2. State delivery semantics and what acknowledgement proves.
3. Define stable operation identity and duplicate handling where redelivery is possible.
4. Bound timeouts, retries, queues, fan-out, and retention.
5. Define ordering scope, stale-read expectations, conflicts, convergence, and repair.
6. Preserve durable handoff between local state and remote effects where required.
7. Provide observability that can distinguish delay, duplication, rejection, and loss.
8. Exercise recovery from interruption at every consequential boundary.

## Modes

### `synchronous-transactional`

Prefer one bounded request and local transaction when it meets the actual failure model. Do not add asynchronous delivery for hypothetical scale.

### `idempotent-ingress`

Accept duplicate delivery safely using durable identity and atomic effect recording. A check followed by an unguarded effect is not idempotency.

### `eventually-consistent`

Define authoritative state, ordering scope, staleness, merge or conflict rules, convergence, and repair. Immediate consistency MUST NOT be implied.

### `high-reliability`

Add durable handoff, containment, bounded failover, recovery evidence, and service-level observability from an explicit failure model.

## Conflict decisions

- Retry versus duplication: retry only when the operation is idempotent, deduplicated atomically, or explicitly compensatable.
- Availability versus consistency: document the degraded behavior, authoritative owner, and repair path rather than claiming both without trade-offs.
- Reliability versus simplicity: use the simplest mechanism that satisfies the verified failure and recovery targets.

## Outputs and review

Produce a failure model, ownership map, delivery and acknowledgement semantics, retry policy, ordering and convergence rules, repair procedure, and observability signals.

See [decision examples](examples/scenarios.md). Evaluations: `reliability-local-transaction`, `reliability-idempotent-webhook`, and `reliability-unbounded-retry`.

## Non-goals

This Skill does not promise exactly-once execution, prescribe messaging, or require distribution where a local transaction suffices.
