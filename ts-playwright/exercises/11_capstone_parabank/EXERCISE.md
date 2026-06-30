# Exercise 11 — Capstone: bank flow end-to-end  🔜 (stub)

**Goal:** combine everything against a realistic banking app.

**Target:** https://parabank.parasoft.com/parabank

## Outline (build it like a mini real project)
1. **Register** a new user via the UI (unique username each run).
2. **Log in**, capture the account id.
3. **Open a new account** (savings) — verify via UI *and* the REST API.
4. **Transfer funds** between accounts; assert the new balances.
5. Add **schema validation** on API responses (exercise 07).
6. Add **a mock** for one external call to test an error path (exercise 08).
7. Wire it into **CI with reporting** (exercise 10).

## Suggested structure
- Page objects: `RegisterPage`, `LoginPage`, `AccountsOverviewPage`,
  `OpenAccountPage`, `TransferFundsPage` under `src/pages/parabank/`.
- A `ParabankApiClient` under `src/api/`.
- A fixture that registers a fresh user per run.

> Capstone stub — tackle it once 01-10 feel comfortable, or ask me to scaffold it.
