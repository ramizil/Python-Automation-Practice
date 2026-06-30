"""Topic 4 (worked example): full end-to-end checkout flow with page objects.
pytest tests/ui/test_checkout.py
"""

import pytest
from playwright.sync_api import Page, expect

from framework import config
from framework.pages.cart_page import CartPage
from framework.pages.checkout_page import CheckoutPage
from framework.pages.inventory_page import InventoryPage
from framework.pages.login_page import LoginPage

pytestmark = [pytest.mark.ui, pytest.mark.slow]

ITEM = "Sauce Labs Backpack"


def test_buy_one_item_end_to_end(page: Page, base_url: str):
    LoginPage(page).open(base_url).login(config.SAUCE_USERS["standard"], config.SAUCE_PASSWORD)

    inventory = InventoryPage(page)
    inventory.add_item_to_cart(ITEM)
    assert inventory.cart_count() == 1
    inventory.go_to_cart()

    cart = CartPage(page)
    assert ITEM in cart.item_names()
    cart.checkout()

    checkout = CheckoutPage(page)
    checkout.fill_information("Ada", "Lovelace", "12345")
    checkout.finish()

    expect(checkout.complete_header).to_have_text("Thank you for your order!")
