import pytest
from playwright.sync_api import Page, expect

from framework import config
from framework.pages.login_page import LoginPage


@pytest.mark.parametrize(
    "user_key, can_login",
    [
        ("standard", True),
        ("problem", True),
        ("performance_glitch", True),
        ("locked_out", False),
    ],
)
def test_user_login(page: Page, base_url: str, user_key, can_login):
    login = LoginPage(page).open(base_url)
    login.login(config.SAUCE_USERS[user_key], config.SAUCE_PASSWORD)

    if can_login:
        expect(page.locator(".title")).to_have_text("Products")
    else:
        expect(login.error_message).to_contain_text("locked out")
