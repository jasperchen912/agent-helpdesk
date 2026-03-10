# Editorial Checklist

Use this file before finalizing any draft.

## Frontmatter

- Title follows the archive pattern unless the user supplied a fixed override.
- Cover points to a valid path or URL.
- The title focus is concrete rather than abstract.

## Opening

- The first `120` Chinese characters contain a place, an object, and an unstable element.
- The story opens with scene rather than explanation.
- The protagonist's pressure is readable even if not fully explained.

## Body

- One dominant plot engine carries the story.
- Exposition stays lighter than scene.
- If the piece runs long, each extra paragraph still adds pressure, scene, or revelation instead of recap.
- The cast remains within `1-3` consequential characters unless the premise truly requires more.
- At least one detail feels specific enough that it could not fit any generic urban short story unchanged.

## Ending

- The last paragraph stays local.
- The ending lands on residue, cost, reveal, or suspended action.
- The ending does not resolve into advice, doctrine, or a slogan.
- If this is a serial episode, one local movement is complete and tomorrow's pressure is visible.

## Line Edit Flags

Cut or justify these phrases:

- `命运跟他开了个玩笑`
- `那一刻时间仿佛静止`
- `她突然明白`
- `原来每个人都有自己的苦衷`
- `这就是生活`
- `某种意义上`

## Final QA

- Keep paragraph count within `4-12`, with `5-9` preferred.
- If a local Markdown file exists, run `python3 scripts/lint_story.py path/to/story.md`.
- Add `--variant flash`, `--variant extended`, or `--variant serial` when the story intentionally uses a non-default shape.
- Fix every failure from the lint script. Review every warning before publishing.
