# Terminology

This document defines canonical terms used throughout Code Principles. Components MUST use these terms consistently.

## Adapter

A technology-specific policy component that refines general engineering rules for a programming language, runtime, framework, platform, or closely related ecosystem.

An adapter does not define the primary project type.

Examples:

- TypeScript language adapter;
- Python language adapter;
- React framework adapter;
- Drupal framework adapter.

## Architecture authority

The permitted scope of structural change for the current task.

Canonical values:

- `preserve-existing` — preserve established boundaries and patterns; make only required local changes;
- `incremental-improvement` — allow bounded refactoring around the affected area;
- `redesign-allowed` — allow broader restructuring when justified;
- `greenfield` — permit selection of new architecture;
- `unknown` — no reliable information.

## Artifact type

The primary kind of software deliverable being created or modified.

Examples include application, library, service, plugin, CLI, data pipeline, worker, embedded system, or infrastructure tool.

Artifact type is not the same as language, framework, runtime, or repository type.

## Base profile

The primary project profile selected for the current task. It establishes default quality priorities and core skill modes.

The system normally selects one base profile and composes additional concerns through modifiers and adapters.

## Boundary

A point where ownership, trust, lifecycle, representation, or change responsibility differs.

Common boundaries include:

- external input to internal types;
- browser code to server code;
- application to database;
- domain logic to infrastructure;
- public API to private implementation;
- process to process;
- module to module;
- managed resource to owning component.

A boundary should not be introduced merely to create more layers.

## Compatibility policy

The declared expectations for preserving existing consumers and observable behavior.

Compatibility may apply to:

- source API;
- binary ABI;
- serialized data;
- network protocol;
- database schema;
- CLI interface;
- configuration format;
- extension hooks;
- observable behavior.

## Confidence

The strength of evidence supporting a context decision.

Canonical values:

- `explicit`;
- `observed`;
- `inferred-high`;
- `inferred-low`;
- `unknown`.

## Constraint

A requirement that limits acceptable solutions.

Constraints may concern:

- correctness;
- security;
- latency;
- throughput;
- memory;
- determinism;
- reliability;
- accessibility;
- compatibility;
- deployment;
- language or framework support.

## Core skill

A reusable, language-agnostic unit of engineering decision guidance with a coherent responsibility, explicit modes, conflicts, and verification rules.

A core skill is broader than a single slogan but narrower than a complete project profile.

## Decision

A resolved engineering choice recorded in the policy because it materially affects implementation or review.

Examples:

- use strict boundary validation;
- preserve public API compatibility;
- keep state local to a component subtree;
- stream records instead of loading the complete dataset;
- preserve the existing modular architecture.

## Decision precedence

The ordered priority used to resolve competing instructions. Higher-precedence rules override lower-precedence defaults.

## Domain complexity

The density, interaction, volatility, and importance of business rules, invariants, workflows, and domain terminology.

Repository size, class count, or number of database tables does not by itself determine domain complexity.

## Engineering context

The normalized set of facts, constraints, technologies, project characteristics, and confidence levels used by the orchestrator.

## Engineering policy

A set of selected rules, modes, adapters, modifiers, overrides, and prohibitions governing a task.

## Exposure

The audience and stability expectations of a software boundary.

Canonical values:

- `private-local`;
- `team-internal`;
- `organization-internal`;
- `external-integration`;
- `public-api`;
- `public-library`;
- `extension-platform`;
- `unknown`.

## External input

Data that crosses a trust or representation boundary and cannot be assumed valid solely because internal code expects a type.

Examples:

- HTTP request data;
- files;
- database rows created by older versions;
- queue messages;
- webhook payloads;
- environment variables;
- command-line arguments;
- user-controlled browser state;
- third-party SDK responses.

## Framework adapter

An adapter that refines policy according to a framework's lifecycle, dependency model, state model, extension points, caching, rendering, or testing conventions.

## Heuristic

A strong but defeasible engineering default. A heuristic should normally use `SHOULD`, not `MUST`.

Examples:

- prefer composition over inheritance;
- keep functions focused;
- favor immutable values;
- colocate behavior with the data it governs.

## Internal contract

A contract whose consumers can normally be updated atomically within the same controlled change.

Internal does not necessarily mean unimportant, but it usually permits more refactoring freedom than a public contract.

## Language adapter

An adapter that refines policy according to language semantics and ecosystem conventions.

Typical concerns include:

