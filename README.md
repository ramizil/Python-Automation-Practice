# Python + TypeScript Playwright Automation Practice

A hands-on course for building **UI + API test automation frameworks from scratch**
with Playwright, in **two mirrored stacks**:

| Stack | Runner | Folder |
|-------|--------|--------|
| Python + Playwright | `pytest` (+ `pytest-playwright`) | [`python-playwright/`](python-playwright/) |
| TypeScript + Playwright | `@playwright/test` | [`ts-playwright/`](ts-playwright/) |

Every topic is implemented the same way in both languages, so you can compare the
idioms side by side while learning the same testing concepts.

## What you'll practice

- Web-first **UI testing** (locators, assertions, Page Object Model, e2e flows)
- **API testing** (auth tokens, CRUD, schema/contract validation)
- **Mocking & network interception** (stub/modify/fail backend responses)
- **Hybrid** tests (seed state via API, verify in the UI)
- **Reporting + CI** (HTML/Allure reports, GitHub Actions)
- A **capstone**: end-to-end bank flow (UI + API)

## Target applications (free, public, automation-friendly)

| Purpose | App | URL |
|---------|-----|-----|
| Dummy store (UI) | SauceDemo | https://www.saucedemo.com |
| Clean REST API (auth + CRUD) | restful-booker | https://restful-booker.herokuapp.com |
| Store API + mocking | DummyJSON | https://dummyjson.com |
| Dummy bank (capstone) | Parabank | https://parabank.parasoft.com |

> These are shared public demo sites. Treat their data as ephemeral and don't run
> destructive load against them.

## Learning path

Each exercise lives under `exercises/NN_topic/` in **both** stacks and contains:

- `EXERCISE.md` — the brief: goal, steps, hints, and "done when" criteria
- a **skeleton** test with `TODO`s for you to implement
- a **reference solution** you can peek at when stuck

The `tests/` folder in each stack holds **worked reference examples** (read & run
these first for each new topic), and the framework code (`pages/`, `api/`,
fixtures) is the scaffolding you'll extend.

| #  | Topic | Target | Status |
|----|-------|--------|--------|
| 01 | First test & runner setup | SauceDemo | ✅ ready |
| 02 | Locators & web-first assertions | SauceDemo | ✅ ready |
| 03 | Page Object Model | SauceDemo | ✅ ready |
| 04 | End-to-end checkout flow | SauceDemo | ✅ ready |
| 05 | Data-driven tests | SauceDemo | ✅ ready |
| 06 | API testing basics (auth + CRUD) | restful-booker | ✅ ready |
| 07 | API schema / contract validation | restful-booker | ✅ ready |
| 08 | Network mocking & interception | DummyJSON | ✅ ready |
| 09 | Hybrid UI + API (seed then verify) | restful-booker + UI | 🔜 stub |
| 10 | Reporting, quality gates & CI | both | ✅ ready |
| 11 | Capstone: bank flow end-to-end | Parabank | 🔜 stub |
| 12 | Layered framework architecture | SauceDemo + restful-booker | ✅ ready |

## Quick start

Runs on **Windows, macOS, and Linux**. Needs Git, Python 3.10+, and Node.js 18+.
Full prerequisites and per-OS instructions are in **[SETUP.md](SETUP.md)**.
Prefer a visual guide? Open **[instructions.html](instructions.html)** in a browser.

One cross-platform installer (only needs Python 3.10+) sets up **both** stacks
— venv + pytest + Playwright (Python) and npm + Playwright (TypeScript), browsers
included — from the repo root:

```bash
python install.py        # Windows
python3 install.py       # macOS / Linux
```

Flags: `--python-only`, `--ts-only`, `--all-browsers`. OS-native wrappers
`./setup.ps1` (Windows) and `bash setup.sh` (macOS/Linux) do the same thing.

Then run the suites:

```bash
# Python  (from python-playwright/, venv activated)
pytest
# TypeScript  (from ts-playwright/)
npx playwright test
```

Or set up manually:

### Python stack
```bash
cd python-playwright
python -m venv .venv                 # python3 on macOS/Linux
source .venv/bin/activate            # Windows: .\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
playwright install                   # download browsers (first time)
pytest
```

### TypeScript stack
```bash
cd ts-playwright
npm install
npx playwright install               # download browsers (first time)
npx playwright test
```

See each stack's own `README.md` for details and how to run individual exercises.

## Quality gates & CI (topic 10)

The repo is wired like a real project:

```bash
# Python clean-code gates (from python-playwright/, venv activated)
pip install -r requirements-dev.txt
ruff format --check .     # formatting
ruff check .              # linting
mypy framework            # type checking
pytest tests --html=report.html --self-contained-html   # HTML report

# Pre-commit (run from repo root) formats/lints before every commit
pip install pre-commit && pre-commit install
```

- `python-playwright/pyproject.toml` — ruff + mypy config
- `.pre-commit-config.yaml` — git hooks
- `.github/workflows/ci.yml` — runs **lint**, **python-tests**, and **ts-tests**
  on every push/PR and uploads reports as artifacts

## Framework architecture (topic 12)

Topics 01–08 use a flat Page Object Model (good while learning). **Topic 12**
shows the 3-layer design real frameworks use — **infrastructure → business steps
→ tests** — with a shared `core/` (config, logging, `BaseApiClient` auth/logging
interceptor) and per-product `products/` packages. Full write-up in
**[ARCHITECTURE.md](ARCHITECTURE.md)**.

## How to work through it

1. Read the topic's worked example in `tests/`.
2. Open `exercises/NN_topic/EXERCISE.md` and implement the skeleton.
3. Run just that exercise (commands are in each `EXERCISE.md`).
4. Compare against the reference solution.
5. Do the topic in the **other** language to cement the concept.

Happy testing!
