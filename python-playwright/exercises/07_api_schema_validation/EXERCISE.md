# Exercise 07 — API schema / contract validation  🔜 (stub)

**Goal:** assert the *shape* of API responses, not just values, so you catch
breaking contract changes.

**Target:** https://restful-booker.herokuapp.com

## Outline
1. Define a JSON Schema for a booking (`firstname`, `lastname`, `totalprice`,
   `depositpaid`, `bookingdates.checkin/checkout`, `additionalneeds`).
2. `GET /booking/{id}` and validate the body with the `jsonschema` package
   (already in `requirements.txt`): `jsonschema.validate(instance, schema)`.
3. Validate the `GET /booking` list returns an array of `{ "bookingid": int }`.

## Hints
- `from jsonschema import validate, ValidationError`.
- Keep schemas in a `schemas/` module so they're reusable.

> This is a stub — implement it as practice (or ask me to flesh it out).
