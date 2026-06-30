// Topic 3 (worked example): login via the LoginPage page object + fixture.
//   npx playwright test tests/ui/pom-login.spec.ts
import { test, expect } from '../../src/fixtures';
import { SAUCE_USERS, SAUCE_PASSWORD } from '../../src/config';

test.describe('Login via Page Object @ui', () => {
  test('standard user reaches inventory', async ({ loginPage, page }) => {
    await loginPage.open();
    await loginPage.login(SAUCE_USERS.standard, SAUCE_PASSWORD);
    await expect(page.locator('.title')).toHaveText('Products');
  });

  test('locked out user sees error', async ({ loginPage }) => {
    await loginPage.open();
    await loginPage.login(SAUCE_USERS.lockedOut, SAUCE_PASSWORD);
    await expect(loginPage.errorMessage).toContainText('locked out');
  });
});
