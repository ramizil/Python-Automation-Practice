"""Parabank page objects (the interaction layer of the Parabank product).

Parabank populates several dropdowns/tables asynchronously after the page loads,
so a few methods explicitly wait for options/rows to be attached before acting —
a realistic example of handling an AJAX-driven UI.
"""

from __future__ import annotations

from playwright.sync_api import Page

from framework.pages.base_page import BasePage

from .data import Customer


class RegisterPage(BasePage):
    def __init__(self, page: Page) -> None:
        super().__init__(page)
        self.right_panel = page.locator("#rightPanel")

    def open(self, base: str) -> RegisterPage:
        self.page.goto(f"{base}/register.htm")
        return self

    def register(self, c: Customer) -> str:
        fields = {
            "customer.firstName": c.first_name,
            "customer.lastName": c.last_name,
            "customer.address.street": c.street,
            "customer.address.city": c.city,
            "customer.address.state": c.state,
            "customer.address.zipCode": c.zip_code,
            "customer.phoneNumber": c.phone,
            "customer.ssn": c.ssn,
            "customer.username": c.username,
            "customer.password": c.password,
            "repeatedPassword": c.password,
        }
        for name, value in fields.items():
            self.page.locator(f'[name="{name}"]').fill(value)
        self.page.get_by_role("button", name="Register").click()
        self.right_panel.get_by_text("Your account was created successfully").wait_for()
        return self.right_panel.inner_text()


class AccountsOverviewPage(BasePage):
    def __init__(self, page: Page) -> None:
        super().__init__(page)
        self.account_links = page.locator("#accountTable tbody tr td a")

    def open(self, base: str) -> AccountsOverviewPage:
        self.page.goto(f"{base}/overview.htm")
        return self

    def account_ids(self) -> list[str]:
        self.account_links.first.wait_for(state="attached")
        return self.account_links.all_inner_texts()


class OpenAccountPage(BasePage):
    TYPE_CHECKING = "0"
    TYPE_SAVINGS = "1"

    def __init__(self, page: Page) -> None:
        super().__init__(page)
        self.type_select = page.locator("#type")
        self.from_account = page.locator("#fromAccountId")
        self.submit = page.get_by_role("button", name="Open New Account")
        self.new_account_id = page.locator("#newAccountId")
        self.result_header = page.locator("#openAccountResult h1")

    def open(self, base: str) -> OpenAccountPage:
        self.page.goto(f"{base}/openaccount.htm")
        return self

    def open_account(self, account_type: str = TYPE_SAVINGS) -> str:
        # The from-account dropdown is filled by JS after load — wait for it.
        self.from_account.locator("option").first.wait_for(state="attached")
        self.type_select.select_option(account_type)
        self.submit.click()
        self.new_account_id.wait_for(state="visible")
        return self.new_account_id.inner_text()


class TransferFundsPage(BasePage):
    def __init__(self, page: Page) -> None:
        super().__init__(page)
        self.amount = page.locator("#amount")
        self.from_account = page.locator("#fromAccountId")
        self.to_account = page.locator("#toAccountId")
        self.submit = page.get_by_role("button", name="Transfer")
        self.result_header = page.locator("#showResult h1")

    def open(self, base: str) -> TransferFundsPage:
        self.page.goto(f"{base}/transfer.htm")
        return self

    def transfer(self, amount: int, to_account: str, from_account: str | None = None) -> str:
        self.from_account.locator("option").first.wait_for(state="attached")
        self.amount.fill(str(amount))
        if from_account is not None:
            self.from_account.select_option(from_account)
        self.to_account.select_option(to_account)
        self.submit.click()
        self.result_header.wait_for(state="visible")
        return self.result_header.inner_text()
