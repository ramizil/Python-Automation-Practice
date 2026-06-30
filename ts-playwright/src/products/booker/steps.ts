// Layer 2 — restful-booker business steps (workflows a test cares about).
import { BookerApiClient } from './BookerApiClient';

export class BookerSteps {
  constructor(private client: BookerApiClient) {}

  async createPaidBooking(firstname: string, lastname: string, total = 150): Promise<number> {
    const resp = await this.client.create({
      firstname,
      lastname,
      totalprice: total,
      depositpaid: true,
      bookingdates: { checkin: '2025-01-01', checkout: '2025-01-05' },
      additionalneeds: 'Breakfast',
    });
    return (await resp.json()).bookingid as number;
  }

  async cancelBooking(id: number, admin: { username: string; password: string }): Promise<void> {
    // Cancelling needs auth — the client handles token injection for us.
    await this.client.auth(admin.username, admin.password);
    await this.client.delete(id);
  }
}
