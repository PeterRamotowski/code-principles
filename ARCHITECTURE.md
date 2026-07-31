# Architecture

## 1. Overview

Code Principles is a policy-composition system for AI coding assistants. Its architecture separates stable engineering concepts from project-specific and technology-specific refinements.

The system is intentionally layered:

```text
orchestrator
  ├── project profiles
  ├── modifiers
  ├── language adapters
  ├── framework adapters
  └── core skills
          ↓
    resolved policy
          ↓
    task execution
```

This structure prevents the repository from becoming a collection of duplicated “best practices” prompts.

## 2. Architectural principles

### 2.1 Project type before technology

The dominant policy is selected from the artifact and operational context, not from the language name.

Examples:

- a reusable Python package and a reusable PHP package share the `reusable-library` profile;
- a React single-page application and a Vue single-page application share the `browser-web-application` profile;
- a Go service and a PHP service may share the `backend-service` profile;
- a C++ real-time component requires constraints not present in a generic C++ library.

### 2.2 One source of truth per rule

A general rule belongs in one core skill. Profiles, modifiers, and adapters reference or refine that rule instead of copying it.

For example:

- the meaning of DRY belongs in `core/abstraction-and-reuse`;
- `profiles/reusable-library` selects a stricter extension and compatibility mode;
- `languages/go` refines interface guidance for Go;
- `frameworks/react` refines composition and state-placement guidance for React.

### 2.3 Refinement, not replacement

Adapters refine general policy within their domain. They must not silently replace higher-precedence project requirements.

### 2.4 Explicit conflict handling

Conflicts are expected. A profile is valuable because it determines which quality attributes dominate in a given context.

### 2.5 Conservative behavior under uncertainty

When context is uncertain, the system favors local, reversible, low-coupling decisions and avoids speculative architecture.

## 3. Repository layers

## 3.1 Orchestrator

Path:

```text
orchestrator/
```

Responsibilities:

- context detection;
- evidence classification;
- base profile selection;
- modifier activation;
- adapter selection;
- override application;
- conflict resolution;
- resolved-policy generation;
- visible policy summary.

Non-responsibilities:

- defining all engineering principles;
- containing framework implementation guidance;
- generating project architecture from language detection alone;
- forcing a confirmation step for every task.

The orchestrator metadata is stored in `orchestrator/skill.yaml`, while normative model behavior is stored in `orchestrator/SKILL.md`.

## 3.2 Core skills

Planned path:

```text
core/<skill-id>/
├── SKILL.md
├── skill.yaml
└── examples/
```

A core skill owns a coherent decision domain. Proposed domains are:

| Skill | Primary responsibility |
|---|---|
| `code-clarity` | local readability, naming, explicitness, level of abstraction |
| `abstraction-and-reuse` | DRY, YAGNI, extension points, duplication of knowledge |
| `modular-design` | cohesion, coupling, responsibilities, composition, encapsulation |
| `contracts-and-errors` | validation, parsing, fail-fast behavior, error boundaries |
| `dependencies-and-boundaries` | dependency direction, DI, modules, ports and adapters |
| `state-and-side-effects` | mutability, commands, queries, idempotency, state ownership |
| `api-and-compatibility` | public surface, versioning, deprecation, compatibility |
| `testing-strategy` | test levels, behavior focus, test design, legacy characterization |
| `performance` | measurement, budgets, resource constraints, hot paths |
| `safe-change` | bounded refactoring, legacy behavior, Chesterton’s Fence |
| `distributed-reliability` | retries, duplicates, ordering, partial failure, consistency |
| `engineering-review-lenses` | Conway, Hyrum, Gall, Brooks, Murphy, organizational review |

A core skill may define multiple modes. For example, `abstraction-and-reuse` may expose:

- `conservative`;
- `balanced`;
- `extensible-library`.

## 3.3 Project profiles

Planned path:

```text
profiles/<profile-id>/
├── PROFILE.md
└── profile.yaml
```

A profile:

- describes a class of project;
- sets default priorities;
- activates relevant core skills;
- selects default modes;
- defines typical risks;
- defines non-goals;
- may recommend modifiers;
- must remain language-agnostic.

A profile must not contain syntax or APIs specific to PHP, TypeScript, Python, Go, C++, or any framework.

Example profile composition:

```yaml
id: reusable-library
default_skill_modes:
  code-clarity: public-consumer-readable
  abstraction-and-reuse: extensible-library
  modular-design: stable-boundaries
  contracts-and-errors: strict-boundaries
  api-and-compatibility: public-library
  testing-strategy: unit-focused
  performance: evidence-based
```

## 3.4 Modifiers

Planned path:

```text
modifiers/<modifier-id>/
├── MODIFIER.md
└── modifier.yaml
```

