# Canonical Principles Registry

This directory is the controlled knowledge base for the project. It is both:

1. the authoritative source used by the orchestrator and Core Skills; and
2. a human-readable compendium of software engineering practices and principles.

The registry currently contains **72** entries derived from the initial project scope. It intentionally distinguishes principles from heuristics, techniques, architecture styles, system properties, testing patterns, development methods, organizational laws, and umbrella concepts.

## Source-of-truth policy

- `entries/*.yaml` files are canonical.
- `registry.yaml` is a generated machine-readable index.
- `relationships.yaml` records cross-entry relationships.
- `INDEX.md`, `categories/*.md`, and `compendium/*.md` are generated views.
- Generated Markdown MUST NOT become an independent normative source.

## Why entries are not individual Skills

A named idea is not automatically a useful standalone AI Skill. Several entries are too broad, too contextual, descriptive rather than prescriptive, or meaningful only in combination with other rules. Core Skills group related entries into decision procedures with modes, exceptions, and conflict handling.

For example, `dry`, `yagni`, `open-closed-principle`, `single-source-of-truth`, and `premature-generalization` are owned primarily by the future `abstraction-and-reuse` Core Skill.

## Self-containment

The canonical entries and the future Core Skills are maintained in this repository. No external Skill is required to interpret or apply a principle. External books, papers, repositories, and articles MAY be cited as references, but they are non-authoritative and cannot change runtime policy.

## Regeneration

```bash
python3 tools/generate_compendium.py
```

Run validation after regeneration:

```bash
python3 tools/validate.py
```
