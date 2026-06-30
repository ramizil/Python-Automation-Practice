# Exercise 12 — Layered framework architecture

**Goal:** feel the difference between a *page object* (interaction primitive) and
a *business step* (Layer 2) by building a small steps layer yourself, then
writing a Layer-3 test that reads like a spec.

**Target:** https://www.saucedemo.com

## Background (read `ARCHITECTURE.md` at the repo root)
A real framework is layered:
1. **Infrastructure** — product-agnostic (config, logging, `BaseApiClient`
   auth/logging interceptor). See `src/core/`.
2. **Business steps** — per-product reusable workflows. See
   `src/products/saucedemo/steps.ts` (`SauceDemoSteps`).
3. **Tests** — specific flows that only call steps and assert.

Compare the worked examples:
- `tests/ui/layered-architecture.spec.ts` (UI via `SauceDemoSteps`)
- `tests/api/layered-steps.spec.ts` (API via `BaseApiClient` → `BookerApiClient`
  → `BookerSteps`)

## Steps
1. In the skeleton, finish the `ShopSteps` class (a Layer-2 steps object) that
   composes the `LoginPage` and `InventoryPage` page objects:
   - `loginAs(userKey = 'standard')` — open the site and log in with
     `SAUCE_USERS[userKey]` / `SAUCE_PASSWORD`.
   - `addItems(names)` — add each product name to the cart.
2. Finish the test (Layer 3) so it logs in as standard, adds two items, and
   asserts the cart count is 2 — **using only `ShopSteps`** (no raw locators).

## Hints
- `InventoryPage.addItemToCart(name)` and `InventoryPage.cartCount()` already
  exist — your step composes them.
- Have each step `return this` so calls chain, like the real `SauceDemoSteps`.
- The point: selectors live in page objects, workflows in steps, intent in tests.

## Run it
```bash
npx playwright test -c playwright.exercises.config.ts 12_layered_architecture/build-steps.spec.ts
```

## Done when
The test passes and its body contains **no locators** — only `ShopSteps` calls
and an assertion.

Peek at `solution/` only after you've tried.
