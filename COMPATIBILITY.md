# Compatibility Policy

## Candidate scope

Version `0.10.x` is a candidate policy package for manual evaluation. The implemented adapters cover JavaScript,
TypeScript, Python, PHP, Go, C++, React, Next.js, Angular, Vue, Nuxt, Symfony, and Drupal. Candidate coverage means
the repository can select and supply guidance for those technologies; it is not a promise that every ecosystem
version or integration has been practitioner-validated.

The target repository's manifests, runtime configuration, framework conventions, and supported-version policy are
authoritative. An adapter MUST NOT recommend syntax or APIs merely because they exist in a newer release.

## Priority manual baselines

The initial practical test paths are PHP and Composer libraries, Symfony applications, Drupal modules, JavaScript
and TypeScript packages, Vue applications, and Nuxt applications. Existing executable fixtures exercise PHP 8.3,
Symfony 7, Drupal 11, Vue 3, and Nuxt 4 repository signals. These versions are evaluation inputs, not a stable
support range.

Before `1.0.0`, practitioner testing MUST establish explicit supported version ranges or document an intentionally
version-independent adapter. Results SHOULD cover maintained and migration-relevant versions used by reviewers.

## Policy and output compatibility

- Repository `VERSION` is authoritative for foundation releases.
- Patch releases may clarify wording or correct behavior without intentionally changing a resolved decision.
- Minor releases may add compatible components, fields, scenarios, or optional behavior.
- Major releases are required for incompatible precedence, context, schema, default-mode, or stable-identifier changes.
- Additive optional output fields are compatible. Removing or changing a required field is incompatible.
- A selected child language adapter includes its parent runtime policy even when the parent is omitted from the concise adapter list.
- Framework requirements are resolved transitively and MUST appear in the applied policy bundle.

Stable support claims require a green distribution validation, executable policy evaluations, documented manual
evidence, and the external reviews required by the roadmap.

