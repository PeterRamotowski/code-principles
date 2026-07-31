---
id: galls-law
name: Gall’s Law
classification: law
category: change-and-engineering-systems
status: candidate
source: principles/entries/galls-law.yaml
generated: true
---

# Gall’s Law

> Working complex systems generally evolve from working simpler systems.

## Canonical interpretation

Prefer evolutionary growth from validated foundations over designing a complete complex system in one step.

## Purpose

Working complex systems generally evolve from working simpler systems.

## Apply when

- The project is being evolved, modernized, reviewed, or reorganized.
- Organizational and historical context affects technical outcomes.

## This does not mean

- Do not assume every simple system can evolve into any complex target.
- Do not avoid necessary architectural preparation for known constraints.

## Trade-offs

- Local improvement can enlarge the scope and risk of a change.
- Organizational laws are diagnostic lenses, not deterministic commands.

## Conflicts with canonical entries

- None recorded.

## Broader policy tensions

- `big-design-up-front`

## Reinforces canonical entries

- `kiss`
- `make-it-work-right-fast`

## Supports broader concerns

- None recorded.

## Core Skill ownership

Primary owner: `engineering-review-lenses`

## Positive example

Deliver a small working workflow and evolve it with observed needs.

## Counterexample

Launch an untested platform containing every anticipated subsystem.

## Guidance for AI models

- Apply this guidance only after considering the active project profile, constraints, and architecture authority.
- State the concrete design consequence instead of citing the principle name as sufficient justification.

## Editorial note

This page is generated from the canonical YAML entry. Edit `principles/entries/galls-law.yaml` and regenerate the compendium instead of editing this file directly.
