---
id: self-documenting-code
name: Self-Documenting Code
classification: heuristic
category: simplicity-and-clarity
status: candidate
source: principles/entries/self-documenting-code.yaml
generated: true
---

# Self-Documenting Code

> Express intent through structure, names, types, and explicit control flow.

## Canonical interpretation

Code should explain its normal behavior without requiring comments that translate unclear implementation.

## Purpose

Express intent through structure, names, types, and explicit control flow.

## Apply when

- The code must be understood and changed by people other than its author.
- A simpler implementation satisfies the current verified requirements.

## This does not mean

- Do not eliminate comments that explain rationale, constraints, or surprising external behavior.
- Do not assume readable code replaces public documentation.

## Trade-offs

- Local simplicity can conflict with extensibility, reuse, or performance requirements.
- Reducing visible code can increase hidden behavior; clarity is more important than terseness.

## Conflicts with canonical entries

- None recorded.

## Broader policy tensions

- `concise-code`

## Reinforces canonical entries

- `explicit-over-implicit`
- `meaningful-names`

## Supports broader concerns

- None recorded.

## Core Skill ownership

Primary owner: `code-clarity`

## Positive example

Use a named domain operation and comment only why a regulatory exception exists.

## Counterexample

Keep obscure bit manipulation and add a comment that paraphrases each line.

## Guidance for AI models

- Apply this guidance only after considering the active project profile, constraints, and architecture authority.
- State the concrete design consequence instead of citing the principle name as sufficient justification.

## Editorial note

This page is generated from the canonical YAML entry. Edit `principles/entries/self-documenting-code.yaml` and regenerate the compendium instead of editing this file directly.
