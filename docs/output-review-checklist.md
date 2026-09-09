# The Output Review Checklist

This is how you review code you did not write. From HW3 it is what your evaluation memo works
through, and the memo is a required artifact on every homework from there on. Items unlock in the
week their idea is taught; by the end of the course you have all 23.

**You are not expected to answer all of them every week.** Your memo answers the item(s) that
unlocked this week, plus the ones on the current **Top-10 card** that apply to your homework. The
card is posted in Canvas at a fixed link and changes weekly, with a line at the top saying what
changed.

## Half 1: the code itself (items 1 to 15)

| # | Ask | Unlocks |
|---|---|---|
| 1 | What exactly is Claude about to run, from which directory, and does it touch anything it should not (the deny list)? | W1 |
| 2 | Does the output match the spec as written (not as intended), and which inputs were never considered (empty, lowercase, wrong type)? | W2 |
| 3 | Are missing or empty inputs and errors handled, without a bare `except`? | W3 |
| 4 | Did Claude follow its own plan, or drift from it? | W3 |
| 5 | Are the tests real (asserting on behavior, covering edges) or tautological? | W4 |
| 6 | Is there shared mutable state (default arguments; class variables from W7)? | W4, again W7 |
| 7 | Does each function do one job, with an honest name, docstring, and type hints? | W4 |
| 8 | Any hidden O(n squared)? Is the data structure right (list, set, dict, Counter)? | W5 |
| 9 | Can the module be imported without side effects (`__main__` guard)? | W5 |
| 10 | Does it stream the file or slurp it into memory? | W6 |
| 11 | Does the pandas code lose rows silently (`merge how=`, NaN)? | W6 |
| 12 | Is the plot honest (axes, scale, labels)? | W6 |
| 13 | Does the class earn its existence, or would a function and a dict do? | W7 |
| 14 | Does the context manager release its resource when an exception is raised? | W7 |
| 15 | Is the inheritance earned (is-a, not has-a), and do the dunder methods preserve invariants (`__eq__` with `__hash__`)? | W8 |

## Half 2: the agent and its configuration (items 16 to 23)

| # | Ask | Unlocks |
|---|---|---|
| 16 | Did the plan touch files outside its scope? | W9 |
| 17 | Is this rule in CLAUDE.md, or did you repeat it in the prompt again? | W9 |
| 18 | Which permission did you grant that you should not have? | W9 |
| 19 | Does the diff match the plan and nothing more, and is this a commit message you would sign? | W10 |
| 20 | Did the subagent's summary lose something you needed? Is the slash command safe to run twice? | W11 |
| 21 | Are latency, rate limits, and cost accounted for, and is the MCP scope justified? | W12 |
| 22 | Does the skill trigger when it should, not trigger when it should not, and stay read-only where it should? | W13 |
| 23 | Is the hook deterministic, fast, and not trivially bypassed? | W14 |

## How to use it in a memo

Answer the question, do not repeat it, and cite where you saw the evidence.

- Weak: "Did the tests cover edge cases? Yes."
- Strong: "Item 5: the three generated tests all assert on the same happy-path string
  (`test_gc.py:8-19`). None covers an empty sequence, which my contract row 3 requires, so I asked
  for it in turn 14 and it failed until turn 17."
