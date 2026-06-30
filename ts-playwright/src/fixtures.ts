// Custom fixtures: ready-to-use page objects and a restful-booker client.
// Use `import { test, expect } from '@framework/fixtures'` in your specs.
import { test as base, expect, request, APIRequestContext } from '@playwright/test';
import { URLS, IGNORE_HTTPS_ERRORS } from './config';
import { LoginPage } from './pages/LoginPage';
import { InventoryPage } from './pages/InventoryPage';
import { CartPage } from './pages/CartPage';
import { CheckoutPage } from './pages/CheckoutPage';
import { BookerClient } from './api/BookerClient';

type Fixtures = {
  loginPage: LoginPage;
  inventoryPage: InventoryPage;
  cartPage: CartPage;
  checkoutPage: CheckoutPage;
  bookerRequest: APIRequestContext;
  booker: BookerClient;
};

export const test = base.extend<Fixtures>({
  loginPage: async ({ page }, use) => use(new LoginPage(page)),
  inventoryPage: async ({ page }, use) => use(new InventoryPage(page)),
  cartPage: async ({ page }, use) => use(new CartPage(page)),
  checkoutPage: async ({ page }, use) => use(new CheckoutPage(page)),

  bookerRequest: async ({}, use) => {
    const ctx = await request.newContext({
      baseURL: URLS.bookerApi,
      ignoreHTTPSErrors: IGNORE_HTTPS_ERRORS,
    });
    await use(ctx);
    await ctx.dispose();
  },
  booker: async ({ bookerRequest }, use) => use(new BookerClient(bookerRequest)),
});

export { expect };
