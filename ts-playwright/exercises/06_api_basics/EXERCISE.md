# Exercise 06 — API testing basics

**Goal:** test a REST API directly (no browser) with Playwright's request context.

**Target:** https://restful-booker.herokuapp.com
([docs](https://restful-booker.herokuapp.com/apidoc/index.html))

## Steps
1. Create a booking and assert `200` + the returned `booking.firstname`.
2. Read it back and assert a field.
3. Authenticate, then update the booking and assert the change.
4. Delete it (expect `201`), then assert a follow-up GET returns `404`.

## Hints
- Use the `booker` fixture (a `BookerClient`) and `BOOKER_ADMIN` from config.
- Update/delete need auth — `booker.auth(...)` stores the cookie for you.

## Run it
```bash
npx playwright test -c playwright.exercises.config.ts 06_api_basics/booking-crud.spec.ts
```

## Done when
The CRUD lifecycle test passes.
