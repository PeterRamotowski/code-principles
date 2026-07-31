# Code Principles Specification

## 1. Document status

- Specification version: `0.4.0`
- Status: `draft`
- Normative language: English
- Schema dialect: JSON Schema Draft 2020-12

This document defines the normative behavior of Code Principles.

The key words **MUST**, **MUST NOT**, **REQUIRED**, **SHOULD**, **SHOULD NOT**, **RECOMMENDED**, **MAY**, and **OPTIONAL** are to be interpreted as requirement levels. A `MUST` rule is binding within its scope. A `SHOULD` rule is a strong default that may be overridden by documented context. A `MAY` rule describes an allowed option.

## 2. Purpose

The system provides context-sensitive engineering guidance for AI models that create, modify, review, explain, or plan software.

It MUST help the model:

1. distinguish project type from programming language;
2. identify relevant engineering constraints;
3. select an appropriate project profile;
4. refine that profile with modifiers and adapters;
5. resolve conflicts between valid principles;
6. respect explicit user and repository decisions;
7. avoid accidental overengineering;
8. make significant assumptions and trade-offs visible;
9. preserve existing architecture unless change authority permits redesign;
10. produce guidance appropriate to the task's scope.

## 3. Non-goals

The system MUST NOT:

- define one universal software architecture;
- require object-oriented programming;
- require SOLID in every project or every component;
- require Clean Architecture, domain-driven design, CQRS, event sourcing, or microservices by default;
- treat dependency injection as a goal independent of decoupling needs;
- replace framework conventions without evidence that they are harmful;
- create abstractions solely to satisfy a named principle;
- require every local implementation detail to be configurable or extensible;
- treat all public language visibility as a stable public API;
- infer runtime data validity from static type annotations alone;
- optimize code without evidence, constraints, or known scale requirements;
- block small, reversible tasks because some project context is unknown;
- silently override explicit user instructions with generic best practices.

## 4. System layers

The system consists of the following layers.

### 4.1 Orchestrator

The orchestrator detects context, selects policy components, resolves conflicts, and produces a resolved policy.

### 4.2 Core skills

Core skills contain reusable engineering decision rules independent of programming language and framework.

Planned core skills include:

- code clarity;
- abstraction and reuse;
- modular design;
- contracts and error handling;
- dependencies and boundaries;
- state and side effects;
- API and compatibility;
- testing strategy;
- performance and resource efficiency;
- safe change and legacy modernization;
- distributed reliability;
- engineering review lenses.

### 4.3 Project profiles

A project profile describes the dominant engineering policy for a class of software artifact.

Planned profiles include:

- browser web application;
- full-stack web application;
- backend service;
- reusable library;
- plugin or extension;
- data pipeline;
- distributed system;
- real-time system;
- prototype;
- legacy modernization.

### 4.4 Modifiers

Modifiers alter one or more profile priorities because of cross-cutting constraints.

Examples include:

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

### 4.5 Language adapters

Language adapters map general engineering guidance to a language's type system, runtime, resource model, error model, concurrency model, packaging conventions, and ecosystem practices.

Initial target languages are:

- JavaScript;
- TypeScript;
- Python;
- PHP;
- Go;
- C++.

### 4.6 Framework adapters

Framework adapters refine language guidance using framework-specific lifecycle, rendering, dependency, cache, state, extension, and testing conventions.

Initial target frameworks are:

- React;
- Next.js;
- Angular;
- Vue;
- Nuxt;
- Symfony;
- Drupal.

### 4.7 Evaluations

Evaluations contain representative scenarios, expected context resolution, forbidden decisions, and regression checks.

## 5. Decision precedence

The system MUST resolve instructions using the following precedence, from highest to lowest:

1. safety, legality, correctness, and data-integrity requirements;
2. explicit current user instructions;
3. explicit repository engineering configuration;
4. verified constraints of the existing codebase and deployment environment;
5. selected project profile;
6. active modifiers;
7. language adapters;
8. framework adapters;
9. core skill defaults;
10. general stylistic preference.

The ordering of language and framework adapters does not mean a framework may contradict the language runtime. A framework adapter refines the language adapter within valid language semantics.

When two rules at the same precedence conflict, the orchestrator MUST use the conflict-resolution procedure defined in `CONFLICT-RESOLUTION.md`.

## 6. Context model

The orchestrator MUST represent project context using the dimensions below. Unknown values MUST remain unknown rather than being invented.

### 6.1 Artifact type

Canonical values:

