---
name: write-wechat-short-fiction
description: Create, revise, and quality-check publish-ready Markdown drafts for a recurring WeChat short-fiction series in Simplified Chinese. Use when Codex needs to turn a story seed, overheard line, image, character sketch, urban scene, dream fragment, or lightly fictionalized real-life premise into a finished short story; continue or vary a standing fiction series; polish an existing draft into the series voice; generate compliant titles and frontmatter; or run editorial QA before handoff to publishing.
---

# Write WeChat Short Fiction

## Default Resources

- Read `references/series-profile.yaml` first for the standing defaults.
- Read `references/series-bible.md` before drafting or revising so the series promise stays stable.
- Read `references/default-template.md` for the standard issue shape.
- Read `references/structure-variants.md` when the pacing or narrative engine needs to change.
- Read `references/serialization-playbook.md` when the premise benefits from a multi-day arc or when the user asks for a serial.
- Read `references/prompt-examples.md` when the user request is brief and you need to map it to the right job.
- Read `references/topic-selection.md` when no premise is provided.
- Read `references/continuity-playbook.md` before self-selecting a premise for an ongoing series.
- Read `references/title-playbook.md` when naming or renaming the story.
- Read `references/risk-policy.md` before using real people, public events, minors, violence, illness, or workplace details.
- Read `references/anti-patterns.md` before final polish whenever the draft starts sounding generic or essay-like.
- Read `references/editorial-checklist.md` before finalizing any publish-ready draft.
- Read `references/tool-boundary.md` when deciding whether the request belongs here or should hand off to `wechat-publisher`.

## Supported Jobs

- Draft one full issue from a premise, image, object, fragment, or character seed.
- Self-select a fresh story premise when the user gives no seed.
- Rewrite a rough, over-explained, or low-tension draft into the series voice.
- Expand a thin idea into a complete short story or compress an overgrown draft into phone-friendly fiction.
- Split a broad premise into a multi-day serial or continue the next installment of an existing arc when that structure improves suspense.
- Generate one chosen title or a small set of title options when the user asks for title work.
- Review an existing Markdown draft and return editorial findings before publishing.

## Default Workflow

1. Treat the request as the next issue of a recurring WeChat short-fiction series unless the user changes the format or date.
2. Determine the job type first: new draft, rewrite, expand, compress, serial split, serial continuation, title work, or QA-only review.
3. Load `references/series-profile.yaml` and `references/series-bible.md` before making editorial decisions.
4. If the request is brief or ambiguous, read `references/prompt-examples.md` and match the closest job.
5. If drafting from scratch and no premise is supplied, read `references/topic-selection.md` and `references/continuity-playbook.md`, then choose a premise that feels fresh against recent issues when that history is available.
6. Decide whether the premise is best as `standard issue`, `extended issue`, or `serial episode`. Use serial mode when the story benefits from multiple publish beats, not merely because it runs past a target length.
7. Pick the default structure from `references/default-template.md`. Switch to `references/structure-variants.md` only when the premise clearly benefits from another engine or the user asks for a different pacing.
8. Build the title with `references/title-playbook.md`. Use the default archive format unless the user supplies a fixed title or series name.
9. Draft or revise one complete WeChat-ready Markdown story with frontmatter, not an outline, notes, or commentary, unless the user explicitly asks for those.
10. Fill frontmatter with:
   - `title`: `《短篇小说｜YYYY.MM.DD｜篇名》` by default
   - `cover`: `./assets/default-cover.jpg` by default
11. Keep the body in Simplified Chinese. Default to `1000-1800` Chinese characters, with `700-1000` for flash fiction, `1800-2800` for an extended issue when the tension supports it, and usually `1000-1800` for each serial episode.
12. Open on a concrete scene within the first `120` Chinese characters. Establish at least one unstable element early: a desire, pressure, omission, mismatch, or small impending consequence.
13. Keep the cast focused. Default to `1-3` consequential characters and one stable point of view per issue.
14. Let the story move through behavior, objects, and decisions. Keep explanation lighter than scene.
15. In `serial episode` mode, resolve one local movement per installment and leave the next pressure visible without turning the episode into a cliffhanger-only fragment.
16. Land on a reveal, reversal, suspended choice, or lingering image. Do not end with a moral or abstract summary.
17. If the article will be saved outside the skill folder, either copy `assets/default-cover.jpg` next to the Markdown file under `./assets/` or replace `cover` with another valid image path.
18. Run the draft against `references/risk-policy.md`, `references/anti-patterns.md`, and `references/editorial-checklist.md`.
19. If the draft exists as a file, run `python3 scripts/lint_story.py path/to/story.md` from the skill directory. Add `--variant flash`, `--variant extended`, or `--variant serial` when the story intentionally uses a non-default shape, then fix any failures before handoff.
20. Hand off to `wechat-publisher` only when the user asks to publish or push the story into the WeChat draft flow.

## Output Variants

- `standard issue`: Default. Use the core series voice and the normal `1000-1800` character range.
- `flash fiction`: Use when the user asks for a tighter story or when the premise is too thin for a longer treatment. Keep `700-1000` Chinese characters and reduce side movement, not tension.
- `extended issue`: Use when one post should carry more scene, pressure, or consequence and the story still reads cleanly as a single sitting. Usually `1800-2800` Chinese characters.
- `serial episode`: Use when the premise benefits from multiple publish beats or when the user explicitly wants a multi-day serial. Usually keep each episode within `1000-1800` Chinese characters.
- `title work`: Use only when the user asks for title help. Return the requested count of title options plus the recommended pick.
- `QA review`: Use when the user asks to review an existing Markdown draft. Return findings first, then concise fix suggestions.

## Output Rules

- Output exactly one finished Markdown story by default.
- Preserve a contemporary, human-scale, phone-readable fiction voice.
- Keep paragraphs short enough for mobile reading. Prefer `1-3` sentences per paragraph.
- Keep one dominant plot engine. Side details should sharpen the same pressure, not start a second story.
- Use dialogue sparingly and purposefully. Do not let characters explain the theme to each other.
- Let subtext carry part of the meaning. Do not unpack every symbol, motive, or coincidence.
- Keep speculative or uncanny elements lightly handled unless the user explicitly asks for genre-forward fiction.
- If using serial mode, output one publishable episode by default unless the user explicitly asks for multiple installments in one turn.
- Do not add section headings, editorial notes, prompt explanations, or publishing instructions inside the story.
- If the user asks for alternatives, keep them few and editorially defensible rather than brainstormy.

## Failure Modes

- If the premise only supports a fragment, switch to `flash fiction` instead of padding with reflection.
- If the story runs long, decide whether the extra length is earning more tension. If not, cut or split into serial instead of letting it sprawl.
- If the draft reads like an essay wearing fiction clothing, restore scene, pressure, and decision before polishing sentences.
- If the ending depends on hiding basic information unfairly, add setup earlier and make the turn feel earned.
- If the story becomes generic because too many characters or settings compete for attention, cut back to one core movement.
- If a real-world tie-in relies on uncertain facts or identifiable private people, fictionalize it further or drop the tie-in entirely.
