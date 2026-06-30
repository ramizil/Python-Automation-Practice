# Exercise 07 — API schema / contract validation  🔜 (stub)

**Goal:** assert the *shape* of API responses to catch breaking contract changes.

**Target:** https://restful-booker.herokuapp.com

## Outline
1. Define the expected booking shape. Options in TS:
   - hand-rolled type guards, or
   - a runtime validator like `zod` (`npm i -D zod`) or `ajv` for JSON Schema.
2. `GET /booking/{id}` and validate the parsed body against the schema.
3. Validate `GET /booking` returns an array of `{ bookingid: number }`.

## Hints
- `zod`: `const Booking = z.object({ firstname: z.string(), ... }); Booking.parse(json)`.

> Stub — implement it as practice (or ask me to flesh it out).
