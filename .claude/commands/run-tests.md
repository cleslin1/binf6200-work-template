---
description: Run the test suite and report results with a short diagnosis of any failure.
---

Run the project's test suite:

```bash
uv run pytest -q
```

If everything passes, report the pass count in one line. If anything fails, show the failing
test's output, explain the failure in plain language (naming the Output Review Checklist item it
maps to, if any), and suggest the smallest next step. Do not edit any test file.
