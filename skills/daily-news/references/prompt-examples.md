# Prompt Examples

Use this file to map user requests to the single standing `《环球日报》` shape. Match the closest intent and keep the same fixed structure. Do not copy the example wording mechanically.

## Example 1: default issue

### Prompt

`按《环球日报》的固定格式写今天这一期`

### Expected traits

- use the standing `《环球日报》` structure
- keep the exact title pattern
- start with a `先看三句` first-screen module
- write one strong lead
- keep `top 3 + grouped sections + 经济投资风向标 + what to watch today`
- balance domestic, global, policy, and market signals around one shared agenda
- make the `Top 3` detailed enough that each one reads like a small explainer, not a clip
- do not let two `Top 3` items tell the same event chain twice
- make each `Top 3` item name concrete actors, dates, or numbers

## Example 2: policy and macro heavier

### Prompt

`按《环球日报》的默认格式写今天这一期，但更关注政策、宏观和市场信号`

### Expected traits

- still use `《环球日报》`
- keep the fixed title pattern unless the user changes it
- let policy, economy, and market signals take more space in the top 3 and `经济投资风向标`
- do not turn the whole piece into a narrow market note unless the user explicitly asks for that

## Example 3: lighter news day

### Prompt

`按《环球日报》写今天这一期，但不要为了凑数塞太多新闻`

### Expected traits

- keep the same column structure
- reduce story count rather than padding
- let the lead, `经济投资风向标`, and `what to watch today` carry more weight
- keep the `先看三句` especially sharp because it may carry more of the reader value on a light day
- keep the article compact and confident
- even on a light day, keep the `Top 3` informative rather than skeletal

## Example 4: wind-vane request

### Prompt

`按《环球日报》写，并把经济投资风向标写得更有信息量`

### Expected traits

- still use `《环球日报》`
- keep the fixed title pattern and stable structure
- expand the `经济投资风向标` with sharper macro, policy, and market signals
- keep the grouped sections short so the extra density sits inside the wind-vane, not everywhere
- keep the rest of the piece general-news, not pure investment content

## Example 5: more detailed top 3

### Prompt

`按《环球日报》写，但 Top 3 每条都多给一点细节和背景`

### Expected traits

- still use `《环球日报》`
- keep the stable structure
- upgrade the `Top 3` into concrete explainers with facts, numbers, timing, and transmission
- keep the `先看三句` and grouped sections concise so the extra detail stays concentrated in `Top 3`
- keep grouped sections tighter than the `Top 3`

## Example 6: fixed custom title

### Prompt

`标题就用《环球日报》｜3月9日，按默认栏目写`

### Expected traits

- obey the exact title
- keep the rest of the standing defaults
- do not generate extra title candidates
