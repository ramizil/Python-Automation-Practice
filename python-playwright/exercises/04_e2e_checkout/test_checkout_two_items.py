import pytest
from playwright.sync_api import Page, expect

from framework import config
from framework.pages.cart_page import CartPage
from framework.pages.checkout_page import CheckoutPage
from framework.pages.inventory_page import InventoryPage
from framework.pages.login_page import LoginPage

ITEMS = ["Sauce Labs Backpack", "Sauce Labs Bike Light"]


def test_buy_two_items(page: Page, base_url: str):
    # TODO 1: log in as the standard user
    # TODO 2: add both ITEMS to the cart, assert cart_count() == 2
    # TODO 3: go to cart, assert both names present
    # TODO 4: checkout -> fill_information -> finish
    # TODO 5: assert confirmation header "Thank you for your order!"
    pytest.fail("TODO: implement, then delete this line")
