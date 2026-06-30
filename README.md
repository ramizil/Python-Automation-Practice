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
| 07 | API schema / contract validation | restful-booker | 🔜 stub |
| 08 | Network mocking & interception | DummyJSON | 🔜 stub |
| 09 | Hybrid UI + API (seed then verify) | restful-booker + UI | 🔜 stub |
| 10 | Reporting + GitHub Actions CI | both | 🔜 stub |
| 11 | Capstone: bank flow end-to-end | Parabank | 🔜 stub |

## Quick start

Runs on **Windows, macOS, and Linux**. Needs Git, Python 3.10+, and Node.js 18+.
Full prerequisites and per-OS instructions are in **[SETUP.md](SETUP.md)**.
Prefer a visual guide? Open **[instructions.html](instructions.html)** in a browser.

One-command setup of both stacks from the repo root:

```bash
./setup.ps1        # Windows (PowerShell)
bash setup.sh      # macOS / Linux
```

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

## How to work through it

1. Read the topic's worked example in `tests/`.
2. Open `exercises/NN_topic/EXERCISE.md` and implement the skeleton.
3. Run just that exercise (commands are in each `EXERCISE.md`).
4. Compare against the reference solution.
5. Do the topic in the **other** language to cement the concept.

Happy testing!
