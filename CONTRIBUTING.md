# Contributing

## 1. Purpose

This repository defines reusable engineering policy for AI coding assistants. Contributions must preserve consistency, explicit scope, and machine-readable contracts.

All normative repository content MUST be written in English.

## 2. Contribution types

Contributions may add or update:

- foundation documentation;
- core skills;
- project profiles;
- modifiers;
- language adapters;
- framework adapters;
- schemas;
- examples;
- evaluation scenarios;
- validation tooling.

## 3. Before adding a component

Before creating a new component, determine whether the guidance belongs in an existing one.

### Add a core skill only when:

- the topic applies across multiple languages and project types;
- it owns a coherent decision responsibility;
- it requires distinct modes, conflicts, or checks;
- placing it in an existing skill would reduce cohesion.

### Add a profile only when:

- the artifact class has a distinct quality-priority model;
- the difference cannot be expressed by modifiers;
- the profile is language-independent.

### Add a modifier only when:

- the concern applies across multiple profiles;
- it changes priorities or requirements without defining the whole project;
- it can be independently activated.

### Add an adapter only when:

- language or framework semantics materially refine core guidance;
- the content cannot be expressed as a generic core rule;
- the adapter avoids duplicating its parent language or profile.

## 4. Normative language

Use requirement levels deliberately:

- `MUST` or `MUST NOT` for binding rules within scope;
- `SHOULD` or `SHOULD NOT` for strong defaults that admit contextual exceptions;
- `MAY` for allowed options.

Avoid ambiguous commands such as:

- “always keep functions short”;
- “never use inheritance”;
- “all dependencies need interfaces”;
- “all code must be immutable”;
- “every project should use Clean Architecture.”

Prefer contextual rules such as:

> A function SHOULD represent one coherent operation at one primary level of abstraction. Length alone MUST NOT determine extraction.

## 5. Required component structure

### 5.1 Core skill

```text
core/<skill-id>/
├── SKILL.md
├── skill.yaml
└── examples/
```

Recommended `SKILL.md` headings:

```text
# Skill name
## Purpose
## Scope
## Non-goals
## Activation signals
## Supported modes
## Mandatory rules
## Preferred heuristics
## Allowed exceptions
## Conflicts
## Conflict resolution
## Decision procedure
## Positive examples
## Counterexamples
## Review checklist
## Expected output
```

### 5.2 Profile

```text
profiles/<profile-id>/
├── PROFILE.md
└── profile.yaml
```

A profile MUST define:

- intended artifact type;
- non-goals;
- priority order;
- default skill modes;
- typical modifiers;
- expected risks;
- prohibited default assumptions.

### 5.3 Adapter

```text
languages/<adapter-id>/
├── SKILL.md
├── adapter.yaml
└── optional-topic-documents.md
```

or:

```text
frameworks/<adapter-id>/
├── SKILL.md
├── adapter.yaml
└── examples/
```

An adapter MUST define:

- language or framework scope;
- parent adapters;
- refined core skills;
- runtime or lifecycle constraints;
- common misuse patterns;
- compatibility considerations;
- examples and counterexamples.

## 6. Metadata requirements

Metadata MUST validate against the relevant schema.

Identifiers MUST:

- use lowercase kebab-case;
- be globally unique within their component type;
- remain stable after a component reaches `candidate` status;
- describe responsibility rather than implementation technology where possible.

Dependencies MUST be explicit and acyclic.

Every declared mode MUST be documented in the human-readable component file.

## 7. Single source of truth

General engineering rules belong in core skills.

Profiles and adapters SHOULD reference core rules by identifier and mode. They MUST NOT independently redefine the same general rule.

Allowed refinement:

> Go interfaces SHOULD normally be defined by the consuming package and kept minimal.

Disallowed duplication:

> DRY means every repeated block must be extracted.

The definition of DRY belongs in the abstraction and reuse core skill.

## 8. Examples and counterexamples

Examples MUST illustrate decisions, not become hidden normative rules.

A useful example states:

- project context;
- selected mode;
- decision;
- why it fits;
- what alternative was rejected.

Counterexamples SHOULD include plausible overapplications, such as:

- adding interfaces to every class;
- creating a generic form engine for two similar forms;
- introducing CQRS for a small CRUD application;
- replacing framework conventions during a local bug fix;
- trusting external data because a static type says it is valid.

