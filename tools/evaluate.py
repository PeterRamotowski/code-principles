#!/usr/bin/env python3
"""Execute whole-system evaluation scenarios against the policy resolver."""

from __future__ import annotations

import argparse
import json
import sys
import tempfile
from pathlib import Path
from typing import Any

import yaml

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from orchestrator.resolver import OrchestrationError, resolve_policy  # noqa: E402


class EvaluationError(ValueError):
    """Raised when an executable scenario is malformed."""


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--scenario",
        action="append",
        default=[],
        help="scenario id to run; repeatable (default: all executable scenarios)",
    )
    parser.add_argument("--format", choices=("text", "json"), default="text")
    return parser.parse_args()


def _load(path: Path) -> dict[str, Any]:
    try:
        data = yaml.safe_load(path.read_text(encoding="utf-8"))
    except (OSError, yaml.YAMLError) as exc:
        raise EvaluationError(f"cannot load {path}: {exc}") from exc
    if not isinstance(data, dict):
        raise EvaluationError(f"{path} must contain a mapping")
    return data


def _write_repository(root: Path, signals: dict[str, Any]) -> None:
    for relative, content in signals.items():
        if not isinstance(relative, str) or not isinstance(content, str):
            raise EvaluationError("repository_signals must map relative paths to string content")
        target = (root / relative).resolve()
        if not target.is_relative_to(root):
            raise EvaluationError(f"repository signal escapes its temporary root: {relative}")
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(content, encoding="utf-8")


def _compare_subset(actual: Any, expected: Any, path: str, failures: list[str]) -> None:
    if isinstance(expected, dict):
        if not isinstance(actual, dict):
            failures.append(f"{path}: expected mapping, got {actual!r}")
            return
        for key, value in expected.items():
            if key not in actual:
                failures.append(f"{path}.{key}: missing")
            else:
                _compare_subset(actual[key], value, f"{path}.{key}", failures)
        return
    if actual != expected:
        failures.append(f"{path}: expected {expected!r}, got {actual!r}")


def _ids(items: list[dict[str, Any]]) -> list[str]:
    return [item["id"] for item in items]


def evaluate(scenario: dict[str, Any]) -> tuple[dict[str, Any] | None, list[str]]:
    scenario_id = scenario.get("id", "<unknown>")
    inputs = scenario.get("input", {})
    signals = inputs.get("repository_signals")
    request = inputs.get("request")
    if not isinstance(signals, dict) or not isinstance(request, str):
        raise EvaluationError(
            f"{scenario_id}: executable scenarios require input.request and input.repository_signals"
        )

    try:
        with tempfile.TemporaryDirectory(prefix="code-principles-eval-") as directory:
            repository = Path(directory).resolve()
            _write_repository(repository, signals)
            policy = resolve_policy(
                repository,
                task=request,
                repository_context=inputs.get("repository_context", {}),
                user_context=inputs.get("user_context", {}),
            )
    except (EvaluationError, OrchestrationError) as exc:
        return None, [str(exc)]

    expected = scenario.get("expected", {})
    failures: list[str] = []
    scalar_fields = {"profile": "base_profile"}
    for expected_name, policy_name in scalar_fields.items():
        if expected_name in expected:
            _compare_subset(
                policy[policy_name], expected[expected_name], f"expected.{expected_name}", failures
            )
    if "context" in expected:
        _compare_subset(policy["context"], expected["context"], "expected.context", failures)
    if "modifiers" in expected:
        _compare_subset(policy["modifiers"], expected["modifiers"], "expected.modifiers", failures)

    adapter_fields = {
        "language_adapters": "language_adapters",
        "framework_adapters": "framework_adapters",
    }
    for expected_name, policy_name in adapter_fields.items():
        if expected_name in expected:
            _compare_subset(
                _ids(policy[policy_name]),
                expected[expected_name],
                f"expected.{expected_name}",
                failures,
            )

    if "significant_decisions" in expected:
        actual = set(_ids(policy["significant_decisions"]))
        for identifier in expected["significant_decisions"]:
            if identifier not in actual:
                failures.append(f"expected.significant_decisions: missing {identifier!r}")

    if "skill_modes" in expected:
        actual_modes = {item["id"]: item["mode"] for item in policy["active_core_skills"]}
        _compare_subset(actual_modes, expected["skill_modes"], "expected.skill_modes", failures)

    if "conflicts" in expected:
        actual_conflicts = {item["id"]: item["decision"] for item in policy["conflicts"]}
        _compare_subset(actual_conflicts, expected["conflicts"], "expected.conflicts", failures)

    actual_prohibitions = set(policy["prohibited_decisions"])
    for decision in scenario.get("forbidden", []):
        if decision not in actual_prohibitions:
            failures.append(f"forbidden: resolver did not prohibit {decision!r}")
    return policy, failures


def main() -> int:
    arguments = parse_args()
    selected = set(arguments.scenario)
    documents = [_load(path) for path in sorted((ROOT / "evaluations/scenarios").glob("*.yaml"))]
    executable = [
        item
        for item in documents
        if isinstance(item.get("input"), dict)
        and "request" in item["input"]
        and (not selected or item.get("id") in selected)
    ]
    known = {item.get("id") for item in documents}
    missing = selected - known
    if missing:
        print(f"Unknown scenario ids: {', '.join(sorted(missing))}", file=sys.stderr)
        return 2
    if not executable:
        print("No executable evaluation scenarios selected.", file=sys.stderr)
        return 2

    results = []
    for scenario in executable:
        _, failures = evaluate(scenario)
        results.append({"id": scenario["id"], "passed": not failures, "failures": failures})

    if arguments.format == "json":
        print(json.dumps({"scenarios": results}, indent=2, ensure_ascii=False))
    else:
        for result in results:
            status = "PASS" if result["passed"] else "FAIL"
            print(f"{status} {result['id']}")
            for failure in result["failures"]:
                print(f"  - {failure}")
        passed = sum(result["passed"] for result in results)
        print(f"{passed}/{len(results)} executable evaluation scenarios passed")
    return 0 if all(result["passed"] for result in results) else 1


if __name__ == "__main__":
    sys.exit(main())
