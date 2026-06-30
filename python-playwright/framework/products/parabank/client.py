"""Parabank REST client, built on the Layer-1 ``BaseApiClient``.

The request context is based at ``<PARABANK_URL>/services/bank/`` (trailing
slash) — see the ``parabank_request`` fixture — so paths here are relative and
carry NO leading slash, otherwise they'd resolve against the host root and drop
the ``/parabank/services/bank`` prefix. Parabank returns JSON when
``Accept: application/json`` is sent, which ``BaseApiClient`` already does.
"""

from __future__ import annotations

from typing import Any

from framework.core import BaseApiClient


class ParabankApiClient(BaseApiClient):
    def login(self, username: str, password: str) -> dict[str, Any]:
        """Return the customer record for these credentials (incl. its ``id``)."""
        resp = self.call("GET", f"login/{username}/{password}")
        data: dict[str, Any] = resp.json()
        return data

    def accounts(self, customer_id: int) -> list[dict[str, Any]]:
        resp = self.call("GET", f"customers/{customer_id}/accounts")
        data: list[dict[str, Any]] = resp.json()
        return data

    def account(self, account_id: int) -> dict[str, Any]:
        resp = self.call("GET", f"accounts/{account_id}")
        data: dict[str, Any] = resp.json()
        return data

    def transactions(self, account_id: int) -> list[dict[str, Any]]:
        resp = self.call("GET", f"accounts/{account_id}/transactions")
        data: list[dict[str, Any]] = resp.json()
        return data
