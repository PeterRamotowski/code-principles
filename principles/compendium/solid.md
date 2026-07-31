---
id: solid
name: SOLID
classification: umbrella-concept
category: umbrella-concepts
status: candidate
source: principles/entries/solid.yaml
generated: true
---

# SOLID

> A mnemonic grouping five object-oriented design principles.

## Canonical interpretation

Use the individual principles selectively; SOLID is not a universal compliance target.

## Purpose

A mnemonic grouping five object-oriented design principles.

## Apply when

- A broad family of related practices needs a shared vocabulary.
- The concept is used as an index into more precise rules.

## This does not mean

- Do not score code by counting interfaces or classes.
- Do not apply object-oriented rules to data pipelines or functional code without translation.

## Trade-offs

- Umbrella labels can hide disagreements about their actual meaning.
- They must not replace concrete context-sensitive guidance.

## Conflicts with canonical entries

- `kiss`
- `yagni`

## Broader policy tensions

- `data-oriented-design`

## Reinforces canonical entries

- `open-closed-principle`
- `single-responsibility-principle`

## Supports broader concerns

- None recorded.

## Core Skill ownership

Primary owner: `engineering-review-lenses`

## Positive example

Use LSP to review a public subtype contract where substitution is required.

## Counterexample

Add interfaces and layers merely to claim that a small script is SOLID.

## Guidance for AI models

- Apply this guidance only after considering the active project profile, constraints, and architecture authority.
- State the concrete design consequence instead of citing the principle name as sufficient justification.

## Editorial note

This page is generated from the canonical YAML entry. Edit `principles/entries/solid.yaml` and regenerate the compendium instead of editing this file directly.
