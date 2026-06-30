import { test, expect } from '../../../src/fixtures';
import { BOOKER_ADMIN } from '../../../src/config';
import { Booking } from '../../../src/api/BookerClient';

const BOOKING: Booking = {
  firstname: 'Alan',
  lastname: 'Turing',
  totalprice: 200,
  depositpaid: true,
  bookingdates: { checkin: '2025-06-01', checkout: '2025-06-10' },
  additionalneeds: 'Late checkout',
};

test('booking CRUD lifecycle @api', async ({ booker }) => {
  const create = await booker.createBooking(BOOKING);
  expect(create.status()).toBe(200);
  const created = await create.json();
  const id = created.bookingid;
  expect(created.booking.firstname).toBe('Alan');

  const read = await booker.getBooking(id);
  expect((await read.json()).lastname).toBe('Turing');

  await booker.auth(BOOKER_ADMIN.username, BOOKER_ADMIN.password);
  const put = await booker.updateBooking(id, { ...BOOKING, firstname: 'Alonzo' });
  expect(put.status()).toBe(200);
  expect((await put.json()).firstname).toBe('Alonzo');

  const del = await booker.deleteBooking(id);
  expect(del.status()).toBe(201);
  expect((await booker.getBooking(id)).status()).toBe(404);
});
