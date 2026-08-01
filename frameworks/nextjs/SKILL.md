# Next.js Framework Adapter

## Purpose

Apply this adapter with React and TypeScript when Next.js routing, rendering, data, or mutation semantics
matter. React owns component policy; TypeScript owns erased static types.

## Server and client execution

Treat server and client as separate trust and execution environments. Components SHOULD remain server-owned
unless browser APIs, interactive state, or client-only lifecycle require a client boundary. A client marker
pulls its dependency graph toward the browser; keep that graph small and pass serializable data across it.

Secrets, privileged credentials, and server-only dependencies MUST NOT enter a client-reachable module.
Environment naming is not the sole protection: preserve a structurally server-only boundary. Parameters,
cookies, headers, forms, and third-party responses remain untrusted at every server entry point.

## Rendering, data, and cache policy

Choose static, dynamic, streaming, or client rendering from freshness, personalization, and operational
requirements. Do not opt an entire route into dynamic rendering for incidental convenience.

Every fetch or computed cache SHOULD have a named owner, key identity, lifetime, and invalidation event.
Cache tags and path revalidation must correspond to the data dependency being changed. Sensitive or
per-user results MUST NOT enter a shared cache. Make cache behavior explicit when stale results affect
correctness; do not scatter disabling flags as a substitute for a policy.

## Routing and server actions

Use the framework's file routing, layouts, loading states, error boundaries, and route handlers for ordinary
application code. Route handlers and server actions are externally callable server boundaries: authenticate,
authorize, parse input, enforce invariants, and handle duplicate submission there. Server actions MUST NOT
trust hidden fields, client validation, or a generated invocation path.

Redirects and not-found control flow SHOULD remain distinguishable from unexpected failures. Avoid catching
framework control-flow signals in broad error translation.

## Review checklist

1. Is every module deliberately server, client, or shared, with a serializable boundary?
2. Can any client dependency reach secrets or privileged capabilities?
3. Is rendering mode justified by freshness and personalization?
4. Does each cache have explicit scope, key, lifetime, and invalidation?
5. Do server actions and route handlers reauthorize and parse their inputs?

## Non-goals

This adapter does not duplicate React rendering guidance or TypeScript typing rules, and it does not require
one rendering or cache strategy for every route.
