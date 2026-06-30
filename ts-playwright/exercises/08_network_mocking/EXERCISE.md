# Exercise 08 — Network mocking & interception

**Goal:** control the backend a UI depends on so you can test edge cases
(empty states, errors, slow responses) **deterministically**, without waiting for
the real server to misbehave.

**Target:** a tiny built-in app (`src/mockApp.ts` → `PRODUCTS_APP_HTML`) that
fetches `https://dummyjson.com/products` and renders product titles.

## Why this matters (the concept)
Real backends are hard to push into edge cases on demand. You intercept the
request in the browser instead. `page.route(urlGlob, handler)` registers an
interceptor for every matching request the page makes; inside the handler you
choose the outcome:

| You want to test... | Use |
|---|---|
| A specific response (stub the backend) | `route.fulfill({ json, status })` |
| A network/connection failure | `route.abort()` |
| A server error | `route.fulfill({ status: 500 })` |
| A tweak of the *real* data | `const r = await route.fetch()` → edit → `route.fulfill({ json })` |

> **CORS note:** the app fetches a cross-origin URL, so when you *fulfill* with
> your own data include `headers: { 'Access-Control-Allow-Origin': '*' }`.

## Steps
1. `await page.route('**/products*', handler)` to **stub** exactly two fake
   products, then `await page.setContent(PRODUCTS_APP_HTML)`, click `#load`, and
   assert `.product` has count 2 with your titles.
2. In a second test, fulfill with `{ status: 500 }` (or `route.abort()`) and
   assert `#error` is visible and there are 0 `.product` items.
3. **Bonus:** pass-through + modify — `await route.fetch()`, `unshift` your own
   first product, `route.fulfill({ json })`, and assert it appears first.

## Hints
- Register routes **before** the click that triggers the fetch.
- `route.fulfill({ json })` sets the body and JSON content-type for you.
- `await expect(page.locator('.product')).toHaveCount(2)` auto-waits for you.

## Run it
```bash
npx playwright test -c playwright.exercises.config.ts 08_network_mocking/products-mock.spec.ts
```

## Done when
The stub renders 2 products and the error case reveals `#error`.

Peek at `solution/` only after you've tried.
