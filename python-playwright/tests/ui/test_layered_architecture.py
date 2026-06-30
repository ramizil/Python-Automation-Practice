"""Topic 12 (worked example): layered framework architecture — UI.

Compare this with tests/ui/test_checkout.py (topic 4). Same flow, but here the
test only speaks the *business* language (login_as, add_items_to_cart, checkout)
— all the page-object mechanics live in the Layer-2 steps. The test reads like a
spec a product owner would recognise.

    pytest tests/ui/test_layered_architecture.py
"""

import pytest
from playwright.sync_api import Page

from framework.products.saucedemo import SauceDemoSteps

pytestmark = [pytest.mark.ui, pytest.mark.slow]


def test_checkout_two_items_via_steps(page: Page, base_url: str):
    steps = SauceDemoSteps(page, base_url)

    steps.login_as("standard")
    steps.add_items_to_cart(["Sauce Labs Backpack", "Sauce Labs Bike Light"])
    confirmation = steps.checkout("Ada", "Lovelace", "12345")

    assert confirmation == "Thank you for your order!"
