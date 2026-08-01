# Go Language Adapter

## Purpose

Apply this adapter after the selected project profile and Core Skill modes when Go is materially involved.
It translates policy into consumer-defined interfaces, explicit error values, context propagation, goroutine
lifecycle, state coordination, package visibility, and evidence-based allocation decisions.

## Consumer-defined small interfaces

Accept interfaces and return concrete values by default, but introduce an interface only where a consumer
needs substitution, isolation, or multiple implementations. Define that interface in or near the consuming
package so it contains only the operations the consumer uses. A one-method function type may be clearer than
an interface for one behavior.

Do not publish a broad provider interface merely because a concrete type has many methods. Small interfaces
reduce coupling, but splitting a coherent consumer contract into fragments can obscure required invariants.
Compile-time satisfaction is structural and does not prove behavioral substitutability.

## Explicit error values

Return errors when an operation cannot fulfill its contract and handle each error exactly once at the layer
that can add context, recover, translate, or report it. Wrap with meaningful operation context while
preserving error identity when callers use `errors.Is` or `errors.As`.

- Do not compare error strings or expose unstable infrastructure text as a public contract.
- Use sentinel or typed errors only when callers require programmatic branching; otherwise contextual errors
  are sufficient.
- Treat partial results explicitly and document whether they are valid when an error is non-nil.
- Reserve panic for violated internal invariants or process-startup conditions under project policy, not
  routine external failure.
- Check deferred cleanup errors when they can change the operation's result.

## Context propagation

Pass `context.Context` as the first parameter across request-scoped operations that support cancellation,
deadlines, or scoped metadata. Derive child contexts, call cancellation functions, and stop owned work when
the context finishes. Do not store a context in a long-lived struct or pass `nil`.

Context values are for request-scoped cross-boundary metadata, not required business parameters, optional
configuration, dependency injection, or mutable process state. Preserve cancellation identity when adding
error context, and do not claim cancellation support if a blocking dependency ignores it.

## Goroutine lifecycle

Every goroutine MUST have a named owner and a termination argument: what starts it, how it stops, how failure
is observed, and who waits for completion. Bound fan-out and queued work. A caller must not return while its
goroutines still access caller-owned values unless ownership was explicitly transferred.

Use synchronization or an established task-group pattern to aggregate failures and cancellation. Recovering
inside a goroutine is justified only at a boundary that can restore valid state and report the failure. Ensure
timers, tickers, subscriptions, and blocked sends or receives are released on every exit path.

## Channels versus shared state

Use channels when they express ownership transfer, event delivery, coordination, or backpressure. Use a mutex
or other synchronization primitive when several operations protect one coherent piece of shared state and a
channel would create an indirect command protocol.

The sender generally owns closing a channel. Closing is a lifecycle signal, not resource cleanup, and a
channel need not be closed when receivers already terminate by context or scope. Select buffer size from
backpressure and burst requirements; a large buffer is not a fix for missing ownership.

Shared mutable data MUST have one documented synchronization strategy. Do not copy values containing mutexes
after use, and verify race freedom through design as well as available tooling.

## Package visibility and API design

Package boundaries should group cohesive behavior and keep dependencies acyclic. Lowercase identifiers and
`internal` packages limit access, but exported names, package paths, concrete types, method sets, interfaces,
error identities, and observable behavior form the consumer contract.

Under a reusable-library profile, minimize exports, avoid exposing implementation dependencies, and place
interfaces with consumers. Preserve zero-value usefulness only when it produces a valid, unsurprising state;
otherwise require a constructor and keep invalid construction inaccessible. Avoid package-level mutable state
and hidden initialization work.

## Allocation and benchmark discipline

Under clarity-first policy, choose straightforward values, slices, maps, and standard synchronization with
clear ownership. Before retaining pooling, manual buffer reuse, representation tricks, or concurrency added
for speed, establish a representative benchmark and use profiling or allocation evidence to locate the cost.

Benchmark the workload that matters, report allocations where relevant, control setup and I/O noise, and
compare statistically meaningful runs. Escape-analysis output is evidence about compiler decisions, not a
user-facing performance requirement. Pooling can increase retention, aliasing risk, and complexity; use it
only when measured gains exceed those costs.

## Profile refinement examples

- `backend-service`: propagate request context, wrap integration errors, and own all request goroutines before
  returning.
- `reusable-library`: export a small concrete API, let consuming packages define interfaces, and preserve error
  identities intentionally.
- `legacy-modernization`: establish goroutine and shared-state ownership before restructuring packages.
- a high-throughput modifier requires benchmark and profile evidence before introducing pooling or fan-out.

## Review checklist

1. Is each interface minimal, behaviorally coherent, and owned by its consumer?
2. Are error identity, wrapping, partial results, and cleanup failures intentional?
3. Is context propagated and canceled without becoming a parameter bag?
4. Can every goroutine terminate, report failure, and be awaited by its owner?
5. Do channels or locks express the state-ownership model clearly?
6. Is the exported package surface no larger than verified consumers require?
7. Are allocation and concurrency choices supported by representative benchmark evidence?

## Non-goals

This adapter does not teach Go syntax or prescribe one package layout, router, task group, error taxonomy,
channel architecture, or optimization. It refines the selected policy according to observed constraints.
