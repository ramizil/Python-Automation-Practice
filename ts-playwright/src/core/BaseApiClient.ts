// Layer 1 — a product-agnostic base API client.
//
// The equivalent of a Java HTTP/login *interceptor*: cross-cutting concerns
// (auth header injection + request/response logging) live in ONE place — the
// `call()` method. Every product client (BookerApiClient, a future
// BillingApiClient, ...) extends this and inherits that behaviour.
import { APIRequestContext, APIResponse } from '@playwright/test';
import { getLogger, Logger } from './logger';

export class BaseApiClient {
  protected request: APIRequestContext;
  protected log: Logger;
  private token: string | null = null;

  constructor(request: APIRequestContext, name = 'BaseApiClient') {
    this.request = request;
    this.log = getLogger(name);
  }

  setToken(token: string): void {
    this.token = token;
  }

  private headers(extra?: Record<string, string>): Record<string, string> {
    const headers: Record<string, string> = {
      Accept: 'application/json',
      'Content-Type': 'application/json',
    };
    if (this.token) headers.Cookie = `token=${this.token}`;
    return { ...headers, ...extra };
  }

  protected async call(
    method: string,
    path: string,
    opts: { data?: unknown; headers?: Record<string, string> } = {},
  ): Promise<APIResponse> {
    this.log.info(`>>> ${method.toUpperCase()} ${path}`);
    const resp = await this.request.fetch(path, {
      method,
      data: opts.data as never,
      headers: this.headers(opts.headers),
    });
    this.log.info(`<<< ${method.toUpperCase()} ${path} -> ${resp.status()}`);
    return resp;
  }
}
