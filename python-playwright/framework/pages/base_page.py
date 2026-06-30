"""Base class shared by all page objects.

A page object wraps a Playwright ``Page`` and exposes intention-revealing methods
(``login``, ``add_item_to_cart``) and locators, so tests read like user stories
and selectors live in one place.
"""

from __future__ import annotations

from typing import TypeVar

from playwright.sync_api import Page

# Bound TypeVar so open() returns the concrete subclass type, enabling fluent
# chaining like LoginPage(page).open(url).login(...) without breaking overrides.
_T = TypeVar("_T", bound="BasePage")


class BasePage:
    def __init__(self, page: Page) -> None:
        self.page = page

    def open(self: _T, url: str) -> _T:
        self.page.goto(url)
        return self

    @property
    def title(self) -> str:
        return self.page.title()
