---
id: linus-law
name: Linus’s Law
classification: law
category: change-and-engineering-systems
status: candidate
source: principles/entries/linus-law.yaml
generated: true
---

# Linus’s Law

> With enough qualified review, many defects become easier to identify.

## Canonical interpretation

Use diverse review and transparent diagnostics to improve defect discovery, while preserving ownership and review quality.

## Purpose

With enough qualified review, many defects become easier to identify.

## Apply when

- The project is being evolved, modernized, reviewed, or reorganized.
- Organizational and historical context affects technical outcomes.

## This does not mean

- Do not assume more reviewers automatically produce better review.
- Do not expose sensitive code or data indiscriminately.

## Trade-offs

- Local improvement can enlarge the scope and risk of a change.
- Organizational laws are diagnostic lenses, not deterministic commands.

## Conflicts with canonical entries

- None recorded.

## Broader policy tensions

- `coordination-cost`

## Reinforces canonical entries

- None recorded.

## Supports broader concerns

- `code-review`

## Core Skill ownership

Primary owner: `engineering-review-lenses`

## Positive example

Invite focused review from domain, security, and operations perspectives.

## Counterexample

Add dozens of unfocused reviewers and assume defects will disappear.

## Guidance for AI models

- Apply this guidance only after considering the active project profile, constraints, and architecture authority.
- State the concrete design consequence instead of citing the principle name as sufficient justification.

## Editorial note

This page is generated from the canonical YAML entry. Edit `principles/entries/linus-law.yaml` and regenerate the compendium instead of editing this file directly.
