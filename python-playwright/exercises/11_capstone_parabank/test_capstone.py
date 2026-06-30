import pytest

from framework.products.parabank import ParabankApiClient, ParabankSteps

pytestmark = [pytest.mark.capstone, pytest.mark.slow]


def test_capstone(page, parabank_user, parabank_request):
    steps = ParabankSteps(page)
    api = ParabankApiClient(parabank_request)
    customer_id = parabank_user.customer_id

    # TODO 1: read starting accounts via API (api.accounts(customer_id)); assert >= 1
    # TODO 2: open a savings account via the UI -> steps.open_savings_account()
    # TODO 3: verify by API the new account exists and its type == "SAVINGS"
    # TODO 4: transfer 25 into it via UI; assert "Transfer Complete!" in result
    # TODO 5: verify by API there is >= 1 transaction on the new account
    pytest.fail("TODO: implement the capstone flow, then delete this line")
