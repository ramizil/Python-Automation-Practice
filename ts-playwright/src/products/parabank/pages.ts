// Parabank page objects (the interaction layer of the Parabank product).
// Parabank fills several dropdowns/tables via JS after load, so a few methods
// wait for options/rows to be attached before acting — realistic AJAX handling.
import { Locator, Page } from '@playwright/test';
import { Customer } from './data';

export class RegisterPage {
  readonly rightPanel: Locator;
  constructor(private page: Page) {
    this.rightPanel = page.locator('#rightPanel');
  }

  async open(base: string): Promise<this> {
    await this.page.goto(`${base}/register.htm`);
    return this;
  }

  async register(c: Customer): Promise<string> {
    const fields: Record<string, string> = {
      'customer.firstName': c.firstName,
      'customer.lastName': c.lastName,
      'customer.address.street': c.street,
      'customer.address.city': c.city,
      'customer.address.state': c.state,
      'customer.address.zipCode': c.zipCode,
      'customer.phoneNumber': c.phone,
      'customer.ssn': c.ssn,
      'customer.username': c.username,
      'customer.password': c.password,
      repeatedPassword: c.password,
    };
    for (const [name, value] of Object.entries(fields)) {
      await this.page.locator(`[name="${name}"]`).fill(value);
    }
    await this.page.getByRole('button', { name: 'Register' }).click();
    await this.rightPanel.getByText('Your account was created successfully').waitFor();
    return this.rightPanel.innerText();
  }
}

export class AccountsOverviewPage {
  readonly accountLinks: Locator;
  constructor(private page: Page) {
    this.accountLinks = page.locator('#accountTable tbody tr td a');
  }

  async open(base: string): Promise<this> {
    await this.page.goto(`${base}/overview.htm`);
    return this;
  }

  async accountIds(): Promise<string[]> {
    await this.accountLinks.first().waitFor({ state: 'attached' });
    return this.accountLinks.allInnerTexts();
  }
}

export class OpenAccountPage {
  static readonly TYPE_CHECKING = '0';
  static readonly TYPE_SAVINGS = '1';

  readonly typeSelect: Locator;
  readonly fromAccount: Locator;
  readonly submit: Locator;
  readonly newAccountId: Locator;
  readonly resultHeader: Locator;

  constructor(private page: Page) {
    this.typeSelect = page.locator('#type');
    this.fromAccount = page.locator('#fromAccountId');
    this.submit = page.getByRole('button', { name: 'Open New Account' });
    this.newAccountId = page.locator('#newAccountId');
    this.resultHeader = page.locator('#openAccountResult h1');
  }

  async open(base: string): Promise<this> {
    await this.page.goto(`${base}/openaccount.htm`);
    return this;
  }

  async openAccount(accountType: string = OpenAccountPage.TYPE_SAVINGS): Promise<string> {
    await this.fromAccount.locator('option').first().waitFor({ state: 'attached' });
    await this.typeSelect.selectOption(accountType);
    await this.submit.click();
    await this.newAccountId.waitFor({ state: 'visible' });
    return this.newAccountId.innerText();
  }
}

export class TransferFundsPage {
  readonly amount: Locator;
  readonly fromAccount: Locator;
  readonly toAccount: Locator;
  readonly submit: Locator;
  readonly resultHeader: Locator;

  constructor(private page: Page) {
    this.amount = page.locator('#amount');
    this.fromAccount = page.locator('#fromAccountId');
    this.toAccount = page.locator('#toAccountId');
    this.submit = page.getByRole('button', { name: 'Transfer' });
    this.resultHeader = page.locator('#showResult h1');
  }

  async open(base: string): Promise<this> {
    await this.page.goto(`${base}/transfer.htm`);
    return this;
  }

  async transfer(amount: number, toAccount: string, fromAccount?: string): Promise<string> {
    await this.fromAccount.locator('option').first().waitFor({ state: 'attached' });
    await this.amount.fill(String(amount));
    if (fromAccount) await this.fromAccount.selectOption(fromAccount);
    await this.toAccount.selectOption(toAccount);
    await this.submit.click();
    await this.resultHeader.waitFor({ state: 'visible' });
    return this.resultHeader.innerText();
  }
}
