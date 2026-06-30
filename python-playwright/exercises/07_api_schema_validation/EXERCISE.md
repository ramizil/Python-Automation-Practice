# Exercise 07 — API schema / contract validation

**Goal:** assert the *shape* of API responses, not just one value, so you catch
breaking contract changes (renamed fields, wrong types) before your users do.

**Target:** https://restful-booker.herokuapp.com

## Why this matters (the concept)
A normal assertion like `assert body["firstname"] == "Grace"` only proves that
**one record** looks right **today**. If the backend renames `totalprice` to
`price`, or starts returning it as the string `"150"` instead of the number
`150`, your value checks might still pass (or fail for the wrong reason) while
real clients break.

A **JSON Schema** describes the *structure* data must have:
- `type` — `"string"`, `"number"`, `"boolean"`, `"object"`, `"array"`...
- `required` — which keys MUST be present
- nested `properties` — the shape of sub-objects (e.g. `bookingdates`)
- `items` — the shape of every element in an array

`jsonschema.validate(instance, schema)` walks the data against the schema and
raises `ValidationError` on the first mismatch. That single failing test then
tells you *exactly* which part of the contract broke.

## Steps
1. Import the ready-made schemas:
   `from framework.schemas.booking import BOOKING_SCHEMA, BOOKING_ID_LIST_SCHEMA`.
2. Create a booking with the `booker` fixture, `GET` it back, and
   `validate(instance=body, schema=BOOKING_SCHEMA)`.
3. `GET /booking` (the list) via `booker_request` and validate it against
   `BOOKING_ID_LIST_SCHEMA`.
4. Prove the schema has teeth: build a *broken* booking (e.g. `totalprice` as a
   string, or delete `lastname`) and assert it raises `ValidationError`
   (`with pytest.raises(ValidationError): ...`).

## Hints
- `from jsonschema import validate, ValidationError`.
- `validate(...)` returns `None` on success and **raises** on failure — there is
  nothing to assert on the happy path; reaching the next line means it passed.
- Open `framework/schemas/booking.py` and read the comments — then try tightening
  it (e.g. set `additionalProperties: False`) and see what breaks.

## Run it
```bash
pytest exercises/07_api_schema_validation/test_booking_schema.py
```

## Done when
Both happy-path validations pass and the broken-shape case raises
`ValidationError`.

Peek at `solution/` only after you've tried.
