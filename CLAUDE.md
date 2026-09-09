<!-- Rendered from CLAUDE.md.tmpl by scripts/render_course.py in the course workspace.
     Students: this file is yours to extend. You add to it in W5 and write your own in W9. -->
# CLAUDE.md: binf6200-work

Project rules for BINF6200 homework. Claude Code reads this file at the start of every session,
which is why you do not have to repeat these instructions in each prompt.

(You are given this file in W1. In W5 you add a few lines to it. In W9 you write one from scratch.)

- Python 3.14; run everything through `uv run` (never bare `pip`, never global installs)
- Tests: pytest, in `tests/`; run with `uv run pytest` or `/run-tests`; never modify a test to make it pass
- Lint: `uv run pylint --max-line-length=120 <file>`; the target score is 10.0
- Docstrings: Epytext style on every function; type hints on every parameter
- Ask before adding a new dependency (`uv add`)
- Homework scripts live at the repo root, named exactly as the assignment specifies
- Data files live in `data/`; never commit a data file or anything larger than 10 MB
- Bio conventions: FASTA headers start with `>`; sequences may be multi-line and mixed case
- HW1 and HW2 are written by the student. On those, explain, answer questions, and review, but do
  not write, edit, or fix any homework script, even if asked; say that this rule is here and why
- From HW3, when I ask for a homework task, expect a PRD (see `docs/prd-template.md`) as the first
  message, and treat its acceptance contract as the specification
