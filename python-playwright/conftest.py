"""Shared pytest fixtures.

``pytest-playwright`` already provides ``page``, ``context``, ``browser`` and a
session-scoped ``playwright`` instance. We add:
- ``base_url``  -> defaults to SauceDemo (overridable with --base-url)
- ``booker_request`` -> a Playwright APIRequestContext pointed at restful-booker
- ``booker`` -> a ready-to-use BookerClient
"""

from __future__ import annotations

import pytest
from playwright.sync_api import APIRequestContext, Page, Playwright

from framework import config
from framework.api.booker_client import BookerClient
from framework.products.parabank import Customer, ParabankApiClient, ParabankSteps, new_customer


@pytest.fixture(scope="session")
def base_url() -> str:
    # Overrides pytest-base-url's fixture so UI tests default to SauceDemo.
    return config.SAUCEDEMO_URL


@pytest.fixture(scope="session")
def browser_context_args(browser_context_args: dict) -> dict:
    # Applied to every browser context pytest-playwright creates (UI tests).
    return {**browser_context_args, "ignore_https_errors": config.IGNORE_HTTPS_ERRORS}


@pytest.fixture()
def booker_request(playwright: Playwright) -> APIRequestContext:
    request = playwright.request.new_context(
        base_url=config.BOOKER_API_URL,
        ignore_https_errors=config.IGNORE_HTTPS_ERRORS,
    )
    yield request
    request.dispose()


@pytest.fixture()
def booker(booker_request: APIRequestContext) -> BookerClient:
    return BookerClient(booker_request)


# ---- Parabank (capstone, topic 11) ---- #
@pytest.fixture()
def parabank_request(playwright: Playwright) -> APIRequestContext:
    # Based at the REST root so client paths are relative (login, accounts, ...).
    # Trailing slash matters: it preserves the /parabank/services/bank prefix when
    # relative paths (no leading slash) are resolved against it.
    request = playwright.request.new_context(
        base_url=f"{config.PARABANK_URL}/services/bank/",
        ignore_https_errors=config.IGNORE_HTTPS_ERRORS,
    )
    yield request
    request.dispose()


@pytest.fixture()
def parabank_user(page: Page, parabank_request: APIRequestContext) -> Customer:
    """Register a brand-new Parabank customer (unique per run) and return it.

    Registration also logs the browser in, so a test receiving this fixture can
    drive the UI immediately. The customer's id is resolved via the API.
    """
    customer = new_customer()
    ParabankSteps(page).register(customer)
    info = ParabankApiClient(parabank_request).login(customer.username, customer.password)
    customer.customer_id = info["id"]
    return customer
