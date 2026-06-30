"""Parabank business steps (Layer 2) — the bank workflows a test cares about."""

from __future__ import annotations

from playwright.sync_api import Page

from framework import config
from framework.core import get_logger

from .data import Customer
from .pages import AccountsOverviewPage, OpenAccountPage, RegisterPage, TransferFundsPage


class ParabankSteps:
    def __init__(self, page: Page) -> None:
        self.page = page
        self.base = config.PARABANK_URL
        # Parabank can be slow; give actions room.
        self.page.set_default_timeout(45_000)
        self.register_page = RegisterPage(page)
        self.overview = AccountsOverviewPage(page)
        self.open_account_page = OpenAccountPage(page)
        self.transfer_page = TransferFundsPage(page)
        self.log = get_logger("ParabankSteps")

    def register(self, customer: Customer) -> str:
        self.log.info("register user %s", customer.username)
        self.register_page.open(self.base)
        return self.register_page.register(customer)

    def open_savings_account(self) -> str:
        self.log.info("open a savings account")
        new_id = self.open_account_page.open(self.base).open_account(OpenAccountPage.TYPE_SAVINGS)
        self.log.info("opened account %s", new_id)
        return new_id

    def transfer(self, amount: int, to_account: str, from_account: str | None = None) -> str:
        self.log.info("transfer %s -> %s", amount, to_account)
        return self.transfer_page.open(self.base).transfer(amount, to_account, from_account)

    def overview_account_ids(self) -> list[str]:
        return self.overview.open(self.base).account_ids()
