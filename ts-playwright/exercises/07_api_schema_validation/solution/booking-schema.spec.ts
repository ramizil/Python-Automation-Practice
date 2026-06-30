import { test, expect } from '../../../src/fixtures';
import { Booking } from '../../../src/api/BookerClient';
import {
  bookingSchema,
  bookingIdListSchema,
  validateOrThrow,
} from '../../../src/schemas/booking';

const BOOKING: Booking = {
  firstname: 'Ada',
  lastname: 'Lovelace',
  totalprice: 175,
  depositpaid: true,
  bookingdates: { checkin: '2025-03-01', checkout: '2025-03-04' },
  additionalneeds: 'Breakfast',
};

test('booking response matches the contract @api', async ({ booker, bookerRequest }) => {
  const id = (await (await booker.createBooking(BOOKING)).json()).bookingid;
  const body = await (await booker.getBooking(id)).json();
  expect(validateOrThrow(bookingSchema, body)).toBe(true);

  const listing = await (await bookerRequest.get('/booking', {
    headers: { Accept: 'application/json' },
  })).json();
  expect(validateOrThrow(bookingIdListSchema, listing)).toBe(true);

  const broken: Record<string, unknown> = { ...BOOKING, totalprice: '175' };
  delete broken.lastname;
  expect(() => validateOrThrow(bookingSchema, broken)).toThrow();
});
