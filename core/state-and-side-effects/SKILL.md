# State and Side Effects

## Purpose

Make state ownership, mutation, effect order, and consistency visible. Every consequential writable value MUST have an authoritative owner, and queries MUST NOT conceal externally significant commands.

## Decision procedure

1. Inventory durable, shared, derived, cached, and transient state.
2. Assign authoritative ownership and list legitimate writers and readers.
3. Define invariants and transitions before choosing mutation mechanics.
4. Separate calculation from external effects where that makes sequencing testable.
5. Choose the least restrictive mode that prevents races, divergence, and invalid intermediate state.
6. Define atomicity, cancellation, rollback, and observation points.
7. Remove duplicated writable sources or specify synchronization and conflict policy.

## Modes

### `pragmatic-mutable`

Mutation MAY be used inside a clear owner with enforced invariants. Hidden shared mutation and effectful queries are prohibited.

### `immutable-core`

Represent core transitions as new values and execute effects at boundaries. Copying costs remain subject to measurement.

### `localized-state`

Keep state at the narrowest scope that contains all coordinating consumers. Derived values SHOULD be computed rather than stored as another writable truth.

### `single-owner-mutation`

Route consequential transitions through one owner and explicit commands. Other components observe results or request transitions rather than mutating storage directly.

### `cqrs-event-driven`

Separate command and read models only for verified independent scaling, modeling, or consistency needs. Projection lag, ordering, replay, and repair MUST be specified.

## Conflict decisions

- Immutability versus resource cost: start with safe value semantics; allow bounded local mutation when measurement and ownership support it.
- Local convenience versus one truth: do not create a second writer merely to simplify one consumer.
- CQRS versus simplicity: require a concrete asymmetry or consistency need before accepting dual-model cost.

## Outputs and review

Produce a state inventory, ownership map, transition rules, effect sequence, atomicity boundary, and consistency policy. Review hidden writes, duplicate truth, races, cancellation, and invalid intermediate states.

See [decision examples](examples/scenarios.md). Evaluations: `state-localized-ui`, `state-single-owner-effects`, and `state-cqrs-overengineering`.

## Non-goals

This Skill does not mandate functional programming, event sourcing, CQRS, global immutability, or a particular state library.
