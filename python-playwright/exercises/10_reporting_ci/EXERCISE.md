# Exercise 10 — Reporting, quality gates & CI

**Goal:** produce shareable reports, keep the code clean automatically, and run
the whole suite on every push. This is what turns a folder of tests into a
*pipeline*.

This repo already ships a working setup — your job is to **run it, read it, and
extend it**.

## What's already wired up
- **HTML report** — `pytest-html` (in `requirements-dev.txt`).
- **Lint + format** — `ruff` (config in `pyproject.toml`).
- **Type checking** — `mypy framework` (config in `pyproject.toml`).
- **Pre-commit hooks** — `.pre-commit-config.yaml` (repo root) runs ruff before
  each commit.
- **CI** — `.github/workflows/ci.yml` runs `lint`, `python-tests`, and
  `ts-tests` jobs on every push/PR and uploads reports as artifacts.

## Steps
1. Install the dev tooling and generate a report:
   ```bash
   pip install -r requirements-dev.txt
   pytest tests --html=report.html --self-contained-html
   ```
   Open `report.html` in a browser.
2. Run the quality gates the way CI does:
   ```bash
   ruff format --check .
   ruff check .
   mypy framework
   ```
3. Turn on pre-commit so you can't commit unformatted code:
   ```bash
   pip install pre-commit
   pre-commit install
   pre-commit run --all-files
   ```
4. Capture a failure trace: make a test fail on purpose, run
   `pytest --tracing=retain-on-failure`, then open it with
   `playwright show-trace test-results/.../trace.zip`.

## Extend it (practice)
- Add a `ruff` rule (e.g. `"C4"` comprehensions) and fix what it flags.
- Tighten `mypy` with `disallow_untyped_defs = true` and add the missing hints.
- Add a job to `ci.yml` that uploads the `pytest-html` report on failure only.

## Done when
You've opened an HTML report, all three gates pass locally, and you understand
what each CI job does.
