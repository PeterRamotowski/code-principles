# Language Adapters

Language adapters translate language-independent policy into concrete runtime, type-system, resource,
concurrency, and packaging decisions. They refine the selected project profile and Core Skill modes; they
do not select profiles or redefine canonical principles.

## Implemented adapters

- [JavaScript](javascript/SKILL.md) — runtime validation, coercion, dynamic contracts, mutation, promises,
  errors, modules, and package exports;
- [TypeScript](typescript/SKILL.md) — JavaScript runtime boundaries, strict typing, discriminated unions,
  type-complexity limits, and typed package APIs;
- [Python](python/SKILL.md) — optional static typing, structural contracts, exceptions, resource scopes,
  concurrency choices, and public imports;
- [PHP](php/SKILL.md) — strict typing limitations, value objects, exceptions, Composer boundaries, reflection,
  process lifetime, and framework interoperability;
- [Go](go/SKILL.md) — consumer-owned interfaces, explicit errors, context, goroutine ownership, packages, and
  benchmark-backed allocation decisions;
- [C++](cpp/SKILL.md) — RAII, ownership, value semantics, error policy, deterministic resources, ABI, and
  undefined-behavior controls.

Each package contains schema-validated `adapter.yaml`, normative `SKILL.md`, and positive and negative
decision examples. Adapter evaluation scenarios live in
[`evaluations/scenarios/`](../evaluations/scenarios/).

TypeScript explicitly extends the implemented JavaScript adapter. The other adapters have no parent adapter.
The dependency graph is validated as acyclic. Evaluation scenarios apply the same reusable-library task to
both the representative and remaining adapter groups and require language-specific resolutions.
