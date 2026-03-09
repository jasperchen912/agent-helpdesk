# Memory Contract

Use this file when the host environment provides the paired OpenClaw memory file for `《浴室沉思》`.

## Role

Treat the paired memory file as the primary continuity source for the series. Read it before drafting or revising. Write back to it after producing a publishable issue.

## Read Order

1. Read the most recent `7-14` issue records first.
2. Extract these fields from each record when present:
   - `date`
   - `title`
   - `scene_family`
   - `anchor_object`
   - `social_pattern`
   - `ending_mode`
   - `keywords`
3. Use those fields to avoid repetition before selecting a topic, title, or ending move.

## Write-Back Rule

Append or update one record only after the draft is publishable or after a publish-ready revision is complete. Do not write back brainstorming attempts, rejected titles, or QA-only notes.

## Required Record Fields

- `date`: publication date in `YYYY-MM-DD`
- `title`: final issue title
- `scene_family`: one normalized value from the continuity playbook
- `anchor_object`: one concrete object
- `social_pattern`: one short phrase describing the human relation or pressure
- `ending_mode`: one normalized value from the continuity playbook
- `keywords`: `3-6` short tags

## Preferred Markdown Shape

Use append-only issue blocks when the memory file is Markdown:

```markdown
## 2026-03-10
- title: 《浴室沉思｜2026.03.10｜钥匙落在桌上的声音》
- scene_family: home interior
- anchor_object: keys
- social_pattern: returning home alone after shared public fatigue
- ending_mode: object left behind
- keywords: keys, home, return, fatigue, night
```

## If the Memory File Is Structured

If the host exposes JSON, YAML, or another structured memory format, keep the same field names and semantics instead of forcing Markdown.

## If Memory Is Missing

- Fall back to scanning recent local drafts.
- Assume the most recent issue may already have used a mirror, steam, bathroom, elevator, or queue motif.
- Prefer a scene family and ending mode different from the last obvious pattern.

## Quality Rule

If the draft repeats the same `scene_family` and `anchor_object` as the most recent published issue, treat that as a quality problem unless the user explicitly asked for a deliberate echo.
