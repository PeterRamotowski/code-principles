---
id: law-of-demeter
name: Law of Demeter
classification: heuristic
category: modularity-and-object-design
status: candidate
source: principles/entries/law-of-demeter.yaml
generated: true
---

# Law of Demeter

> Limit knowledge of distant object structure and collaboration chains.

## Canonical interpretation

Collaborate through direct dependencies and stable operations rather than navigating internal object graphs.

## Purpose

Limit knowledge of distant object structure and collaboration chains.

## Apply when

- Responsibilities change for different reasons or at different rates.
- A boundary can reduce coupling or protect an invariant.

## This does not mean

- Do not wrap every property access in a forwarding method.
- Do not apply the rule mechanically to transparent data records.

## Trade-offs

- More modules and interfaces increase navigation and integration cost.
- A boundary that does not protect independent change can become ceremony.

## Conflicts with canonical entries

- `locality-of-behaviour`

## Broader policy tensions

- `data-transfer-objects`

## Reinforces canonical entries

- `information-hiding`

## Supports broader concerns

- `low-coupling`

## Core Skill ownership

Primary owner: `modular-design`

## Positive example

Ask an order to calculate its total instead of traversing internal line-item implementation details.

## Counterexample

Use `a.getB().getC().getD().execute()` across module boundaries.

## Guidance for AI models

- Apply this guidance only after considering the active project profile, constraints, and architecture authority.
- State the concrete design consequence instead of citing the principle name as sufficient justification.

## Editorial note

This page is generated from the canonical YAML entry. Edit `principles/entries/law-of-demeter.yaml` and regenerate the compendium instead of editing this file directly.
