# Abstraction and Reuse

## Purpose

Decide when knowledge should have one owner, when similar code should remain separate, and when a verified
variation deserves an extension point. The aim is independent changeability with proportionate complexity,
not maximum deduplication.

## Activation and inputs

Activate for proposed helpers, shared modules, generalized workflows, extension points, reuse boundaries, or
duplicated policy. Inspect concept ownership, consumers, change history, known near-term variation, public
exposure, compatibility, and architecture authority.

## Decision procedure

1. Identify what is repeated: authoritative knowledge, representation, control shape, or coincidence.
2. Establish whether instances represent the same concept and should change together.
3. Name the present consumers and verified variation; unknown future consumers do not count as evidence.
4. Compare the coupling created by an abstraction with the divergence risk of repetition.
5. Choose the smallest interface that represents current commonality without erasing meaningful differences.
6. For public extension points, define the supported contract, stability promise, and failure behavior.
7. Prefer a reversible concrete implementation when evidence is incomplete.

The Skill MUST centralize duplicated authoritative policy that can diverge. It MUST NOT merge independently
changing concepts merely because their current syntax is similar.

## Modes

### `conservative`

Default when context is uncertain or the task is local. Require demonstrated shared knowledge and common
change before extraction. One current implementation is not evidence for a generic capability.

### `balanced`

Centralize stable knowledge and repeated decisions while preserving local representations and independent
change. Prefer small purpose-named abstractions over generic parameter surfaces.

### `extensible-public-library`

Use for an intentional public reuse boundary. Verified consumer variation MAY justify a stable extension
seam, but the public surface MUST stay minimal and documented. Internal mechanisms are not extension contracts.

### `legacy-preservation`

Preserve existing behavior and seams until characterization and history explain them. Consolidation SHOULD
proceed incrementally with rollback and compatibility evidence.

## Conflict decisions

### DRY versus YAGNI

- Decision: whether repetition warrants an abstraction now.
- Protected qualities: consistency, simplicity, and independent change.
- Default: centralize duplicated knowledge; tolerate duplicated shape until common change is demonstrated.
- Change the resolution when the same rule already diverges or a verified second consumer needs it.

### Open/Closed versus simple modification

- Decision: whether to add an extension mechanism or edit concrete code.
- Protected qualities: stability and present-day comprehensibility.
- Default: make the direct change for one bounded requirement.
- Change the resolution when a stable variation axis, public consumer contract, or repeated independent
  extension is observed.

### Reuse versus locality

- Decision: whether to move behavior into shared infrastructure.
- Protected qualities: discoverability, cohesion, and reuse.
- Default: keep feature-specific behavior local.
- Change the resolution when the shared concept has one authoritative owner and consumer-oriented boundaries.

### Generalization versus legacy preservation

- Decision: whether to replace irregular existing paths with one generalized path.
- Protected qualities: behavioral compatibility and maintainability.
- Default: characterize and preserve before consolidation.
- Change the resolution when differences are proven accidental, consumers are known, and migration is reversible.

## Outputs and review

Produce knowledge ownership, the abstraction or non-abstraction decision, consumer and variation evidence,
the supported extension policy, and suppressed speculative behavior. Review whether concepts change together,
whether parameters encode real variation, and whether coupling and reversibility are explicit.

See [decision examples](examples/scenarios.md). Evaluations:
`abstraction-shared-policy`, `abstraction-public-variation`, and `abstraction-similarity-trap`.

## Non-goals

This Skill MUST NOT require a fixed duplication count, universal utilities, dependency injection, plugin
systems, or configuration for hypothetical needs. It does not decide module deployment or API versioning.
