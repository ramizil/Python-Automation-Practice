import { test, expect } from '../../src/fixtures';
import { Booking } from '../../src/api/BookerClient';
import { bookingSchema, bookingIdListSchema, validateOrThrow } from '../../src/schemas/booking';

const BOOKING: Booking = {
  firstname: 'Ada',
  lastname: 'Lovelace',
  totalprice: 175,
  depositpaid: true,
  bookingdates: { checkin: '2025-03-01', checkout: '2025-03-04' },
  additionalneeds: 'Breakfast',
};

test('booking response matches the contract @api', async ({ booker, bookerRequest }) => {
  // TODO 1: create BOOKING, getBooking(id), validate body against bookingSchema
  // TODO 2: GET /booking (list) via bookerRequest, validate vs bookingIdListSchema
  // TODO 3: build a broken booking (totalprice="175" or drop lastname) and
  //         expect(() => validateOrThrow(bookingSchema, broken)).toThrow()
  expect(true, 'TODO: implement the steps above, then delete this line').toBe(false);
});
