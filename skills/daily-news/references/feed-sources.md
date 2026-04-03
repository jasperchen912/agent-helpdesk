# Feed Sources

Use this file to keep the standing source mix for `《环球日报》` aligned with its editorial goal.

## Discovery Principle

`toprss.ifeed.cc` is useful as a feed-discovery surface, not as a flat endorsement of source quality. Many entries are delivered through mirrors such as `plink.anyfeeder.com` or `rsshub.app`; treat those as transport layers and attribute the final article to the original publisher.

The concrete automation feed URLs belong in `tools/global-daily/config.example.json` and `tools/global-daily/generate_global_daily.py`. Keep that tool-level feed list aligned with the editorial roles below instead of copying raw URLs into the skill prompt.

Split the standing source set into six editorial roles:

### 1. Chinese public agenda and official signals

Use these to capture the shared domestic agenda first:

- 新华社 / 新华网
- 央视新闻 / 中国政府网
- 中国人民银行
- 国家统计局
- 财政部 / 海关总署 / 证监会 and other directly relevant agencies
- 人民日报 / 光明日报 / 半月谈 / 求是网 when official-public framing matters

These sources surface the domestic policy, economy, regulation, and public-interest signals that matter most to a Chinese morning reader.

### 2. Chinese-language broad news bridge

Use these to enrich overnight scanning and improve Chinese-language transmission without abandoning primary reporting:

- 《联合早报》-中港台-即时
- 《联合早报》-国际-即时
- 纽约时报中文网 国际纵览
- BBC 中文网
- 中国日报: 时政
- 腾讯新闻：国际
- iDaily 每日环球视野

These sources are useful when the final article is in Chinese and the editor needs a fast, broad, Chinese-language picture of what moved overnight. They are especially helpful for early framing, headline wording, and section assembly.

Default use:

- discover overnight developments quickly
- improve Chinese-language framing for international stories
- cross-check whether a story is traveling as a broad public agenda item

### 3. International macro and primary reporting

Use these to capture the overnight global agenda and cross-check fast-moving world stories:

- Reuters World / Business / Markets
- AP Top News / World / Business
- BBC World / Business
- SCMP News when filtered down to world, China, tech-policy, and macro/economy items
- FT or WSJ reporting when they materially add context to macro, policy, or market moves

These sources help define the global part of the agenda, especially when the overnight signal affects markets, trade, commodities, conflict risk, or policy expectations.

### 4. China business and markets depth

Use these after the public agenda is set, especially for the `Top 3`, company stories, and `经济投资风向标`:

- 第一财经
- 财新
- 财联社
- 界面新闻: 商业
- 华尔街见闻
- 财富中文网 / 商业
- 财富中文网 / 科技

These sources improve Chinese-language business framing, market texture, company detail, and cross-sector implications. They can supply section stories and occasionally a `Top 3` item, but they should not displace a bigger public-interest or macro lead without a clear reason.

### 5. Tech, science, and platform-impact detail

Use these for sector detail only after checking that the story matters beyond a niche product crowd:

- 36氪
- 虎嗅
- 钛媒体
- 极客公园
- IT之家
- 果壳网
- Readhub / 开发者资讯

These sources help the column cover AI, big tech, consumer platforms, hardware, science, and internet-product shifts with better specificity. They are most valuable when a technology story has clear business, regulatory, platform-power, or mainstream daily-life impact.

When using tech-detail feeds, prefer company results, platform rules, supply-chain moves, or infrastructure changes. Down-rank brand campaigns, conference hype, consumer-product launches, game long-features, and narrative interviews unless they clearly change the broader agenda.

### 6. Discovery-only and heat-check feeds

Use these to spot candidate topics or check whether something is spreading, but never as the main cited source:

- 微博热搜榜
- 知乎热榜
- 知乎日报
- ZAKER 精读新闻
- Readhub - 每日早报
- Google News 的站内搜索 RSS（例如定向 Reuters 的 query feed）
- other ranking, digest, or aggregator feeds

