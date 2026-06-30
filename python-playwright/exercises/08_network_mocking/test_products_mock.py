import pytest
from playwright.sync_api import Page, expect

from framework.mock_app import PRODUCTS_APP_HTML, PRODUCTS_URL_GLOB

pytestmark = [pytest.mark.ui, pytest.mark.mocks]


def test_stub_two_products(page: Page):
    # TODO 1: page.route(PRODUCTS_URL_GLOB, ...) -> fulfill with 2 fake products
    #         (remember the Access-Control-Allow-Origin: * header)
    # TODO 2: page.set_content(PRODUCTS_APP_HTML); click "#load"
    # TODO 3: assert .product has count 2 with your titles
    pytest.fail("TODO: implement, then delete this line")


def test_error_state(page: Page):
    # TODO: route the request to status=500 (or route.abort()), load, and
    #       assert "#error" is visible and there are 0 ".product" items
    pytest.fail("TODO: implement, then delete this line")
