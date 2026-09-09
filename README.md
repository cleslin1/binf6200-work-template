<!-- Rendered from README.md.tmpl by scripts/render_course.py in the course workspace. -->
# BINF6200 course repository

The starting point for everything you build in BINF6200 (Fall 2026). You clone it in
Week 1 as `binf6200-work` for the weekly examples, and again at the start of each homework into
its own directory (`hw01`, `hw02`, and so on), so every homework starts clean and picks up any
fixes made since your last clone.

## Setup (the Week 1 and Week 2 modules walk you through this)

```bash
uv sync                 # creates .venv with Python 3.14 and the pinned tools
uv run pytest           # one green test proves the wiring works
claude                  # start Claude Code from the repo root (you install it in Week 2)
```

## Keep this repository private

If you push this repo anywhere, it **must be private**. A public course repo earns a **0 on the
assignment** and is treated as a copyright and academic-integrity violation. This rule is unchanged
from previous semesters.

## What you submit

| Homework | You submit | Templates |
|---|---|---|
| HW1 (written by hand) | Three programs and a `README.md` in four parts: what each program does, your own five protocol numbers and the three lines you predicted before writing A3, your pasted runs, and your `git log --oneline` | none; the spec says what goes in the README |
| HW2 (written by hand) | Your code and its tests, plus `hw02-plan.md`: the spec you wrote before the code, your own check, and your judgment of Claude Code's read-only review of your code | `docs/hw-plan-template.md` |
| HW3 and HW4 (the PRD-to-output loop) | Your PRD (with the acceptance contract you wrote first), Claude Code's output (numbered transcript + the code), and an evaluation memo (~1 page, with evidence) | `docs/prd-template.md`, `docs/evaluation-memo-template.md` |

On HW1 and HW2, Claude Code or Claude in the browser may explain a traceback, a command, or a
concept, but neither writes your programs. `CLAUDE.md` tells Claude Code so; Claude in the browser
never reads that file, so there the rule is yours to keep.

Graded from an itemized list, grouped by the file each point belongs to. Every line is a fact you
can check yourself before submitting: does this function exist, does it do what the spec said, does
it have a docstring, does the suite still pass. The rubric is posted in Canvas. The checklist your
review of Claude Code's output is measured against is `docs/output-review-checklist.md`.

## Exporting your transcript

Your memo (and on HW2, section 7 of your plan file) cites evidence by turn number, so you need a
numbered transcript. The first export is HW2, where Claude Code reviews the code you wrote:

```bash
uv run python scripts/export_transcript.py --hw 2     # writes transcripts/hw02-transcript.md
uv run python scripts/export_transcript.py --list     # show the sessions it can see
```

Run it from the repo root after you finish a homework session. It reads the session log Claude Code
already keeps for this directory; it does not record anything new.

## What is already in here (and when you learn to build it yourself)

| Piece | What it does for you | You author your own in |
|---|---|---|
| `CLAUDE.md` | Project rules Claude Code follows every session (uv, pytest, docstrings) | W9 |
| `.claude/hooks/guard.sh` | Safety hook: blocks a few catastrophic commands (sudo, curl-pipe-sh, recursive deletes aimed outside the repo) | W14 (optional) |
| `.claude/hooks/format.sh` | Formats Python files after Claude Code edits them | W14 (optional) |
| `.claude/agents/code-reviewer.md` | "Ask the reviewer": a second pair of eyes on generated code (optional until W10) | W11 |
| `.claude/commands/run-tests.md` | `/run-tests`: runs pytest and explains any failure | W11 |
| `pyproject.toml` | Project and tool configuration (uv, pytest, pylint, ruff) | W5 |

Everything else at the permission prompt is your call: read the command before you approve it
(checklist item 1).

## Layout

- Homework scripts at the repo root, named exactly as the assignment specifies
- Tests in `tests/`; data files in `data/` (never committed); transcripts in `transcripts/`
- Course handouts in `docs/`

## If the safety hook blocks something legitimate

It prints why it blocked. If you believe the command is safe and needed, ask the TA; the override is
to comment out the matching rule in `.claude/hooks/guard.sh`. The optional Week 14 lecture explains
how hooks like it work.
