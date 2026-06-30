// Parabank business steps (Layer 2) — the bank workflows a test cares about.
import { Page } from '@playwright/test';
import { URLS } from '../../config';
import { getLogger, Logger } from '../../core/logger';
import { Customer } from './data';
import {
  AccountsOverviewPage,
  OpenAccountPage,
  RegisterPage,
  TransferFundsPage,
} from './pages';

export class ParabankSteps {
  private base = URLS.parabank;
  private registerPage: RegisterPage;
  private overview: AccountsOverviewPage;
  private openAccountPage: OpenAccountPage;
  private transferPage: TransferFundsPage;
  private log: Logger;

  constructor(private page: Page) {
    this.page.setDefaultTimeout(45_000); // Parabank can be slow
    this.registerPage = new RegisterPage(page);
    this.overview = new AccountsOverviewPage(page);
    this.openAccountPage = new OpenAccountPage(page);
    this.transferPage = new TransferFundsPage(page);
    this.log = getLogger('ParabankSteps');
  }

  async register(customer: Customer): Promise<string> {
    this.log.info(`register user ${customer.username}`);
    await this.registerPage.open(this.base);
    return this.registerPage.register(customer);
  }

  async openSavingsAccount(): Promise<string> {
    this.log.info('open a savings account');
    await this.openAccountPage.open(this.base);
    const id = await this.openAccountPage.openAccount(OpenAccountPage.TYPE_SAVINGS);
    this.log.info(`opened account ${id}`);
    return id;
  }

  async transfer(amount: number, toAccount: string, fromAccount?: string): Promise<string> {
    this.log.info(`transfer ${amount} -> ${toAccount}`);
    await this.transferPage.open(this.base);
    return this.transferPage.transfer(amount, toAccount, fromAccount);
  }

  async overviewAccountIds(): Promise<string[]> {
    await this.overview.open(this.base);
    return this.overview.accountIds();
  }
}
