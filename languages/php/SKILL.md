# PHP Language Adapter

## Purpose

Apply this adapter after the selected project profile and Core Skill modes when PHP is materially involved.
It translates policy into PHP type-boundary, value-object, exception, Composer, metadata, process-lifetime,
and framework interoperability decisions.

## Strict typing limitations and runtime boundaries

Use `declare(strict_types=1)` consistently in new or actively maintained source when compatible with the
repository. It reduces scalar coercion for calls made from that file, but it is not whole-program strictness
and does not validate semantic meaning, array shapes, deserialized objects, or values arriving from external
systems.

Requests, configuration, environment variables, database rows, messages, uploaded files, and deserialized
data MUST be parsed at runtime before trusted domain use. Static-analysis annotations refine tooling but MUST
NOT substitute for executable boundary checks. Avoid broad `mixed` inside trusted code; narrow it at the seam.

## Value objects and domain state

Use value objects when a domain value has reusable validation, normalization, comparison, or behavior, or
when several scalars permit invalid combinations. Establish invariants at construction and avoid partially
initialized instances. Immutable or `readonly` forms are useful when identity does not require mutation, but
object members can still reference mutable values and must be reasoned about explicitly.

Do not wrap every scalar. Local, already-valid values can remain scalars when a class would add ceremony
without protecting a contract. Arrays are suitable for short-lived open-shaped transport data; do not let
unverified associative arrays become an implicit domain model across durable boundaries.

## Exceptions and failure contracts

Throw an exception when an operation cannot fulfill its documented contract. Use a small public taxonomy
only where callers need distinct recovery actions. Translate infrastructure or framework failures at a named
boundary while preserving the previous exception and useful diagnostic context.

Do not catch `Throwable` merely to log and continue, and do not hide programming errors as ordinary domain
failures. Cleanup belongs in `finally` or a resource owner when failure can interrupt the normal path.
Public packages MUST document stable exception categories they expect consumers to handle.

## Composer package boundaries

Composer metadata, autoload rules, documented namespaces, public classes and functions, dependencies, and
supported PHP versions form the distribution contract. Under a reusable-library profile:

- keep implementation namespaces undocumented or otherwise clearly internal;
- minimize required dependencies and do not expose a dependency's concrete types unnecessarily;
- classify version constraints and platform requirements from verified compatibility;
- treat public signatures, named-argument parameter names where supported, exceptions, attributes, and
  observable behavior as compatibility concerns;
- avoid side effects during autoload and file inclusion.

## Attributes and reflection

Attributes are declarative metadata, not self-executing validation or authorization. The code interpreting an
attribute MUST validate target, arguments, multiplicity, inheritance behavior, and failure policy. Keep
reflected conventions discoverable and prefer direct code when metadata would obscure a small local decision.

Reflection can be expensive and can bypass ordinary visibility assumptions. Cache derived metadata only at a
lifetime with correct invalidation and memory bounds. Never treat a reflected type declaration as proof that
external values satisfy domain semantics.

## Long-running process concerns

Workers, event loops, persistent application servers, and queue consumers do not receive traditional
request-end cleanup. Per-operation services, identity, locale, transactions, buffers, handlers, and caches
MUST be reset or scoped explicitly. Close resources, roll back failed units of work, remove listeners, and
release large references on success, failure, cancellation, and shutdown.

Bound memory growth and concurrency, make signal handling and graceful shutdown explicit, and assume static
properties and container singletons persist until process exit. A retry MUST start from known valid state.

## Framework interoperability

Preserve ordinary framework lifecycle, container, event, middleware, extension, serialization, and error
conventions unless project evidence authorizes a different boundary. Put framework-independent policy behind
small adapters only where it provides actual portability or testability. Do not mirror the entire framework
API behind custom abstractions.

Framework-owned objects may carry lifecycle and proxy behavior that makes cloning, serialization, or manual
construction unsafe. Respect documented extension points and translate to domain values at deliberate seams.

## Profile refinement examples

- `backend-service`: parse request data into value objects, translate infrastructure exceptions once, and
  scope transaction state per operation.
- `reusable-library`: keep Composer dependencies and public namespaces small and document stable exceptions.
- `legacy-modernization`: introduce strict declarations and value parsing file by file while preserving
  observed framework behavior.
- a background worker strengthens reset, memory-bound, retry, and graceful-shutdown requirements.

## Review checklist

1. Is `strict_types` being mistaken for external or semantic validation?
2. Does each value object protect a durable invariant without needless wrapping?
3. Are exception translation and cleanup owned at one boundary?
4. Is the Composer and public namespace surface intentional?
5. Are attributes validated and reflection costs and failures controlled?
6. Does long-running state reset after every operation and failure?
7. Are framework interoperability contracts preserved?

## Non-goals

This adapter does not teach PHP syntax or prescribe one framework, analyzer, container, ORM, serializer, or
application architecture. It refines the selected policy within repository and framework constraints.
