# Contracts, Validation, Errors, and Security

## Purpose

Make boundary meaning, invariants, failures, and authority explicit. This Skill distinguishes untrusted
representation from validated semantic data and selects proportionate failure containment.

## Activation and inputs

Activate when data crosses a trust or component boundary, when invalid states or partial failure are possible,
or when permissions affect outcomes. Identify provenance, caller trust, consequences, recovery, public
compatibility, observability, and resource constraints.

## Decision procedure

1. Enumerate boundaries and classify data provenance and authority.
2. Define accepted semantics, invariants, and rejected ambiguity before implementation details.
3. Parse untrusted representations into a form that can represent only accepted meaning where practical.
4. Validate at provenance-changing boundaries; rely on established invariants within controlled regions.
5. Select fail-fast, contained recovery, retry, or degraded operation from consequence and recoverability.
6. Preserve error cause and actionable context without exposing sensitive data.
7. Grant only required capabilities and make privileged transitions explicit.
8. Document compatibility effects when an accepted input or error contract changes.

Static declarations alone MUST NOT be treated as runtime validation. Invalid or ambiguous input MUST NOT
silently enter trusted state.

## Modes

### `strict-boundaries`

Use by default for external and public inputs. Parse and reject invalid meaning at entry, return a stable
error contract where one exists, and prevent partially valid domain state.

### `tolerant-syntax-strict-semantics`

Accept harmless syntax variants only when they map unambiguously to one documented meaning. Conflicting,
lossy, or guessed interpretations MUST be rejected or explicitly quarantined.

### `trusted-internal-pipeline`

Validate when provenance changes and define stage contracts. Repeated defensive checks MAY be omitted inside
a controlled pipeline when construction and ownership guarantee the invariant.

### `safety-critical`

Use for high-consequence behavior. Make invariants, containment, authority, monitoring, and verification
explicit. Continuing after invariant loss requires a proven safe degraded state.

## Conflict decisions

### Tolerant input versus fail fast

- Decision: whether to accept a non-canonical representation.
- Protected qualities: interoperability and semantic correctness.
- Default: tolerate harmless syntax, reject ambiguous or invalid meaning.
- Change the resolution when compatibility evidence requires a legacy form with an explicit normalization.

### Defensive checks versus trusted invariants

- Decision: where repeated validation is required.
- Protected qualities: fault containment and comprehensibility.
- Default: validate at trust and provenance boundaries, then rely on controlled construction.
- Change the resolution when data can bypass construction or consequence warrants defense in depth.

### Fail fast versus graceful recovery

- Decision: whether processing stops, isolates failure, retries, or degrades.
- Protected qualities: integrity, availability, and diagnosability.
- Default: stop the affected operation close to the invalid condition.
- Change the resolution when a documented safe recovery preserves invariants and provides actionable evidence.

### Validation versus resource budget

- Decision: how to retain required checks on a constrained path.
- Protected qualities: safety and resource predictability.
- Default: keep semantic checks and measure their cost.
- Change the implementation, not the guarantee, when evidence supports staged parsing, bounded input, or an
  equivalent prevalidated channel.

## Outputs and review

Produce a trust-boundary map, accepted and rejected semantics, invariant ownership, error and recovery policy,
authority limits, and verification needs. Review provenance, ambiguity, partial-state prevention, cause
preservation, sensitive-data handling, and compatibility.

See [decision examples](examples/scenarios.md). Evaluations: `contracts-external-command`,
`contracts-tolerant-legacy-syntax`, and `contracts-internal-overvalidation`.

## Non-goals

This Skill does not define transport formats, exception syntax, status codes, authentication mechanisms, or
type-system features. It MUST NOT turn all internal calls into hostile boundaries or catch every failure.
