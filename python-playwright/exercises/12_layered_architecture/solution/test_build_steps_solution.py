from playwright.sync_api import Page

from framework import config
from framework.pages.inventory_page import InventoryPage
from framework.pages.login_page import LoginPage


class ShopSteps:
    def __init__(self, page: Page, base_url: str) -> None:
        self.page = page
        self.base_url = base_url
        self.login_page = LoginPage(page)
        self.inventory = InventoryPage(page)

    def login_as(self, user_key: str = "standard") -> "ShopSteps":
        self.login_page.open(self.base_url)
        self.login_page.login(config.SAUCE_USERS[user_key], config.SAUCE_PASSWORD)
        return self

    def add_items(self, names: list[str]) -> "ShopSteps":
        for name in names:
            self.inventory.add_item_to_cart(name)
        return self


def test_layered_flow(page: Page, base_url: str):
    steps = ShopSteps(page, base_url)
    steps.login_as("standard").add_items(["Sauce Labs Backpack", "Sauce Labs Bike Light"])
    assert steps.inventory.cart_count() == 2
