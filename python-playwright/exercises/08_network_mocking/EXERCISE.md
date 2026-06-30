# Exercise 08 — Network mocking & interception

**Goal:** control the backend a UI depends on so you can test edge cases
(empty states, errors, slow responses) **deterministically**, without waiting for
the real server to misbehave.

**Target:** a tiny built-in app (`framework.mock_app.PRODUCTS_APP_HTML`) that
fetches `https://dummyjson.com/products` and renders product titles.

## Why this matters (the concept)
Real backends are hard to push into edge cases on demand — how do you make the
products API return *zero* items, or a `500`, exactly when your test runs? You
intercept the request in the browser instead.

`page.route(url_glob, handler)` registers an interceptor for every matching
request the page makes. Inside the handler you choose the outcome:

| You want to test... | Use |
|---|---|
| A specific response (stub the backend) | `route.fulfill(json=..., status=...)` |
| A network/connection failure | `route.abort()` |
| A server error | `route.fulfill(status=500)` |
| A tweak of the *real* data | `resp = route.fetch()` → edit → `route.fulfill(response=resp/json=...)` |

> **CORS note:** the app fetches a cross-origin URL, so when you *fulfill* with
> your own data include the header `{"Access-Control-Allow-Origin": "*"}` (the
> worked example shows this). Real DummyJSON already sends it.

## Steps
1. `page.route("**/products*", handler)` to **stub** the response with exactly
   two fake products, then `page.set_content(PRODUCTS_APP_HTML)`, click `#load`,
   and assert `.product` has count 2 with your titles.
2. In a second test, fulfill with `status=500` (or `route.abort()`) and assert
   `#error` becomes visible and there are 0 `.product` items.
3. **Bonus:** pass-through + modify — `route.fetch()` the real response, insert
   your own first product, `route.fulfill(json=...)`, and assert it appears
   first.

## Hints
- Register routes **before** the click that triggers the fetch.
- `route.fulfill(json={...})` sets the body and JSON content-type for you.
- Web-first assertions wait for you: `expect(page.locator(".product")).to_have_count(2)`.

## Run it
```bash
pytest exercises/08_network_mocking/test_products_mock.py
```

## Done when
The stub renders 2 products and the error case reveals `#error`.

Peek at `solution/` only after you've tried.
