# Engineering Modifiers

Modifiers strengthen selected profile policy when a verified cross-cutting constraint applies. They do not
replace the base profile and MUST NOT activate from vague future possibility.

- [Public API](public-api/MODIFIER.md)
- [Strict Backward Compatibility](strict-backward-compatibility/MODIFIER.md)
- [Security Sensitive](security-sensitive/MODIFIER.md)
- [High Throughput](high-throughput/MODIFIER.md)
- [Memory Sensitive](memory-sensitive/MODIFIER.md)
- [Latency Sensitive](latency-sensitive/MODIFIER.md)
- [Real Time](real-time/MODIFIER.md)
- [Multi-tenant](multi-tenant/MODIFIER.md)
- [Accessibility Required](accessibility-required/MODIFIER.md)
- [Offline First](offline-first/MODIFIER.md)

Every package contains schema-validated `modifier.yaml` metadata and normative `MODIFIER.md` guidance.
The orchestrator loads Skill-mode effects directly from this metadata; explicit repository and user overrides
retain higher precedence.
