# React Framework Adapter

## Purpose

Apply this adapter after the project profile and JavaScript adapter when React semantics affect a change.
React refines UI composition and lifecycle policy; it does not define TypeScript typing rules.

## Components and composition

- A component SHOULD own one cohesive user-facing responsibility. Split it when independent behavior,
  lifecycle, or reuse makes the boundary clearer, not merely because its line count grew.
- Prefer composition of components, children, and focused hooks to inheritance or configuration-heavy
  universal components. Preserve existing framework conventions for ordinary application code.
- Keep state at the lowest common owner that needs to coordinate it. Lift or externalize state only when
  multiple consumers, persistence, navigation, or a longer lifetime demonstrates the need.
- Use stable keys that identify domain items. Array position MUST NOT identify reorderable or mutable data.

## Rendering, state locality, and effects

Rendering MUST remain pure: do not mutate external state, perform I/O, or rely on render count. Derive values
during rendering when they are a pure function of props and state; do not mirror them into state.

Effects synchronize a committed tree with an external system. Each effect SHOULD declare the complete
reactive inputs it uses and return cleanup when it acquires subscriptions, timers, or resources. Event-driven
work belongs in the event path, not in an effect that observes an intermediate flag. Effects MUST tolerate
restart and cleanup behavior in development and concurrent rendering.

## Boundaries and testing

Context is appropriate for stable subtree-wide dependencies, not as a default global store. Custom hooks
SHOULD package cohesive reusable behavior while leaving UI composition visible. Error boundaries MAY isolate
rendering failures but do not replace explicit handling of event and asynchronous failures.

Behavior-focused tests SHOULD exercise accessible roles, labels, user actions, and visible outcomes. Avoid
asserting hook call order, private state, or component structure unless that structure is itself a contract.

## Review checklist

1. Is component responsibility cohesive and composition simpler than added configuration?
2. Is each state value authoritative, local to its owner, and not derivable?
3. Does every effect synchronize an external system with complete cleanup and dependencies?
4. Do list keys preserve identity through insertion and reordering?
5. Do tests observe user behavior rather than implementation details?

## Non-goals

This adapter does not select a router, state library, styling system, or testing tool. It does not restate
JavaScript behavior or establish TypeScript typing rules.
