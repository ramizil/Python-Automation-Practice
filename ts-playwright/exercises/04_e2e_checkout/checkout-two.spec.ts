import { test, expect } from '../../src/fixtures';
import { SAUCE_USERS, SAUCE_PASSWORD } from '../../src/config';

const ITEMS = ['Sauce Labs Backpack', 'Sauce Labs Bike Light'];

test('buy two items @ui', async ({ loginPage, inventoryPage, cartPage, checkoutPage }) => {
  // TODO 1: log in as the standard user
  // TODO 2: add both ITEMS, assert cartCount() === 2
  // TODO 3: go to cart, assert both names present
  // TODO 4: checkout -> fillInformation -> finish
  // TODO 5: assert completeHeader 'Thank you for your order!'
  throw new Error('TODO: implement, then delete this line');
});
