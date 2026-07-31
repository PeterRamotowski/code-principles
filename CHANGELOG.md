# Changelog

All notable changes to the foundation package are documented here.

## [Unreleased]

No changes yet.

## [0.4.0] — 2026-07-31

### Added

- six language-independent Core Skill MVP packages covering clarity, abstraction and reuse, modular
  design, contracts and errors, testing strategy, and safe change;
- documented selection behavior for every supported mode, concrete conflict-resolution rules, positive
  and negative decision examples, and eighteen evaluation scenarios;
- validation of Core Skill package layout, catalogue consistency, conflict counts, documented modes,
  example polarity, and evaluation coverage.

### Changed

- repository status now reflects completion of Milestone 4, and Core Skills are included in controlled
  distributions.

## [0.3.0] — 2026-07-31

### Added

- deterministic Orchestrator MVP with repository evidence detection, confidence-preserving context
  normalization, artifact-driven profile selection, modifier and adapter activation, override merging,
  conflict records, schema-validated resolved policies, and compact visible summaries;
- `tools/orchestrate.py` CLI with YAML, JSON, and summary output plus repository and user context inputs;
- conservative `general-software` fallback profile for materially uncertain artifact evidence;
- repository-wide reference, identifier, dependency-cycle, duplicate-key, and Markdown-anchor validation;
- optional normative-keyword linting and continuous integration validation;
- negative fixtures covering malformed documents, schema violations, duplicate identifiers, dependency
  cycles, broken references, broken Markdown links, and normative-keyword casing.

### Fixed

- resolved-policy examples now use canonical Core Skill, mode, and principle identifiers.

## [0.2.0] — 2026-07-30

### Added

- self-contained canonical registry containing 72 engineering entries;
- generated human-readable compendium and category indexes;
- explicit classification model for principles, heuristics, techniques, methods, properties, laws, patterns, and umbrella concepts;
- canonical rejected interpretations, trade-offs, conflicts, examples, and AI guidance;
- Core Skill, profile, modifier, language, and framework blueprint catalogues;
- Python as a first-class language adapter target alongside JavaScript, TypeScript, PHP, Go, and C++;
- principle, registry, relationship, modifier, and evaluation schemas;
- compendium generation, validation, and packaging tools;
- self-containment and knowledge-model documents;
- active-principle output in resolved policy examples.

### Changed

- the project is explicitly both an AI policy system and a human-readable engineering compendium;
- external Skills are prohibited as normative dependencies;
- adapters refine canonical meaning but cannot redefine it;
- the project is named Code Principles and uses `code-principles` as its repository and package name;
- plugin installation is described as planned rather than currently supported;
- release archives and manifests use an explicit distribution allowlist;
- generated-output freshness and version consistency are validated;
- the project is licensed under the MIT License.

## [0.1.0] — 2026-07-30

Initial specification foundation with orchestrator, schemas, examples, and core architecture documents.
