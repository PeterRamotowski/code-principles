#!/usr/bin/env python3
"""Validate the complete Code Principles repository."""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import subprocess
import sys
from collections import Counter, defaultdict
from pathlib import Path
from urllib.parse import unquote

import yaml
from jsonschema import Draft202012Validator

from distribution import distribution_files


ROOT = Path(__file__).resolve().parents[1]
IDENTIFIER_RE = re.compile(r"^[a-z][a-z0-9]*(?:-[a-z0-9]+)*$")
SEMANTIC_VERSION_RE = re.compile(
    r"^(0|[1-9][0-9]*)\.(0|[1-9][0-9]*)\.(0|[1-9][0-9]*)"
    r"(?:-[0-9A-Za-z.-]+)?(?:\+[0-9A-Za-z.-]+)?$"
)
MILESTONE_4_SKILLS = {
    "code-clarity",
    "abstraction-and-reuse",
    "modular-design",
    "contracts-and-errors",
    "testing-strategy",
    "safe-change",
}
MILESTONE_5_PROFILES = {
    "browser-web-application",
    "fullstack-web-application",
    "backend-service",
    "reusable-library",
    "legacy-modernization",
}
MILESTONE_6_ADAPTERS = {"typescript", "python", "cpp"}
MILESTONE_7_ADAPTERS = {"javascript", "php", "go"}
IMPLEMENTED_LANGUAGE_ADAPTERS = MILESTONE_6_ADAPTERS | MILESTONE_7_ADAPTERS
MILESTONE_8_ADAPTERS = {"react", "nextjs", "vue", "nuxt", "angular", "symfony", "drupal"}


class DuplicateKeyError(ValueError):
    """Raised when YAML or JSON contains a duplicate mapping key."""


class UniqueKeyLoader(yaml.SafeLoader):
    """Safe YAML loader that rejects duplicate mapping keys."""


def construct_unique_mapping(loader, node, deep=False):
    mapping = {}
    for key_node, value_node in node.value:
        key = loader.construct_object(key_node, deep=deep)
        if key in mapping:
            raise DuplicateKeyError(f"duplicate mapping key: {key!r}")
        mapping[key] = loader.construct_object(value_node, deep=deep)
    return mapping


UniqueKeyLoader.add_constructor(
    yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG, construct_unique_mapping
)


def unique_json_object(pairs):
    result = {}
    for key, value in pairs:
        if key in result:
            raise DuplicateKeyError(f"duplicate mapping key: {key!r}")
        result[key] = value
    return result


