import pytest

from framework.products.parabank import ParabankApiClient, ParabankSteps

pytestmark = [pytest.mark.capstone, pytest.mark.slow]


def test_capstone(page, parabank_user, parabank_request):
    steps = ParabankSteps(page)
    api = ParabankApiClient(parabank_request)
    customer_id = parabank_user.customer_id

    start = api.accounts(customer_id)
    assert len(start) >= 1

    new_id = steps.open_savings_account()

    after = api.accounts(customer_id)
    assert len(after) == len(start) + 1
    assert any(str(a["id"]) == new_id for a in after)
    assert api.account(int(new_id))["type"] == "SAVINGS"

    confirmation = steps.transfer(amount=25, to_account=new_id)
    assert "Transfer Complete!" in confirmation

    assert len(api.transactions(int(new_id))) >= 1
