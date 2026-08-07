"""Define the files that belong in a Code Principles distribution."""
from pathlib import Path


ROOT_FILES = {
    ".gitignore",
    "ARCHITECTURE.md",
    "CHANGELOG.md",
    "CONFLICT-RESOLUTION.md",
    "CONTRIBUTING.md",
    "DOCUMENTATION.md",
    "KNOWLEDGE-MODEL.md",
    "LICENSE",
    "Makefile",
    "README.md",
    "ROADMAP.md",
    "SELF-CONTAINMENT.md",
    "SPECIFICATION.md",
    "TERMINOLOGY.md",
    "VERSION",
    "engineering-context.example.yaml",
    "requirements-dev.txt",
}

DISTRIBUTION_DIRECTORIES = {
    "catalogs",
    "core",
    "evaluations",
    "frameworks",
    "languages",
    "modifiers",
    "orchestrator",
    "principles",
    "profiles",
    "schemas",
    "tools",
}

ALLOWED_SUFFIXES = {".json", ".md", ".py", ".yaml", ".yml"}


def distribution_files(root: Path) -> list[Path]:
    """Return a stable, allowlisted set of files relative to ``root``."""
    files = [root / name for name in ROOT_FILES if (root / name).is_file()]

    for directory in DISTRIBUTION_DIRECTORIES:
        base = root / directory
        if not base.is_dir():
            continue
        for path in base.rglob("*"):
            relative = path.relative_to(root)
            if (
                path.is_file()
                and path.suffix in ALLOWED_SUFFIXES
                and not any(part.startswith(".") or part == "__pycache__" for part in relative.parts)
            ):
                files.append(path)

    return sorted(set(files), key=lambda path: path.relative_to(root).as_posix())
