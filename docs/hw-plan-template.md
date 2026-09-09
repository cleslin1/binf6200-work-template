# HW<NN> plan: <your name>, <date>

The spec you write for yourself. Used from **HW2** (HW1 uses its `README.md` instead). Copy this
file to the repo root as `hw<NN>-plan.md` (for example `hw02-plan.md`) and fill in sections 1 to 3
**before you write any code**. Then write the program, committing as you go. Come back for sections
4 onward once it runs.

In HW3 this file grows into the PRD (`docs/prd-template.md`), where the one doing the building is
Claude instead of you. The habit is the same: say what the right answer is before anyone, you or
Claude, produces one.

## 1. Goal, one sentence per program

> Example: "`protein_analyzer.py` reads a FASTA file given with `--infile` and writes one line of
> statistics per sequence to the file given with `--outfile`, exiting with an error if the FASTA is
> malformed."

- `<program>.py`:
- `<program>.py`:

## 2. Input and expected output table (write this BEFORE the code)

One table per program that takes input. Include at least one row that is not an example from the
assignment and one row that is deliberately awkward (zero, a value that should be rejected, a very
large number). Write what the output **should be**; you find out later whether it is.

**`<program>.py`**

| # | Input | Expected output |
|---|---|---|
| 1 (from the assignment) | | |
| 2 (my own) | | |
| 3 (awkward) | | |

## 3. Edge cases

What could go wrong, and what should happen when it does. Name the behavior ("print an error and
exit with a non-zero code"), not "handle errors".

| Edge case | What should happen |
|---|---|
| | |
| | |

After Week 4, turn sections 2 and 3 into a few pytest tests in `tests/`, written before the
implementation, so they fail at first. This section then just points at them: "see
`tests/test_protein_analyzer.py`".

## 4. What I checked (after the code runs)

Run every row of your table and paste the real output. Do not retype it.

```
$ uv run python <program>.py
<paste what appeared>
```

Which rows matched? Which did not, and what did you change? A row that failed and then got fixed
is worth more here than a table that passed the first time.

## 5. What I understand now

Answer the questions the assignment asks, two or three sentences each, in your own words. Not "I
learned about variables": name a decision in your program and say why it is right.

## 6. My commits

Paste the output of `git log --oneline`. Several commits with messages that say what changed is the
shape we want; one commit at the end called "hw2" is not.

```
$ git log --oneline
<paste what appeared>
```

## 7. Claude's review of my code (HW2 only)

Only after sections 1 to 6 are done. Ask Claude Code to review your program against your tests,
read-only ("review this; do not edit anything"). Export the transcript with
`uv run python scripts/export_transcript.py --hw 2`, then fill in one row per claim Claude made:

| Claude said (turn N) | Right or wrong? | Evidence (file:line, or a command you ran) | What I did about it |
|---|---|---|---|
| | | | |

Finish with one sentence: which claim would you not have caught on your own, and which one was
wrong?
