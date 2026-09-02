"""Generate MkDocs navigation from the repository's canonical metadata.

This hook keeps generated documentation pages inside the Material navigation tree so
active tabs and side navigation remain available on deep pages without maintaining a
large static nav block by hand.
"""
from __future__ import annotations

from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]


def load_yaml(path: Path):
    return yaml.safe_load(path.read_text(encoding="utf-8"))


def component_pages(directory: str, metadata_name: str) -> list[dict[str, str]]:
    pages: list[dict[str, str]] = []
    for metadata in sorted((ROOT / directory).glob(f"*/{metadata_name}")):
        data = load_yaml(metadata) or {}
        item_id = data.get("id", metadata.parent.name)
        name = data.get("name") or item_id.replace("-", " ").title()
        pages.append({str(name): f"{directory}/{item_id}/index.md"})
    return sorted(pages, key=lambda item: next(iter(item)).casefold())


def principle_catalogue() -> list[dict[str, list[dict[str, str]]]]:
    registry = load_yaml(ROOT / "principles" / "registry.yaml") or {}
    categories_data = load_yaml(ROOT / "principles" / "categories.yaml") or {}
    principles = registry.get("principles") or []

    categories = [
        (category["id"], category["name"])
        for category in categories_data.get("categories") or []
    ]

    groups: list[dict[str, list[dict[str, str]]]] = []
    for category_id, category_name in categories:
        entries = [item for item in principles if item.get("category") == category_id]
        if not entries:
            continue
        pages = [
            {str(item["name"]): f"principles/compendium/{item['id']}.md"}
            for item in sorted(entries, key=lambda value: str(value["name"]).casefold())
        ]
        groups.append({str(category_name): pages})
    return groups


def evaluation_pages() -> list[dict[str, str]]:
    pages: list[dict[str, str]] = []
    for path in sorted((ROOT / "evaluations" / "scenarios").glob("*.yaml")):
        data = load_yaml(path) or {}
        scenario_id = data.get("id", path.stem)
        title = data.get("name") or data.get("title") or scenario_id.replace("-", " ").title()
        pages.append({str(title): f"evaluations/{scenario_id}/index.md"})
    return sorted(pages, key=lambda item: next(iter(item)).casefold())


def build_nav():
    return [
        {"Home": "index.md"},
        {
            "Principles": [
                "principles/index.md",
                {"Catalogue": principle_catalogue()},
                {"Classification": "principles/CLASSIFICATION.md"},
                {"Authoring guide": "principles/AUTHORING-GUIDE.md"},
            ]
        },
        {
            "Decision system": [
                "decision-system/index.md",
                {"Core Skills": ["core/index.md", *component_pages("core", "skill.yaml")]},
                {"Project profiles": ["profiles/index.md", *component_pages("profiles", "profile.yaml")]},
                {"Modifiers": ["modifiers/index.md", *component_pages("modifiers", "modifier.yaml")]},
                {"Conflict resolution": "CONFLICT-RESOLUTION.md"},
                {"Orchestrator": "orchestrator/SKILL.md"},
            ]
        },
        {
            "Technologies": [
                "technologies/index.md",
                {"Languages": ["languages/index.md", *component_pages("languages", "adapter.yaml")]},
                {"Frameworks": ["frameworks/index.md", *component_pages("frameworks", "adapter.yaml")]},
            ]
        },
        {
            "Examples": [
                "examples/index.md",
                {"Evaluation scenarios": ["evaluations/index.md", *evaluation_pages()]},
            ]
        },
        {
            "Reference": [
                "reference/index.md",
                {"Repository overview": "README.md"},
                {"Specification": "SPECIFICATION.md"},
                {"Architecture": "ARCHITECTURE.md"},
                {"Knowledge model": "KNOWLEDGE-MODEL.md"},
                {"Terminology": "TERMINOLOGY.md"},
                {"Self-containment": "SELF-CONTAINMENT.md"},
                {"Contributing": "CONTRIBUTING.md"},
                {"Roadmap": "ROADMAP.md"},
                {"Changelog": "CHANGELOG.md"},
            ]
        },
    ]


def on_config(config, **kwargs):
    config["nav"] = build_nav()
    return config
