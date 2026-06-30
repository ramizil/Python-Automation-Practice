"""Base class shared by all page objects.

A page object wraps a Playwright ``Page`` and exposes intention-revealing methods
(``login``, ``add_item_to_cart``) and locators, so tests read like user stories
and selectors live in one place.
"""
from __future__ import annotations

from playwright.sync_api import Page


class BasePage:
    def __init__(self, page: Page) -> None:
        self.page = page

    def open(self, url: str) -> None:
        self.page.goto(url)

    @property
    def title(self) -> str:
        return self.page.title()
