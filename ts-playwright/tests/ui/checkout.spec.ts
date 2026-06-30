// Topic 4 (worked example): full end-to-end checkout with page objects.
//   npx playwright test tests/ui/checkout.spec.ts
import { test, expect } from '../../src/fixtures';
import { SAUCE_USERS, SAUCE_PASSWORD } from '../../src/config';

const ITEM = 'Sauce Labs Backpack';

test('buy one item end-to-end @ui', async ({
  loginPage,
  inventoryPage,
  cartPage,
  checkoutPage,
}) => {
  await loginPage.open();
  await loginPage.login(SAUCE_USERS.standard, SAUCE_PASSWORD);

  await inventoryPage.addItemToCart(ITEM);
  expect(await inventoryPage.cartCount()).toBe(1);
  await inventoryPage.goToCart();

  expect(await cartPage.itemNames()).toContain(ITEM);
  await cartPage.checkout();

  await checkoutPage.fillInformation('Ada', 'Lovelace', '12345');
  await checkoutPage.finish();
  await expect(checkoutPage.completeHeader).toHaveText('Thank you for your order!');
});