class RepositoryValidator:
    def __init__(self, *, lint_normative: bool = False):
        self.errors: list[str] = []
        self.lint_normative = lint_normative
        self.documents: dict[Path, object] = {}
        self.version = ""

    def relative(self, path: Path) -> str:
        return path.relative_to(ROOT).as_posix()

    def error(self, message: str) -> None:
        self.errors.append(message)

    def load_json(self, path: Path):
        if path in self.documents:
            return self.documents[path]
        data = json.loads(path.read_text(encoding="utf-8"), object_pairs_hook=unique_json_object)
        self.documents[path] = data
        return data

    def load_yaml(self, path: Path):
        if path in self.documents:
            return self.documents[path]
        data = yaml.load(path.read_text(encoding="utf-8"), Loader=UniqueKeyLoader)
        self.documents[path] = data
        return data

    def load(self, path: Path):
        return self.load_json(path) if path.suffix == ".json" else self.load_yaml(path)

    def parse_machine_readable_files(self) -> None:
        paths = set(distribution_files(ROOT))
        github_dir = ROOT / ".github"
        if github_dir.is_dir():
            paths.update(path for path in github_dir.rglob("*") if path.is_file())
        for path in sorted(paths):
            if path.suffix not in {".json", ".yaml", ".yml"}:
                continue
            try:
                data = self.load(path)
                if data is None:
                    self.error(f"{self.relative(path)}: document is empty")
            except Exception as exc:
                self.error(f"{self.relative(path)}: invalid {path.suffix[1:].upper()}: {exc}")

    def validate_schema_instance(self, path: Path, schema_path: Path) -> None:
        if path not in self.documents or schema_path not in self.documents:
            return
        instance = self.documents[path]
        schema = self.documents[schema_path]
        for issue in sorted(
            Draft202012Validator(schema).iter_errors(instance),
            key=lambda error: [str(part) for part in error.absolute_path],
        ):
            location = ".".join(str(part) for part in issue.absolute_path)
            suffix = f" at {location}" if location else ""
            self.error(f"{self.relative(path)}{suffix}: {issue.message}")

    def check_schemas(self) -> None:
        for path in sorted((ROOT / "schemas").glob("*.json")):
            if path not in self.documents:
                continue
            try:
                schema = self.documents[path]
                Draft202012Validator.check_schema(schema)
                if not schema.get("$id", "").endswith(f":{self.version}"):
                    self.error(f"{self.relative(path)}: $id version does not match VERSION")
                declared = schema.get("properties", {}).get("schema_version", {}).get("const")
                if declared is not None and declared != self.version:
                    self.error(
                        f"{self.relative(path)}: schema_version const does not match VERSION"
                    )
            except Exception as exc:
                self.error(f"{self.relative(path)}: invalid schema: {exc}")

    def validate_known_instances(self) -> None:
        schema_dir = ROOT / "schemas"
        mappings = [
            (ROOT / "principles/registry.yaml", schema_dir / "principle-registry.schema.json"),
            (ROOT / "principles/relationships.yaml", schema_dir / "relationships.schema.json"),
            (ROOT / "engineering-context.example.yaml", schema_dir / "project-context.schema.json"),
        ]
        mappings.extend(
            (path, schema_dir / "principle.schema.json")
            for path in sorted((ROOT / "principles/entries").glob("*.yaml"))
        )
        mappings.extend(
            (path, schema_dir / "resolved-policy.schema.json")
            for path in sorted((ROOT / "orchestrator/examples").glob("*.yaml"))
        )
        mappings.extend(
            (path, schema_dir / "evaluation-scenario.schema.json")
            for path in sorted((ROOT / "evaluations/scenarios").glob("*.yaml"))
        )
        mappings.extend(
            (path, schema_dir / "skill.schema.json")
            for path in sorted(ROOT.glob("**/skill.yaml"))
            if ".git" not in path.parts
        )
        mappings.extend(
            (path, schema_dir / "profile.schema.json")
            for path in sorted(ROOT.glob("profiles/*/profile.yaml"))
        )
        mappings.extend(
            (path, schema_dir / "modifier.schema.json")
            for path in sorted(ROOT.glob("modifiers/*/modifier.yaml"))
        )
        mappings.extend(
            (path, schema_dir / "adapter.schema.json")
            for path in sorted(ROOT.glob("languages/*/adapter.yaml"))
            + sorted(ROOT.glob("frameworks/*/adapter.yaml"))
        )
        for path, schema_path in mappings:
            self.validate_schema_instance(path, schema_path)

    def check_unique_ids(self, items, label: str, path: Path) -> set[str]:
        ids = [item.get("id") for item in items if isinstance(item, dict)]
        for identifier, count in sorted(Counter(ids).items(), key=lambda pair: str(pair[0])):
            if identifier is None:
                continue
            if count > 1:
                self.error(f"{self.relative(path)}: duplicate {label} id: {identifier}")
        return {identifier for identifier in ids if isinstance(identifier, str)}

    def require_reference(self, source: str, field: str, target: str, known: set[str]) -> None:
        if target not in known:
            self.error(f"{source}: {field} references unknown identifier {target}")

    def check_cycle(self, graph: dict[str, set[str]], label: str) -> None:
        state: dict[str, int] = {}
        stack: list[str] = []

        def visit(node: str) -> None:
            state[node] = 1
            stack.append(node)
            for dependency in sorted(graph.get(node, set())):
                if dependency not in graph:
                    continue
                if state.get(dependency) == 1:
                    start = stack.index(dependency)
                    cycle = stack[start:] + [dependency]
                    self.error(f"{label} dependency cycle: {' -> '.join(cycle)}")
                elif state.get(dependency, 0) == 0:
                    visit(dependency)
            stack.pop()
            state[node] = 2

        for node in sorted(graph):
            if state.get(node, 0) == 0:
                visit(node)

    def check_metadata_and_references(self) -> int:
        categories_path = ROOT / "principles/categories.yaml"
        entries_paths = sorted((ROOT / "principles/entries").glob("*.yaml"))
        registry_path = ROOT / "principles/registry.yaml"
        relationships_path = ROOT / "principles/relationships.yaml"
        catalogs = {
            name: self.documents.get(ROOT / f"catalogs/{name}.yaml", {})
            for name in ("core-skills", "profiles", "modifiers", "languages", "frameworks")
        }

        categories = self.check_unique_ids(
            self.documents.get(categories_path, {}).get("categories", []), "category", categories_path
        )
        skill_items = catalogs["core-skills"].get("skills", [])
        profile_items = catalogs["profiles"].get("profiles", [])
        modifier_items = catalogs["modifiers"].get("modifiers", [])
        language_items = catalogs["languages"].get("languages", [])
        framework_items = catalogs["frameworks"].get("frameworks", [])
        skills = self.check_unique_ids(skill_items, "core skill", ROOT / "catalogs/core-skills.yaml")
        profiles = self.check_unique_ids(profile_items, "profile", ROOT / "catalogs/profiles.yaml")
        modifiers = self.check_unique_ids(
            modifier_items, "modifier", ROOT / "catalogs/modifiers.yaml"
        )
        languages = self.check_unique_ids(
            language_items, "language adapter", ROOT / "catalogs/languages.yaml"
        )
        frameworks = self.check_unique_ids(
            framework_items, "framework adapter", ROOT / "catalogs/frameworks.yaml"
        )
        adapters = languages | frameworks
        for identifier in sorted(languages & frameworks):
            self.error(
                f"adapter id is used by both language and framework catalogues: {identifier}"
            )

        skill_modes = {
            item["id"]: set(item.get("modes", []))
            for item in skill_items
            if isinstance(item, dict) and isinstance(item.get("id"), str)
        }

        entries = {}
        for path in entries_paths:
            data = self.documents.get(path)
            if not isinstance(data, dict) or not isinstance(data.get("id"), str):
                continue
            identifier = data["id"]
            if identifier in entries:
                self.error(f"duplicate principle id: {identifier}")
            entries[identifier] = data
            if path.stem != identifier:
                self.error(f"{self.relative(path)}: filename does not match principle id {identifier}")
        principles = set(entries)

        for identifier, data in entries.items():
            source = f"principles/entries/{identifier}.yaml"
            self.require_reference(source, "category", data.get("category"), categories)
            self.require_reference(
                source, "primary_core_skill", data.get("primary_core_skill"), skills
            )
            for field in ("conflicts_with", "reinforces"):
                for target in data.get(field, []):
                    self.require_reference(source, field, target, principles)
            if not (ROOT / "principles/compendium" / f"{identifier}.md").exists():
                self.error(f"missing compendium page for {identifier}")

        registry = self.documents.get(registry_path, {})
        registry_ids = self.check_unique_ids(
            registry.get("principles", []), "registry principle", registry_path
        )
        if registry_ids != principles:
            self.error("principles/registry.yaml: IDs do not match canonical entry IDs")

        relationships = self.documents.get(relationships_path, {}).get("relationships", [])
        seen_relationships = set()
        for index, relationship in enumerate(relationships):
            if not isinstance(relationship, dict):
                continue
            source = f"principles/relationships.yaml relationship {index}"
            for field in ("from", "to"):
                self.require_reference(source, field, relationship.get(field), principles)
            key = (relationship.get("from"), relationship.get("type"), relationship.get("to"))
            if key in seen_relationships:
                self.error(f"{source}: duplicate relationship {key}")
            seen_relationships.add(key)

        adapter_graph = {identifier: set() for identifier in adapters}
        for item in language_items:
            source = f"catalogs/languages.yaml {item.get('id')}"
            for target in item.get("extends", []):
                self.require_reference(source, "extends", target, languages)
                adapter_graph[item["id"]].add(target)
        for item in framework_items:
            source = f"catalogs/frameworks.yaml {item.get('id')}"
            for target in item.get("requires", []):
                self.require_reference(source, "requires", target, adapters)
                adapter_graph[item["id"]].add(target)
        self.check_cycle(adapter_graph, "adapter catalogue")

        implemented_skills = []
        for path in sorted(ROOT.glob("**/skill.yaml")):
            data = self.documents.get(path)
            if isinstance(data, dict):
                implemented_skills.append((path, data))
                if data.get("type") == "core-skill":
                    skills.add(data.get("id"))
                    skill_modes[data.get("id")] = {
                        mode.get("id") for mode in data.get("modes", []) if isinstance(mode, dict)
                    }
        self.check_duplicate_metadata(implemented_skills, "skill")
        skill_graph = {
            data["id"]: set(data.get("requires", []))
            for _, data in implemented_skills
            if isinstance(data.get("id"), str)
        }
        for path, data in implemented_skills:
            source = self.relative(path)
            normative_document = data.get("normative_document")
            if normative_document and not (ROOT / normative_document).is_file():
                self.error(f"{source}: normative_document does not exist: {normative_document}")
            modes = {
                mode.get("id") for mode in data.get("modes", []) if isinstance(mode, dict)
            }
            if data.get("default_mode") is not None:
                self.require_reference(source, "default_mode", data.get("default_mode"), modes)
            for target in data.get("requires", []):
                self.require_reference(source, "requires", target, skills)
            for conflict in data.get("conflicts_with", []):
                self.require_reference(source, "conflicts_with", conflict.get("id"), skills)
            for field in ("primary", "supporting", "constrains"):
                for target in data.get("principles", {}).get(field, []):
                    self.require_reference(source, f"principles.{field}", target, principles)
            for mode in data.get("modes", []):
                for field in ("emphasizes", "constrains"):
                    for target in mode.get(field, []):
                        self.require_reference(
                            source, f"modes.{mode.get('id')}.{field}", target, principles
                        )
        self.check_cycle(skill_graph, "skill metadata")

        self.check_core_skill_mvp(
            skill_items,
            implemented_skills,
            languages | frameworks,
        )

        self.check_component_metadata(
            profiles, modifiers, adapters, skills, skill_modes, principles
        )
        self.check_project_profiles_mvp(profile_items, adapters, skills, skill_modes)
        self.check_language_adapters_mvp(language_items, skills, principles)
        self.check_framework_adapters_mvp(framework_items, skills, principles)
        self.check_examples_and_context(
            profiles, modifiers, languages, frameworks, skills, skill_modes, principles
        )
        self.check_profiles_are_language_independent(profile_items, adapters)
        return len(principles)

    def check_language_adapters_mvp(self, catalogue_items, skills, principles) -> None:
        """Enforce the Definitions of Done for implemented language adapters."""
        catalogue = {
            item.get("id"): item
            for item in catalogue_items
            if isinstance(item, dict) and isinstance(item.get("id"), str)
        }
        implemented = {
            data.get("id"): (path, data)
            for path in sorted(ROOT.glob("languages/*/adapter.yaml"))
            if isinstance((data := self.documents.get(path)), dict)
            and data.get("type") == "language-adapter"
            and isinstance(data.get("id"), str)
        }
        missing = sorted(MILESTONE_6_ADAPTERS - set(implemented))
        if missing:
            self.error(
                f"Milestone 6: missing implemented language adapters: {', '.join(missing)}"
            )
        missing = sorted(MILESTONE_7_ADAPTERS - set(implemented))
        if missing:
            self.error(
                f"Milestone 7: missing implemented language adapters: {', '.join(missing)}"
            )

        scenarios_by_adapter = defaultdict(list)
        resolutions_by_profile = defaultdict(dict)
        for path in sorted((ROOT / "evaluations/scenarios").glob("*.yaml")):
            data = self.documents.get(path)
            if not isinstance(data, dict):
                continue
            adapter = data.get("input", {}).get("language_adapter")
            if isinstance(adapter, str):
                scenarios_by_adapter[adapter].append((path, data))
                profile = data.get("input", {}).get("profile")
                resolution = data.get("expected", {}).get("resolution")
                if isinstance(profile, str) and isinstance(resolution, str):
                    resolutions_by_profile[profile][adapter] = resolution

        required_terms = {
            "typescript": ("`unknown`", "discriminated unions", "runtime", "generics", "package"),
            "python": (
                "`Protocol`",
                "data class",
                "exceptions",
                "generators",
                "context manager",
                "CPU-bound",
                "public imports",
            ),
            "cpp": (
                "RAII",
                "ownership",
                "value semantics",
                "smart pointers",
                "const",
                "error policy",
                "templates",
                "allocation",
                "ABI",
                "undefined behavior",
                "concurrency",
            ),
            "javascript": (
                "coercion",
                "runtime validation",
                "modules",
                "promises",
                "mutation",
                "dynamic contracts",
            ),
            "php": (
                "strict_types",
                "exceptions",
                "value objects",
                "composer",
                "attributes",
                "reflection",
                "long-running",
                "framework interoperability",
            ),
            "go": (
                "consumer-defined",
                "error values",
                "context",
                "goroutine",
                "channels",
                "shared state",
                "package visibility",
                "allocation",
                "benchmark",
            ),
        }
        for identifier in sorted(IMPLEMENTED_LANGUAGE_ADAPTERS & set(implemented)):
            path, data = implemented[identifier]
            expected_path = ROOT / "languages" / identifier / "adapter.yaml"
            if path != expected_path:
                self.error(
                    f"{self.relative(path)}: adapter metadata must be at "
                    f"languages/{identifier}/adapter.yaml"
                )
            catalogue_item = catalogue.get(identifier)
            if not catalogue_item:
                self.error(
                    f"{self.relative(path)}: adapter is missing from catalogs/languages.yaml"
                )
            elif set(data.get("extends", [])) != set(catalogue_item.get("extends", [])):
                self.error(f"{self.relative(path)}: extends does not match catalogs/languages.yaml")
            if not data.get("refines"):
                self.error(f"{self.relative(path)}: adapter must refine at least one Core Skill")
            for refinement in data.get("refines", []):
                self.require_reference(
                    self.relative(path), "refines.skill", refinement.get("skill"), skills
                )
            for refinement in data.get("principle_refinements", []):
                self.require_reference(
                    self.relative(path),
                    "principle_refinements.principle",
                    refinement.get("principle"),
                    principles,
                )

            normative = ROOT / data.get("normative_document", "")
            if normative.is_file():
                text = normative.read_text(encoding="utf-8").lower()
                for term in required_terms[identifier]:
                    if term.lower() not in text:
                        self.error(
                            f"{self.relative(normative)}: required adapter focus is not documented: {term}"
                        )
            examples = ROOT / "languages" / identifier / "examples"
            example_text = "\n".join(
                item.read_text(encoding="utf-8") for item in sorted(examples.glob("*.md"))
            )
            if "Positive example" not in example_text or "Negative example" not in example_text:
                self.error(
                    f"languages/{identifier}/examples: positive and negative examples are required"
                )
            if not scenarios_by_adapter.get(identifier):
                self.error(f"languages/{identifier}: at least one evaluation scenario is required")

        same_profile_variance = any(
            MILESTONE_6_ADAPTERS <= set(by_adapter)
            and len({by_adapter[item] for item in MILESTONE_6_ADAPTERS})
            == len(MILESTONE_6_ADAPTERS)
            for by_adapter in resolutions_by_profile.values()
        )
        if not same_profile_variance:
            self.error(
                "Milestone 6: one project profile must produce distinct guidance for all representative adapters"
            )

        remaining_profile_variance = any(
            MILESTONE_7_ADAPTERS <= set(by_adapter)
            and len({by_adapter[item] for item in MILESTONE_7_ADAPTERS})
            == len(MILESTONE_7_ADAPTERS)
            for by_adapter in resolutions_by_profile.values()
        )
        if not remaining_profile_variance:
            self.error(
                "Milestone 7: one project profile must produce distinct guidance for all remaining adapters"
            )

        typescript = implemented.get("typescript")
        if typescript and set(typescript[1].get("extends", [])) != {"javascript"}:
            self.error("Milestone 7: TypeScript must explicitly extend JavaScript")

    def check_framework_adapters_mvp(self, catalogue_items, skills, principles) -> None:
        """Enforce the Milestone 8 Definition of Done for framework adapters."""
        catalogue = {
            item.get("id"): item
            for item in catalogue_items
            if isinstance(item, dict) and isinstance(item.get("id"), str)
        }
        implemented = {
            data.get("id"): (path, data)
            for path in sorted(ROOT.glob("frameworks/*/adapter.yaml"))
            if isinstance((data := self.documents.get(path)), dict)
            and data.get("type") == "framework-adapter"
            and isinstance(data.get("id"), str)
        }
        missing = sorted(MILESTONE_8_ADAPTERS - set(implemented))
        if missing:
            self.error(f"Milestone 8: missing implemented framework adapters: {', '.join(missing)}")

        scenarios = defaultdict(list)
        for path in sorted((ROOT / "evaluations/scenarios").glob("*.yaml")):
            data = self.documents.get(path)
            adapter = data.get("input", {}).get("framework_adapter") if isinstance(data, dict) else None
            if isinstance(adapter, str):
                scenarios[adapter].append(path)

        required_terms = {
            "react": ("state locality", "effects", "composition", "behavior-focused", "typescript typing rules"),
            "nextjs": ("server", "client", "cache", "server actions", "secrets"),
            "vue": ("reactivity", "composables", "component scope", "state locality", "effects"),
            "nuxt": ("refines vue", "server", "client", "ssr", "data fetching", "auto-import"),
            "angular": ("dependency injection", "standalone components", "signals", "rxjs", "forms"),
            "symfony": ("service container", "httpkernel", "messenger", "doctrine", "configuration"),
            "drupal": ("extension", "cacheability metadata", "entities", "configuration", "hooks"),
        }
        for identifier in sorted(MILESTONE_8_ADAPTERS & set(implemented)):
            path, data = implemented[identifier]
            expected_path = ROOT / "frameworks" / identifier / "adapter.yaml"
            if path != expected_path:
                self.error(f"{self.relative(path)}: adapter metadata must be at frameworks/{identifier}/adapter.yaml")
            item = catalogue.get(identifier)
            if not item:
                self.error(f"{self.relative(path)}: adapter is missing from catalogs/frameworks.yaml")
            elif set(data.get("requires", [])) != set(item.get("requires", [])):
                self.error(f"{self.relative(path)}: requires does not match catalogs/frameworks.yaml")
            if not data.get("refines"):
                self.error(f"{self.relative(path)}: adapter must refine at least one Core Skill")
            normative = ROOT / data.get("normative_document", "")
            if normative.is_file():
                content = normative.read_text(encoding="utf-8").lower()
                for term in required_terms[identifier]:
                    if term not in content:
                        self.error(f"{self.relative(normative)}: required adapter focus is not documented: {term}")
            examples = ROOT / "frameworks" / identifier / "examples"
            example_text = "\n".join(item.read_text(encoding="utf-8") for item in sorted(examples.glob("*.md")))
            if "Positive example" not in example_text or "Negative example" not in example_text:
                self.error(f"frameworks/{identifier}/examples: positive and negative examples are required")
            if not scenarios.get(identifier):
                self.error(f"frameworks/{identifier}: at least one evaluation scenario is required")

        if implemented.get("react") and "typescript" in implemented["react"][1].get("requires", []):
            self.error("Milestone 8: React must not require TypeScript or define its typing policy")
        if implemented.get("nuxt") and "vue" not in implemented["nuxt"][1].get("requires", []):
            self.error("Milestone 8: Nuxt must refine Vue")
        if implemented.get("drupal") and set(implemented["drupal"][1].get("requires", [])) != {"php", "symfony"}:
            self.error("Milestone 8: Drupal must require PHP and Symfony")

    def check_project_profiles_mvp(
        self, catalogue_items, technologies, skills, skill_modes
    ) -> None:
        """Enforce the Milestone 5 Definition of Done for project profiles."""
        catalogue = {
            item.get("id"): item
            for item in catalogue_items
            if isinstance(item, dict) and isinstance(item.get("id"), str)
        }
        implemented = {
            data.get("id"): (path, data)
            for path in sorted(ROOT.glob("profiles/*/profile.yaml"))
            if isinstance((data := self.documents.get(path)), dict)
            and data.get("type") == "project-profile"
            and isinstance(data.get("id"), str)
        }
        missing = sorted(MILESTONE_5_PROFILES - set(implemented))
        if missing:
            self.error(f"Milestone 5: missing implemented profiles: {', '.join(missing)}")

        scenarios_by_profile = defaultdict(list)
        shared_conflict_resolutions = defaultdict(set)
        for path in sorted((ROOT / "evaluations/scenarios").glob("*.yaml")):
            data = self.documents.get(path)
            if not isinstance(data, dict):
                continue
            profile = data.get("input", {}).get("profile")
            if isinstance(profile, str):
                scenarios_by_profile[profile].append((path, data))
                conflict = data.get("input", {}).get("conflict")
                resolution = data.get("expected", {}).get("resolution")
                if isinstance(conflict, str) and isinstance(resolution, str):
                    shared_conflict_resolutions[conflict].add(resolution)

        technology_re = re.compile(
            r"\b(?:" + "|".join(re.escape(item) for item in sorted(technologies)) + r")\b",
            re.IGNORECASE,
        )
        for identifier in sorted(MILESTONE_5_PROFILES & set(implemented)):
            path, data = implemented[identifier]
            expected_path = ROOT / "profiles" / identifier / "profile.yaml"
            if path != expected_path:
                self.error(
                    f"{self.relative(path)}: profile metadata must be at "
                    f"profiles/{identifier}/profile.yaml"
                )
            if identifier not in catalogue:
                self.error(f"{self.relative(path)}: profile is missing from catalogs/profiles.yaml")

            normative = ROOT / data.get("normative_document", "")
            if not normative.is_file():
                continue
            text = normative.read_text(encoding="utf-8")
            for skill, mode in sorted(data.get("skill_modes", {}).items()):
                self.check_skill_mode(self.relative(path), skill, mode, skills, skill_modes)
                if f"`{skill}`" not in text or f"`{mode}`" not in text:
                    self.error(
                        f"{self.relative(normative)}: default mode is not documented: "
                        f"{skill}={mode}"
                    )
            combined_text = text + "\n" + yaml.safe_dump(data, sort_keys=True)
            match = technology_re.search(combined_text)
            if match:
                self.error(
                    f"{self.relative(normative)}: profile contains technology-specific guidance: "
                    f"{match.group(0)}"
                )
            if not scenarios_by_profile.get(identifier):
                self.error(f"profiles/{identifier}: at least one evaluation scenario is required")

        if not any(len(resolutions) >= 3 for resolutions in shared_conflict_resolutions.values()):
            self.error(
                "Milestone 5: scenarios must demonstrate at least three different resolutions "
                "for the same principle conflict"
            )

    def check_core_skill_mvp(self, catalogue_items, implemented_skills, technologies) -> None:
        """Enforce the Milestone 4 Definition of Done for implemented Core Skills."""
        catalogue = {
            item.get("id"): item
            for item in catalogue_items
            if isinstance(item, dict) and isinstance(item.get("id"), str)
        }
        implemented = {
            data.get("id"): (path, data)
            for path, data in implemented_skills
            if data.get("type") == "core-skill" and isinstance(data.get("id"), str)
        }
        missing = sorted(MILESTONE_4_SKILLS - set(implemented))
        if missing:
            self.error(f"Milestone 4: missing implemented Core Skills: {', '.join(missing)}")

        scenarios_by_skill = defaultdict(list)
        for path in sorted((ROOT / "evaluations/scenarios").glob("*.yaml")):
            data = self.documents.get(path)
            if not isinstance(data, dict):
                continue
            skill = data.get("input", {}).get("skill")
            if isinstance(skill, str):
                scenarios_by_skill[skill].append((path, data))

        technology_re = re.compile(
            r"\b(?:" + "|".join(re.escape(item) for item in sorted(technologies)) + r")\b",
            re.IGNORECASE,
        )
        for identifier in sorted(MILESTONE_4_SKILLS & set(implemented)):
            path, data = implemented[identifier]
            expected_path = ROOT / "core" / identifier / "skill.yaml"
            if path != expected_path:
                self.error(
                    f"{self.relative(path)}: Core Skill metadata must be at "
                    f"core/{identifier}/skill.yaml"
                )
            catalogue_item = catalogue.get(identifier, {})
            catalogue_modes = set(catalogue_item.get("modes", []))
            metadata_modes = {
                mode.get("id") for mode in data.get("modes", []) if isinstance(mode, dict)
            }
            if catalogue_modes != metadata_modes:
                self.error(
                    f"{self.relative(path)}: modes do not match catalogs/core-skills.yaml"
                )
            if len(data.get("conflicts_with", [])) < 3:
                self.error(f"{self.relative(path)}: Core Skill must define at least three conflicts")

            normative = ROOT / data.get("normative_document", "")
            if not normative.is_file():
                continue
            text = normative.read_text(encoding="utf-8")
            for mode in sorted(metadata_modes):
                if f"`{mode}`" not in text:
                    self.error(
                        f"{self.relative(normative)}: mode is not documented: {mode}"
                    )
            match = technology_re.search(text)
            if match:
                self.error(
                    f"{self.relative(normative)}: Core Skill contains technology-specific rule: "
                    f"{match.group(0)}"
                )

            examples = sorted((ROOT / "core" / identifier / "examples").glob("*.md"))
            example_text = "\n".join(item.read_text(encoding="utf-8") for item in examples)
            if "Positive example" not in example_text or "Negative example" not in example_text:
                self.error(
                    f"core/{identifier}/examples: positive and negative examples are required"
                )

            scenarios = scenarios_by_skill.get(identifier, [])
            if len(scenarios) < 3:
                self.error(
                    f"core/{identifier}: at least three evaluation scenarios are required"
                )
            modes_under_evaluation = {
                scenario.get("input", {}).get("mode") for _, scenario in scenarios
            }
            unknown_modes = sorted(
                mode for mode in modes_under_evaluation if mode not in metadata_modes
            )
            if unknown_modes:
                self.error(
                    f"core/{identifier}: evaluation scenarios reference unknown modes: "
                    f"{', '.join(unknown_modes)}"
                )

    def check_duplicate_metadata(self, metadata, label: str) -> None:
        paths_by_id = defaultdict(list)
        for path, data in metadata:
            if isinstance(data.get("id"), str):
                paths_by_id[data["id"]].append(self.relative(path))
        for identifier, paths in sorted(paths_by_id.items()):
            if len(paths) > 1:
                self.error(f"duplicate implemented {label} id {identifier}: {', '.join(paths)}")

    def check_component_metadata(
        self, profiles, modifiers, adapters, skills, skill_modes, principles
    ) -> None:
        groups = [
            (sorted(ROOT.glob("profiles/*/profile.yaml")), "profile"),
            (sorted(ROOT.glob("modifiers/*/modifier.yaml")), "modifier"),
            (
                sorted(ROOT.glob("languages/*/adapter.yaml"))
                + sorted(ROOT.glob("frameworks/*/adapter.yaml")),
                "adapter",
            ),
        ]
        metadata_by_label = {}
        for paths, label in groups:
            metadata_by_label[label] = [
                (path, self.documents[path])
                for path in paths
                if isinstance(self.documents.get(path), dict)
            ]
        profiles.update(
            data["id"]
            for _, data in metadata_by_label["profile"]
            if isinstance(data.get("id"), str)
        )
        modifiers.update(
            data["id"]
            for _, data in metadata_by_label["modifier"]
            if isinstance(data.get("id"), str)
        )
        adapters.update(
            data["id"]
            for _, data in metadata_by_label["adapter"]
            if isinstance(data.get("id"), str)
        )
        adapter_graph = {identifier: set() for identifier in adapters}
        for paths, label in groups:
            metadata = metadata_by_label[label]
            self.check_duplicate_metadata(metadata, label)
            for path, data in metadata:
                source = self.relative(path)
                normative_document = data.get("normative_document")
                if normative_document and not (ROOT / normative_document).is_file():
                    self.error(
                        f"{source}: normative_document does not exist: {normative_document}"
                    )
                if label == "profile":
                    for skill, mode in data.get("skill_modes", {}).items():
                        self.check_skill_mode(source, skill, mode, skills, skill_modes)
                    for target in data.get("recommended_modifiers", []):
                        self.require_reference(source, "recommended_modifiers", target, modifiers)
                    for field in ("requires", "conflicts_with"):
                        for target in data.get(field, []):
                            self.require_reference(
                                source, field, target, profiles | modifiers
                            )
                elif label == "modifier":
                    for target in data.get("conflicts", []):
                        self.require_reference(source, "conflicts", target, modifiers)
                else:
                    adapter_graph.setdefault(data.get("id"), set())
                    for field in ("extends", "requires"):
                        for target in data.get(field, []):
                            self.require_reference(source, field, target, adapters)
                            adapter_graph[data.get("id")].add(target)
                    for refinement in data.get("refines", []):
                        skill = refinement.get("skill")
                        self.require_reference(source, "refines.skill", skill, skills)
                        for mode in refinement.get("supported_modes", []):
                            self.check_skill_mode(source, skill, mode, skills, skill_modes)
                    for refinement in data.get("principle_refinements", []):
                        self.require_reference(
                            source,
                            "principle_refinements.principle",
                            refinement.get("principle"),
                            principles,
                        )
        self.check_cycle(adapter_graph, "adapter metadata")

    def check_skill_mode(self, source, skill, mode, skills, skill_modes) -> None:
        self.require_reference(source, "skill", skill, skills)
        if skill in skill_modes:
            self.require_reference(source, f"mode for {skill}", mode, skill_modes[skill])

    def check_examples_and_context(
        self, profiles, modifiers, languages, frameworks, skills, skill_modes, principles
    ) -> None:
        context_path = ROOT / "engineering-context.example.yaml"
        context = self.documents.get(context_path, {})
        source = self.relative(context_path)
        configured_profiles = context.get("profiles", {})
        if configured_profiles.get("base"):
            self.require_reference(source, "profiles.base", configured_profiles["base"], profiles)
        for target in configured_profiles.get("modifiers", []):
            self.require_reference(source, "profiles.modifiers", target, modifiers)
        for field, known in (("languages", languages), ("frameworks", frameworks)):
            for technology in context.get(field, []):
                self.require_reference(source, field, technology.get("value"), known)
        for skill, mode in context.get("overrides", {}).get("skill_modes", {}).items():
            self.check_skill_mode(source, skill, mode, skills, skill_modes)

        for path in sorted((ROOT / "orchestrator/examples").glob("*.yaml")):
            data = self.documents.get(path, {})
            source = self.relative(path)
            self.check_unique_ids(
                data.get("language_adapters", []), "selected language adapter", path
            )
            self.check_unique_ids(
                data.get("framework_adapters", []), "selected framework adapter", path
            )
            self.check_unique_ids(data.get("active_core_skills", []), "active core skill", path)
            self.check_unique_ids(data.get("conflicts", []), "conflict", path)
            self.check_unique_ids(
                data.get("significant_decisions", []), "significant decision", path
            )
            self.check_unique_ids(data.get("active_principles", []), "active principle", path)
            self.require_reference(source, "base_profile", data.get("base_profile"), profiles)
            for target in data.get("modifiers", []):
                self.require_reference(source, "modifiers", target, modifiers)
            for adapter in data.get("language_adapters", []):
                self.require_reference(source, "language_adapters", adapter.get("id"), languages)
            for adapter in data.get("framework_adapters", []):
                self.require_reference(source, "framework_adapters", adapter.get("id"), frameworks)
            for active in data.get("active_core_skills", []):
                self.check_skill_mode(
                    source, active.get("id"), active.get("mode"), skills, skill_modes
                )
            for conflict in data.get("conflicts", []):
                for target in conflict.get("principles", []):
                    self.require_reference(source, "conflicts.principles", target, principles)
            for active in data.get("active_principles", []):
                self.require_reference(source, "active_principles.id", active.get("id"), principles)
                self.require_reference(source, "active_principles.source", active.get("source"), skills)

        scenario_ids = []
        for path in sorted((ROOT / "evaluations/scenarios").glob("*.yaml")):
            data = self.documents.get(path, {})
            source = self.relative(path)
            scenario_ids.append((data.get("id"), source))
            profile = data.get("input", {}).get("profile")
            if profile is not None:
                self.require_reference(source, "input.profile", profile, profiles)
            language_adapter = data.get("input", {}).get("language_adapter")
            if language_adapter is not None:
                self.require_reference(
                    source, "input.language_adapter", language_adapter, languages
                )
            for target in data.get("principles_under_test", []):
                self.require_reference(source, "principles_under_test", target, principles)
            expected = data.get("expected", {})
            for field in ("active_principles", "constrained_principles", "suppressed_principles"):
                for target in expected.get(field, []):
                    self.require_reference(source, f"expected.{field}", target, principles)
        duplicate_scenarios = [
            identifier
            for identifier, count in Counter(identifier for identifier, _ in scenario_ids).items()
            if identifier is not None and count > 1
        ]
        for identifier in sorted(duplicate_scenarios):
            self.error(f"duplicate evaluation scenario id: {identifier}")

    def check_profiles_are_language_independent(self, profile_items, adapters) -> None:
        technology_re = re.compile(
            r"\b(?:" + "|".join(re.escape(identifier) for identifier in sorted(adapters)) + r")\b",
            re.IGNORECASE,
        )
        for item in profile_items:
            text = " ".join(str(value) for key, value in item.items() if key != "id")
            match = technology_re.search(text)
            if match:
                self.error(
                    f"catalogs/profiles.yaml {item.get('id')}: profile is coupled to technology {match.group(0)}"
                )

    def check_versions(self) -> None:
        version_path = ROOT / "VERSION"
        self.version = version_path.read_text(encoding="utf-8").strip()
        if not SEMANTIC_VERSION_RE.fullmatch(self.version):
            self.error(f"VERSION is not valid semantic versioning: {self.version}")

        for path, data in self.documents.items():
            if isinstance(data, dict):
                for field in (
                    "schema_version",
                    "specification_version",
                    "policy_version",
                    "version",
                ):
                    if field in data and data[field] != self.version:
                        self.error(
                            f"{self.relative(path)}: {field} does not match VERSION ({data[field]!r})"
                        )

        declarations = [
            (ROOT / "README.md", f"Foundation version: `{self.version}`", "foundation version"),
            (
                ROOT / "SPECIFICATION.md",
                f"Specification version: `{self.version}`",
                "specification version",
            ),
        ]
        for path, expected, label in declarations:
            if expected not in path.read_text(encoding="utf-8"):
                self.error(f"{self.relative(path)}: {label} does not match VERSION")
        changelog = (ROOT / "CHANGELOG.md").read_text(encoding="utf-8")
        if not re.search(
            rf"^## \[{re.escape(self.version)}\](?:\s|$)", changelog, re.MULTILINE
        ):
            self.error("CHANGELOG.md: missing release heading for VERSION")

    def check_generated_outputs(self) -> None:
        generated = subprocess.run(
            [sys.executable, str(ROOT / "tools/generate_compendium.py"), "--check"],
            cwd=ROOT,
            text=True,
            capture_output=True,
        )
        if generated.returncode:
            detail = (generated.stdout or generated.stderr).strip()
            suffix = f": {detail}" if detail else ""
            self.error(f"generated outputs are not current{suffix}")

    def check_manifest(self) -> None:
        manifest_path = ROOT / "MANIFEST.sha256"
        expected = {
            path.relative_to(ROOT).as_posix(): hashlib.sha256(path.read_bytes()).hexdigest()
            for path in distribution_files(ROOT)
        }
        actual = {}
        for line in manifest_path.read_text(encoding="utf-8").splitlines():
            digest, separator, relative = line.partition("  ")
            if not separator or not re.fullmatch(r"[0-9a-f]{64}", digest) or not relative:
                self.error(f"MANIFEST.sha256: invalid line: {line}")
                continue
            if relative in actual:
                self.error(f"MANIFEST.sha256: duplicate path: {relative}")
            actual[relative] = digest
        missing = sorted(set(expected) - set(actual))
        extra = sorted(set(actual) - set(expected))
        changed = sorted(
            path for path in set(actual) & set(expected) if actual[path] != expected[path]
        )
        if missing:
            self.error(f"MANIFEST.sha256: missing files: {', '.join(missing)}")
        if extra:
            self.error(f"MANIFEST.sha256: unexpected files: {', '.join(extra)}")
        if changed:
            self.error(f"MANIFEST.sha256: stale hashes: {', '.join(changed)}")

    @staticmethod
    def markdown_anchor(text: str) -> str:
        text = re.sub(r"<[^>]+>", "", text).strip().lower()
        text = re.sub(r"[^\w\- ]", "", text, flags=re.UNICODE)
        return re.sub(r"[ ]+", "-", text)

    def markdown_anchors(self, path: Path) -> set[str]:
        anchors = set()
        counts = Counter()
        in_fence = False
        for line in path.read_text(encoding="utf-8").splitlines():
            if re.match(r"^\s*(```|~~~)", line):
                in_fence = not in_fence
                continue
            if in_fence:
                continue
            match = re.match(r"^#{1,6}\s+(.+?)\s*#*\s*$", line)
            if not match:
                continue
            base = self.markdown_anchor(match.group(1))
            count = counts[base]
            counts[base] += 1
            anchors.add(base if count == 0 else f"{base}-{count}")
        return anchors

    @staticmethod
    def link_destination(raw: str) -> str:
        raw = raw.strip()
        if raw.startswith("<") and ">" in raw:
            return raw[1 : raw.index(">")]
        return raw.split(maxsplit=1)[0]

    def check_markdown_file(self, path: Path, anchor_cache=None) -> None:
        inline_re = re.compile(r"!?\[[^\]]*\]\(([^)]+)\)")
        reference_re = re.compile(r"^\s*\[[^\]]+\]:\s*(\S+)", re.MULTILINE)
        anchor_cache = anchor_cache if anchor_cache is not None else {}
        text = path.read_text(encoding="utf-8")
        for raw in inline_re.findall(text) + reference_re.findall(text):
            target = self.link_destination(raw)
            if not target or "://" in target or target.startswith("mailto:"):
                continue
            file_part, _, fragment = target.partition("#")
            decoded = unquote(file_part)
            resolved = (path.parent / decoded).resolve() if decoded else path.resolve()
            try:
                resolved.relative_to(ROOT.resolve())
            except ValueError:
                self.error(f"{self.relative(path)}: link escapes repository: {raw}")
                continue
            if not resolved.exists():
                self.error(f"{self.relative(path)}: broken local link: {raw}")
                continue
            if fragment and resolved.suffix == ".md":
                anchors = anchor_cache.setdefault(resolved, self.markdown_anchors(resolved))
                if unquote(fragment).lower() not in anchors:
                    self.error(f"{self.relative(path)}: broken Markdown anchor: {raw}")

    def check_markdown_links(self) -> None:
        anchor_cache = {}
        for path in (file for file in distribution_files(ROOT) if file.suffix == ".md"):
            self.check_markdown_file(path, anchor_cache)

    def check_normative_file(self, path: Path) -> None:
        mixed_case = re.compile(r"\b(?:Must|Should|May|must NOT|should NOT|MUST not|SHOULD not)\b")
        in_fence = False
        for line_number, line in enumerate(
            path.read_text(encoding="utf-8").splitlines(), start=1
        ):
            if re.match(r"^\s*(```|~~~)", line):
                in_fence = not in_fence
                continue
            if in_fence or line.lstrip().startswith(">"):
                continue
            match = mixed_case.search(line)
            if match:
                self.error(
                    f"{self.relative(path)}:{line_number}: normative keyword has inconsistent casing: {match.group(0)}"
                )

    def check_normative_keywords(self) -> None:
        if not self.lint_normative:
            return
        for path in (file for file in distribution_files(ROOT) if file.suffix == ".md"):
            self.check_normative_file(path)

    def run(self) -> int:
        self.check_versions()
        self.parse_machine_readable_files()
        self.check_schemas()
        self.validate_known_instances()
        principle_count = self.check_metadata_and_references()
        self.check_versions()
        self.check_generated_outputs()
        self.check_manifest()
        self.check_markdown_links()
        self.check_normative_keywords()
        if self.errors:
            print(f"Validation failed with {len(self.errors)} error(s):")
            for error in sorted(set(self.errors)):
                print(f"- {error}")
            return 1
        lint_note = " with normative-keyword linting" if self.lint_normative else ""
        print(
            f"Validation passed{lint_note}: {principle_count} canonical entries; schemas, "
            "metadata, references, dependency graphs, examples, generated outputs, manifest, "
            "and Markdown links are consistent."
        )
        return 0


def parse_args():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--lint-normative",
        action="store_true",
        help="also reject inconsistently cased RFC 2119-style normative keywords",
    )
    return parser.parse_args()


if __name__ == "__main__":
    arguments = parse_args()
    sys.exit(RepositoryValidator(lint_normative=arguments.lint_normative).run())
