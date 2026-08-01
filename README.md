# Code Principles

A self-contained, language-agnostic knowledge base and policy system for AI coding agents. It combines a broad software engineering compendium with context-aware Skills that select, interpret, and reconcile practices according to the actual project.

## What makes this project different

Most engineering Skill collections provide isolated prompts such as “Clean Code,” “SOLID,” or “TDD.” This project is designed around a wider and more controlled model:

- a canonical registry covering **72** principles, heuristics, techniques, methods, architecture rules, properties, laws, patterns, and umbrella concepts;
- explicit rejected interpretations and trade-offs for every catalogue entry;
- controlled Core Skills that group related entries into practical decision procedures;
- project profiles that configure Skills without duplicating their rules;
- modifiers for security, compatibility, performance, real-time, accessibility, and other constraints;
- production-shaped language adapters for JavaScript, TypeScript, Python, PHP, Go, and C++;
- production-shaped framework adapters for React, Next.js, Angular, Vue, Nuxt, Symfony, and Drupal;
- an orchestrator that detects context, resolves conflicts, and produces an explainable engineering policy;
- no dependency on externally maintained Skills.

The repository is a useful human-readable compendium and the foundation of a planned AI-agent plugin. Host-specific plugin packaging and installation support are not implemented yet.

## Status

- Foundation version: `0.8.0`
- Status: `Framework Adapters Complete`
- Content language: English
- Schema dialect: JSON Schema Draft 2020-12
- External Skill dependencies: none
- Repository name: `code-principles`

This repository defines the knowledge model, canonical principle catalogue, schemas, validation tooling,
an executable deterministic orchestrator, six production-shaped language-independent Core Skills, five
operational project profiles, complete JavaScript, TypeScript, Python, PHP, Go, and C++ language adapters,
and complete React, Next.js, Vue, Nuxt, Angular, Symfony, and Drupal framework adapters.

## Resolution model

```text
User request and repository evidence
        ↓
Normalized project context
        ↓
Language-independent project profile
        ↓
Cross-cutting modifiers
        ↓
Controlled Core Skills and modes
        ↓
Language and framework refinements
        ↓
Principle conflict resolution
        ↓
Resolved engineering policy
        ↓
Task execution and review
```

The project type is more important than the implementation language. A public Python library is governed primarily as a reusable public library, then refined by Python-specific semantics.

## Authority and precedence

```text
Safety, correctness, and data integrity
> explicit current user requirements
> explicit repository configuration
> verified existing project constraints and conventions
> selected project profile
> active modifiers
> controlled Core Skill modes
> language and framework refinements
> default heuristics
```

An adapter MAY explain how a principle is realized in a technology. It MUST NOT silently redefine the canonical principle.

## Self-contained content policy

All normative principles, Core Skills, profiles, modifiers, language adapters, and framework adapters are maintained in this repository and versioned together.

External resources MAY be cited for history or further reading, but:

- they are never required at runtime;
- they are not installed as Skill dependencies;
- they cannot override the resolved policy;
- upstream changes cannot silently change this project’s behavior.

## Foundation package structure

```text
.
├── README.md
├── SPECIFICATION.md
├── ARCHITECTURE.md
├── KNOWLEDGE-MODEL.md
├── SELF-CONTAINMENT.md
├── TERMINOLOGY.md
├── CONFLICT-RESOLUTION.md
├── CONTRIBUTING.md
├── ROADMAP.md
├── CHANGELOG.md
├── VERSION
├── engineering-context.example.yaml
├── principles/
│   ├── README.md
│   ├── CLASSIFICATION.md
│   ├── AUTHORING-GUIDE.md
│   ├── registry.yaml
│   ├── relationships.yaml
│   ├── entries/          # canonical YAML sources
│   ├── compendium/       # generated human-readable pages
│   └── categories/       # generated category views
├── catalogs/
│   ├── core-skills.yaml
│   ├── profiles.yaml
│   ├── modifiers.yaml
│   ├── languages.yaml
│   └── frameworks.yaml
├── schemas/
├── orchestrator/
├── core/                 # implemented Core Skills
├── profiles/             # implemented project profiles
├── languages/            # implemented language adapters
├── frameworks/           # implemented framework adapters
├── tools/
└── requirements-dev.txt
```

## Quick validation

```bash
python3 -m pip install -r requirements-dev.txt
make validate
```

The validation command parses every distributed YAML and JSON document with duplicate-key detection,
validates schemas and known instances, checks identifier uniqueness, verifies references and dependency
graphs, confirms generated output and manifest freshness, and validates local Markdown links. It does not
rewrite the repository. The same command runs negative fixtures that prove malformed documents, schema
violations, duplicate identifiers, dependency cycles, broken references, and broken links are rejected.

To additionally reject inconsistently cased normative keywords:

```bash
make validate-normative
```

## Resolve a policy

The Orchestrator MVP inspects bounded repository evidence, automatically loads
`engineering-context.yaml` when present, and accepts a higher-precedence partial user context:

```bash
python3 tools/orchestrate.py \
  --repository . \
  --task "Implement a payment webhook" \
  --user-context user-context.yaml
```

Use `--format summary` for the compact visible result, or `--format json` for JSON instead of the
default schema-validated YAML. Direct user overrides are also available for common manual cases:

```bash
python3 tools/orchestrate.py \
  --profile reusable-library \
  --modifier public-api \
  --skill-mode abstraction-and-reuse=conservative
```

Merge precedence is detected evidence, repository context, then user context. Explicit user skill-mode
overrides therefore take precedence over repository skill-mode overrides. The base profile is selected
from artifact and lifecycle evidence; detected languages and frameworks only select refinements.

Before creating a release archive, regenerate the content and manifest, validate them, and package the controlled distribution set:

```bash
make package
```

## Important scope boundary

Not every blueprint is a finished production component. The six Milestone 4 Core Skills, five Milestone 5
project profiles, all six target language adapters, all seven framework adapters, and orchestrator have
detailed guidance. Modifiers and extended Core Skills remain scheduled for later milestones. The canonical
principle catalogue is usable immediately as a compendium and as the source for resolved Skill behavior.

## License

Code Principles is released under the [MIT License](LICENSE).
