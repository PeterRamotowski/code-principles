#!/usr/bin/env python3
"""Build a non-normative MkDocs source tree from the repository's canonical documentation."""
from __future__ import annotations

import html
import shutil
from pathlib import Path
from typing import Iterable

import yaml

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / ".site-docs"
SITE_SOURCE = ROOT / "docs-site"

ROOT_DOCS = [
    "README.md",
    "SPECIFICATION.md",
    "ARCHITECTURE.md",
    "KNOWLEDGE-MODEL.md",
    "SELF-CONTAINMENT.md",
    "TERMINOLOGY.md",
    "CONFLICT-RESOLUTION.md",
    "CONTRIBUTING.md",
    "ROADMAP.md",
    "CHANGELOG.md",
]

MARKDOWN_TREES = [
    "principles",
    "core",
    "profiles",
    "modifiers",
    "languages",
    "frameworks",
    "orchestrator",
    "evaluations",
]

COMPONENT_INDEX_SOURCE = {
    "core": "SKILL.md",
    "profiles": "PROFILE.md",
    "modifiers": "MODIFIER.md",
    "languages": "SKILL.md",
    "frameworks": "SKILL.md",
}


def load_yaml(path: Path):
    return yaml.safe_load(path.read_text(encoding="utf-8"))


def copy_markdown_tree(relative: str) -> None:
    source = ROOT / relative
    if not source.is_dir():
        return

    index_source = COMPONENT_INDEX_SOURCE.get(relative)
    for path in source.rglob("*.md"):
        destination = OUT / path.relative_to(ROOT)
        destination.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(path, destination)

        # Component cards link to /<collection>/<id>/. Publish the canonical
        # component document at that directory index as well as its source name.
        if index_source and path.name == index_source and path.parent.parent == source:
            shutil.copy2(path, destination.parent / "index.md")


def write(relative: str, content: str) -> None:
    path = OUT / relative
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content.rstrip() + "\n", encoding="utf-8")


def cards(items: Iterable[dict], details_key: str = "description") -> str:
    rendered = []
    for item in sorted(items, key=lambda value: value.get("name", value["id"])):
        item_id = item["id"]
        name = html.escape(str(item.get("name", item_id)))
        description = html.escape(str(item.get(details_key, "")))
        search_text = html.escape(f"{name} {description} {item_id}".lower(), quote=True)
        rendered.append(
            f'<a class="catalog-card" data-catalog-item data-search="{search_text}" href="{item_id}/">'
            f'<span class="catalog-card__title">{name}</span>'
            f'<span class="catalog-card__description">{description}</span>'
            f'<span class="catalog-card__id">{html.escape(item_id)}</span>'
            "</a>"
        )
    return "\n".join(rendered)


def catalog_page(title: str, intro: str, body: str, count: int) -> str:
    return f"""# {title}

{intro}

<div class="catalog-toolbar">
  <label for="catalog-filter">Filter {count} entries</label>
  <input id="catalog-filter" type="search" placeholder="Type a name, topic, or identifier…" autocomplete="off" data-catalog-filter>
  <span class="catalog-toolbar__count" data-catalog-count>{count} entries</span>
</div>

<div class="catalog-grid" data-catalog>
{body}
</div>

<p class="catalog-empty" data-catalog-empty hidden>No matching entries.</p>
"""


