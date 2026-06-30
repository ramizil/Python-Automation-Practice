from playwright.sync_api import Page, expect

from framework import config


class MyLoginPage:
    def __init__(self, page: Page) -> None:
        self.page = page
        self.username_input = page.locator("#user-name")
        self.password_input = page.locator("#password")
        self.login_button = page.locator("#login-button")

    def open(self, base_url: str) -> "MyLoginPage":
        self.page.goto(base_url)
        return self

    def login(self, username: str, password: str) -> None:
        self.username_input.fill(username)
        self.password_input.fill(password)
        self.login_button.click()


def test_login_with_my_page_object(page: Page, base_url: str):
    login = MyLoginPage(page).open(base_url)
    login.login(config.SAUCE_USERS["standard"], config.SAUCE_PASSWORD)
    expect(page.locator(".title")).to_have_text("Products")
