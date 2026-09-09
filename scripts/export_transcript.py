#!/usr/bin/env python3
"""Export this repo's most recent Claude Code session as a numbered-turn transcript.

Your evaluation memo cites evidence by turn number ("turn 12"), and the grader checks a
citation or two against the file you submit. This script produces that file.

It reads the session log Claude Code already keeps for this directory
(``~/.claude/projects/<this-repo>/<session-id>.jsonl``). It records nothing new.

Usage:
    uv run python scripts/export_transcript.py --hw 2
    uv run python scripts/export_transcript.py --hw 2 --session <session-id>
    uv run python scripts/export_transcript.py --list
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from datetime import datetime
from pathlib import Path

# Tool output is the evidence your memo quotes, so it is kept, but a single huge result
# would bury the conversation. Long results are trimmed with a marker.
MAX_RESULT_CHARS = 2000
PROJECTS_ROOT = Path.home() / ".claude" / "projects"


def project_slug(path: Path) -> str:
    """Claude Code names a project directory after its working directory."""
    return re.sub(r"[^A-Za-z0-9]", "-", str(path.resolve()))


def find_sessions(repo: Path) -> list[Path]:
    """Session logs for this repo, newest first."""
    directory = PROJECTS_ROOT / project_slug(repo)
    if not directory.is_dir():
        return []
    return sorted(directory.glob("*.jsonl"), key=lambda p: p.stat().st_mtime, reverse=True)


def block_to_text(block: dict) -> str:
    """Render one content block as readable markdown."""
    kind = block.get("type")
    if kind == "text":
        return block.get("text", "")
    if kind == "tool_use":
        name = block.get("name", "tool")
        payload = block.get("input", {}) or {}
        if "command" in payload:
            return f"**[{name}]**\n\n```bash\n{payload['command']}\n```"
        target = payload.get("file_path") or payload.get("path") or ""
        return f"**[{name}]** {target}".rstrip()
    if kind == "tool_result":
        content = block.get("content", "")
        if isinstance(content, list):
            content = "\n".join(
                part.get("text", "") for part in content if isinstance(part, dict)
            )
        content = str(content)
        if len(content) > MAX_RESULT_CHARS:
            content = content[:MAX_RESULT_CHARS] + f"\n... [trimmed at {MAX_RESULT_CHARS} characters]"
        return f"**[output]**\n\n```\n{content}\n```"
    if kind == "thinking":
        return ""
    return ""


def message_text(message: dict) -> str:
    """Flatten a message's content into markdown."""
    content = message.get("content")
    if isinstance(content, str):
        return content
    if isinstance(content, list):
        parts = [block_to_text(b) for b in content if isinstance(b, dict)]
        return "\n\n".join(p for p in parts if p.strip())
    return ""


def read_turns(session: Path) -> list[tuple[str, str]]:
    """Return (role, text) for each real conversation turn, in order."""
    turns: list[tuple[str, str]] = []
    with session.open(encoding="utf-8") as handle:
        for line in handle:
            try:
                entry = json.loads(line)
            except json.JSONDecodeError:
                continue
            if entry.get("type") not in {"user", "assistant"}:
                continue
            # Skip harness bookkeeping and subagent side conversations.
            if entry.get("isMeta") or entry.get("isSidechain"):
                continue
            message = entry.get("message")
            if not isinstance(message, dict):
                continue
            text = message_text(message).strip()
            if text:
                turns.append((message.get("role", entry["type"]), text))
    return turns


def write_transcript(turns: list[tuple[str, str]], session: Path, out_path: Path) -> None:
    """Write the numbered transcript your memo will cite."""
    stamp = datetime.fromtimestamp(session.stat().st_mtime).isoformat(timespec="seconds")
    lines = [
        f"# Claude Code transcript: {out_path.stem}",
        "",
        f"- Session: `{session.stem}`",
        f"- Exported: {datetime.now().isoformat(timespec='seconds')}",
        f"- Last activity: {stamp}",
        f"- Turns: {len(turns)}",
        "",
        "Cite evidence in your memo as **turn N** using the numbers below.",
        "",
        "---",
        "",
    ]
    for number, (role, text) in enumerate(turns, start=1):
        speaker = "You" if role == "user" else "Claude"
        lines.append(f"## Turn {number} ({speaker})")
        lines.append("")
        lines.append(text)
        lines.append("")
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text("\n".join(lines), encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--hw", type=int, help="homework number, used to name the output file")
    parser.add_argument("--session", help="session id to export (default: most recent)")
    parser.add_argument("--list", action="store_true", help="list sessions for this repo")
    args = parser.parse_args()

    repo = Path.cwd()
    sessions = find_sessions(repo)
    if not sessions:
        print(
            f"No Claude Code sessions found for {repo}.\n"
            "Run `claude` from this directory first, and export after the session.",
            file=sys.stderr,
        )
        return 1

    if args.list:
        print(f"Sessions for {repo}:")
        for session in sessions:
            stamp = datetime.fromtimestamp(session.stat().st_mtime).isoformat(timespec="minutes")
            print(f"  {session.stem}  last activity {stamp}")
        return 0

    if args.hw is None:
        parser.error("--hw is required (or use --list)")

    if args.session:
        matches = [s for s in sessions if s.stem == args.session]
        if not matches:
            print(f"No session {args.session} for this repo; try --list.", file=sys.stderr)
            return 1
        session = matches[0]
    else:
        session = sessions[0]

    turns = read_turns(session)
    if not turns:
        print(f"Session {session.stem} has no conversation turns to export.", file=sys.stderr)
        return 1

    out_path = repo / "transcripts" / f"hw{args.hw:02d}-transcript.md"
    write_transcript(turns, session, out_path)
    print(f"Wrote {out_path.relative_to(repo)} ({len(turns)} turns) from session {session.stem}.")
    print("Check that turn 1 is your PRD before you submit.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