A modifier represents a cross-cutting constraint that can apply to multiple profiles.

A modifier may:

- raise the priority of a quality attribute;
- activate a core skill;
- strengthen a skill mode;
- add prohibited decisions;
- add verification requirements.

A modifier must not behave as an alternative full profile.

Examples:

- `public-api` strengthens compatibility and contract requirements;
- `security-sensitive` strengthens validation, secret handling, least privilege, and auditability;
- `memory-sensitive` strengthens streaming and allocation awareness;
- `accessibility-required` adds UI accessibility verification without replacing the web-application profile.

## 3.5 Language adapters

Planned path:

```text
languages/<language-id>/
├── SKILL.md
├── adapter.yaml
├── typing.md
├── errors.md
├── state-and-mutability.md
├── concurrency.md
├── packaging.md
└── examples/
```

A language adapter may cover:

- runtime semantics;
- type system and type-checking limitations;
- error model;
- resource ownership;
- concurrency model;
- module and packaging conventions;
- public API conventions;
- testing conventions;
- common language-specific failure modes.

A language adapter must not restate the entire project profile.

### 3.5.1 Planned language relationships

```text
javascript
└── typescript extends javascript

php
python
go
cpp
```

Inheritance between adapters must be explicit and acyclic.

### 3.5.2 Python adapter scope

The Python adapter is expected to refine guidance for:

- type hints and their runtime limitations;
- `Any`, `Unknown`-equivalent boundaries, and optional values;
- `Protocol` and structural typing;
- `dataclass` use;
- mutable default arguments;
- exceptions and context preservation;
- context managers;
- iterators and generators;
- CPU-bound versus I/O-bound concurrency;
- `asyncio`, threading, and multiprocessing trade-offs;
- package API and `pyproject.toml` conventions.

## 3.6 Framework adapters

Planned path:

```text
frameworks/<framework-id>/
├── SKILL.md
├── adapter.yaml
└── examples/
```

A framework adapter should contain only framework-specific refinements.

Examples:

- React: component boundaries, state placement, effects, composition, user-behavior testing;
- Next.js: server/client boundaries, caching, rendering modes, routing, server actions, secret handling;
- Vue: reactivity, composables, component state, dependency injection where applicable;
- Nuxt: server/client boundaries, auto-imports, SSR, server routes, data fetching;
- Angular: framework DI, signals, RxJS, services, standalone components, forms;
- Symfony: service container, request lifecycle, Messenger, Doctrine integration, configuration conventions;
- Drupal: plugin APIs, hooks, cache metadata, entities, configuration, extension lifecycle, Symfony integration.

## 3.7 Schemas

Path:

```text
schemas/
```

Schemas provide machine-readable validation for metadata and resolved state.

### `skill.schema.json`

Validates orchestrator and core skill metadata.

### `profile.schema.json`

Validates language-independent project profiles and modifiers represented as profile-like policy components.

### `adapter.schema.json`

Validates language and framework adapter metadata.

### `project-context.schema.json`

Validates explicit repository configuration and detected context snapshots.

### `resolved-policy.schema.json`

Validates the final merged policy used to perform a task.

## 3.8 Evaluations

Planned path:

```text
evaluations/
├── scenarios/
├── expected-results/
├── conflict-tests/
└── regression-tests/
```

Each scenario should contain:

```text
input.md
repository-signals.yaml
expected-context.yaml
expected-policy.yaml
forbidden-decisions.md
review-notes.md
```

Evaluations should test policy selection, not only final code output.

## 4. Resolution pipeline

## 4.1 Input collection

Inputs may include:

- current user request;
- explicit user constraints;
- repository configuration;
- repository files and structure;
- existing code conventions;
- deployment or runtime information;
- previous decisions preserved in project context.

## 4.2 Context normalization

Inputs are normalized to the canonical context vocabulary defined in `TERMINOLOGY.md` and `project-context.schema.json`.

## 4.3 Evidence classification

Each important value is classified by confidence:

```text
explicit
observed
inferred-high
inferred-low
unknown
```

## 4.4 Base profile selection

Exactly one primary profile is normally selected. Composite policy is created using modifiers rather than selecting several overlapping base profiles.

Exceptions may exist for repositories containing clearly separate deliverables, but task-scoped resolution should still identify one dominant profile for the affected code.

## 4.5 Modifier activation

Modifiers are activated only when evidence supports them.

## 4.6 Adapter selection

Language and framework adapters are selected for the affected implementation boundary.

## 4.7 Mode resolution

Profiles set defaults, modifiers strengthen or adjust them, adapters refine them, and explicit overrides take precedence.

## 4.8 Conflict resolution

Conflicts are resolved using:

- precedence;
- protected quality attributes;
- task scope;
- evidence strength;
- failure consequences;
- reversibility;
- public exposure;
- compatibility requirements;
- architecture authority.

