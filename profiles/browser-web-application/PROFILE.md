# Browser Web Application Profile

## Purpose and intended artifacts

Use this profile when the affected artifact is primarily a browser-executed user interface. Intended artifacts own interaction, rendering, navigation, accessibility, and client-side state, without substantial server responsibility in the same scope.

Do not select this profile merely because another product contains a small administrative or diagnostic interface.

## Priority order

Apply this order after higher-precedence safety and explicit requirements:

1. correctness of user-visible behavior;
2. accessibility;
3. usability and predictable interaction;
4. browser-side security boundaries;
5. maintainability of features and state ownership;
6. measured rendering and interaction performance.

## Default Core Skill modes

This profile selects existing Core Skill rules; it does not redefine them.

| Core Skill | Mode | Profile rationale |
| --- | --- | --- |
| `code-clarity` | `balanced` | Keep user behavior and state transitions readable within the touched feature. |
| `abstraction-and-reuse` | `conservative` | Prefer local feature clarity until repeated behavior and a stable variation axis are demonstrated. |
| `modular-design` | `feature-oriented` | Keep behavior, state, and interaction tests close to the user capability they serve. |
| `contracts-and-errors` | `strict-boundaries` | Treat external data, persisted state, and user-controlled input as boundary data. |
| `state-and-side-effects` | `localized-state` | Give state the narrowest owner that coordinates all legitimate writers. |
| `testing-strategy` | `integration-balanced` | Verify interaction behavior across rendering and boundary seams. |
| `safe-change` | `local-safe-change` | Keep ordinary interface changes bounded to the affected behavior. |

Explicit configuration and active modifiers MAY override these defaults through normal precedence.

## Typical risks

- inaccessible semantics, focus, keyboard operation, or feedback;
- duplicated or ambiguous state ownership;
- stale asynchronous results and unhandled failure states;
- trusting client-held identity, authority, or validation;
- abstractions organized around visual resemblance instead of shared behavior;
- performance work without an interaction or rendering budget.

## Common modifiers

- `accessibility-required` makes accessibility an explicit correctness constraint;
- `offline-first` adds synchronization and recovery requirements;
- `security-sensitive` strengthens handling of untrusted data and authority.

Modifiers apply their own Core Skill refinements and MUST NOT be inferred solely from the profile.

## Prohibited default assumptions

- Do not assume client input or client-held authority is trustworthy.
- Do not assume global state is needed for data used by one feature boundary.
- Do not assume visually similar elements require one shared abstraction.
- Do not assume every failure should be hidden behind a generic user message.
- Do not assume performance problems or solutions without measurement.

## Non-goals

This profile does not define server deployment, persistence architecture, distributed consistency, a framework, a component library, or visual design conventions.

## Profile decision example

When two nearby interactions contain similar markup but represent different behavior, `abstraction-and-reuse: conservative` keeps them local until shared knowledge and a stable variation point exist. This resolution protects locality and YAGNI; a reusable-library profile can resolve the same DRY-versus-YAGNI tension differently when independent consumers require an extension contract.
