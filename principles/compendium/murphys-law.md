---
id: murphys-law
name: Murphy’s Law
classification: law
category: change-and-engineering-systems
status: candidate
source: principles/entries/murphys-law.yaml
generated: true
---

# Murphy’s Law

> Failure paths that are possible should be expected over sufficient time and scale.

## Canonical interpretation

Design proportionate safeguards for plausible failures rather than assuming ideal operation.

## Purpose

Failure paths that are possible should be expected over sufficient time and scale.

## Apply when

- The project is being evolved, modernized, reviewed, or reorganized.
- Organizational and historical context affects technical outcomes.

## This does not mean

- Do not attempt to defend against every imaginable scenario.
- Do not replace risk analysis with pessimism.

## Trade-offs

- Local improvement can enlarge the scope and risk of a change.
- Organizational laws are diagnostic lenses, not deterministic commands.

## Conflicts with canonical entries

- `kiss`

## Broader policy tensions

- `cost-control`

## Reinforces canonical entries

- `defensive-programming`

## Supports broader concerns

- `observability`

## Core Skill ownership

Primary owner: `engineering-review-lenses`

## Positive example

Handle network timeout and retry semantics in an external integration.

## Counterexample

Assume a remote service will always return once and exactly once.

## Guidance for AI models

- Apply this guidance only after considering the active project profile, constraints, and architecture authority.
- State the concrete design consequence instead of citing the principle name as sufficient justification.

## Editorial note

This page is generated from the canonical YAML entry. Edit `principles/entries/murphys-law.yaml` and regenerate the compendium instead of editing this file directly.
