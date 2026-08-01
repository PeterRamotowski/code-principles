# Language Adapters

Language adapters translate language-independent policy into concrete runtime, type-system, resource,
concurrency, and packaging decisions. They refine the selected project profile and Core Skill modes; they
do not select profiles or redefine canonical principles.

## Milestone 6 implementations

- [TypeScript](typescript/SKILL.md) — JavaScript runtime boundaries, strict typing, discriminated unions,
  type-complexity limits, and typed package APIs;
- [Python](python/SKILL.md) — optional static typing, structural contracts, exceptions, resource scopes,
  concurrency choices, and public imports;
- [C++](cpp/SKILL.md) — RAII, ownership, value semantics, error policy, deterministic resources, ABI, and
  undefined-behavior controls.

Each package contains schema-validated `adapter.yaml`, normative `SKILL.md`, and positive and negative
decision examples. Adapter evaluation scenarios live in
[`evaluations/scenarios/`](../evaluations/scenarios/).

TypeScript explicitly extends the JavaScript catalogue adapter. Python and C++ have no parent adapter.
The dependency graph is validated as acyclic.
