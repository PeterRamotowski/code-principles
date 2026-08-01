# Symfony Framework Adapter

## Purpose

Apply this adapter after PHP when Symfony's service container, HttpKernel lifecycle, Messenger, Doctrine, or
configuration semantics affect the work.

## Service container and configuration

Use constructor injection and autowiring for ordinary services. Fetching arbitrary services from the service
container MUST be limited to framework-defined locator or extension seams. Service visibility and scope
SHOULD be as narrow as practical; mutable service state MUST account for long-running workers.

Keep environment-specific values in configuration and secrets, and domain policy in code. Configuration
SHOULD use standard Symfony files, bundles, compiler passes, and environment overrides before a custom
loading layer. Validate required configuration at startup or the owning boundary.

## HttpKernel and controllers

Controllers SHOULD translate HTTP input, invoke an application operation, and translate its result. Parse
and authorize at the boundary while keeping domain invariants inside their owner. Use HttpKernel events when
the concern genuinely spans requests or extends framework lifecycle; do not hide feature flow in listeners.

## Doctrine boundaries

Treat Doctrine entities and the unit of work as persistence concerns with explicit transaction ownership.
Avoid implicit lazy loading across serialization, rendering, or asynchronous boundaries. Repositories SHOULD
express meaningful application queries rather than expose a generic persistence API. Schema migrations are
deployable compatibility steps and MUST account for mixed application versions when rollout requires them.

## Messenger

Messages crossing a transport are durable contracts and SHOULD contain stable identifiers or values, not
managed Doctrine objects. Messenger delivery may repeat; handlers MUST be idempotent or protect effects with
a deduplication policy. Define retryable versus terminal errors, transaction boundaries, failure transport,
and observability. Do not dispatch work whose committed data is not yet visible without an outbox or an
equivalent ordering guarantee.

## Review checklist

1. Are dependencies declared through the container with an appropriate lifetime?
2. Is HttpKernel extension behavior cross-cutting and lifecycle-appropriate?
3. Are Doctrine query and transaction boundaries explicit?
4. Can each Messenger handler safely tolerate retry and partial failure?
5. Does configuration follow Symfony conventions and fail clearly when invalid?

## Non-goals

This adapter does not replace PHP policy or require ports around every Symfony API. Ordinary framework code
should retain recognizable Symfony conventions.
