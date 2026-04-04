# global-daily

Prepare and optionally publish the standing `08:00 Asia/Shanghai` WeChat issue of `《环球日报》`.

## What It Does

1. Fetch recent items from RSS feeds
2. Build a prompt from the `daily-news` skill references
3. Write a local bundle under `tools/global-daily/out/`
4. Let the current host LLM draft the article from that bundle
5. Optionally publish it through `skills/wechat-publisher/scripts/publish.sh`

The bundle protocol is defined in [BUNDLE_CONTRACT.md](/Users/jiajunch/Documents/personal_code/agent-helpdesk/tools/global-daily/BUNDLE_CONTRACT.md).

## Setup

```bash
cp tools/global-daily/config.example.json tools/global-daily/config.json
```

`config.json` lets you override feeds, output paths, theme, highlight theme, and default cover path.

## Run

Prepare today's bundle:

```bash
./tools/global-daily/run_global_daily.sh
```

Print the drafting prompt to stdout as well:

```bash
python3 tools/global-daily/generate_global_daily.py --print-prompt
```

Print the structured bundle manifest to stdout:

```bash
python3 tools/global-daily/generate_global_daily.py --print-manifest
```

Write a placeholder article for inspection:

```bash
./tools/global-daily/run_global_daily.sh --dry-run
```

Publish an article that has already been drafted by the current host LLM:

```bash
./tools/global-daily/run_global_daily.sh --publish --article /path/to/article.md
```

## Host Agent Flow

For any host agent with a local `exec` or shell tool:

1. Run `python3 tools/global-daily/generate_global_daily.py --print-manifest` via the host `exec` tool.
2. Parse the manifest JSON, then read `artifacts.prompt_path` and `artifacts.sources_path`.
3. Use the current host model to draft the full article from that prompt.
4. Write the final Markdown to the `article_path` reported by the tool, or another path you control.
5. Publish with `./tools/global-daily/run_global_daily.sh --publish --article /path/to/article.md` if needed.

For machine-readable integration, prefer `--print-manifest` and the versioned schema in [BUNDLE_CONTRACT.md](/Users/jiajunch/Documents/personal_code/agent-helpdesk/tools/global-daily/BUNDLE_CONTRACT.md).

## Install Daily 08:00 Bundle Prep

Install the bundled `launchd` job on macOS:

```bash
./tools/global-daily/install_launchd.sh
```

This creates a LaunchAgent that prepares the `《环球日报》` bundle every day at `08:00`.
