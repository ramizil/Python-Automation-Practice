"""SauceDemo inventory (product list) page."""

from __future__ import annotations

from playwright.sync_api import Locator, Page

from .base_page import BasePage


class InventoryPage(BasePage):
    def __init__(self, page: Page) -> None:
        super().__init__(page)
        self.title_label = page.locator(".title")
        self.cart_link = page.locator(".shopping_cart_link")
        self.cart_badge = page.locator(".shopping_cart_badge")

    def _add_button_for(self, item_name: str) -> Locator:
        # The item card; from it, find its "Add to cart" button.
        card = self.page.locator(".inventory_item").filter(has_text=item_name)
        return card.get_by_role("button", name="Add to cart")

    def add_item_to_cart(self, item_name: str) -> None:
        self._add_button_for(item_name).click()

    def cart_count(self) -> int:
        if self.cart_badge.count() == 0:
            return 0
        return int(self.cart_badge.inner_text())

    def go_to_cart(self) -> None:
        self.cart_link.click()
