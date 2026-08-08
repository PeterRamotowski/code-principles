# Evaluations

Evaluation scenarios test policy selection and rejected behavior, not only output wording. Each scenario should identify active, constrained, and suppressed principles plus forbidden decisions.

The suite contains one cross-cutting orchestrator scenario and three scenarios for every Milestone 4 and 9 Core
Skill: a positive case, a conflict or boundary case, and an overengineering counterexample. Five
Milestone 5 scenarios apply the same DRY-versus-YAGNI conflict to different project profiles and require
artifact-specific resolutions. Three Milestone 6 scenarios apply the same reusable-library profile and task
to TypeScript, Python, and C++, requiring distinct runtime, type, resource, and package guidance. Later
Milestone 7 scenarios apply that profile and task to JavaScript, PHP, and Go, requiring distinct dynamic
runtime, value-object and Composer, and consumer-interface and lifecycle guidance. Seven Milestone 8
scenarios cover framework-specific component, execution, reactivity, SSR, DI, messaging, extension, entity,
configuration, and caching decisions. Milestone 10 scenarios cover every extended artifact profile and every
modifier while exercising boundary, positive, and overengineering decisions in the extended Core Skills.

Milestone 11 adds twelve executable whole-system scenarios. Each creates a minimal temporary repository from
`input.repository_signals`, passes `input.request` plus optional context to the deterministic orchestrator, and
asserts structured policy outcomes. Run all executable scenarios with:

```bash
make evaluate
```

Run one scenario or emit a machine-readable report with:

```bash
python3 tools/evaluate.py --scenario nextjs-payment-webhook
python3 tools/evaluate.py --format json
```

Assertions intentionally target semantic fields rather than complete rendered text: detected context, profile,
modifiers, adapter IDs, selected Skill modes, significant decision IDs, prohibited decisions, and conflict
decisions. This makes request testing deterministic and resistant to harmless wording changes.

This runner evaluates the repository's deterministic policy prompt inputs; it does not call an LLM. An LLM-facing
integration can use the same scenarios by requiring schema-shaped output, checking these deterministic assertions,
and separately grading free-form implementation quality. Stochastic model evaluations SHOULD run each case more
than once and report pass rate rather than treating one sampled response as stable.
