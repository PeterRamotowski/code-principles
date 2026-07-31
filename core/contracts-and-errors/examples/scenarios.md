# Contracts and Errors Decision Examples

## Positive example — semantic boundary parsing

- Context: an external command contains identifiers, quantities, and an optional timestamp.
- Mode: `strict-boundaries`.
- Decision: parse it once into validated semantic values, reject ambiguity, and expose a stable failure result.
- Why it fits: trusted code cannot receive a partial invalid command.
- Rejected alternative: pass a loosely checked representation through multiple layers.

## Negative example — indiscriminate defensiveness

- Context: controlled pipeline stages exchange values created only by a validated constructor.
- Mode: `trusted-internal-pipeline`.
- Bad decision: reparse and catch every possible failure at every local handoff.
- Why it fails: duplicated checks obscure invariant ownership and can conceal programming errors.
- Better decision: validate provenance changes and fail visibly if an internal invariant is violated.
