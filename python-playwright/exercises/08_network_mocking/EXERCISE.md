# Exercise 08 — Network mocking & interception  🔜 (stub)

**Goal:** control the backend a UI depends on, so you can test edge cases
(empty states, errors, slow responses) deterministically.

**Target:** https://dummyjson.com (and its docs at https://dummyjson.com/docs)

## Outline
1. Open a page that fetches `https://dummyjson.com/products`.
2. Use `page.route("**/products*", handler)` to **stub** the response with your
   own JSON (e.g. exactly 2 fake products) and assert the UI renders 2 items.
3. **Fail** the request (`route.abort()`) or return `500`
   (`route.fulfill(status=500)`) and assert the UI shows an error state.
4. Bonus: modify a real response — fetch via `route.fetch()`, tweak the JSON,
   then `route.fulfill(response=...)`.

## Hints
- `page.route(url, lambda route: route.fulfill(json={...}))`.
- For a quick UI to drive, you can build a tiny local HTML file that calls the
  API, or intercept on any page that uses fetch/XHR.

> This is a stub — implement it as practice (or ask me to flesh it out).