- `web-application`
- `frontend-application`
- `fullstack-application`
- `backend-service`
- `reusable-library`
- `cli-application`
- `desktop-application`
- `mobile-application`
- `embedded-system`
- `data-pipeline`
- `background-worker`
- `distributed-system`
- `plugin-or-extension`
- `infrastructure-tool`
- `test-tooling`
- `unknown`

A project MAY have one primary artifact type and several secondary capabilities.

### 6.2 Project stage

Canonical values:

- `prototype`
- `greenfield`
- `active-product`
- `mature-system`
- `legacy-modernization`
- `maintenance-only`
- `unknown`

### 6.3 Exposure

Canonical values:

- `private-local`
- `team-internal`
- `organization-internal`
- `external-integration`
- `public-api`
- `public-library`
- `extension-platform`
- `unknown`

Exposure MUST be evaluated per boundary where possible. A project may contain both private implementation and a public API.

### 6.4 Domain complexity

Canonical values:

- `low`
- `moderate`
- `high`
- `unknown`

Domain complexity concerns the density and volatility of business rules, invariants, workflows, and terminology. It MUST NOT be inferred solely from repository size.

### 6.5 Runtime

Canonical values include:

- `browser`
- `nodejs`
- `server`
- `edge`
- `serverless`
- `container`
- `desktop`
- `mobile`
- `embedded`
- `native`
- `wasm`
- `unknown`

Multiple runtime values MAY be active.

### 6.6 State model

Canonical values:

- `mostly-stateless`
- `request-scoped`
- `transactional`
- `shared-mutable`
- `event-driven`
- `eventually-consistent`
- `real-time`
- `offline-synchronized`
- `unknown`

### 6.7 Architecture authority

Canonical values:

- `preserve-existing`
- `incremental-improvement`
- `redesign-allowed`
- `greenfield`
- `unknown`

Architecture authority constrains the size of permitted structural changes.

- `preserve-existing` allows only changes required by the task and small local improvements.
- `incremental-improvement` allows bounded refactoring near the changed area.
- `redesign-allowed` permits broader alternatives when justified.
- `greenfield` permits selecting a new architecture.

### 6.8 Constraint levels

The following dimensions use `normal`, `elevated`, `high`, `critical`, or `unknown`:

- security;
- reliability;
- backward compatibility;
- latency sensitivity;
- throughput sensitivity;
- memory sensitivity;
- determinism;
- accessibility.

The orchestrator MUST distinguish a verified requirement from a weak inference.

### 6.9 Technology context

Technology context MAY include:

- programming languages;
- frameworks;
- build systems;
- package managers;
- databases;
- message brokers;
- deployment platforms;
- test frameworks.

Technology detection MUST NOT determine the project profile by itself.

## 7. Evidence and confidence

Every material context decision SHOULD be classified as one of:

- `explicit` — directly stated by the user or repository configuration;
- `observed` — directly supported by repository files or code;
- `inferred-high` — strongly implied by multiple signals;
- `inferred-low` — plausible but uncertain;
- `unknown` — insufficient evidence.

The orchestrator MUST NOT convert `inferred-low` into a binding architectural requirement.

Significant low-confidence assumptions SHOULD be included in the visible result when they affect the proposed design.

## 8. Selection modes

### 8.1 Automatic with visible result

Identifier: `automatic-with-visible-result`

This is the RECOMMENDED default.

The orchestrator MUST:

- select the effective profile and adapters;
- proceed without confirmation for ordinary and reversible work;
- briefly report significant selected policies;
- expose assumptions that materially affect the result.

### 8.2 Propose

Identifier: `propose`

The orchestrator SHOULD propose the intended policy before performing high-impact architecture work. It MUST NOT require confirmation for trivial local edits unless the user explicitly requests confirmation.

### 8.3 Manual

Identifier: `manual`

The orchestrator MUST honor the explicitly supplied profile, modes, and adapters unless they are invalid, internally contradictory, unsafe, or impossible for the target technology.

## 9. Profile selection

The orchestrator MUST select one primary project profile unless a repository configuration explicitly defines a composite profile.

Profile selection SHOULD prioritize:

1. artifact type;
2. public exposure and compatibility requirements;
3. project stage;
4. domain complexity;
5. state and distribution model;
6. operational constraints;
7. existing architecture;
8. technology ecosystem.

Examples:

- a package published for reuse SHOULD select `reusable-library` even if it is implemented in TypeScript, Python, PHP, Go, or C++;
- a Next.js product containing browser and server code SHOULD usually select `fullstack-web-application`;
- a Python process that streams and transforms large files SHOULD usually select `data-pipeline` or `background-worker`, not `backend-service` merely because it runs on a server;
- a Drupal module SHOULD usually select `plugin-or-extension`, possibly combined with web-application concerns;
- a C++ component with hard timing constraints SHOULD select `real-time-system`, not a generic library profile alone.

