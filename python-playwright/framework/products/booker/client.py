"""Layer 2 — restful-booker API client, built on the Layer-1 ``BaseApiClient``.

Notice this class only declares *endpoints*. Auth-header injection and
request/response logging are inherited from ``BaseApiClient`` (the interceptor),
so they aren't repeated here — exactly the cross-product reuse the layering buys.
"""

from __future__ import annotations

from typing import Any

from playwright.sync_api import APIResponse

from framework.core import BaseApiClient


class BookerApiClient(BaseApiClient):
    def ping(self) -> APIResponse:
        return self.call("GET", "/ping")

    def auth(self, username: str, password: str) -> str:
        resp = self.call("POST", "/auth", data={"username": username, "password": password})
        token: str = resp.json()["token"]
        self.set_token(token)  # inherited: now injected on every later call
        return token

    def create(self, booking: dict[str, Any]) -> APIResponse:
        return self.call("POST", "/booking", data=booking)

    def get(self, booking_id: int) -> APIResponse:
        return self.call("GET", f"/booking/{booking_id}")

    def delete(self, booking_id: int) -> APIResponse:
        return self.call("DELETE", f"/booking/{booking_id}")
