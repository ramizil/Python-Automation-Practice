# Python + Playwright stack

Playwright driven by **pytest** (via `pytest-playwright`).

## Setup
```bash
cd python-playwright
python -m venv .venv
.venv\Scripts\activate          # Windows  (macOS/Linux: source .venv/bin/activate)
pip install -r requirements.txt
playwright install               # one-time: download browser binaries
```

## Run
```bash
pytest                                   # the worked reference suite (tests/)
pytest -m ui                             # only UI tests
pytest -m api                            # only API tests
pytest tests/ui/test_checkout.py         # a single file
pytest --headed                          # watch the browser
pytest --headed --slowmo 500             # ...slowed down
```

`pytest.ini` sets `testpaths = tests`, so a plain `pytest` runs only the
reference examples. Exercises are run explicitly by path.

## Layout
```
python-playwright/
├─ conftest.py            # fixtures: base_url, booker_request, booker
├─ pytest.ini
├─ framework/             # the reusable framework you extend
│  ├─ config.py           # URLs + demo credentials (env-overridable)
│  ├─ pages/              # SauceDemo page objects (POM)
│  └─ api/booker_client.py# restful-booker API client (Playwright request)
├─ tests/                 # worked reference examples (read these first)
│  ├─ ui/                 # SauceDemo UI tests
│  └─ api/                # restful-booker API tests
└─ exercises/             # your practice: brief + skeleton + solution
   ├─ 01_first_test/ … 06_api_basics/      # ready
   └─ 07_…/ … 11_capstone_parabank/        # stubs to grow into
```

## Working an exercise
```bash
# 1. read the brief
#    exercises/01_first_test/EXERCISE.md
# 2. implement the skeleton
pytest exercises/01_first_test/test_first_test.py
# 3. compare with the reference
pytest exercises/01_first_test/solution/
```

## Notes
- Selectors/credentials are centralised in `framework/config.py` and the page
  objects, so tests stay readable.
- Override any URL with an env var or a local `.env`, e.g.
  `SAUCEDEMO_URL=...`, `BOOKER_API_URL=...`.
