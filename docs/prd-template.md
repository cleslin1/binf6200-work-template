<!-- Rendered from prd-template.md.tmpl by scripts/render_course.py in the course workspace. -->
# HW<NN> PRD: <your name>, <date>

Used from HW3, the first PRD-to-output loop (HW2 uses `docs/hw-plan-template.md`; HW1 uses its
`README.md`). Copy
this file to the repo root as `hw<NN>-prd.md` (for example `hw03-prd.md`) and fill it in. Keep it
to one page.

**The order matters.** Write section 3 before you open Claude Code. Then paste this whole PRD as
your first message to Claude. Your transcript should open with it, and that is what the grader
looks for.

## 1. Goal (one sentence)

What should Claude build? Be specific enough that a stranger could tell whether the finished thing
satisfies it.

> Example: "Read a FASTA file and print the GC percentage of each record, sorted highest first."

## 2. Inputs and outputs

- **Input:** exact file name, type, and format, with one real example line
- **Output:** exact format, with one real example line
- **How it is run:** `uv run python <script>.py --input <file>`

## 3. Acceptance contract (write this BEFORE you open Claude)

This is the part you write by hand: pytest test names and assertions only. No implementation
exists yet, so these will fail; that is correct. You did the same thing for yourself on HW2; now
the tests are the contract Claude builds to.

```python
def test_gc_content_typical_sequence():
    assert gc_content("GCGCAT") == 50.0

def test_gc_content_empty_sequence():
    assert gc_content("") == 0.0

def test_gc_content_accepts_lowercase():
    assert gc_content("gcgcat") == 50.0
```

## 4. Edge cases

List at least three inputs that would break a naive solution, and say what *should* happen for each.
Not "handle errors": name the error and name the correct behavior (raise? return zero? skip with a
warning?).

| Edge case | What should happen |
|---|---|
| | |
| | |
| | |

## 5. Constraints and non-goals

- Allowed modules for this homework: <copy from the assignment>
- Required file and function names, exactly: <copy from the assignment>
- Python 3.14, run through `uv run`
- Style: `uv run pylint --max-line-length=120`, target score 10.0
- Docstrings on every function; type hints on every parameter
- Do not commit data files. Do not change a test to make it pass.
- What Claude should NOT do here: <e.g. "no pandas for this one", "no extra CLI flags">

## 6. Definition of done

- [ ] Every test in section 3 passes
- [ ] It also survives edge cases I did not write down
- [ ] `uv run pytest` green; `uv run pylint` at or above the required score
- [ ] File and function names match this PRD exactly
- [ ] No data files committed; no bare `except`

---

**Now paste this PRD into Claude Code as your first message.** When you are finished, export the
transcript with `uv run python scripts/export_transcript.py --hw <N>` and write your evaluation
memo from `docs/evaluation-memo-template.md`.
