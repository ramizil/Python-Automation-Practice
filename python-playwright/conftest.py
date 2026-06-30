"""Shared pytest fixtures.

``pytest-playwright`` already provides ``page``, ``context``, ``browser`` and a
session-scoped ``playwright`` instance. We add:
- ``base_url``  -> defaults to SauceDemo (overridable with --base-url)
- ``booker_request`` -> a Playwright APIRequestContext pointed at restful-booker
- ``booker`` -> a ready-to-use BookerClient
"""
from __future__ import annotations

import pytest
from playwright.sync_api import APIRequestContext, Playwright

from framework import config
from framework.api.booker_client import BookerClient


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
