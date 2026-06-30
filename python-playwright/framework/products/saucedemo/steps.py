"""Layer 2 — SauceDemo business steps.

Steps are reusable *business actions* ("log in as the standard user", "check
out"). They compose the page objects (the interaction primitives in
``framework/pages``) so that Layer-3 tests read like user stories and never touch
selectors directly.
"""

from __future__ import annotations

from playwright.sync_api import Page

from framework import config
from framework.core import get_logger
from framework.pages.cart_page import CartPage
from framework.pages.checkout_page import CheckoutPage
from framework.pages.inventory_page import InventoryPage
from framework.pages.login_page import LoginPage


class SauceDemoSteps:
    def __init__(self, page: Page, base_url: str) -> None:
        self.page = page
        self.base_url = base_url
        self.login_page = LoginPage(page)
        self.inventory = InventoryPage(page)
        self.cart = CartPage(page)
        self.checkout_page = CheckoutPage(page)
        self.log = get_logger("SauceDemoSteps")

    def login_as(self, user_key: str = "standard") -> SauceDemoSteps:
        self.log.info("login as %s", user_key)
        self.login_page.open(self.base_url)
        self.login_page.login(config.SAUCE_USERS[user_key], config.SAUCE_PASSWORD)
        return self

    def add_items_to_cart(self, item_names: list[str]) -> SauceDemoSteps:
        self.log.info("add to cart: %s", ", ".join(item_names))
        for name in item_names:
            self.inventory.add_item_to_cart(name)
        return self

    def checkout(self, first: str, last: str, postal: str) -> str:
        """Complete checkout for whatever is in the cart; return the confirmation."""
        self.log.info("checkout as %s %s", first, last)
        self.inventory.go_to_cart()
        self.cart.checkout()
        self.checkout_page.fill_information(first, last, postal)
        self.checkout_page.finish()
        return self.checkout_page.confirmation_text()
