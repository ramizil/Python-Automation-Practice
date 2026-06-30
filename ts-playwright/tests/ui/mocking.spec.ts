// Topic 8 (worked example): network mocking & interception.
//   npx playwright test tests/ui/mocking.spec.ts
//
// page.route(urlGlob, handler) intercepts every matching request. The handler
// chooses the outcome:
//   route.fulfill(...) -> answer with YOUR response (stub the backend)
//   route.abort()      -> simulate a network failure
//   route.fetch()      -> get the REAL response so you can tweak it, then fulfill
import { test, expect } from '../../src/fixtures';
import { PRODUCTS_APP_HTML, PRODUCTS_URL_GLOB } from '../../src/mockApp';

const CORS = { 'Access-Control-Allow-Origin': '*' };

function fakeProducts(...titles: string[]) {
  return { products: titles.map((title, i) => ({ id: i + 1, title })) };
}

test.describe('network mocking @ui', () => {
  test('stub returns two products', async ({ page }) => {
    await page.route(PRODUCTS_URL_GLOB, (route) =>
      route.fulfill({ json: fakeProducts('Mock Widget', 'Mock Gadget'), headers: CORS }),
    );
    await page.setContent(PRODUCTS_APP_HTML);
    await page.locator('#load').click();

    await expect(page.locator('.product')).toHaveCount(2);
    await expect(page.locator('.product')).toHaveText(['Mock Widget', 'Mock Gadget']);
  });

  test('server error shows the error state', async ({ page }) => {
    await page.route(PRODUCTS_URL_GLOB, (route) => route.fulfill({ status: 500, headers: CORS }));
    await page.setContent(PRODUCTS_APP_HTML);
    await page.locator('#load').click();

    await expect(page.locator('#error')).toBeVisible();
    await expect(page.locator('.product')).toHaveCount(0);
  });

  test('aborted request shows the error state', async ({ page }) => {
    await page.route(PRODUCTS_URL_GLOB, (route) => route.abort());
    await page.setContent(PRODUCTS_APP_HTML);
    await page.locator('#load').click();

    await expect(page.locator('#error')).toBeVisible();
  });

  test('modify the real response', async ({ page }) => {
    await page.route(PRODUCTS_URL_GLOB, async (route) => {
      const original = await (await route.fetch()).json();
      original.products.unshift({ id: 999, title: 'INJECTED' });
      await route.fulfill({ json: original, headers: CORS });
    });
    await page.setContent(PRODUCTS_APP_HTML);
    await page.locator('#load').click();

    await expect(page.locator('.product').first()).toHaveText('INJECTED');
  });
});
