# Exercise 02 — Locators & web-first assertions

**Goal:** drive the login form and assert different outcomes.

## Steps
1. Test that logging in as `locked_out_user` shows an error containing `locked out`.
2. Test that clicking login with **empty** fields shows `Username is required`.

## Hints
- `page.locator('#user-name').fill(...)`, `.click()`.
- `await expect(locator).toContainText(...)` auto-waits.
- Credentials are in `src/config.ts` (`SAUCE_USERS`, `SAUCE_PASSWORD`).

## Run it
```bash
npx playwright test -c playwright.exercises.config.ts 02_locators_assertions/login-states.spec.ts
```

## Done when
Both tests pass.
