---
id: inversion-of-control
name: Inversion of Control
classification: architecture-pattern
category: architecture-and-dependencies
status: candidate
source: principles/entries/inversion-of-control.yaml
generated: true
---

# Inversion of Control

> Delegate control of lifecycle or flow to a framework, runtime, or coordinating component.

## Canonical interpretation

Use IoC where a host legitimately controls execution; keep application policy visible and testable.

## Purpose

Delegate control of lifecycle or flow to a framework, runtime, or coordinating component.

## Apply when

- High-level policy must evolve independently from volatile infrastructure.
- Dependency direction affects testability, deployability, or independent ownership.

## This does not mean

- Do not confuse IoC with dependency injection alone.
- Do not allow framework callbacks to scatter business policy invisibly.

## Trade-offs

- Indirection and adapters have a maintenance cost.
- Framework isolation is valuable only where independent evolution is required.

## Conflicts with canonical entries

- `explicit-over-implicit`

## Broader policy tensions

- `framework-native-design`

## Reinforces canonical entries

- `dependency-injection`

## Supports broader concerns

- None recorded.

## Core Skill ownership

Primary owner: `dependencies-and-boundaries`

## Positive example

A web framework invokes request handlers while the handler delegates to an explicit use case.

## Counterexample

Business decisions are distributed across undocumented lifecycle hooks.

## Guidance for AI models

- Apply this guidance only after considering the active project profile, constraints, and architecture authority.
- State the concrete design consequence instead of citing the principle name as sufficient justification.

## Editorial note

This page is generated from the canonical YAML entry. Edit `principles/entries/inversion-of-control.yaml` and regenerate the compendium instead of editing this file directly.
