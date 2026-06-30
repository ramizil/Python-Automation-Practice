import { test, expect } from '../../../src/fixtures';
import { SAUCE_USERS, SAUCE_PASSWORD } from '../../../src/config';

const ITEMS = ['Sauce Labs Backpack', 'Sauce Labs Bike Light'];

test('buy two items @ui', async ({ loginPage, inventoryPage, cartPage, checkoutPage }) => {
  await loginPage.open();
  await loginPage.login(SAUCE_USERS.standard, SAUCE_PASSWORD);

  for (const item of ITEMS) await inventoryPage.addItemToCart(item);
  expect(await inventoryPage.cartCount()).toBe(2);
  await inventoryPage.goToCart();

  const names = await cartPage.itemNames();
  for (const item of ITEMS) expect(names).toContain(item);
  await cartPage.checkout();

  await checkoutPage.fillInformation('Ada', 'Lovelace', '12345');
  await checkoutPage.finish();
  await expect(checkoutPage.completeHeader).toHaveText('Thank you for your order!');
});
