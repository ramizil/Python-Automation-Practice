# Exercise 03 — Page Object Model

**Goal:** build your own page object class, then use it in the test.

## Steps
1. Complete the `MyLoginPage` class in `pom.spec.ts` (locators + `open()` + `login()`).
2. Use it to log in as the standard user and assert `.title` reads `Products`.

## Why
Page objects keep selectors in one place. Compare with `src/pages/LoginPage.ts`.

## Run it
```bash
npx playwright test -c playwright.exercises.config.ts 03_page_object_model/pom.spec.ts
```

## Done when
The POM-based test passes.
