#!/usr/bin/env bash
# BINF6200 course safety hook (PreToolUse).
#
# The optional Week 14 lecture explains how hooks like this work. Either way, it is your seatbelt:
# it blocks a handful of catastrophic commands so one careless "approve"
# cannot damage your machine. Everything else is still YOUR call at the
# permission prompt (Output Review Checklist item 1).
#
# If it blocks something you believe is legitimate, ask the TA. The override
# is to comment out the matching rule below.

set -euo pipefail

input=$(cat)

block() {
  echo "BLOCKED by the course safety hook: $1" >&2
  echo "Why: $2. (The optional Week 14 lecture explains how hooks work.)" >&2
  exit 2
}

# Claude Code describes the action it wants to take as JSON on stdin. This reads one field of it.
# jq is the usual tool but is not installed everywhere (older macOS, many Linux desktops), so
# python3 is the fallback. Exit code 2 is the only one Claude Code treats as "stop", so if the
# field cannot be read at all, the hook blocks instead of failing and letting everything through.
json_field() {
  if command -v jq >/dev/null 2>&1; then
    printf '%s' "$input" | jq -r ".$1 // empty" 2>/dev/null
  elif command -v python3 >/dev/null 2>&1; then
    printf '%s' "$input" | python3 -c '
import json, sys
value = json.load(sys.stdin)
for key in sys.argv[1].split("."):
    value = value.get(key) if isinstance(value, dict) else None
print("" if value is None else value)
' "$1" 2>/dev/null
  else
    return 1
  fi
}

unreadable() {
  block "an action it could not read" \
    "it needs jq or python3 to check what is about to run; install jq (brew install jq, or sudo apt install jq) and try again"
}

cmd=$(json_field tool_input.command) || unreadable
path=$(json_field tool_input.file_path) || unreadable

if [[ -n "$cmd" ]]; then
  # Rule 1: nothing in this course needs administrator rights.
  if printf '%s' "$cmd" | grep -Eq '(^|[;&| ])sudo( |$)'; then
    block "$cmd" "sudo runs as administrator; nothing in this course needs it"
  fi
  # Rule 2: piping a download straight into a shell runs unreviewed code.
  if printf '%s' "$cmd" | grep -Eq '(curl|wget)[^|]*\|[ ]*(ba|z)?sh'; then
    block "$cmd" "piping a download into a shell executes code nobody reviewed"
  fi
  # Rule 3: recursive delete aimed at an absolute path, your home, or a parent dir.
  if printf '%s' "$cmd" | grep -Eq '\brm\b[^|;&]*-[a-zA-Z]*r[a-zA-Z]*[ ]+("?(/|~|\.\.))'; then
    block "$cmd" "recursive delete outside this repo can destroy work beyond the course"
  fi
fi

# Rule 4: file edits stay inside the project directory.
proj="${CLAUDE_PROJECT_DIR:-$PWD}"
if [[ -n "$path" && "$path" != "$proj"* ]]; then
  block "write to $path" "Claude Code should only edit files inside $proj"
fi

exit 0
