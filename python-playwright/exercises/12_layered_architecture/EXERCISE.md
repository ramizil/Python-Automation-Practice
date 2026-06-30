# Exercise 12 — Layered framework architecture

**Goal:** feel the difference between a *page object* (interaction primitive) and
a *business step* (Layer 2) by building a small steps layer yourself, then
writing a Layer-3 test that reads like a spec.

**Target:** https://www.saucedemo.com

## Background (read `ARCHITECTURE.md` at the repo root)
A real framework is layered:
1. **Infrastructure** — product-agnostic (config, logging, browser lifecycle,
   `BaseApiClient` auth/logging interceptor). See `framework/core/`.
2. **Business steps** — per-product reusable workflows. See
   `framework/products/saucedemo/steps.py` (`SauceDemoSteps`).
3. **Tests** — specific flows that only call steps and assert.

Compare the worked examples to see it in action:
- `tests/ui/test_layered_architecture.py` (UI via `SauceDemoSteps`)
- `tests/api/test_layered_steps.py` (API via `BaseApiClient` → `BookerApiClient`
  → `BookerSteps`)

## Steps
1. In the skeleton, finish the `ShopSteps` class (a Layer-2 steps object) that
   composes the `LoginPage` and `InventoryPage` page objects:
   - `login_as(user_key="standard")` — open the site and log in using
     `config.SAUCE_USERS[user_key]` / `config.SAUCE_PASSWORD`.
   - `add_items(names)` — add each product name to the cart.
2. Finish `test_layered_flow` (Layer 3) so it: logs in as standard, adds two
   items, and asserts the cart count is 2 — **using only `ShopSteps`** (no raw
   locators in the test).

## Hints
- `InventoryPage.add_item_to_cart(name)` and `InventoryPage.cart_count()` already
  exist — your step just composes them.
- Have each step `return self` so calls can chain, like the real
  `SauceDemoSteps`.
- The point: selectors live in page objects, workflows live in steps, intent
  lives in the test.

## Run it
```bash
pytest exercises/12_layered_architecture/test_build_steps.py
```

## Done when
The test passes and your test body contains **no locators** — only `ShopSteps`
calls and an assertion.

Peek at `solution/` only after you've tried.
