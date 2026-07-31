# Modular and Object Design

## Purpose

Assign responsibilities and information boundaries so related behavior changes together and collaborators
depend on the smallest stable knowledge they need. This Skill supports object, functional, procedural, and
data-oriented designs without privileging one paradigm.

## Activation and inputs

Activate when module, package, service, component, object, or data ownership changes. Use the artifact type,
domain complexity, change drivers, consumer relationships, deployment constraints, existing architecture,
and authority to restructure.

## Decision procedure

1. Identify capabilities, invariants, state ownership, change drivers, and consumers.
2. Keep behavior and data together when they enforce one concept or invariant.
3. Separate responsibilities when they change for different reasons or cross a material boundary.
4. Hide volatile decisions behind focused contracts; expose only what consumers need.
5. Prefer composition and direct collaboration unless substitutability is a real contract.
6. Evaluate coupling by required knowledge and coordinated change, not only dependency count.
7. Retain established boundaries for local tasks unless evidence and authority justify movement.

Every new boundary MUST have a concrete responsibility, consumer, or protected quality. The Skill MUST NOT
infer services, objects, layers, or inheritance from terminology alone.

## Modes

### `feature-oriented`

Group behavior around coherent user or business capabilities. Keep feature-local data and operations close,
extracting shared policy only where ownership is genuinely shared.

### `domain-oriented`

Center boundaries on domain concepts and invariants when business rules are dense. Keep infrastructure
details from defining domain ownership, but do not manufacture domain layers for simple transformations.

### `service-oriented`

Define explicit capability and contract ownership for independently operated units. A service boundary MUST
be supported by deployment, ownership, scaling, isolation, or integration evidence.

### `data-oriented`

Organize around data ownership and transformation stages when flow is clearer than collaborating objects.
Make mutation, provenance, and stage contracts visible.

### `library-oriented`

Minimize consumer dependencies and expose focused stable contracts. Package together what consumers reuse
together and hide volatile implementation choices.

## Conflict decisions

### Locality versus separation of concerns

- Decision: whether related behavior stays together or moves behind a separate boundary.
- Protected qualities: discoverability and independent change.
- Default: keep behavior local when it serves one concept.
- Change the resolution when responsibilities have distinct change drivers, privileges, or lifecycles.

### Common closure versus common reuse

- Decision: whether packaging follows coordinated maintenance or consumer dependency sets.
- Protected qualities: change containment and minimal consumer coupling.
- Default: application code groups cohesive change; reusable boundaries prioritize consumer needs.
- Change the resolution when release and consumption evidence favors the other axis.

### Composition versus inheritance

- Decision: how variable behavior is assembled.
- Protected qualities: substitutability, reuse, and coupling control.
- Default: use composition or direct functions.
- Change the resolution when a stable behavioral subtype contract exists and consumers rely on substitution.

### Encapsulation versus direct data flow

- Decision: whether state requires a behavior-owning abstraction.
- Protected qualities: invariant safety and transparent transformation.
- Default: encapsulate state with meaningful invariants; use direct data flow for transparent transformations.
- Change the resolution when mutation authority or lifecycle complexity makes one model materially safer.

## Outputs and review

Produce a responsibility map, selected mode, boundary rationale, public collaborations, state ownership, and
rejected decompositions. Review cohesion, consumer knowledge, invariant ownership, change coupling, and
whether every boundary earns its cost.

See [decision examples](examples/scenarios.md). Evaluations: `modular-feature-cohesion`,
`modular-library-consumers`, and `modular-service-splitting`.

## Non-goals

This Skill MUST NOT require classes, layers, domain-driven design, microservices, dependency injection, or
one directory organization. It does not select runtime topology from project size or implementation language.
