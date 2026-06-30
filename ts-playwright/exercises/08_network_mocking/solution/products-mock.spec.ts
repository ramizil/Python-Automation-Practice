import { test, expect } from '../../../src/fixtures';
import { PRODUCTS_APP_HTML, PRODUCTS_URL_GLOB } from '../../../src/mockApp';

const CORS = { 'Access-Control-Allow-Origin': '*' };

test('stub two products @ui', async ({ page }) => {
  const fake = { products: [{ id: 1, title: 'Alpha' }, { id: 2, title: 'Beta' }] };
  await page.route(PRODUCTS_URL_GLOB, (route) => route.fulfill({ json: fake, headers: CORS }));
  await page.setContent(PRODUCTS_APP_HTML);
  await page.locator('#load').click();

  await expect(page.locator('.product')).toHaveCount(2);
  await expect(page.locator('.product')).toHaveText(['Alpha', 'Beta']);
});

test('error state @ui', async ({ page }) => {
  await page.route(PRODUCTS_URL_GLOB, (route) => route.fulfill({ status: 500, headers: CORS }));
  await page.setContent(PRODUCTS_APP_HTML);
  await page.locator('#load').click();

  await expect(page.locator('#error')).toBeVisible();
  await expect(page.locator('.product')).toHaveCount(0);
});
