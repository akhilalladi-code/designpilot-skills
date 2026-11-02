#!/usr/bin/env python3
"""Validate DesignPilot skill files using only the Python standard library."""

from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
SKILLS_DIR = ROOT / "skills"
REQUIRED_SECTIONS = ("## Objective", "## Workflow", "## Quality checklist", "## Output format", "## Guardrails")


def fail(message: str) -> None:
    print(f"ERROR: {message}")
    raise SystemExit(1)


def main() -> int:
    if not SKILLS_DIR.is_dir():
        fail("skills/ directory is missing")

    skill_files = sorted(SKILLS_DIR.glob("*/SKILL.md"))
    if not skill_files:
        fail("no skills/*/SKILL.md files found")

    names = set()
    errors = []

    for path in skill_files:
        text = path.read_text(encoding="utf-8")
        rel = path.relative_to(ROOT)
        if not text.startswith("---\n"):
            errors.append(f"{rel}: missing YAML frontmatter")
            continue

        parts = text.split("---", 2)
        if len(parts) < 3:
            errors.append(f"{rel}: frontmatter is not closed")
            continue

        frontmatter, body = parts[1], parts[2]
        name_match = re.search(r"^name:\s*([a-z0-9]+(?:-[a-z0-9]+)*)\s*$", frontmatter, re.M)
        desc_match = re.search(r"^description:\s*.+$", frontmatter, re.M)

        if not name_match:
            errors.append(f"{rel}: missing or invalid name")
        else:
            name = name_match.group(1)
            if name != path.parent.name:
                errors.append(f"{rel}: name '{name}' must match directory '{path.parent.name}'")
            if name in names:
                errors.append(f"{rel}: duplicate skill name '{name}'")
            names.add(name)

        if not desc_match:
            errors.append(f"{rel}: missing description")

        for section in REQUIRED_SECTIONS:
            if section not in body:
                errors.append(f"{rel}: missing section '{section}'")

        if len(body.strip()) < 300:
            errors.append(f"{rel}: content is unexpectedly short")

    readme = ROOT / "README.md"
    if readme.exists():
        readme_text = readme.read_text(encoding="utf-8")
        for path in skill_files:
            relative_link = f"({path.as_posix()})"
            if relative_link not in readme_text:
                errors.append(f"README.md: missing link to {path.relative_to(ROOT)}")

    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1

    print(f"Validated {len(skill_files)} skills successfully.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
