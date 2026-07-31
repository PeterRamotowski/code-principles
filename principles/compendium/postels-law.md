---
id: postels-law
name: Postel’s Law / Robustness Principle
classification: heuristic
category: contracts-errors-and-security
status: candidate
source: principles/entries/postels-law.yaml
generated: true
---

# Postel’s Law / Robustness Principle

> Historically: be conservative in output and liberal in accepted input; modern use requires caution.

## Canonical interpretation

Tolerate harmless representational variation only when semantics remain unambiguous and interoperability benefits outweigh long-term ambiguity.

## Purpose

Historically: be conservative in output and liberal in accepted input; modern use requires caution.

## Apply when

- Data or control crosses a trust, process, module, or API boundary.
- Invalid state could threaten correctness, security, or recoverability.

## This does not mean

- Do not accept malformed or ambiguous semantics.
- Do not normalize security-sensitive input in surprising ways.

## Trade-offs

- Stricter contracts can reduce compatibility with inconsistent external producers.
- Defensive checks can duplicate validation if trust boundaries are not explicit.

## Conflicts with canonical entries

- `fail-fast`
- `parse-dont-validate`

## Broader policy tensions

- `api-evolution`

## Reinforces canonical entries

- `principle-of-least-astonishment`

## Supports broader concerns

- None recorded.

## Core Skill ownership

Primary owner: `contracts-and-errors`

## Positive example

Accept equivalent whitespace variants while producing one canonical format.

## Counterexample

Guess which account an ambiguous identifier refers to.

## Guidance for AI models

- Apply this guidance only after considering the active project profile, constraints, and architecture authority.
- State the concrete design consequence instead of citing the principle name as sufficient justification.

## Editorial note

This page is generated from the canonical YAML entry. Edit `principles/entries/postels-law.yaml` and regenerate the compendium instead of editing this file directly.
