import { test, expect, Page } from '@playwright/test';
import { SAUCE_USERS, SAUCE_PASSWORD } from '../../src/config';

class MyLoginPage {
  readonly page: Page;
  constructor(page: Page) {
    this.page = page;
    // TODO: define locators for #user-name, #password, #login-button
  }

  async open(): Promise<void> {
    // TODO: navigate to '/'
    throw new Error('TODO: implement open()');
  }

  async login(username: string, password: string): Promise<void> {
    // TODO: fill username + password and click login
    throw new Error('TODO: implement login()');
  }
}

test('login with my page object @ui', async ({ page }) => {
  // TODO: use MyLoginPage to open + login as the standard user,
  //       then assert .title has text 'Products'.
  throw new Error('TODO: implement, then delete this line');
});
