// Parabank REST client, built on the Layer-1 BaseApiClient.
//
// The request context is based at `<PARABANK_URL>/services/bank/` (trailing
// slash) — see the parabankRequest fixture — so paths here are relative and
// carry NO leading slash, otherwise they'd resolve against the host root and
// drop the /parabank/services/bank prefix.
import { BaseApiClient } from '../../core/BaseApiClient';

export interface ParabankAccount {
  id: number;
  customerId: number;
  type: string;
  balance: number;
}

export class ParabankApiClient extends BaseApiClient {
  async login(username: string, password: string): Promise<{ id: number; [k: string]: unknown }> {
    const resp = await this.call('GET', `login/${username}/${password}`);
    return resp.json();
  }

  async accounts(customerId: number): Promise<ParabankAccount[]> {
    const resp = await this.call('GET', `customers/${customerId}/accounts`);
    return resp.json();
  }

  async account(accountId: number): Promise<ParabankAccount> {
    const resp = await this.call('GET', `accounts/${accountId}`);
    return resp.json();
  }

  async transactions(accountId: number): Promise<Array<Record<string, unknown>>> {
    const resp = await this.call('GET', `accounts/${accountId}/transactions`);
    return resp.json();
  }
}
