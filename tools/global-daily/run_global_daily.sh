#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"
TOOL_DIR="$ROOT_DIR/tools/global-daily"
GENERATOR="$TOOL_DIR/generate_global_daily.py"
PUBLISHER="$ROOT_DIR/skills/wechat-publisher/scripts/publish.sh"
CONFIG_FILE="$TOOL_DIR/config.json"

publish=0
article_path=""
args=()

while [[ $# -gt 0 ]]; do
  case "$1" in
    --publish)
      publish=1
      shift
      ;;
    --article)
      if [[ $# -lt 2 ]]; then
        echo "--article requires a file path" >&2
        exit 1
      fi
      article_path="$2"
      shift 2
      ;;
    *)
      args+=("$1")
      shift
      ;;
  esac
done

mkdir -p "$TOOL_DIR/out" "$TOOL_DIR/logs"

if [[ ! -f "$GENERATOR" ]]; then
  echo "Generator not found: $GENERATOR" >&2
  exit 1
fi

if [[ -f "$CONFIG_FILE" ]]; then
  echo "Using config: $CONFIG_FILE"
else
  echo "Using default config; copy config.example.json to config.json to override."
fi

if [[ -n "$article_path" ]]; then
  echo "Using existing article: $article_path"
else
  BUNDLE_PATH="$(python3 "$GENERATOR" "${args[@]}")"
  echo "Prepared bundle: $BUNDLE_PATH"
fi

if [[ "$publish" -eq 1 ]]; then
  if [[ ! -x "$PUBLISHER" ]]; then
    echo "Publisher script not executable: $PUBLISHER" >&2
    exit 1
  fi
  if [[ -z "$article_path" ]]; then
    echo "Publishing now requires an explicit article path via --article." >&2
    exit 1
  fi
  if [[ ! -f "$article_path" ]]; then
    echo "Article not found: $article_path" >&2
    exit 1
  fi
  "$PUBLISHER" "$article_path"
fi
