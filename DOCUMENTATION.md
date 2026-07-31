# Documentation Map

## Start here

- `README.md` — project overview and package structure.
- `SPECIFICATION.md` — normative system behavior.
- `ARCHITECTURE.md` — component and dependency architecture.
- `KNOWLEDGE-MODEL.md` — separation between canonical knowledge and operational Skills.
- `SELF-CONTAINMENT.md` — prohibition of normative external Skill dependencies.

## Knowledge base

- `principles/README.md` — registry overview.
- `principles/INDEX.md` — generated compendium index.
- `principles/CLASSIFICATION.md` — concept taxonomy.
- `principles/AUTHORING-GUIDE.md` — contribution rules.

## Policy resolution

- `CONFLICT-RESOLUTION.md` — conflict matrix and precedence.
- `orchestrator/SKILL.md` — orchestrator behavior.
- `orchestrator/resolver.py` — deterministic context and policy resolver implementation.
- `orchestrator/principle-selection.md` — activation and interpretation of principles.
- `tools/orchestrate.py` — command-line policy resolution and visible summaries.

## Core Skills

- `core/README.md` — implemented Core Skill index and package conventions.
- `core/*/SKILL.md` — language-independent decision procedures and mode behavior.
- `core/*/skill.yaml` — machine-readable activation, conflicts, modes, outputs, and principle selection.
- `core/*/examples/` — positive and negative decisions.
- `evaluations/scenarios/` — policy-selection and forbidden-behavior scenarios.

## Development

- `CONTRIBUTING.md` — contribution requirements.
- `ROADMAP.md` — implementation milestones.
- `catalogs/` — controlled component identifiers, modes, and remaining blueprints.
- `schemas/` — machine-readable contracts.
