---
id: defensive-programming
name: Defensive Programming
classification: technique
category: contracts-errors-and-security
status: candidate
source: principles/entries/defensive-programming.yaml
generated: true
---

# Defensive Programming

> Anticipate invalid input, partial failure, and misuse at relevant boundaries.

## Canonical interpretation

Defend trust boundaries and dangerous operations without scattering redundant checks through trusted internal code.

## Purpose

Anticipate invalid input, partial failure, and misuse at relevant boundaries.

## Apply when

- Data or control crosses a trust, process, module, or API boundary.
- Invalid state could threaten correctness, security, or recoverability.

## This does not mean

- Do not silently swallow errors.
- Do not validate the same trusted invariant in every private helper.

## Trade-offs

- Stricter contracts can reduce compatibility with inconsistent external producers.
- Defensive checks can duplicate validation if trust boundaries are not explicit.

## Conflicts with canonical entries

- `fail-fast`
- `performance-budgeting`

## Broader policy tensions

- None recorded.

## Reinforces canonical entries

- `design-by-contract`
- `principle-of-least-privilege`

## Supports broader concerns

- None recorded.

## Core Skill ownership

Primary owner: `contracts-and-errors`

## Positive example

Validate an external webhook signature, schema, and replay key.

## Counterexample

Wrap every internal call in a catch-all that converts errors to `null`.

## Guidance for AI models

- Apply this guidance only after considering the active project profile, constraints, and architecture authority.
- State the concrete design consequence instead of citing the principle name as sufficient justification.

## Editorial note

This page is generated from the canonical YAML entry. Edit `principles/entries/defensive-programming.yaml` and regenerate the compendium instead of editing this file directly.
