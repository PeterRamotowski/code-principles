# Legacy Modernization Profile

## Purpose and intended artifacts

Use this profile when the central task is safely evolving a difficult existing system under uncertain behavior or historical constraints. Intended artifacts require discovery, characterization, bounded change, and reversible migration.

Age, unfamiliar style, or missing fashionable architecture is not sufficient evidence. Select the profile because modernization risk dominates the task.

## Priority order

1. observed behavior correctness;
2. compatibility;
3. data integrity;
4. operational reliability;
5. testability needed for safe change;
6. incremental maintainability improvement;
7. local simplicity.

## Default Core Skill modes

| Core Skill | Mode | Profile rationale |
| --- | --- | --- |
| `code-clarity` | `balanced` | Clarify the touched path without disguising uncertain behavior. |
| `abstraction-and-reuse` | `legacy-preservation` | Preserve divergent behavior until evidence proves shared knowledge and safe convergence. |
| `modular-design` | `feature-oriented` | Create seams around affected behavior rather than imposing a wholesale target architecture. |
| `contracts-and-errors` | `tolerant-syntax-strict-semantics` | Accept evidenced legacy representations while protecting required meaning. |
| `testing-strategy` | `characterization-first` | Capture observable behavior before consequential structural change. |
| `safe-change` | `incremental-modernization` | Use bounded, reversible steps with explicit migration checkpoints. |
| `api-and-compatibility` | `internal-application` | Preserve verified internal behavior without inventing a public contract. |

## Typical risks

- removing undocumented but relied-upon behavior;
- broad rewrites that eliminate rollback and comparison points;
- treating every inconsistency as a defect before its consumers are known;
- tests that freeze incidental implementation rather than observable behavior;
- forcing divergent cases through a premature shared abstraction;
- indefinite preservation with no explicit modernization boundary.

## Common modifiers

- `strict-backward-compatibility` protects observable contracts during migration;
- `security-sensitive` prevents behavior preservation from perpetuating unacceptable exposure;
- `public-api` identifies contracts that require external migration policy.

Safety, legality, correctness, and data integrity remain higher precedence than preserving legacy behavior.

## Prohibited default assumptions

- Do not infer that old or unfamiliar code is wrong.
- Do not remove behavior before identifying evidence and consumers.
- Do not combine cleanup, behavior change, and migration in one unbounded step.
- Do not impose a target architecture before a safe seam and transition are demonstrated.
- Do not preserve a dangerous behavior merely because it already exists.

## Non-goals

This profile does not preserve every implementation detail forever, authorize a rewrite, prescribe a target architecture, or lower safety and correctness requirements.

## Profile decision example

When two legacy flows appear duplicated but produce subtly different observed results, `abstraction-and-reuse: legacy-preservation` keeps them separate until characterization proves shared knowledge and a safe convergence path. This resolves DRY versus YAGNI in favor of behavior preservation, unlike the reusable-library profile's evidence-backed extension seam.
