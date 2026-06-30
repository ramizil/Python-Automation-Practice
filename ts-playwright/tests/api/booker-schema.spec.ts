// Topic 7 (worked example): API schema / contract validation with Ajv.
//   npx playwright test tests/api/booker-schema.spec.ts
import { test, expect } from '../../src/fixtures';
import { Booking } from '../../src/api/BookerClient';
import { bookingSchema, bookingIdListSchema, validateOrThrow } from '../../src/schemas/booking';

const NEW_BOOKING: Booking = {
  firstname: 'Grace',
  lastname: 'Hopper',
  totalprice: 150,
  depositpaid: true,
  bookingdates: { checkin: '2025-01-01', checkout: '2025-01-05' },
  additionalneeds: 'Breakfast',
};

test.describe('restful-booker schema @api', () => {
  test('created booking matches the schema', async ({ booker }) => {
    const id = (await (await booker.createBooking(NEW_BOOKING)).json()).bookingid;
    const body = await (await booker.getBooking(id)).json();
    // Throws (failing the test) if the shape is wrong.
    expect(validateOrThrow(bookingSchema, body)).toBe(true);
  });

  test('booking list matches the schema', async ({ bookerRequest }) => {
    const body = await (await bookerRequest.get('/booking', {
      headers: { Accept: 'application/json' },
    })).json();
    expect(validateOrThrow(bookingIdListSchema, body)).toBe(true);
  });

  test('schema rejects a bad shape', async () => {
    // totalprice as a string + missing lastname must fail validation.
    const broken: Record<string, unknown> = { ...NEW_BOOKING, totalprice: '150' };
    delete broken.lastname;
    expect(() => validateOrThrow(bookingSchema, broken)).toThrow();
  });
});
