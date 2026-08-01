# Full-stack Web Application Profile

## Purpose and intended artifacts

Use this profile when one affected product artifact owns meaningful browser and server behavior. Intended artifacts combine interactive delivery with server authority, application operations, and persistence boundaries.

The profile applies to the integrated lifecycle, not to two unrelated artifacts merely stored together.

## Priority order

1. end-to-end correctness;
2. security and authority separation;
3. data integrity;
4. usability;
5. operational reliability;
6. maintainability across client and server boundaries;
7. operability.

## Default Core Skill modes

| Core Skill | Mode | Profile rationale |
| --- | --- | --- |
| `code-clarity` | `balanced` | Make execution context and authority visible in the affected feature. |
| `abstraction-and-reuse` | `balanced` | Share stable domain knowledge without forcing client and server mechanics into one abstraction. |
| `modular-design` | `feature-oriented` | Preserve end-to-end feature cohesion while keeping trust boundaries explicit. |
| `contracts-and-errors` | `strict-boundaries` | Validate whenever data crosses an authority or persistence boundary. |
| `api-and-compatibility` | `internal-application` | Evolve product-internal contracts atomically unless exposure says otherwise. |
| `testing-strategy` | `integration-balanced` | Verify behavior at client/server and persistence boundaries. |
| `safe-change` | `local-safe-change` | Bound changes while tracing their end-to-end effects. |

The referenced modes remain normative in their Core Skills. Explicit context and modifiers MAY replace these defaults.

## Typical risks

- trusting a browser assertion that the server must authorize;
- exposing secrets or privileged operations to an untrusted execution context;
- duplicating validation or business decisions until they diverge;
- cache, rendering, and persistence semantics becoming inconsistent;
- coupling client presentation mechanics to server internals;
- introducing distributed deployment boundaries without an operational need.

## Common modifiers

- `security-sensitive` strengthens boundary and authority controls;
- `multi-tenant` adds isolation and ownership constraints;
- `accessibility-required` elevates interface accessibility;
- `public-api` changes exposed server contracts from internal to externally governed.

## Prohibited default assumptions

- Do not equate shared source code with a shared trust boundary.
- Do not expose secrets to make browser and server implementations symmetrical.
- Do not treat internal request shapes as public compatibility commitments.
- Do not split deployment units merely to mirror source modules.
- Do not assume one validation mechanism is suitable in every execution context.

## Non-goals

This profile does not prescribe deployment topology, rendering strategy, persistence technology, transport, or a specific user-interface or server framework.

## Profile decision example

If client and server repeat one authorization policy, `abstraction-and-reuse: balanced` favors one authoritative server decision and may share only safe contract knowledge. Unlike the browser profile's conservative local default, verified duplicated knowledge can justify a narrow shared representation; unlike a public library, hypothetical consumer variation does not justify an extension surface.