def generate_principles() -> None:
    registry = load_yaml(ROOT / "principles" / "registry.yaml")
    categories = {
        item["id"]: item["name"]
        for item in load_yaml(ROOT / "principles" / "categories.yaml")["categories"]
    }
    principles = registry["principles"]
    groups = []
    for category_id, category_name in categories.items():
        group = [item for item in principles if item["category"] == category_id]
        if not group:
            continue
        rows = []
        for item in sorted(group, key=lambda value: value["name"]):
            entry = load_yaml(ROOT / item["source"])
            name = html.escape(entry["name"])
            summary = html.escape(entry["summary"])
            classification = html.escape(entry["classification"])
            search_text = html.escape(
                f"{entry['name']} {entry['id']} {entry['summary']} {entry['classification']} {category_name}".lower(),
                quote=True,
            )
            rows.append(
                f'<a class="catalog-card" data-catalog-item data-search="{search_text}" '
                f'href="compendium/{entry["id"]}/">'
                f'<span class="catalog-card__title">{name}</span>'
                f'<span class="catalog-card__description">{summary}</span>'
                f'<span class="catalog-card__meta">{classification}</span>'
                "</a>"
            )
        groups.append(
            f'<section class="catalog-group"><h2>{html.escape(category_name)}</h2>'
            f'<div class="catalog-grid">{"".join(rows)}</div></section>'
        )

    page = f"""# Principles

Browse the canonical engineering catalogue as a human-readable reference. The YAML entries remain the source of truth; these pages are generated views.

<div class="catalog-toolbar">
  <label for="catalog-filter">Filter {len(principles)} principles</label>
  <input id="catalog-filter" type="search" placeholder="Try “compatibility”, “testing”, or “complexity”…" autocomplete="off" data-catalog-filter>
  <span class="catalog-toolbar__count" data-catalog-count>{len(principles)} entries</span>
</div>

<div data-catalog>
{''.join(groups)}
</div>

<p class="catalog-empty" data-catalog-empty hidden>No matching principles.</p>
"""
    write("principles/index.md", page)


def load_components(directory: str, metadata_name: str) -> list[dict]:
    items = []
    for metadata in sorted((ROOT / directory).glob(f"*/{metadata_name}")):
        data = load_yaml(metadata)
        if data:
            items.append(data)
    return items


def generate_component_hubs() -> None:
    skills = load_components("core", "skill.yaml")
    write(
        "core/index.md",
        catalog_page(
            "Core Skills",
            "Core Skills turn canonical principles into language-independent decision procedures. Choose a Skill to inspect its modes, conflicts, and review rules.",
            cards(skills),
            len(skills),
        ),
    )

    profiles = load_components("profiles", "profile.yaml")
    write(
        "profiles/index.md",
        catalog_page(
            "Project profiles",
            "Profiles configure the dominant artifact and failure model before language or framework refinements are applied.",
            cards(profiles),
            len(profiles),
        ),
    )

    modifiers = load_components("modifiers", "modifier.yaml")
    write(
        "modifiers/index.md",
        catalog_page(
            "Engineering modifiers",
            "Modifiers strengthen policy when a verified cross-cutting constraint applies. They never replace the base project profile.",
            cards(modifiers),
            len(modifiers),
        ),
    )

    languages = load_components("languages", "adapter.yaml")
    write(
        "languages/index.md",
        catalog_page(
            "Language adapters",
            "Language adapters refine generic engineering policy with runtime, type-system, packaging, concurrency, and resource semantics.",
            cards(languages),
            len(languages),
        ),
    )

    frameworks = load_components("frameworks", "adapter.yaml")
    write(
        "frameworks/index.md",
        catalog_page(
            "Framework adapters",
            "Framework adapters refine project policy with lifecycle, boundary, state, extension, and convention decisions.",
            cards(frameworks),
            len(frameworks),
        ),
    )


def inline_code(value) -> str:
    return f"`{str(value).replace('`', '\\`')}`"


def render_value(value) -> str:
    if value is None:
        return "—"
    if isinstance(value, list):
        return ", ".join(inline_code(item) for item in value) if value else "—"
    if isinstance(value, dict):
        return "; ".join(f"{inline_code(key)}: {inline_code(item)}" for key, item in value.items()) or "—"
    return inline_code(value)


def markdown_table(mapping: dict) -> str:
    if not mapping:
        return "_None._"
    rows = ["| Item | Expected |", "| --- | --- |"]
    for key, value in mapping.items():
        rendered = render_value(value).replace("|", "\\|")
        rows.append(f"| {inline_code(key)} | {rendered} |")
    return "\n".join(rows)


def yaml_block(value) -> str:
    dumped = yaml.safe_dump(value, sort_keys=False, allow_unicode=True).rstrip()
    return f"```yaml\n{dumped}\n```"


