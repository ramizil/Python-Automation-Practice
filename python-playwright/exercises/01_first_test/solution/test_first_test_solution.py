from playwright.sync_api import Page, expect


def test_saucedemo_loads(page: Page, base_url: str):
    page.goto(base_url)
    expect(page).to_have_title("Swag Labs")
    expect(page.locator("#login-button")).to_be_visible()
