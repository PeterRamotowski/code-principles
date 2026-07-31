---
id: make-illegal-states-unrepresentable
name: Make Illegal States Unrepresentable
classification: principle
category: contracts-errors-and-security
status: candidate
source: principles/entries/make-illegal-states-unrepresentable.yaml
generated: true
---

# Make Illegal States Unrepresentable

> Use types and constructors that prevent invalid combinations where practical.

## Canonical interpretation

Represent invariants structurally when doing so improves correctness without disproportionate complexity.

## Purpose

Use types and constructors that prevent invalid combinations where practical.

## Apply when

- Data or control crosses a trust, process, module, or API boundary.
- Invalid state could threaten correctness, security, or recoverability.

## This does not mean

- Do not encode every business possibility into an unmanageable type system.
- Do not assume compile-time types validate external runtime data.

## Trade-offs

- Stricter contracts can reduce compatibility with inconsistent external producers.
- Defensive checks can duplicate validation if trust boundaries are not explicit.

## Conflicts with canonical entries

- None recorded.

## Broader policy tensions

- `dynamic-schema-evolution`
- `serialization`

## Reinforces canonical entries

- `encapsulation`
- `parse-dont-validate`

## Supports broader concerns

- None recorded.

## Core Skill ownership

Primary owner: `contracts-and-errors`

## Positive example

Represent payment status as a closed set with state-specific required data.

## Counterexample

Use independent booleans that permit mutually contradictory states.

## Guidance for AI models

- Apply this guidance only after considering the active project profile, constraints, and architecture authority.
- State the concrete design consequence instead of citing the principle name as sufficient justification.

## Editorial note

This page is generated from the canonical YAML entry. Edit `principles/entries/make-illegal-states-unrepresentable.yaml` and regenerate the compendium instead of editing this file directly.
