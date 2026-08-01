# JavaScript Language Adapter

## Purpose

Apply this adapter after the selected project profile and Core Skill modes when JavaScript is materially
involved. It translates general policy into JavaScript runtime validation, coercion, object-state,
asynchronous-lifecycle, module, and package decisions. TypeScript extends this adapter because its emitted
program still follows these runtime semantics.

## Dynamic contracts and runtime validation

Function documentation, editor inference, tests, and naming communicate a contract but do not enforce one.
Requests, storage, environment values, parsed JSON, DOM data, messages, and untyped integrations MUST be
validated or parsed before trusted use when malformed values can cross the boundary.

- Parse once at ingress into the shape and semantics required by the domain.
- Check own properties and permitted variants when prototype inheritance or open objects would be unsafe.
- Do not repeatedly validate values inside a trusted pipeline without a separate boundary or mutation risk.
- Use lightweight guards for small contracts and a repository-approved validator for complex schemas; the
  required assurance, not fashion, selects the mechanism.

## Coercion, equality, and absence

Implicit coercion is part of JavaScript, but consequential conversions SHOULD be explicit. Parse numeric,
boolean, and date-like external values according to a documented grammar instead of relying on truthiness or
permissive conversion. Use strict equality by default; use deliberate coercive equality only when its finite
accepted cases are understood and useful.

Distinguish missing properties, `undefined`, `null`, empty strings, zero, and `false` when the contract does.
Defaulting with truthiness MUST NOT erase valid falsy values. Avoid precision-sensitive integer work outside
the verified `Number` range; choose an appropriate representation and serialization contract.

## Objects, prototypes, and mutation

Prefer a plain object, array, function, or module when it expresses the model directly. Classes are useful
when identity, construction invariants, or polymorphic behavior are real requirements, not as a default
wrapper for every record.

Mutable state MUST have a clear owner. Copying an object or freezing it shallowly does not make nested values
immutable. Avoid mutating caller-owned values unless the API says so. Treat prototype modification and
import-time global mutation as process-wide effects requiring explicit compatibility evidence.

## Promises and asynchronous lifetime

A promise represents eventual completion, not automatic ownership or cancellation.

- Await work whose result, failure, or lifetime belongs to the current operation.
- Intentionally detached work MUST have an owner, rejection handling, observability, and shutdown policy.
- Preserve rejection context when translating errors, and do not mix callbacks and promises in a way that can
  settle an operation twice.
- Propagate supported cancellation and deadlines through the call chain. Removing a listener or abandoning a
  promise does not necessarily stop the underlying operation.
- Bound fan-out and queues from workload and resource limits rather than starting one promise per item without
  control.

## Exceptions and error contracts

JavaScript can throw any value. Narrow caught values before reading assumed fields. Throw or reject with the
boundary's documented error form and preserve causes where supported. Do not catch an error only to log and
continue with invalid state; recover only where the caller can establish a valid next action.

Expected domain outcomes may use explicit result values when that makes caller branching clearer. Do not mix
sentinels, exceptions, and rejected promises for the same failure category without a named translation
boundary.

## Modules and package boundaries

Use the repository's established ESM or CommonJS model unless changing it is explicitly in scope. The two
module systems differ in loading, interop, cycles, resolution, and observable export behavior; a file rename
or build transform is not proof of equivalent consumer semantics.

Under a reusable-library profile:

- define intentional package exports and keep private paths outside the supported surface;
- treat module format, conditions, entry points, runtime requirements, accepted inputs, errors, and timing as
  compatibility commitments;
- avoid import-time I/O and environment-dependent global initialization;
- verify both supported import styles and platforms rather than assuming bundlers hide incompatibilities.

## Profile refinement examples

- `browser-web-application`: validate network and storage data, keep UI state ownership visible, and clean up
  listeners and asynchronous work with the owning lifecycle.
- `backend-service`: parse ingress values, bound concurrent work, and make request cancellation reach owned I/O.
- `reusable-library`: minimize documented exports and preserve runtime behavior across supported module forms.
- `legacy-modernization`: characterize coercion, mutation, and async ordering before making local, compatible
  changes.

## Review checklist

1. Are dynamic values parsed before trusted use?
2. Could coercion or truthiness collapse contractually different values?
3. Is mutation owned and are prototype or module side effects intentional?
4. Does every promise have failure, cancellation, and lifetime ownership?
5. Is one coherent error form visible at each boundary?
6. Are module entry points and deep-import compatibility intentional?

## Non-goals

This adapter does not teach JavaScript syntax or prescribe one validator, module system, object style,
framework, or build tool. It refines rather than replaces the selected project policy.
