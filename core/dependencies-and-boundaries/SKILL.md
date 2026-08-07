# Dependencies and Architecture Boundaries

## Purpose

Control dependency direction and place boundaries where ownership, volatility, or independent evolution justifies them. Boundaries MUST protect a named policy or lifecycle; indirection is not a goal.

## Decision procedure

1. Identify policy, mechanisms, owners, consumers, and independently changing parts.
2. Draw current compile-time and runtime dependencies and find cycles or ownership leaks.
3. Select the least elaborate mode that preserves required independence.
4. Point dependencies toward the more stable policy when a real boundary exists.
5. Define provided and required contracts from the consumer's needs.
6. Keep construction and integration details at the edge of the boundary.
7. Verify the result can be changed, tested, deployed, or versioned in the way used to justify it.

Dependency inversion MUST NOT mean an interface for every class. A framework type MAY remain in ordinary application code when it does not contaminate independently evolving policy.

## Modes

### `framework-native`

Follow native lifecycle and composition conventions. Isolate volatile integrations or independently tested policy, not stable framework facilities used directly by application code.

### `modular-monolith`

Keep one deployable while enforcing cohesive ownership, explicit module APIs, and an acyclic dependency graph. A module MUST NOT reach through another module to mutate its storage.

### `domain-centric`

Keep domain policy independent of delivery, persistence, and infrastructure. Ports MUST express domain needs; they MUST NOT become generic wrappers around every mechanism.

### `component-based`

Use explicit provided and required contracts for independently built or versioned components. Shared internals MUST NOT serve as an undocumented integration surface.

## Conflict decisions

- Simplicity versus isolation: keep direct dependencies unless volatility, ownership, testing, or lifecycle evidence requires isolation.
- Reuse versus ownership: boundary contracts follow consumer and owner needs, not coincidental shared code.
- Performance versus indirection: measure the actual boundary cost before weakening it; document any critical-path exception.

## Outputs and review

Produce a dependency map, ownership boundaries, allowed dependency directions, contracts, construction policy, and evidence for each nontrivial boundary. Review cycles, leaked mechanism types, bypass paths, and unsupported extension points.

See [decision examples](examples/scenarios.md). Evaluations: `dependencies-framework-native`, `dependencies-domain-boundary`, and `dependencies-interface-overengineering`.

## Non-goals

This Skill does not prescribe layers, services, repositories, dependency-injection containers, or a universal architecture.
