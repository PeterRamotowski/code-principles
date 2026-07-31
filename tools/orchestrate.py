#!/usr/bin/env python3
"""Resolve repository evidence and overrides into an engineering policy."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from orchestrator.resolver import OrchestrationError, load_context, resolve_policy  # noqa: E402


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repository", type=Path, default=Path.cwd(), help="repository to inspect")
    parser.add_argument("--task", default="", help="current task statement used as explicit evidence")
    parser.add_argument(
        "--context",
        type=Path,
        help="repository engineering context (defaults to engineering-context.yaml when present)",
    )
    parser.add_argument("--user-context", type=Path, help="higher-precedence partial user context")
    parser.add_argument("--profile", help="explicit user base-profile override")
    parser.add_argument("--modifier", action="append", default=[], help="explicit user modifier; repeatable")
    parser.add_argument(
        "--skill-mode",
        action="append",
        default=[],
        metavar="SKILL=MODE",
        help="explicit user skill-mode override; repeatable",
    )
    parser.add_argument("--format", choices=("yaml", "json", "summary"), default="yaml")
    parser.add_argument("--output", type=Path, help="write output to a file instead of stdout")
    return parser.parse_args()


def _cli_user_context(arguments: argparse.Namespace) -> dict:
    context = load_context(arguments.user_context)
    if arguments.profile or arguments.modifier:
        profiles = context.setdefault("profiles", {})
        if arguments.profile:
            profiles["base"] = arguments.profile
        if arguments.modifier:
            profiles["modifiers"] = arguments.modifier
    if arguments.skill_mode:
        modes = context.setdefault("overrides", {}).setdefault("skill_modes", {})
        for value in arguments.skill_mode:
            skill, separator, mode = value.partition("=")
            if not separator or not skill or not mode:
                raise OrchestrationError(f"invalid --skill-mode {value!r}; expected SKILL=MODE")
            modes[skill] = mode
    return context


def main() -> int:
    arguments = parse_args()
    repository = arguments.repository.resolve()
    context_path = arguments.context
    if context_path is None and (repository / "engineering-context.yaml").is_file():
        context_path = repository / "engineering-context.yaml"
    try:
        policy = resolve_policy(
            repository,
            task=arguments.task,
            repository_context=load_context(context_path),
            user_context=_cli_user_context(arguments),
        )
    except OrchestrationError as exc:
        print(f"Orchestration failed: {exc}", file=sys.stderr)
        return 1

    if arguments.format == "json":
        rendered = json.dumps(policy, indent=2, ensure_ascii=False) + "\n"
    elif arguments.format == "summary":
        rendered = "\n".join(f"- {item}" for item in policy["visible_summary"]["items"]) + "\n"
    else:
        rendered = yaml.safe_dump(policy, sort_keys=False, allow_unicode=True)
    if arguments.output:
        arguments.output.write_text(rendered, encoding="utf-8")
    else:
        print(rendered, end="")
    return 0


if __name__ == "__main__":
    sys.exit(main())
