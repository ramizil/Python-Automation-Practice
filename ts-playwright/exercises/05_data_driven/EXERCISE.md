# Exercise 05 — Data-driven tests

**Goal:** run the same logic over a table of inputs by looping `test(...)`.

## Steps
1. Build a `cases` array of `{ user, canLogin }` for all four SauceDemo users.
2. Loop and generate a test per case.
3. Assert `Products` for users who can log in; `locked out` error for the locked user.

## Hints
- In Playwright you data-drive by calling `test()` inside a `for` loop.
- Give each generated test a unique title (include the username).

## Run it
```bash
npx playwright test -c playwright.exercises.config.ts 05_data_driven/users.spec.ts
```

## Done when
All four generated tests pass.
