# Exercise 04 — End-to-end checkout

**Goal:** automate a full purchase of **two** items using the fixture page objects.

## Steps
1. Log in as the standard user.
2. Add `Sauce Labs Backpack` and `Sauce Labs Bike Light`; assert cart count is 2.
3. Go to the cart, assert both names present.
4. Check out, fill the form, finish.
5. Assert the confirmation header is `Thank you for your order!`.

## Hints
- Use the `loginPage`, `inventoryPage`, `cartPage`, `checkoutPage` fixtures.
- Compare with the single-item example in `tests/ui/checkout.spec.ts`.

## Run it
```bash
npx playwright test -c playwright.exercises.config.ts 04_e2e_checkout/checkout-two.spec.ts
```

## Done when
The two-item purchase passes.
