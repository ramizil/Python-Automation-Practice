# Exercise 11 — Capstone: bank flow end-to-end  🔜 (stub)

**Goal:** combine everything against a realistic banking app.

**Target:** https://parabank.parasoft.com/parabank
(REST docs: https://parabank.parasoft.com/parabank/services/bank/...)

## Outline (build it like a mini real project)
1. **Register** a new user via the UI (unique username each run).
2. **Log in**, capture the account id.
3. **Open a new account** (savings) — verify via UI *and* the REST API
   (`/services/bank/...`).
4. **Transfer funds** between accounts; assert the new balances.
5. Add **schema validation** on the API responses (exercise 07).
6. Add **a mock** for one external call to test an error path (exercise 08).
7. Wire it into **CI with reporting** (exercise 10).

## Suggested structure
- Page objects: `RegisterPage`, `LoginPage`, `AccountsOverviewPage`,
  `OpenAccountPage`, `TransferFundsPage`.
- An API client for the ParaBank REST services.
- A fixture that registers a fresh user per test run.

> This is the capstone stub — tackle it once 01-10 feel comfortable, or ask me
> to scaffold it.
