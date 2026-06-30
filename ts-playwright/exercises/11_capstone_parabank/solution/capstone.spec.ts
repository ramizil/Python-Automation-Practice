import { test, expect } from '../../../src/fixtures';
import { ParabankSteps } from '../../../src/products/parabank/steps';
import { ParabankApiClient } from '../../../src/products/parabank/ParabankApiClient';

test('parabank capstone @capstone @slow', async ({ page, parabankUser, parabankRequest }) => {
  const steps = new ParabankSteps(page);
  const api = new ParabankApiClient(parabankRequest);
  const customerId = parabankUser.customerId!;

  const start = await api.accounts(customerId);
  expect(start.length).toBeGreaterThanOrEqual(1);

  const newId = await steps.openSavingsAccount();

  const after = await api.accounts(customerId);
  expect(after.length).toBe(start.length + 1);
  expect(after.some((a) => String(a.id) === newId)).toBeTruthy();
  expect((await api.account(Number(newId))).type).toBe('SAVINGS');

  const confirmation = await steps.transfer(25, newId);
  expect(confirmation).toContain('Transfer Complete!');

  expect((await api.transactions(Number(newId))).length).toBeGreaterThanOrEqual(1);
});
