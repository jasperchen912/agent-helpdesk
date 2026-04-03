# Tool Boundary

Use this file to keep `daily-news` the skill separate from `tools/global-daily` the automation toolchain.

## `daily-news` Owns

- editorial rules
- the fixed `《环球日报》` structure
- source weighting logic
- style anchors
- prompt-to-behavior mapping
- what a good issue of `《环球日报》` looks like

`daily-news` should answer questions like:

- how should `《环球日报》` be structured
- what should lead the article
- how should sources be weighted
- what tone should the article use
- how should emphasis change without breaking the standing format

## `tools/global-daily` Owns

- feed fetching
- prompt assembly
- local bundle output
- Markdown file output
- optional scheduling
- optional handoff to `wechat-publisher`

`tools/global-daily` should answer questions like:

- where the feeds are configured
- how the drafting bundle is prepared at 08:00
- where generated files are stored
- how to publish to WeChat automatically

## Host LLM Boundary

- `daily-news` should use the current host model to draft the article itself.
- `tools/global-daily` should not shell out to a second model provider or CLI by default.
- In any host agent that exposes a local `exec` or shell tool, run `tools/global-daily/generate_global_daily.py` first, then draft with the current host model.

## Decision Rule

- If the change affects writing behavior, sourcing judgment, tone, structure, or triggering, change `daily-news`.
- If the change affects fetching, generation plumbing, scheduling, or publishing flow, change `tools/global-daily`.
- If a request touches both, update the skill first, then update the tool to follow the new skill behavior.

## Common Mistakes

- putting RSS URLs into `SKILL.md`
- encoding API or cron details into the skill instructions
- using tool defaults as if they were editorial truth
- changing the toolchain without updating the skill references it depends on
