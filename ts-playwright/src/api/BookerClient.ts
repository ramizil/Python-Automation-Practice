import { APIRequestContext, APIResponse } from '@playwright/test';

export interface Booking {
  firstname: string;
  lastname: string;
  totalprice: number;
  depositpaid: boolean;
  bookingdates: { checkin: string; checkout: string };
  additionalneeds?: string;
}

/**
 * Thin client for the restful-booker API.
 * Quirks: POST /auth returns a token (sent as a cookie for update/delete);
 * DELETE returns 201 on success.
 */
export class BookerClient {
  private request: APIRequestContext;
  private token: string | null = null;

  constructor(request: APIRequestContext) {
    this.request = request;
  }

  async auth(username: string, password: string): Promise<string> {
    const resp = await this.request.post('/auth', { data: { username, password } });
    if (!resp.ok()) throw new Error(`auth failed: ${resp.status()} ${await resp.text()}`);
    this.token = (await resp.json()).token;
    return this.token!;
  }

  private authHeaders(): Record<string, string> {
    if (!this.token) throw new Error('Call auth() before update/delete.');
    return {
      Cookie: `token=${this.token}`,
      'Content-Type': 'application/json',
      Accept: 'application/json',
    };
  }

  createBooking(booking: Booking): Promise<APIResponse> {
    return this.request.post('/booking', {
      data: booking,
      headers: { 'Content-Type': 'application/json', Accept: 'application/json' },
    });
  }

  getBooking(id: number): Promise<APIResponse> {
    return this.request.get(`/booking/${id}`, { headers: { Accept: 'application/json' } });
  }

  updateBooking(id: number, booking: Booking): Promise<APIResponse> {
    return this.request.put(`/booking/${id}`, { data: booking, headers: this.authHeaders() });
  }

  deleteBooking(id: number): Promise<APIResponse> {
    return this.request.delete(`/booking/${id}`, { headers: this.authHeaders() });
  }
}
