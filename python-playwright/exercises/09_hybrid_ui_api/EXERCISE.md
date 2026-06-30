# Exercise 09 — Hybrid UI + API (seed then verify)  🔜 (stub)

**Goal:** use the API to set up state fast, then verify behaviour through the UI
(a very common real-world pattern that keeps tests fast and reliable).

## Outline
1. Via the API, create a record (e.g. a restful-booker booking).
2. Open the UI and confirm the created data is reflected
   (or drive a UI action and confirm it via the API).
3. Tear down via the API in a fixture (`yield` then delete).

## Hints
- Reuse the `booker` client fixture for setup/teardown.
- Setup-by-API + assert-by-UI avoids slow UI-only data creation.

> This is a stub — implement it as practice (or ask me to flesh it out).
