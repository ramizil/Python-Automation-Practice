# Exercise 01 — Your first test

**Goal:** get the runner working and write a first assertion against SauceDemo.

**Target:** https://www.saucedemo.com

## Steps
1. Open the `base_url` (injected by the `base_url` fixture).
2. Assert the page title is `Swag Labs`.
3. Assert the login button (`#login-button`) is visible.

## Hints
- Use the `page` and `base_url` fixtures (already provided by the framework).
- Web-first assertions: `from playwright.sync_api import expect` then
  `expect(page).to_have_title(...)` and `expect(locator).to_be_visible()`.

## Run it
```bash
pytest exercises/01_first_test/test_first_test.py
```

## Done when
The test passes (and you removed the `pytest.fail` placeholder).

Peek at `solution/` only after you've tried.
