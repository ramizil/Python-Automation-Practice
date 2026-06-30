# Exercise 05 — Data-driven tests

**Goal:** run the same logic over a table of inputs with `@pytest.mark.parametrize`.

**Target:** https://www.saucedemo.com

## Steps
1. Parametrize a test over all four SauceDemo users in `config.SAUCE_USERS`.
2. For users that can log in (`standard`, `problem`, `performance_glitch`), assert
   the inventory `.title` shows `Products`.
3. For `locked_out`, assert the error banner contains `locked out`.

## Hints
- `@pytest.mark.parametrize("user_key, can_login", [...])`.
- Build the cases from `config.SAUCE_USERS.keys()` or list them explicitly.

## Run it
```bash
pytest exercises/05_data_driven/test_users.py
```

## Done when
All parametrized cases pass (4 test instances).
