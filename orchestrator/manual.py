"""Render a self-contained task bundle for manual agent testing."""

from __future__ import annotations

from pathlib import Path
from typing import Any

import yaml

from orchestrator.resolver import ADAPTER_METADATA, ROOT


def _load_yaml(path: Path) -> dict[str, Any]:
    data = yaml.safe_load(path.read_text(encoding="utf-8"))
    return data if isinstance(data, dict) else {}


def _applied_adapter_ids(policy: dict[str, Any]) -> list[str]:
    ordered: list[str] = []

    def add(identifier: str) -> None:
        metadata = ADAPTER_METADATA[identifier]
        for dependency in metadata.get("extends", []) + metadata.get("requires", []):
            add(dependency)
        if identifier not in ordered:
            ordered.append(identifier)

    for item in policy.get("language_adapters", []) + policy.get("framework_adapters", []):
        add(item["id"])
    return ordered


def _source_documents(policy: dict[str, Any]) -> list[tuple[str, str, Path]]:
    documents: list[tuple[str, str, Path]] = []
    for skill in policy["active_core_skills"]:
        path = ROOT / "core" / skill["id"] / "SKILL.md"
        documents.append(("Core Skill", f"{skill['id']} ({skill['mode']})", path))

    profile_metadata = _load_yaml(ROOT / "profiles" / policy["base_profile"] / "profile.yaml")
    profile_path = ROOT / profile_metadata["normative_document"]
    documents.append(("Profile", policy["base_profile"], profile_path))

    for identifier in policy.get("modifiers", []):
        metadata = _load_yaml(ROOT / "modifiers" / identifier / "modifier.yaml")
        documents.append(("Modifier", identifier, ROOT / metadata["normative_document"]))

    for identifier in _applied_adapter_ids(policy):
        metadata = ADAPTER_METADATA[identifier]
        kind = "Language adapter" if metadata["type"] == "language-adapter" else "Framework adapter"
        documents.append((kind, identifier, ROOT / metadata["normative_document"]))
    return documents


def render_manual_bundle(repository: Path, task: str, policy: dict[str, Any]) -> str:
    """Create one Markdown prompt containing the resolved policy and selected sources."""
    lines = [
        "# Code Principles Manual Test Bundle",
        "",
        "Use this task-scoped bundle while implementing or reviewing the task in the target repository.",
        "Repository evidence and the current user request outrank general guidance in the source documents.",
        "",
        "## Target",
        "",
        f"- Repository: `{repository}`",
        f"- Task: {task or '[No task supplied]'}",
        f"- Base profile: `{policy['base_profile']}`",
        f"- Modifiers: {', '.join(f'`{item}`' for item in policy.get('modifiers', [])) or 'none'}",
        "- Language adapters: "
        + (", ".join(f"`{item['id']}`" for item in policy.get("language_adapters", [])) or "none"),
        "- Framework adapters: "
        + (", ".join(f"`{item['id']}`" for item in policy.get("framework_adapters", [])) or "none"),
        "",
        "## Manual execution contract",
        "",
        "1. Inspect the target repository and verify the detected context before changing code.",
        "2. Apply only guidance relevant to the requested task and affected technology paths.",
        "3. Preserve existing conventions unless the task authorizes a broader change.",
        "4. Treat significant decisions and prohibitions below as task requirements.",
        "5. Run the target repository's existing tests, linters, analyzers, and build checks; do not invent success.",
        "6. Report the files changed, verification performed, unresolved uncertainty, and any policy conflict.",
        "",
        "## Selected modes",
        "",
    ]
    for skill in policy["active_core_skills"]:
        lines.append(f"- `{skill['id']}`: `{skill['mode']}` ({skill['source']})")

    lines.extend(["", "## Significant decisions", ""])
    for decision in policy["significant_decisions"]:
        lines.append(f"- `{decision['id']}`: {decision['statement']}")

    lines.extend(["", "## Prohibited decisions", ""])
    prohibitions = policy.get("prohibited_decisions", [])
    lines.extend(f"- {item}" for item in prohibitions)
    if not prohibitions:
        lines.append("- None beyond the selected source documents and repository policy.")

    uncertainties = policy.get("unresolved_uncertainties", [])
    if uncertainties:
        lines.extend(["", "## Unresolved uncertainties", ""])
        for item in uncertainties:
            lines.append(
                f"- {item['question']} Default: {item.get('default_action', 'keep the change conservative')}"
            )

    lines.extend([
        "",
        "## Selected policy sources",
        "",
        "Apply these documents in the displayed order. Later technology-specific documents refine earlier general guidance.",
    ])
    for kind, identifier, path in _source_documents(policy):
        relative = path.relative_to(ROOT).as_posix()
        lines.extend([
            "",
            f"### {kind}: {identifier}",
            "",
            f"Source: `{relative}`",
            "",
            path.read_text(encoding="utf-8").rstrip(),
        ])
    return "\n".join(lines) + "\n"