def scenario_page(path: Path, data: dict) -> str:
    scenario_id = data.get("id", path.stem)
    title = data.get("name") or data.get("title") or scenario_id.replace("-", " ").title()
    description = data.get("description") or "Executable policy resolution scenario."
    scenario_input = data.get("input") or {}
    expected = data.get("expected") or {}
    request = scenario_input.get("request") or ""
    repository_signals = scenario_input.get("repository_signals") or {}
    forbidden = data.get("forbidden") or []
    principles = data.get("principles_under_test") or []

    summary_rows = {
        "Profile": expected.get("profile"),
        "Modifiers": expected.get("modifiers"),
        "Language adapters": expected.get("language_adapters"),
        "Framework adapters": expected.get("framework_adapters"),
    }

    repository_sections = []
    for filename, content in repository_signals.items():
        repository_sections.append(f"### `{filename}`\n\n```text\n{str(content).rstrip()}\n```")
    repository_body = "\n\n".join(repository_sections) if repository_sections else "_No repository signals._"

    principle_links = "\n".join(
        f"- [{principle}](../../principles/compendium/{principle}.md)" for principle in principles
    ) or "_None._"
    decision_list = "\n".join(f"- {inline_code(item)}" for item in expected.get("significant_decisions") or []) or "_None._"
    forbidden_list = "\n".join(f"- {item}" for item in forbidden) or "_None._"

    return f"""# {title}

{description}

!!! info "Generated example"
    This page is generated from `{path.relative_to(ROOT)}`. The scenario YAML remains the executable source of truth.

## Request

> {request}

## Repository evidence

{repository_body}

## Expected resolution

| Resolution layer | Expected |
| --- | --- |
| Profile | {render_value(summary_rows['Profile'])} |
| Modifiers | {render_value(summary_rows['Modifiers'])} |
| Language adapters | {render_value(summary_rows['Language adapters'])} |
| Framework adapters | {render_value(summary_rows['Framework adapters'])} |

### Normalized context

{yaml_block(expected.get('context') or {})}

### Skill modes

{markdown_table(expected.get('skill_modes') or {})}

### Conflict decisions

{markdown_table(expected.get('conflicts') or {})}

### Significant decisions

{decision_list}

### Principles under test

{principle_links}

### Forbidden outcomes

{forbidden_list}

## Scenario source

{yaml_block(data)}
"""


def generate_evaluations() -> None:
    scenario_dir = ROOT / "evaluations" / "scenarios"
    scenarios = []
    for path in sorted(scenario_dir.glob("*.yaml")):
        data = load_yaml(path) or {}
        scenario_id = data.get("id", path.stem)
        title = data.get("name") or data.get("title") or scenario_id.replace("-", " ").title()
        request = ((data.get("input") or {}).get("request") or "")
        description = data.get("description") or request or "Executable policy scenario"
        scenarios.append((scenario_id, title, description, data, path))

    rows = []
    for scenario_id, title, description, data, path in scenarios:
        search_text = html.escape(f"{scenario_id} {title} {description}".lower(), quote=True)
        rows.append(
            f'<a class="catalog-card" data-catalog-item data-search="{search_text}" href="{scenario_id}/">'
            f'<span class="catalog-card__title">{html.escape(str(title))}</span>'
            f'<span class="catalog-card__description">{html.escape(str(description))}</span>'
            f'<span class="catalog-card__id">{html.escape(str(scenario_id))}</span>'
            "</a>"
        )
        write(f"evaluations/{scenario_id}/index.md", scenario_page(path, data))

    write(
        "evaluations/index.md",
        catalog_page(
            "Evaluation scenarios",
            "Browse generated, human-readable views of the executable scenarios that exercise policy selection, conflict boundaries, technology refinements, and rejected overengineering.",
            "\n".join(rows),
            len(rows),
        ),
    )


def main() -> None:
    if OUT.exists():
        shutil.rmtree(OUT)
    shutil.copytree(SITE_SOURCE, OUT)

    for filename in ROOT_DOCS:
        shutil.copy2(ROOT / filename, OUT / filename)
    for relative in MARKDOWN_TREES:
        copy_markdown_tree(relative)

    generate_principles()
    generate_component_hubs()
    generate_evaluations()
    print(f"Generated MkDocs source at {OUT.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
