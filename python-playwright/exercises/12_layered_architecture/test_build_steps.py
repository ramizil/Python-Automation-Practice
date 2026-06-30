import pytest
from playwright.sync_api import Page

from framework import config
from framework.pages.inventory_page import InventoryPage
from framework.pages.login_page import LoginPage


class ShopSteps:  # Layer 2 — business steps (you implement)
    def __init__(self, page: Page, base_url: str) -> None:
        self.page = page
        self.base_url = base_url
        self.login_page = LoginPage(page)
        self.inventory = InventoryPage(page)

    def login_as(self, user_key: str = "standard"):
        # TODO: open base_url and log in with config.SAUCE_USERS[user_key]
        #       and config.SAUCE_PASSWORD; return self for chaining
        raise NotImplementedError

    def add_items(self, names):
        # TODO: add each name to the cart via self.inventory; return self
        raise NotImplementedError


def test_layered_flow(page: Page, base_url: str):
    steps = ShopSteps(page, base_url)
    # TODO: login as "standard", add two items, assert steps.inventory.cart_count() == 2
    pytest.fail("TODO: implement ShopSteps and this flow, then delete this line")
