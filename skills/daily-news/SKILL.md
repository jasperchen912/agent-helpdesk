---
name: daily-news
description: Create the single standing Chinese daily news article for the WeChat column `《环球日报》`. Use when the host agent needs to prepare today's one fixed 08:00 Asia/Shanghai issue in Simplified Chinese with a stable title pattern, a light cutoff/read-time metadata line, one fast first-screen summary, one strong lead, a detailed Top 3, grouped sections, a fixed `经济投资风向标`, source attribution, and a same-day watchlist.
---

# Daily News

## Default Resources

- Read `references/global-daily-profile.yaml` first for the standing `《环球日报》` defaults.
- Read `references/global-daily-template.md` first for the fixed article structure.
- Read `references/feed-sources.md` when choosing or weighting candidate sources.
- Read `references/source-policy.md` when selecting, merging, qualifying, or carrying over stories.
- Read `references/top3-playbook.md` when drafting the `Top 3`.
- Read `references/investment-wind-vane.md` when building the fixed `经济投资风向标` section.
- Read `references/prompt-examples.md` when the user request is brief and you need to map it back to the standing column behavior.
- Read `references/golden-sample.md` and `references/global-daily-final-sample.md` before final polishing.
- Read `references/anti-patterns.md` before finalizing whenever the draft starts feeling generic, imbalanced, or thin.
- Read `references/tool-boundary.md` when deciding whether a change belongs in the editorial skill or the automation toolchain.

## Supported Job

- Produce exactly one publish-ready issue of `《环球日报》` for the target day.

## Default Workflow

1. Treat the request as today's issue of `《环球日报》` unless the user explicitly changes the date.
2. Load `references/global-daily-profile.yaml` and `references/global-daily-template.md` before making editorial decisions.
3. If the request is brief or ambiguous, read `references/prompt-examples.md` and map it back to the standing `《环球日报》` behavior instead of inventing a new format.
4. If tool execution is available and `tools/global-daily/generate_global_daily.py` exists, run `python3 tools/global-daily/generate_global_daily.py --print-manifest` through the host `exec` tool first. Use that bundle as drafting input and keep article generation in the current host model.
5. Treat the article as an `08:00 Asia/Shanghai` publication and use the most recent reliable information available by that cutoff.
6. Gather high-signal stories from mixed Chinese and English sources. Prefer official statements and primary reporting, then use follow-up reporting for context.
7. Weight candidate sources using `references/feed-sources.md` before deciding what can lead the article and what should stay as section support.
8. Score candidate stories with the selection rubric in `references/source-policy.md`.
9. De-duplicate overlapping coverage and cluster related updates into a single item. Do not let the same event chain occupy multiple `Top 3` slots unless the reader value is clearly different.
10. Rank by China-reader relevance and shared public value, not by raw virality.
11. Build one fixed article using the standing structure: title, light metadata line, `先看三句`, lead, `Top 3`, grouped sections, `经济投资风向标`, and `今天还要继续看什么`.
12. Use `references/top3-playbook.md` so each `Top 3` item names the concrete actors, facts, figures, timing, friction point, who gets hit first, and why the development matters now.
13. Use `references/investment-wind-vane.md` to keep `经济投资风向标` short, directional, labeled, and explanatory rather than tactical.
14. Draft the full article in Chinese with a fast first screen, one clear `为什么重要 / 对谁有影响` line per major item, and visibly tighter grouped sections than `Top 3`. The top of the piece should feel easy to enter for a broad reader, while the body should still read like restrained newsroom copy.
15. Use `references/golden-sample.md` and `references/global-daily-final-sample.md` to match the intended pacing, headline density, and closing rhythm of `《环球日报》`.
16. Read `references/anti-patterns.md` and remove filler, source imbalance, tech bias, shallow `Top 3`, or template drift.
17. Add source names and publish dates to every major item. Mark unresolved stories as developing.
18. Finish as one WeChat-ready article, not notes, outlines, or multiple variants.

## Output Rules

- Output Simplified Chinese article copy by default.
- Output exactly one finished issue of `《环球日报》`.
- Use the fixed title pattern `《环球日报》｜X月X日` unless the user explicitly supplies another exact title.
- Do not generate multiple title candidates unless the user explicitly asks for title work.
- Produce a WeChat-ready article, not a raw bullet dump.
- Keep the standing structure stable: light metadata line, `先看三句`, one lead, `Top 3`, grouped sections, `经济投资风向标`, and `今天还要继续看什么`.
- By default add a light metadata line under the title with the information cutoff; add an estimated read time when it improves mobile scanning.
- Open with a first-screen module that lets the reader grasp the day in about 10 seconds.
- For each story include: headline, factual summary, why it matters, source/date.
- Treat the `Top 3` as the most detailed blocks in the article. Each one should give enough concrete facts, figures, timing, and transmission for the reader to understand the story without immediate follow-up reading.
- For major `Top 3` items, prefer adding one more layer of value through `why now`, `transmission chain`, or `market / business mechanism` rather than adding extra lower-value stories elsewhere.
- Do not use two `Top 3` slots on the same event chain unless the angles are genuinely distinct in public value and downstream impact.
- Reduce item count on slow news days instead of padding.
- If the user asks for more macro, more global, more company, or more tech emphasis, adjust weighting inside the same `《环球日报》` structure instead of switching formats.
- Keep grouped-section items fast and mobile-readable; they should usually answer `发生了什么` and `影响谁 / 为什么看`, not replay a full `Top 3` block.
- Keep `经济投资风向标` as a distinct short section rather than scattering those signals across the whole article.
- Write the `经济投资风向标` as a direction-of-travel section, not as stock tips, trading calls, or investment advice.
- Keep `今天还要继续看什么` concrete: each point should name the actor, trigger, or consequence to watch, not just a vague topic.
- Keep continuity across days: avoid leading with the same story two days in a row unless there is a meaningful overnight development.
- Do not invoke a second LLM from inside the toolchain when the current host model can draft the article directly.

## Editorial Standard

- Prefer confirmed facts over opinion.
- Keep commentary brief, restrained, and useful.
- Explicitly separate confirmed facts, claims, estimates, and open questions.
- Do not repeat the same story in multiple sections.
- Skip low-signal celebrity or internet topics unless they have clear public, policy, platform, business, or cultural impact.
- Avoid exaggerated headlines or clickbait phrasing.
- Front-load hard facts before abstract synthesis whenever possible.
- Let the first screen and lead feel easy to enter, but let the body and wind-vane keep editor-like density.
- Keep paragraph rhythm close to the sample: one light metadata line, one fast first screen, one strong lead, compact but information-rich body blocks, a clear wind-vane section, and a concise closing watchlist.

## Failure Modes

- If no reliable sourcing is available, say so and omit the item.
- If a breaking story is moving fast, label it as developing and state what is confirmed.
- If source dates fall outside the requested window, note the carry-over clearly.
- If there is no meaningful macro, policy, or market signal for the `经济投资风向标`, keep the section minimal rather than padding it with weak takes.
- If the `Top 3` only repeats headlines and conclusions without key detail or transmission logic, expand them before adding lower-priority stories.
