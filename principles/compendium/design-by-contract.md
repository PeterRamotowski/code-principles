---
id: design-by-contract
name: Design by Contract
classification: method
category: contracts-errors-and-security
status: candidate
source: principles/entries/design-by-contract.yaml
generated: true
---

# Design by Contract

> Specify preconditions, postconditions, and invariants for operations and types.

## Canonical interpretation

A contract defines obligations of callers and guarantees of implementations.

## Purpose

Specify preconditions, postconditions, and invariants for operations and types.

## Apply when

- Data or control crosses a trust, process, module, or API boundary.
- Invalid state could threaten correctness, security, or recoverability.

## This does not mean

- Do not rely only on comments when contracts can be encoded or tested.
- Do not expose implementation details as contractual guarantees.

## Trade-offs

- Stricter contracts can reduce compatibility with inconsistent external producers.
- Defensive checks can duplicate validation if trust boundaries are not explicit.

## Conflicts with canonical entries

- `backward-compatibility`

## Broader policy tensions

- `tolerant-input`

## Reinforces canonical entries

- `fail-fast`
- `liskov-substitution-principle`

## Supports broader concerns

- None recorded.

## Core Skill ownership

Primary owner: `contracts-and-errors`

## Positive example

Document and enforce that a transfer amount is positive and balances remain valid.

## Counterexample

Accept any input and leave callers to infer failure from later state.

## Guidance for AI models

- Apply this guidance only after considering the active project profile, constraints, and architecture authority.
- State the concrete design consequence instead of citing the principle name as sufficient justification.

## Editorial note

This page is generated from the canonical YAML entry. Edit `principles/entries/design-by-contract.yaml` and regenerate the compendium instead of editing this file directly.
