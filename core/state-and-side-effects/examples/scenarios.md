# State and Side-Effect Decision Examples

## Positive example — owned transition and effect

- Context: one operation updates durable state and schedules an external notification.
- Mode: `single-owner-mutation`.
- Decision: one owner validates and commits the transition, then records the notification handoff explicitly.
- Why it fits: mutation and effect ordering have one accountable owner.

## Negative example — speculative CQRS

- Context: one process maintains a small record with identical read and write needs.
- Mode: `pragmatic-mutable`.
- Bad decision: add command buses, events, projections, and eventual consistency.
- Better decision: keep one model and explicit local transitions.
