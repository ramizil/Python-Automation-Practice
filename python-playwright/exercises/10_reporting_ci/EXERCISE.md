# Exercise 10 — Reporting + GitHub Actions CI  🔜 (stub)

**Goal:** produce shareable reports and run the suite automatically on push.

## Outline
1. Add an HTML report (`pip install pytest-html`; `pytest --html=report.html`)
   or Allure (`allure-pytest`).
2. Capture screenshots/trace on failure (`--screenshot=only-on-failure
   --tracing=retain-on-failure` from pytest-playwright).
3. Add `.github/workflows/python-tests.yml` that installs deps,
   runs `playwright install --with-deps`, and runs `pytest`.
4. Upload the report and traces as workflow artifacts.

## Hints
- View a trace with `playwright show-trace test-results/.../trace.zip`.

> This is a stub — implement it as practice (or ask me to flesh it out).
