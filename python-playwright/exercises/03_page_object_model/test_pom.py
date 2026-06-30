"""Build your own page object, then use it in the test below.

Keep everything in this one file (no sibling imports) to avoid import headaches.
"""
import pytest
from playwright.sync_api import Page, expect

from framework import config


class MyLoginPage:
    def __init__(self, page: Page) -> None:
        self.page = page
        # TODO: define locators for #user-name, #password, #login-button

    def open(self, base_url: str) -> "MyLoginPage":
        # TODO: navigate to base_url and return self
        raise NotImplementedError

    def login(self, username: str, password: str) -> None:
        # TODO: fill username + password and click login
        raise NotImplementedError


def test_login_with_my_page_object(page: Page, base_url: str):
    # TODO: use MyLoginPage to open + login as the standard user,
    #       then assert .title has text "Products".
    pytest.fail("TODO: implement MyLoginPage and this test, then delete this line")
