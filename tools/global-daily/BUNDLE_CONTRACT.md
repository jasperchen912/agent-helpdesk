# Bundle Contract

`global-daily` writes one bundle manifest per issue under `tools/global-daily/out/`.

Current schema:

- `global-daily.bundle/v1`

## Purpose

This manifest is the stable handoff contract between:

- `tools/global-daily`, which fetches and prepares inputs
- the host agent, which uses its current host model to draft the article
- optional downstream publishers such as `wechat-publisher`

`tools/global-daily` should not call a second LLM. The host agent should read this manifest, then read the referenced prompt and sources files.

## Guarantees

- The manifest is UTF-8 JSON.
- `repo_root` and every path under `artifacts.*_path` are absolute filesystem paths.
- `issue.cover_path` is the frontmatter value for the article and may be relative.
- `artifacts.prompt_path` always points to the draft prompt file.
- `artifacts.sources_path` always points to the selected-source JSON file.
- `artifacts.article_path` is the recommended write target for the final Markdown article.
- `drafting.frontmatter_required` is always `true` for this toolchain.
- New fields may be added in future schema revisions, but existing `v1` fields should remain stable.

## Shape

```json
{
  "schema_version": "global-daily.bundle/v1",
  "tool_name": "global-daily",
  "generated_at": "2026-04-03T08:00:00+08:00",
  "repo_root": "/abs/path/to/repo",
  "issue": {
    "date": "2026-04-03",
    "title": "《环球日报》｜4月3日",
    "timezone": "Asia/Shanghai",
    "publish_time": "08:00",
    "cover_path": "../assets/global-daily-cover.svg"
  },
  "artifacts": {
    "bundle_path": "/abs/path/to/out/2026-04-03-global-daily.bundle.json",
    "prompt_path": "/abs/path/to/out/2026-04-03-global-daily.prompt.txt",
    "sources_path": "/abs/path/to/out/2026-04-03-global-daily.sources.json",
    "article_path": "/abs/path/to/out/2026-04-03-global-daily.md"
  },
  "drafting": {
    "mode": "host-llm",
    "article_format": "markdown",
    "frontmatter_required": true,
    "article_status": "pending",
    "selected_item_count": 19
  }
}
```

## Host Flow

1. Run `python3 tools/global-daily/generate_global_daily.py --print-manifest` through the host `exec` tool.
2. Parse the JSON manifest from stdout.
3. Read `artifacts.prompt_path` and `artifacts.sources_path`.
4. Draft the final article with the current host model.
5. Write Markdown to `artifacts.article_path`.
6. If needed, publish with `./tools/global-daily/run_global_daily.sh --publish --article /path/to/article.md`.
