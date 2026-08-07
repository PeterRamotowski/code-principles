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

## Project profiles

- `profiles/README.md` — implemented profile index and package behavior.
- `profiles/*/PROFILE.md` — language-independent artifact priorities and policy decisions.
- `profiles/*/profile.yaml` — machine-readable selection evidence and default Core Skill modes.

## Language adapters

- `languages/README.md` — implemented adapter index and refinement rules.
- `languages/*/SKILL.md` — normative language-specific decision guidance.
- `languages/*/adapter.yaml` — machine-readable activation, dependencies, and refinements.
- `languages/*/examples/` — positive and negative language decisions.

## Framework adapters

- `frameworks/README.md` — implemented adapter index and dependency relationships.
- `frameworks/*/SKILL.md` — normative framework-specific decision guidance.
- `frameworks/*/adapter.yaml` — machine-readable activation, dependencies, and refinements.
- `frameworks/*/examples/` — positive and negative framework decisions.

## Development

- `CONTRIBUTING.md` — contribution requirements.
- `ROADMAP.md` — implementation milestones.
- `catalogs/` — controlled component identifiers, modes, and implementation status.
- `schemas/` — machine-readable contracts.
