---
id: ports-and-adapters
name: Ports and Adapters
classification: architecture-style
category: architecture-and-dependencies
status: candidate
source: principles/entries/ports-and-adapters.yaml
generated: true
---

# Ports and Adapters

> Place application policy behind explicit ports and implement external interactions through adapters.

## Canonical interpretation

Use the style when independent evolution from infrastructure is valuable; scale the number of ports to actual boundaries.

## Purpose

Place application policy behind explicit ports and implement external interactions through adapters.

## Apply when

- High-level policy must evolve independently from volatile infrastructure.
- Dependency direction affects testability, deployability, or independent ownership.

## This does not mean

- Do not wrap every framework function in an adapter.
- Do not force a simple CRUD application into many layers without domain or portability needs.

## Trade-offs

- Indirection and adapters have a maintenance cost.
- Framework isolation is valuable only where independent evolution is required.

## Conflicts with canonical entries

- `kiss`

## Broader policy tensions

- `framework-native-design`

## Reinforces canonical entries

- `dependency-inversion-principle`
- `information-hiding`

## Supports broader concerns

- None recorded.

## Core Skill ownership

Primary owner: `dependencies-and-boundaries`

## Positive example

Isolate a public library’s storage integration behind a small port.

## Counterexample

Create ports for string formatting, logging syntax, and every local helper.

## Guidance for AI models

- Apply this guidance only after considering the active project profile, constraints, and architecture authority.
- State the concrete design consequence instead of citing the principle name as sufficient justification.

## Editorial note

This page is generated from the canonical YAML entry. Edit `principles/entries/ports-and-adapters.yaml` and regenerate the compendium instead of editing this file directly.
