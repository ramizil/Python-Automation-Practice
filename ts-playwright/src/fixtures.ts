// Custom fixtures: ready-to-use page objects and a restful-booker client.
// Use `import { test, expect } from '@framework/fixtures'` in your specs.
import { test as base, expect, request, APIRequestContext } from '@playwright/test';
import { URLS, IGNORE_HTTPS_ERRORS } from './config';
import { LoginPage } from './pages/LoginPage';
import { InventoryPage } from './pages/InventoryPage';
import { CartPage } from './pages/CartPage';
import { CheckoutPage } from './pages/CheckoutPage';
import { BookerClient } from './api/BookerClient';
import { ParabankSteps } from './products/parabank/steps';
import { ParabankApiClient } from './products/parabank/ParabankApiClient';
import { newCustomer, Customer } from './products/parabank/data';

type Fixtures = {
  loginPage: LoginPage;
  inventoryPage: InventoryPage;
  cartPage: CartPage;
  checkoutPage: CheckoutPage;
  bookerRequest: APIRequestContext;
  booker: BookerClient;
  parabankRequest: APIRequestContext;
  parabankUser: Customer;
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

  // ---- Parabank (capstone, topic 11) ---- //
  parabankRequest: async ({}, use) => {
    // Trailing slash preserves the /parabank/services/bank prefix for relative paths.
    const ctx = await request.newContext({
      baseURL: `${URLS.parabank}/services/bank/`,
      ignoreHTTPSErrors: IGNORE_HTTPS_ERRORS,
    });
    await use(ctx);
    await ctx.dispose();
  },
  parabankUser: async ({ page, parabankRequest }, use) => {
    // Register a brand-new customer (unique per run); this also logs the browser
    // in, so a test can drive the UI immediately. Resolve its id via the API.
    const customer = newCustomer();
    await new ParabankSteps(page).register(customer);
    const info = await new ParabankApiClient(parabankRequest).login(
      customer.username,
      customer.password,
    );
    customer.customerId = info.id;
    await use(customer);
  },
});

export { expect };
