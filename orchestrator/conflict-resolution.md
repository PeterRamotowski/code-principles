# Orchestrator Conflict Resolution

## 1. Purpose

This document translates the repository-wide conflict policy into concrete orchestrator behavior.

The canonical conflict matrix is maintained in `../CONFLICT-RESOLUTION.md`.

## 2. Conflict detection

The orchestrator should mark a conflict when:

- two active skill modes recommend different implementation structures;
- a modifier strengthens a rule beyond what the base profile normally permits;
- an adapter convention conflicts with repository architecture;
- an explicit override conflicts with a selected default;
- public compatibility conflicts with a requested cleanup;
- performance constraints conflict with general clarity defaults;
- strict internal contracts conflict with tolerant external data handling.

A mere difference in emphasis is not necessarily a conflict.

## 3. Resolution record

For each material conflict, record:

```yaml
id: stable-kebab-case-id
principles:
  - first-policy
  - second-policy
protected_attributes:
  - simplicity
  - compatibility
decision: selected-decision
rationale: Concrete context-based explanation.
reconsider_when:
  - Condition that would change the decision.
```

## 4. Resolution algorithm

### 4.1 Remove invalid options

Discard options that violate:

- correctness;
- security;
- data integrity;
- language semantics;
- hard runtime constraints;
- explicit user prohibitions.

### 4.2 Apply precedence

Prefer higher-precedence explicit or observed rules over profile and heuristic defaults.

### 4.3 Compare failure consequences

Prefer the option with acceptable failure behavior.

Examples:

- a strict parser is preferred over silent corruption;
- compatibility is preferred over cosmetic API cleanup for public consumers;
- deterministic allocation may be preferred over elegance in a hard real-time loop.

### 4.4 Prefer bounded and reversible choices

When options remain close and evidence is incomplete, prefer the one that:

- changes less public surface;
- adds less infrastructure;
- can be replaced locally;
- preserves repository conventions;
- keeps future options open without speculative frameworks.

### 4.5 Define reconsideration triggers

A deferred principle should include a practical trigger.

Examples:

- extract after a stable third use appears;
- introduce a read model when query load or authorization diverges;
- optimize after profiling identifies the path;
- create a portability boundary when a second runtime is committed;
- break API only in the next major version.

## 5. Common orchestrator resolutions

### DRY versus YAGNI

Default:

- unify duplicated authoritative rules;
- keep superficially similar implementations separate when concepts differ;
- defer generalization without a stable variation axis.

### Framework-native versus framework-independent

Default:

- use framework conventions for application code;
- isolate domain logic or external boundaries that need independent evolution;
- do not wrap framework APIs mechanically.

### Strict contracts versus tolerant integration

Default:

- tolerate explicitly supported syntactic variation at ingress;
- parse into a strict internal representation;
- reject ambiguous or unsafe semantics;
- keep internal contracts strict.

### Public compatibility versus simplification

Default:

- preserve supported public behavior;
- deprecate before removal;
- simplify internal implementation freely within the atomic change boundary.

### Immutability versus performance or framework lifecycle

Default:

- prefer immutable values;
- allow controlled mutation with clear ownership;
- require evidence for performance-driven mutation;
- isolate mutable critical sections.

### Testing purity versus integration confidence

Default:

- test pure logic at the unit level;
- use real framework or infrastructure integration where mocks would duplicate implementation;
- choose test level by risk and cost.

## 6. When to surface alternatives

Show alternatives rather than silently resolving when:

- both options are valid but commit substantial future cost;
- the user is choosing a public contract;
- the decision changes persistence or protocol format;
- architecture authority is unknown and broad redesign is proposed;
- security requirements are ambiguous;
- performance constraints are claimed but not defined and architecture depends on them.

## 7. When not to ask

Do not ask for a decision when:

- the safer option is clear;
- the task is local and reversible;
- repository conventions resolve the issue;
- an explicit user instruction already answers it;
- the question would only select a style preference;
- a conservative implementation can proceed without reducing future options.

## 8. Example

Context:

- existing React application;
- two similar forms;
- user requests one validation change;
- no shared business specification;
- architecture authority is `preserve-existing`.

Conflict:

- DRY suggests shared validation;
- YAGNI and task scope suggest a local change.

Resolution:

```yaml
id: dry-vs-yagni-two-form-validation
principles:
  - dry
  - yagni
protected_attributes:
  - maintainability
  - simplicity
decision: preserve-separate-validation
rationale: >-
  The forms are textually similar but represent separate workflows. The task is
  local, no stable shared rule is documented, and extraction would expand scope.
reconsider_when:
  - both forms become governed by one authoritative validation specification
  - a third consumer needs the same rule
```
