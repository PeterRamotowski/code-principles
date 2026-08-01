"""Resolve repository evidence and explicit context into an engineering policy.

The resolver deliberately uses small, inspectable decision tables.  It does not ask a
language or framework to choose an architecture: artifact evidence selects the base
profile, while technology evidence only selects adapters.
"""

from __future__ import annotations

import json
import re
from copy import deepcopy
from pathlib import Path
from typing import Any, Iterable

import yaml
from jsonschema import Draft202012Validator


ROOT = Path(__file__).resolve().parents[1]
SPECIFICATION_VERSION = (ROOT / "VERSION").read_text(encoding="utf-8").strip()
CONFIDENCE_ORDER = {
    "unknown": 0,
    "inferred-low": 1,
    "inferred-high": 2,
    "observed": 3,
    "explicit": 4,
}
LEVEL_ORDER = {"unknown": 0, "normal": 1, "elevated": 2, "high": 3, "critical": 4}

ARTIFACT_PROFILES = {
    "unknown": "general-software",
    "web-application": "browser-web-application",
    "frontend-application": "browser-web-application",
    "fullstack-application": "fullstack-web-application",
    "backend-service": "backend-service",
    "reusable-library": "reusable-library",
    "legacy-modernization": "legacy-modernization",
}

FALLBACK_PROFILE_MODES = {
    "general-software": {
        "code-clarity": "balanced",
        "abstraction-and-reuse": "conservative",
        "safe-change": "local-safe-change",
    },
}


def _load_profile_modes() -> dict[str, dict[str, str]]:
    """Load implemented profiles as the source of truth for default Skill modes."""
    modes = deepcopy(FALLBACK_PROFILE_MODES)
    for path in sorted((ROOT / "profiles").glob("*/profile.yaml")):
        data = yaml.safe_load(path.read_text(encoding="utf-8"))
        if not isinstance(data, dict):
            continue
        identifier = data.get("id")
        skill_modes = data.get("skill_modes")
        if isinstance(identifier, str) and isinstance(skill_modes, dict):
            modes[identifier] = dict(skill_modes)
    return modes


PROFILE_MODES = _load_profile_modes()

MODIFIER_MODES = {
    "public-api": {"api-and-compatibility": "external-api", "contracts-and-errors": "strict-boundaries"},
    "strict-backward-compatibility": {"safe-change": "compatibility-first"},
    "security-sensitive": {"contracts-and-errors": "strict-boundaries"},
    "high-throughput": {"performance-and-resources": "budget-constrained"},
    "memory-sensitive": {"performance-and-resources": "budget-constrained"},
    "latency-sensitive": {"performance-and-resources": "budget-constrained"},
    "real-time": {
        "contracts-and-errors": "safety-critical",
        "performance-and-resources": "hard-real-time",
        "state-and-side-effects": "single-owner-mutation",
    },
    "accessibility-required": {"testing-strategy": "integration-balanced"},
    "offline-first": {"distributed-reliability": "eventually-consistent"},
    "multi-tenant": {"contracts-and-errors": "strict-boundaries"},
}

SKILL_PRINCIPLES = {
    "code-clarity": ("kiss", "explicit-over-implicit"),
    "abstraction-and-reuse": ("yagni", "dry"),
    "modular-design": ("high-cohesion-low-coupling", "separation-of-concerns"),
    "contracts-and-errors": ("parse-dont-validate", "fail-fast"),
    "dependencies-and-boundaries": ("dependency-inversion-principle",),
    "state-and-side-effects": ("immutability", "command-query-separation"),
    "api-and-compatibility": ("backward-compatibility", "semantic-versioning"),
    "testing-strategy": ("test-behaviour-not-implementation",),
    "performance-and-resources": ("measure-dont-guess", "performance-budgeting"),
    "safe-change": ("chestertons-fence", "boy-scout-rule"),
    "distributed-reliability": ("idempotency", "eventual-consistency"),
    "engineering-review-lenses": ("murphys-law",),
}

