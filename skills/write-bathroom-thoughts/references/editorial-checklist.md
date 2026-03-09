# Editorial Checklist

Use this file before finalizing any draft.

## Frontmatter

- Title follows the archive pattern exactly unless the user supplied a fixed override.
- Cover points to a valid path or URL.
- The title focus is concrete rather than abstract.

## Opening

- The first two sentences contain a place, an object, and an action.
- The draft does not open with a thesis such as `我常常觉得`, `其实`, or `很多时候`.
- The opening uses one physical scene instead of summarizing the whole article.

## Body

- One dominant scene family carries the piece.
- Reflection arrives after observation rather than before it.
- At least one paragraph implies another person, a public atmosphere, or a social pressure unless solitude is the point.
- Remove any sentence that could fit into any generic late-night essay unchanged.

## Ending

- The last paragraph stays local.
- The ending lands on an image, a pause, or an unfinished action.
- The ending does not resolve into advice, doctrine, or `答案`.
- Cut phrases like `其实我们都`, `也许这就是成长`, `生活终究会...` unless there is a strong reason to keep them.

## Line Edit Flags

Cut or justify these fashionable but weak phrases:

- `治愈`
- `和解`
- `内耗`
- `情绪价值`
- `松弛感`
- `被看见`
- `某种意义上`
- `成年人都不容易`

## Final QA

- Keep paragraph count within `3-5` unless a short-edition piece clearly works shorter.
- If a local Markdown file exists, run `python3 scripts/lint_article.py path/to/article.md`.
- Add `--variant short` or `--variant long` when the piece intentionally uses a non-default length target.
- Fix every failure from the lint script. Review every warning before publishing.
- If the paired OpenClaw memory file exists, append or update the current issue record after the draft is publishable.
