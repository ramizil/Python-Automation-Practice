import { test, expect } from '../../src/fixtures';
import { SAUCE_USERS, SAUCE_PASSWORD } from '../../src/config';

// TODO: build a cases array of { user, canLogin } for all four users
const cases: { user: string; canLogin: boolean }[] = [];

if (cases.length === 0) {
  test('implement me @ui', async () => {
    throw new Error('TODO: fill the cases array and the loop below, then delete this test');
  });
}

for (const { user, canLogin } of cases) {
  test(`login outcome for ${user} @ui`, async ({ loginPage, page }) => {
    // TODO: open + login with `user`; assert based on `canLogin`
    throw new Error('TODO: implement');
  });
}
