import { test, expect, Page, Locator } from '@playwright/test';
import { SAUCE_USERS, SAUCE_PASSWORD } from '../../../src/config';

class MyLoginPage {
  readonly page: Page;
  readonly username: Locator;
  readonly password: Locator;
  readonly loginButton: Locator;

  constructor(page: Page) {
    this.page = page;
    this.username = page.locator('#user-name');
    this.password = page.locator('#password');
    this.loginButton = page.locator('#login-button');
  }

  async open(): Promise<void> {
    await this.page.goto('/');
  }

  async login(username: string, password: string): Promise<void> {
    await this.username.fill(username);
    await this.password.fill(password);
    await this.loginButton.click();
  }
}

test('login with my page object @ui', async ({ page }) => {
  const login = new MyLoginPage(page);
  await login.open();
  await login.login(SAUCE_USERS.standard, SAUCE_PASSWORD);
  await expect(page.locator('.title')).toHaveText('Products');
});
