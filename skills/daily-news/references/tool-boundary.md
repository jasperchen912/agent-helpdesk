# Tool Boundary

Use this file to keep `daily-news` the skill separate from `tools/morning-column` the automation toolchain.

## `daily-news` Owns

- editorial rules
- output structures and variants
- source weighting logic
- style anchors
- prompt-to-behavior mapping
- what a good morning column looks like

`daily-news` should answer questions like:

- how should the morning column be structured
- what should lead the article
- how should sources be weighted
- what tone should the article use
- when should a request switch to fast brief or topic focus

## `tools/morning-column` Owns

- feed fetching
- prompt assembly
- OpenAI API calls
- Markdown file output
- optional scheduling
- optional handoff to `wechat-publisher`

`tools/morning-column` should answer questions like:

- where the feeds are configured
- how the article is generated automatically at 08:00
- where generated files are stored
- how to publish to WeChat automatically

## Decision Rule

- If the change affects writing behavior, sourcing judgment, tone, structure, or triggering, change `daily-news`.
- If the change affects fetching, generation plumbing, scheduling, or publishing flow, change `tools/morning-column`.
- If a request touches both, update the skill first, then update the tool to follow the new skill behavior.

## Common Mistakes

- putting RSS URLs into `SKILL.md`
- encoding API or cron details into the skill instructions
- using tool defaults as if they were editorial truth
- changing the toolchain without updating the skill references it depends on
