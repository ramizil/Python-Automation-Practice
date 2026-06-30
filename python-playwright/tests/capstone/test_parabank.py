"""Topic 11 (capstone, worked example): Parabank end-to-end, UI + API combined.

This pulls together everything: the layered architecture (core BaseApiClient ->
ParabankApiClient + ParabankSteps), a unique-user-per-run fixture, schema
validation (topic 07), and the **hybrid pattern** (topic 09) — drive an action in
one channel, verify it in the other:

  - drive UI (open account / transfer)  ->  verify by API (account/txn exists)

Parabank is a public demo bank: occasionally slow or reset, so this is marked
`capstone`/`slow` and excluded from the fast/default CI run. Run it explicitly:
    pytest tests/capstone -m capstone
"""

import pytest
from jsonschema import validate

from framework.products.parabank import ParabankApiClient, ParabankSteps
from framework.schemas.parabank import ACCOUNTS_LIST_SCHEMA, TRANSACTIONS_LIST_SCHEMA

pytestmark = [pytest.mark.capstone, pytest.mark.slow]


def test_open_account_and_transfer_end_to_end(page, parabank_user, parabank_request):
    steps = ParabankSteps(page)
    api = ParabankApiClient(parabank_request)
    customer_id = parabank_user.customer_id

    # Starting state via API — a freshly registered user has one CHECKING account.
    start = api.accounts(customer_id)
    validate(instance=start, schema=ACCOUNTS_LIST_SCHEMA)  # contract check (topic 07)
    assert len(start) >= 1

    # Drive the UI: open a new savings account.
    new_id = steps.open_savings_account()

    # Verify by API (hybrid): the account now exists and is a SAVINGS account.
    after = api.accounts(customer_id)
    assert len(after) == len(start) + 1
    assert any(str(a["id"]) == new_id for a in after)
    assert api.account(int(new_id))["type"] == "SAVINGS"

    # Drive the UI: transfer funds into the new account.
    confirmation = steps.transfer(amount=25, to_account=new_id)
    assert "Transfer Complete!" in confirmation

    # Verify by API (hybrid): the transfer produced a transaction on the account.
    txns = api.transactions(int(new_id))
    validate(instance=txns, schema=TRANSACTIONS_LIST_SCHEMA)
    assert len(txns) >= 1