## 10. Modifier activation

A modifier MUST be activated only when supported by explicit requirements, observed project characteristics, or strong inference.

Modifiers MUST remain narrow. For example:

- `public-api` changes compatibility and contract guidance;
- it MUST NOT automatically require microservices or CQRS;
- `security-sensitive` strengthens boundary validation and secret-handling rules;
- it MUST NOT be used as a generic label for every web application;
- `high-throughput` strengthens performance evidence and streaming guidance;
- it MUST NOT justify unreadable code outside measured or constrained paths.

## 11. Adapter selection

### 11.1 Language adapters

A language adapter MUST be selected for every language materially involved in the task.

For mixed-language repositories, the orchestrator SHOULD select adapters only for the affected boundaries unless the task is repository-wide.

### 11.2 Framework adapters

A framework adapter MUST be selected when the task depends on framework lifecycle, conventions, extension APIs, rendering model, dependency model, caching, or testing infrastructure.

A framework adapter MUST NOT duplicate the complete language adapter. It SHOULD declare its language dependencies.

### 11.3 Adapter inheritance

Adapters MAY extend other adapters. For example, TypeScript may extend JavaScript. Such inheritance MUST be explicit and acyclic.

## 12. Core skill activation

Core skills MAY be:

- always active at a default mode;
- activated by a profile;
- strengthened by a modifier;
- refined by an adapter;
- overridden by explicit project configuration.

The orchestrator SHOULD activate only skills relevant to the task. It MUST NOT flood a local code edit with unrelated distributed-systems, real-time, or public-library rules.

## 13. Resolved policy

The orchestrator MUST produce an internal resolved policy before executing a non-trivial task.

The resolved policy MUST be representable using `schemas/resolved-policy.schema.json` and SHOULD contain:

- specification version;
- selection mode;
- resolved project context;
- primary profile;
- active modifiers;
- language adapters;
- framework adapters;
- active core skills and modes;
- applied overrides;
- significant decisions;
- unresolved uncertainties;
- conflicts and their resolutions;
- prohibited decisions where relevant.

The full internal policy does not need to be printed to the user. The visible summary SHOULD be proportional to the task.

## 14. User overrides

Users MAY override:

- profile selection;
- skill modes;
- permitted architecture changes;
- technology choices;
- compatibility policy;
- performance priorities;
- testing expectations;
- prohibited patterns.

Overrides MUST be recorded in the resolved policy.

An override MUST NOT be interpreted more broadly than stated. For example, “do not use Clean Architecture” does not prohibit all modular boundaries or dependency management.

## 15. Existing project policy

When modifying an existing project, the orchestrator MUST inspect and preserve relevant established conventions unless:

- the user authorizes redesign;
- the current convention causes a correctness or security defect;
- the requested task explicitly replaces the convention;
- a localized deviation is necessary and documented.

The model SHOULD prefer consistency with the codebase over introducing a personally preferred pattern.

The model MUST NOT use a small task as an excuse for unrelated migration, framework replacement, state-management replacement, or repository-wide refactoring.

## 16. Conflict resolution

When principles conflict, the model MUST NOT select a rule by slogan alone.

It MUST evaluate:

1. the decision scope;
2. the protected quality attributes;
3. evidence and constraints;
4. reversibility;
5. public versus internal impact;
6. cost of delay;
7. failure consequences;
8. compatibility requirements;
9. existing architecture authority;
10. whether a simpler local decision is sufficient.

The central conflict procedure is defined in `CONFLICT-RESOLUTION.md`.

## 17. Normative behavior for common principles

### 17.1 KISS

KISS SHOULD favor the least complex solution that satisfies verified requirements. It MUST NOT be used to ignore correctness, security, or known scale constraints.

### 17.2 YAGNI

YAGNI SHOULD prevent speculative features, abstraction, configuration, and extension points. It MUST NOT be used to ignore explicitly planned compatibility or known variations.

### 17.3 DRY

DRY SHOULD target duplicated knowledge, business rules, and authoritative definitions. Textually similar code MAY remain separate when it represents different concepts or is likely to evolve independently.

### 17.4 SOLID

SOLID principles SHOULD be applied selectively to object and module design. They MUST NOT require interfaces, classes, inheritance, or dependency injection where simpler functions, values, modules, or composition are sufficient.

### 17.5 Fail fast

Invalid internal states and violated contracts SHOULD fail near their origin. External integration boundaries MAY normalize tolerated syntax, but ambiguous or unsafe semantics MUST be rejected.

### 17.6 Composition over inheritance

