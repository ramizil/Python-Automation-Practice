// Topic 12 (worked example): layered framework architecture — API.
//   npx playwright test tests/api/layered-steps.spec.ts
//
// Layer 1: BaseApiClient (auth + logging interceptor) — product-agnostic.
// Layer 2: BookerApiClient (endpoints) + BookerSteps (workflows).
// Layer 3: this test — only business steps + assertions.
import { test, expect } from '../../src/fixtures';
import { BOOKER_ADMIN } from '../../src/config';
import { BookerApiClient } from '../../src/products/booker/BookerApiClient';
import { BookerSteps } from '../../src/products/booker/steps';

test('booking lifecycle via steps @api', async ({ bookerRequest }) => {
  const client = new BookerApiClient(bookerRequest); // Layer 2 client on Layer 1 infra
  const steps = new BookerSteps(client); // Layer 2 workflows

  const id = await steps.createPaidBooking('Grace', 'Hopper');
  expect((await client.get(id)).status()).toBe(200);

  await steps.cancelBooking(id, BOOKER_ADMIN);
  expect((await client.get(id)).status()).toBe(404);
});
