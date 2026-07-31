---
id: boy-scout-rule
name: Boy Scout Rule
classification: change-principle
category: change-and-engineering-systems
status: candidate
source: principles/entries/boy-scout-rule.yaml
generated: true
---

# Boy Scout Rule

> Leave the code you touch slightly better than you found it.

## Canonical interpretation

Make bounded local improvements that support the task without turning every change into a broad rewrite.

## Purpose

Leave the code you touch slightly better than you found it.

## Apply when

- The project is being evolved, modernized, reviewed, or reorganized.
- Organizational and historical context affects technical outcomes.

## This does not mean

- Do not expand scope into unrelated refactoring.
- Do not change public behavior without requirement and review.

## Trade-offs

- Local improvement can enlarge the scope and risk of a change.
- Organizational laws are diagnostic lenses, not deterministic commands.

## Conflicts with canonical entries

- `backward-compatibility`

## Broader policy tensions

- `minimal-change-scope`

## Reinforces canonical entries

- None recorded.

## Supports broader concerns

- `safe-change`

## Core Skill ownership

Primary owner: `safe-change`

## Positive example

Rename a misleading local variable and remove dead code while fixing the related bug.

## Counterexample

Reorganize the entire repository during a one-line production fix.

## Guidance for AI models

- Apply this guidance only after considering the active project profile, constraints, and architecture authority.
- State the concrete design consequence instead of citing the principle name as sufficient justification.

## Editorial note

This page is generated from the canonical YAML entry. Edit `principles/entries/boy-scout-rule.yaml` and regenerate the compendium instead of editing this file directly.
