import pytest
from playwright.sync_api import Page, expect

from framework import config


def test_locked_out_user_sees_error(page: Page, base_url: str):
    # TODO: go to base_url, log in as the locked_out user,
    #       assert the error banner contains "locked out".
    pytest.fail("TODO: implement, then delete this line")


def test_empty_credentials_shows_required_error(page: Page, base_url: str):
    # TODO: go to base_url, click #login-button with empty fields,
    #       assert the error contains "Username is required".
    pytest.fail("TODO: implement, then delete this line")
