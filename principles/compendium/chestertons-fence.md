---
id: chestertons-fence
name: Chesterton’s Fence
classification: law
category: change-and-engineering-systems
status: candidate
source: principles/entries/chestertons-fence.yaml
generated: true
---

# Chesterton’s Fence

> Understand why an existing rule or mechanism exists before removing it.

## Canonical interpretation

Investigate historical constraints, users, and failure modes before deleting apparently unnecessary complexity.

## Purpose

Understand why an existing rule or mechanism exists before removing it.

## Apply when

- The project is being evolved, modernized, reviewed, or reorganized.
- Organizational and historical context affects technical outcomes.

## This does not mean

- Do not preserve obsolete code forever.
- Do not require perfect historical knowledge before reversible experiments.

## Trade-offs

- Local improvement can enlarge the scope and risk of a change.
- Organizational laws are diagnostic lenses, not deterministic commands.

## Conflicts with canonical entries

- `yagni`

## Broader policy tensions

- `simplification`

## Reinforces canonical entries

- None recorded.

## Supports broader concerns

- `characterization-testing`
- `safe-change`

## Core Skill ownership

Primary owner: `engineering-review-lenses`

## Positive example

Check incident history before removing a duplicated validation path.

## Counterexample

Delete a strange retry guard because no current test explains it.

## Guidance for AI models

- Apply this guidance only after considering the active project profile, constraints, and architecture authority.
- State the concrete design consequence instead of citing the principle name as sufficient justification.

## Editorial note

This page is generated from the canonical YAML entry. Edit `principles/entries/chestertons-fence.yaml` and regenerate the compendium instead of editing this file directly.
