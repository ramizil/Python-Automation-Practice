# Framework architecture — the 3 layers

Topics 01–08 use a deliberately flat **Page Object Model**: page objects/API
clients + tests. That's the right amount of structure while you're learning the
APIs. But a real, multi-product automation framework (the kind you build at work)
is usually organised into **three layers**, and that's what **topic 12**
demonstrates.

```
┌─────────────────────────────────────────────────────────────┐
│  LAYER 3 — TESTS            specific flows, read like specs   │
│  "log in as standard, buy 2 items, expect order complete"     │
│  no locators, no HTTP plumbing — only business steps + asserts│
└───────────────▲─────────────────────────────────────────────┘
                │ calls
┌───────────────┴─────────────────────────────────────────────┐
│  LAYER 2 — BUSINESS STEPS    per-product reusable workflows   │
│  SauceDemoSteps.login_as(), .checkout(...)                    │
│  BookerSteps.create_paid_booking()                            │
│  composes page objects (UI) and API clients (API)             │
└───────────────▲─────────────────────────────────────────────┘
                │ built on
┌───────────────┴─────────────────────────────────────────────┐
│  LAYER 1 — INFRASTRUCTURE    product-agnostic, shared by ALL  │
│  browser/context lifecycle, config, logging,                  │
│  BaseApiClient (auth + request/response logging interceptor)  │
│  reused by every product: saucedemo, booker, parabank, ...    │
└───────────────────────────────────────────────────────────────┘
```

This mirrors a layered Java framework where **infrastructure** is shared across
products (ordering, customer-services, billing), **business steps** are the
common actions for one product, and **tests** are the specific flows.

## Layer 1 — Infrastructure (`framework/core/`, `src/core/`)
Product-agnostic plumbing every product reuses:
- **Config** — env-driven URLs/credentials (`config`).
- **Driver/context lifecycle** — Playwright browser & context, the
  `IGNORE_HTTPS_ERRORS` flag, `base_url` (pytest fixtures / Playwright fixtures).
- **Logging** — `get_logger(name)` / `getLogger(name)`.
- **`BaseApiClient`** — wraps Playwright's `APIRequestContext` with a single
  `call()` entry point that **injects auth + JSON headers and logs every
  request/response**. This is the equivalent of a Java **login/HTTP
  interceptor**: cross-cutting behaviour lives in one place instead of being
  repeated in every client.

> **UI "login interceptor" analog:** reuse a logged-in session via Playwright
> `storage_state` (log in once, replay the cookies) and/or `context.on('request')`
> for logging — the browser equivalent of an auth/logging interceptor.

## Layer 2 — Business steps (`framework/products/<product>/`, `src/products/<product>/`)
One package **per product** (the analog of ordering / billing / customer
services). The **Parabank** product (topic 11 capstone) is the fully
self-contained example: `products/parabank/` holds its own `pages`, a
`ParabankApiClient` (extends the Layer-1 `BaseApiClient`), `steps`, and a `data`
factory. Each product package contains:
- **pages** — page objects: locators + atomic interactions (the interaction
  primitives). *For SauceDemo the page objects already live in `framework/pages`
  / `src/pages` and the steps layer composes them; Parabank keeps its own pages
  inside its product package — the cleaner greenfield layout.*
- **client** — a product API client extending `BaseApiClient`
  (e.g. `BookerApiClient`).
- **steps** — **business workflows** that read like product actions
  (`login_as`, `checkout`, `create_paid_booking`). Steps orchestrate pages/clients;
  they are where "what a user does" lives, decoupled from "how" (selectors,
  endpoints).

## Layer 3 — Tests (`tests/`)
Specific flows that **only call steps and assert outcomes**. No selectors, no
status-code plumbing. A test should read like a sentence a product owner would
recognise.

## Why bother (the payoff)
- **Change isolation:** a selector change touches one page object; an auth change
  touches one `BaseApiClient`; neither ripples into tests.
- **Reuse across products:** Layer 1 is written once; every product builds on it.
- **Readable tests:** Layer 3 documents behaviour, not mechanics.
- **Onboarding:** new flows are assembled from existing steps.

See **topic 12** (`exercises/12_layered_architecture/`) for a hands-on exercise
and the worked examples in each stack's `tests/` (`*layered*`).
