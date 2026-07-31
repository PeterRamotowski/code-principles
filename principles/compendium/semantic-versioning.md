---
id: semantic-versioning
name: Semantic Versioning
classification: versioning-method
category: api-and-evolution
status: candidate
source: principles/entries/semantic-versioning.yaml
generated: true
---

# Semantic Versioning

> Communicate compatibility impact through major, minor, and patch versions.

## Canonical interpretation

Apply SemVer to a clearly defined public API; version numbers cannot replace documented compatibility policy.

## Purpose

Communicate compatibility impact through major, minor, and patch versions.

## Apply when

- Consumers cannot be updated atomically with the implementation.
- Observable behavior or data formats form an external contract.

## This does not mean

- Do not claim SemVer when the public API is undefined.
- Do not assume every observable bug fix is non-breaking for every consumer.

## Trade-offs

- Compatibility limits refactoring freedom.
- Preserving accidental behavior can accumulate long-term complexity.

## Conflicts with canonical entries

- `hyrums-law`

## Broader policy tensions

- `security-fix`

## Reinforces canonical entries

- `backward-compatibility`

## Supports broader concerns

- None recorded.

## Core Skill ownership

Primary owner: `api-and-compatibility`

## Positive example

Release a breaking public API change in a new major version with migration notes.

## Counterexample

Ship incompatible behavior as a patch because the code change is small.

## Guidance for AI models

- Apply this guidance only after considering the active project profile, constraints, and architecture authority.
- State the concrete design consequence instead of citing the principle name as sufficient justification.

## Editorial note

This page is generated from the canonical YAML entry. Edit `principles/entries/semantic-versioning.yaml` and regenerate the compendium instead of editing this file directly.
