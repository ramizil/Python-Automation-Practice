import { test, expect } from '../../src/fixtures';
import { SAUCE_USERS, SAUCE_PASSWORD } from '../../src/config';

test('locked out user sees error @ui', async ({ page }) => {
  // TODO: go to '/', log in as the locked out user,
  //       assert the error banner contains 'locked out'.
  throw new Error('TODO: implement, then delete this line');
});

test('empty credentials show required error @ui', async ({ page }) => {
  // TODO: go to '/', click #login-button with empty fields,
  //       assert the error contains 'Username is required'.
  throw new Error('TODO: implement, then delete this line');
});
