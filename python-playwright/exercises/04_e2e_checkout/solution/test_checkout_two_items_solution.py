from playwright.sync_api import Page, expect

from framework import config
from framework.pages.cart_page import CartPage
from framework.pages.checkout_page import CheckoutPage
from framework.pages.inventory_page import InventoryPage
from framework.pages.login_page import LoginPage

ITEMS = ["Sauce Labs Backpack", "Sauce Labs Bike Light"]


def test_buy_two_items(page: Page, base_url: str):
    LoginPage(page).open(base_url).login(
        config.SAUCE_USERS["standard"], config.SAUCE_PASSWORD)

    inventory = InventoryPage(page)
    for item in ITEMS:
        inventory.add_item_to_cart(item)
    assert inventory.cart_count() == 2
    inventory.go_to_cart()

    cart = CartPage(page)
    names = cart.item_names()
    for item in ITEMS:
        assert item in names
    cart.checkout()

    checkout = CheckoutPage(page)
    checkout.fill_information("Ada", "Lovelace", "12345")
    checkout.finish()
    expect(checkout.complete_header).to_have_text("Thank you for your order!")
