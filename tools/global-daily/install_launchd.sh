#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"
TOOL_DIR="$ROOT_DIR/tools/global-daily"
TEMPLATE="$TOOL_DIR/launchd/com.agenthelpdesk.global-daily.plist.template"
TARGET_DIR="$HOME/Library/LaunchAgents"
TARGET="$TARGET_DIR/com.agenthelpdesk.global-daily.plist"
RUN_SCRIPT="$TOOL_DIR/run_global_daily.sh"
STDOUT_LOG="$TOOL_DIR/logs/launchd.stdout.log"
STDERR_LOG="$TOOL_DIR/logs/launchd.stderr.log"

mkdir -p "$TARGET_DIR" "$TOOL_DIR/logs"

python3 - <<PY
from pathlib import Path

template = Path(r"$TEMPLATE").read_text(encoding="utf-8")
replacements = {
    "__RUN_SCRIPT__": r"$RUN_SCRIPT",
    "__WORKDIR__": r"$ROOT_DIR",
    "__STDOUT_LOG__": r"$STDOUT_LOG",
    "__STDERR_LOG__": r"$STDERR_LOG",
}
for key, value in replacements.items():
    template = template.replace(key, value)
Path(r"$TARGET").write_text(template, encoding="utf-8")
PY

launchctl unload "$TARGET" >/dev/null 2>&1 || true
launchctl load -w "$TARGET"

echo "Installed launchd job:"
echo "  $TARGET"
echo "It will prepare the bundle every day at 08:00 local machine time."
