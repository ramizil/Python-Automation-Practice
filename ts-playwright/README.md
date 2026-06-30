# TypeScript + Playwright stack

Playwright with its built-in test runner **`@playwright/test`**.

## Setup
```bash
cd ts-playwright
npm install
npx playwright install            # one-time: download browser binaries
```

## Run
```bash
npx playwright test                       # the worked reference suite (tests/)
npx playwright test --grep @ui            # only UI tests (tagged in titles)
npx playwright test --grep @api           # only API tests
npx playwright test tests/ui/checkout.spec.ts
npx playwright test --headed              # watch the browser
npm run report                            # open the HTML report
```

`testDir` is `./tests`, so a plain run executes only the reference examples.

## Layout
```
ts-playwright/
├─ playwright.config.ts            # baseURL=SauceDemo, reporters, trace on fail
├─ playwright.exercises.config.ts  # same, but testDir=./exercises
├─ src/                            # the reusable framework you extend
│  ├─ config.ts                    # URLs + demo credentials (env-overridable)
│  ├─ fixtures.ts                  # custom fixtures: page objects + booker client
│  ├─ pages/                       # SauceDemo page objects (POM)
│  └─ api/BookerClient.ts          # restful-booker API client
├─ tests/                          # worked reference examples (read first)
│  ├─ ui/  └─ api/
└─ exercises/                      # your practice: brief + skeleton + solution
   ├─ 01_first_test/ … 06_api_basics/    # ready
   └─ 07_…/ … 11_capstone_parabank/      # stubs to grow into
```

## Working an exercise
```bash
# 1. read exercises/01_first_test/EXERCISE.md
# 2. implement the skeleton spec, then:
npx playwright test -c playwright.exercises.config.ts 01_first_test/first-test.spec.ts
# (or)  npm run test:exercise -- 01_first_test/first-test.spec.ts
# 3. compare with the reference:
npx playwright test -c playwright.exercises.config.ts 01_first_test/solution
```

## Notes
- Tests use the custom `test`/`expect` from `src/fixtures.ts` to get page objects
  and the `booker` API client injected.
- UI/API are tagged with `@ui` / `@api` in test titles so you can `--grep` them.
- Override any URL with an env var, e.g. `SAUCEDEMO_URL=...`.
