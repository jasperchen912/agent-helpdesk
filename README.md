# agent-helpdesk

This repository is a workspace for building reusable agent skills and local helper tools.

## Layout

- `skills/`: one folder per skill
- `scripts/new-skill`: initialize a new skill under `skills/`
- `scripts/validate-skills`: validate all skills in `skills/`
- `tools/`: non-skill helper scripts/tools for this repo

Each skill should contain:

- required: `SKILL.md`
- optional: `agents/`, `scripts/`, `references/`, `assets/`

## Quick Start

Create a new skill:

```bash
./scripts/new-skill my-skill --resources scripts,references
```

Validate all skills:

```bash
./scripts/validate-skills
```

## Conventions

- Use lowercase hyphenated skill names (for example: `daily-news`).
- Keep trigger rules in `SKILL.md` frontmatter `description`.
- Keep skill folders minimal and focused on execution (avoid extra docs inside skills).
