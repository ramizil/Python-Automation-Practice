"""Topics 1-2 (worked examples): first test, locators & web-first assertions.

Run just this file:
    pytest tests/ui/test_login.py
"""

import pytest
from playwright.sync_api import Page, expect

from framework import config

pytestmark = pytest.mark.ui


def test_login_page_loads(page: Page, base_url: str):
    page.goto(base_url)
    expect(page).to_have_title("Swag Labs")
    expect(page.locator("#login-button")).to_be_visible()


def test_successful_login_shows_inventory(page: Page, base_url: str):
    page.goto(base_url)
    page.locator("#user-name").fill(config.SAUCE_USERS["standard"])
    page.locator("#password").fill(config.SAUCE_PASSWORD)
    page.locator("#login-button").click()

    expect(page).to_have_url(f"{base_url}/inventory.html")
    expect(page.locator(".title")).to_have_text("Products")


def test_bad_credentials_show_error(page: Page, base_url: str):
    page.goto(base_url)
    page.locator("#user-name").fill("nope")
    page.locator("#password").fill("wrong")
    page.locator("#login-button").click()

    error = page.locator('[data-test="error"]')
    expect(error).to_be_visible()
    expect(error).to_contain_text("Username and password do not match")
