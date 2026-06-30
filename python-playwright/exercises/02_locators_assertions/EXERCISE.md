# Exercise 02 — Locators & web-first assertions

**Goal:** drive the login form and assert different outcomes.

**Target:** https://www.saucedemo.com

## Steps
1. Write a test that logs in as `locked_out_user` / `secret_sauce` and asserts the
   error banner (`[data-test="error"]`) contains `locked out`.
2. Write a test that clicks login with **empty** fields and asserts the error
   contains `Username is required`.

## Hints
- `page.locator("#user-name").fill(...)`, `.click()`.
- Prefer `expect(locator).to_contain_text(...)` over reading `.inner_text()` —
  it auto-waits and retries.
- Credentials live in `framework.config` (`SAUCE_USERS`, `SAUCE_PASSWORD`).

## Run it
```bash
pytest exercises/02_locators_assertions/test_login_states.py
```

## Done when
Both tests pass.
