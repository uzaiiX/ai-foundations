# ai-foundations

Phase 1 of my AI/ML engineering roadmap: Python in depth, the math behind ML, and a neural network from scratch.

## Structure

| Path | Purpose |
|---|---|
| `src/ai_foundations/weekNN/` | Code for each week (one subpackage per week) |
| `tests/weekNN/` | Tests for that week's code |
| `notebooks/` | Jupyter notebooks for math experiments and plots |
| `notes/learning-log.md` | Daily learning log |

## Commands

```bash
uv sync                      # install everything from uv.lock
uv run pytest                # run tests
uv run ruff check . --fix    # lint and auto-fix
uv run ruff format .         # format
uv run mypy                  # type check (strict)
uv run pre-commit run -a     # run every check, same as on commit
```

## Progress

- [x] Week 0: Setup
- [ ] Week 1: How Python thinks
