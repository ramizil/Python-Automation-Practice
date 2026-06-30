from playwright.sync_api import Page, expect

from framework import config


def test_locked_out_user_sees_error(page: Page, base_url: str):
    page.goto(base_url)
    page.locator("#user-name").fill(config.SAUCE_USERS["locked_out"])
    page.locator("#password").fill(config.SAUCE_PASSWORD)
    page.locator("#login-button").click()
    expect(page.locator('[data-test="error"]')).to_contain_text("locked out")


def test_empty_credentials_shows_required_error(page: Page, base_url: str):
    page.goto(base_url)
    page.locator("#login-button").click()
    expect(page.locator('[data-test="error"]')).to_contain_text("Username is required")
