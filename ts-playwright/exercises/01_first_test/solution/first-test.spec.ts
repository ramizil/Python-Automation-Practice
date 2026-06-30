import { test, expect } from '../../../src/fixtures';

test('SauceDemo loads @ui', async ({ page }) => {
  await page.goto('/');
  await expect(page).toHaveTitle('Swag Labs');
  await expect(page.locator('#login-button')).toBeVisible();
});
