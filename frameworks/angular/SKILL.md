# Angular Framework Adapter

## Purpose

Apply this adapter with TypeScript when Angular component, dependency, state, routing, or forms semantics
affect a change. Preserve framework-native conventions for ordinary application code.

## Standalone components and dependency injection

Prefer focused standalone components and directives with explicit imports. Introduce shared modules only
where an existing repository or packaging boundary requires them. Inputs and outputs define the component
contract; services coordinate longer-lived or shared work.

Use Angular dependency injection instead of service locators or manual global registries. Provider scope MUST
match state lifetime: root for intentionally application-wide stateless or shared services, route or feature
scope for feature lifetime, and component scope for instance-local state. Injection tokens SHOULD represent
real substitution or configuration boundaries, not ceremonial indirection.

## Signals and RxJS

Use signals for synchronous state and derivation owned by Angular rendering. Use RxJS when cancellation,
multiple asynchronous values, time, backpressure-like composition, or an existing observable API makes a
stream the natural contract. Do not mirror the same authoritative value between a signal and subscription.
Derived signals MUST remain pure; effects are reserved for synchronization with external state.

Subscriptions require explicit lifecycle ownership. Prefer template consumption or framework lifecycle
integration; otherwise bind teardown to the owning injector or component. Flattening semantics MUST match
the operation: cancellation, ordering, concurrency, and dropped work are behavior, not style.

## Forms and service boundaries

Choose template-driven forms for small local interactions and reactive forms for explicit dynamic structure,
composition, or complex validation. Client validation improves feedback but MUST NOT replace validation and
authorization at a server boundary. Map transport models to application-owned values when transport changes
must not leak through the UI.

## Review checklist

1. Are standalone components cohesive with explicit contracts and imports?
2. Does each dependency injection provider have the correct lifetime?
3. Is each state value owned once, with signals or RxJS chosen for its semantics?
4. Are subscriptions and effects cleaned up by their owning lifecycle?
5. Are forms and service boundaries explicit without duplicating server trust checks?

## Non-goals

This adapter does not mandate RxJS for every value, a global service for every state, or a private abstraction
over Angular dependency injection, forms, routing, or standalone components.
