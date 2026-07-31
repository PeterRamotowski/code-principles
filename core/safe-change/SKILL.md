# Safe Change and Legacy Modernization

## Purpose

Change existing systems with an explicit behavioral boundary, evidence, migration sequence, and recovery path.
This Skill controls scope and modernization authority without treating old behavior as automatically correct.

## Activation and inputs

Activate for fixes, refactors, migrations, modernization, compatibility work, or removal of unfamiliar code.
Use architecture authority, current behavior, tests, consumers, operational history, public exposure, rollout
capabilities, reversibility, and data-migration consequences.

## Decision procedure

1. Define the requested outcome and the behavior that must remain unchanged.
2. Identify consumers, state, integrations, operational controls, and historical reasons for unusual code.
3. Choose the smallest change boundary consistent with the outcome and architecture authority.
4. Establish evidence before risky restructuring: characterization, contract checks, representative samples,
   or operational observation.
5. Separate functional change from structural cleanup when doing so improves review and rollback.
6. Sequence migration through compatible intermediate states when consumers or persisted data outlive deployment.
7. Define verification, rollout, rollback, and removal criteria before irreversible steps.
8. Make unknowns visible; use reversible probes rather than inventing historical intent.

The Skill MUST preserve explicit compatibility and data-integrity requirements. It MUST NOT authorize a rewrite
solely because the existing design is unfamiliar or untidy.

## Modes

### `local-safe-change`

Use by default for ordinary existing-system work. Keep the diff and rollback surface bounded; allow only
directly supporting cleanup.

### `incremental-modernization`

Move one verified seam at a time. Each increment SHOULD have behavior evidence, an independently useful
outcome, and a rollback or containment strategy.

### `compatibility-first`

Use when public or long-lived consumers constrain change. Prefer additive transitions, explicit deprecation,
dual-read or dual-write only when justified, and removal after measured migration.

### `redesign-authorized`

Use only with explicit broad authority. Redesign remains bounded by outcomes, compatibility decisions, data
migration, verification, rollout, and rollback; authority is not permission for an unbounded rewrite.

## Conflict decisions

### Minimal scope versus local improvement

- Decision: whether cleanup accompanies a functional change.
- Protected qualities: maintainability, reviewability, and rollback.
- Default: allow small directly supporting improvements in touched code.
- Change the resolution when cleanup changes behavior, public surface, or obscures the functional diff.

### Simplification versus historical constraints

- Decision: whether apparently redundant behavior can be removed.
- Protected qualities: clarity and operational compatibility.
- Default: inspect history, consumers, and failure evidence before removal.
- Change the resolution when the purpose is disproven, replacement evidence exists, and removal is reversible.

### Modernization versus backward compatibility

- Decision: whether to replace or sequence an existing contract.
- Protected qualities: evolvability and consumer continuity.
- Default: migrate through compatible intermediate states.
- Change the resolution when all consumers are coordinated and an explicit breaking change is authorized.

### Redesign versus incremental evolution

- Decision: whether broad replacement is justified.
- Protected qualities: architectural coherence and delivery risk.
- Default: improve bounded seams incrementally.
- Change the resolution when redesign authority, outcome constraints, migration evidence, and rollback capacity
  are explicit and incremental paths cannot meet the requirement.

## Outputs and review

Produce the change boundary, preservation requirements, unknowns, evidence plan, migration sequence, rollout,
rollback, and cleanup criteria. Review consumer impact, persisted data, operational controls, observability,
reversibility, and whether unrelated work expanded scope.

See [decision examples](examples/scenarios.md). Evaluations: `safe-change-local-fix`,
`safe-change-compatible-migration`, and `safe-change-unbounded-rewrite`.

## Non-goals

This Skill MUST NOT preserve known defects without a compatibility decision, demand perfect history before a
reversible change, forbid redesign, or use test coverage as the only measure of migration safety.
