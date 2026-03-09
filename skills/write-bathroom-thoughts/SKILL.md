---
name: write-bathroom-thoughts
description: Create, revise, and quality-check publish-ready Markdown drafts for 《浴室沉思》, a recurring nightly around-20:00 WeChat essay series in Simplified Chinese. Use when Codex needs to turn a trigger word, small incident, image, daily-life slice, or lightly adapted current event into a finished article; polish an existing draft into the column voice; generate compliant titles and frontmatter; or run editorial QA before handoff to publishing.
---

# Write Bathroom Thoughts

## Default Resources

- Read `references/series-profile.yaml` first for the standing operational defaults.
- Read `references/series-bible.md` before writing or revising so the column promise stays stable across issues.
- Read `references/brand-audit.md` before writing when you need to remember what the series must not drift into.
- Read `references/default-template.md` for the standard nightly article.
- Read `references/structure-variants.md` when the pacing needs to change or the default structure feels repetitive.
- Read `references/prompt-examples.md` when the request is short and you need to map it to the right job.
- Read `references/topic-selection.md` when no topic is provided.
- Read `references/memory-contract.md` before drafting or revising when the paired OpenClaw memory file is available.
- Read `references/continuity-playbook.md` before self-selecting a topic or when trying to avoid repeating recent issues.
- Read `references/title-playbook.md` when building or revising the title focus.
- Read `references/risk-policy.md` before using public events, private people, grief, health, or workplace details.
- Read `references/banned-phrasings.md` before final polish whenever the draft starts sounding too much like a generic公众号观点文。
- Read `references/editorial-checklist.md` before finalizing any publish-ready draft.
- Read `references/anti-patterns.md` whenever the draft starts sounding generic, preachy, or over-written.
- Read `references/tool-boundary.md` when deciding whether the request belongs here or should hand off to `wechat-publisher`.
- Read `references/golden-sample.md` when the nightly voice needs calibration.
- Read `references/secondary-sample.md` when the draft needs a second approved scene family reference beyond the primary golden sample.

## Supported Jobs

- Draft tonight's full issue from a trigger word, small incident, image, or scene.
- Self-select a fresh topic when the user gives no seed.
- Rewrite a rough or over-written draft into the column voice.
- Shorten or expand an issue without breaking the series identity.
- Generate one chosen title or a small set of title options when the user asks for title work.
- Review a finished Markdown draft and return editorial findings before publishing.

## Default Workflow

1. Treat the request as tonight's `20:00 Asia/Shanghai` WeChat column unless the user changes the date.
2. Determine the job type first: new draft, rewrite, title work, or QA-only review.
3. Load `references/series-profile.yaml` and `references/series-bible.md` before making editorial decisions.
4. If the request is brief or ambiguous, read `references/prompt-examples.md` and match the closest job.
5. If drafting from scratch, use the user's trigger word, incident, image, or scene as the center of the piece whenever one is provided.
6. If the paired OpenClaw memory file is available, read the last `7-14` issue records before drafting or revising. Treat that memory as the continuity source of truth.
7. If no topic is provided, read `references/topic-selection.md` and `references/continuity-playbook.md`, then pick a fresh late-evening scene that does not feel adjacent to recent issues or memory records.
8. If no memory is available, fall back to scanning recent local drafts and apply the same continuity checks.
9. Use `references/default-template.md` for the standard nightly piece. Switch to `references/structure-variants.md` only when the default rhythm would make the series feel repetitive or when the user asks for a different pacing.
10. Read `references/risk-policy.md` before touching current events or any material that could expose private people, grief, health, or workplace specifics.
11. Build the title with `references/title-playbook.md`. Use the standing archive format unless the user supplies a fixed title.
12. Draft or revise one complete WeChat-ready Markdown article with frontmatter, not an outline, notes, title list, or commentary.
13. Fill frontmatter with:
   - `title`: `《浴室沉思｜YYYY.MM.DD｜题眼》` by default
   - `cover`: `./assets/default-cover.jpg` by default
14. Keep the body in Simplified Chinese, usually `700-1200` Chinese characters, with no section headings. Use the shorter or longer ranges in `references/series-profile.yaml` only when the user asks.
15. Preserve a restrained introspective voice. Stay specific, quiet, observant, and urban.
16. If the article will be saved outside the skill folder, either copy `assets/default-cover.jpg` next to the Markdown file under `./assets/` or replace `cover` with another valid image path.
17. Run the draft against `references/brand-audit.md`, `references/anti-patterns.md`, `references/banned-phrasings.md`, and `references/editorial-checklist.md`.
18. If the draft exists as a file, run `python3 scripts/lint_article.py path/to/article.md` from the skill directory. Add `--variant short` or `--variant long` when the article intentionally uses a non-default length target, then fix any failures before handoff.
19. If the paired OpenClaw memory file is writable and the article is publishable, append or update the issue record using `references/memory-contract.md` before handoff.
20. Hand off to `wechat-publisher` only when the user asks to publish or push the article into the WeChat draft flow.

## Output Variants

- `standard nightly issue`: Default. Use the core series voice and the normal `700-1200` character range.
- `short edition`: Use when the user asks for a tighter piece. Keep `450-700` Chinese characters and cut scene count, not depth.
- `long edition`: Use when the user explicitly wants a denser or more layered issue. Keep `1100-1500` Chinese characters and add one more turn of observation, not abstract explanation.
- `title work`: Use only when the user asks for title help. Return the requested count of title options plus the recommended pick.
- `QA review`: Use when the user asks to review an existing Markdown draft. Return findings first, then concise fix suggestions.

## Output Rules

- Output exactly one finished article by default.
- Preserve the series identity: urban, nocturnal, restrained, specific, and human-scaled.
- Keep the title in series format unless the user supplies a fixed title.
- Use one continuous short essay. Do not switch into bullet points, numbered lists, or newsletter sections inside the article body.
- Let the reflection emerge from the scene. Do not summarize the article's "lesson" in a didactic final paragraph.
- Keep imagery ordinary and grounded. Prefer bathrooms, mirrors, steam, tiles, corridor lights, elevators, queues, buses, convenience stores, stairwells, receipts, umbrellas, keys, and other urban everyday textures over abstract metaphors.
- Vary scene family, anchor object, sentence pace, and landing mode across issues when recent articles are available.
- Keep the title focus concrete. Prefer an object, action, pause, sound, or tiny social movement over abstract nouns.
- When adapting a current event, keep the event factual and minimal; the article should still read like 《浴室沉思》 rather than a news analysis or social commentary.
- Do not append meta text such as "以下是成稿", "可直接发布", "封面建议", or writing notes unless the user explicitly asks for them.
- If the user asks for alternatives, keep them few and editorially defensible rather than brainstormy.

## Failure Modes

- If no reliable facts are available for a current-event angle, drop the event tie-in and return to a purely observational piece.
- If the chosen topic only supports a one-paragraph thought, choose a stronger angle or shift to the short-edition format instead of padding with abstractions.
- If the draft becomes diary-like, pull it back toward shared urban experience without inventing facts.
- If the draft sounds like a sermon, cut the explanation and leave more space in the ending.
- If the draft sounds too much like a previous issue, change at least two of these: scene family, anchor object, narrator distance, sentence cadence, ending mode.
