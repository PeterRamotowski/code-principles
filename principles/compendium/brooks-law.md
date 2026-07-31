---
id: brooks-law
name: Brooks’s Law
classification: law
category: change-and-engineering-systems
status: candidate
source: principles/entries/brooks-law.yaml
generated: true
---

# Brooks’s Law

> Adding people to a late software project can make it later.

## Canonical interpretation

Account for onboarding and communication overhead when changing staffing under schedule pressure.

## Purpose

Adding people to a late software project can make it later.

## Apply when

- The project is being evolved, modernized, reviewed, or reorganized.
- Organizational and historical context affects technical outcomes.

## This does not mean

- Do not conclude that staffing never helps.
- Do not use the law to avoid addressing chronic understaffing.

## Trade-offs

- Local improvement can enlarge the scope and risk of a change.
- Organizational laws are diagnostic lenses, not deterministic commands.

## Conflicts with canonical entries

- None recorded.

## Broader policy tensions

- `deadline-pressure`

## Reinforces canonical entries

- `conways-law`

## Supports broader concerns

- None recorded.

## Core Skill ownership

Primary owner: `engineering-review-lenses`

## Positive example

Add contributors to separable work with onboarding capacity instead of the critical path.

## Counterexample

Put many new developers into a tightly coupled late subsystem and expect immediate acceleration.

## Guidance for AI models

- Apply this guidance only after considering the active project profile, constraints, and architecture authority.
- State the concrete design consequence instead of citing the principle name as sufficient justification.

## Editorial note

This page is generated from the canonical YAML entry. Edit `principles/entries/brooks-law.yaml` and regenerate the compendium instead of editing this file directly.