- static and runtime typing;
- ownership and resource lifetime;
- exceptions or explicit error values;
- concurrency;
- module visibility;
- packaging;
- binary compatibility;
- reflection and metaprogramming.

## Mode

A named configuration of a skill representing a coherent policy variant.

Example modes for abstraction guidance:

- `conservative`;
- `balanced`;
- `extensible-library`.

Modes allow the same skill to support different project contexts without duplicating the skill.

## Modifier

A cross-cutting policy component activated by a concern that applies to several project types.

A modifier changes priorities or rules without becoming the primary project profile.

Examples:

- `public-api`;
- `security-sensitive`;
- `memory-sensitive`;
- `real-time`;
- `accessibility-required`.

## Non-goal

A behavior, responsibility, or design ambition explicitly excluded from a component's scope.

Non-goals prevent broad prompts from expanding into universal architecture rules.

## Normative rule

A rule expressed using `MUST`, `SHOULD`, or `MAY` and intended to affect model behavior.

## Observed behavior

Any externally detectable result of a component, including undocumented behavior that consumers may rely on.

Observed behavior matters especially for public APIs because of Hyrum's Law.

## Orchestrator

The policy-routing component that detects context, selects profiles, modifiers, and adapters, resolves conflicts, and produces a resolved policy.

The orchestrator is not a universal coding-style skill.

## Override

An explicit instruction that changes a selected default.

Overrides may come from:

- current user request;
- repository configuration;
- organization policy;
- task-specific constraints.

## Principle

A general engineering idea used to guide decisions, such as KISS, DRY, YAGNI, information hiding, or dependency inversion.

A principle is not automatically a standalone skill.

## Profile

A language-independent policy component describing priorities and default skill modes for a class of software project.

Examples:

- `reusable-library`;
- `fullstack-web-application`;
- `legacy-modernization`.

## Project stage

The lifecycle condition of the software.

Canonical values:

- `prototype`;
- `greenfield`;
- `active-product`;
- `mature-system`;
- `legacy-modernization`;
- `maintenance-only`;
- `unknown`.

## Protected quality attribute

A quality the conflicting rule is intended to preserve.

Examples:

- correctness;
- security;
- simplicity;
- maintainability;
- extensibility;
- performance;
- compatibility;
- reliability;
- testability;
- usability.

Conflict resolution should compare protected attributes rather than principle names alone.

## Public API

An intentionally supported interface consumed outside the implementation's atomic change boundary.

A public API may include:

- functions, methods, classes, or types;
- HTTP or RPC contracts;
- events and messages;
- configuration files;
- plugin interfaces;
- CLI commands and output formats;
- database or serialized formats;
- documented extension behavior.

Language-level `public` visibility does not automatically mean stable public API.

## Resolved policy

The final, task-scoped composition of context, profile, modifiers, adapters, skill modes, overrides, conflicts, decisions, and prohibitions.

## Runtime validation

Validation performed while the program is running against actual data.

Static type checking does not replace runtime validation for external input.

## Selection mode

The degree to which profile selection is automatic or user-controlled.

Canonical values:

- `automatic-with-visible-result`;
- `propose`;
- `manual`.

## Skill

A reusable instruction unit with a defined scope, metadata, activation rules, modes, conflicts, examples, and verification checklist.

The orchestrator is itself a skill of type `orchestrator`. Core engineering skills use type `core-skill`.

## Skill mode override

A configuration that selects a non-default mode for a skill.

## Significant decision

A decision that materially affects architecture, compatibility, security, correctness, resource use, or future change cost and should therefore be visible or recorded.

## Stable public surface

The intentionally supported subset of externally accessible behavior governed by a compatibility policy.

## Technology context

Languages, frameworks, runtimes, package managers, databases, build tools, deployment environments, and other implementation technologies relevant to the task.

## User-visible result

A concise explanation of significant context and policy choices shown to the user. It is not necessarily the complete internal resolved policy.


## Canonical principle entry

The authoritative machine-readable definition of one named engineering concept. It may represent a principle, heuristic, technique, method, property, law, pattern, or umbrella concept.

## Compendium

The generated human-readable view of the canonical principle registry. It is a project deliverable but not a second normative source.

## Principle interpretation

The context-specific operational meaning selected by a Core Skill and resolved policy without changing the canonical definition.

## Suppressed behaviour

A common but rejected application of a principle that the active policy explicitly prevents.

## External Skill dependency

A runtime or content dependency on a Skill maintained outside this repository. Such dependencies are prohibited for normative project behavior.
