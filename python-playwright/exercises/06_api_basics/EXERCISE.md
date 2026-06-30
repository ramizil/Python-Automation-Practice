# Exercise 06 — API testing basics

**Goal:** test a REST API directly (no browser) with Playwright's request context.

**Target:** https://restful-booker.herokuapp.com
([docs](https://restful-booker.herokuapp.com/apidoc/index.html))

## Steps
1. Create a booking (`POST /booking`) and assert status `200` and that the
   returned `booking.firstname` matches what you sent.
2. Read it back (`GET /booking/{id}`) and assert a field.
3. Authenticate (`POST /auth`) to get a token, then **update** the booking
   (`PUT /booking/{id}`) and assert the change.
4. **Delete** it (`DELETE /booking/{id}`) — remember restful-booker returns
   `201` on delete — then assert a follow-up GET returns `404`.

## Hints
- Use the `booker` fixture (a ready `BookerClient`) and `config.BOOKER_ADMIN`.
- Or use the raw `booker_request` fixture to call endpoints yourself.
- Update/delete need the auth cookie — `BookerClient.auth(...)` handles it.

## Run it
```bash
pytest exercises/06_api_basics/test_booking_crud.py
```

## Done when
The CRUD lifecycle test passes.
