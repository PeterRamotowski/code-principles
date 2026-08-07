# Distributed Reliability Decision Examples

## Positive example — idempotent ingress

- Context: a sender may repeat a command after losing the acknowledgement.
- Mode: `idempotent-ingress`.
- Decision: use a stable operation key and atomically record the accepted effect and result.
- Why it fits: redelivery cannot duplicate the consequential effect.

## Negative example — unbounded retry

- Context: a remote operation has unknown duplicate semantics and persistent failures.
- Mode: `synchronous-transactional`.
- Bad decision: retry forever with increasing queues.
- Better decision: bound attempts, expose failure, and establish effect semantics before retrying.
