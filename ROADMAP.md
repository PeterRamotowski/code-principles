# Roadmap

## 1. Purpose

This public roadmap communicates the intended direction after the foundation package. It prioritizes architectural validation before breadth. It is not a delivery commitment; sequencing may change as implementation and external review produce new evidence. Detailed scheduling and ownership belong in the issue tracker or internal planning.

## Milestone 1 — Specification and Knowledge Foundation

Status: `complete in foundation package`

Deliverables:

- `README.md`;
- `SPECIFICATION.md`;
- `ARCHITECTURE.md`;
- `TERMINOLOGY.md`;
- `CONFLICT-RESOLUTION.md`;
- `CONTRIBUTING.md`;
- `ROADMAP.md`;
- `CHANGELOG.md`;
- example repository engineering context;
- machine-readable schemas;
- orchestrator specification and metadata;
- representative resolved-policy examples.

Exit criteria:

- all JSON schemas parse successfully;
- orchestrator metadata validates;
- terminology is consistent;
- example YAML documents represent valid intended structures;
- no profile is coupled to a programming language.

## Milestone 2 — Validation Tooling

Status: `complete`

Goal: make repository consistency testable.

Deliverables:

- schema validation command;
- YAML and JSON parsing checks;
- identifier uniqueness check;
- dependency-cycle detection;
- broken-reference detection;
- Markdown link validation;
- optional linting for normative keywords.

Suggested implementation options:

- Python CLI using `jsonschema` and `PyYAML`;
- Node.js CLI using Ajv and a YAML parser;
- language-neutral CI wrappers.

Exit criteria:

- one command validates the entire repository;
- validation runs in CI;
- invalid example fixtures prove that checks fail correctly.

## Milestone 3 — Orchestrator MVP

Status: `complete`

Goal: convert requests and repository evidence into a deterministic resolved policy.

Deliverables:

- context-detection implementation;
- evidence-confidence model;
- profile-selection algorithm;
- modifier activation rules;
- adapter selection rules;
- user and repository override merge;
- conflict record generation;
- visible summary format.

Minimum supported artifact types:

- browser application;
- full-stack application;
- backend service;
- reusable library;
- legacy modernization.

Exit criteria:

- representative scenarios resolve consistently;
- uncertainty is preserved;
- low-risk tasks do not require unnecessary confirmation;
- user overrides take precedence;
- the orchestrator does not select architecture from language alone.

Implementation notes:

- `tools/orchestrate.py` is the command-line entry point;
- `orchestrator/resolver.py` contains bounded evidence detection, precedence-aware merging, deterministic
  profile and modifier selection, adapter selection, conflict records, and visible summaries;
- automatic resolution supports browser applications, full-stack applications, backend services,
  reusable libraries, and legacy modernization;
- uncertain artifact evidence uses the conservative `general-software` profile and remains visible as an
  unresolved uncertainty;
- all emitted policies are checked against `schemas/resolved-policy.schema.json` before output.

## Milestone 4 — Core Skills MVP

Status: `complete`

Implement:

1. `code-clarity`;
2. `abstraction-and-reuse`;
3. `modular-design`;
4. `contracts-and-errors`;
5. `testing-strategy`;
6. `safe-change`.

Priority recommendation:

Start with `abstraction-and-reuse` because it tests the most important conflicts among DRY, YAGNI, KISS, Open/Closed Principle, and speculative extensibility.

Exit criteria for each skill:

- metadata validates;
- all modes are documented;
- at least three conflicts are defined;
- positive and negative examples exist;
- at least three evaluation scenarios exist;
- no language-specific rules appear.

Implementation notes:

- each Skill is implemented under `core/<skill-id>/` with schema-validated metadata, a normative
  `SKILL.md`, and decision examples;
- all catalogue modes have operational selection rules and mode-specific constraints;
- conflict sections state the decision, protected qualities, default resolution, and evidence that changes
  the resolution;
- each Skill has a positive case, a boundary case, and an overengineering evaluation scenario;
- repository validation enforces the Milestone 4 package structure and minimum scenario/conflict counts.

## Milestone 5 — Project Profiles MVP

Status: `complete`

Implement:

1. `browser-web-application`;
2. `fullstack-web-application`;
3. `backend-service`;
4. `reusable-library`;
5. `legacy-modernization`.

Each profile should define:

- intended artifacts;
- priority order;
- default core skill modes;
- typical risks;
- non-goals;
- common modifiers;
- prohibited default assumptions.

Exit criteria:

- profiles remain language-independent;
- profiles select modes without duplicating core rules;
- scenarios demonstrate different resolutions for the same principle conflict.

Implementation notes:

- each profile is implemented under `profiles/<profile-id>/` with schema-validated metadata and a
  normative `PROFILE.md`;
- profile metadata is the orchestrator's runtime source for default Core Skill modes;
- profile guidance defines artifact scope, ordered qualities, risks, modifiers, assumptions, and
  non-goals while referencing rather than duplicating Core Skill rules;
- five evaluation scenarios resolve the same DRY-versus-YAGNI conflict according to different artifact
  constraints;
- repository validation enforces the Milestone 5 package set, documented modes, evaluation coverage,
  cross-profile resolution variance, and language independence.

## Milestone 6 — Representative Language Adapters

