// Topic 6 (worked example): API testing basics against restful-booker.
//   npx playwright test tests/api/booker.spec.ts
import { test, expect } from '../../src/fixtures';
import { BOOKER_ADMIN } from '../../src/config';
import { Booking } from '../../src/api/BookerClient';

const NEW_BOOKING: Booking = {
  firstname: 'Grace',
  lastname: 'Hopper',
  totalprice: 150,
  depositpaid: true,
  bookingdates: { checkin: '2025-01-01', checkout: '2025-01-05' },
  additionalneeds: 'Breakfast',
};

test.describe('restful-booker @api', () => {
  test('health check (/ping returns 201)', async ({ bookerRequest }) => {
    const resp = await bookerRequest.get('/ping');
    expect(resp.status()).toBe(201);
  });

  test('create and read a booking', async ({ booker }) => {
    const create = await booker.createBooking(NEW_BOOKING);
    expect(create.status()).toBe(200);
    const body = await create.json();
    expect(body.booking.firstname).toBe('Grace');

    const read = await booker.getBooking(body.bookingid);
    expect(read.status()).toBe(200);
    expect((await read.json()).lastname).toBe('Hopper');
  });

  test('update requires auth then succeeds', async ({ booker }) => {
    const create = await booker.createBooking(NEW_BOOKING);
    const id = (await create.json()).bookingid;

    await booker.auth(BOOKER_ADMIN.username, BOOKER_ADMIN.password);
    const updated: Booking = { ...NEW_BOOKING, firstname: 'Ada', totalprice: 999 };
    const resp = await booker.updateBooking(id, updated);
    expect(resp.status()).toBe(200);
    const json = await resp.json();
    expect(json.firstname).toBe('Ada');
    expect(json.totalprice).toBe(999);
  });

  test('delete a booking', async ({ booker }) => {
    const create = await booker.createBooking(NEW_BOOKING);
    const id = (await create.json()).bookingid;
    await booker.auth(BOOKER_ADMIN.username, BOOKER_ADMIN.password);

    const del = await booker.deleteBooking(id);
    expect(del.status()).toBe(201); // restful-booker returns 201 on delete

    const read = await booker.getBooking(id);
    expect(read.status()).toBe(404);
  });
});
