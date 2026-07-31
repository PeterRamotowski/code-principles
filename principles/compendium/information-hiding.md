---
id: information-hiding
name: Information Hiding
classification: principle
category: modularity-and-object-design
status: candidate
source: principles/entries/information-hiding.yaml
generated: true
---

# Information Hiding

> Hide volatile design decisions behind stable boundaries.

## Canonical interpretation

A module should expose what consumers need while retaining freedom to change implementation details.

## Purpose

Hide volatile design decisions behind stable boundaries.

## Apply when

- Responsibilities change for different reasons or at different rates.
- A boundary can reduce coupling or protect an invariant.

## This does not mean

- Do not hide information required for observability or correct use.
- Do not create opaque abstractions with undocumented behavior.

## Trade-offs

- More modules and interfaces increase navigation and integration cost.
- A boundary that does not protect independent change can become ceremony.

## Conflicts with canonical entries

- None recorded.

## Broader policy tensions

- `debuggability`
- `performance-control`

## Reinforces canonical entries

- `encapsulation`
- `open-closed-principle`

## Supports broader concerns

- None recorded.

## Core Skill ownership

Primary owner: `modular-design`

## Positive example

Expose a storage contract without leaking database-specific query objects.

## Counterexample

Return internal mutable collections that callers can modify freely.

## Guidance for AI models

- Apply this guidance only after considering the active project profile, constraints, and architecture authority.
- State the concrete design consequence instead of citing the principle name as sufficient justification.

## Editorial note

This page is generated from the canonical YAML entry. Edit `principles/entries/information-hiding.yaml` and regenerate the compendium instead of editing this file directly.
