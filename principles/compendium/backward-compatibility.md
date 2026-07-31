---
id: backward-compatibility
name: Backward Compatibility
classification: evolution-principle
category: api-and-evolution
status: candidate
source: principles/entries/backward-compatibility.yaml
generated: true
---

# Backward Compatibility

> Preserve existing consumer behavior across compatible releases.

## Canonical interpretation

Protect intentional public contracts and provide migration or deprecation paths for necessary breaking changes.

## Purpose

Preserve existing consumer behavior across compatible releases.

## Apply when

- Consumers cannot be updated atomically with the implementation.
- Observable behavior or data formats form an external contract.

## This does not mean

- Do not preserve every internal implementation detail.
- Do not keep unsafe behavior indefinitely without a security transition plan.

## Trade-offs

- Compatibility limits refactoring freedom.
- Preserving accidental behavior can accumulate long-term complexity.

## Conflicts with canonical entries

- `kiss`

## Broader policy tensions

- `refactoring-freedom`
- `security-hardening`

## Reinforces canonical entries

- `hyrums-law`
- `semantic-versioning`

## Supports broader concerns

- None recorded.

## Core Skill ownership

Primary owner: `api-and-compatibility`

## Positive example

Add a field without changing existing response semantics and document deprecation before removal.

## Counterexample

Rename a public field in a patch release without migration.

## Guidance for AI models

- Apply this guidance only after considering the active project profile, constraints, and architecture authority.
- State the concrete design consequence instead of citing the principle name as sufficient justification.

## Editorial note

This page is generated from the canonical YAML entry. Edit `principles/entries/backward-compatibility.yaml` and regenerate the compendium instead of editing this file directly.
