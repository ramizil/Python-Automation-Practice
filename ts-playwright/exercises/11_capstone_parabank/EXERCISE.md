# Exercise 11 — Capstone: Parabank end-to-end (UI + API)

**Goal:** combine everything — layered architecture, a per-run unique user, and
the **hybrid pattern** (drive one channel, verify in the other) — into one
realistic bank flow.

**Target:** https://parabank.parasoft.com/parabank (a public demo bank with both
a UI **and** a REST API over the same data — the only target where a true hybrid
flow is possible).

## The hybrid pattern (topic 09, folded in here)
Real suites stay fast and reliable by mixing channels: set up/verify via the API,
drive behaviour via the UI. You'll open an account and transfer funds in the
browser, then assert the new account and transaction exist via the REST API.

## What the framework gives you
- `new ParabankSteps(page)` (Layer 2): `openSavingsAccount(): Promise<string>`,
  `transfer(amount, toAccount): Promise<string>`, `overviewAccountIds()`.
- `new ParabankApiClient(parabankRequest)` (Layer 2 on Layer-1 `BaseApiClient`):
  `accounts(customerId)`, `account(id)`, `transactions(id)`.
- Fixtures (from `src/fixtures.ts`):
  - `parabankUser` — registers a brand-new customer (unique per run), logs the
    browser in; exposes `.username`, `.password`, `.customerId`.
  - `parabankRequest` — an API context based at the bank's REST root.
  - `page` — already logged in.

## Steps
1. Read starting accounts via the API (`api.accounts(customerId)`); assert ≥ 1.
2. **Drive UI:** `steps.openSavingsAccount()` → capture the new id.
3. **Verify by API:** the list grew by one, the new id is present, and
   `(await api.account(Number(newId))).type === 'SAVINGS'`.
4. **Drive UI:** `steps.transfer(25, newId)` → expect `'Transfer Complete!'`.
5. **Verify by API:** `api.transactions(Number(newId))` has ≥ 1 entry.

## Run it
```bash
npx playwright test -c playwright.exercises.config.ts 11_capstone_parabank/capstone.spec.ts
```
> Parabank is a public demo and can be slow or reset — tagged `@capstone`/`@slow`
> and excluded from the fast/CI run. Re-run if the site is having a moment.

## Done when
The flow passes: every UI action is confirmed through the API.

Peek at `solution/` only after you've tried.
