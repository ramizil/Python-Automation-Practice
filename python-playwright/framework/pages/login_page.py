"""SauceDemo login page."""
from __future__ import annotations

from playwright.sync_api import Page

from .base_page import BasePage


class LoginPage(BasePage):
    def __init__(self, page: Page) -> None:
        super().__init__(page)
        self.username_input = page.locator("#user-name")
        self.password_input = page.locator("#password")
        self.login_button = page.locator("#login-button")
        self.error_message = page.locator('[data-test="error"]')

    def open(self, base_url: str) -> "LoginPage":
        self.page.goto(base_url)
        return self

    def login(self, username: str, password: str) -> None:
        self.username_input.fill(username)
        self.password_input.fill(password)
        self.login_button.click()
