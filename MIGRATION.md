# Migration Policy

## Stable identifiers

Component identifiers become compatibility contracts at `candidate` status and MUST NOT be renamed or reused for a
different meaning. A required rename MUST introduce a new identifier, retain an explicit deprecated alias or
migration mapping for at least one compatible release line, and document the policy-output difference.

## Release migration requirements

For any incompatible schema, context, precedence, mode, or output change:

1. describe affected identifiers and consumers in `CHANGELOG.md`;
2. provide before-and-after configuration and resolved-policy examples;
3. state whether automated conversion is possible;
4. preserve safe parsing of the old form when feasible during a documented transition period;
5. add or update evaluation coverage for both the supported migration path and rejected ambiguous behavior;
6. require a major version when stable behavior is intentionally broken.

Candidate components may gain compatible refinements during the `0.x` series, but the repository MUST still record
behavior changes and MUST NOT silently repurpose identifiers.

## Repository contexts

When `engineering-context.yaml` changes schema, a migration note MUST identify renamed fields, changed enum values,
new defaults, and precedence effects. Unknown or removed values MUST fail visibly rather than silently selecting a
different profile.

## Manual bundle consumers

The `--format manual` output is a generated task artifact. Consumers SHOULD regenerate it after changing the task,
repository revision, engineering context, or Code Principles version. Generated bundles are not long-lived policy
configuration and SHOULD NOT be edited as a substitute for repository or user context.

