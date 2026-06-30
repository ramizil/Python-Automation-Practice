"""SauceDemo cart page."""

from __future__ import annotations

from playwright.sync_api import Page

from .base_page import BasePage


class CartPage(BasePage):
    def __init__(self, page: Page) -> None:
        super().__init__(page)
        self.items = page.locator(".cart_item")
        self.checkout_button = page.locator("#checkout")

    def item_names(self) -> list[str]:
        return self.page.locator(".cart_item .inventory_item_name").all_inner_texts()

    def checkout(self) -> None:
        self.checkout_button.click()
