# Exercise 07 — API schema / contract validation

**Goal:** assert the *shape* of API responses, not just one value, so you catch
breaking contract changes (renamed fields, wrong types) before your users do.

**Target:** https://restful-booker.herokuapp.com

## Why this matters (the concept)
`expect(body.firstname).toBe('Grace')` proves **one record** looks right
**today**. If the backend renames `totalprice` to `price`, or returns it as the
string `"150"` instead of the number `150`, that check won't protect real
clients.

A **JSON Schema** describes the *structure* data must have — `type`, `required`
keys, nested `properties`, array `items`. We validate with **Ajv**, the standard
JSON Schema validator for JS/TS. The helper `validateOrThrow(schema, data)`
returns `true` on success and throws (listing every mismatch) on failure.

## Steps
1. Import the schemas + helper:
   `import { bookingSchema, bookingIdListSchema, validateOrThrow } from '../../src/schemas/booking';`
2. Create a booking with the `booker` fixture, `getBooking(id)`, and
   `expect(validateOrThrow(bookingSchema, body)).toBe(true)`.
3. `GET /booking` (the list) via `bookerRequest` and validate it against
   `bookingIdListSchema`.
4. Prove the schema has teeth: build a *broken* booking (e.g. `totalprice` as a
   string, or delete `lastname`) and
   `expect(() => validateOrThrow(bookingSchema, broken)).toThrow()`.

## Hints
- `validateOrThrow` throws on failure, so the happy path has nothing else to
  assert — reaching the next line means it passed.
- Open `src/schemas/booking.ts` and try `additionalProperties: false` to make it
  strict, then see what fails.

## Run it
```bash
npx playwright test -c playwright.exercises.config.ts 07_api_schema_validation/booking-schema.spec.ts
```

## Done when
Both happy-path validations pass and the broken-shape case throws.

Peek at `solution/` only after you've tried.
