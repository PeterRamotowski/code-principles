# Testing Strategy

## Purpose

Choose the smallest credible set of tests that produces evidence for required behavior and material risks.
This Skill governs behavioral focus, test levels, feedback speed, characterization, and verification gaps.

## Activation and inputs

Activate when behavior is added, changed, fixed, preserved, or reviewed. Use risk, observable contracts,
system boundaries, failure cost, existing tests, environment availability, determinism, and change authority.

## Decision procedure

1. State the behavior and risk that need evidence; do not begin with a test-count target.
2. Choose the narrowest stable observable boundary capable of detecting the failure.
3. Add integration evidence where serialization, persistence, process, timing, or external collaboration is
   itself the risk.
4. Keep each test focused on one logical behavior while allowing related assertions.
5. Make tests repeatable, self-verifying, and independent to the extent the target permits.
6. For unknown existing behavior, characterize relied-upon outcomes before restructuring.
7. Separate fast deterministic feedback from scarce, slow, or representative-environment checks.
8. Report risks that cannot be tested credibly in the available environment.

Tests MUST verify observable contracts rather than private structure unless that structure is itself an
intentional contract. Passing tests MUST NOT be presented as evidence for risks they do not exercise.

## Modes

### `unit-focused`

Use for reusable logic with small stable public units. Favor fast behavioral tests and add integration tests
only for actual boundary risks.

### `integration-balanced`

Use by default for applications and services. Distribute tests by risk: focused logic tests, boundary tests,
and a small set of representative workflows. The pyramid is a heuristic, not a quota.

### `characterization-first`

Use for uncertain legacy behavior. Capture relied-upon observations before change, label known defects and
intentional corrections, and avoid treating every accident as permanent policy.

### `hardware-integration`

Use when credible evidence depends on physical or specialized environments. Retain deterministic simulation
and contract feedback while explicitly scheduling representative integration verification.

## Conflict decisions

### Behavior focus versus failure localization

- Decision: how broad a test boundary should be.
- Protected qualities: refactorability and diagnostic precision.
- Default: use the narrowest stable observable contract.
- Change the resolution when the failure exists only across a material integration boundary.

### Fast feedback versus representative evidence

- Decision: whether a slow or scarce environment belongs in the primary loop.
- Protected qualities: iteration speed and validity.
- Default: keep fast deterministic feedback primary and run representative checks separately.
- Change the resolution when no substitute can exercise the safety- or release-critical behavior.

### Characterization versus correcting defects

- Decision: whether current behavior becomes a preservation oracle.
- Protected qualities: compatibility and correctness.
- Default: characterize relied-upon behavior before restructuring.
- Change the expected result when requirements explicitly identify a defect and compatibility impact is handled.

### Test-first method versus task proportionality

- Decision: whether red-green-refactor drives the change.
- Protected qualities: design feedback and delivery efficiency.
- Default: use it when behavior can be expressed cheaply before implementation.
- Change the workflow for exploratory, generated, environment-bound, or purely mechanical work while still
  producing credible verification.

## Outputs and review

Produce a risk-to-test map, selected modes and levels, observable oracles, environment needs, and known gaps.
Review behavior focus, determinism, independence, meaningful failure messages, boundary coverage, and whether
the suite overfits private structure.

See [decision examples](examples/scenarios.md). Evaluations: `testing-balanced-boundary`,
`testing-characterization-change`, and `testing-end-to-end-only`.

## Non-goals

This Skill MUST NOT mandate one development method, coverage percentage, test pyramid ratio, naming style,
or use of mocks. It does not claim tests replace static analysis, review, monitoring, or formal verification.
