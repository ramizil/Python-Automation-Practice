import { test, expect } from '../../src/fixtures';
import { ParabankSteps } from '../../src/products/parabank/steps';
import { ParabankApiClient } from '../../src/products/parabank/ParabankApiClient';

test('parabank capstone @capstone @slow', async ({ page, parabankUser, parabankRequest }) => {
  const steps = new ParabankSteps(page);
  const api = new ParabankApiClient(parabankRequest);
  const customerId = parabankUser.customerId!;

  // TODO 1: read starting accounts via API (api.accounts(customerId)); assert >= 1
  // TODO 2: open a savings account via the UI -> steps.openSavingsAccount()
  // TODO 3: verify by API the new account exists and its type === 'SAVINGS'
  // TODO 4: transfer 25 into it via UI; expect 'Transfer Complete!'
  // TODO 5: verify by API there is >= 1 transaction on the new account
  expect(true, 'TODO: implement the capstone flow, then delete this line').toBe(false);
});
