// Topic 12 (worked example): layered framework architecture — UI.
//   npx playwright test tests/ui/layered-architecture.spec.ts
//
// Compare with tests/ui/checkout.spec.ts (topic 4): same flow, but here the test
// only speaks the business language (loginAs, addItemsToCart, checkout). The
// page-object mechanics live in the Layer-2 SauceDemoSteps.
import { test, expect } from '../../src/fixtures';
import { SauceDemoSteps } from '../../src/products/saucedemo/steps';

test('checkout two items via steps @ui', async ({ page }) => {
  const steps = new SauceDemoSteps(page);

  await steps.loginAs('standard');
  await steps.addItemsToCart(['Sauce Labs Backpack', 'Sauce Labs Bike Light']);
  const confirmation = await steps.checkout('Ada', 'Lovelace', '12345');

  expect(confirmation).toBe('Thank you for your order!');
});