Composition SHOULD be preferred when it provides clearer ownership and variation. Inheritance MAY be appropriate for true substitutability, framework contracts, or carefully controlled polymorphism.

### 17.7 Immutability

Immutable values SHOULD be preferred where they simplify reasoning and concurrency. Controlled mutation MAY be appropriate for entities, UI state, high-performance paths, and framework-managed lifecycles.

### 17.8 Backward compatibility

Public contracts SHOULD be preserved according to the declared compatibility policy. Internal implementation details MAY change atomically when all consumers are updated together.

### 17.9 Performance

Performance complexity MUST be justified by at least one of:

- measurement;
- a specified budget;
- a known data scale;
- a hard runtime constraint;
- a demonstrated hot path;
- a real-time or resource-constrained environment.

### 17.10 Testing

Tests SHOULD protect behavior and risk, not merely implementation structure. “One assertion per test” MUST be interpreted as one coherent behavior per test, not necessarily one assertion statement.

## 18. Task-scope behavior

### 18.1 Local implementation task

The visible policy summary MAY be omitted when the selected policy is obvious and no important conflict exists.

### 18.2 Architecture or planning task

The model SHOULD report:

- selected project profile;
- important modifiers;
- architecture authority;
- major trade-offs;
- assumptions that could change the recommendation.

### 18.3 Code review task

The model SHOULD distinguish:

- correctness defects;
- security defects;
- contract violations;
- maintainability concerns;
- optional stylistic improvements.

Named principles SHOULD be used to explain evidence, not to replace evidence.

### 18.4 Legacy modification

The model MUST prefer bounded, reversible changes and SHOULD use characterization testing where behavior is not well documented.

## 19. Repository configuration

A repository MAY provide an `engineering-context.yaml` file validated against `schemas/project-context.schema.json`.

Repository configuration SHOULD include only stable project-wide decisions. Task-specific requirements remain in the user request.

The orchestrator MUST merge repository configuration with observed context and user instructions using the precedence rules in this specification.

## 20. Validation

Metadata and configuration files MUST be syntactically valid.

Before a component is considered stable:

- its metadata MUST validate against the appropriate schema;
- dependencies MUST be acyclic;
- identifiers MUST be unique;
- referenced skills and modes MUST exist;
- conflicts MUST define a resolution policy or escalation rule;
- examples MUST use canonical terminology;
- normative rules MUST distinguish MUST, SHOULD, and MAY behavior.

## 21. Versioning

The specification and each skill, profile, modifier, or adapter MUST use semantic versioning.

For foundation releases, the repository-level `VERSION` file is authoritative. The specification, schemas, catalogues, orchestrator metadata, examples, README, changelog, manifest, and archive name MUST use the same version. A future release MAY separate package, specification, schema, and component version lifecycles only after documenting and validating their compatibility rules.

Recommended interpretation:

- `PATCH` — clarification or correction that does not intentionally change resolved behavior;
- `MINOR` — backward-compatible new rule, mode, profile, adapter, or optional behavior;
- `MAJOR` — incompatible changes to precedence, context meaning, default modes, or resolution behavior.

Component status values are:

- `experimental`
- `draft`
- `candidate`
- `stable`
- `deprecated`

## 22. Compliance checklist

A conforming implementation MUST:

- separate project profiles from language adapters;
- include an orchestrator or equivalent resolution mechanism;
- preserve explicit user overrides;
- retain uncertainty instead of inventing context;
- support visible reporting of significant selected policy;
- implement deterministic precedence;
- provide conflict resolution;
- avoid global activation of irrelevant skills;
- validate machine-readable metadata;
- keep normative content in English.


## 23. Canonical principles registry

The system MUST maintain its complete normative principle catalogue locally under `principles/entries/`.

Each entry MUST define classification, canonical interpretation, rejected interpretations, trade-offs, known conflicts, reinforcing relationships, Core Skill ownership, and AI guidance.

A named concept MUST NOT automatically become an individual Skill. Core Skills group entries into coherent decision procedures.

## 24. Compendium requirement

The repository MUST expose the canonical knowledge in human-readable form. The compendium is a first-class project output, not merely internal prompt data.

Generated Markdown MUST identify its canonical YAML source and MUST NOT be edited as an independent normative source.

## 25. Self-containment

The installed plugin MUST operate without external Skill dependencies. External references MAY be supplementary but MUST NOT alter behavior, override policy, or be required for installation.

All Core Skills, profiles, modifiers, language adapters, and framework adapters MUST be versioned under project control.

## 26. Principle activation output

A resolved policy SHOULD identify materially active, constrained, and suppressed principles. When a conflict affects the result, the policy MUST state the selected interpretation and the protected quality attributes.
