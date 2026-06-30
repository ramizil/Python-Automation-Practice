# Exercise 11 — Capstone: Parabank end-to-end (UI + API)

**Goal:** combine everything — layered architecture, a per-run unique user,
schema validation, and the **hybrid pattern** (drive one channel, verify in the
other) — into one realistic bank flow.

**Target:** https://parabank.parasoft.com/parabank (a public demo bank with both
a UI **and** a REST API over the same data — the only target where a true hybrid
flow is possible).

## The hybrid pattern (topic 09, folded in here)
Real suites stay fast and reliable by mixing channels:
- **Set up / tear down via the API** (fast, no clicking).
- **Drive the behaviour under test via the UI**, then **verify the result via
  the API** (or vice-versa).

You'll *open an account and transfer funds in the browser*, then *assert the new
account and transaction exist via the REST API*.

## What the framework gives you
- `ParabankSteps(page)` (Layer 2): `open_savings_account() -> str`,
  `transfer(amount, to_account) -> str`, `overview_account_ids()`.
- `ParabankApiClient(parabank_request)` (Layer 2 on the Layer-1 `BaseApiClient`):
  `accounts(customer_id)`, `account(id)`, `transactions(id)`.
- Fixtures (from `conftest.py`):
  - `parabank_user` — registers a brand-new customer (unique per run) and logs
    the browser in; exposes `.username`, `.password`, `.customer_id`.
  - `parabank_request` — an API context based at the bank's REST root.
  - `page` — already logged in (registration happens in the fixture).
- Schemas: `framework.schemas.parabank.ACCOUNTS_LIST_SCHEMA`,
  `TRANSACTIONS_LIST_SCHEMA`.

## Steps
1. Read the starting accounts via the API (`api.accounts(customer_id)`); a fresh
   user has one CHECKING account. Optionally `validate(...)` against
   `ACCOUNTS_LIST_SCHEMA`.
2. **Drive UI:** `steps.open_savings_account()` → capture the new id.
3. **Verify by API:** the account list grew by one, the new id is present, and
   `api.account(int(new_id))["type"] == "SAVINGS"`.
4. **Drive UI:** `steps.transfer(amount=25, to_account=new_id)` →
   assert `"Transfer Complete!"` in the result.
5. **Verify by API:** `api.transactions(int(new_id))` has at least one entry.

## Run it
```bash
pytest exercises/11_capstone_parabank/test_capstone.py -m capstone
```
> Parabank is a public demo and can be slow or reset — these tests are marked
> `capstone`/`slow` and are excluded from the fast/CI run. Re-run if the site is
> having a moment.

## Done when
The flow passes: every UI action is confirmed through the API.

Peek at `solution/` only after you've tried.
