#!/usr/bin/env bash
# BINF6200 formatter hook (PostToolUse).
#
# After Claude Code edits a Python file, ruff formats it. This is a HOOK: a
# deterministic action the harness runs for you, every time, no judgment
# involved. You will notice it in W2 ("why did the file change?") and learn
# to write your own in the optional Week 14 lecture.

set -euo pipefail

input=$(cat)

# Read the edited file's path from the JSON Claude Code sends on stdin, with jq if it is installed
# and python3 if not. If neither can read it, skip formatting: this hook tidies, it never blocks.
if command -v jq >/dev/null 2>&1; then
  path=$(printf '%s' "$input" | jq -r '.tool_input.file_path // empty') || exit 0
elif command -v python3 >/dev/null 2>&1; then
  path=$(printf '%s' "$input" | python3 -c '
import json, sys
print(json.load(sys.stdin).get("tool_input", {}).get("file_path") or "")
') || exit 0
else
  exit 0
fi

if [[ "$path" == *.py && -f "$path" ]]; then
  # Formatting must never break the edit itself.
  uv run ruff format "$path" >/dev/null 2>&1 || true
fi

exit 0