Implement three deliberately different adapters:

### TypeScript

Focus:

- JavaScript runtime inheritance;
- strict mode;
- `unknown` versus `any`;
- discriminated unions;
- runtime validation boundaries;
- generics and type-complexity limits;
- package API typing.

### Python

Focus:

- optional static typing;
- runtime validation;
- `Protocol` and structural typing;
- data classes and domain objects;
- exception design;
- iterators and generators;
- context managers;
- CPU-bound versus I/O-bound concurrency;
- packaging and public imports.

### C++

Focus:

- RAII and ownership;
- value semantics;
- smart pointers;
- const correctness;
- exceptions versus explicit error policies;
- templates and runtime polymorphism;
- allocations and deterministic resource use;
- ABI considerations;
- undefined behavior and concurrency.

Exit criteria:

- each adapter refines, rather than duplicates, core rules;
- the same project profile produces meaningfully different language-specific guidance;
- adapter dependencies are acyclic.

Implementation notes:

- TypeScript, Python, and C++ are implemented under `languages/<language-id>/` with schema-validated
  metadata, normative `SKILL.md` guidance, and positive and negative decision examples;
- adapter metadata declares Core Skill and canonical-principle refinements without selecting or copying a
  project profile;
- TypeScript explicitly extends the JavaScript catalogue adapter, while Python and C++ are independent;
- three evaluation scenarios apply the same reusable-library task to all representative adapters and require
  different language-specific resolutions;
- repository validation enforces package completeness, focus coverage, catalogue inheritance, evaluation
  coverage, cross-language variance, and acyclic dependencies.

## Milestone 7 — Remaining Language Adapters

Implement:

- JavaScript;
- PHP;
- Go.

TypeScript should explicitly extend JavaScript.

PHP focus:

- strict typing limitations;
- exceptions and value objects;
- Composer package boundaries;
- attributes and reflection;
- long-running process concerns;
- framework interoperability.

Go focus:

- consumer-defined small interfaces;
- explicit error values;
- context propagation;
- goroutine lifecycle;
- channels versus shared state;
- package visibility;
- allocation and benchmark discipline.

## Milestone 8 — Framework Adapters

Implement after language adapters stabilize:

1. React;
2. Next.js;
3. Vue;
4. Nuxt;
5. Angular;
6. Symfony;
7. Drupal.

Important requirements:

- React must not define TypeScript typing rules;
- Next.js must distinguish server and client execution;
- Nuxt must refine Vue rather than duplicate it;
- Drupal may depend on PHP and Symfony but must define its own extension, cache, entity, configuration, and hook concerns;
- framework conventions should be preserved for ordinary application code.

## Milestone 9 — Extended Core Skills

Implement:

- `dependencies-and-boundaries`;
- `state-and-side-effects`;
- `api-and-compatibility`;
- `performance`;
- `distributed-reliability`;
- `engineering-review-lenses`.

## Milestone 10 — Extended Profiles and Modifiers

Profiles:

- plugin or extension;
- data pipeline;
- background worker;
- distributed system;
- real-time system;
- prototype;
- CLI application;
- infrastructure tool.

Modifiers:

- public API;
- strict backward compatibility;
- security sensitive;
- high throughput;
- memory sensitive;
- latency sensitive;
- real time;
- multi-tenant;
- accessibility required;
- offline first.

## Milestone 11 — Evaluation Suite

Initial scenarios:

- Next.js SaaS with public API and payment webhooks;
- React browser dashboard with local and shared state;
- Python large-file data pipeline;
- public Python package;
- Go HTTP API service;
- Go high-throughput worker;
- C++ embedded real-time communication module;
- public PHP library;
- Symfony business application;
- legacy Drupal module;
- Vue/Nuxt content application;
- Angular enterprise form application.

Each scenario should define:

- input request;
- repository signals;
- expected context;
- expected profile and modifiers;
- expected active adapters;
- expected significant decisions;
- forbidden overengineering decisions;
- conflict-resolution expectations.

## Milestone 12 — Stable Release Candidate

Requirements:

- complete validation tooling;
- stable identifiers;
- documented migration policy;
- no unresolved dependency cycles;
- evaluation coverage for all stable profiles and adapters;
- at least one external review from practitioners in web, Python, Go, and C++ ecosystems;
- complete license and governance decision;
- release notes and compatibility policy.

## Future possibilities

After the stable foundation:

- Rust, Java, C#, Kotlin, Swift, and Ruby adapters;
- Svelte and SvelteKit adapters;
- FastAPI, Django, Flask, Laravel, Spring, .NET, and Qt adapters;
- organization-specific policy overlays;
- IDE and agent integrations;
- automatic repository context extraction;
- policy-diff output when configuration changes;
- machine-generated evaluation reports;
- adapters for safety-critical or regulated domains.


## Foundation v0.2.0 additions

Completed in this package:

- canonical registry with 72 entries;
- generated human-readable compendium;
- principle classification and authoring model;
- relationship registry;
- self-containment policy;
- Core Skill, profile, modifier, language, and framework blueprints;
- principle and relationship schemas;
- validation and generation tooling.

The next implementation milestone should create complete normative Core Skills from the blueprints, beginning with `abstraction-and-reuse` and `code-clarity`.
