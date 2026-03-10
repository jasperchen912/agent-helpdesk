# Prompt Examples

Use this file to map user requests to a stable response shape. Match the closest intent and carry over the expected output traits. Do not copy the example wording mechanically.

## Example 1: default morning column

### Prompt

`按今天的固定晨间专栏格式，写一篇《X月X日最该看的几件大事》`

### Expected traits

- use `morning column`
- keep the exact title pattern
- write one strong lead
- keep `top 3 + grouped sections + 经济投资风向标 + what to watch today`
- balance domestic, global, policy, and market signals around one shared agenda
- make the `Top 3` detailed enough that each one reads like a small explainer, not a clip
- make each `Top 3` item name concrete actors, dates, or numbers

## Example 2: policy and macro heavier but still daily column

### Prompt

`按默认晨报格式写今天的日报，但更关注政策、宏观和市场信号`

### Expected traits

- still use `morning column`
- keep the fixed title pattern unless the user changes it
- let policy, economy, and market signals take more space in the top 3 and `经济投资风向标`
- do not turn the whole piece into a narrow market note unless the user explicitly asks for that

## Example 3: business-first daily column

### Prompt

`按每天 8 点的固定专栏格式写，但从商业和市场角度排序今天的新闻`

### Expected traits

- use `morning column` with `business focus`
- rank stories by market and company impact
- push human-interest or soft tech items downward
- make `为什么重要` and `经济投资风向标` more business-facing
- keep the `Top 3` detailed enough to explain how the signal reaches markets or companies

## Example 4: lighter news day

### Prompt

`按今天的晨报栏目写，但不要为了凑数塞太多新闻`

### Expected traits

- keep the same column structure
- reduce story count rather than padding
- let the lead, `经济投资风向标`, and `what to watch today` carry more weight
- keep the article compact and confident
- even on a light day, keep the `Top 3` informative rather than skeletal

## Example 5: fast brief request

### Prompt

`给我今天的快速晨报版，5 分钟看完`

### Expected traits

- switch to `fast brief`
- shorten the lead to one sentence
- compress each item
- avoid section sprawl

## Example 6: wind-vane request

### Prompt

`按默认晨报写，并把经济投资风向标写得更有信息量`

### Expected traits

- still use `morning column`
- keep the fixed title pattern and stable structure
- expand the `经济投资风向标` with sharper macro, policy, and market signals
- keep the rest of the piece general-news, not pure investment content

## Example 7: more detailed top 3

### Prompt

`按默认晨报写，但 Top 3 每条都多给一点细节和背景`

### Expected traits

- still use `morning column`
- keep the stable structure
- upgrade the `Top 3` into concrete explainers with facts, numbers, timing, and transmission
- keep grouped sections tighter than the `Top 3`

## Example 8: topic focus request

### Prompt

`只写今天 AI 圈最该看的几件事`

### Expected traits

- switch to `topic focus`
- make the theme explicit in the title
- keep one core narrative through the whole piece
- avoid unrelated general headlines

## Example 9: fixed custom title

### Prompt

`标题就用《3月9日最该看的几件大事》，按默认栏目写`

### Expected traits

- obey the exact title
- keep the rest of the morning-column defaults
- do not generate extra title candidates
