# Project Profiles

Project profiles are language-independent configurations for the dominant artifact and failure model of a task. Each profile selects default Core Skill modes and priority order without copying the normative rules owned by those Skills.

## Milestone 5 implementations

- [`browser-web-application`](browser-web-application/PROFILE.md) — interactive browser behavior, accessibility, and localized state;
- [`fullstack-web-application`](fullstack-web-application/PROFILE.md) — integrated browser/server authority and data boundaries;
- [`backend-service`](backend-service/PROFILE.md) — service contracts, transactions, reliability, and operation;
- [`reusable-library`](reusable-library/PROFILE.md) — intentional public surface, compatibility, and independent consumers;
- [`legacy-modernization`](legacy-modernization/PROFILE.md) — behavior discovery, bounded change, and reversible migration.

Every package contains normative `PROFILE.md` guidance and schema-validated `profile.yaml` metadata. The orchestrator reads `skill_modes` from that metadata as the runtime source of profile defaults. Explicit context, repository configuration, and active modifiers retain their defined precedence.

The remaining identifiers in [`catalogs/profiles.yaml`](../catalogs/profiles.yaml) are blueprints for later milestones.
