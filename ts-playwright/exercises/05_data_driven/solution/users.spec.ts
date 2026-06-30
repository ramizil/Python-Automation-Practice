import { test, expect } from '../../../src/fixtures';
import { SAUCE_USERS, SAUCE_PASSWORD } from '../../../src/config';

const cases = [
  { user: SAUCE_USERS.standard, canLogin: true },
  { user: SAUCE_USERS.problem, canLogin: true },
  { user: SAUCE_USERS.performanceGlitch, canLogin: true },
  { user: SAUCE_USERS.lockedOut, canLogin: false },
];

for (const { user, canLogin } of cases) {
  test(`login outcome for ${user} @ui`, async ({ loginPage, page }) => {
    await loginPage.open();
    await loginPage.login(user, SAUCE_PASSWORD);

    if (canLogin) {
      await expect(page.locator('.title')).toHaveText('Products');
    } else {
      await expect(loginPage.errorMessage).toContainText('locked out');
    }
  });
}
