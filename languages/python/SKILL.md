# Python Language Adapter

## Purpose

Apply this adapter after the project profile and Core Skill modes when Python is materially involved. It
translates general policy into decisions appropriate for Python's dynamic runtime, optional static analysis,
resource protocol, concurrency mechanisms, and import system.

## Typing and runtime validation

Type hints improve tooling and communicate contracts, but normally do not enforce runtime values. Choose the
annotation coverage and checker strictness appropriate to the repository, strengthening durable boundaries
before incidental locals.

- Data from requests, files, environment variables, deserialization, and untyped integrations MUST be
  parsed or validated at runtime before trusted domain use.
- `Any`, casts, and ignored checker errors MUST NOT stand in for parsing. Keep unavoidable `Any` at a narrow
  interoperability seam.
- Use `object` for a value of unknown concrete type when arbitrary operations are not permitted. Narrow it
  explicitly.
- Do not repeat expensive validation throughout an already trusted internal pipeline.

## Protocols and structural contracts

Use a narrow, consumer-owned `Protocol` when multiple implementations need to satisfy a behavioral shape
without sharing an inheritance hierarchy. Prefer an ordinary callable type when the contract is only one
operation. Do not create protocols for every concrete class or add members for provider convenience.

Runtime-checkable protocols verify only limited structural presence, not full behavioral correctness. Use
them only when that limited runtime check is actually required.

## Data classes and domain objects

Use a data class for a record with meaningful fields and value-oriented behavior. Validate construction when
invalid instances would otherwise circulate. Use factories when parsing, normalization, or alternative
construction would overload `__post_init__`.

- Use `default_factory` for mutable defaults.
- Consider frozen instances for value objects when mutation is not part of the model; do not claim deep
  immutability for mutable members.
- A dictionary is sufficient for short-lived, local, genuinely open-shaped data. Do not manufacture a class
  solely to satisfy style.

## Exceptions and cleanup

Raise exceptions for operations that cannot fulfill their documented contract. Preserve causal context when
translating lower-level failures, and expose a small exception taxonomy only where callers need distinct
recovery behavior. Never catch `BaseException` for ordinary recovery, and do not swallow an exception merely
to log it.

Use `with` or an appropriate context manager for resources and reversible state changes. Cleanup MUST remain
correct when acquisition, body execution, or release fails. Async resources use `async with` when their
protocol requires it.

## Iterators and generators

Use iterators or generators when incremental production improves memory use, latency, or composition. Their
laziness changes when work and errors occur, so document single-pass behavior, ownership, and cleanup when
these matter. Do not return a generator while silently depending on a file or transaction scope that has
already closed.

Materialize a collection when callers require repeated traversal, stable snapshots, immediate failure, or
simple ownership and the bounded size is acceptable.

## Concurrency choice

Choose from the workload and dependencies:

- use `asyncio` for coordinated high-concurrency I/O when the call chain and libraries are async-aware;
- use threads for blocking I/O or integrations that release the interpreter lock, with bounded work and
  explicit shared-state control;
- use processes or native/vectorized work for CPU-bound parallelism when serialization, startup, and memory
  costs are justified;
- keep synchronous code when concurrency adds no measured or required benefit.

Cancellation, deadlines, task ownership, and failure aggregation MUST be explicit. An `async def` declaration
does not make CPU-bound work non-blocking.

## Packaging and public imports

Under a reusable-library profile, `pyproject.toml` and the documented package entry points define the
supported distribution. Export intentional names from stable modules or package `__init__` files, and treat
documented import paths, signatures, return behavior, and public exceptions as compatibility commitments.

Keep build metadata sufficient for isolated builds. Avoid import-time I/O and mutable global initialization
that makes consumers depend on environment order. Internal underscore naming is useful evidence but cannot
undo a path that is explicitly documented as public.

## Profile refinement examples

- `backend-service`: parse request data into domain objects, use context managers for transactions, and pick
  concurrency from the actual I/O/CPU mix.
- `reusable-library`: prefer narrow structural contracts and stable public imports; avoid leaking dependency
  classes through annotations.
- `legacy-modernization`: add annotations and domain parsing at change seams without requiring a repository-
  wide typing conversion.

## Review checklist

1. Are annotations being mistaken for runtime validation?
2. Is a Protocol owned by and minimal for its consumer?
3. Are mutable defaults, resource lifetime, and exception context correct?
4. Is laziness compatible with scope, repeatability, and failure timing?
5. Does the concurrency mechanism match the measured workload?
6. Are public imports and exception contracts intentional?

## Non-goals

This adapter does not mandate one type checker, validator, framework, or concurrency model. It refines the
selected policy without replacing it.
