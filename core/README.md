# Core Skills

Core Skills turn canonical principles into language-independent decision procedures. The orchestrator selects
a mode for each task-relevant Skill; the selected mode emphasizes, constrains, and suppresses behavior without
redefining the canonical principle entries.

## Implemented Core Skills

- [Code Clarity and Simplicity](code-clarity/SKILL.md)
- [Abstraction and Reuse](abstraction-and-reuse/SKILL.md)
- [Modular and Object Design](modular-design/SKILL.md)
- [Contracts, Validation, Errors, and Security](contracts-and-errors/SKILL.md)
- [Testing Strategy](testing-strategy/SKILL.md)
- [Safe Change and Legacy Modernization](safe-change/SKILL.md)
- [Dependencies and Architecture Boundaries](dependencies-and-boundaries/SKILL.md)
- [State and Side Effects](state-and-side-effects/SKILL.md)
- [API and Compatibility](api-and-compatibility/SKILL.md)
- [Performance and Resource Efficiency](performance-and-resources/SKILL.md)
- [Distributed Reliability](distributed-reliability/SKILL.md)
- [Engineering Review Lenses](engineering-review-lenses/SKILL.md)

Each directory contains schema-validated `skill.yaml` metadata, a normative `SKILL.md`, and positive and
negative decision examples. Its positive, boundary, and overengineering scenarios live in
[`evaluations/scenarios/`](../evaluations/scenarios/).

Milestones 4 and 9 now implement every controlled Core Skill in the catalogue.
