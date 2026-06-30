import { test, expect } from '../../../src/fixtures';
import { SAUCE_USERS, SAUCE_PASSWORD } from '../../../src/config';

test('locked out user sees error @ui', async ({ page }) => {
  await page.goto('/');
  await page.locator('#user-name').fill(SAUCE_USERS.lockedOut);
  await page.locator('#password').fill(SAUCE_PASSWORD);
  await page.locator('#login-button').click();
  await expect(page.locator('[data-test="error"]')).toContainText('locked out');
});

test('empty credentials show required error @ui', async ({ page }) => {
  await page.goto('/');
  await page.locator('#login-button').click();
  await expect(page.locator('[data-test="error"]')).toContainText('Username is required');
});
