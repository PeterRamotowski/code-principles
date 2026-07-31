---
id: principle-of-least-astonishment
name: Principle of Least Astonishment
classification: principle
category: simplicity-and-clarity
status: candidate
source: principles/entries/principle-of-least-astonishment.yaml
generated: true
---

# Principle of Least Astonishment

> Design behavior and interfaces to match reasonable user expectations.

## Canonical interpretation

Similar operations should behave consistently, and surprising behavior should be removed or made explicit.

## Purpose

Design behavior and interfaces to match reasonable user expectations.

## Apply when

- The code must be understood and changed by people other than its author.
- A simpler implementation satisfies the current verified requirements.

## This does not mean

- Do not assume all users share the same expectations.
- Do not preserve an unsafe convention solely because it is familiar.

## Trade-offs

- Local simplicity can conflict with extensibility, reuse, or performance requirements.
- Reducing visible code can increase hidden behavior; clarity is more important than terseness.

## Conflicts with canonical entries

- `backward-compatibility`

## Broader policy tensions

- `security-hardening`

## Reinforces canonical entries

- `explicit-over-implicit`
- `meaningful-names`

## Supports broader concerns

- None recorded.

## Core Skill ownership

Primary owner: `code-clarity`

## Positive example

A method named `find` returns absence without mutating state.

## Counterexample

A getter sends a network request and deletes expired records.

## Guidance for AI models

- Apply this guidance only after considering the active project profile, constraints, and architecture authority.
- State the concrete design consequence instead of citing the principle name as sufficient justification.

## Editorial note

This page is generated from the canonical YAML entry. Edit `principles/entries/principle-of-least-astonishment.yaml` and regenerate the compendium instead of editing this file directly.
