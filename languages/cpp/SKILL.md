# C++ Language Adapter

## Purpose

Apply this adapter after the selected project profile and Core Skill modes when C++ is materially involved.
It makes ownership, lifetime, error, resource, concurrency, and compatibility policy concrete while retaining
the project's actual compiler, platform, and standard-version constraints.

## RAII, ownership, smart pointers, and value semantics

Every resource MUST have clear lifetime ownership. Prefer RAII owners whose destructors release resources and
whose invariants survive all normal exits. This applies to memory, handles, locks, mappings, transactions, and
temporary state—not only heap allocations.

- Prefer values when identity, polymorphic lifetime, or shared ownership is unnecessary.
- Use `std::unique_ptr` for exclusive dynamic ownership and transfer it explicitly.
- Use `std::shared_ptr` only for genuine shared lifetime; account for cycles, synchronization, and allocation
  cost. A raw pointer or reference may express a non-owning observation when lifetime is evident.
- Follow the rule of zero where member types already manage resources. Define copy and move behavior
  deliberately for owning types.
- Never encode ownership ambiguously through an undocumented raw owning pointer.

## Const correctness and state

Use `const` to express non-mutation through an interface and to narrow reasoning about aliases. It does not
make shared mutable state thread-safe and does not guarantee transitive immutability. Avoid `const_cast`
except at a verified interoperability boundary where the original object is legally mutable.

Keep invariants valid at construction and after moves. Prefer scoped mutation under a clear owner rather than
widely aliased writable state.

## Error policy

Select the error policy from platform constraints and caller needs:

- exceptions suit failures that prevent a function from returning its promised value when unwinding is
  supported and the boundary documents exception guarantees;
- explicit result/status types suit expected failures, exception-disabled builds, hard real-time paths, and
  boundaries where control flow must be visible;
- termination or assertions are limited to violated internal invariants that cannot be recovered under the
  project's policy.

Do not mix policies casually. Translate once at subsystem, C, ABI, thread, or process boundaries. Destructors
MUST NOT allow exceptions to escape during unwinding. Preserve diagnostic context without exposing unstable
implementation detail as a public contract.

## Templates and runtime polymorphism

Use templates when compile-time variation, static dispatch, or generic value algorithms provide a concrete
benefit. Keep constraints and diagnostics understandable. Do not turn a private implementation choice into a
large public template surface merely to avoid one virtual call.

Use runtime polymorphism when behavior must vary behind a stable runtime boundary and object identity/lifetime
is part of the design. Prefer a value, tagged variant, callable, or composition when the set is closed or the
behavior is small. Measure performance-sensitive dispatch rather than assuming either mechanism wins.

## Allocations and deterministic resources

Under `performance-and-resources: clarity-first`, use standard owners and containers with clear complexity.
Under budgeted or hot-path modes, measure allocations, copies, locality, contention, and worst-case latency.
Reserve capacity or choose arenas only from demonstrated lifetime and budget needs.

Under `hard-real-time`, operations on the critical path MUST have bounded execution and resource behavior:
exclude unbounded allocation, blocking, page faults, uncontrolled locks, exception paths, and other prohibited
platform behavior according to the verified system budget. Preallocate and establish ownership outside the
critical path where appropriate.

## Undefined behavior and concurrency

Potential undefined behavior is a correctness defect, not a performance trade. Review lifetime, bounds,
initialization, signed overflow assumptions, aliasing, alignment, iterator invalidation, and data races.
Compiler and sanitizer evidence strengthen but do not replace reasoning about valid executions.

Shared data accessed concurrently MUST have a synchronization or immutability strategy. Define thread
ownership, lock ordering, atomic memory ordering, task lifetime, cancellation, and shutdown. Use the weakest
memory ordering only when its proof is documented and valuable; otherwise prefer a clearer correct ordering.

## Public headers, source compatibility, and ABI

Under `api-and-compatibility: public-library`, distinguish source compatibility from binary compatibility.
Public headers expose names, overloads, templates, inline code, layouts, exception behavior, and transitive
includes. A stable ABI additionally constrains object layout, virtual tables, symbols, calling conventions,
standard-library exposure, compiler/toolchain support, and allocation ownership across boundaries.

Minimize public surface, avoid leaking private dependencies, and use an established isolation technique such
as an opaque implementation only when ABI stability is a real requirement. Define which side allocates and
destroys cross-boundary objects. Never promise stable ABI merely because the semantic version did not change.

## Profile refinement examples

- `backend-service`: make request and transaction resources RAII-owned, choose one subsystem error policy,
  and synchronize shared state explicitly.
- `reusable-library`: minimize public headers and state source/ABI guarantees separately.
- `legacy-modernization`: establish ownership and characterization before replacing raw handles or changing
  layout and error flow.
- a real-time modifier strengthens deterministic resource and worst-case execution requirements; it does not
  make all code globally allocation-free.

## Review checklist

1. Is ownership visible and is every lifetime valid across success, failure, and moves?
2. Are copy, move, const, and nullability semantics intentional?
3. Is one coherent error policy used or translated at a named boundary?
4. Are templates or virtual dispatch justified by actual variation?
5. Are allocation and blocking compatible with the active resource mode?
6. Are races and other undefined behavior excluded by design?
7. Are source and ABI promises explicit and independently verified?

## Non-goals

This adapter does not prescribe one C++ standard, build system, exception policy, ownership form, or universal
zero-allocation design. Platform and repository evidence control those choices.
