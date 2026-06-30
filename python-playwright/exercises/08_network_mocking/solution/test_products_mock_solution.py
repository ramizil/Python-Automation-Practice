import pytest
from playwright.sync_api import Page, expect

from framework.mock_app import PRODUCTS_APP_HTML, PRODUCTS_URL_GLOB

pytestmark = [pytest.mark.ui, pytest.mark.mocks]

CORS = {"Access-Control-Allow-Origin": "*"}


def test_stub_two_products(page: Page):
    fake = {"products": [{"id": 1, "title": "Alpha"}, {"id": 2, "title": "Beta"}]}
    page.route(PRODUCTS_URL_GLOB, lambda route: route.fulfill(json=fake, headers=CORS))
    page.set_content(PRODUCTS_APP_HTML)
    page.locator("#load").click()

    expect(page.locator(".product")).to_have_count(2)
    expect(page.locator(".product")).to_have_text(["Alpha", "Beta"])


def test_error_state(page: Page):
    page.route(PRODUCTS_URL_GLOB, lambda route: route.fulfill(status=500, headers=CORS))
    page.set_content(PRODUCTS_APP_HTML)
    page.locator("#load").click()

    expect(page.locator("#error")).to_be_visible()
    expect(page.locator(".product")).to_have_count(0)
