---
id: meaningful-names
name: Meaningful Names
classification: heuristic
category: simplicity-and-clarity
status: candidate
source: principles/entries/meaningful-names.yaml
generated: true
---

# Meaningful Names

> Use names that communicate domain meaning, role, and units.

## Canonical interpretation

A name should help a reader understand what a value or operation represents without decoding implementation history.

## Purpose

Use names that communicate domain meaning, role, and units.

## Apply when

- The code must be understood and changed by people other than its author.
- A simpler implementation satisfies the current verified requirements.

## This does not mean

- Do not make names long merely to restate the type.
- Do not use domain terminology inconsistently.

## Trade-offs

- Local simplicity can conflict with extensibility, reuse, or performance requirements.
- Reducing visible code can increase hidden behavior; clarity is more important than terseness.

## Conflicts with canonical entries

- None recorded.

## Broader policy tensions

- `local-conventions`

## Reinforces canonical entries

- `principle-of-least-astonishment`
- `self-documenting-code`

## Supports broader concerns

- None recorded.

## Core Skill ownership

Primary owner: `code-clarity`

## Positive example

Name a duration `retryDelayMilliseconds` when the unit matters.

## Counterexample

Name important values `data`, `tmp`, or `manager` without a specific role.

## Guidance for AI models

- Apply this guidance only after considering the active project profile, constraints, and architecture authority.
- State the concrete design consequence instead of citing the principle name as sufficient justification.

## Editorial note

This page is generated from the canonical YAML entry. Edit `principles/entries/meaningful-names.yaml` and regenerate the compendium instead of editing this file directly.
