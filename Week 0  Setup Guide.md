# Week 0: Setup Guide

**Goal:** A professional Python project, `ai-foundations`, where every commit is automatically linted, formatted, type-checked and tested, both on your machine and on GitHub.
**Time:** 2–3 days (about 6–8 hours total)
**Tested:** Every command and file below was run and verified on November 5, 2026 (uv 0.13, Python 3.13, ruff 0.17.3, mypy 2.4, pytest 9.2).

**Rule:** Type every file yourself. Don't copy-paste, and don't use Cursor to generate it. The template zip is only for checking your work at the end.

---

## Your TypeScript knowledge, mapped to Python

You already know these ideas. Only the names are different:

| You know (TypeScript) | Python equivalent | What it does |
|---|---|---|
| `nvm` + `npm`/`pnpm` | **uv** | Installs Python versions, creates environments, manages dependencies |
| `package.json` | **pyproject.toml** | Project metadata, dependencies, tool settings |
| `pnpm-lock.yaml` | **uv.lock** | Exact versions so every machine installs the same thing |
| `node_modules/` (per project) | **.venv/** | The project's isolated environment |
| `npx some-tool` | **uv run some-tool** | Run a tool inside the project environment |
| ESLint + Prettier | **ruff** | Linting and formatting (one tool, very fast) |
| `tsc --noEmit` | **mypy** | Static type checking |
| Jest / Vitest | **pytest** | Testing |
| husky + lint-staged | **pre-commit** | Runs checks automatically before each commit |
| GitHub Actions | GitHub Actions | Same; runs everything in the cloud on every push |

Python doesn't check types at runtime. Type hints are like TypeScript types: they only help if a checker (mypy) enforces them. That's why mypy runs in **strict** mode here.

---

## Day 1: Install the tools (2–3 hours)

### Step 1. Install the basics

1. **Git**: [git-scm.com](https://git-scm.com/downloads). Check: `git --version`
2. **VS Code**: [code.visualstudio.com](https://code.visualstudio.com/) (Cursor works too, but keep AI autocomplete off for learning projects)
3. **GitHub account**, with Git configured:
   ```bash
   git config --global user.name "Your Name"
   git config --global user.email "you@example.com"
   git config --global init.defaultBranch main
   ```

### Step 2. Install uv

**Windows (PowerShell):**
```powershell
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

**macOS / Linux:**
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

Close and reopen your terminal, then check:
```bash
uv --version
```

### Step 3. Install Python through uv

```bash
uv python install 3.13
uv python list
```

**Why 3.13 and not the newest (3.15)?** ML libraries such as PyTorch take months to support each new Python release. 3.13 is stable and supported everywhere, so you won't lose hours to installation errors in Phase 2.

**Don't install Python from python.org, and don't use `pip install` globally.** uv manages everything per project, which avoids the classic "it works on my machine" problems.

### Step 4. Install VS Code extensions

Install these four extensions:
- **Python** (Microsoft)
- **Ruff** (Astral Software)
- **Mypy Type Checker** (Microsoft)
- **Jupyter** (Microsoft)

### Day 1 understanding check

Answer these in your learning log, in your own words:
1. Why does each project get its own `.venv` instead of sharing one global Python?
2. What's the difference between `pyproject.toml` and `uv.lock`?

---

## Day 2: Build the project (3–4 hours)

### Step 5. Create the project

```bash
uv init --lib --python 3.13 ai-foundations
cd ai-foundations
```

`--lib` creates the **src layout**:

```
ai-foundations/
├── pyproject.toml
├── .python-version
├── README.md
└── src/
    └── ai_foundations/
        ├── __init__.py
        └── py.typed
```

**Why src layout?** Your code lives inside `src/`, so tests can only import it the way a real user would, after it's installed. This catches packaging bugs that a flat layout hides. Professional Python libraries use this layout.

- `py.typed` tells type checkers that your package ships type hints.
- The package name uses underscores (`ai_foundations`) because Python imports can't contain hyphens.

### Step 6. Add dependencies

```bash
uv add numpy
uv add --dev ruff mypy pytest pytest-cov pre-commit ipykernel
```

- `uv add` puts packages in `dependencies`: code your project needs to run.
- `uv add --dev` puts them in the `dev` group: tools only you need while developing (like `devDependencies` in npm).
- `ipykernel` lets Jupyter notebooks in VS Code use this project's environment.

Open `pyproject.toml` and see what uv wrote. Then look at `uv.lock`; you never edit it by hand.

### Step 7. Configure the tools in `pyproject.toml`

Change the `description` line, then add this at the bottom:

```toml
[tool.ruff]
line-length = 100
target-version = "py313"

[tool.ruff.lint]
select = ["E", "F", "W", "I", "N", "UP", "B", "SIM", "NPY", "RUF"]

[tool.mypy]
python_version = "3.13"
strict = true
files = ["src", "tests"]

[tool.pytest.ini_options]
testpaths = ["tests"]
addopts = "-v --cov=ai_foundations --cov-report=term-missing"
```

**What each ruff rule set catches:**

| Code | Catches |
|---|---|
| `E`, `W` | Style errors and warnings (PEP 8) |
| `F` | Real bugs: unused imports, undefined names (Pyflakes) |
| `I` | Unsorted imports |
| `N` | Naming conventions (`snake_case` functions, `PascalCase` classes) |
| `UP` | Outdated syntax; suggests modern Python |
| `B` | Common bug patterns (bugbear), such as mutable default arguments |
| `SIM` | Code that can be simplified |
| `NPY` | NumPy-specific mistakes and deprecated APIs |
| `RUF` | Ruff's own extra checks |

When ruff flags something you don't understand, look up the rule code (for example `B006`) in the [ruff rules list](https://docs.astral.sh/ruff/rules/). Each one is a small Python lesson.

### Step 8. Create the folder structure

```bash
mkdir -p src/ai_foundations/week00 tests/week00 notebooks notes .github/workflows .vscode
```

On Windows PowerShell, create each folder with `mkdir` separately (PowerShell creates parent folders automatically).

Create these empty files (they mark folders as Python packages):
- `src/ai_foundations/week00/__init__.py`
- `tests/__init__.py`
- `tests/week00/__init__.py`
- `notebooks/.gitkeep` (Git doesn't track empty folders)

Replace the generated `hello()` function in `src/ai_foundations/__init__.py` with one line:
```python
"""AI foundations: Phase 1 learning code, one subpackage per week."""
```

**The structure for the whole of Phase 1:**

```
ai-foundations/
├── src/ai_foundations/
│   ├── week00/        # setup smoke test
│   ├── week01/        # Vector class
│   ├── week07/        # gradient checker (reused in weeks 10, 13, 14)
│   └── ...
├── tests/
│   ├── week00/
│   └── ...
├── notebooks/         # math experiments and plots
└── notes/
    └── learning-log.md
```

Using one package with a subpackage per week means later weeks can import earlier ones, for example `from ai_foundations.week07.gradcheck import check_gradient`. By Week 13 you'll have built your own small library.

### Step 9. Write your first typed code and tests

`src/ai_foundations/week00/stats.py`:
```python
"""Week 0 smoke test: a tiny typed function to prove the toolchain works."""


def mean(values: list[float]) -> float:
    """Return the arithmetic mean of a non-empty list of numbers."""
    if not values:
        raise ValueError("mean() requires at least one value")
    return sum(values) / len(values)
```

`tests/week00/test_stats.py`:
```python
import pytest

from ai_foundations.week00.stats import mean


def test_mean_of_simple_list() -> None:
    assert mean([1.0, 2.0, 3.0]) == 2.0


def test_mean_of_single_value() -> None:
    assert mean([5.0]) == 5.0


def test_mean_of_empty_list_raises() -> None:
    with pytest.raises(ValueError):
        mean([])
```

pytest finds any file named `test_*.py` and runs every function starting with `test_`. A plain `assert` is all you need; there's no `expect().toBe()` like in Jest.

### Step 10. Run every check by hand

```bash
uv run ruff check .
uv run ruff format --check .
uv run mypy
uv run pytest
```

Expected results:
- ruff: `All checks passed!`
- mypy: `Success: no issues found`
- pytest: `3 passed`, plus a coverage table showing `stats.py` at 100%

### Step 11. Set up pre-commit

Create `.pre-commit-config.yaml`:
```yaml
repos:
  - repo: https://github.com/astral-sh/ruff-pre-commit
    rev: v0.17.3
    hooks:
      - id: ruff-check
        args: [--fix]
      - id: ruff-format
  - repo: https://github.com/pre-commit/pre-commit-hooks
    rev: v6.0.0
    hooks:
      - id: trailing-whitespace
      - id: end-of-file-fixer
      - id: check-yaml
      - id: check-added-large-files
        args: [--maxkb=2000]
  - repo: local
    hooks:
      - id: mypy
        name: mypy (strict)
        entry: uv run mypy
        language: system
        types: [python]
        pass_filenames: false
```

Then:
```bash
git init
git add -A
uv run pre-commit install
uv run pre-commit run --all-files
```

All seven hooks should show `Passed`. From now on they run automatically on every `git commit`.

- `check-added-large-files` stops you from committing datasets or model files by accident, a very common ML mistake.
- mypy runs through `uv run`, so it uses your project's exact environment.

### Step 12. Add the CI workflow

`.github/workflows/ci.yml`:
```yaml
name: CI

on:
  push:
  pull_request:

jobs:
  check:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v7

      - name: Install uv
        uses: astral-sh/setup-uv@v10.3.3
        with:
          enable-cache: true

      - name: Install Python and dependencies
        run: uv sync --locked

      - name: Lint (ruff)
        run: uv run ruff check .

      - name: Format check (ruff)
        run: uv run ruff format --check .

      - name: Type check (mypy)
        run: uv run mypy

      - name: Tests (pytest)
        run: uv run pytest
```

`uv sync --locked` fails if `uv.lock` is out of date with `pyproject.toml`. That guarantees CI tests exactly what you tested locally. The uv action reads `.python-version`, so CI also uses Python 3.13.

### Step 13. Finish `.gitignore`

uv already ignores `.venv` and Python build files. Add these lines:
```gitignore

# Jupyter
.ipynb_checkpoints/
# Data and model files (keep large files out of Git)
data/
*.npz
*.pt
# Coverage
.coverage
htmlcov/
```

### Step 14. VS Code settings

`.vscode/settings.json`:
```json
{
  "python.defaultInterpreterPath": "${workspaceFolder}/.venv",
  "python.testing.pytestEnabled": true,
  "[python]": {
    "editor.defaultFormatter": "charliermarsh.ruff",
    "editor.formatOnSave": true,
    "editor.codeActionsOnSave": {
      "source.fixAll": "explicit",
      "source.organizeImports": "explicit"
    }
  },
  "mypy-type-checker.importStrategy": "fromEnvironment"
}
```

Then run **Python: Select Interpreter** from the VS Code command palette and choose the `.venv` inside your project. Open the Testing panel (flask icon); your 3 tests should appear there.

### Step 15. Push to GitHub

1. Create an empty repository named `ai-foundations` on GitHub. Don't add a README, `.gitignore` or license, because you already have them.
2. Push:
   ```bash
   git add -A
   git commit -m "Week 0: project setup with uv, ruff, mypy, pytest, pre-commit and CI"
   git remote add origin https://github.com/YOUR-USERNAME/ai-foundations.git
   git push -u origin main
   ```
3. Open the **Actions** tab on GitHub and watch the CI run turn green.

---

## Day 3: Break things on purpose, then prepare (1–2 hours)

### Step 16. Prove each safety net works

Do each one, see it fail, and read the error message carefully before fixing it.

| Break it | What should catch it |
|---|---|
| Add `import os` at the top of `stats.py` and don't use it | ruff `F401` (unused import) |
| Change `-> float` to `-> str` in `mean` | mypy: incompatible return type |
| Remove the type hint from `values` | mypy strict: missing type annotation |
| Change a test to expect `mean([1.0, 2.0, 3.0]) == 3.0` | pytest: assertion failure, showing both values |
| Write `def f(items: list[int] = []):` | ruff `B006` (mutable default argument). Look up why this is dangerous; it comes back in Week 1 |
| Push a commit with a failing test, using `git commit --no-verify` to skip pre-commit | GitHub Actions turns red |

The last one shows why CI matters: local hooks can be skipped, but CI can't.

### Step 17. Notebook check

Create `notebooks/00_setup_check.ipynb` in VS Code, choose the `.venv` kernel, and run:
```python
import sys
import numpy as np

print(sys.version)
print(np.__version__)
print(np.arange(6).reshape(2, 3))
```
If you see Python 3.13 and a 2×3 array, notebooks are working.

### Step 18. Learning log, README and schedule

1. Create `notes/learning-log.md` with this template:
   ```markdown
   ## YYYY-MM-DD — Week X, Day Y
   - **Learned:**
   - **Confused by:**
   - **Explain-back (2–3 sentences in my own words):**
   - **Next:**
   ```
2. Write a `README.md` describing the project, its structure, the commands, and a progress checklist (Week 0 ticked).
3. **Block fixed study times in your calendar**, for example 2 hours each weekday plus one longer weekend session. A fixed schedule matters more than motivation.

### Step 19. Get the resources

- Buy or borrow **Fluent Python, 2nd edition**. You start it in Week 1.
- Bookmark: [3Blue1Brown, Essence of Linear Algebra](https://www.3blue1brown.com/lessons/vectors/), [Mathematics for Machine Learning](https://mml-book.github.io/), and the [NeetCode roadmap](https://neetcode.io/roadmap).
- Create a free NeetCode account so your progress is saved.

---

## Daily commands (keep this handy)

```bash
uv sync                      # install everything (after cloning or pulling)
uv add <package>             # add a runtime dependency
uv add --dev <package>       # add a development tool
uv run pytest                # run tests
uv run ruff check . --fix    # lint and auto-fix
uv run ruff format .         # format
uv run mypy                  # type check
uv run pre-commit run -a     # run every check
```

---

## Week 0 exit checklist

- [ ] `uv --version` works and Python 3.13 is installed through uv
- [ ] The project uses the src layout, and I can explain why
- [ ] ruff, mypy (strict) and pytest all pass locally
- [ ] pre-commit runs automatically on `git commit`
- [ ] GitHub Actions shows a green check on my latest push
- [ ] I broke each safety net on purpose and read every error
- [ ] Notebooks run with the project's `.venv` kernel
- [ ] Learning log started, study times blocked in my calendar
- [ ] Fluent Python ready for Week 1
- [ ] I can explain every line of `pyproject.toml` and `ci.yml` without notes

---

## If something goes wrong

| Problem | Fix |
|---|---|
| `uv: command not found` | Reopen the terminal. On Windows, restart VS Code so it picks up the new PATH |
| VS Code can't import `ai_foundations` | Select the `.venv` interpreter (Step 14), then run `uv sync` |
| mypy says "Cannot find implementation or library stub" | Run `uv sync`; the package must be installed in `.venv` |
| CI fails at `uv sync --locked` | You changed `pyproject.toml` without updating the lock file. Run `uv lock`, then commit `uv.lock` |
| pre-commit is slow the first time | Normal; it's installing hook environments once |
| A ruff error you don't understand | Look up the rule code in the [ruff rules list](https://docs.astral.sh/ruff/rules/) |

Only when you've ticked every box on the exit checklist, compare your project with the template zip. Then start Week 1.
