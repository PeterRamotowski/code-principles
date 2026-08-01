# TypeScript Language Adapter

## Purpose

Apply this adapter when TypeScript is materially involved in implementation or review. First apply the
selected project profile and Core Skill modes, then use this document to translate that policy into
TypeScript decisions. JavaScript runtime semantics remain authoritative because TypeScript types are erased.

## Runtime and compiler baseline

- New or actively maintained code SHOULD use the strictest compiler configuration compatible with the
  repository. At minimum, prefer `strict`; strengthen indexed access and optional-property checks when the
  migration cost is controlled.
- Existing non-strict code MUST be migrated incrementally when a repository-wide switch would create an
  unreviewable change. New unsafe gaps MUST NOT be justified by the legacy baseline.
- A type assertion, non-null assertion, `satisfies`, or generic constraint MUST NOT be treated as runtime
  validation.
- JavaScript rules for coercion, equality, mutation, exceptions, promises, and module loading still apply.

## Unknown input and runtime boundaries

External JSON, storage, environment values, messages, DOM data, and untyped library results begin as
`unknown` unless a trusted boundary has already parsed them. Under `contracts-and-errors:
strict-boundaries`, parse once at ingress and pass the resulting domain type inward.

- Narrow with explicit checks, a small parser, or a repository-approved validation library.
- Return or throw the boundary's documented error form; do not leak arbitrary validator internals.
- Use `any` only at an unavoidable interoperability seam, keep its scope minimal, and convert it to
  `unknown` or a concrete type immediately.
- Do not repeatedly validate the same trusted value inside every helper.

## Modeling states

Use discriminated unions for a closed set of states whose variants require different data. A stable literal
tag and exhaustive `switch` make transition and rendering policy visible. Do not use optional fields to
represent mutually exclusive states when invalid combinations would result.

Prefer ordinary objects, functions, and unions over class hierarchies when identity and inheritance are not
part of the model. Preserve intentional `readonly` contracts, but do not imply deep immutability from a
shallow modifier.

## Generics and type-complexity limits

Generics SHOULD encode a relationship that callers benefit from, such as preserving an input/output type or
constraining an extension point. They MUST NOT exist only to eliminate a few repeated declarations.

Stop and simplify when a public type requires callers to understand recursive conditionals, broad overload
sets, unstable inference tricks, or compiler-limit workarounds. Prefer a named type, explicit overload, or
small runtime function when it gives clearer diagnostics and a more stable contract. Under
`abstraction-and-reuse: conservative`, require demonstrated variation before creating a generic framework.

## Errors and asynchronous work

- JavaScript can throw any value. Catch variables SHOULD remain `unknown` until narrowed.
- Reject promises with the same documented error policy used by synchronous entry points.
- Await work whose failure or lifetime belongs to the current operation. Intentionally detached work MUST
  have explicit ownership and rejection handling.
- Cancellation and timeout support MUST be propagated across boundaries that claim to support it.

## Package APIs

Under `api-and-compatibility: public-library` or `external-api`:

- define explicit exports and keep internal modules outside the supported import map;
- review emitted declarations as part of the public contract;
- avoid leaking private dependency types, compiler-version-sensitive inference, or unnameable implementation
  details;
- assess both runtime and source-type compatibility when evolving an export;
- use type-only exports and imports where they clarify runtime loading, without assuming they change the
  consumer contract automatically.

For an internal application, explicit public typing is still useful at durable boundaries, but internal
refactoring does not need library-grade compatibility machinery.

## Profile refinement examples

- `backend-service`: validate request and integration data at runtime, then use discriminated domain types
  inside transaction owners.
- `reusable-library`: keep the export map and declaration surface intentional; optimize generic ergonomics
  for verified consumers, not hypothetical flexibility.
- `browser-web-application`: represent UI state transitions explicitly and remember that DOM, storage, and
  network values remain runtime inputs.
- `legacy-modernization`: introduce `unknown`, strictness, and narrower types seam by seam while preserving
  observed JavaScript behavior.

## Review checklist

1. Is every untrusted value validated before a type-dependent use?
2. Did an assertion or `any` hide missing evidence?
3. Does each union prevent a real invalid state and remain exhaustively handled?
4. Are generics simpler for callers than the concrete alternatives?
5. Are asynchronous failures and cancellation owned?
6. Are runtime exports and declaration exports intentionally compatible?

## Non-goals

This adapter does not teach TypeScript syntax, prescribe one validator, or replace profile decisions. It does
not make maximal type cleverness a quality goal.
