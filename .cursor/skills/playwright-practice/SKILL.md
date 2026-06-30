---
name: playwright-practice
description: >-
  Extend and validate the Python+TypeScript Playwright practice repo
  (Python-Automation-Practice). Use when adding/fleshing exercises, building the
  next topic or the Parabank capstone, running or fixing the reference suites,
  or whenever working in this repo's python-playwright/ or ts-playwright/ folders
  (SauceDemo, restful-booker, DummyJSON, Parabank targets).
---

# Playwright Practice Repo

A learning repo with **two mirrored stacks** teaching the same automation topics:
- `python-playwright/` — pytest + `pytest-playwright`
- `ts-playwright/` — `@playwright/test`

Topics 01–06 are complete (worked example + exercise skeleton + solution);
07–11 are `EXERCISE.md` stubs to flesh out. Always implement a topic in **both**
stacks to keep them mirrored.

## Targets (free public demo sites)
- SauceDemo `https://www.saucedemo.com` — UI store (login/cart/checkout)
- restful-booker `https://restful-booker.herokuapp.com` — API auth + CRUD
- DummyJSON `https://dummyjson.com` — store API for mocking (topic 08)
- Parabank `https://parabank.parasoft.com/parabank` — dummy bank (capstone 11)

## Critical gotchas (read before editing)

1. **Corporate TLS proxy.** This network does TLS inspection → Playwright errors
   with "self-signed certificate in certificate chain". Both stacks default
   `IGNORE_HTTPS_ERRORS` ON (Python `framework/config.py`, TS `src/config.ts`)
   and apply it to browser contexts and API request contexts. Keep new API
   contexts / browser launches honoring this flag.
2. **Numeric exercise dir names** (`01_first_test`) are NOT valid Python package
   names — never add `__init__.py` to exercise dirs and never use relative
   imports there. Keep each Python exercise **self-contained in one file**
   (import only from the `framework` package).
3. **Duplicate test basenames break pytest.** Skeleton and solution must have
   different filenames. Convention: skeleton `test_x.py`, solution
   `solution/test_x_solution.py`. (TS may reuse the name since solutions live in
   a `solution/` subdir under a separate testDir.)
4. **Default runs are scoped.** Python `pytest.ini` sets `testpaths = tests`;
   TS `playwright.config.ts` sets `testDir: ./tests`. So a plain run executes
   only the worked reference suite, never the exercise skeletons (which fail on
   purpose). Exercises run explicitly: Python by path, TS via
   `playwright.exercises.config.ts`.
5. **TS parallel timeouts.** Demo sites behind the proxy are slow; the TS config
   sets `workers: 4`, `timeout: 60_000`, `navigationTimeout: 45_000`. Don't drop
   these or UI specs flake with "timeout while setting up page".

## Validate (run after any change)

Python:
```bash
cd python-playwright
.venv\Scripts\python.exe -m pytest tests -q          # reference suite must be green
.venv\Scripts\python.exe -m pytest exercises/06_api_basics/solution   # spot-check a solution
```
TypeScript:
```bash
cd ts-playwright
npx playwright test --reporter=list                   # reference suite must be green
npx playwright test -c playwright.exercises.config.ts 06_api_basics/solution
```
First-time setup if `.venv`/`node_modules` are missing: run `./setup.ps1`
(Windows) or `bash setup.sh` (macOS/Linux) from the repo root, which sets up
both stacks. Full cross-platform prerequisites are in `SETUP.md`.

Expected baseline: **14 reference tests pass per stack** (4 API + 10 UI).
Solutions pass; skeletons fail with a `TODO` until implemented.

## Adding a new topic / fleshing a stub

Mirror the existing layout exactly. For topic `NN_<slug>`:

Python (`python-playwright/exercises/NN_<slug>/`):
- `EXERCISE.md` — brief (see format below)
- `test_<slug>.py` — skeleton: real scaffolding + `# TODO` lines, ending in
  `pytest.fail("TODO: ...")`
- `solution/test_<slug>_solution.py` — working reference

TS (`ts-playwright/exercises/NN_<slug>/`):
- `EXERCISE.md`
- `<slug>.spec.ts` — skeleton ending in `throw new Error('TODO: ...')`
- `solution/<slug>.spec.ts` — working reference (imports from `../../../src/...`)

Also: add a **worked example** under each stack's `tests/` for the topic's first
case, and tick the status table in the **root `README.md`**.

`EXERCISE.md` format: `# Exercise NN — Title`, then **Goal**, **Target**,
**Steps** (numbered), **Hints**, **Run it** (exact command), **Done when**.

### Remaining stubs and their key APIs
- **07 schema/contract**: Python `jsonschema.validate`; TS `zod`/`ajv`. Validate
  a restful-booker booking's shape, not just values.
- **08 mocking**: `page.route('**/products*', route => route.fulfill({json}))`,
  `route.abort()`, `route.fetch()` then modify. Target DummyJSON; set the route
  before navigation.
- **09 hybrid**: seed via the `booker` API client/fixture, assert in UI; tear
  down in a fixture (`yield`/`use` then delete).
- **10 reporting/CI**: Python `pytest-html` + `--tracing`; TS HTML reporter is
  already on. Add `.github/workflows/*.yml` (`playwright install --with-deps`).
- **11 capstone (Parabank)**: page objects `RegisterPage`, `LoginPage`,
  `AccountsOverviewPage`, `OpenAccountPage`, `TransferFundsPage` + a REST client;
  fixture that registers a unique user per run; verify account/transfer via UI
  **and** the `/services/bank/...` REST API.

## Conventions
- Selectors live in page objects (`framework/pages/`, `src/pages/`); credentials
  and URLs in `config` modules (env-overridable). Tests read as intent only.
- TS tags topics with `@ui` / `@api` in titles for `--grep`; Python uses pytest
  markers (`ui`, `api`, `mocks`, `slow`) declared in `pytest.ini`.
- restful-booker quirks: `POST /auth` → token sent as `Cookie: token=...` for
  update/delete; `DELETE` returns **201**; `/ping` returns **201**.
