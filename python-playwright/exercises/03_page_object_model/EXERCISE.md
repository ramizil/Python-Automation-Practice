# Exercise 03 — Page Object Model

**Goal:** build your own page object instead of using raw selectors in the test.

**Target:** https://www.saucedemo.com

## Steps
1. In `pageobjects.py`, complete the `MyLoginPage` class:
   - locators for username, password, login button, error banner
   - an `open(base_url)` method that navigates and returns `self`
   - a `login(username, password)` method
2. In `test_pom.py`, use `MyLoginPage` to log in as the standard user and assert
   the inventory `.title` reads `Products`.

## Why
Page objects keep selectors in one place and make tests read like user stories.
Compare with `framework/pages/login_page.py`.

## Run it
```bash
pytest exercises/03_page_object_model/test_pom.py
```

## Done when
The POM-based test passes.
