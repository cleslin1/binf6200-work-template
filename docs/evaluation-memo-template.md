# HW<NN> evaluation memo: <your name>

Used from HW3 (on HW2, Claude's review of your code is judged in section 7 of your plan file
instead). About one page. Copy to the repo root as `hw<NN>-memo.md` (for example `hw03-memo.md`).

**Every claim needs a locator**: a turn number from your exported transcript (`turn 12`) or a
`file.py:41` reference. A locator that does not resolve is spot-checked and an invented one is an
academic-integrity matter, not a lost point. Aim for at least three verbatim
quotes across sections 2, 3, and 5.

## 1. Session facts

- Iterations before you accepted the result: <number>
- Where your acceptance contract appears as your own prompt: turn <N>
- First line of that turn, quoted: `<paste it>`

## 2. What Claude got right

Paste the exact command you ran and its literal output. Do not summarize it.

```
$ <command>
<output>
```

Which test in section 3 of your PRD does that output satisfy? (locator: turn <N>)

## 3. What needed iteration

Name one specific thing that was wrong on the first attempt.

- What was wrong (locator: turn <N>):
- The failing output, quoted verbatim:
- What you said back to Claude:
- The corrected output, quoted verbatim:
- Iterations this took:

## 4. What you rejected

Name one thing Claude proposed that you did not accept: a design choice, a library, a snippet. One
sentence on why (locator: turn <N>).

If you accepted everything on the first pass, say so plainly and name the specific edge case you ran
to confirm it was actually right. Do not simply assert that it was.

## 5. Output Review Checklist findings

Answer this week's new item(s) plus the items on the current Top-10 card that apply. Answer the
question; do not restate it.

| Item # | What you found | Evidence (turn N, or file:line) |
|---|---|---|
| | | |
| | | |
| | | |

## 6. Final artifact against the definition of done

Does the delivered artifact satisfy section 6 of your PRD? List anything still wrong or out of
scope, even if you chose not to fix it. An honest gap costs less than one the grader finds.

## 7. What this taught you (two or three sentences, your own words)

Not "I learned about dictionaries." Name a decision you now understand differently, and connect it
to something Claude did or got wrong in this session.
