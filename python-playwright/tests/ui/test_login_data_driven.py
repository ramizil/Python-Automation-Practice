"""Topic 5 (worked example): data-driven tests via pytest.mark.parametrize.
pytest tests/ui/test_login_data_driven.py
"""

import pytest
from playwright.sync_api import Page, expect

from framework import config
from framework.pages.login_page import LoginPage

pytestmark = pytest.mark.ui


@pytest.mark.parametrize(
    "user_key, expect_success, expected_text",
    [
        ("standard", True, "Products"),
        ("problem", True, "Products"),
        ("performance_glitch", True, "Products"),
        ("locked_out", False, "locked out"),
    ],
)
def test_login_outcomes(page: Page, base_url: str, user_key, expect_success, expected_text):
    login = LoginPage(page).open(base_url)
    login.login(config.SAUCE_USERS[user_key], config.SAUCE_PASSWORD)

    if expect_success:
        expect(page.locator(".title")).to_have_text(expected_text)
    else:
        expect(login.error_message).to_contain_text(expected_text)