## 9. Conflict documentation

Each core skill MUST document at least three relevant conflicts or explicitly explain why fewer exist.

Each conflict MUST identify:

- the concrete decision;
- protected quality attributes;
- default resolution;
- conditions that change the resolution.

Conflicts that apply across multiple skills SHOULD be added to `CONFLICT-RESOLUTION.md`.

## 10. Definition of Done

A component is complete when:

1. its purpose and non-goals are explicit;
2. its activation conditions are machine-readable;
3. its metadata validates against the relevant schema;
4. it uses MUST, SHOULD, and MAY intentionally;
5. all supported modes are documented;
6. it explains relevant conflicts;
7. it includes positive examples and counterexamples;
8. it avoids language-specific content unless it is an adapter;
9. it does not duplicate another component's primary responsibility;
10. it defines expected output or observable behavior;
11. it has evaluation scenarios or references planned evaluations;
12. its dependencies are acyclic;
13. its terminology matches `TERMINOLOGY.md`;
14. its changes are reflected in `ROADMAP.md` or `CHANGELOG.md` when applicable.

## 11. Review checklist

Reviewers should verify:

### Scope

- Does the component have one coherent responsibility?
- Is it a skill, profile, modifier, or adapter for the correct reason?
- Are non-goals strong enough to prevent overreach?

### Correctness

- Are rules context-sensitive?
- Are exceptions safe and explicit?
- Do conflicts use quality attributes and evidence?
- Does precedence match the specification?

### Duplication

- Is general guidance copied from another component?
- Could a refinement reference an existing core skill mode instead?

### Technology neutrality

For profiles and core skills:

- Are language-specific APIs absent?
- Would the guidance remain valid for TypeScript, Python, PHP, Go, and C++?

### Adapter quality

- Does the adapter explain actual language or framework semantics?
- Does it avoid merely listing popular style rules?
- Does it distinguish compile-time guarantees from runtime guarantees?

### Model usability

- Can an AI model determine when to activate the component?
- Are outputs and prohibitions concrete?
- Are important assumptions visible?

## 12. Evaluation requirements

A new stable core skill or profile SHOULD include at least three scenarios:

- a straightforward positive case;
- a conflict or boundary case;
- an overengineering counterexample.

Language adapters SHOULD be tested against at least:

- an application task;
- a reusable-library task;
- a performance, error, or concurrency-sensitive task relevant to the language.

## 13. Change management

Use semantic versioning for each component.

### Patch

- wording clarification;
- typo correction;
- example correction;
- schema tightening that does not intentionally change valid behavior.

### Minor

- new optional mode;
- new non-breaking field;
- additional adapter refinement;
- new evaluation scenario.

### Major

- changed default mode;
- changed precedence;
- renamed stable identifier;
- incompatible schema change;
- materially different conflict resolution.

## 14. Pull request guidance

A contribution description should include:

- problem being solved;
- component type;
- why an existing component is insufficient;
- affected schemas or dependencies;
- new conflicts or precedence effects;
- evaluation evidence;
- compatibility impact.

## 15. Prohibited contribution patterns

Do not contribute:

- generic “clean code” lists without decision context;
- framework preferences disguised as universal principles;
- rules based only on line counts or class counts;
- unsupported claims of performance improvement;
- language adapters that repeat the language documentation without policy relevance;
- profiles named after languages or frameworks when an adapter is sufficient;
- examples that require a specific architecture without explaining why;
- metadata that references nonexistent modes;
- circular adapter or skill dependencies.


## Canonical principle contributions

Edit `principles/entries/*.yaml`, not generated compendium Markdown. Every new or materially changed entry must pass `schemas/principle.schema.json`, update relationships where needed, regenerate documentation, and include an evaluation impact review.

A contribution must preserve self-containment. It may add supplementary references but may not introduce a normative external Skill dependency.

## Repository validation

Install `requirements-dev.txt` and run `make validate` before submitting a change. This single command
checks syntax, schemas, identifiers, references, dependency cycles, generated content, the release
manifest, local Markdown links, and the negative validation fixtures. Run `make validate-normative` when
changing normative prose to also check RFC 2119-style keyword casing. The same commands run in CI.
