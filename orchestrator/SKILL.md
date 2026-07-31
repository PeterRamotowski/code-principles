# Code Principles Orchestrator

## Purpose

The Code Principles Orchestrator determines which engineering policies apply to a software task. It converts user instructions and project evidence into a task-scoped resolved policy.

The orchestrator is a router and decision resolver. It is not a universal “clean code” prompt and MUST NOT contain the complete guidance of every core skill, project profile, language, or framework.

## Scope

Activate this skill for software-related tasks involving one or more of:

- implementation;
- modification;
- refactoring;
- code review;
- architecture;
- technical planning;
- testing strategy;
- API design;
- performance analysis;
- migration;
- library design;
- framework extension;
- repository policy.

## Non-goals

The orchestrator MUST NOT:

- choose architecture from language or framework name alone;
- treat every task as a greenfield design;
- require the user to select dozens of individual principles;
- activate every available skill for every task;
- silently invent project constraints;
- replace existing project conventions during an unrelated local change;
- present profile selection as objectively correct when evidence is incomplete;
- use principle names as substitutes for concrete reasoning;
- produce a large visible policy dump for a trivial task;
- block reversible work because nonessential context is unknown.

## Inputs

The orchestrator MAY use:

1. the current user request;
2. explicit user constraints and overrides;
3. repository configuration such as `engineering-context.yaml`;
4. repository manifests and file structure;
5. existing source code and tests;
6. deployment and runtime configuration;
7. public API declarations and package metadata;
8. prior stable project decisions available in the current project context.

The orchestrator MUST distinguish current-task instructions from stable repository policy.

## Outputs

For a non-trivial task, the orchestrator MUST internally produce:

- normalized project context;
- one primary base profile;
- active modifiers;
- selected language adapters;
- selected framework adapters;
- active core skills and modes;
- applied overrides;
- significant conflict resolutions;
- significant decisions;
- unresolved uncertainties;
- prohibited decisions where relevant.

The output SHOULD conform to `schemas/resolved-policy.schema.json`.

## Selection modes

### Automatic with visible result

Identifier: `automatic-with-visible-result`

This is the default mode.

The orchestrator MUST:

- resolve the policy automatically;
- proceed without confirmation for ordinary, local, and reversible work;
- report significant policy choices when they affect the result;
- state material uncertainty without turning it into a blocker.

### Propose

Identifier: `propose`

The orchestrator SHOULD show the proposed policy before decisions that are expensive, public, security-sensitive, or difficult to reverse.

It MUST NOT ask for confirmation for trivial implementation details unless the user explicitly requests review before changes.

### Manual

Identifier: `manual`

The orchestrator MUST use explicit profile, modifier, adapter, and skill-mode configuration.

It MAY reject or flag a manual configuration when:

- a referenced component does not exist;
- dependencies are cyclic;
- the configuration contradicts language or runtime semantics;
- a lower-priority override conflicts with safety or correctness;
- required values are missing and cannot be conservatively resolved.

## Decision precedence

Apply this order:

1. safety, correctness, and data integrity;
2. explicit current user requirements;
3. explicit repository engineering configuration;
4. verified existing project constraints and conventions;
5. base project profile;
6. modifiers;
7. language adapters;
8. framework adapters;
9. core skill defaults;
10. style preferences.

A lower-precedence component MUST NOT silently override a higher-precedence instruction.

## Operating procedure

### Step 1: Determine task scope

Classify the task as one or more of:

- local implementation;
- local modification;
- code review;
- refactor;
- architecture design;
- project planning;
- migration;
- performance work;
- public API work;
- security-sensitive work;
- repository-wide policy work.

Task scope determines how much context and visible reporting are necessary.

### Step 2: Collect explicit facts

Extract direct statements about:

- artifact type;
- project stage;
- public exposure;
- architecture authority;
- language and framework;
- runtime;
- constraints;
- compatibility requirements;
- required and forbidden patterns;
- expected deliverables.

Explicit facts have higher confidence than repository inference.

### Step 3: Inspect repository evidence when available

Use repository evidence to detect:

- manifests and lock files;
- language files;
- framework configuration;
- directory structure;
- package publishing configuration;
- public exports;
- deployment environment;
- test infrastructure;
- existing architecture patterns;
- legacy constraints;
- generated code boundaries.

Do not inspect unrelated repository areas when the task is clearly local and context is already sufficient.

### Step 4: Normalize context

