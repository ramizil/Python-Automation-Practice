"""Topic 8 (worked example): network mocking & interception.

`page.route(url_glob, handler)` lets you intercept every matching request the
page makes. The handler decides what happens:
  - route.fulfill(...)  -> answer with YOUR response (stub the backend)
  - route.abort()       -> simulate a network failure
  - route.fetch()       -> get the REAL response so you can tweak it, then fulfill

This makes edge cases (empty lists, 500s, slow APIs) deterministic instead of
hoping the real server misbehaves on cue.

    pytest tests/ui/test_mocking.py
"""

import pytest
from playwright.sync_api import Page, expect

from framework.mock_app import PRODUCTS_APP_HTML, PRODUCTS_URL_GLOB

pytestmark = [pytest.mark.ui, pytest.mark.mocks]


def _fake_products(*titles: str) -> dict:
    return {"products": [{"id": i, "title": t} for i, t in enumerate(titles, 1)]}


def test_stub_returns_two_products(page: Page):
    # The page never reaches DummyJSON; it gets exactly what we fulfill.
    page.route(
        PRODUCTS_URL_GLOB,
        lambda route: route.fulfill(
            json=_fake_products("Mock Widget", "Mock Gadget"),
            headers={"Access-Control-Allow-Origin": "*"},
        ),
    )
    page.set_content(PRODUCTS_APP_HTML)
    page.locator("#load").click()

    expect(page.locator(".product")).to_have_count(2)
    expect(page.locator(".product")).to_have_text(["Mock Widget", "Mock Gadget"])


def test_server_error_shows_error_state(page: Page):
    page.route(
        PRODUCTS_URL_GLOB,
        lambda route: route.fulfill(status=500, headers={"Access-Control-Allow-Origin": "*"}),
    )
    page.set_content(PRODUCTS_APP_HTML)
    page.locator("#load").click()

    expect(page.locator("#error")).to_be_visible()
    expect(page.locator(".product")).to_have_count(0)


def test_aborted_request_shows_error_state(page: Page):
    page.route(PRODUCTS_URL_GLOB, lambda route: route.abort())
    page.set_content(PRODUCTS_APP_HTML)
    page.locator("#load").click()

    expect(page.locator("#error")).to_be_visible()


def test_modify_real_response(page: Page):
    # Pass-through + tweak: fetch the real API, then inject our own first item.
    def handler(route):
        original = route.fetch().json()
        original["products"].insert(0, {"id": 999, "title": "INJECTED"})
        route.fulfill(json=original, headers={"Access-Control-Allow-Origin": "*"})

    page.route(PRODUCTS_URL_GLOB, handler)
    page.set_content(PRODUCTS_APP_HTML)
    page.locator("#load").click()

    expect(page.locator(".product").first).to_have_text("INJECTED")
