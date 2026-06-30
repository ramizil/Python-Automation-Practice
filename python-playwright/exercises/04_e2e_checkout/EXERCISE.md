# Exercise 04 — End-to-end checkout

**Goal:** automate a full purchase of **two** items using the framework page objects.

**Target:** https://www.saucedemo.com

## Steps
1. Log in as the standard user (use `framework.pages.login_page.LoginPage`).
2. Add **two** items to the cart:
   `Sauce Labs Backpack` and `Sauce Labs Bike Light`.
3. Assert the cart badge shows `2`.
4. Go to the cart and assert both item names are present.
5. Check out, fill the information form, finish.
6. Assert the confirmation header is `Thank you for your order!`.

## Hints
- Reuse `InventoryPage`, `CartPage`, `CheckoutPage` from `framework/pages/`.
- Compare with the single-item worked example in `tests/ui/test_checkout.py`.

## Run it
```bash
pytest exercises/04_e2e_checkout/test_checkout_two_items.py
```

## Done when
The two-item purchase test passes.
