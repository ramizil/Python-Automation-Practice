// Layer 2 — restful-booker API client, built on the Layer-1 BaseApiClient.
// Only endpoints are declared here; auth injection + logging are inherited.
import { APIRequestContext, APIResponse } from '@playwright/test';
import { BaseApiClient } from '../../core/BaseApiClient';
import { Booking } from '../../api/BookerClient';

export class BookerApiClient extends BaseApiClient {
  constructor(request: APIRequestContext) {
    super(request, 'BookerApiClient');
  }

  ping(): Promise<APIResponse> {
    return this.call('GET', '/ping');
  }

  async auth(username: string, password: string): Promise<string> {
    const resp = await this.call('POST', '/auth', { data: { username, password } });
    const token = (await resp.json()).token as string;
    this.setToken(token); // inherited: injected on every later call
    return token;
  }

  create(booking: Booking): Promise<APIResponse> {
    return this.call('POST', '/booking', { data: booking });
  }

  get(id: number): Promise<APIResponse> {
    return this.call('GET', `/booking/${id}`);
  }

  delete(id: number): Promise<APIResponse> {
    return this.call('DELETE', `/booking/${id}`);
  }
}
