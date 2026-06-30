import pytest
from playwright.sync_api import Page, expect

from framework import config
from framework.pages.login_page import LoginPage


# TODO: add @pytest.mark.parametrize over the four users (user_key, can_login)
def test_user_login(page: Page, base_url: str):
    # TODO: log in with config.SAUCE_USERS[user_key];
    #       assert "Products" when can_login else error contains "locked out".
    pytest.fail("TODO: parametrize + implement, then delete this line")
