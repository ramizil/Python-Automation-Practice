// Topic 11 (capstone, worked example): Parabank end-to-end, UI + API combined.
//
// Pulls together the layered architecture (BaseApiClient -> ParabankApiClient +
// ParabankSteps), a unique-user-per-run fixture, and the hybrid pattern
// (topic 09): drive an action via the UI, verify it via the API.
//
// Parabank is a public demo bank (sometimes slow/reset), so this is tagged
// @capstone/@slow and excluded from the fast/CI run:
//   npx playwright test tests/capstone
import { test, expect } from '../../src/fixtures';
import { ParabankSteps } from '../../src/products/parabank/steps';
import { ParabankApiClient } from '../../src/products/parabank/ParabankApiClient';

test('open account and transfer end-to-end @capstone @slow', async ({
  page,
  parabankUser,
  parabankRequest,
}) => {
  const steps = new ParabankSteps(page);
  const api = new ParabankApiClient(parabankRequest);
  const customerId = parabankUser.customerId!;

  // Starting state via API — a fresh user has one CHECKING account.
  const start = await api.accounts(customerId);
  expect(start.length).toBeGreaterThanOrEqual(1);

  // Drive the UI: open a new savings account.
  const newId = await steps.openSavingsAccount();

  // Verify by API (hybrid): the new account exists and is a SAVINGS account.
  const after = await api.accounts(customerId);
  expect(after.length).toBe(start.length + 1);
  expect(after.some((a) => String(a.id) === newId)).toBeTruthy();
  expect((await api.account(Number(newId))).type).toBe('SAVINGS');

  // Drive the UI: transfer funds into the new account.
  const confirmation = await steps.transfer(25, newId);
  expect(confirmation).toContain('Transfer Complete!');

  // Verify by API (hybrid): the transfer produced a transaction.
  expect((await api.transactions(Number(newId))).length).toBeGreaterThanOrEqual(1);
});