Normalize findings using the canonical vocabulary from `TERMINOLOGY.md` and `schemas/project-context.schema.json`.

For each material value, record confidence:

- `explicit`;
- `observed`;
- `inferred-high`;
- `inferred-low`;
- `unknown`.

Unknown values MUST remain unknown.

### Step 5: Resolve architecture authority

Architecture authority is critical for existing projects.

Use:

- `preserve-existing` for bug fixes and narrow changes unless broader change is authorized;
- `incremental-improvement` when bounded refactoring is allowed;
- `redesign-allowed` when the task requests broader restructuring;
- `greenfield` for new designs with no established architecture.

When authority is unknown, default to `preserve-existing` for local tasks and `incremental-improvement` for planning that explicitly asks for improvement proposals.

### Step 6: Select the base profile

Select one primary profile based primarily on:

1. artifact type;
2. exposure and compatibility;
3. project stage;
4. domain complexity;
5. state and distribution model;
6. operational constraints;
7. existing architecture;
8. technology context.

Do not select a profile solely because a framework is present.

Examples:

- Next.js product with browser and server execution: `fullstack-web-application`;
- published Python package: `reusable-library`;
- Go HTTP daemon: `backend-service`;
- C++ control component with timing guarantees: `real-time-system`;
- Drupal module extending a host application: `plugin-or-extension`;
- Python batch transformer processing large files: `data-pipeline`.

### Step 7: Activate modifiers

Activate only modifiers supported by evidence.

Typical triggers:

- external consumers or published package: `public-api` or `strict-backward-compatibility`;
- credentials, payments, personal data, authorization, or sensitive operations: `security-sensitive`;
- explicit throughput budget or large event volume: `high-throughput`;
- large datasets or constrained environment: `memory-sensitive`;
- explicit response-time budget: `latency-sensitive`;
- hard execution deadlines: `real-time`;
- tenant-isolated data and authorization: `multi-tenant`;
- required WCAG or inclusive interaction behavior: `accessibility-required`;
- disconnected operation and synchronization: `offline-first`.

Do not label every web application security-sensitive merely because all software needs secure behavior. Use the modifier when security materially changes policy intensity or verification.

### Step 8: Select technology adapters

Select language adapters for languages materially affected by the task.

Select framework adapters when framework semantics affect the decision.

Examples:

- a TypeScript type utility in a React repository may need TypeScript but not React guidance;
- a React state-management task needs React and the underlying JavaScript or TypeScript adapter;
- a Next.js server/client boundary task needs Next.js, React, and TypeScript or JavaScript;
- a Symfony service configuration task needs PHP and Symfony;
- a Drupal cache invalidation task needs PHP, Symfony where relevant, and Drupal;
- a Python packaging task needs Python but not a web-framework adapter.

### Step 9: Activate core skills

Activate skills relevant to the current decision.

Examples:

- local readability change: `code-clarity`;
- shared abstraction proposal: `abstraction-and-reuse`;
- class and module boundaries: `modular-design`;
- request parsing and errors: `contracts-and-errors`;
- public package change: `api-and-compatibility`;
- memory optimization: `performance`;
- legacy fix: `safe-change` and `testing-strategy`;
- retries and message duplication: `distributed-reliability`.

Do not activate distributed-systems guidance for an ordinary local function.

### Step 10: Resolve skill modes

Use this merge order:

```text
core default
→ base profile
→ modifier
→ language adapter refinement
→ framework adapter refinement
→ repository override
→ user override
```

Higher-precedence safety and correctness rules remain binding.

### Step 11: Detect conflicts

Detect conflicts when selected policies recommend materially different actions.

Common examples:

- DRY versus YAGNI;
- public compatibility versus API cleanup;
- immutability versus framework lifecycle;
- dependency inversion versus framework-native simplicity;
- performance versus readability;
- strict validation versus tolerant external integration;
- local improvement versus minimal task scope.

Use `CONFLICT-RESOLUTION.md` and `orchestrator/conflict-resolution.md`.

### Step 12: Produce significant decisions

A significant decision should state:

- the selected behavior;
- why it applies;
- its scope;
- when it should be reconsidered, if relevant.

Examples:

- Keep the public API backward compatible and use deprecation for renames.
- Validate webhook data at runtime even when TypeScript types are available.
- Stream input records because memory sensitivity is high.
- Preserve the existing framework-native architecture for this local change.
- Do not introduce CQRS without a demonstrated read/write scaling or domain need.

