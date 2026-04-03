# Source Policy

## Source Priority

Use this order when possible:

1. Official announcements, filings, transcripts, and agency statements
2. Primary reporting from reputable outlets
3. Follow-up explainers for context
4. Aggregators only for discovery, not as the main cited source

## Feed Transport Rules

- Treat `toprss.ifeed.cc` as a discovery index, not as the editorial source of truth.
- If a feed arrives through `plink.anyfeeder.com`, `rsshub.app`, or another mirror, cite the original publisher in the article rather than the transport layer.
- Prefer original feeds when they are stable and complete; use mirrors as intake fallback, not attribution fallback.
- If a mirror strips timing, context, or source detail from a high-stakes story, go back to the publisher page or drop the item.
- Do not treat search-result pages, redirect pages, or other non-canonical URLs as article sources.
- Treat query-based Google News RSS as discovery-only unless you separately verify the publisher page; do not cite the Google wrapper as if it were Reuters or another newsroom.

## Selection Rules

- Use mixed Chinese and English sources when that improves coverage.
- Prefer high-signal stories with clear public, policy, market, platform, or business impact.
- Merge duplicate angles into one item instead of repeating the same story.
- Skip low-value virality unless it reflects a larger shift worth explaining.
- Default to China-reader relevance when two stories look equally large on paper.
- Use ranking, digest, and hot-list feeds only to discover or prioritize candidates; they do not satisfy sourcing requirements by themselves.
- Use Chinese-language bridge feeds to improve transmission and framing, but do not let them replace stronger primary reporting on high-stakes international stories.
- For high-stakes cross-border `Top 3` items, prefer at least one primary or official source plus one corroborating report or follow-up source when available.
- Prefer sources that provide a usable publish timestamp; drop items that cannot be reliably placed inside the coverage window.

## Selection Rubric

Score each candidate story before drafting. Use a `0-2` score for each dimension.

### Positive dimensions

- `importance`: Does it affect policy, markets, major platforms, or public life?
- `china-reader relevance`: Will a Chinese WeChat reader feel this matters this morning?
- `freshness`: Did it materially happen or materially advance in the target window?
- `public-interest value`: Does it help explain the shared agenda of the day rather than just a niche corner?
- `explanatory value`: Does it help explain a larger shift, not just a one-off event?
- `section fit`: Does it strengthen one of the default sections?

### Negative dimensions

- `duplication penalty`: Is it just another angle on a story already selected?
- `noise penalty`: Is it mostly virality, outrage bait, or low-consequence chatter?

### Decision rule

- Strong keep: total score `8+` with no major sourcing problem
- Borderline: total score `6-7`; keep only if the news day is light or the item adds needed variety
- Drop: total score `5 or below`, or any item with unresolved credibility issues

Prefer `8-12` total stories for a normal full report, including the top 3. On slow days, go lower.

## Wind-Vane Rules

- Build `经济投资风向标` from macro, policy, rates, currency, commodity, sector-temperature, or risk-appetite signals.
- Prefer developments that change the direction of travel, not just routine price noise.
- Keep each signal short: what changed, what it suggests, and why a reader should care.
- Do not turn the section into explicit buy/sell advice or a list of stock picks.
- If the day has only one clean signal, keep the section to one strong point rather than padding it.

## Uncertainty Rules

- Mark fast-moving stories as `developing` when facts are still changing.
- Separate confirmed facts from claims, estimates, allegations, and predictions.
- If the available sourcing is weak or single-source, either qualify it clearly or drop the item.
- If the item only survives through an empty summary, missing timestamp, or search-result link, treat it as weak sourcing and drop it.

## Attribution Rules

- Every story must include a source name and publish date.
- If multiple sources are used, cite the dominant reporting source and cross-check silently unless cross-checking changes the interpretation.
- Do not imply firsthand certainty when the article is based on reported information.
- Do not cite `AnyFeeder`, `RSSHub`, `TopRSS`, or another feed wrapper as if it were the newsroom or publisher.
- If a cross-check materially changes confidence or interpretation, surface that uncertainty in the copy instead of hiding it.

## Day Boundary Rules

- Default to the current `Asia/Shanghai` calendar day.
- If a major story started earlier but materially changed today, include it and note that it is a carry-over.

## Column Continuity Rules

- For the standing issue of `《环球日报》`, treat `08:00 Asia/Shanghai` as the publication cutoff.
- Prefer the latest reliable information available by the cutoff rather than waiting for perfect completeness.
- Avoid using the same lead story on consecutive days unless there is a clear overnight development.
- If a story continues across multiple days, change the angle to reflect what is newly important.
- Avoid repeating the same `经济投资风向标` conclusion on consecutive days unless the signal truly persisted and materially strengthened.
