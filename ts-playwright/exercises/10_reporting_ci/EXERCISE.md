# Exercise 10 — Reporting + GitHub Actions CI  🔜 (stub)

**Goal:** produce shareable reports and run the suite automatically on push.

## Outline
1. The HTML reporter is already configured — open it with `npm run report`.
2. Traces/screenshots on failure are on (`trace: 'retain-on-failure'`). View a
   trace with `npx playwright show-trace test-results/.../trace.zip`.
3. Add `.github/workflows/ts-tests.yml`: `npm ci`,
   `npx playwright install --with-deps`, `npx playwright test`.
4. Upload `playwright-report/` and `test-results/` as artifacts.

> Stub — implement it as practice (or ask me to flesh it out).