### Step 13: Execute the task

Apply the resolved policy proportionally.

The final answer or code SHOULD show the effect of the policy without becoming a lecture about every activated principle.

### Step 14: Review the result

Before completion, verify:

- explicit requirements are satisfied;
- no selected rule exceeded its scope;
- public compatibility is handled as configured;
- external input is validated where required;
- architecture authority was respected;
- performance claims are supported;
- significant trade-offs are visible;
- no unrelated redesign was introduced.

## Context-specific defaults

### Local change in an existing repository

Default behavior:

- architecture authority: `preserve-existing`;
- prefer repository conventions;
- make the smallest coherent change;
- allow small local cleanup;
- do not migrate frameworks or architecture;
- test the changed behavior.

### Greenfield architecture task

Default behavior:

- architecture authority: `greenfield`;
- select the simplest profile-compatible architecture;
- identify known constraints;
- avoid speculative distribution and extensibility;
- expose major trade-offs.

### Public library task

Default behavior:

- minimal intentional public surface;
- strict contract clarity;
- runtime boundary validation where relevant;
- compatibility and deprecation policy;
- low dependency footprint;
- framework independence unless framework integration is the library purpose.

### Legacy modernization task

Default behavior:

- preserve observed behavior unless change is explicit;
- add characterization tests around risky paths;
- prefer incremental and reversible changes;
- separate behavior change from broad refactoring;
- investigate before removing unexplained mechanisms.

## Visible reporting rules

The orchestrator SHOULD show a concise summary when:

- designing architecture;
- selecting among meaningful profiles;
- making public API decisions;
- applying high-impact modifiers;
- resolving a material conflict;
- relying on an assumption that could change the answer.

Example:

```yaml
resolved_context:
  profile: fullstack-web-application
  modifiers: [public-api, security-sensitive]
  language_adapters: [typescript]
  framework_adapters: [react, nextjs]
  architecture_authority: incremental-improvement

significant_decisions:
  - Keep server-side validation authoritative.
  - Preserve public API compatibility.
  - Avoid CQRS until a concrete scaling or workflow need appears.
```

For a small function fix, visible reporting may be limited to a sentence explaining an important exception.

## Uncertainty handling

The orchestrator MUST NOT ask questions that repository evidence or conservative defaults can resolve safely.

It SHOULD ask or present alternatives when uncertainty affects:

- public compatibility;
- security or data integrity;
- irreversible architecture;
- expensive technology commitment;
- protocol or persistence format;
- hard real-time or performance guarantees.

When proceeding under uncertainty, record the default action.

Example:

> Public API status is unclear. Treat the changed export as internal for this task, but avoid unnecessary renaming until consumers are confirmed.

## Prohibited behavior

The orchestrator MUST NOT:

- infer domain-driven design from the presence of classes;
- infer microservices from a backend-service request;
- infer CQRS from separate read and write functions;
- infer public API from language visibility alone;
- infer runtime validation from static typing;
- infer performance requirements from a developer's preference for speed;
- infer greenfield authority in an existing repository;
- replace Redux, Doctrine, an ORM, or a framework merely because an alternative is popular;
- create an interface for every implementation;
- force rich domain objects into data transformation pipelines;
- use “best practice” without explaining the applicable context.

## Review checklist

Before applying a resolved policy, confirm:

- [ ] The artifact type is based on the deliverable, not just the language.
- [ ] Project stage and exposure are separated.
- [ ] Architecture authority is explicit or conservatively defaulted.
- [ ] Constraints are evidence-based.
- [ ] Exactly one primary profile is selected for the task scope.
- [ ] Modifiers are narrow and justified.
- [ ] Language and framework adapters match the affected code.
- [ ] Only relevant core skills are active.
- [ ] User and repository overrides are preserved.
- [ ] Material conflicts are resolved using evidence and consequences.
- [ ] Significant decisions are concise and traceable.
- [ ] The implementation respects existing project conventions.


## Canonical principle authority

The orchestrator MUST resolve engineering guidance from the local canonical registry and controlled Core Skills. It MUST NOT recommend or load an external Skill as a substitute for missing local policy.

For material decisions, the internal resolved policy SHOULD record:

- active canonical principle IDs;
- the context-specific interpretation selected by the owning Core Skill;
- constrained or suppressed principles;
- rejected common behaviours;
- conflicts and protected quality attributes.

The orchestrator may cite an external resource for explanation, but that resource has no policy authority.
