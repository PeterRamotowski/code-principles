---
id: principle-of-least-privilege
name: Principle of Least Privilege
classification: security-principle
category: contracts-errors-and-security
status: candidate
source: principles/entries/principle-of-least-privilege.yaml
generated: true
---

# Principle of Least Privilege

> Grant only the permissions and capabilities required for the task.

## Canonical interpretation

Limit authority by default and expand it deliberately for verified needs.

## Purpose

Grant only the permissions and capabilities required for the task.

## Apply when

- Data or control crosses a trust, process, module, or API boundary.
- Invalid state could threaten correctness, security, or recoverability.

## This does not mean

- Do not break required operations by removing essential access without analysis.
- Do not treat application-level checks as a replacement for infrastructure permissions.

## Trade-offs

- Stricter contracts can reduce compatibility with inconsistent external producers.
- Defensive checks can duplicate validation if trust boundaries are not explicit.

## Conflicts with canonical entries

- None recorded.

## Broader policy tensions

- `operational-convenience`

## Reinforces canonical entries

- `defensive-programming`
- `information-hiding`

## Supports broader concerns

- None recorded.

## Core Skill ownership

Primary owner: `contracts-and-errors`

## Positive example

Give a worker read access only to the bucket prefix it processes.

## Counterexample

Run every service with administrative database credentials.

## Guidance for AI models

- Apply this guidance only after considering the active project profile, constraints, and architecture authority.
- State the concrete design consequence instead of citing the principle name as sufficient justification.

## Editorial note

This page is generated from the canonical YAML entry. Edit `principles/entries/principle-of-least-privilege.yaml` and regenerate the compendium instead of editing this file directly.
