// Topics 1-2 (worked examples): first test, locators & web-first assertions.
//   npx playwright test tests/ui/login.spec.ts
import { test, expect } from '../../src/fixtures';
import { SAUCE_USERS, SAUCE_PASSWORD } from '../../src/config';

test.describe('SauceDemo login @ui', () => {
  test('login page loads', async ({ page }) => {
    await page.goto('/');
    await expect(page).toHaveTitle('Swag Labs');
    await expect(page.locator('#login-button')).toBeVisible();
  });

  test('successful login shows inventory', async ({ page, baseURL }) => {
    await page.goto('/');
    await page.locator('#user-name').fill(SAUCE_USERS.standard);
    await page.locator('#password').fill(SAUCE_PASSWORD);
    await page.locator('#login-button').click();

    await expect(page).toHaveURL(`${baseURL}/inventory.html`);
    await expect(page.locator('.title')).toHaveText('Products');
  });

  test('bad credentials show an error', async ({ page }) => {
    await page.goto('/');
    await page.locator('#user-name').fill('nope');
    await page.locator('#password').fill('wrong');
    await page.locator('#login-button').click();

    const error = page.locator('[data-test="error"]');
    await expect(error).toBeVisible();
    await expect(error).toContainText('Username and password do not match');
  });
});
