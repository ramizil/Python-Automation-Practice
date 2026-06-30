import { Page } from '@playwright/test';
import { test, expect } from '../../src/fixtures';
import { SAUCE_USERS, SAUCE_PASSWORD } from '../../src/config';
import { LoginPage } from '../../src/pages/LoginPage';
import { InventoryPage } from '../../src/pages/InventoryPage';

class ShopSteps {
  // Layer 2 — business steps (you implement)
  readonly inventory: InventoryPage;
  private loginPage: LoginPage;

  constructor(page: Page) {
    this.loginPage = new LoginPage(page);
    this.inventory = new InventoryPage(page);
  }

  async loginAs(userKey: keyof typeof SAUCE_USERS = 'standard'): Promise<this> {
    // TODO: open the site and login with SAUCE_USERS[userKey] / SAUCE_PASSWORD;
    //       return this for chaining
    throw new Error('TODO: implement loginAs');
  }

  async addItems(names: string[]): Promise<this> {
    // TODO: add each name to the cart via this.inventory; return this
    throw new Error('TODO: implement addItems');
  }
}

test('layered flow @ui', async ({ page }) => {
  const steps = new ShopSteps(page);
  // TODO: loginAs('standard'), addItems(two products), assert cartCount() === 2
  expect(true, 'TODO: implement ShopSteps and this flow, then delete this line').toBe(false);
});
