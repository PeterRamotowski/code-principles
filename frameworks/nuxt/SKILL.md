# Nuxt Framework Adapter

## Purpose

This adapter refines Vue rather than repeating it. Apply Vue's component scope, reactivity, composables,
state locality, and effects first; apply this document to Nuxt SSR, server/client execution, data fetching,
caching, routing, runtime configuration, and auto-import behavior.

## Server, client, and SSR boundaries

Classify code as server-only, client-only, or universal. Universal setup may run during SSR and hydration, so
it MUST NOT assume browser globals, mutate process-global request state, or repeat non-idempotent effects.
Private runtime configuration and privileged dependencies MUST remain server-only; expose only intentional,
non-secret public configuration to client bundles.

Hydration requires the server and initial client render to agree. Time, randomness, locale, browser-only
state, and unstable markup SHOULD be deferred or serialized deliberately when they affect initial output.

## Data fetching and caching

Use Nuxt's SSR-aware data fetching when data belongs to rendering. Give each request a stable key and make
deduplication, freshness, and error behavior explicit. Reuse transferred SSR data during hydration rather
than issuing an automatic duplicate request. User-specific data MUST NOT leak through shared cache state.

Server routes are trust boundaries: parse input, authenticate, authorize, and return a deliberate error
contract. Keep private infrastructure behind the server directory rather than importing it into universal
composables.

## Routing, middleware, plugins, and auto-imports

Preserve file-based routing, layouts, middleware, plugins, and auto-import conventions for ordinary code.
Name reusable auto-imports clearly and avoid collisions or hidden side effects. A plugin MUST declare the
environment and lifecycle it needs. Route middleware SHOULD make navigation decisions, not become a general
data-access or business-logic layer.

## Review checklist

1. Is code correctly server-only, client-only, or universal?
2. Will SSR and hydration produce stable equivalent initial output?
3. Does data fetching reuse payloads with explicit keys and cache lifetime?
4. Are secrets and per-request state isolated from client and process-global scope?
5. Are Nuxt routing and auto-import conventions preserved without ambiguous magic?

## Non-goals

This adapter does not duplicate Vue guidance or require one SSR, rendering, or caching strategy everywhere.
