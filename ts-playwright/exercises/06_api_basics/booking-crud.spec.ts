import { test, expect } from '../../src/fixtures';
import { BOOKER_ADMIN } from '../../src/config';
import { Booking } from '../../src/api/BookerClient';

const BOOKING: Booking = {
  firstname: 'Alan',
  lastname: 'Turing',
  totalprice: 200,
  depositpaid: true,
  bookingdates: { checkin: '2025-06-01', checkout: '2025-06-10' },
  additionalneeds: 'Late checkout',
};

test('booking CRUD lifecycle @api', async ({ booker }) => {
  // TODO 1: create BOOKING, assert 200 + firstname echoed back
  // TODO 2: GET it back, assert lastname === 'Turing'
  // TODO 3: auth as admin, update (firstname -> 'Alonzo'), assert it
  // TODO 4: delete (expect 201), then GET should be 404
  throw new Error('TODO: implement, then delete this line');
});
