# Project Profiles

Project profiles are language-independent configurations for the dominant artifact and failure model of a task. Each profile selects default Core Skill modes and priority order without copying the normative rules owned by those Skills.

## Implemented profiles

- [`browser-web-application`](browser-web-application/PROFILE.md) — interactive browser behavior, accessibility, and localized state;
- [`fullstack-web-application`](fullstack-web-application/PROFILE.md) — integrated browser/server authority and data boundaries;
- [`backend-service`](backend-service/PROFILE.md) — service contracts, transactions, reliability, and operation;
- [`reusable-library`](reusable-library/PROFILE.md) — intentional public surface, compatibility, and independent consumers;
- [`legacy-modernization`](legacy-modernization/PROFILE.md) — behavior discovery, bounded change, and reversible migration.
- [`plugin-or-extension`](plugin-or-extension/PROFILE.md) — host lifecycle, extension contracts, and coexistence;
- [`data-pipeline`](data-pipeline/PROFILE.md) — staged transformation, provenance, restartability, and bounded resources;
- [`background-worker`](background-worker/PROFILE.md) — delivery, retries, acknowledgement, concurrency, and shutdown;
- [`distributed-system`](distributed-system/PROFILE.md) — ownership, partial failure, convergence, and repair;
- [`real-time-system`](real-time-system/PROFILE.md) — deterministic timing, bounded resources, and target verification;
- [`prototype`](prototype/PROFILE.md) — bounded learning, reversibility, and explicit instability;
- [`cli-application`](cli-application/PROFILE.md) — invocation, streams, exits, automation, and process effects;
- [`infrastructure-tool`](infrastructure-tool/PROFILE.md) — planning, least authority, safe application, and recovery.

Every package contains normative `PROFILE.md` guidance and schema-validated `profile.yaml` metadata. The orchestrator reads `skill_modes` from that metadata as the runtime source of profile defaults. Explicit context, repository configuration, and active modifiers retain their defined precedence.

Milestones 5 and 10 now implement every controlled profile in the catalogue except the conservative
`general-software` fallback, which is owned directly by the orchestrator.
