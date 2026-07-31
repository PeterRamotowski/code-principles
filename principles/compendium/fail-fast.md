---
id: fail-fast
name: Fail Fast
classification: principle
category: contracts-errors-and-security
status: candidate
source: principles/entries/fail-fast.yaml
generated: true
---

# Fail Fast

> Detect and report invalid conditions close to their source.

## Canonical interpretation

Do not continue with corrupted assumptions when a required contract is violated.

## Purpose

Detect and report invalid conditions close to their source.

## Apply when

- Data or control crosses a trust, process, module, or API boundary.
- Invalid state could threaten correctness, security, or recoverability.

## This does not mean

- Do not crash whole systems for recoverable external failures.
- Do not expose sensitive diagnostics to untrusted users.

## Trade-offs

- Stricter contracts can reduce compatibility with inconsistent external producers.
- Defensive checks can duplicate validation if trust boundaries are not explicit.

## Conflicts with canonical entries

- None recorded.

## Broader policy tensions

- `fault-tolerance`
- `tolerant-input`

## Reinforces canonical entries

- `design-by-contract`
- `parse-dont-validate`

## Supports broader concerns

- None recorded.

## Core Skill ownership

Primary owner: `contracts-and-errors`

## Positive example

Reject an invalid configuration during startup with a precise message.

## Counterexample

Replace a missing required value with an arbitrary default and fail later.

## Guidance for AI models

- Apply this guidance only after considering the active project profile, constraints, and architecture authority.
- State the concrete design consequence instead of citing the principle name as sufficient justification.

## Editorial note

This page is generated from the canonical YAML entry. Edit `principles/entries/fail-fast.yaml` and regenerate the compendium instead of editing this file directly.
