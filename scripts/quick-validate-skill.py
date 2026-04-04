#!/usr/bin/env python3
"""
Lightweight validator for a skill folder.
No third-party dependencies.
"""

import re
import sys
from pathlib import Path

MAX_SKILL_NAME_LENGTH = 64
ALLOWED_PROPERTIES = {"name", "description", "license", "allowed-tools", "metadata"}


def parse_frontmatter(content: str) -> tuple[dict[str, str], str | None]:
    match = re.match(r"^---\n(.*?)\n---", content, re.DOTALL)
    if not match:
        return {}, "Invalid or missing YAML frontmatter"

    frontmatter_text = match.group(1)
    data: dict[str, str] = {}

    for raw_line in frontmatter_text.splitlines():
        line = raw_line.strip()
        if not line or line.startswith("#"):
            continue
        if raw_line.startswith((" ", "\t")):
            # Skip nested mappings/lists under allowed top-level keys.
            continue
        if ":" not in line:
            continue
        key, value = line.split(":", 1)
        key = key.strip()
        value = value.strip()
        if key:
            data[key] = value.strip('"').strip("'")

    return data, None


def validate_skill(skill_path: Path) -> tuple[bool, str]:
    skill_md = skill_path / "SKILL.md"
    if not skill_md.exists():
        return False, "SKILL.md not found"

    content = skill_md.read_text(encoding="utf-8")
    if not content.startswith("---"):
        return False, "No YAML frontmatter found"

    frontmatter, error = parse_frontmatter(content)
    if error:
        return False, error

    unexpected_keys = set(frontmatter.keys()) - ALLOWED_PROPERTIES
    if unexpected_keys:
        return (
            False,
            f"Unexpected key(s) in frontmatter: {', '.join(sorted(unexpected_keys))}",
        )

    name = frontmatter.get("name", "").strip()
    if not name:
        return False, "Missing 'name' in frontmatter"
    if not re.match(r"^[a-z0-9-]+$", name):
        return False, "Name must be hyphen-case (lowercase letters, digits, hyphens)"
    if name.startswith("-") or name.endswith("-") or "--" in name:
        return False, "Name cannot start/end with hyphen or contain consecutive hyphens"
    if len(name) > MAX_SKILL_NAME_LENGTH:
        return False, f"Name too long ({len(name)}), max is {MAX_SKILL_NAME_LENGTH}"

    description = frontmatter.get("description", "").strip()
    if not description:
        return False, "Missing 'description' in frontmatter"
    if "<" in description or ">" in description:
        return False, "Description cannot contain angle brackets"
    if len(description) > 1024:
        return False, f"Description too long ({len(description)}), max is 1024"

    return True, "Skill is valid!"


def main() -> int:
    if len(sys.argv) != 2:
        print("Usage: ./scripts/quick-validate-skill.py <skill_directory>")
        return 1

    skill_path = Path(sys.argv[1]).resolve()
    ok, message = validate_skill(skill_path)
    print(message)
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
