---
id: parse-dont-validate
name: Parse, Don’t Validate
classification: principle
category: contracts-errors-and-security
status: candidate
source: principles/entries/parse-dont-validate.yaml
generated: true
---

# Parse, Don’t Validate

> Transform untrusted input into types that represent validated meaning.

## Canonical interpretation

Validation should produce a trusted representation, not merely a boolean followed by continued use of raw data.

## Purpose

Transform untrusted input into types that represent validated meaning.

## Apply when

- Data or control crosses a trust, process, module, or API boundary.
- Invalid state could threaten correctness, security, or recoverability.

## This does not mean

- Do not assume parsing can encode every cross-record business rule.
- Do not discard useful error detail.

## Trade-offs

- Stricter contracts can reduce compatibility with inconsistent external producers.
- Defensive checks can duplicate validation if trust boundaries are not explicit.

## Conflicts with canonical entries

- `performance-budgeting`

## Broader policy tensions

- `tolerant-input`

## Reinforces canonical entries

- `fail-fast`
- `make-illegal-states-unrepresentable`

## Supports broader concerns

- None recorded.

## Core Skill ownership

Primary owner: `contracts-and-errors`

## Positive example

Parse a raw currency string into a validated Money value.

## Counterexample

Call `isValid(raw)` and then pass the same raw dictionary throughout the system.

## Guidance for AI models

- Apply this guidance only after considering the active project profile, constraints, and architecture authority.
- State the concrete design consequence instead of citing the principle name as sufficient justification.

## Editorial note

This page is generated from the canonical YAML entry. Edit `principles/entries/parse-dont-validate.yaml` and regenerate the compendium instead of editing this file directly.
