# Exercise 08 — Network mocking & interception  🔜 (stub)

**Goal:** control the backend a UI depends on to test edge cases deterministically.

**Target:** https://dummyjson.com (docs: https://dummyjson.com/docs)

## Outline
1. Open a page that fetches `https://dummyjson.com/products`.
2. `await page.route('**/products*', route => route.fulfill({ json: {...} }))`
   to stub 2 fake products; assert the UI renders 2 items.
3. Return `500` (`route.fulfill({ status: 500 })`) or `route.abort()` and assert
   the UI's error state.
4. Bonus: `const resp = await route.fetch(); const body = await resp.json();`
   tweak it, then `route.fulfill({ response: resp, json: body })`.

## Hints
- Set up `page.route(...)` **before** the navigation/action that triggers the request.

> Stub — implement it as practice (or ask me to flesh it out).
