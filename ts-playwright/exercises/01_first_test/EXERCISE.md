# Exercise 01 — Your first test

**Goal:** get the runner working and write a first assertion against SauceDemo.

**Target:** https://www.saucedemo.com (set as `baseURL` in the config)

## Steps
1. Navigate to `/`.
2. Assert the page title is `Swag Labs`.
3. Assert the login button (`#login-button`) is visible.

## Hints
- `await page.goto('/')`, `await expect(page).toHaveTitle(...)`.
- Web-first assertions auto-wait — no manual sleeps.

## Run it
```bash
npx playwright test -c playwright.exercises.config.ts 01_first_test/first-test.spec.ts
```

## Done when
The test passes (remove the failing TODO line).

Peek at `solution/` only after you've tried.
