import { Page } from '@playwright/test';
import { test, expect } from '../../../src/fixtures';
import { SAUCE_USERS, SAUCE_PASSWORD } from '../../../src/config';
import { LoginPage } from '../../../src/pages/LoginPage';
import { InventoryPage } from '../../../src/pages/InventoryPage';

class ShopSteps {
  readonly inventory: InventoryPage;
  private loginPage: LoginPage;

  constructor(page: Page) {
    this.loginPage = new LoginPage(page);
    this.inventory = new InventoryPage(page);
  }

  async loginAs(userKey: keyof typeof SAUCE_USERS = 'standard'): Promise<this> {
    await this.loginPage.open();
    await this.loginPage.login(SAUCE_USERS[userKey], SAUCE_PASSWORD);
    return this;
  }

  async addItems(names: string[]): Promise<this> {
    for (const name of names) await this.inventory.addItemToCart(name);
    return this;
  }
}

test('layered flow @ui', async ({ page }) => {
  const steps = new ShopSteps(page);
  await steps.loginAs('standard');
  await steps.addItems(['Sauce Labs Backpack', 'Sauce Labs Bike Light']);
  expect(await steps.inventory.cartCount()).toBe(2);
});
