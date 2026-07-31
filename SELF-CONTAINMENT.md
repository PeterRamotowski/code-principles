# Self-Containment and Dependency Policy

## Normative rule

The installed project MUST contain all normative knowledge required to select and apply its engineering policy.

## Prohibited dependencies

The project MUST NOT require an externally maintained Skill collection for:

- canonical principle definitions;
- Core Skill behavior;
- profile selection;
- conflict resolution;
- language or framework interpretation;
- validation of the resolved policy.

## Permitted external material

Books, standards, articles, papers, and repositories MAY be referenced for:

- historical attribution;
- comparison;
- further reading;
- contributor research.

Such material has `supplementary-only` authority. It is not loaded as executable policy and cannot override local content.

## Optional platform integrations

Future packaging for Codex, ChatGPT, Claude Code, Cursor, GitHub Copilot, or other hosts may adapt file layout and activation syntax. These integrations must package the same controlled knowledge and must not substitute third-party Skills.

## Supply-chain rationale

Self-containment provides:

- stable versioned behavior;
- reviewable changes;
- reproducible installations;
- controlled licensing;
- protection from upstream deletion or incompatible changes;
- consistent conflict resolution;
- one quality standard across all supported languages.
