import { test, expect } from '../../src/fixtures';
import { PRODUCTS_APP_HTML, PRODUCTS_URL_GLOB } from '../../src/mockApp';

test('stub two products @ui', async ({ page }) => {
  // TODO 1: page.route(PRODUCTS_URL_GLOB, ...) -> fulfill 2 fake products
  //         (include headers: { 'Access-Control-Allow-Origin': '*' })
  // TODO 2: await page.setContent(PRODUCTS_APP_HTML); click '#load'
  // TODO 3: assert '.product' has count 2 with your titles
  expect(true, 'TODO: implement, then delete this line').toBe(false);
});

test('error state @ui', async ({ page }) => {
  // TODO: route to { status: 500 } (or route.abort()), load, and assert
  //       '#error' is visible and '.product' count is 0
  expect(true, 'TODO: implement, then delete this line').toBe(false);
});
