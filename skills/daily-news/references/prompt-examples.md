# Prompt Examples

Use this file to map user requests to a stable response shape. Match the closest intent and carry over the expected output traits. Do not copy the example wording mechanically.

## Example 1: default morning column

### Prompt

`按今天的固定晨间专栏格式，写一篇《X月X日最该看的几件大事》`

### Expected traits

- use `morning column`
- keep the exact title pattern
- write one strong lead
- keep `top 3 + grouped sections + what to watch today`
- balance macro agenda with tech and business emphasis

## Example 2: AI heavier but still daily column

### Prompt

`按默认晨报格式写今天的日报，但更关注 AI 和科技公司动态`

### Expected traits

- still use `morning column`
- keep the fixed title pattern unless the user changes it
- let AI and company moves take more space in the sections
- do not turn the whole piece into a narrow AI-only report unless the user explicitly asks for that

## Example 3: business-first daily column

### Prompt

`按每天 8 点的固定专栏格式写，但从商业和市场角度排序今天的新闻`

### Expected traits

- use `morning column` with `business focus`
- rank stories by market and company impact
- push human-interest or soft tech items downward
- make `为什么重要` more business-facing

## Example 4: lighter news day

### Prompt

`按今天的晨报栏目写，但不要为了凑数塞太多新闻`

### Expected traits

- keep the same column structure
- reduce story count rather than padding
- let the lead and `what to watch today` carry more weight
- keep the article compact and confident

## Example 5: fast brief request

### Prompt

`给我今天的快速晨报版，5 分钟看完`

### Expected traits

- switch to `fast brief`
- shorten the lead to one sentence
- compress each item
- avoid section sprawl

## Example 6: topic focus request

### Prompt

`只写今天 AI 圈最该看的几件事`

### Expected traits

- switch to `topic focus`
- make the theme explicit in the title
- keep one core narrative through the whole piece
- avoid unrelated general headlines

## Example 7: fixed custom title

### Prompt

`标题就用《3月9日最该看的几件大事》，按默认栏目写`

### Expected traits

- obey the exact title
- keep the rest of the morning-column defaults
- do not generate extra title candidates
