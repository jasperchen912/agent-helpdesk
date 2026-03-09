---
name: daily-news
description: Create polished, personalized Chinese daily news reports for a recurring WeChat column by curating major headlines, grouping them into sections, and adding brief editorial insight, source attribution, and image suggestions. Use when Codex needs to prepare a daily news article, especially a recurring 8:00 AM morning column, plus morning briefings, hot-topic roundups, or topic-focused news reports for zh-CN readers with AI, technology, and business emphasis.
metadata:
  {
    "openclaw":
      {
        "emoji": "📰",
      },
  }
---

# Daily News

## Default Resources

- Read `references/morning-column-profile.yaml` first when the user wants the standing daily WeChat column.
- Read `references/morning-column-template.md` first when the user asks for the default daily article.
- Read `references/default-profile.yaml` first for the standing audience profile.
- Read `references/wechat-daily-template.md` for the standard flagship daily report.
- Read `references/fast-brief-template.md` for a shorter briefing-style output.
- Read `references/evening-recap-template.md` for an end-of-day recap with a tomorrow watchlist.
- Read `references/weekend-longread-template.md` for a slower, more synthesized weekly-style piece.
- Read `references/topic-focus-template.md` for a single-theme or single-sector report.
- Read `references/business-focus-profile.yaml` when the user wants a business-first or markets-and-companies angle.
- Read `references/feed-sources.md` when you need the standing source mix for the morning column.
- Read `references/prompt-examples.md` when you need to map a user request to the right morning-column behavior.
- Read `references/anti-patterns.md` before finalizing the draft when quality feels off.
- Read `references/tool-boundary.md` when deciding whether a request belongs to the skill or to the automation toolchain.
- Read `references/source-policy.md` when selecting, merging, or qualifying stories.
- Read `references/golden-sample.md` before final polishing when the user wants the default flagship daily report.

## Default Workflow

1. If the user asks for the daily column, assume the default `8:00 AM Asia/Shanghai morning column`.
2. Confirm which output variant the user wants: morning column, standard daily report, fast brief, evening recap, weekend longread, or topic focus.
3. Confirm whether a theme preset is needed. If the user asks for business-first coverage, load `references/business-focus-profile.yaml`.
4. If the user request is brief or ambiguous, read `references/prompt-examples.md` and match the closest intent.
5. Load the matching standing profile:
   - morning column: `references/morning-column-profile.yaml`
   - generic daily report: `references/default-profile.yaml`
6. Use the profile defaults unless the user explicitly overrides audience, tone, date, or coverage mix.
7. For the morning column, treat the article as an `08:00 Asia/Shanghai` publication and use the most recent reliable information available by that cutoff.
8. Gather high-signal stories from mixed Chinese and English sources. Prefer primary reporting and official announcements.
9. Weight candidate sources using `references/feed-sources.md` before deciding what can lead the article and what should stay as section support.
10. Score candidate stories with the selection rubric in `references/source-policy.md`.
11. De-duplicate overlapping coverage and cluster related updates into a single item.
12. Rank by reader value, not by raw virality. Keep public-interest headlines plus clear AI, technology, and business emphasis unless a theme preset changes that balance.
13. Pick the matching template:
   - morning column: `references/morning-column-template.md`
   - standard report: `references/wechat-daily-template.md`
   - fast brief: `references/fast-brief-template.md`
   - evening recap: `references/evening-recap-template.md`
   - weekend longread: `references/weekend-longread-template.md`
   - topic focus: `references/topic-focus-template.md`
14. Draft the article in Chinese with one brief "why it matters" line per item unless the selected template says otherwise.
15. Use `references/golden-sample.md` to match the intended pacing, headline density, and closing rhythm for the morning column and standard report.
16. Read `references/anti-patterns.md` and remove any signs of filler, source imbalance, or template drift.
17. Add source names and publish dates to every item. Mark unresolved stories as developing.
18. Finish with image suggestions, not actual image retrieval, unless the user explicitly asks for images.

## Output Variants

- `morning column`: Default. Use for the recurring daily WeChat article published at `08:00` China time with a fixed title pattern and consistent section rhythm.
- `standard daily report`: Use for a polished mid-length WeChat article with a lead, top 3, grouped sections, and a closing synthesis when the user wants a broader non-column version.
- `fast brief`: Use when the user wants a quicker scan, a shorter morning digest, or fewer paragraphs. Keep it tight and front-loaded.
- `evening recap`: Use when the user wants an end-of-day read with "what changed today" and "what to watch tomorrow".
- `weekend longread`: Use when the user wants a slower, more synthesized piece that compresses several days into a few larger threads.
- `topic focus`: Use when the user asks for one theme, one industry, one company cluster, or one policy line. Keep the narrative centered on that theme instead of balancing all categories.

## Theme Presets

- `business focus`: Use the topic-focus structure or the standard structure with a business-first story order. Prioritize markets, major company actions, earnings-relevant developments, trade, policy, and industry structure over general-interest headlines.

## Output Rules

- Output Simplified Chinese article copy by default.
- Produce a WeChat-ready article, not a raw bullet dump.
- Offer 3 title options unless the user asks for one or specifies a fixed title.
- For each story include: headline, factual summary, why it matters, source/date, unless the selected template explicitly compresses the format.
- Reduce item count on slow news days instead of padding.
- When the user specifies a fixed title pattern, obey it exactly.
- Preserve the selected variant instead of blending structures.
- When a preset is selected, preserve that editorial weight through headline order, section choice, and commentary emphasis.
- For the morning column, default to the exact title pattern `《X月X日最该看的几件大事》`.
- For the morning column, keep continuity across days: avoid leading with the same story two days in a row unless there is a meaningful new development.

## Editorial Standard

- Prefer confirmed facts over opinion.
- Keep commentary brief, restrained, and useful.
- Explicitly separate confirmed facts, claims, estimates, and open questions.
- Do not repeat the same story in multiple sections.
- Skip low-signal celebrity or internet topics unless they have clear business, policy, platform, or cultural impact.
- Avoid exaggerated headlines or clickbait phrasing.
- Keep paragraph rhythm close to the golden sample: one strong lead, compact body blocks, and a concise closing line.

## Failure Modes

- If no reliable sourcing is available, say so and omit the item.
- If a breaking story is moving fast, label it as developing and state what is confirmed.
- If source dates fall outside the requested window, note the carry-over clearly.
