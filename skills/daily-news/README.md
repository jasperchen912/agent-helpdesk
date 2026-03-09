# daily-news

**面向微信公众号晨间专栏的新闻日报 skill**

`daily-news` 用来生成一篇稳定的、适合日更的中文新闻专栏，默认场景是 `每天北京时间 08:00` 发布一篇微信公众号晨报。

## 适用场景

- 每天早上固定生成一篇公众号日报
- 按 `《X月X日最该看的几件大事》` 这种固定栏目标题输出
- 需要综合热点，但重点偏向 `AI / 科技 / 商业`
- 需要稳定的栏目节奏，而不是每次都重新定义版式

## 默认能力

- 固定晨间专栏模式
- 中文成稿
- 中英混合信源
- 每条新闻附 `来源 / 日期`
- 简短 `为什么重要`
- 微信文章友好的段落和栏目结构
- 可选配图建议

## 主要资源

- `references/morning-column-profile.yaml`
  定义晨间专栏的默认画像、发布时间、标题模板和栏目顺序
- `references/morning-column-template.md`
  定义每天 08:00 专栏的成稿结构
- `references/source-policy.md`
  定义选题打分、来源规则和连续日更时的 lead 控制
- `references/morning-column-final-sample.md`
  定义整篇文章的风格锚点

## 常见调用方式

```text
请按今天的晨间专栏格式，生成一篇《X月X日最该看的几件大事》
```

```text
按默认晨报栏目写今天的日报，但更关注 AI 和科技公司动态
```

```text
按每天 8 点的固定专栏格式，输出今天最该看的几件大事
```

## 目录结构

```text
daily-news/
├── SKILL.md
├── README.md
├── _meta.json
├── agents/
│   └── openai.yaml
└── references/
    ├── morning-column-profile.yaml
    ├── morning-column-template.md
    ├── morning-column-final-sample.md
    ├── source-policy.md
    └── ...
```
