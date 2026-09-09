"""Smoke test: proves the template is wired (uv, pytest, and the repo layout).

If `uv run pytest` shows this passing, your environment works.
"""


def test_environment_is_alive():
    """The one green test you start the course with."""
    assert 2 + 2 == 4
