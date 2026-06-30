# Exercise 10 — Reporting & CI

**Goal:** produce shareable reports and run the suite automatically on push.
This is what turns a folder of tests into a *pipeline*.

This repo already ships a working setup — your job is to **run it, read it, and
extend it**.

## What's already wired up
- **HTML report + trace + screenshots on failure** — configured in
  `playwright.config.ts` (`reporter`, `trace: 'retain-on-failure'`,
  `screenshot: 'only-on-failure'`).
- **CI** — `.github/workflows/ci.yml` has a `ts-tests` job that runs
  `npm ci` → `npx playwright install --with-deps chromium` → `npx playwright test`
  and uploads `playwright-report/` as an artifact (the same file also runs the
  Python suite and lints).

## Steps
1. Run the suite and open the report:
   ```bash
   npx playwright test
   npm run report           # opens the HTML report
   ```
2. Capture and inspect a trace: make a test fail on purpose, re-run, then:
   ```bash
   npx playwright show-trace test-results/.../trace.zip
   ```
   Step through the timeline, DOM snapshots, and network tab.
3. Read `.github/workflows/ci.yml` and map each step to what you ran locally.

## Extend it (practice)
- Add a `test:ci` script to `package.json` that runs with `--reporter=github`.
- Add the `@axe-core/playwright` package and a basic accessibility check, then a
  CI step for it.
- Make the `ts-tests` job a matrix across `chromium` and `firefox`.

## Done when
You've opened an HTML report, viewed a trace, and can explain what the CI job
does step by step.