## 4.9 Policy output

The final resolved policy is an immutable decision snapshot for the current task. It should be reproducible from the same evidence and configuration.

## 5. Configuration model

A repository may include:

```text
engineering-context.yaml
```

This file should describe stable project policy, not temporary task instructions.

Example:

```yaml
specification_version: 0.2.0
selection_mode: automatic-with-visible-result

project:
  artifact_type: fullstack-application
  project_stage: active-product
  exposure:
    - organization-internal
    - public-api
  domain_complexity: moderate
  architecture_authority: incremental-improvement

runtime:
  - browser
  - nodejs

languages:
  - typescript

frameworks:
  - react
  - nextjs

modifiers:
  - public-api
  - security-sensitive

overrides:
  prohibited_patterns:
    - microservices-without-explicit-approval
    - full-cqrs-without-demonstrated-need
  skill_modes:
    abstraction-and-reuse: conservative
```

## 6. Dependency rules

### 6.1 Allowed dependencies

```text
orchestrator → all metadata layers
profile → core skill identifiers and modes
modifier → core skill identifiers and modes
language adapter → core skills and parent language adapters
framework adapter → core skills, language adapters, parent framework adapters
resolved policy → all selected identifiers
```

### 6.2 Forbidden dependencies

- core skills must not depend on framework adapters;
- project profiles must not depend on specific programming languages;
- language adapters must not select a project profile by themselves;
- framework adapters must not redefine language runtime semantics;
- metadata dependency graphs must not contain cycles;
- examples must not become normative sources of truth.

## 7. Duplication policy

The repository distinguishes three forms of duplication:

### 7.1 Duplicated normative knowledge

Not allowed. The same general rule must not be independently defined in multiple components.

### 7.2 Contextual refinement

Allowed. An adapter may explain how a general rule applies in its technology.

### 7.3 Illustrative repetition

Allowed in examples when necessary for clarity, but examples must link conceptually to the normative source.

## 8. Extensibility model

A new component should be introduced only when it owns a distinct decision responsibility.

### Add a new core skill when:

- the rule domain applies across multiple project types and languages;
- it has a coherent set of conflicts and modes;
- existing skills cannot own it without losing cohesion.

### Add a new profile when:

- the artifact type has a meaningfully different priority model;
- the difference cannot be represented by a modifier;
- the profile applies across more than one language.

### Add a new modifier when:

- the concern applies across several profiles;
- it changes priorities but does not define the whole artifact;
- it can be activated independently.

### Add a new adapter when:

- the language or framework has distinct semantics or conventions that materially change how core rules are implemented.

## 9. Visible reporting

The user-facing summary should normally be compact. A recommended shape is:

```yaml
resolved_context:
  profile: fullstack-web-application
  modifiers: [public-api, security-sensitive]
  languages: [typescript]
  frameworks: [react, nextjs]
  architecture_authority: incremental-improvement

significant_decisions:
  - Keep server-side validation authoritative.
  - Preserve public API compatibility.
  - Do not introduce CQRS without demonstrated need.
```

For a small local task, only exceptional assumptions or trade-offs need to be shown.

## 10. Security architecture

The skills system itself is advisory, but it must treat security constraints as high precedence.

The orchestrator must not allow a profile or style rule to override:

- secret protection;
- access-control requirements;
- data-integrity requirements;
- memory-safety requirements where applicable;
- untrusted-input validation;
- safe dependency and execution boundaries.

A security modifier may strengthen the policy, but the absence of a modifier does not permit insecure code.

## 11. Evolution strategy

The architecture should evolve through working increments:

1. foundation documents and schemas;
2. orchestrator MVP;
3. six core skills;
4. five profiles;
5. TypeScript, Python, and C++ adapters;
6. remaining language adapters;
7. framework adapters;
8. modifiers;
9. evaluation suite;
10. stable release.

This follows the principle that a complex working system should evolve from a simpler working system rather than being designed as an untested complete hierarchy.


## 12. Canonical knowledge architecture

The `principles/` layer precedes Core Skills in the dependency graph:

```text
principle entries
    ↓
Core Skills
    ↓
profiles and modifiers
    ↓
language/framework refinements
    ↓
orchestrator resolution
```

Core Skills may reference principle IDs. Principle entries must not depend on profiles, languages, frameworks, or task-specific policies.

## 13. Compendium generation architecture

Canonical YAML is transformed into human-readable Markdown by `tools/generate_compendium.py`. Generated documentation is committed so the repository is useful without contributor tooling, but validation detects missing generated pages.

## 14. External dependency boundary

Platform integrations may depend on the host’s plugin format. Normative engineering behavior must remain local and self-contained. Third-party Skills are outside the authority graph and cannot be resolution inputs.
