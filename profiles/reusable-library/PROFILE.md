# Reusable Library Profile

## Purpose and intended artifacts

Use this profile when independent consumers rely on an intentional public surface and evolve on a different schedule from the artifact's implementation. Intended artifacts include published or organization-shared libraries with a supported contract and release lifecycle.

Code reuse inside one application does not by itself make a reusable-library artifact.

## Priority order

1. correctness;
2. consumer compatibility;
3. API usability and predictability;
4. maintainability;
5. portability appropriate to supported environments;
6. evidence-backed extensibility;
7. measured performance.

## Default Core Skill modes

| Core Skill | Mode | Profile rationale |
| --- | --- | --- |
| `code-clarity` | `balanced` | Keep the contract and implementation understandable without exposing internals. |
| `abstraction-and-reuse` | `extensible-public-library` | Permit narrow extension seams for verified independent consumer variation. |
| `modular-design` | `library-oriented` | Minimize the intentional public surface and dependency cost. |
| `contracts-and-errors` | `strict-boundaries` | Define deterministic validation and failure behavior at the consumer boundary. |
| `api-and-compatibility` | `public-library` | Govern evolution, deprecation, and observable behavior as public commitments. |
| `testing-strategy` | `unit-focused` | Cover the public contract and edge cases with fast, portable tests. |
| `safe-change` | `compatibility-first` | Preserve consumer behavior or provide an explicit migration path. |

## Typical risks

- accidental exports becoming compatibility obligations;
- behavior changes that compile but break consumer expectations;
- broad extension surfaces designed for hypothetical consumers;
- dependencies, global state, or environment assumptions imposed on consumers;
- ambiguous errors and invalid states at the public boundary;
- tests coupled to internals instead of the supported contract.

## Common modifiers

- `public-api` makes external contract governance explicit;
- `strict-backward-compatibility` raises migration and deprecation requirements;
- resource modifiers apply only when supported environments provide a verified budget.

## Prohibited default assumptions

- Do not assume consumers release or migrate atomically with the library.
- Do not expose internal machinery as an extension mechanism.
- Do not add hooks for unverified variation axes.
- Do not broaden the public surface to make internal tests convenient.
- Do not claim portability beyond the environments the project supports.

## Non-goals

This profile does not maximize API size, promise universal portability, define application deployment, or require abstraction for every repeated implementation detail.

## Profile decision example

If independent consumers require two documented policies at one stable decision point, `abstraction-and-reuse: extensible-public-library` permits a narrow extension seam. This resolves DRY versus YAGNI in favor of verified consumer variation, while still rejecting hooks for hypothetical variation. Browser and legacy-modernization profiles intentionally resolve the same tension more conservatively.
