# Knowledge Model

## 1. Purpose

The project separates engineering knowledge from its operational application.

A named principle such as DRY is stored once as a canonical entry. A Core Skill then combines it with related and conflicting entries, selects a mode, and turns the combined knowledge into task-specific instructions.

## 2. Knowledge layers

### Canonical principle entries

Atomic knowledge records with classification, interpretation, rejected meanings, trade-offs, conflicts, examples, and Core Skill ownership.

### Core Skills

Operational decision systems. A Core Skill contains procedures, modes, exceptions, and review checklists for a coherent problem area. It references canonical entries instead of redefining them.

### Profiles

Language-independent configurations for project types. A profile selects Core Skill modes but does not copy their normative content.

### Modifiers

Cross-cutting constraints that strengthen, constrain, or add requirements to a profile.

### Language adapters

Technology refinements that translate canonical guidance into language semantics. For example, the Python adapter can explain Protocols, dataclasses, iterators, exception policy, and runtime validation.

### Framework adapters

Host-specific refinements that account for lifecycle, state, extension APIs, rendering, caching, and conventions.

### Orchestrator

The policy resolver that combines context with the controlled knowledge layers.

## 3. Single-source-of-truth rules

- Canonical principle meaning lives in `principles/entries/*.yaml`.
- Operational decisions live in Core Skills.
- Profile selection lives in profiles.
- Language semantics live in language adapters.
- Framework conventions live in framework adapters.
- Conflict precedence lives in the orchestrator and conflict-resolution documents.

No lower layer may redefine the meaning owned by a higher-authority source.

## 4. Generated human documentation

The compendium Markdown is generated from YAML. This provides readable knowledge without creating a second independently edited specification.

## 5. Why broad concepts remain in the registry

Entries such as Clean Code and SOLID are included because users and models frequently invoke them. They are classified as umbrella concepts and explicitly prevented from acting as universal standalone commands.

Similarly, Conway’s Law and Brooks’s Law are included as review lenses, not implementation rules.
