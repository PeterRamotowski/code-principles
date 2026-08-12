# Governance

## Decision authority

Repository maintainers are responsible for accepting changes, publishing releases, and enforcing the specification.
No single adapter may override safety, explicit user requirements, repository policy, or canonical principle meaning.

Changes to schemas, precedence, stable identifiers, default modes, or compatibility policy require explicit review
of migration impact. Technology adapter changes require review from someone able to evaluate the affected ecosystem.

## Review and release

A release candidate requires:

- green validation and deterministic evaluations;
- documented compatibility and migration impact;
- manual evidence for materially affected technology paths;
- no unresolved high-severity correctness or dependency issue;
- release notes identifying policy-output changes.

A stable release additionally requires the external practitioner reviews listed in the roadmap. Review records MUST
identify the ecosystem, target revision, task, verification performed, result, and actionable feedback. Missing
external review cannot be replaced by self-review or synthetic evaluation.

## Disagreements

Resolve policy disagreements using `CONFLICT-RESOLUTION.md` and the authority order in `SPECIFICATION.md`. Record
material unresolved disagreement in the change discussion. Safety and data-integrity concerns block release until
resolved; stylistic preferences do not.

## Security and conduct

Do not include secrets, private source, personal data, or proprietary evaluation artifacts in public review records.
Contributors and reviewers must communicate professionally and evaluate proposals on technical evidence.