These feeds are useful for discovery, gap detection, and agenda comparison. They are not evidence by themselves.

## Source Weighting

Use the source set by editorial role, not as a flat pool.

### Tier A: lead-story candidates

These sources can supply stories that lead the article when the development has clear China-reader, public, market, or policy impact:

- major Chinese official announcements
- Reuters / AP / BBC primary reporting on major global developments
- major macro releases, filings, and agency statements
- Chinese-language broad-news bridge feeds only when they point to a genuinely shared agenda item that is then confirmed elsewhere
- authoritative macro, policy, or economic releases

Default use:

- choose the day's shared agenda
- support the lead paragraph
- supply 1-2 of the top 3 stories

### Tier B: section-story candidates

These sources are usually better for the `国内/政策与经济`, `国际`, and `科技与公司` body sections than for the lead story:

- 《联合早报》-中港台-即时
- 《联合早报》-国际-即时
- 中国日报: 时政
- 第一财经
- 财新
- 财联社
- 界面新闻: 商业
- 华尔街见闻
- 财富中文网 / 商业
- 财富中文网 / 科技
- Reuters Markets / Business
- BBC Business
- company filings or official newsroom updates when the story is already selected

Default use:

- enrich Chinese-language framing
- find section-worthy market, company, and sector developments
- add context after the shared agenda is set

### Tier C: confirmation or detail sources

These sources should often confirm or deepen an already selected story rather than define the whole column by themselves:

- 36氪
- 虎嗅
- 钛媒体
- 极客公园
- IT之家
- 果壳网
- Readhub / 开发者资讯
- specialist outlets for sector detail
- official company blogs for niche product updates
- market commentary or strategy notes only when they clarify the direction of travel instead of replacing primary reporting
- ranking and digest feeds only for discovery or heat-checking

Default use:

- confirm dates, release scope, filings, quotes, and market implications
- sharpen `为什么重要`
- supply detail for topic-focus or `经济投资风向标` items

## Lead Selection Rules

- Do not let a niche company announcement lead the whole issue of `《环球日报》` unless it clearly changes markets, policy, platform power, or mainstream daily life.
- Prefer a China-relevant macro or public-interest lead when several stories compete.
- Use specialist business or tech outlets to improve framing, but not as the sole basis for a major headline if stronger primary or broad reporting exists.
- Use Chinese-language bridge feeds to improve transmission into a Chinese morning-news frame, but still confirm high-stakes stories with primary reporting, official releases, or multiple reputable outlets.
- If the day is light, it is acceptable for a high-impact company announcement to enter the top 3, but it should still be written in a broad reader-facing frame.

## Editorial Use

- Do not treat every company newsroom post as a lead story.
- Do not let sector media overwhelm the shared agenda; use them to improve framing and specificity after the lead is set.
- Do not confuse feed mirrors, ranking pages, or aggregator wrappers with the reporting source.
- Use official sources for confirmation, detail, and original framing.
- Keep `《环球日报》` balanced: public agenda first, sector detail second.
- If an official announcement matters only inside one product ecosystem, it should usually stay in a section rather than become the headline of the day.
- Use macro and policy sources to support the `经济投资风向标`, but keep the section explanatory rather than tactical.

## Maintenance

- Prefer feeds that are stable, machine-readable, and close to the original publisher.
- If a mirrored feed on `plink.anyfeeder.com` or `rsshub.app` is the most stable transport, keep it, but still record the publisher as the source of record.
- Prefer direct institution feeds for macro and policy when they exist, especially central-bank, rates, trade, and regulatory release feeds.
- Remove feeds that frequently emit search-result links, archive links, or other non-canonical URLs instead of newsroom article URLs.
- Remove feeds that frequently omit usable publish timestamps or summaries; they create ranking noise and stale carry-over risk.
- If a feed becomes noisy or unreliable, replace it with another source in the same editorial role instead of expanding the feed list without bound.
- If a source changes quality, adjust its tier before removing it entirely.
