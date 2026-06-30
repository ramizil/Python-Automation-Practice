"""Topic 3 (worked example): the same login, refactored to a Page Object.

Notice how the test reads as intent only - selectors live in LoginPage.
    pytest tests/ui/test_pom_login.py
"""
import pytest
from playwright.sync_api import Page, expect

from framework import config
from framework.pages.login_page import LoginPage

pytestmark = pytest.mark.ui


def test_login_via_page_object(page: Page, base_url: str):
    login = LoginPage(page).open(base_url)
    login.login(config.SAUCE_USERS["standard"], config.SAUCE_PASSWORD)
    expect(page.locator(".title")).to_have_text("Products")


def test_locked_out_user_via_page_object(page: Page, base_url: str):
    login = LoginPage(page).open(base_url)
    login.login(config.SAUCE_USERS["locked_out"], config.SAUCE_PASSWORD)
    expect(login.error_message).to_contain_text("locked out")
