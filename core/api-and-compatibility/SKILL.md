# API and Compatibility

## Purpose

Define what consumers may rely on and how that contract evolves. Compatibility covers documented behavior and materially observable semantics, not only signatures.

## Decision procedure

1. Identify consumers, upgrade independence, exposure, and architecture authority.
2. Enumerate supported names, data, errors, ordering, timing, side effects, and ownership rules.
3. Separate intentional promises from internals and accidental observations.
4. Classify each proposed change as compatible, conditionally compatible, or breaking for each consumer class.
5. Prefer additive evolution where it remains understandable and safe.
6. For a break, choose versioning, deprecation, negotiation, or coordinated migration with an exit condition.
7. Verify old and new behavior over the declared support window.

## Modes

### `internal-application`

Internal contracts MAY change atomically with their callers. Externally observable product behavior still requires compatibility analysis.

### `public-library`

Keep exports and supported behavior small and documented. Independent consumers MUST receive semantic versioning and migration treatment appropriate to the compatibility impact.

### `external-api`

Treat request, response, error, authorization, idempotency, and deprecation behavior as contract. Silent semantic repurposing is prohibited.

### `stable-abi`

Include binary layout, calling convention, ownership, allocation, and toolchain constraints in the promise. Source compatibility MUST NOT be assumed to prove ABI compatibility.

## Conflict decisions

- Cleanup versus compatibility: keep translation inside the boundary or provide a migration; do not export current internals merely for neatness.
- Strictness versus legacy acceptance: preserve evidenced supported semantics, normalize harmless representation, and reject ambiguity.
- Performance versus contract: optimize implementation while retaining semantics, or make the contract change explicit and versioned.

## Outputs and review

Produce the public surface, consumer classes, compatibility matrix, version impact, deprecation window, migration path, and removal criteria. Review observable behavior beyond signatures and identify accidental dependencies using evidence.

See [decision examples](examples/scenarios.md). Evaluations: `api-internal-atomic-change`, `api-public-deprecation`, and `api-accidental-surface`.

## Non-goals

This Skill does not freeze all behavior, promise compatibility for undocumented internals, or use version numbers as a substitute for contract documentation.