TECHNOLOGY_FILES = {
    "typescript": ("*.ts", "*.tsx", "tsconfig.json"),
    "javascript": ("*.js", "*.jsx", "package.json"),
    "python": ("*.py", "pyproject.toml"),
    "php": ("*.php", "composer.json"),
    "go": ("*.go", "go.mod"),
    "cpp": ("*.cpp", "*.cc", "*.cxx", "*.hpp", "*.h", "CMakeLists.txt"),
}


class OrchestrationError(ValueError):
    """Raised when explicit orchestration input cannot produce a valid policy."""


def evidenced(value: str, confidence: str, evidence: Iterable[str]) -> dict[str, Any]:
    return {"value": value, "confidence": confidence, "evidence": sorted(set(evidence))}


def _load_yaml(path: Path) -> dict[str, Any]:
    try:
        data = yaml.safe_load(path.read_text(encoding="utf-8"))
    except (OSError, yaml.YAMLError) as exc:
        raise OrchestrationError(f"cannot read {path}: {exc}") from exc
    if not isinstance(data, dict):
        raise OrchestrationError(f"{path} must contain a mapping")
    return data


def _dependency_data(repository: Path) -> dict[str, Any]:
    package = repository / "package.json"
    if not package.is_file():
        return {}
    try:
        data = json.loads(package.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return {}
    dependencies: dict[str, Any] = {}
    for field in ("dependencies", "devDependencies", "peerDependencies"):
        if isinstance(data.get(field), dict):
            dependencies.update(data[field])
    return {"package": data, "dependencies": dependencies}


def _has(repository: Path, pattern: str) -> bool:
    if "*" not in pattern:
        return (repository / pattern).exists()
    return next(repository.rglob(pattern), None) is not None


def detect_repository_context(repository: Path, task: str = "") -> dict[str, Any]:
    """Detect conservative context from bounded repository signals."""
    repository = repository.resolve()
    if not repository.is_dir():
        raise OrchestrationError(f"repository is not a directory: {repository}")
    task_lower = task.lower()
    detected_languages = []
    for language, patterns in TECHNOLOGY_FILES.items():
        matches = [pattern for pattern in patterns if _has(repository, pattern)]
        if matches:
            detected_languages.append(evidenced(language, "observed", matches))
    if any(item["value"] == "typescript" for item in detected_languages):
        detected_languages = [item for item in detected_languages if item["value"] != "javascript"]

    node = _dependency_data(repository)
    dependencies = node.get("dependencies", {})
    framework_signals = {
        "react": "react",
        "nextjs": "next",
        "angular": "@angular/core",
        "vue": "vue",
        "nuxt": "nuxt",
    }
    frameworks = [
        evidenced(identifier, "observed", [f"package.json dependency {dependency}"])
        for identifier, dependency in framework_signals.items()
        if dependency in dependencies
    ]
    composer = repository / "composer.json"
    if composer.is_file():
        try:
            composer_data = json.loads(composer.read_text(encoding="utf-8"))
            php_dependencies = {**composer_data.get("require", {}), **composer_data.get("require-dev", {})}
        except (OSError, json.JSONDecodeError, TypeError):
            php_dependencies = {}
        for identifier, prefix in (("symfony", "symfony/"), ("drupal", "drupal/")):
            if any(name.startswith(prefix) for name in php_dependencies):
                frameworks.append(evidenced(identifier, "observed", [f"composer dependency {prefix}*"]))

    artifact = "unknown"
    artifact_evidence: list[str] = []
    confidence = "unknown"
    package = node.get("package", {})
    if "next" in dependencies or "nuxt" in dependencies:
        artifact, confidence = "fullstack-application", "inferred-high"
        artifact_evidence.append("integrated browser/server framework dependency")
    elif any(name in dependencies for name in ("react", "vue", "@angular/core")):
        artifact, confidence = "frontend-application", "inferred-high"
        artifact_evidence.append("browser UI framework dependency")
    elif package.get("exports") or package.get("publishConfig") or package.get("private") is False:
        artifact, confidence = "reusable-library", "inferred-high"
        artifact_evidence.append("package publishing or exports metadata")
    elif (repository / "pyproject.toml").is_file() and not any(
        word in task_lower for word in ("service", "server", "pipeline", "worker")
    ):
        artifact, confidence = "reusable-library", "inferred-low"
        artifact_evidence.append("Python project metadata without an observed executable role")

    task_artifacts = (
        ("legacy-modernization", ("legacy modernization", "modernize legacy", "migrate legacy")),
        ("fullstack-application", ("full-stack", "fullstack")),
        (
            "reusable-library",
            ("reusable library", "public library", "published library", "published package", " sdk"),
        ),
        ("frontend-application", ("browser application", "frontend application", "front-end application")),
        ("backend-service", ("backend service", "http service", "api service")),
    )
    stage = "unknown"
    stage_confidence = "unknown"
    for candidate, signals in task_artifacts:
        if any(signal in f" {task_lower}" for signal in signals):
            if candidate == "legacy-modernization":
                stage, stage_confidence = "legacy-modernization", "inferred-high"
            else:
                artifact, confidence = candidate, "inferred-high"
                artifact_evidence.append(f"task wording indicates {candidate}")
            break

    authority = "preserve-existing"
    authority_confidence = "inferred-high" if any(repository.iterdir()) else "inferred-low"
    if re.search(r"\b(redesign|re-architect|rearchitect)\b", task_lower):
        authority, authority_confidence = "redesign-allowed", "inferred-high"
    elif re.search(r"\b(refactor|moderniz|migrat|implement|add|build)\b", task_lower):
        authority, authority_confidence = "incremental-improvement", "inferred-high"
    elif re.search(r"\b(new project|greenfield)\b", task_lower):
        authority, authority_confidence = "greenfield", "inferred-high"

    exposure = []
    if re.search(r"\b(public api|webhook|external (?:api|integration|consumer))\b", task_lower):
        exposure.append(evidenced("external-integration", "inferred-high", ["task boundary wording"]))
    if re.search(r"\b(public|published) (?:\w+ )?library\b|\bpublished package\b", task_lower):
        exposure.append(evidenced("public-library", "inferred-high", ["task consumer wording"]))

    constraints = {}
    constraint_signals = {
        "security": (r"\b(payment|credential|authorization|authentication|personal data|secret)\b", "high"),
        "memory_sensitivity": (r"\b(memory limit|bounded memory|large (?:file|dataset|input))\b", "high"),
        "throughput_sensitivity": (r"\b(high throughput|throughput budget|events per second)\b", "high"),
        "latency_sensitivity": (r"\b(latency budget|response-time budget|low latency)\b", "high"),
        "accessibility": (r"\b(accessibility|required wcag|wcag requirement)\b", "high"),
        "backward_compatibility": (r"\b(backward compatibility|without changing (?:the )?(?:public )?api)\b", "high"),
    }
    for name, (pattern, level) in constraint_signals.items():
        if re.search(pattern, task_lower):
            constraints[name] = evidenced(level, "inferred-high", ["task constraint wording"])

    return {
        "specification_version": SPECIFICATION_VERSION,
        "selection_mode": "automatic-with-visible-result",
        "project": {
            "artifact_type": evidenced(artifact, confidence, artifact_evidence),
            "secondary_artifact_types": [],
            "project_stage": evidenced(stage, stage_confidence, []),
            "exposure": exposure,
            "domain_complexity": evidenced("unknown", "unknown", []),
            "architecture_authority": evidenced(
                authority, authority_confidence, ["task scope and repository state"]
            ),
            "state_model": [],
        },
        "constraints": constraints,
        "runtime": [],
        "languages": detected_languages,
        "frameworks": sorted(frameworks, key=lambda item: item["value"]),
        "technologies": [],
        "profiles": {},
        "overrides": {},
    }


def _normalize_evidenced(value: Any, confidence: str) -> dict[str, Any]:
    if isinstance(value, str):
        return evidenced(value, confidence, ["explicit override"])
    if not isinstance(value, dict) or "value" not in value:
        raise OrchestrationError(f"expected an evidenced value, got {value!r}")
    result = deepcopy(value)
    result.setdefault("confidence", confidence)
    result.setdefault("evidence", [])
    return result


def _merge_context(base: dict[str, Any], overlay: dict[str, Any], confidence: str) -> dict[str, Any]:
    """Merge a partial repository or user context; arrays intentionally replace."""
    result = deepcopy(base)
    singleton_project = {"artifact_type", "project_stage", "domain_complexity", "architecture_authority"}
    list_project = {"secondary_artifact_types", "exposure", "state_model"}
    for key, value in overlay.items():
        if key == "specification_version":
            if value != SPECIFICATION_VERSION:
                raise OrchestrationError(
                    f"context specification_version {value!r} does not match {SPECIFICATION_VERSION}"
                )
        elif key == "project" and isinstance(value, dict):
            for project_key, project_value in value.items():
                if project_key in singleton_project:
                    result["project"][project_key] = _normalize_evidenced(project_value, confidence)
                elif project_key in list_project:
                    result["project"][project_key] = [
                        _normalize_evidenced(item, confidence) for item in project_value
                    ]
                else:
                    raise OrchestrationError(f"unknown project context field: {project_key}")
        elif key == "constraints" and isinstance(value, dict):
            result["constraints"].update(
                {name: _normalize_evidenced(item, confidence) for name, item in value.items()}
            )
        elif key in {"runtime", "languages", "frameworks", "technologies"}:
            result[key] = [_normalize_evidenced(item, confidence) for item in value]
        elif key in {"profiles", "overrides"} and isinstance(value, dict):
            result[key].update(deepcopy(value))
        elif key == "selection_mode":
            result[key] = value
        else:
            raise OrchestrationError(f"unknown context field: {key}")
    return result


def _schema_errors(instance: dict[str, Any], schema_name: str) -> list[str]:
    schema = json.loads((ROOT / "schemas" / schema_name).read_text(encoding="utf-8"))
    issues = Draft202012Validator(schema).iter_errors(instance)
    return [
        f"{'.'.join(str(part) for part in issue.absolute_path) or '<root>'}: {issue.message}"
        for issue in sorted(issues, key=lambda error: [str(part) for part in error.absolute_path])
    ]


def _plain_context(context: dict[str, Any]) -> dict[str, Any]:
    project = context["project"]
    plain = {
        "artifact_type": project["artifact_type"]["value"],
        "architecture_authority": project["architecture_authority"]["value"],
    }
    for name in ("secondary_artifact_types", "exposure", "state_model"):
        values = [item["value"] for item in project.get(name, [])]
        if values:
            plain[name] = list(dict.fromkeys(values))
    for name in ("project_stage", "domain_complexity"):
        if name in project:
            plain[name] = project[name]["value"]
    runtime = [item["value"] for item in context.get("runtime", [])]
    if runtime:
        plain["runtime"] = list(dict.fromkeys(runtime))
    constraints = {name: item["value"] for name, item in context.get("constraints", {}).items()}
    if constraints:
        plain["constraints"] = constraints
    return plain


def _activate_modifiers(context: dict[str, Any], task: str) -> list[str]:
    exposure = {item["value"] for item in context["project"].get("exposure", [])}
    constraints = context.get("constraints", {})
    state = {item["value"] for item in context["project"].get("state_model", [])}
    modifiers = set(context.get("profiles", {}).get("modifiers", []))
    if exposure & {"public-api", "public-library", "external-integration", "extension-platform"}:
        modifiers.add("public-api")
    trigger_levels = {
        "security": "security-sensitive",
        "backward_compatibility": "strict-backward-compatibility",
        "throughput_sensitivity": "high-throughput",
        "memory_sensitivity": "memory-sensitive",
        "latency_sensitivity": "latency-sensitive",
        "accessibility": "accessibility-required",
    }
    for constraint, modifier in trigger_levels.items():
        level = constraints.get(constraint, {}).get("value", "unknown")
        threshold = "elevated" if constraint == "accessibility" else "high"
        if LEVEL_ORDER.get(level, 0) >= LEVEL_ORDER[threshold]:
            modifiers.add(modifier)
    determinism = constraints.get("determinism", {}).get("value", "unknown")
    if "real-time" in state or LEVEL_ORDER.get(determinism, 0) >= LEVEL_ORDER["high"]:
        modifiers.add("real-time")
    if "offline-synchronized" in state:
        modifiers.add("offline-first")
    if re.search(r"\bmulti[ -]?tenant\b", task.lower()):
        modifiers.add("multi-tenant")
    return sorted(modifiers)


def _selected_adapters(context: dict[str, Any], field: str) -> list[dict[str, Any]]:
    selected = []
    for item in context.get(field, []):
        if item.get("confidence") == "unknown":
            continue
        adapter = {"id": item["value"]}
        if item.get("version"):
            adapter["version"] = item["version"]
        selected.append(adapter)
    return sorted({item["id"]: item for item in selected}.values(), key=lambda item: item["id"])


def _skill_modes(
    profile: str, modifiers: list[str], repository_overrides: dict[str, Any], user_overrides: dict[str, Any]
) -> list[dict[str, Any]]:
    modes: dict[str, tuple[str, str, str]] = {
        skill: (mode, "profile", f"The {profile} profile selects this mode.")
        for skill, mode in PROFILE_MODES[profile].items()
    }
    for modifier in modifiers:
        for skill, mode in MODIFIER_MODES.get(modifier, {}).items():
            modes[skill] = (mode, "modifier", f"The {modifier} modifier strengthens this policy.")
    for source, overrides, output_source in (
        ("repository", repository_overrides, "repository-override"),
        ("user", user_overrides, "user-override"),
    ):
        for skill, mode in overrides.get("skill_modes", {}).items():
            modes[skill] = (mode, output_source, f"An explicit {source} override selects this mode.")
    return [
        {"id": skill, "mode": mode, "source": source, "rationale": rationale}
        for skill, (mode, source, rationale) in sorted(modes.items())
    ]


def _core_skill_policy(skill: str, mode: str) -> tuple[list[str], list[str], str] | None:
    """Load the implemented, mode-specific policy for a Core Skill when available."""
    metadata_path = ROOT / "core" / skill / "skill.yaml"
    if not metadata_path.is_file():
        return None
    metadata = _load_yaml(metadata_path)
    selected = next(
        (item for item in metadata.get("modes", []) if item.get("id") == mode),
        None,
    )
    if selected is None:
        raise OrchestrationError(f"implemented Core Skill {skill} has no mode {mode}")
    return (
        list(selected.get("emphasizes", [])),
        list(selected.get("suppressed_behaviours", [])),
        selected["description"],
    )


def _record_overrides(overrides: dict[str, Any], source: str) -> list[dict[str, Any]]:
    records = []
    for skill, mode in sorted(overrides.get("skill_modes", {}).items()):
        records.append({
            "source": source,
            "target": f"skill-modes.{skill}",
            "value": mode,
            "rationale": f"Explicit {source} engineering context.",
        })
    for field in ("required_patterns", "prohibited_patterns", "notes"):
        for index, value in enumerate(overrides.get(field, [])):
            records.append({
                "source": source,
                "target": f"{field.replace('_', '-')}.{index + 1}",
                "value": value,
                "rationale": f"Explicit {source} engineering context.",
            })
    return records


def _conflicts(profile: str, modifiers: list[str], languages: set[str]) -> list[dict[str, Any]]:
    conflicts = []
    if "public-api" in modifiers and languages & {"typescript", "python", "php"}:
        conflicts.append({
            "id": "static-types-vs-runtime-validation",
            "decision": "require-runtime-validation",
            "principles": ["make-illegal-states-unrepresentable", "parse-dont-validate"],
            "protected_attributes": ["correctness", "data-integrity"],
            "rationale": "Static type declarations do not validate external runtime input; parse it into a trusted representation.",
            "reconsider_when": [],
        })
    if "memory-sensitive" in modifiers:
        conflicts.append({
            "id": "materialization-vs-bounded-memory",
            "decision": "prefer-bounded-processing",
            "principles": ["kiss", "performance-budgeting"],
            "protected_attributes": ["memory-efficiency", "reliability"],
            "rationale": "Verified memory sensitivity makes bounded buffers or streaming safer than unbounded materialization.",
            "reconsider_when": ["verified input limits make full materialization safely bounded"],
        })
    if profile == "legacy-modernization":
        conflicts.append({
            "id": "cleanup-vs-behavior-preservation",
            "decision": "prefer-bounded-compatible-change",
            "principles": ["boy-scout-rule", "chestertons-fence"],
            "protected_attributes": ["correctness", "compatibility", "maintainability"],
            "rationale": "Modernization should improve the affected boundary while preserving behavior that is not explicitly authorized to change.",
            "reconsider_when": ["broader redesign authority and migration evidence are available"],
        })
    return conflicts


def _decisions(
    profile: str, modifiers: list[str], authority: str, *, explicitly_configured: bool
) -> list[dict[str, Any]]:
    profile_rationale = (
        "Explicit engineering context selects the base profile and takes precedence over detected defaults."
        if explicitly_configured
        else "The artifact and its consumers determine dominant engineering priorities; technology only refines them."
    )
    decisions = [{
        "id": "artifact-driven-profile",
        "statement": f"Apply the {profile} base profile to the affected artifact.",
        "rationale": profile_rationale,
        "scope": ["task"],
    }]
    if authority == "preserve-existing":
        decisions.append({
            "id": "preserve-existing-architecture",
            "statement": "Keep structural change local to the requested behavior.",
            "rationale": "The task does not grant authority for broad architectural replacement.",
            "scope": ["architecture"],
        })
    elif authority == "incremental-improvement":
        decisions.append({
            "id": "incremental-architecture-change",
            "statement": "Allow bounded refactoring near the changed behavior.",
            "rationale": "Incremental authority permits local improvement without repository-wide redesign.",
            "scope": ["architecture"],
        })
    modifier_decisions = {
        "public-api": ("preserve-public-contracts", "Preserve supported public behavior or provide an explicit migration path.", "Independent consumers cannot be changed atomically."),
        "security-sensitive": ("enforce-trust-boundaries", "Validate untrusted input and enforce authority at server or process boundaries.", "Elevated security makes boundary validation and least privilege correctness requirements."),
        "memory-sensitive": ("bound-memory-use", "Use bounded buffering or streaming for potentially large inputs.", "Unbounded materialization conflicts with the verified memory constraint."),
        "accessibility-required": ("verify-accessibility", "Treat accessibility behavior as a tested correctness requirement.", "The accessibility constraint changes implementation and verification policy."),
        "real-time": ("bound-critical-path", "Keep critical-path operations and resource use deterministic and bounded.", "Timing correctness requires explicit worst-case behavior."),
    }
    for modifier in modifiers:
        if modifier in modifier_decisions:
            identifier, statement, rationale = modifier_decisions[modifier]
            decisions.append({"id": identifier, "statement": statement, "rationale": rationale, "scope": ["task"]})
    return decisions


def _uncertainties(context: dict[str, Any]) -> list[dict[str, str]]:
    uncertainties = []
    material = (
        (context["project"]["artifact_type"], "What is the primary artifact type?", "Profile-specific priorities may change.", "Use the conservative general-software profile."),
        (context["project"]["architecture_authority"], "How much architectural change is authorized?", "The safe refactoring boundary may change.", "Preserve existing architecture and keep changes local."),
    )
    for item, question, impact, action in material:
        if item.get("confidence") in {"unknown", "inferred-low"}:
            uncertainties.append({"question": question, "impact": impact, "default_action": action})
    return uncertainties


def resolve_policy(
    repository: Path,
    *,
    task: str = "",
    repository_context: dict[str, Any] | None = None,
    user_context: dict[str, Any] | None = None,
) -> dict[str, Any]:
    """Produce a deterministic, schema-valid resolved policy."""
    detected = detect_repository_context(repository, task)
    repository_context = repository_context or {}
    user_context = user_context or {}
    normalized = _merge_context(detected, repository_context, "explicit")
    normalized = _merge_context(normalized, user_context, "explicit")
    context_errors = _schema_errors(normalized, "project-context.schema.json")
    if context_errors:
        raise OrchestrationError("invalid normalized context:\n- " + "\n- ".join(context_errors))

    artifact = normalized["project"]["artifact_type"]["value"]
    stage = normalized["project"].get("project_stage", {}).get("value", "unknown")
    explicit_profile = normalized.get("profiles", {}).get("base")
    if normalized["selection_mode"] == "manual" and not explicit_profile:
        raise OrchestrationError("manual selection_mode requires an explicit profiles.base value")
    profile = explicit_profile or (
        "legacy-modernization" if stage == "legacy-modernization" else ARTIFACT_PROFILES.get(artifact)
    )
    if profile not in PROFILE_MODES:
        raise OrchestrationError(f"unsupported base profile for the MVP: {profile or artifact}")
    modifiers = _activate_modifiers(normalized, task)
    languages = _selected_adapters(normalized, "languages")
    frameworks = _selected_adapters(normalized, "frameworks")
    repository_overrides = repository_context.get("overrides", {})
    user_overrides = user_context.get("overrides", {})
    active_skills = _skill_modes(profile, modifiers, repository_overrides, user_overrides)

    principles_by_id: dict[str, dict[str, str]] = {}
    skill_prohibitions = []
    for skill in active_skills:
        core_policy = _core_skill_policy(skill["id"], skill["mode"])
        if core_policy:
            principles, suppressed, mode_description = core_policy
            skill_prohibitions.extend(suppressed)
        else:
            principles = list(SKILL_PRINCIPLES.get(skill["id"], ()))
            suppressed = []
            mode_description = f"Apply the selected {skill['mode']} mode to the current task scope."
        for principle in principles:
            principles_by_id.setdefault(principle, {
                "id": principle,
                "interpretation": mode_description,
                "source": skill["id"],
                "status": "active",
            })
    active_principles = [principles_by_id[item] for item in sorted(principles_by_id)]
    language_ids = {item["id"] for item in languages}
    authority = normalized["project"]["architecture_authority"]["value"]
    prohibited = list(dict.fromkeys(
        repository_overrides.get("prohibited_patterns", [])
        + user_overrides.get("prohibited_patterns", [])
        + skill_prohibitions
    ))
    decisions = _decisions(
        profile, modifiers, authority, explicitly_configured=bool(explicit_profile)
    )
    profile_summary = (
        f"{profile} profile selected by explicit engineering context."
        if explicit_profile
        else f"{profile} profile selected from {artifact} artifact evidence."
    )
    summary_items = [
        profile_summary,
        f"Architecture authority: {authority}.",
    ]
    if modifiers:
        summary_items.append(f"Active modifiers: {', '.join(modifiers)}.")
    adapters = [item["id"] for item in languages + frameworks]
    if adapters:
        summary_items.append(f"Technology refinements: {', '.join(adapters)}.")

    policy = {
        "specification_version": SPECIFICATION_VERSION,
        "policy_version": SPECIFICATION_VERSION,
        "selection_mode": normalized["selection_mode"],
        "context": _plain_context(normalized),
        "base_profile": profile,
        "modifiers": modifiers,
        "language_adapters": languages,
        "framework_adapters": frameworks,
        "active_core_skills": active_skills,
        "overrides": _record_overrides(repository_overrides, "repository")
        + _record_overrides(user_overrides, "user"),
        "conflicts": _conflicts(profile, modifiers, language_ids),
        "significant_decisions": decisions,
        "unresolved_uncertainties": _uncertainties(normalized),
        "prohibited_decisions": prohibited,
        "visible_summary": {
            "show": normalized["selection_mode"] != "manual" or bool(summary_items),
            "items": summary_items,
        },
        "active_principles": active_principles,
        "external_skill_dependencies": [],
    }
    policy_errors = _schema_errors(policy, "resolved-policy.schema.json")
    if policy_errors:
        raise OrchestrationError("resolver produced an invalid policy:\n- " + "\n- ".join(policy_errors))
    return policy


def load_context(path: Path | None) -> dict[str, Any]:
    """Load an optional YAML context document."""
    return _load_yaml(path) if path else {}
